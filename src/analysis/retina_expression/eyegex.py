"""EyeGEx: the abundance question answered in 500+ human retinas.

GSE115828 (Ratnapriya et al. 2019, Nat Genet; the Eye Genotype Expression
resource) is bulk RNA-seq of post-mortem human retina from 523 donors graded for
AMD.  It is here purely as a **scale reference**: a cohort two orders of
magnitude larger than anything single-cell, used to establish where PPARA sits
in the retinal transcriptome without any dropout or per-cell sampling in the way.

It carries no diabetes annotation, so it says nothing about the diabetic
contrast; that is GSE160306's job.

Usage:  python src/analysis/retina_expression/eyegex.py --work-dir DIR
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from analysis.retina_expression.census_client import fix_proxy_env  # noqa: E402
from analysis.retina_expression.gene_panel import all_genes  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "data" / "processed"
URL = (
    "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE115nnn/GSE115828/suppl/"
    "GSE115828_RSEM_gene_counts.tsv.gz"
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work-dir", default=str(pathlib.Path.cwd() / "_eyegex"))
    ap.add_argument("--out-dir", default=str(OUT_DIR))
    args = ap.parse_args()
    fix_proxy_env()
    work = pathlib.Path(args.work_dir)
    work.mkdir(parents=True, exist_ok=True)
    counts_p = work / "counts.tsv.gz"
    if not counts_p.exists():
        subprocess.run(
            ["curl", "-sSL", "--fail", "--max-time", "900", "-o", str(counts_p), URL],
            check=True,
        )

    counts = pd.read_csv(counts_p, sep="\t", index_col=0)
    counts.index = [i.split(".")[0] for i in counts.index]
    print(
        f"[info] EyeGEx counts: {counts.shape[0]:,} genes x {counts.shape[1]:,} retinas"
    )

    cpm = counts.div(counts.sum(axis=0), axis=1) * 1e6
    mean_cpm = cpm.mean(axis=1)
    med_cpm = cpm.median(axis=1)
    detected = (counts > 0).mean(axis=1) * 100

    pct_all = mean_cpm.rank(pct=True) * 100
    expressed = mean_cpm[mean_cpm >= 1]
    pct_expr = expressed.rank(pct=True) * 100
    print(f"[info] features with mean CPM >= 1: {len(expressed):,}")

    genes = all_genes()
    hpa = pd.read_csv(OUT_DIR / "retina_hpa_bulk_ntpm.tsv", sep="\t")
    ens = dict(zip(hpa.gene, hpa.ensembl_id))
    recs = []
    for g, cat in sorted(genes.items()):
        e = ens.get(g)
        if e is None or e not in cpm.index:
            recs.append(
                {"gene": g, "ensembl_id": e, "category": cat, "in_matrix": False}
            )
            continue
        recs.append(
            {
                "gene": g,
                "ensembl_id": e,
                "category": cat,
                "in_matrix": True,
                "n_retinas": int(counts.shape[1]),
                "mean_cpm": float(mean_cpm.loc[e]),
                "median_cpm": float(med_cpm.loc[e]),
                "pct_samples_detected": float(detected.loc[e]),
                "abundance_pctile_all_features": float(pct_all.loc[e]),
                "abundance_pctile_expressed": (
                    float(pct_expr.loc[e]) if e in pct_expr.index else np.nan
                ),
            }
        )
    df = pd.DataFrame(recs)
    p = pathlib.Path(args.out_dir) / "retina_eyegex_abundance.tsv"
    df.to_csv(p, sep="\t", index=False)
    print(f"[ok] {p}  ({len(df):,} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
