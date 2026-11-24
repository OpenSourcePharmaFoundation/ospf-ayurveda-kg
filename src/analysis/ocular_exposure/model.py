"""The model: uniform draws in, free-drug margins per compartment out.

Everything is written as a function of a matrix of uniform [0,1) variates with
one column per declared input, rather than as a function of random draws.  That
costs nothing for a plain Monte-Carlo (feed it ``rng.random``) and it is what
makes a Sobol decomposition possible at all: ``sensitivity.py`` has to be able
to swap one column between two sample matrices and re-evaluate.

The margin is

    margin = Cu(compartment) / EC50(free)

with the free fraction taken out of *both* sides.  A margin of 1 means the free
concentration in that compartment sits at the free EC50.  Below 1 the receptor
is under-occupied; the reciprocal is the fold shortfall.
"""

from __future__ import annotations

import dataclasses

import numpy as np

from . import barrier, binding, parameters, potency
from .compounds import REFERENCE, Compound

# Input order is the model's public contract: the Sobol indices are reported
# against these names and in this order.
INPUT_NAMES = [
    "anchor.retina_ffa",
    "anchor.plasma_ffa",
    "anchor.retina_protein_mg",
    "anchor.vitreous_vol_ul",
    "anchor.retina_vol_ul",
    "anchor.plasma_protein_mouse",
    "anchor.fu_plasma_mouse_ffa",
    "anchor.fu_tissue_retina",
    "anchor.late_sample_bias",
    "barrier.perm_logd_slope",
    "barrier.perm_mw_slope",
    "barrier.efflux_share",
    "barrier.efflux_rel",
    "barrier.endo_retention",
    "barrier.rpe_net",
    "assay.serum_fraction",
    "assay.fbs_albumin_ratio",
    "compound.c_plasma",
    "compound.fu_plasma",
    "compound.pka",
    "compound.ec50_nominal",
    "reference.pka",
    "compound.logp",
]
N_INPUTS = len(INPUT_NAMES)
IDX = {n: i for i, n in enumerate(INPUT_NAMES)}

COMPARTMENTS = ("endothelium", "rpe", "neural_retina")


@dataclasses.dataclass
class Result:
    compound: Compound
    gene: str
    exposure: str  # "c_avg" or "c_max"
    potency: potency.Potency
    margins: dict[str, np.ndarray]  # compartment -> margin draws
    kpuu_neural_retina: np.ndarray
    kpuu_reference: np.ndarray
    cu_plasma_nM: np.ndarray
    ec50_free_nM: np.ndarray
    ec50_nominal_nM: np.ndarray


def _anchor_draws(u: np.ndarray) -> dict[str, np.ndarray]:
    a = parameters.ANCHOR
    return {
        "retina_ffa": np.clip(
            a["retina_ffa"].ppf(u[:, IDX["anchor.retina_ffa"]]), 1e-4, None
        ),
        "plasma_ffa": np.clip(
            a["plasma_ffa"].ppf(u[:, IDX["anchor.plasma_ffa"]]), 1e-2, None
        ),
        "retina_protein_mg": a["retina_protein_mg"].ppf(
            u[:, IDX["anchor.retina_protein_mg"]]
        ),
        "vitreous_vol_ul": a["vitreous_vol_ul"].ppf(
            u[:, IDX["anchor.vitreous_vol_ul"]]
        ),
        "retina_vol_ul": a["retina_vol_ul"].ppf(u[:, IDX["anchor.retina_vol_ul"]]),
        "plasma_protein_mouse": a["plasma_protein_mouse"].ppf(
            u[:, IDX["anchor.plasma_protein_mouse"]]
        ),
        "fu_plasma_mouse_ffa": a["fu_plasma_mouse_ffa"].ppf(
            u[:, IDX["anchor.fu_plasma_mouse_ffa"]]
        ),
        "fu_tissue_retina": a["fu_tissue_retina"].ppf(
            u[:, IDX["anchor.fu_tissue_retina"]]
        ),
        "late_sample_bias": a["late_sample_bias"].ppf(
            u[:, IDX["anchor.late_sample_bias"]]
        ),
    }


def evaluate(
    u: np.ndarray, cmp: Compound, pot: potency.Potency, exposure: str = "c_avg"
) -> Result:
    """Run the model over a matrix of uniform variates."""
    u = np.asarray(u, dtype=float)
    if u.shape[1] != N_INPUTS:
        raise ValueError(f"expected {N_INPUTS} input columns, got {u.shape[1]}")

    B, A = parameters.BARRIER, parameters.ASSAY

    # 1. Neural-retina Kp,uu, calibrated on the mouse fenofibric-acid anchor.
    kpuu_ref = barrier.kpuu_neural_retina_reference(_anchor_draws(u))

    # 2. Transfer it to this compound on relative passive permeability and
    #    relative efflux liability.  The reference compound shares its pKa
    #    draw with itself, or the transfer would carry spurious variance.
    cmp_pka = cmp.pka.ppf(u[:, IDX["compound.pka"]])
    ref_pka = (
        cmp_pka
        if cmp.key == REFERENCE.key
        else REFERENCE.pka.ppf(u[:, IDX["reference.pka"]])
    )
    if cmp.key == REFERENCE.key:
        r_perm = np.ones_like(kpuu_ref)
        r_efflux = np.ones_like(kpuu_ref)
    else:
        # Only the logP *difference* from the reference drives the transfer, so
        # one error term on the difference is the right parameterisation -- two
        # independent ones would double-count a shared calculator bias.  Every
        # logP here is calculated (ChEMBL alogp); none of the four has a
        # published shake-flask value.
        cmp_logp = cmp.logp + parameters.LOGP_ERROR.ppf(u[:, IDX["compound.logp"]])
        r_perm = barrier.relative_permeability(
            cmp_logp,
            cmp_pka,
            cmp.mw,
            REFERENCE.logp,
            ref_pka,
            REFERENCE.mw,
            B["perm_logd_slope"].ppf(u[:, IDX["barrier.perm_logd_slope"]]),
            B["perm_mw_slope"].ppf(u[:, IDX["barrier.perm_mw_slope"]]),
        )
        r_efflux = B["efflux_rel"].ppf(u[:, IDX["barrier.efflux_rel"]])

    kpuu_nr = barrier.kpuu_transfer(
        kpuu_ref,
        r_perm,
        r_efflux,
        B["efflux_share"].ppf(u[:, IDX["barrier.efflux_share"]]),
    )

    ratios = barrier.compartment_ratios(
        kpuu_nr,
        B["endo_retention"].ppf(u[:, IDX["barrier.endo_retention"]]),
        B["rpe_net"].ppf(u[:, IDX["barrier.rpe_net"]]),
    )

    # 3. Free plasma concentration.
    c_param = cmp.c_avg if exposure == "c_avg" else cmp.c_max
    c_total_ng_ml = c_param.ppf(u[:, IDX["compound.c_plasma"]])
    fu_plasma = cmp.fu_plasma.ppf(u[:, IDX["compound.fu_plasma"]])
    cu_plasma_nM = c_total_ng_ml * 1000.0 / cmp.mw * fu_plasma

    # 4. Free EC50: undo the protein binding that was present in the assay.
    ec50_nom = pot.sample(u[:, IDX["compound.ec50_nominal"]])
    ec50_free = binding.free_ec50(
        ec50_nom,
        fu_plasma,
        A["serum_fraction"].ppf(u[:, IDX["assay.serum_fraction"]]),
        A["fbs_albumin_ratio"].ppf(u[:, IDX["assay.fbs_albumin_ratio"]]),
    )

    margins = {k: cu_plasma_nM * ratios[k] / ec50_free for k in COMPARTMENTS}
    return Result(
        cmp,
        pot.gene,
        exposure,
        pot,
        margins,
        kpuu_nr,
        kpuu_ref,
        cu_plasma_nM,
        ec50_free,
        ec50_nom,
    )


def run(
    cmp: Compound,
    pot: potency.Potency,
    n: int = 200_000,
    seed: int = 20261109,
    exposure: str = "c_avg",
) -> Result:
    rng = np.random.default_rng(seed)
    return evaluate(rng.random((n, N_INPUTS)), cmp, pot, exposure)


def quantiles(x: np.ndarray, qs=(2.5, 50, 97.5)) -> tuple[float, ...]:
    return tuple(float(v) for v in np.percentile(x, qs))
