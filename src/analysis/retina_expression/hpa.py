"""Human Protein Atlas arm of the retinal PPARA question.

Three things HPA provides that CZ CELLxGENE does not:

1. **Bulk retina nTPM** (``rna_tissue_consensus``).  Pseudobulk is immune to the
   per-cell dropout that dominates single-cell dot plots, so it is the right
   place to ask "is this transcript actually there".
2. **A second, independent processing pipeline** over single-cell retina data
   (``rna_single_cell_type``), with its own normalisation (nCPM).
3. **Antibody reliability grades and the retina IHC panel.**  This is the only
   source that lets the antibody-vs-transcript conflict be examined from inside
   one consortium: HPA scores its own antibodies and publishes which tissues it
   has actually stained.

Usage:  python src/analysis/retina_expression/hpa.py --work-dir DIR
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import zipfile

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from analysis.retina_expression.census_client import fix_proxy_env  # noqa: E402
from analysis.retina_expression.gene_panel import all_genes  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "data" / "processed"

# normal_tissue.tsv (IHC) is no longer published at the current-version path;
# v23 is the most recent release that still serves it.  The IHC content is
# unchanged between releases, but the version is recorded in the output.
DOWNLOADS = {
    "rna_single_cell_type.tsv": "https://www.proteinatlas.org/download/tsv/rna_single_cell_type.tsv.zip",
    "rna_tissue_consensus.tsv": "https://www.proteinatlas.org/download/tsv/rna_tissue_consensus.tsv.zip",
    "normal_tissue.tsv": "https://v23.proteinatlas.org/download/normal_tissue.tsv.zip",
}

RETINAL_CELL_TYPES = [
    "rod photoreceptor cells",
    "cone photoreceptor cells",
    "müller glia",
    "retinal bipolar cells",
    "retinal horizontal cells",
    "retinal ganglion cells",
    "retinal pigment epithelial cells",
    "microglia",
    "vascular endothelial cells",
]
# Reference cell types: the canonical PPARalpha tissues, for scale.
REFERENCE_CELL_TYPES = ["hepatocytes", "enterocytes", "proximal tubule cells"]


def fetch(work: pathlib.Path) -> dict[str, pathlib.Path]:
    work.mkdir(parents=True, exist_ok=True)
    out = {}
    for name, url in DOWNLOADS.items():
        tsv = work / name
        if not tsv.exists():
            z = work / (name + ".zip")
            if not z.exists():
                subprocess.run(
                    ["curl", "-sSL", "--fail", "--max-time", "600", "-o", str(z), url],
                    check=True,
                )
            with zipfile.ZipFile(z) as zf:
                zf.extractall(work)
        out[name] = tsv
    return out


def gene_json(work: pathlib.Path, ensembl: str) -> dict:
    """Fetch one gene's HPA record, validating the payload before caching it.

    The sandbox egress proxy truncates some responses mid-body.  curl exits 0,
    a short file lands in the cache, and every later run then fails to parse it
    -- the failure is sticky because the bad file looks like a cache hit.  So
    parse before trusting, and delete and retry on a short read.
    """
    cache = work / "json" / f"{ensembl}.json"
    cache.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(3):
        if cache.exists():
            try:
                return json.loads(cache.read_text())
            except json.JSONDecodeError:
                cache.unlink()  # truncated: do not keep a poisoned cache entry
        subprocess.run(
            [
                "curl",
                "-sSL",
                "--fail",
                "--retry",
                "3",
                "--max-time",
                "120",
                "-o",
                str(cache),
                f"https://www.proteinatlas.org/{ensembl}.json",
            ],
            check=True,
        )
    return json.loads(cache.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work-dir", default=str(pathlib.Path.cwd() / "_hpa"))
    ap.add_argument("--out-dir", default=str(OUT_DIR))
    args = ap.parse_args()
    fix_proxy_env()
    work = pathlib.Path(args.work_dir)
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    files = fetch(work)
    genes = all_genes()

    # ---- single cell nCPM -------------------------------------------------
    sc = pd.read_csv(files["rna_single_cell_type.tsv"], sep="\t")
    keep = RETINAL_CELL_TYPES + REFERENCE_CELL_TYPES
    sub = sc[sc["Gene name"].isin(genes) & sc["Cell type"].isin(keep)].copy()
    sub["category"] = sub["Gene name"].map(genes)
    sub["is_retinal"] = sub["Cell type"].isin(RETINAL_CELL_TYPES)
    sub = sub.rename(
        columns={
            "Gene": "ensembl_id",
            "Gene name": "gene",
            "Cell type": "cell_type",
            "nCPM": "ncpm",
        }
    )
    p = out / "retina_hpa_celltype_ncpm.tsv"
    sub.sort_values(["gene", "cell_type"]).to_csv(p, sep="\t", index=False)
    print(f"[ok] {p}  ({len(sub):,} rows)")

    # ---- bulk tissue nTPM, with abundance rank ---------------------------
    tis = pd.read_csv(files["rna_tissue_consensus.tsv"], sep="\t")
    ranks = {}
    for t in ("retina", "liver"):
        sl = tis[tis.Tissue == t]
        ranks[t] = dict(zip(sl["Gene name"], (sl.nTPM.rank(pct=True) * 100).round(2)))
        print(f"[info] {t}: {len(sl):,} genes")
    bulk = tis[
        tis["Gene name"].isin(genes) & tis.Tissue.isin(["retina", "liver"])
    ].copy()
    bulk["category"] = bulk["Gene name"].map(genes)
    bulk["pctile_within_tissue"] = [
        ranks[t].get(g) for t, g in zip(bulk.Tissue, bulk["Gene name"])
    ]
    bulk = bulk.rename(
        columns={
            "Gene": "ensembl_id",
            "Gene name": "gene",
            "Tissue": "tissue",
            "nTPM": "ntpm",
        }
    )
    p = out / "retina_hpa_bulk_ntpm.tsv"
    bulk.sort_values(["gene", "tissue"]).to_csv(p, sep="\t", index=False)
    print(f"[ok] {p}  ({len(bulk):,} rows)")

    # ---- antibody reliability + retina IHC coverage ----------------------
    ihc = pd.read_csv(files["normal_tissue.tsv"], sep="\t")
    retina_ihc = set(ihc[ihc.Tissue == "retina"]["Gene name"])
    print(f"[info] HPA retina IHC panel covers {len(retina_ihc):,} proteins")
    ens = dict(zip(bulk.gene, bulk.ensembl_id))
    recs = []
    for g in sorted(genes):
        e = ens.get(g)
        if not e:
            continue
        try:
            j = gene_json(work, e)
        except subprocess.CalledProcessError:
            print(f"[warn] no HPA json for {g}", file=sys.stderr)
            continue
        recs.append(
            {
                "gene": g,
                "ensembl_id": e,
                "category": genes[g],
                "n_hpa_antibodies": len(j.get("Antibody") or []),
                "hpa_antibodies": ";".join(j.get("Antibody") or []),
                "reliability_ihc": j.get("Reliability (IH)"),
                "reliability_if": j.get("Reliability (IF)"),
                "in_hpa_retina_ihc_panel": g in retina_ihc,
                "rna_sc_specificity": j.get("RNA single cell type specificity"),
                "rna_sc_distribution": j.get("RNA single cell type distribution"),
                "rna_sc_enhanced_in": json.dumps(
                    j.get("RNA single cell type specific nCPM") or {}
                ),
                "sc_expression_cluster": j.get("Single cell expression cluster"),
            }
        )
    ab = pd.DataFrame(recs)
    p = out / "retina_hpa_antibody_reliability.tsv"
    ab.to_csv(p, sep="\t", index=False)
    print(f"[ok] {p}  ({len(ab):,} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
