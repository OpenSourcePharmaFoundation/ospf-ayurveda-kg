"""Turn raw axis activities into a ranked, annotated candidate table.

Three things happen here and they are kept separate on purpose.

**Aggregation.**  ChEMBL holds many activities per molecule-target pair,
measured in different assays by different groups.  The per-pair summary is the
*median* pchembl, not the best: taking the maximum over a dozen assays ranks
compounds by how often they were measured, which is the same literature-
attention artefact that makes the knowledge graph useless on this axis
(``gnn_rank.benchmark_axis_retrieval``).  The **internal range** is carried
alongside, because a median hides disagreement and on this axis the
disagreement decides the answer: 29% of molecule-gene pairs with two or more
EC50 values span more than a log, and for the single most selective candidate
the two reported LXR-alpha values differ 57-fold -- enough to move it across
the selectivity threshold in ``steatosis.py``.  A reader has to see that.

**Direction, and what the assay actually was.**  Efflux needs an *agonist*:
raising ABCA1/ABCG1 means turning LXR on.  The naive signal is
``standard_type`` -- EC50 for function, IC50/Ki/Kd for displacement -- but on
this axis it is misleading.  1,324 of the 1,801 EC50 rows carry
``assay_type = 'B'``: they come from a cell-free coactivator-recruitment FRET
assay on the isolated ligand-binding domain, not from a cellular
transactivation assay, and that patent assay is run in *both* agonist and
antagonist mode, so even an EC50 from it is not unambiguously agonist.  The
three tiers are therefore labelled explicitly:

    ``cell_functional``   EC50 from a cell-based assay (assay_type F).
                          Agonist-directional and cellular.
    ``lbd_recruitment``   EC50 from a cell-free LBD assay (assay_type B).
                          Reports a conformational response, not transcription,
                          and the source assay also runs in antagonist mode.
    ``displacement``      IC50/Ki/Kd.  Affinity only; direction unknown.

**Selectivity.**  ``beta_selectivity = p(NR1H2) - p(NR1H3)``, in log units,
positive meaning LXR-beta-preferring, computed only within one tier so a
cellular number is never differenced against a cell-free one.  This is the
axis on which the class lives or dies: LXR-alpha drives hepatic SREBF1 and so
the steatosis and hypertriglyceridaemia that killed every systemic agent of
this class, while LXR-beta carries the ABCA1/ABCG1 efflux programme.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

CELL_FUNCTIONAL = "cell_functional"
LBD_RECRUITMENT = "lbd_recruitment"
DISPLACEMENT = "displacement"

# Tier preference, best evidence first.
TIERS = (CELL_FUNCTIONAL, LBD_RECRUITMENT, DISPLACEMENT)


def tier_of(row) -> str:
    """Classify one activity row by what the assay could actually show."""
    if row.standard_type == "EC50":
        return CELL_FUNCTIONAL if row.assay_type == "F" else LBD_RECRUITMENT
    return DISPLACEMENT


def annotate(activities: pd.DataFrame) -> pd.DataFrame:
    out = activities.copy()
    out["pchembl_value"] = pd.to_numeric(out.pchembl_value, errors="coerce")
    out = out.dropna(subset=["pchembl_value"])
    out["tier"] = out.apply(tier_of, axis=1)
    return out


def summarise(activities: pd.DataFrame) -> pd.DataFrame:
    """One row per (molecule, gene, tier), with the internal range exposed."""
    a = annotate(activities)
    g = a.groupby(["molecule_chembl_id", "gene", "tier"]).pchembl_value
    out = pd.DataFrame(
        {
            "p_median": g.median(),
            "p_min": g.min(),
            "p_max": g.max(),
            "n": g.size(),
        }
    ).reset_index()
    out["range_log"] = (out.p_max - out.p_min).round(2)
    return out


def lxr_candidates(activities: pd.DataFrame) -> pd.DataFrame:
    """Best-tier potency at each LXR isoform, side by side, with selectivity.

    A molecule is summarised at the best tier for which *both* isoforms were
    measured, so that ``beta_selectivity`` never differences a cellular number
    against a cell-free one.  Where no tier has both, the best available tier
    per isoform is reported and selectivity is left undefined.
    """
    s = summarise(activities[activities.gene.isin(["NR1H2", "NR1H3"])])
    rows = []
    for mol, sub in s.groupby("molecule_chembl_id"):
        chosen = None
        for tier in TIERS:
            t = sub[sub.tier == tier]
            if {"NR1H2", "NR1H3"} <= set(t.gene):
                chosen = t
                break
        paired = chosen is not None
        if not paired:  # fall back to the best tier available per isoform
            chosen = (
                sub.assign(_o=sub.tier.map({t: i for i, t in enumerate(TIERS)}))
                .sort_values("_o")
                .groupby("gene")
                .head(1)
            )
        rec = {"molecule_chembl_id": mol, "paired_tier": paired}
        for gene, key in (("NR1H2", "beta"), ("NR1H3", "alpha")):
            r = chosen[chosen.gene == gene]
            if len(r):
                r = r.iloc[0]
                rec |= {
                    f"p_{key}": r.p_median,
                    f"p_{key}_min": r.p_min,
                    f"p_{key}_max": r.p_max,
                    f"n_{key}": int(r.n),
                    f"range_{key}_log": r.range_log,
                    f"tier_{key}": r.tier,
                }
            else:
                rec |= {
                    f"p_{key}": np.nan,
                    f"p_{key}_min": np.nan,
                    f"p_{key}_max": np.nan,
                    f"n_{key}": 0,
                    f"range_{key}_log": np.nan,
                    f"tier_{key}": None,
                }
        rows.append(rec)

    wide = pd.DataFrame(rows)
    both = wide.p_beta.notna() & wide.p_alpha.notna() & wide.paired_tier
    wide["beta_selectivity"] = np.where(both, wide.p_beta - wide.p_alpha, np.nan)
    # The selectivity a reader is entitled to assume given the internal spread:
    # worst case is the lowest beta against the highest alpha.
    wide["beta_selectivity_worst"] = np.where(
        both, wide.p_beta_min - wide.p_alpha_max, np.nan
    )
    wide["evidence_tier"] = np.where(
        wide.paired_tier, wide.tier_beta.fillna(wide.tier_alpha), "unpaired"
    )
    wide["p_best"] = wide[["p_beta", "p_alpha"]].max(axis=1)
    wide["n_measurements"] = wide.n_beta + wide.n_alpha
    wide["max_internal_range_log"] = wide[["range_beta_log", "range_alpha_log"]].max(
        axis=1
    )
    return wide.sort_values(["p_best", "n_measurements"], ascending=False).reset_index(
        drop=True
    )


def attach_properties(cands: pd.DataFrame, molecules: pd.DataFrame) -> pd.DataFrame:
    """Join ChEMBL molecule properties.

    ``molecular_species``, ``cx_logd``, ``cx_most_apka`` and ``cx_logp`` are
    requested but come back null for every molecule on this axis -- the same
    gap Step 5 documented for the fibrates -- which is why ``physchem.py`` has
    to derive the ionisation class from the SMILES instead of reading it.
    """
    out = cands.merge(molecules, on="molecule_chembl_id", how="left")
    num = [
        "full_mwt",
        "alogp",
        "cx_logp",
        "cx_logd",
        "cx_most_apka",
        "cx_most_bpka",
        "psa",
        "hba",
        "hbd",
        "rtb",
        "aromatic_rings",
        "heavy_atoms",
        "qed_weighted",
        "num_ro5_violations",
    ]
    for c in num:
        if c in out:
            out[c] = pd.to_numeric(out[c], errors="coerce")
    return out
