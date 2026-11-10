"""Retinal-access filter, driven by the Step 5 exposure model.

The brief for this step says to filter on retinal-access physicochemistry
using the Step 5 model rather than ``alogp``, and the distinction is the whole
point.  ``alogp`` is the partition coefficient of the *neutral* species.  What
crosses a membrane is the neutral species' concentration, which for an acid at
pKa ~3 is six parts in 10^5 of the total at pH 7.4.  Ranking acids by logP
therefore overstates their permeability by four orders of magnitude, and the
fibrate programme is exactly where that error bites.

This module does three things:

1.  **Assign ionisation from structure**, because it cannot be looked up.
    ChEMBL's ChemAxon-derived ``cx_most_apka``, ``cx_logd`` and
    ``molecular_species`` are null for all 990 potent LXR ligands pulled here,
    the same gap Step 5 documented for the fibrates.  So the class comes from
    SMARTS on the canonical SMILES, and the pKa from the class.

2.  **Run the Step 5 barrier model** -- ``ocular_exposure.barrier`` and
    ``ocular_exposure.ionisation``, with Step 5's own declared parameter
    distributions -- to get a neural-retina Kp,uu for each candidate relative
    to the fenofibric-acid anchor Step 5 calibrated against Huang 2021.
    Nothing here re-derives a partition ratio; it transfers Step 5's.

3.  **Apply the window and record what it removed**, with a reason per
    compound, so the filter is auditable rather than a surviving list.

The headline result is a reversal.  Going neutral removes the four-log logD
penalty that caps the fibrates -- but the LXR chemotype pays for its neutral
pocket in lipophilicity (median alogp above 6), and a compound that lipophilic
is not a retinal-access win: it is bound, insoluble, and a P-glycoprotein
substrate.  The filter is therefore mostly rejecting candidates for *excess*
lipophilicity, which is the opposite failure from the one the fibrates have.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from rdkit import Chem, RDLogger

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analysis.ocular_exposure import barrier, ionisation, parameters  # noqa: E402
from src.analysis.ocular_exposure.compounds import FENOFIBRIC_ACID  # noqa: E402

RDLogger.DisableLog("rdApp.*")

ACID = "ACID"
BASE = "BASE"
NEUTRAL = "NEUTRAL"
ZWITTERION = "ZWITTERION"

# Acidic groups that are ionised at pH 7.4, with the representative pKa of the
# unsubstituted parent.  Same convention Step 5 used for the fibrate headgroup.
_ACIDIC = [
    ("carboxylic_acid", Chem.MolFromSmarts("[CX3](=O)[OX2H1,OX1-]"), 4.2),
    ("tetrazole", Chem.MolFromSmarts("c1nnn[nH]1"), 4.9),
    ("acyl_sulfonamide", Chem.MolFromSmarts("[SX4](=O)(=O)[NX3H1][CX3]=O"), 4.5),
    ("sulfonic_acid", Chem.MolFromSmarts("[SX4](=O)(=O)[OX2H1,OX1-]"), 1.0),
    ("phosphonic_acid", Chem.MolFromSmarts("[PX4](=O)([OX2H1,OX1-])"), 2.0),
]
# A basic nitrogen: sp3 N that is not an amide, aniline, sulfonamide or nitrile.
_BASIC = Chem.MolFromSmarts(
    "[NX3;!$(N[CX3]=[OX1,SX1]);!$(N[SX4](=O)=O);!$(Na);!$(N#*);!$([N+]);!$(N[CX3]=[NX2])]"
)
_PKA_BASE = 8.5
# A neutral molecule has no ionisable group; Step 5's Henderson-Hasselbalch is
# written for a monoprotic acid, so a pKa far above pH 7.4 makes the neutral
# fraction unity and logD collapse onto logP, which is the correct limit.
_PKA_NEUTRAL = 14.0


def ionisation_class(smiles: str) -> tuple[str, float, str]:
    """(class, representative pKa, the group that decided it)."""
    mol = Chem.MolFromSmiles(smiles) if smiles else None
    if mol is None:
        return NEUTRAL, _PKA_NEUTRAL, "unparseable"
    hits = [
        (n, p)
        for n, patt, p in _ACIDIC
        if patt is not None and mol.HasSubstructMatch(patt)
    ]
    basic = mol.HasSubstructMatch(_BASIC) if _BASIC is not None else False
    if hits and basic:
        return ZWITTERION, min(p for _, p in hits), f"{hits[0][0]}+basic_N"
    if hits:
        name, pka = min(hits, key=lambda h: h[1])
        return ACID, pka, name
    if basic:
        return BASE, _PKA_BASE, "basic_N"
    return NEUTRAL, _PKA_NEUTRAL, "none"


def classify(df: pd.DataFrame, smiles_col: str = "canonical_smiles") -> pd.DataFrame:
    out = df.copy()
    res = out[smiles_col].fillna("").map(ionisation_class)
    out["ionisation_class"] = [r[0] for r in res]
    out["pka_assigned"] = [r[1] for r in res]
    out["ionisable_group"] = [r[2] for r in res]
    # logD(7.4).  For an ACID this is Step 5's Henderson-Hasselbalch; for a
    # BASE the neutral fraction is 1/(1+10^(pKa-pH)), so the sign flips; for a
    # NEUTRAL compound logD is logP by definition.
    logp = out["alogp"]
    acid = out.ionisation_class.isin([ACID, ZWITTERION])
    base = out.ionisation_class == BASE
    logd = logp.astype(float).copy()
    logd[acid] = ionisation.log_d(
        logp[acid].to_numpy(), out.pka_assigned[acid].to_numpy(), 7.4
    )
    logd[base] = logp[base].to_numpy() - np.log10(
        1.0 + np.power(10.0, out.pka_assigned[base].to_numpy() - 7.4)
    )
    out["logd74"] = logd
    return out


# --- Step 5 transfer --------------------------------------------------------


def kpuu_neural_retina(
    logp: np.ndarray,
    pka: np.ndarray,
    mw: np.ndarray,
    is_reference: np.ndarray | None = None,
    n: int = 200_000,
    seed: int = 20261109,
) -> np.ndarray:
    """Neural-retina Kp,uu for each candidate, as a Monte-Carlo sample.

    Uses Step 5's calibrated anchor and its declared parameter distributions
    verbatim.  Returns an ``[n_compound, n]`` array so that every downstream
    number can be quoted with the interval Step 5's rules require.

    ``is_reference`` marks rows that *are* fenofibric acid.  Step 5 special-cases
    the reference compound -- ``r_perm = r_efflux = 1`` exactly -- because
    transferring the anchor onto itself through a sampled logP error and an
    independently drawn reference pKa would inject variance that is not there.
    Without the flag the reference row is not the anchor, and every fold-change
    quoted against it is wrong.
    """
    rng = np.random.default_rng(seed)
    a = {
        k: parameters.ANCHOR[k].ppf(rng.random(n))
        for k in (
            "retina_ffa",
            "plasma_ffa",
            "retina_protein_mg",
            "vitreous_vol_ul",
            "retina_vol_ul",
            "plasma_protein_mouse",
            "fu_plasma_mouse_ffa",
            "fu_tissue_retina",
            "late_sample_bias",
        )
    }
    a["retina_ffa"] = np.clip(a["retina_ffa"], 1e-4, None)
    a["plasma_ffa"] = np.clip(a["plasma_ffa"], 1e-2, None)
    kpuu_ref = barrier.kpuu_neural_retina_reference(a)

    B = parameters.BARRIER
    slope_d = B["perm_logd_slope"].ppf(rng.random(n))
    slope_mw = B["perm_mw_slope"].ppf(rng.random(n))
    share = B["efflux_share"].ppf(rng.random(n))
    ref_pka = FENOFIBRIC_ACID.pka.ppf(rng.random(n))
    logp_err = parameters.LOGP_ERROR.ppf(rng.random(n))

    if is_reference is None:
        is_reference = np.zeros(len(logp), dtype=bool)

    out = np.empty((len(logp), n))
    for i in range(len(logp)):
        if is_reference[i]:
            r_perm = np.ones(n)
            r_efflux = np.ones(n)
        else:
            r_perm = barrier.relative_permeability(
                logp[i] + logp_err,
                pka[i],
                mw[i],
                FENOFIBRIC_ACID.logp,
                ref_pka,
                FENOFIBRIC_ACID.mw,
                slope_d,
                slope_mw,
            )
            r_efflux = B["efflux_rel"].ppf(rng.random(n))
        out[i] = barrier.kpuu_transfer(kpuu_ref, r_perm, r_efflux, share)
    return out


# --- the window -------------------------------------------------------------
#
# Bounds for a compound that has to reach the neural retina behind a tight
# junction.  They are the CNS-penetrant window, which is the right reference
# class: the blood-retinal barrier is built from the same tight junctions and
# the same efflux pumps as the blood-brain barrier, and the retina expresses
# ABCB1 at 507 nCPM (data/processed/retina_hpa_celltype_ncpm.tsv).

WINDOW = {
    "mw_max": 500.0,
    "tpsa_max": 90.0,
    "hbd_max": 3.0,
    "logd_min": 1.0,
    "logd_max": 5.0,
}


def _efflux_risk(row) -> float:
    """A transparent P-glycoprotein-substrate proxy, 0-3, no measurement behind it.

    No LXR ligand has a measured efflux ratio at any ocular barrier -- the same
    hole Step 5 found for the fibrates and ranked as a dominant uncertainty.
    This is a declared heuristic on the three properties that recur in P-gp
    substrate models (size, hydrogen-bond acceptor count, polar surface), not a
    prediction, and it is reported as a flag rather than folded into a score.
    """
    return float(
        (row.full_mwt > 450) + (row.hba is not None and row.hba > 7) + (row.psa > 75)
    )


def apply_filter(df: pd.DataFrame) -> pd.DataFrame:
    """Annotate every candidate with pass/fail and the reason."""
    out = df.copy()
    reasons = []
    for _, r in out.iterrows():
        why = []
        if not np.isfinite(r.get("logd74", np.nan)):
            why.append("no logP")
        else:
            if r.logd74 < WINDOW["logd_min"]:
                why.append(f"logD {r.logd74:.1f} < {WINDOW['logd_min']}")
            if r.logd74 > WINDOW["logd_max"]:
                why.append(
                    f"logD {r.logd74:.1f} > {WINDOW['logd_max']} (too lipophilic)"
                )
        if r.full_mwt > WINDOW["mw_max"]:
            why.append(f"MW {r.full_mwt:.0f} > {WINDOW['mw_max']:.0f}")
        if np.isfinite(r.psa) and r.psa > WINDOW["tpsa_max"]:
            why.append(f"TPSA {r.psa:.0f} > {WINDOW['tpsa_max']:.0f}")
        if np.isfinite(r.hbd) and r.hbd > WINDOW["hbd_max"]:
            why.append(f"HBD {r.hbd:.0f} > {WINDOW['hbd_max']:.0f}")
        if r.ionisation_class in (ACID, ZWITTERION):
            why.append(f"ionised ({r.ionisable_group}) - the fibrate failure mode")
        reasons.append("; ".join(why))
    out["filter_reasons"] = reasons
    out["passes_filter"] = out.filter_reasons == ""
    out["efflux_risk_flags"] = out.apply(_efflux_risk, axis=1)
    return out
