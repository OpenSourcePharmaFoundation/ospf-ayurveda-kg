"""The liability that has killed every systemic agent of this class.

LXR agonism raises ABCA1 and ABCG1.  It also raises SREBF1 (SREBP-1c), FASN
and SCD1 in hepatocytes, and that second programme is why no LXR agonist has
reached registration.  T0901317 produces frank hepatic steatosis and
hypertriglyceridaemia in rodents; BMS-852927 reached human studies and raised
plasma and hepatic triglyceride with a fall in neutrophils; LXR-623 was
stopped in phase 1 for central nervous system effects.  The brief is right
that isoform selectivity or tissue restriction is the entire problem rather
than a detail.

The division of labour between the isoforms is what makes the problem
tractable in principle:

* **LXR-alpha (NR1H3)** is the hepatocyte-dominant isoform and carries the
  lipogenic output.  It is the one to avoid.
* **LXR-beta (NR1H2)** is ubiquitously expressed, carries the ABCA1/ABCG1
  efflux programme in peripheral and retinal cells, and drives far less
  hepatic lipogenesis.

So the design requirement is a quantity, not a wish, and this module derives
it.  Writing ``Cu`` for the free plasma concentration at steady state, the
retina sees ``Kp,uu x Cu`` (Step 5's transfer, ~0.85 for a neutral ligand) and
the hepatocyte sees ``H x Cu``, where ``H`` exceeds 1 for an orally dosed
lipophilic compound because of first-pass and hepatic partitioning.  Engaging
retinal LXR-beta while leaving hepatic LXR-alpha under-occupied by a factor
``S`` requires

    EC50_alpha / EC50_beta  >  S x H / Kp,uu

which in log units is the selectivity requirement

    beta_selectivity  >  log10(S) + log10(H) - log10(Kp,uu)

``Kp,uu`` close to 1 is worth about 1.2 log units against the fibrates'
0.059, and that is the whole contribution of going neutral: it does not make
the receptor safer, it lowers the selectivity a safe molecule has to carry.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# Hepatic free-concentration multiple over plasma for an orally dosed
# lipophilic neutral compound.  ASSUMED: no LXR ligand has a measured human
# hepatic Kp,uu.  1 is the well-stirred lower bound (free liver = free
# plasma); 10 spans first-pass exposure and the hepatic uptake that a logP-4
# neutral compound would show.
HEPATIC_MULTIPLE = (1.0, 10.0)

# Fold below the hepatic EC50 that counts as "not engaged".  3 is permissive,
# 30 is the margin a chronic ocular indication in a diabetic population would
# realistically be held to.
SAFETY_FACTORS = (3.0, 10.0, 30.0)


def selectivity_requirement(
    kpuu: float, safety_factor: float, hepatic_multiple: float
) -> float:
    """Minimum LXR-beta selectivity, in log10 units, for the stated margin."""
    return float(np.log10(safety_factor) + np.log10(hepatic_multiple) - np.log10(kpuu))


def requirement_grid(kpuu_neutral: float, kpuu_acid: float) -> pd.DataFrame:
    """The requirement across the declared ranges, for both chemotypes.

    The point of tabulating the acid alongside is that the fibrate route needs
    roughly 1.2 log units *more* selectivity than the neutral route to reach
    the same hepatic margin, purely because it reaches the retina 14x less
    well.  That is the same shortfall Step 5 found, re-expressed as a medicinal
    chemistry requirement.
    """
    rows = []
    for label, kpuu in (
        ("neutral LXR ligand", kpuu_neutral),
        ("fibrate-like acid", kpuu_acid),
    ):
        for s in SAFETY_FACTORS:
            for h in HEPATIC_MULTIPLE:
                rows.append(
                    {
                        "chemotype": label,
                        "kpuu_neural_retina": round(kpuu, 4),
                        "hepatic_safety_factor": s,
                        "hepatic_free_multiple": h,
                        "required_beta_selectivity_log": round(
                            selectivity_requirement(kpuu, s, h), 2
                        ),
                    }
                )
    return pd.DataFrame(rows)


def assess(candidates: pd.DataFrame, kpuu_col: str = "kpuu_median") -> pd.DataFrame:
    """Per-candidate verdict against the requirement grid.

    ``margin_log`` is how much measured selectivity the compound has in hand
    beyond what its own Kp,uu demands, at the central assumption (S = 10,
    H = 3.16, the geometric centre of the declared hepatic range).  Negative
    means the compound cannot reach retinal LXR-beta without engaging hepatic
    LXR-alpha, whatever the dose.
    """
    h_central = float(np.sqrt(HEPATIC_MULTIPLE[0] * HEPATIC_MULTIPLE[1]))
    out = candidates.copy()
    out["required_selectivity_log"] = [
        (
            selectivity_requirement(k, 10.0, h_central)
            if np.isfinite(k) and k > 0
            else np.nan
        )
        for k in out[kpuu_col]
    ]
    out["selectivity_margin_log"] = out.beta_selectivity - out.required_selectivity_log
    out["steatosis_verdict"] = np.where(
        out.selectivity_margin_log.isna(),
        "unknown - both isoforms not measured",
        np.where(
            out.selectivity_margin_log >= 0,
            "clears a 10x hepatic margin on measured selectivity",
            "insufficient selectivity for a 10x hepatic margin",
        ),
    )
    return out
