"""Which retina datasets could have detected these genes at all.

Separates the two claims the task insists on keeping apart:

  * **absent** - the gene is not in that dataset's feature space.  The assay or
    the submitter's filtering removed it; a zero there is not evidence of
    anything biological.
  * **below detection threshold** - the gene was measurable in that dataset and
    was observed in zero (or few) cells.

Census stores this as ``feature_dataset_presence_matrix``.  Reading it needs no
expression-matrix traffic, so this runs in a minute where the full per-cell
query takes an hour.

Usage:  python src/analysis/retina_expression/census_presence.py
"""

from __future__ import annotations

import argparse
import pathlib
import sys

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from analysis.retina_expression.census_client import (
    CENSUS_VERSION,
    open_census,
)  # noqa: E402
from analysis.retina_expression.gene_panel import all_genes  # noqa: E402
from analysis.retina_expression.query_census import (
    RETINA_TISSUES,
    _obs_filter,
)  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "data" / "processed"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(OUT_DIR))
    ap.add_argument("--census-version", default=CENSUS_VERSION)
    args = ap.parse_args()
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    genes = all_genes()
    symbols = sorted(genes)

    census = open_census(args.census_version)
    try:
        h = census["census_data"]["homo_sapiens"]
        var = (
            h.ms["RNA"]
            .var.read(
                value_filter=f"feature_name in {symbols!r}",
                column_names=["soma_joinid", "feature_id", "feature_name"],
            )
            .concat()
            .to_pandas()
        )
        obs = (
            h.obs.read(
                value_filter=_obs_filter(),
                column_names=[
                    "dataset_id",
                    "assay",
                    "suspension_type",
                    "disease",
                    "development_stage",
                    "tissue",
                    "donor_id",
                    "cell_type",
                    "raw_sum",
                    "nnz",
                ],
            )
            .concat()
            .to_pandas()
        )
        print(
            f"[info] retina cells (primary): {len(obs):,} "
            f"across {obs.dataset_id.nunique()} datasets"
        )

        ds = census["census_info"]["datasets"].read().concat().to_pandas()
        retina_ds = sorted(obs.dataset_id.unique())
        g = obs.groupby("dataset_id", observed=True)
        prov = pd.DataFrame(
            {
                "retina_cells_used": g.size(),
                "n_donors": g.donor_id.nunique(),
                "n_cell_types": g.cell_type.nunique(),
                "assays": g.assay.agg(lambda s: ";".join(sorted(set(s)))),
                "suspension": g.suspension_type.agg(lambda s: ";".join(sorted(set(s)))),
                "diseases": g.disease.agg(lambda s: ";".join(sorted(set(s)))),
                "development_stages": g.development_stage.agg(
                    lambda s: ";".join(sorted(set(s))[:4])
                ),
                "tissues": g.tissue.agg(lambda s: ";".join(sorted(set(s)))),
                "median_genes_per_cell": g.nnz.median(),
                "median_umis_per_cell": g.raw_sum.median(),
            }
        )
        prov = ds[ds.dataset_id.isin(retina_ds)].merge(
            prov, left_on="dataset_id", right_index=True, how="right"
        )
        p = out / "retina_sc_datasets.tsv"
        prov.sort_values("retina_cells_used", ascending=False).to_csv(
            p, sep="\t", index=False
        )
        print(f"[ok] {p}  ({len(prov):,} datasets)")

        fp = h.ms["RNA"]["feature_dataset_presence_matrix"]
        pres = (
            fp.read((slice(None), var.soma_joinid.to_numpy()))
            .tables()
            .concat()
            .to_pandas()
        )
        pres = pres[pres.soma_data.astype(bool)]
        dsjid = dict(zip(ds.soma_joinid, ds.dataset_id))
        gname = dict(zip(var.soma_joinid, var.feature_name))
        have = {
            (dsjid.get(a), gname.get(b))
            for a, b in zip(pres.soma_dim_0, pres.soma_dim_1)
        }
        rows = [
            {
                "dataset_id": d,
                "gene": gene,
                "category": genes[gene],
                "in_feature_space": (d, gene) in have,
            }
            for d in retina_ds
            for gene in sorted(var.feature_name)
        ]
        df = pd.DataFrame(rows)
        p = out / "retina_sc_gene_presence.tsv"
        df.to_csv(p, sep="\t", index=False)
        print(f"[ok] {p}  ({len(df):,} rows)")
        miss = df[~df.in_feature_space].groupby("gene").size()
        print(
            f"[info] genes absent from >=1 retina dataset's feature space: {len(miss)}"
        )
        if len(miss):
            print(miss.sort_values(ascending=False).head(25).to_string())
    finally:
        census.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
