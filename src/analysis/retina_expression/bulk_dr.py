"""Retinal expression of the DR panel in diabetes: GSE160306.

GSE160306 (Becker et al. 2021, Sci Rep; Iowa eye bank donors) is bulk total-RNA
sequencing of macular and peripheral retina punches from 79 samples across four
donor groups: Control, Diabetic (diabetes without retinopathy), NPDR, and
NPDR + DME.  It is, as of this writing, the only public human *neural retina*
transcriptome series with a graded diabetic axis -- CZ CELLxGENE Census contains
zero diabetic retinal cells, and every public single-cell diabetic eye dataset
profiles fibrovascular membranes or blood rather than retina.

Design notes that matter for the result:

* Macula and periphery are analysed **separately**.  Most donors contribute one
  sample of each, so pooling them would double-count donors and inflate n.
* The primary contrast is Control vs any-retinopathy (NPDR + NPDR+DME).  The
  Diabetic-without-retinopathy group is reported but held out of that contrast,
  because it is the interesting intermediate, not a case or a control.
* A Spearman correlation against ``dr_severity_score`` is reported alongside,
  since a dose-response across severity is much harder to produce by chance than
  a two-group difference.
* Benjamini-Hochberg FDR is computed across the panel, within each site.

Usage:  python src/analysis/retina_expression/bulk_dr.py --work-dir DIR
"""

from __future__ import annotations

import argparse
import gzip
import pathlib
import sys
import urllib.request

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from analysis.retina_expression.census_client import fix_proxy_env  # noqa: E402
from analysis.retina_expression.gene_panel import all_genes  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_DIR = REPO / "data" / "processed"
GEO = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE160nnn/GSE160306"
COUNTS = "suppl/GSE160306_human_retina_DR_totalRNA_counts.txt.gz"
MATRIX = "matrix/GSE160306_series_matrix.txt.gz"

# Every group with diagnosed retinopathy.  "Diabetic" (diabetes, no retinopathy)
# is deliberately NOT a case: it is the intermediate the dose-response needs.
CASE_GROUPS = ("NPDR", "NPDR + DME", "PDR + DME")

# Ensembl IDs retired since the GSE160306 annotation was built.
LEGACY_IDS = {"SOD2": "ENSG00000112096"}


def fetch(work: pathlib.Path) -> tuple[pathlib.Path, pathlib.Path]:
    work.mkdir(parents=True, exist_ok=True)
    paths = []
    for rel in (COUNTS, MATRIX):
        p = work / pathlib.Path(rel).name
        if not p.exists():
            urllib.request.urlretrieve(f"{GEO}/{rel}", p)
        paths.append(p)
    return paths[0], paths[1]


def parse_metadata(matrix_path: pathlib.Path) -> pd.DataFrame:
    """Series-matrix characteristics are ragged: the Nth characteristics line
    holds a *different* key for different samples.  Parse every cell as
    ``key: value`` and assign by key, never by line position."""
    titles: list[str] = []
    rows: list[dict[str, str]] = []
    with gzip.open(matrix_path, "rt", errors="replace") as fh:
        for line in fh:
            if not line.startswith("!Sample_"):
                continue
            parts = [p.strip('"') for p in line.rstrip("\n").split("\t")]
            tag, vals = parts[0], parts[1:]
            if tag == "!Sample_title":
                titles = vals
                rows = [{"sample": t} for t in titles]
            elif tag == "!Sample_geo_accession":
                for r, v in zip(rows, vals):
                    r["gsm"] = v
            elif tag == "!Sample_characteristics_ch1":
                for r, v in zip(rows, vals):
                    if ": " in v:
                        k, _, val = v.partition(": ")
                        r[k.strip()] = val.strip()
    return pd.DataFrame(rows).set_index("sample")


def pooled_sd(a: np.ndarray, b: np.ndarray) -> float:
    na, nb = len(a), len(b)
    if na < 2 or nb < 2:
        return float("nan")
    return float(
        np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    )


def mde(
    a: np.ndarray, b: np.ndarray, alpha: float = 0.05, power: float = 0.80
) -> float:
    """Smallest log2 fold-change this comparison could have detected.

    A null result is only informative with this number attached: "no change"
    means nothing if the study could only have seen a 4-fold change.
    """
    sd = pooled_sd(a, b)
    if not np.isfinite(sd) or sd == 0:
        return float("nan")
    z_a = stats.norm.ppf(1 - alpha / 2)
    z_b = stats.norm.ppf(power)
    return float((z_a + z_b) * sd * np.sqrt(1 / len(a) + 1 / len(b)))


def bh(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    ok = ~np.isnan(p)
    out = np.full(p.shape, np.nan)
    if not ok.any():
        return out
    q = p[ok]
    n = len(q)
    order = np.argsort(q)
    ranked = q[order] * n / (np.arange(n) + 1)
    ranked = np.minimum.accumulate(ranked[::-1])[::-1]
    adj = np.empty(n)
    adj[order] = np.clip(ranked, 0, 1)
    out[ok] = adj
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work-dir", default=str(pathlib.Path.cwd() / "_gse160306"))
    ap.add_argument("--out-dir", default=str(OUT_DIR))
    args = ap.parse_args()
    work = pathlib.Path(args.work_dir)
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    fix_proxy_env()
    counts_p, matrix_p = fetch(work)
    meta = parse_metadata(matrix_p)
    counts = pd.read_csv(counts_p, index_col=0)
    counts.index = [i.split(".")[0] for i in counts.index]
    print(f"[info] counts {counts.shape}, metadata {meta.shape}")

    shared = [s for s in counts.columns if s in meta.index]
    counts = counts[shared]
    meta = meta.loc[shared]
    print(f"[info] samples matched: {len(shared)}")
    print(meta.groupby(["sample_site", "disease_group_detailed"]).size().to_string())

    # counts -> CPM -> log2
    lib = counts.sum(axis=0)
    cpm = counts.div(lib, axis=1) * 1e6
    log2cpm = np.log2(cpm + 1)

    genes = all_genes()
    # map ensembl -> symbol via the census var axis is overkill here; use a
    # static lookup fetched from Ensembl REST once and cached.
    sym = symbol_map(work, sorted(genes))
    for symbol, legacy in LEGACY_IDS.items():
        if symbol in genes and legacy in log2cpm.index:
            sym[legacy] = symbol
    present = {e: s for e, s in sym.items() if e in log2cpm.index}
    missing = sorted(set(genes) - set(present.values()))
    if missing:
        print(f"[warn] not in GSE160306 count matrix: {missing}", file=sys.stderr)

    # percentile of each panel gene among all genes, per site (abundance context)
    recs = []
    for site in sorted(meta.sample_site.unique()):
        m = meta[meta.sample_site == site]
        ctrl = m.index[m.disease_group_detailed == "Control"]
        case = m.index[m.disease_group_detailed.isin(CASE_GROUPS)]
        diab = m.index[m.disease_group_detailed == "Diabetic"]
        sev = pd.to_numeric(m.dr_severity_score, errors="coerce")
        site_mean = cpm[m.index].mean(axis=1)
        pct = site_mean.rank(pct=True) * 100
        # Percentile over all 58k annotated features is inflated by the many
        # never-expressed lncRNA/pseudogene rows; rank among expressed features
        # (mean CPM >= 1) as well, which is the honest abundance statement.
        expressed = site_mean[site_mean >= 1]
        pct_expr = expressed.rank(pct=True) * 100
        for ens, s in present.items():
            v = log2cpm.loc[ens]
            a, b = v[ctrl].to_numpy(), v[case].to_numpy()
            try:
                u_p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
            except ValueError:
                u_p = np.nan
            sm = sev.notna()
            rho, rho_p = (np.nan, np.nan)
            if sm.sum() >= 6:
                rho, rho_p = stats.spearmanr(sev[sm], v[m.index[sm]])
            recs.append(
                {
                    "site": site,
                    "gene": s,
                    "ensembl_id": ens,
                    "category": genes[s],
                    "n_control": len(ctrl),
                    "n_diabetic_no_dr": len(diab),
                    "n_dr": len(case),
                    "mean_cpm_control": float(cpm.loc[ens, ctrl].mean()),
                    "mean_cpm_diabetic_no_dr": float(cpm.loc[ens, diab].mean()),
                    "mean_cpm_dr": float(cpm.loc[ens, case].mean()),
                    "abundance_pctile_all_features": float(pct.loc[ens]),
                    "abundance_pctile_expressed": (
                        float(pct_expr.loc[ens])
                        if ens in pct_expr.index
                        else float("nan")
                    ),
                    "sd_log2cpm_pooled": float(pooled_sd(a, b)),
                    "min_detectable_log2fc_80pct": float(mde(a, b)),
                    "log2fc_dr_vs_control": float(b.mean() - a.mean()),
                    "mwu_p": u_p,
                    "spearman_rho_severity": rho,
                    "spearman_p_severity": rho_p,
                }
            )
    df = pd.DataFrame(recs)
    for site, idx in df.groupby("site").groups.items():
        df.loc[idx, "mwu_fdr"] = bh(df.loc[idx, "mwu_p"].to_numpy())
        df.loc[idx, "spearman_fdr"] = bh(df.loc[idx, "spearman_p_severity"].to_numpy())
    path = out / "retina_bulk_dr_expression.tsv"
    df.sort_values(["site", "gene"]).to_csv(path, sep="\t", index=False)
    print(f"[ok] {path}  ({len(df):,} rows)")

    meta_out = out / "retina_bulk_dr_samples.tsv"
    keep = [
        c
        for c in [
            "gsm",
            "disease_group_detailed",
            "sample_site",
            "donor",
            "dr_severity_score",
            "dme",
            "age",
            "gender",
            "rin",
            "post_mortem_interval",
            "duration_diabetis",
        ]
        if c in meta.columns
    ]
    meta[keep].to_csv(meta_out, sep="\t")
    print(f"[ok] {meta_out}  ({len(meta):,} rows)")
    return 0


def symbol_map(work: pathlib.Path, symbols: list[str]) -> dict[str, str]:
    """symbol -> ensembl gene id, via Ensembl REST, cached on disk."""
    import json

    cache = work / "symbol_map.json"
    if cache.exists():
        return json.loads(cache.read_text())
    url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens"
    req = urllib.request.Request(
        url,
        data=json.dumps({"symbols": symbols}).encode(),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    out = {v["id"]: k for k, v in data.items() if isinstance(v, dict) and "id" in v}
    cache.write_text(json.dumps(out))
    return out


if __name__ == "__main__":
    raise SystemExit(main())
