"""Variance decomposition: which input actually decides the answer.

This is the part of the step that nobody has done.  A model with twenty-three
uncertain inputs and a three-log output spread is not improved by measuring a
random one of them; it is improved by measuring whichever one carries the
variance.  Sobol indices answer that directly and without assuming the model
is linear or monotone.

Two indices per input, by the standard Saltelli/Jansen estimators:

``S1``  first order -- the share of output variance removed by learning that
        input exactly, with every other input left uncertain.
``ST``  total -- the share that would remain if every *other* input were
        learned exactly.  ``ST - S1`` is the part that only acts through
        interactions.

The output is ``log10(margin)``.  That is the right scale for a quantity built
from a product of lognormals: variance decomposition on the linear margin would
describe the behaviour of the top percentile and call it the model.
"""

from __future__ import annotations

import numpy as np

from . import model, potency
from .compounds import Compound


def sobol(
    cmp: Compound,
    pot: potency.Potency,
    compartment: str,
    n: int = 65_536,
    seed: int = 20261109,
    exposure: str = "c_avg",
) -> dict[str, tuple[float, float]]:
    """First-order and total Sobol indices on log10(margin).

    Returns ``{input_name: (S1, ST)}``.  Cost is ``(k + 2) * n`` model
    evaluations; the model is vectorised arithmetic, so that is seconds.
    """
    rng = np.random.default_rng(seed)
    k = model.N_INPUTS
    A = rng.random((n, k))
    B = rng.random((n, k))

    def f(u):
        return np.log10(model.evaluate(u, cmp, pot, exposure).margins[compartment])

    fA, fB = f(A), f(B)
    var = np.var(np.concatenate([fA, fB]))
    if var <= 0:
        return {name: (0.0, 0.0) for name in model.INPUT_NAMES}

    out = {}
    for i, name in enumerate(model.INPUT_NAMES):
        AB = A.copy()
        AB[:, i] = B[:, i]
        fAB = f(AB)
        s1 = float(np.mean(fB * (fAB - fA)) / var)
        st = float(np.mean((fA - fAB) ** 2) / (2.0 * var))
        out[name] = (s1, st)
    return out


# A per-input ranking can mislead when one block of physics is split across
# eighteen parameters and another sits in three.  The decision -- where to spend
# measurement effort -- is made between blocks, so the blocks are indexed as
# units too.
GROUPS: dict[str, list[str]] = {
    "potency (EC50 + its assay conditions)": [
        "compound.ec50_nominal",
        "assay.serum_fraction",
        "assay.fbs_albumin_ratio",
    ],
    "barrier (partition ratio, all inputs)": [
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
        "compound.pka",
        "reference.pka",
        "compound.logp",
    ],
    "plasma exposure (dose, PK, binding)": [
        "compound.c_plasma",
        "compound.fu_plasma",
    ],
}


def sobol_groups(
    cmp: Compound,
    pot: potency.Potency,
    compartment: str,
    n: int = 65_536,
    seed: int = 20261109,
    exposure: str = "c_avg",
) -> dict[str, tuple[float, float]]:
    """Sobol indices for whole blocks of inputs rather than single inputs."""
    rng = np.random.default_rng(seed)
    k = model.N_INPUTS
    A = rng.random((n, k))
    B = rng.random((n, k))

    def f(u):
        return np.log10(model.evaluate(u, cmp, pot, exposure).margins[compartment])

    fA, fB = f(A), f(B)
    var = np.var(np.concatenate([fA, fB]))
    out = {}
    for label, names in GROUPS.items():
        cols = [model.IDX[nm] for nm in names if nm in model.IDX]
        AB = A.copy()
        AB[:, cols] = B[:, cols]
        fAB = f(AB)
        out[label] = (
            float(np.mean(fB * (fAB - fA)) / var),
            float(np.mean((fA - fAB) ** 2) / (2.0 * var)),
        )
    return out


def ranked(indices: dict[str, tuple[float, float]], by: int = 1):
    """Inputs ordered by total (``by=1``) or first-order (``by=0``) index."""
    return sorted(indices.items(), key=lambda kv: -kv[1][by])


def pooled(results: dict[str, dict[str, tuple[float, float]]]) -> dict[str, float]:
    """Mean total index across several compounds, for a single headline rank."""
    names = model.INPUT_NAMES
    return {n: float(np.mean([r[n][1] for r in results.values()])) for n in names}
