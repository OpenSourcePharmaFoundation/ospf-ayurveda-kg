#!/usr/bin/env python3
"""Run the Step 6 efflux-axis analysis and write every artefact.

    python -m src.analysis.efflux_axis.run            # full run, hits ChEMBL
    python -m src.analysis.efflux_axis.run --cached   # reuse the pulled TSVs

Outputs, all under ``data/processed/``:

    efflux_axis_targets.csv            gene -> ChEMBL target resolution
    efflux_axis_bioactivities.csv      every qualifying measured activity
    efflux_axis_edge_semantics.csv     what the knowledge-graph edges assert
    efflux_axis_gnn_benchmark.csv      whether the GNN can rank this axis
    efflux_axis_gnn_predictions.csv    the GNN's ranking, with its degree controls
    efflux_axis_candidates.csv         measured candidates, filtered and scored
    efflux_axis_selectivity_grid.csv   required beta-selectivity vs chemotype
    efflux_axis_burden_model.csv       acceptor vs inducer sweep
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from . import acceptor, axis, candidates, chembl_axis, gnn_rank, physchem, steatosis

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA = PROJECT_ROOT / "data" / "processed"

TARGETS_CSV = DATA / "efflux_axis_targets.csv"
ACT_CSV = DATA / "efflux_axis_bioactivities.csv"
MOLS_CSV = DATA / "efflux_axis_molecules.csv"
SEM_CSV = DATA / "efflux_axis_edge_semantics.csv"
BENCH_CSV = DATA / "efflux_axis_gnn_benchmark.csv"
GNN_CSV = DATA / "efflux_axis_gnn_predictions.csv"
CAND_CSV = DATA / "efflux_axis_candidates.csv"
GRID_CSV = DATA / "efflux_axis_selectivity_grid.csv"
BURDEN_CSV = DATA / "efflux_axis_burden_model.csv"

POTENT = 6.0  # pchembl >= 6 <=> <= 1 uM, the conventional active cut
GNN_TOP_PER_GENE = 50


def pull(cached: bool) -> dict[str, pd.DataFrame]:
    if cached and ACT_CSV.exists():
        return {
            "targets": pd.read_csv(TARGETS_CSV),
            "activities": pd.read_csv(ACT_CSV),
            "molecules": pd.read_csv(MOLS_CSV),
        }
    res = chembl_axis.pull_axis(axis.AXIS)
    cand = candidates.lxr_candidates(res["activities"])
    ids = cand[cand.p_best >= POTENT].molecule_chembl_id.tolist()
    res["molecules"] = chembl_axis.fetch_molecules(ids)
    DATA.mkdir(parents=True, exist_ok=True)
    res["targets"].to_csv(TARGETS_CSV, index=False)
    res["activities"].to_csv(ACT_CSV, index=False)
    res["molecules"].to_csv(MOLS_CSV, index=False)
    return res


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cached", action="store_true", help="reuse the pulled CSVs")
    ap.add_argument("--skip-gnn", action="store_true")
    args = ap.parse_args(argv)
    DATA.mkdir(parents=True, exist_ok=True)

    # 1. What the knowledge graph asserts, and whether the GNN can rank it.
    if not args.skip_gnn:
        gnn_rank.edge_semantics(axis.SYMBOLS).to_csv(SEM_CSV, index=False)
        gnn_rank.benchmark_axis_retrieval(axis.SYMBOLS).to_csv(BENCH_CSV, index=False)
        preds = gnn_rank.score_axis(axis.SYMBOLS)
        (
            preds[~preds.observed_edge]
            .sort_values(["gene", "score"], ascending=[True, False])
            .groupby("gene")
            .head(GNN_TOP_PER_GENE)
            .to_csv(GNN_CSV, index=False)
        )
        print(f"wrote {SEM_CSV.name}, {BENCH_CSV.name}, {GNN_CSV.name}")

    # 2. Measured pharmacology.
    res = pull(args.cached)
    cand = candidates.lxr_candidates(res["activities"])
    cand = cand[cand.p_best >= POTENT]
    cand = candidates.attach_properties(cand, res["molecules"])

    # 3. Retinal access, via the Step 5 barrier model.
    cand = physchem.classify(cand)
    cand = physchem.apply_filter(cand)
    kp = physchem.kpuu_neural_retina(
        cand.alogp.fillna(0).to_numpy(float),
        cand.pka_assigned.to_numpy(float),
        cand.full_mwt.fillna(400).to_numpy(float),
    )
    cand["kpuu_median"] = np.median(kp, axis=1)
    cand["kpuu_lo95"] = np.percentile(kp, 2.5, axis=1)
    cand["kpuu_hi95"] = np.percentile(kp, 97.5, axis=1)

    # 4. The steatosis requirement.
    cand = steatosis.assess(cand)
    cand.sort_values(
        ["passes_filter", "beta_selectivity", "p_beta"], ascending=False
    ).to_csv(CAND_CSV, index=False)
    kpuu_neutral = float(cand.loc[cand.passes_filter, "kpuu_median"].median())
    steatosis.requirement_grid(kpuu_neutral, 0.0594).to_csv(GRID_CSV, index=False)
    print(f"wrote {CAND_CSV.name} ({len(cand)} rows), {GRID_CSV.name}")

    # 5. Acceptor versus inducer.
    acceptor.sweep().to_csv(BURDEN_CSV, index=False)
    print(f"wrote {BURDEN_CSV.name}")


if __name__ == "__main__":
    main()
