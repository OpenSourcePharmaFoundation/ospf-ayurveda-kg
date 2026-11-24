"""Per-cell-type expression of the DR panel in human retina, from CZ CELLxGENE Census.

Computes, for every (dataset x cell type x suspension x assay) group and every gene
in the panel:

  n_cells, n_expressing (raw count > 0), pct_expressing,
  mean_cp10k over all cells in the group, mean_cp10k over expressing cells only.

CP10K is computed from the raw integer count and the cell's own ``raw_sum``, so it
is a real counts-per-10k figure, not a rankit score.  Nothing here is imputed:
a zero is a zero observed count, which is exactly the quantity the dropout
argument is about.

Also emits:
  * the dataset-level feature presence matrix, which distinguishes "the gene was
    not in this dataset's feature space" (absent) from "the gene was measurable
    and seen in zero cells" (below detection threshold);
  * detection rate as a function of per-cell sequencing depth (nnz decile),
    which is the quantitative form of the dropout confound.

Usage:  python src/analysis/retina_expression/query_census.py [--out-dir DIR]
"""

from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from analysis.retina_expression.census_client import (
    CENSUS_VERSION,
    open_census,
)  # noqa: E402
from analysis.retina_expression.gene_panel import all_genes  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "data" / "processed"

# UBERON tissue labels that are retina proper, RPE, or retina+choroid composites.
# Deliberately excludes cornea, lens, iris, sclera, conjunctiva, trabecular
# meshwork, ciliary body, lacrimal gland and optic disc: none of those are the
# neural retina or RPE, and including them would dilute every cell-type figure.
RETINA_TISSUES = [
    "retina",
    "central retina",
    "peripheral region of retina",
    "macula lutea",
    "macula lutea proper",
    "fovea centralis",
    "perifoveal part of retina",
    "retinal neural layer",
    "pigmented layer of retina",
    "chorioretinal region",
]

OBS_COLS = [
    "soma_joinid",
    "dataset_id",
    "tissue",
    "assay",
    "disease",
    "suspension_type",
    "cell_type",
    "tissue_type",
    "development_stage",
    "donor_id",
    "raw_sum",
    "nnz",
]


def _obs_filter() -> str:
    """Primary, non-organoid cells from retina/RPE tissue.

    ``tissue_type == 'tissue'`` matters: CZ CELLxGENE files retinal *organoid*
    cells under the same tissue labels as donor retina.  Organoid photoreceptors
    are developmentally immature and would drag every photoreceptor figure down.
    ``is_primary_data`` prevents cells that appear in more than one published
    dataset from being counted twice.
    """
    tis = ", ".join(f"'{t}'" for t in RETINA_TISSUES)
    return (
        f"tissue in [{tis}] and is_primary_data == True " f"and tissue_type == 'tissue'"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(OUT_DIR))
    ap.add_argument("--census-version", default=CENSUS_VERSION)
    ap.add_argument(
        "--genes",
        help="comma-separated subset of the panel to query.  Dropping the few "
        "transcriptome-dominating genes (ACTB/GAPDH/RHO/B2M/RPL13A) cuts "
        "the expression-matrix traffic by roughly an order of magnitude, "
        "which matters when reading Census through a proxy.",
    )
    ap.add_argument("--prefix", default="retina_sc_", help="output filename prefix")
    args = ap.parse_args()
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    genes = all_genes()
    if args.genes:
        want = {g.strip() for g in args.genes.split(",") if g.strip()}
        unknown = sorted(want - set(genes))
        if unknown:
            print(f"[warn] not in panel, ignored: {unknown}", file=sys.stderr)
        genes = {g: c for g, c in genes.items() if g in want}
    symbols = sorted(genes)

    import tiledbsoma as soma

    census = open_census(args.census_version)
    try:
        h = census["census_data"]["homo_sapiens"]

        # ---- genes -------------------------------------------------------
        var = (
            h.ms["RNA"]
            .var.read(
                value_filter=f"feature_name in {symbols!r}",
                column_names=["soma_joinid", "feature_id", "feature_name"],
            )
            .concat()
            .to_pandas()
        )
        missing = sorted(set(symbols) - set(var.feature_name))
        if missing:
            print(f"[warn] not in census var axis: {missing}", file=sys.stderr)
        var = var.sort_values("feature_name").reset_index(drop=True)
        gene_jids = var.soma_joinid.to_numpy()
        ng = len(gene_jids)
        # vectorised var-joinid -> column lookup; the loop over ~10^8 nonzero
        # entries below cannot afford a Python dict lookup per entry.
        gene_order = np.argsort(gene_jids)
        gene_jids_sorted = gene_jids[gene_order]
        print(f"[info] resolved {ng} genes")

        # ---- cells -------------------------------------------------------
        obs = (
            h.obs.read(value_filter=_obs_filter(), column_names=OBS_COLS)
            .concat()
            .to_pandas()
            .sort_values("soma_joinid")
            .reset_index(drop=True)
        )
        print(f"[info] retina cells (primary): {len(obs):,}")
        obs_jids = obs.soma_joinid.to_numpy()
        raw_sum = obs.raw_sum.to_numpy(dtype=np.float64)

        # fine-grained grouping; everything else is a rollup of this
        key = (
            obs.dataset_id.astype(str)
            + "|"
            + obs.cell_type.astype(str)
            + "|"
            + obs.suspension_type.astype(str)
            + "|"
            + obs.assay.astype(str)
            + "|"
            + obs.disease.astype(str)
            + "|"
            + obs.development_stage.astype(str)
        )
        grp_codes, grp_keys = pd.factorize(key, sort=True)
        ngrp = len(grp_keys)
        print(f"[info] groups: {ngrp:,}")

        # depth bins: deciles of nnz within each suspension type, because
        # nuclei and whole cells have different depth distributions.
        depth_bin = np.zeros(len(obs), dtype=np.int64)
        susp = obs.suspension_type.to_numpy()
        nnz = obs.nnz.to_numpy()
        susp_levels = sorted(set(susp.tolist()))
        for si, s in enumerate(susp_levels):
            m = susp == s
            q = np.quantile(nnz[m], np.linspace(0, 1, 11)[1:-1])
            depth_bin[m] = si * 10 + np.searchsorted(q, nnz[m], side="right")
        nbins = len(susp_levels) * 10

        n_expr = np.zeros(ngrp * ng, dtype=np.int64)
        sum_cp10k = np.zeros(ngrp * ng, dtype=np.float64)
        sum_raw = np.zeros(ngrp * ng, dtype=np.float64)
        d_expr = np.zeros(nbins * ng, dtype=np.int64)

        q = h.axis_query(
            measurement_name="RNA",
            obs_query=soma.AxisQuery(value_filter=_obs_filter()),
            var_query=soma.AxisQuery(coords=(gene_jids,)),
        )
        seen = 0
        for tbl in q.X("raw").tables():
            d0 = tbl.column("soma_dim_0").to_numpy()
            d1 = tbl.column("soma_dim_1").to_numpy()
            val = tbl.column("soma_data").to_numpy().astype(np.float64)
            pos = np.searchsorted(obs_jids, d0)
            gi = gene_order[np.searchsorted(gene_jids_sorted, d1)]
            gidx = grp_codes[pos] * ng + gi
            n_expr += np.bincount(gidx, minlength=ngrp * ng)
            sum_cp10k += np.bincount(
                gidx, weights=val / raw_sum[pos] * 1e4, minlength=ngrp * ng
            )
            sum_raw += np.bincount(gidx, weights=val, minlength=ngrp * ng)
            didx = depth_bin[pos] * ng + gi
            d_expr += np.bincount(didx, minlength=nbins * ng)
            seen += len(val)
            print(f"\r[info] nonzero entries: {seen:,}", end="", file=sys.stderr)
        print(file=sys.stderr)
        q.close()

        # ---- assemble fine table ----------------------------------------
        gsize = np.bincount(grp_codes, minlength=ngrp)
        meta = pd.DataFrame(
            [k.split("|") for k in grp_keys],
            columns=[
                "dataset_id",
                "cell_type",
                "suspension_type",
                "assay",
                "disease",
                "development_stage",
            ],
        )
        meta["n_cells"] = gsize
        rows = meta.loc[np.repeat(np.arange(ngrp), ng)].reset_index(drop=True)
        rows["gene"] = np.tile(var.feature_name.to_numpy(), ngrp)
        rows["ensembl_id"] = np.tile(var.feature_id.to_numpy(), ngrp)
        rows["category"] = rows.gene.map(genes)
        rows["n_expressing"] = n_expr
        rows["sum_cp10k"] = sum_cp10k
        rows["sum_raw_counts"] = sum_raw
        rows.to_csv(out / f"{args.prefix}group_expression.tsv", sep="\t", index=False)
        print(
            f"[ok] {out / (args.prefix + 'group_expression.tsv')}  ({len(rows):,} rows)"
        )

        # Dataset provenance and the feature-presence matrix are written by
        # census_presence.py, which is the single owner of those two files and
        # runs in minutes because it reads no expression data.

        # ---- depth / dropout --------------------------------------------
        bin_n = np.bincount(depth_bin, minlength=nbins)
        med_nnz = pd.Series(nnz).groupby(depth_bin).median().reindex(range(nbins))
        med_umi = pd.Series(raw_sum).groupby(depth_bin).median().reindex(range(nbins))
        drows = pd.DataFrame(
            {
                "suspension_type": np.repeat(
                    [susp_levels[i // 10] for i in range(nbins)], ng
                ),
                "depth_decile": np.repeat([(i % 10) + 1 for i in range(nbins)], ng),
                "n_cells": np.repeat(bin_n, ng),
                "median_genes_per_cell": np.repeat(med_nnz.to_numpy(), ng),
                "median_umis_per_cell": np.repeat(med_umi.to_numpy(), ng),
                "gene": np.tile(var.feature_name.to_numpy(), nbins),
                "category": np.tile([genes[g] for g in var.feature_name], nbins),
                "n_expressing": d_expr,
            }
        )
        drows["pct_expressing"] = (
            100.0 * drows.n_expressing / drows.n_cells.replace(0, np.nan)
        )
        drows.to_csv(out / f"{args.prefix}depth_dropout.tsv", sep="\t", index=False)
        print(
            f"[ok] {out / (args.prefix + 'depth_dropout.tsv')}  ({len(drows):,} rows)"
        )
    finally:
        census.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
