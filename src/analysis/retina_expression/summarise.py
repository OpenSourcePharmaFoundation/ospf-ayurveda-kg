"""Roll the fine-grained Census output up into the per-cell-type answer table.

``query_census.py`` writes one row per (dataset x cell type x suspension x assay
x disease x development stage) x gene, which is the right grain to keep but the
wrong grain to read.  This collapses it to major retinal cell classes, restricted
to adult non-diseased donors, and emits the table the question is actually about:

  gene x cell class -> n cells, n expressing, % expressing, mean CP10K,
  mean CP10K among expressing cells.

Also emits the two stratifications that the dropout argument needs:
  * ``*_by_suspension.tsv``  - whole cell vs nucleus, same cell classes.
  * ``*_by_dataset.tsv``     - per atlas, so detection can be regressed on that
    atlas's sequencing depth.

Usage:  python src/analysis/retina_expression/summarise.py
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "data" / "processed"

# Census cell_type labels are finer than the question needs (16 bipolar subtypes,
# 6 ganglion subtypes).  Collapse to the classes the DR literature argues about.
# Order matters: first match wins.
CLASSES: list[tuple[str, str]] = [
    (r"^retinal rod cell$", "Rod photoreceptor"),
    (r"cone", "Cone photoreceptor"),
    (r"^Mueller cell$|muller", "Mueller glia"),
    (r"pigment epithel", "Retinal pigment epithelium"),
    (r"bipolar", "Bipolar cell"),
    (r"amacrine", "Amacrine cell"),
    (r"horizontal", "Horizontal cell"),
    (r"ganglion|OFFx", "Retinal ganglion cell"),
    (r"endothelial", "Vascular endothelium"),
    (r"^pericyte$", "Pericyte"),
    (r"smooth muscle", "Vascular smooth muscle"),
    (r"microglial|macrophage|monocyte|dendritic", "Microglia / macrophage"),
    (r"astrocyte|^glial cell$|macroglial", "Astrocyte / other glia"),
    (r"melanocyte", "Melanocyte"),
    (r"fibroblast", "Fibroblast"),
]

FETAL = re.compile(r"fetal|embryo|week post-fertilization|carnegie", re.I)


def cell_class(label: str) -> str | None:
    for pat, name in CLASSES:
        if re.search(pat, label, re.I):
            return name
    return None


def _agg(df: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    g = df.groupby(keys, as_index=False, observed=True).agg(
        n_cells=("n_cells", "sum"),
        n_expressing=("n_expressing", "sum"),
        sum_cp10k=("sum_cp10k", "sum"),
        sum_raw_counts=("sum_raw_counts", "sum"),
    )
    g["pct_expressing"] = 100 * g.n_expressing / g.n_cells
    g["mean_cp10k"] = g.sum_cp10k / g.n_cells
    g["mean_cp10k_in_expressing"] = g.sum_cp10k / g.n_expressing.replace(0, pd.NA)
    return g.drop(columns=["sum_cp10k"])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--in-file", default=str(OUT_DIR / "retina_sc_group_expression.tsv")
    )
    ap.add_argument("--out-dir", default=str(OUT_DIR))
    ap.add_argument(
        "--min-cells",
        type=int,
        default=2000,
        help="drop cell classes with fewer cells than this",
    )
    args = ap.parse_args()
    out = pathlib.Path(args.out_dir)

    d = pd.read_csv(args.in_file, sep="\t")
    n0 = len(d)
    # Adult, non-diseased donors only.  Fetal retina has a different cell
    # composition and AMD/cataract donors are a separate question.
    d = d[
        (d.disease == "normal") & (~d.development_stage.astype(str).str.contains(FETAL))
    ]
    # Keep only datasets the provenance step accepted.  That step applies the
    # tissue_type == 'tissue' filter, so this drops retinal-organoid datasets
    # from expression files generated before that filter existed.
    ds_ok = pd.read_csv(
        pathlib.Path(args.out_dir) / "retina_sc_datasets.tsv", sep="\t"
    ).dataset_id
    before = d.dataset_id.nunique()
    d = d[d.dataset_id.isin(set(ds_ok))]
    if d.dataset_id.nunique() != before:
        print(
            f"[info] dropped {before - d.dataset_id.nunique()} dataset(s) "
            f"not in the provenance table (organoid / non-tissue)"
        )
    d["cell_class"] = d.cell_type.map(cell_class)
    d = d[d.cell_class.notna()]
    print(f"[info] {n0:,} rows -> {len(d):,} adult non-diseased rows in named classes")

    by_class = _agg(d, ["cell_class", "gene", "ensembl_id", "category"])
    keep = by_class.groupby("cell_class").n_cells.max()
    keep = keep[keep >= args.min_cells].index
    by_class = by_class[by_class.cell_class.isin(keep)]
    p = out / "retina_sc_celltype_summary.tsv"
    by_class.sort_values(["gene", "cell_class"]).to_csv(p, sep="\t", index=False)
    print(
        f"[ok] {p}  ({len(by_class):,} rows, {by_class.cell_class.nunique()} classes)"
    )

    by_susp = _agg(d, ["cell_class", "suspension_type", "gene", "category"])
    by_susp = by_susp[by_susp.cell_class.isin(keep) & (by_susp.n_cells >= 500)]
    p = out / "retina_sc_celltype_by_suspension.tsv"
    by_susp.sort_values(["gene", "cell_class", "suspension_type"]).to_csv(
        p, sep="\t", index=False
    )
    print(f"[ok] {p}  ({len(by_susp):,} rows)")

    by_ds = _agg(d, ["dataset_id", "gene", "category"])
    ds = pd.read_csv(out / "retina_sc_datasets.tsv", sep="\t")
    cols = [
        c
        for c in [
            "dataset_id",
            "collection_name",
            "dataset_title",
            "citation",
            "suspension",
            "assays",
            "median_genes_per_cell",
            "median_umis_per_cell",
            "n_donors",
        ]
        if c in ds.columns
    ]
    by_ds = by_ds.merge(ds[cols], on="dataset_id", how="left")
    p = out / "retina_sc_by_dataset.tsv"
    by_ds.sort_values(["gene", "median_genes_per_cell"]).to_csv(
        p, sep="\t", index=False
    )
    print(f"[ok] {p}  ({len(by_ds):,} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
