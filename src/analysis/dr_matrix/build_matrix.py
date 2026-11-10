#!/usr/bin/env python3
"""
Regenerate the compound-target matrix for the diabetic-retinopathy (DR)
gene panel as a binding-evidence matrix, built from ChEMBL bioactivity data
(see src/scrapers/chembl/chembl_target_axis.py) rather than the original
Comparative Toxicogenomics Database (CTD) study-count matrix.

The original matrix (data/reports/disease-explorer/diabetic-retinopathy/
2026-10-05/evidence/compound-dr-target-matrix.tsv) is READ ONLY here - it is
never modified. CTD can no longer be queried programmatically (the batch
query endpoint now redirects to a captcha page), so this module cannot be a
like-for-like CTD rebuild. Instead it builds the scientifically preferable
substrate: real ChEMBL binding affinities (IC50/EC50/Ki/Kd) rather than
co-occurrence/study-volume counts.

Outputs (data/processed/):
  dr_compound_target_matrix.tsv              - binding-evidence matrix, all
                                                43-gene-panel compounds
  dr_matrix_legacy_compound_comparison.tsv   - apples-to-apples CTD vs ChEMBL
                                                comparison for the compounds
                                                named in the original matrix
  dr_panel_coverage_summary.tsv              - per-gene pharmacology coverage
"""

import argparse
import csv
import os
import sys
import time
from datetime import date
from typing import Dict, List, Optional

import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

ORIGINAL_MATRIX_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "reports",
    "disease-explorer",
    "diabetic-retinopathy",
    "2026-10-05",
    "evidence",
    "compound-dr-target-matrix.tsv",
)

GENE_PANEL_PATH = os.path.join(DATA_DIR, "dr_gene_panel.csv")
TARGETS_PATH = os.path.join(DATA_DIR, "chembl_panel_targets.csv")
BIOACTIVITIES_PATH = os.path.join(DATA_DIR, "chembl_panel_bioactivities.csv")

CHEMBL_SEARCH_URL = "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json"
RATE_LIMIT_DELAY = 0.3

GENERATION_DATE = date.today().isoformat()

# Conventional "active" cut: pchembl_value >= 6 <=> IC50/EC50/Ki/Kd <= 1 uM.
PCHEMBL_GATE = 6.0


def read_tsv_rows(path, skip_comments=True):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for line in f:
            if skip_comments and line.startswith("#"):
                continue
            rows.append(line.rstrip("\n"))
    reader = csv.DictReader(rows, delimiter="\t")
    return list(reader)


def load_gene_panel():
    rows = {}
    with open(GENE_PANEL_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows[row["gene"]] = row
    return rows


def load_targets():
    rows = {}
    with open(TARGETS_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows[row["gene"]] = row
    return rows


def load_bioactivities():
    with open(BIOACTIVITIES_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def _to_float(value):
    try:
        if value in (None, ""):
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def load_original_matrix_compounds():
    """Returns dict: compound_name -> {n_targets, genes_set}."""
    rows = read_tsv_rows(ORIGINAL_MATRIX_PATH)
    compounds = {}
    all_genes = set()
    for row in rows:
        genes = set(g for g in row["targets"].split(",") if g)
        compounds[row["compound"]] = {
            "ctd_n_targets_27panel": row["n_targets"],
            "genes": genes,
        }
        all_genes |= genes
    return compounds, all_genes


def search_chembl_by_name(name):
    """Fallback molecule lookup via /molecule/search.json. Returns molecule_chembl_id or None."""
    try:
        resp = requests.get(
            CHEMBL_SEARCH_URL, params={"q": name, "limit": 1}, timeout=30
        )
        time.sleep(RATE_LIMIT_DELAY)
    except requests.exceptions.RequestException as e:
        print(f"ERROR ChEMBL search request failed for {name!r}: {e}")
        return None

    if resp.status_code != 200:
        return None

    data = resp.json()
    molecules = data.get("molecules", [])
    if not molecules:
        return None
    return molecules[0].get("molecule_chembl_id")


def header_block(title, means, not_means, extra_notes=None):
    lines = [f"# {title}"]
    lines.append("# WHAT THE NUMBERS MEAN:")
    for m in means:
        lines.append(f"#   - {m}")
    lines.append("# WHAT THEY DO NOT MEAN:")
    for m in not_means:
        lines.append(f"#   - {m}")
    if extra_notes:
        for n in extra_notes:
            lines.append(f"# {n}")
    lines.append(
        "# SOURCE: ChEMBL REST API (https://www.ebi.ac.uk/chembl/api/data), live pull."
    )
    lines.append(f"# GENERATED: {GENERATION_DATE}")
    lines.append(
        "# WARNING: absence of a ChEMBL activity for a gene/compound pair means "
        '"not measured in ChEMBL", NOT "no interaction".'
    )
    return lines


def write_tsv_with_header(path, header_lines, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        for line in header_lines:
            f.write(line + "\n")
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def build_output_a(bioactivities, gene_panel):
    """Output A: binding-evidence matrix for every compound in the panel bioactivities."""
    effector_genes = {
        g for g, row in gene_panel.items() if row.get("role") == "ppar_effector"
    }

    by_compound: Dict[str, Dict] = {}
    for act in bioactivities:
        mol_id = act["molecule_chembl_id"]
        if not mol_id:
            continue
        gene = act["gene"]
        pchembl = _to_float(act.get("pchembl_value"))

        entry = by_compound.setdefault(
            mol_id,
            {
                "compound_name": act.get("molecule_pref_name", ""),
                "gene_best_pchembl": {},
            },
        )
        if not entry["compound_name"] and act.get("molecule_pref_name"):
            entry["compound_name"] = act["molecule_pref_name"]

        current_best = entry["gene_best_pchembl"].get(gene)
        if pchembl is not None and (current_best is None or pchembl > current_best):
            entry["gene_best_pchembl"][gene] = pchembl
        elif gene not in entry["gene_best_pchembl"]:
            entry["gene_best_pchembl"][
                gene
            ] = None  # bound but no pchembl value recorded

    rows = []
    for mol_id, entry in by_compound.items():
        gene_scores = entry["gene_best_pchembl"]
        n_genes_bound = len(gene_scores)
        n_effector_genes_bound = len(set(gene_scores.keys()) & effector_genes)
        numeric_scores = [v for v in gene_scores.values() if v is not None]
        best_pchembl = max(numeric_scores) if numeric_scores else None

        gated_genes = {
            g for g, v in gene_scores.items() if v is not None and v >= PCHEMBL_GATE
        }
        n_genes_bound_pchembl_ge6 = len(gated_genes)
        n_effectors_bound_pchembl_ge6 = len(gated_genes & effector_genes)

        genes_str = ",".join(
            f"{g}:{gene_scores[g]:.2f}" if gene_scores[g] is not None else f"{g}:NA"
            for g in sorted(gene_scores.keys())
        )

        rows.append(
            {
                "compound_chembl_id": mol_id,
                "compound_name": entry["compound_name"],
                "n_genes_bound": n_genes_bound,
                "n_effector_genes_bound": n_effector_genes_bound,
                "n_genes_bound_pchembl_ge6": n_genes_bound_pchembl_ge6,
                "n_effectors_bound_pchembl_ge6": n_effectors_bound_pchembl_ge6,
                "best_pchembl": (
                    f"{best_pchembl:.2f}" if best_pchembl is not None else ""
                ),
                "genes": genes_str,
            }
        )

    rows.sort(
        key=lambda r: (
            -r["n_genes_bound_pchembl_ge6"],
            -(float(r["best_pchembl"]) if r["best_pchembl"] else -1),
            -r["n_genes_bound"],
        )
    )
    return rows


def build_output_b(original_compounds, bioactivities, gene_panel):
    """Output B: apples-to-apples comparison for every compound in the original matrix."""
    effector_genes = {
        g for g, row in gene_panel.items() if row.get("role") == "ppar_effector"
    }

    # molecule_pref_name (lowercased) -> molecule_chembl_id, from panel bioactivities
    pref_name_lookup = {}
    for act in bioactivities:
        name = (act.get("molecule_pref_name") or "").strip().lower()
        if name and name not in pref_name_lookup:
            pref_name_lookup[name] = act["molecule_chembl_id"]

    # Pre-aggregate bioactivities by molecule_chembl_id
    by_molecule: Dict[str, List[Dict]] = {}
    for act in bioactivities:
        by_molecule.setdefault(act["molecule_chembl_id"], []).append(act)

    rows = []
    for compound_name, info in original_compounds.items():
        matched_id = None
        match_method = "unmatched"

        lookup_key = compound_name.strip().lower()
        if lookup_key in pref_name_lookup:
            matched_id = pref_name_lookup[lookup_key]
            match_method = "exact_pref_name"
        else:
            found_id = search_chembl_by_name(compound_name)
            if found_id:
                matched_id = found_id
                match_method = "chembl_search"

        if matched_id is None:
            rows.append(
                {
                    "compound": compound_name,
                    "ctd_n_targets_27panel": info["ctd_n_targets_27panel"],
                    "chembl_n_genes_bound_43panel": "",
                    "chembl_n_effectors_bound": "",
                    "chembl_n_genes_bound_pchembl_ge6": "",
                    "chembl_n_effectors_bound_pchembl_ge6": "",
                    "chembl_best_pchembl": "",
                    "matched_chembl_id": "",
                    "match_method": match_method,
                }
            )
            continue

        acts = by_molecule.get(matched_id, [])
        genes_bound = {a["gene"] for a in acts}
        n_effectors = len(genes_bound & effector_genes)

        gene_best_pchembl: Dict[str, Optional[float]] = {}
        for a in acts:
            pchembl = _to_float(a.get("pchembl_value"))
            if pchembl is None:
                continue
            gene = a["gene"]
            if gene not in gene_best_pchembl or pchembl > gene_best_pchembl[gene]:
                gene_best_pchembl[gene] = pchembl

        pchembl_values = list(gene_best_pchembl.values())
        best_pchembl = max(pchembl_values) if pchembl_values else None

        gated_genes = {g for g, v in gene_best_pchembl.items() if v >= PCHEMBL_GATE}
        n_genes_gated = len(gated_genes)
        n_effectors_gated = len(gated_genes & effector_genes)

        rows.append(
            {
                "compound": compound_name,
                "ctd_n_targets_27panel": info["ctd_n_targets_27panel"],
                "chembl_n_genes_bound_43panel": len(genes_bound),
                "chembl_n_effectors_bound": n_effectors,
                "chembl_n_genes_bound_pchembl_ge6": n_genes_gated,
                "chembl_n_effectors_bound_pchembl_ge6": n_effectors_gated,
                "chembl_best_pchembl": (
                    f"{best_pchembl:.2f}" if best_pchembl is not None else ""
                ),
                "matched_chembl_id": matched_id,
                "match_method": match_method,
            }
        )

    return rows


def build_output_c(gene_panel, targets, bioactivities, original_27_genes):
    by_gene: Dict[str, List[Dict]] = {}
    for act in bioactivities:
        by_gene.setdefault(act["gene"], []).append(act)

    rows = []
    for gene, panel_row in gene_panel.items():
        target_row = targets.get(gene, {})
        acts = by_gene.get(gene, [])
        n_distinct_compounds = len(
            {a["molecule_chembl_id"] for a in acts if a["molecule_chembl_id"]}
        )

        # Best pchembl per compound for this gene, for the gated distinct-compound count
        compound_best_pchembl: Dict[str, float] = {}
        for a in acts:
            mol_id = a.get("molecule_chembl_id")
            pchembl = _to_float(a.get("pchembl_value"))
            if not mol_id or pchembl is None:
                continue
            if (
                mol_id not in compound_best_pchembl
                or pchembl > compound_best_pchembl[mol_id]
            ):
                compound_best_pchembl[mol_id] = pchembl

        max_pchembl = (
            max(compound_best_pchembl.values()) if compound_best_pchembl else None
        )
        n_distinct_compounds_gated = sum(
            1 for v in compound_best_pchembl.values() if v >= PCHEMBL_GATE
        )

        rows.append(
            {
                "gene": gene,
                "role": panel_row.get("role", ""),
                "axis": panel_row.get("axis", ""),
                "chembl_target_id": target_row.get("chembl_target_id", ""),
                "n_activities_raw": target_row.get("n_activities_raw", ""),
                "n_activities_filtered": target_row.get("n_activities_filtered", ""),
                "n_distinct_compounds": n_distinct_compounds,
                "n_distinct_compounds_pchembl_ge6": n_distinct_compounds_gated,
                "max_pchembl": f"{max_pchembl:.2f}" if max_pchembl is not None else "",
                "in_original_27_panel": "yes" if gene in original_27_genes else "no",
            }
        )

    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Build the ChEMBL binding-evidence DR compound-target matrix"
    )
    args = parser.parse_args()

    gene_panel = load_gene_panel()
    targets = load_targets()
    bioactivities = load_bioactivities()
    original_compounds, original_27_genes = load_original_matrix_compounds()

    print(
        f"Original matrix: {len(original_compounds)} compounds, {len(original_27_genes)} genes"
    )

    # Output A
    rows_a = build_output_a(bioactivities, gene_panel)
    header_a = header_block(
        "dr_compound_target_matrix.tsv - ChEMBL binding-evidence matrix (DR 43-gene panel)",
        means=[
            "n_genes_bound: number of distinct panel genes with at least one qualifying "
            "ChEMBL activity (IC50/EC50/Ki/Kd, nM) for this compound, AT ANY POTENCY.",
            f"n_genes_bound_pchembl_ge6 / n_effectors_bound_pchembl_ge6: the same counts "
            f"gated to pchembl_value >= {PCHEMBL_GATE:g} (<= 1 uM), the conventional "
            f"'active' cut. Rows are sorted by this gated count first.",
            "best_pchembl: the highest pchembl_value (-log10 molar potency) observed for "
            "this compound across any bound gene; higher = more potent.",
            "genes: comma-separated SYMBOL:<best pchembl for that gene> pairs, 'NA' where "
            "an activity exists but no pchembl_value was computed.",
        ],
        not_means=[
            "This is NOT a CTD-style literature co-occurrence count - it is measured "
            "binding/functional affinity data.",
            "Absence from this file means the compound had no qualifying ChEMBL activity "
            "against ANY of the 43 panel genes - it does not mean no interaction exists.",
            f"An UNGATED 'bound' (n_genes_bound) can be as weak as >100 uM - it only means "
            f"ChEMBL recorded a qualifying IC50/EC50/Ki/Kd measurement, not that it is a "
            f"meaningful binder. Use the pchembl_ge6 columns for potency-aware ranking.",
            "Rows lacking a pchembl_value for a gene ('NA' in the genes column) are "
            "EXCLUDED from the gated counts - this is missing/unconverted unit data, not "
            "evidence of weak binding.",
        ],
    )
    write_tsv_with_header(
        os.path.join(DATA_DIR, "dr_compound_target_matrix.tsv"),
        header_a,
        [
            "compound_chembl_id",
            "compound_name",
            "n_genes_bound",
            "n_effector_genes_bound",
            "n_genes_bound_pchembl_ge6",
            "n_effectors_bound_pchembl_ge6",
            "best_pchembl",
            "genes",
        ],
        rows_a,
    )

    # Output B
    rows_b = build_output_b(original_compounds, bioactivities, gene_panel)
    header_b = header_block(
        "dr_matrix_legacy_compound_comparison.tsv - CTD vs ChEMBL ranking comparison",
        means=[
            "ctd_n_targets_27panel: the original CTD study-volume count (27-gene panel) "
            "from the 2026-10-05 compound-dr-target-matrix.tsv (read-only, not modified).",
            "chembl_n_genes_bound_43panel / chembl_n_effectors_bound / chembl_best_pchembl: "
            "measured ChEMBL binding evidence for the matched compound against the "
            "extended 43-gene panel, AT ANY POTENCY.",
            f"chembl_n_genes_bound_pchembl_ge6 / chembl_n_effectors_bound_pchembl_ge6: the "
            f"same counts gated to pchembl_value >= {PCHEMBL_GATE:g} (<= 1 uM), the "
            f"conventional 'active' cut.",
            "match_method: how the compound name was resolved to a ChEMBL molecule id "
            "(exact_pref_name, chembl_search, or unmatched).",
        ],
        not_means=[
            "Empty numeric fields mean the compound could NOT be matched to a ChEMBL "
            "molecule id - this is absence of a match, not a measured zero. Do not treat "
            "blank as 0.",
            "A low chembl_n_genes_bound_43panel does not mean the compound lacks "
            "pharmacological activity - it means ChEMBL has not measured it against "
            "these specific targets.",
            f"An UNGATED chembl_n_genes_bound_43panel can be as weak as >100 uM - use the "
            f"pchembl_ge6 columns for potency-aware comparison.",
            "Rows lacking a pchembl_value for a gene are EXCLUDED from the gated counts - "
            "this is missing/unconverted unit data, not evidence of weak binding.",
        ],
    )
    write_tsv_with_header(
        os.path.join(DATA_DIR, "dr_matrix_legacy_compound_comparison.tsv"),
        header_b,
        [
            "compound",
            "ctd_n_targets_27panel",
            "chembl_n_genes_bound_43panel",
            "chembl_n_effectors_bound",
            "chembl_n_genes_bound_pchembl_ge6",
            "chembl_n_effectors_bound_pchembl_ge6",
            "chembl_best_pchembl",
            "matched_chembl_id",
            "match_method",
        ],
        rows_b,
    )

    # Output C
    rows_c = build_output_c(gene_panel, targets, bioactivities, original_27_genes)
    header_c = header_block(
        "dr_panel_coverage_summary.tsv - per-gene ChEMBL pharmacology coverage (DR 43-gene panel)",
        means=[
            "n_activities_raw: the ChEMBL API's raw total_count for "
            "target_chembl_id + standard_type__in=IC50,EC50,Ki,Kd + standard_units=nM - "
            "i.e. everything ChEMBL holds for this target under that type/unit filter.",
            "n_activities_filtered: the subset of n_activities_raw that survives the "
            "additional standard_value-not-null and data_validity_comment-null filter - "
            "this is what was actually written to chembl_panel_bioactivities.csv and what "
            "every downstream number (including this file's own n_distinct_compounds and "
            "max_pchembl) is computed from.",
            "n_distinct_compounds: number of distinct ChEMBL molecules with a qualifying "
            "(filtered) activity against this gene's target, AT ANY POTENCY.",
            f"n_distinct_compounds_pchembl_ge6: the same count gated to pchembl_value >= "
            f"{PCHEMBL_GATE:g} (<= 1 uM), the conventional 'active' cut.",
            "max_pchembl: the single highest pchembl_value observed for this gene.",
            "in_original_27_panel: whether this gene was part of the original CTD-based "
            "27-gene panel (yes/no).",
        ],
        not_means=[
            "An empty chembl_target_id or zero n_activities_filtered means this gene's "
            "pharmacology has not been resolved or measured in ChEMBL - it is a real "
            "finding, not an error, and does not mean the gene is not druggable.",
            "n_activities_raw > 0 with n_activities_filtered == 0 does NOT mean ChEMBL has "
            "no data for this gene - it means every raw record was flagged invalid or had "
            "no usable value (e.g. ACADM: 1 raw record, a 185,710 nM Kd flagged 'Outside "
            "typical range', correctly dropped).",
            f"An UNGATED n_distinct_compounds can be driven entirely by weak (>100 uM) "
            f"binders - use n_distinct_compounds_pchembl_ge6 for potency-aware coverage.",
        ],
    )
    write_tsv_with_header(
        os.path.join(DATA_DIR, "dr_panel_coverage_summary.tsv"),
        header_c,
        [
            "gene",
            "role",
            "axis",
            "chembl_target_id",
            "n_activities_raw",
            "n_activities_filtered",
            "n_distinct_compounds",
            "n_distinct_compounds_pchembl_ge6",
            "max_pchembl",
            "in_original_27_panel",
        ],
        rows_c,
    )

    # Print summary
    total_compounds = len(rows_a)
    binds_effector = sum(1 for r in rows_a if r["n_effector_genes_bound"] > 0)
    print(f"\nTotal compounds in Output A: {total_compounds}")
    print(f"Compounds binding >=1 effector gene: {binds_effector}")
    print(
        "\nTop 20 rows of Output A (sorted by n_genes_bound_pchembl_ge6 desc, best_pchembl desc, n_genes_bound desc):"
    )
    print(
        f"{'compound_chembl_id':20s} {'compound_name':30s} {'n_genes':>8s} {'n_eff':>6s} "
        f"{'n_ge6':>6s} {'n_eff_ge6':>10s} {'best_pchembl':>13s}"
    )
    for r in rows_a[:20]:
        print(
            f"{r['compound_chembl_id']:20s} {r['compound_name'][:30]:30s} "
            f"{r['n_genes_bound']:>8} {r['n_effector_genes_bound']:>6} "
            f"{r['n_genes_bound_pchembl_ge6']:>6} {r['n_effectors_bound_pchembl_ge6']:>10} "
            f"{r['best_pchembl']:>13}"
        )

    quercetin_row = next((r for r in rows_a if r["compound_name"] == "QUERCETIN"), None)
    print("\nQuercetin gated vs ungated:")
    if quercetin_row:
        print(
            f"  n_genes_bound (ungated) = {quercetin_row['n_genes_bound']}, "
            f"n_effector_genes_bound (ungated) = {quercetin_row['n_effector_genes_bound']}"
        )
        print(
            f"  n_genes_bound_pchembl_ge6 (gated) = {quercetin_row['n_genes_bound_pchembl_ge6']}, "
            f"n_effectors_bound_pchembl_ge6 (gated) = {quercetin_row['n_effectors_bound_pchembl_ge6']}"
        )
        print(f"  best_pchembl = {quercetin_row['best_pchembl']}")
        print(f"  genes = {quercetin_row['genes']}")
    else:
        print("  QUERCETIN not found in Output A")

    legacy_binds_gated = sum(
        1
        for r in rows_b
        if r["chembl_n_genes_bound_pchembl_ge6"] not in ("", None)
        and int(r["chembl_n_genes_bound_pchembl_ge6"]) >= 1
    )
    print(
        f"\n{legacy_binds_gated} of {len(rows_b)} legacy (original-matrix) compounds bind "
        f">=1 panel gene at pchembl >= {PCHEMBL_GATE:g}."
    )


if __name__ == "__main__":
    main()
