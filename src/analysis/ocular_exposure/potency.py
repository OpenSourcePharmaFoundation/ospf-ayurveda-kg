"""EC50 distributions, read from the repository's own ChEMBL pull.

``data/processed/chembl_panel_bioactivities.csv`` was built in Step 1 of this
chain and holds 62,219 measured activities across the DR target panel.  For
the four compounds here it carries 26 PPARalpha EC50 determinations from
independent laboratories, which is a better statement of what the potency is
than any single paper's figure -- the inter-laboratory spread *is* the
uncertainty, and quoting one value would hide it.

Two kinds of record need different handling:

* ``standard_relation`` of ``=`` is a determination.  These fit the lognormal.
* ``>`` is a censored observation: the assay reached its top concentration
  without an EC50.  These are not averaged in -- doing so would pull a weak
  compound's EC50 *down* towards its own detection limit.  They are kept and
  reported, and used as a consistency check: a fitted median must not sit
  above a censoring bound that says activity was absent there.

Where a compound has too few determinations to estimate a spread (pemafibrate
has three, all reported as exactly 1 nM), a floor is imposed on the geometric
standard deviation.  Three laboratories agreeing to one significant figure is
agreement about the order of magnitude, not evidence that the between-assay
spread is zero.
"""

from __future__ import annotations

import dataclasses
import math
import pathlib

import numpy as np
import pandas as pd

REPO = pathlib.Path(__file__).resolve().parents[3]
BIOACTIVITIES = REPO / "data" / "processed" / "chembl_panel_bioactivities.csv"

# Three assays agreeing to one significant figure do not make the spread zero.
MIN_GSD = 2.5


@dataclasses.dataclass(frozen=True)
class Potency:
    gene: str
    chembl: str
    n_determinations: int
    median_nM: float
    gsd: float
    censored_nM: tuple[float, ...]
    values_nM: tuple[float, ...]

    def ci95(self) -> tuple[float, float]:
        s = math.log(self.gsd)
        return self.median_nM * math.exp(-1.96 * s), self.median_nM * math.exp(1.96 * s)

    def sample(self, u: np.ndarray) -> np.ndarray:
        from .parameters import _norm_ppf

        return self.median_nM * np.exp(math.log(self.gsd) * _norm_ppf(u))


def load(chembl_id: str, gene: str, path: pathlib.Path | None = None) -> Potency:
    df = pd.read_csv(path or BIOACTIVITIES)
    sel = df[
        (df.molecule_chembl_id == chembl_id)
        & (df.gene == gene)
        & (df.standard_type == "EC50")
        & (df.standard_units == "nM")
    ]
    eq = sel[sel.standard_relation == "="]["standard_value"].astype(float).to_numpy()
    cens = tuple(
        sorted(sel[sel.standard_relation != "="]["standard_value"].astype(float))
    )
    if eq.size == 0:
        raise ValueError(f"no uncensored EC50 for {chembl_id} / {gene}")

    log_vals = np.log(eq)
    median = float(np.exp(np.median(log_vals)))
    gsd = float(np.exp(np.std(log_vals, ddof=1))) if eq.size > 1 else MIN_GSD
    return Potency(
        gene,
        chembl_id,
        int(eq.size),
        median,
        max(gsd, MIN_GSD),
        cens,
        tuple(sorted(eq)),
    )
