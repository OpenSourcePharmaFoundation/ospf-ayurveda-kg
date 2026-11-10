"""Independent cross-check of the Census computation via the CELLxGENE WMG API.

The WMG ("where's my gene") API is the backend of CELLxGENE's Gene Expression
dot plot.  It aggregates the same corpus as the Census but server-side, with its
own normalisation (rankit rather than CP10K).  It therefore validates the
*fraction of cells expressing* computed in ``query_census.py`` -- that number is
normalisation-independent, so the two must agree -- without validating the
expression magnitudes, which are on different scales by construction.

v2 of the API has no tissue filter; results arrive for all tissues and are
filtered to ``UBERON:0000970`` (eye) here.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import subprocess
import tempfile

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from analysis.retina_expression.census_client import fix_proxy_env  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "data" / "processed"
API = "https://api.cellxgene.cziscience.com/wmg/v2"
EYE = "UBERON:0000970"

CHECK_GENES = [
    "PPARA",
    "PPARD",
    "PPARG",
    "RXRA",
    "RXRB",
    "RXRG",
    "TBP",
    "POLR2A",
    "HPRT1",
    "ACTB",
    "GAPDH",
    "RHO",
    "KDR",
    "FLT1",
    "NR2E3",
    "THRB",
    "RORB",
    "CPT1A",
    "ACOX1",
    "PDK4",
    "FABP5",
    "ANGPTL4",
    "ABCG1",
    "ALB",
    "INS",
    "PRM1",
    "MYH7",
]


def _curl(path: str, body: dict | None = None, retries: int = 3) -> dict:
    """Fetch via curl rather than urllib.

    Multi-megabyte responses through the sandbox proxy truncate under
    ``http.client`` (IncompleteRead).  curl negotiates the same proxy without
    the problem, and writing to a file avoids holding two copies in memory.
    """
    last = None
    for attempt in range(retries):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as fh:
            tmp = pathlib.Path(fh.name)
        cmd = ["curl", "-sS", "--fail", "--max-time", "600", "-o", str(tmp)]
        if body is not None:
            cmd += [
                "-X",
                "POST",
                "-H",
                "Content-Type: application/json",
                "--data-binary",
                json.dumps(body),
            ]
        cmd.append(f"{API}/{path}")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        try:
            if proc.returncode == 0:
                return json.loads(tmp.read_text())
            last = proc.stderr.strip()
        except json.JSONDecodeError as exc:
            last = str(exc)
        finally:
            tmp.unlink(missing_ok=True)
        print(f"[warn] {path} attempt {attempt + 1} failed: {last}", file=sys.stderr)
    raise RuntimeError(f"{path}: {last}")


def _post(path: str, body: dict) -> dict:
    return _curl(path, body)


def _get(path: str) -> dict:
    return _curl(path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(OUT_DIR))
    args = ap.parse_args()
    fix_proxy_env()
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    pfd = _get("primary_filter_dimensions")
    sym2ens = {}
    for d in pfd["gene_terms"]["NCBITaxon:9606"]:
        for ens, sym in d.items():
            sym2ens.setdefault(sym, ens)
    ids = [sym2ens[g] for g in CHECK_GENES if g in sym2ens]
    ens2sym = {sym2ens[g]: g for g in CHECK_GENES if g in sym2ens}
    print(f"[info] {len(ids)} genes resolved; snapshot {pfd['snapshot_id']}")

    recs = []
    for i in range(0, len(ids), 3):
        chunk = ids[i : i + 3]
        res = _post(
            "query",
            {
                "filter": {
                    "gene_ontology_term_ids": chunk,
                    "organism_ontology_term_id": "NCBITaxon:9606",
                },
                # is_rollup=False returns HTTP 500 from the v2 service, so the
                # cell-type ontology rollup is always on: parent terms include
                # their descendants.  Read leaf terms, not parents.
                "is_rollup": True,
            },
        )
        labels = res.get("term_id_labels", {}).get("cell_types", {})
        for gene_id, tissues in res["expression_summary"].items():
            eye = tissues.get(EYE)
            if not eye:
                continue
            for ct_id, strata in eye.items():
                agg = strata.get("aggregated")
                if not agg or ct_id == "tissue_stats":
                    continue
                recs.append(
                    {
                        "gene": ens2sym.get(gene_id, gene_id),
                        "cell_type_id": ct_id,
                        "n_cells_expressing": agg.get("n"),
                        "pct_cells_expressing": 100 * (agg.get("pc") or 0),
                        "mean_rankit_expressing": agg.get("me"),
                        "pct_of_tissue_cells": 100 * (agg.get("tpc") or 0),
                    }
                )
        print(f"[info] chunk {i // 3 + 1}: {len(recs):,} rows so far")

    df = pd.DataFrame(recs)
    lbl = {}
    for grp in labels.values() if isinstance(labels, dict) else []:
        pass
    # resolve cell type labels from the primary filter dimensions tissue-agnostic map
    try:
        f = _post(
            "filters",
            {
                "filter": {
                    "organism_ontology_term_id": "NCBITaxon:9606",
                    "tissue_ontology_term_ids": [EYE],
                }
            },
        )
        for d in f["filter_dims"]["cell_type_terms"]:
            lbl.update(d)
    except Exception as exc:  # pragma: no cover
        print(f"[warn] cell-type labels unavailable: {exc}", file=sys.stderr)
    df["cell_type"] = df.cell_type_id.map(lbl)
    path = out / "retina_wmg_crosscheck.tsv"
    df.sort_values(["gene", "cell_type"]).to_csv(path, sep="\t", index=False)
    print(f"[ok] {path}  ({len(df):,} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
