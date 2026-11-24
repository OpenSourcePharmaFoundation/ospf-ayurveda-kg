#!/usr/bin/env python3
"""
ChemBL PPAR-axis + DR gene panel bioactivity scraper.

Resolves every gene in the DR gene panel (data/processed/dr_gene_panel.csv)
to a ChEMBL target (gene symbol -> UniProt accession -> ChEMBL target),
then pulls real binding-affinity bioactivities (IC50/EC50/Ki/Kd, nM) and
mechanism-of-action records for each resolved target. The compound classes
of interest (fibrates, glitazones, glitazars) are not hand-curated - they
fall out of the PPARA/PPARD/PPARG target queries automatically.

Outputs (data/processed/):
  chembl_panel_targets.csv        - gene -> ChEMBL target resolution audit trail
  chembl_panel_bioactivities.csv  - one row per qualifying activity
  chembl_panel_mechanisms.csv     - one row per mechanism-of-action record
  chembl_ppar_compounds.csv       - molecule properties for PPARA/PPARD/PPARG compounds
"""

import argparse
import csv
import os
import sys
import time
from typing import Dict, List, Optional, Tuple

import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, PROJECT_ROOT)

UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"
CHEMBL_BASE = "https://www.ebi.ac.uk/chembl/api/data"
ORIGIN = "https://www.ebi.ac.uk"
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}
RATE_LIMIT_DELAY = 0.3

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
GENE_PANEL_FILE = os.path.join(DATA_DIR, "dr_gene_panel.csv")

ACTIVITY_STANDARD_TYPES = ["IC50", "EC50", "Ki", "Kd"]

# Verified by the lead against the live API - the resolver must reproduce these.
PPAR_EXPECTED_TARGETS = {
    "PPARA": "CHEMBL239",
    "PPARD": "CHEMBL3979",
    "PPARG": "CHEMBL235",
}
PPAR_GENES = list(PPAR_EXPECTED_TARGETS.keys())

SESSION = requests.Session()
SESSION.headers.update(HEADERS)

MOLECULE_CACHE: Dict[str, Dict] = {}


def _get(url: str) -> Optional[Dict]:
    try:
        resp = SESSION.get(url, timeout=30)
        time.sleep(RATE_LIMIT_DELAY)
        if resp.status_code == 200:
            return resp.json()
        print(f"ERROR {resp.status_code} for {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"ERROR request failed for {url}: {e}")
        return None


def _get_paginated(initial_url: str, data_key: str) -> List[Dict]:
    """Paginate a ChEMBL list endpoint, following page_meta.next."""
    results = []
    url = initial_url
    while url:
        data = _get(url)
        if not data:
            break
        results.extend(data.get(data_key, []))
        next_url = data.get("page_meta", {}).get("next")
        url = (ORIGIN + next_url) if next_url and next_url.startswith("/") else next_url
    return results


def _get_total_count(url: str) -> int:
    data = _get(url)
    if not data:
        return 0
    return data.get("page_meta", {}).get("total_count", 0)


def resolve_uniprot_accession(gene: str) -> Optional[str]:
    url = (
        f"{UNIPROT_URL}?query=gene_exact:{gene}+AND+organism_id:9606+AND+reviewed:true"
        f"&fields=accession,gene_primary&format=tsv"
    )
    try:
        resp = SESSION.get(url, timeout=30)
        time.sleep(RATE_LIMIT_DELAY)
    except requests.exceptions.RequestException as e:
        print(f"ERROR UniProt request failed for {gene}: {e}")
        return None

    if resp.status_code != 200:
        print(f"ERROR {resp.status_code} for UniProt lookup of {gene}")
        return None

    lines = [l for l in resp.text.strip().splitlines() if l]
    if len(lines) < 2:
        return None

    # First data row, first column (accession)
    return lines[1].split("\t")[0]


def resolve_chembl_target(accession: str) -> Optional[Dict]:
    url = f"{CHEMBL_BASE}/target.json?target_components__accession={accession}&limit=50"
    data = _get(url)
    if not data:
        return None

    for target in data.get("targets", []):
        if (
            target.get("target_type") == "SINGLE PROTEIN"
            and target.get("organism") == "Homo sapiens"
        ):
            return target
    return None


def resolve_gene(gene: str) -> Tuple[Optional[str], Optional[Dict], str]:
    """Returns (uniprot_accession, chembl_target_dict_or_None, status_so_far)."""
    accession = resolve_uniprot_accession(gene)
    if not accession:
        return None, None, "no_uniprot"

    target = resolve_chembl_target(accession)
    if not target:
        return accession, None, "no_chembl_target"

    return accession, target, "resolved"


def count_activities(target_chembl_id: str) -> int:
    url = (
        f"{CHEMBL_BASE}/activity.json?target_chembl_id={target_chembl_id}"
        f"&standard_type__in={','.join(ACTIVITY_STANDARD_TYPES)}&standard_units=nM&limit=1"
    )
    return _get_total_count(url)


def count_mechanisms(target_chembl_id: str) -> int:
    url = f"{CHEMBL_BASE}/mechanism.json?target_chembl_id={target_chembl_id}&limit=1"
    return _get_total_count(url)


def fetch_activities(target_chembl_id: str) -> List[Dict]:
    url = (
        f"{CHEMBL_BASE}/activity.json?target_chembl_id={target_chembl_id}"
        f"&standard_type__in={','.join(ACTIVITY_STANDARD_TYPES)}&standard_units=nM&limit=1000"
    )
    expected_total = _get_total_count(
        f"{CHEMBL_BASE}/activity.json?target_chembl_id={target_chembl_id}"
        f"&standard_type__in={','.join(ACTIVITY_STANDARD_TYPES)}&standard_units=nM&limit=1"
    )
    records = _get_paginated(url, "activities")

    if len(records) != expected_total:
        raise RuntimeError(
            f"Activity pagination mismatch for {target_chembl_id}: "
            f"collected {len(records)}, API total_count={expected_total}."
        )

    filtered = [
        r
        for r in records
        if r.get("standard_value") is not None
        and r.get("data_validity_comment") is None
    ]
    return filtered


def fetch_mechanisms(target_chembl_id: str) -> List[Dict]:
    url = f"{CHEMBL_BASE}/mechanism.json?target_chembl_id={target_chembl_id}&limit=1000"
    expected_total = _get_total_count(
        f"{CHEMBL_BASE}/mechanism.json?target_chembl_id={target_chembl_id}&limit=1"
    )
    records = _get_paginated(url, "mechanisms")

    if len(records) != expected_total:
        raise RuntimeError(
            f"Mechanism pagination mismatch for {target_chembl_id}: "
            f"collected {len(records)}, API total_count={expected_total}."
        )
    return records


def get_molecule_cached(molecule_chembl_id: str) -> Dict:
    if molecule_chembl_id in MOLECULE_CACHE:
        return MOLECULE_CACHE[molecule_chembl_id]

    data = _get(f"{CHEMBL_BASE}/molecule/{molecule_chembl_id}.json") or {}
    MOLECULE_CACHE[molecule_chembl_id] = data
    return data


def get_molecules_batch(molecule_chembl_ids: List[str]) -> Dict[str, Dict]:
    """Fetch molecule records in batches of 20, caching results."""
    to_fetch = [m for m in molecule_chembl_ids if m not in MOLECULE_CACHE]
    for i in range(0, len(to_fetch), 20):
        batch = to_fetch[i : i + 20]
        url = f"{CHEMBL_BASE}/molecule.json?molecule_chembl_id__in={','.join(batch)}&limit=20"
        data = _get(url) or {}
        for mol in data.get("molecules", []):
            MOLECULE_CACHE[mol["molecule_chembl_id"]] = mol
        for m in batch:
            if m not in MOLECULE_CACHE:
                MOLECULE_CACHE[m] = {}

    return {m: MOLECULE_CACHE[m] for m in molecule_chembl_ids}


def load_gene_panel(genes_filter: Optional[List[str]] = None) -> List[Dict]:
    rows = []
    with open(GENE_PANEL_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if genes_filter and row["gene"] not in genes_filter:
                continue
            rows.append(row)
    return rows


def write_targets_csv(resolution_rows: List[Dict]):
    out_path = os.path.join(DATA_DIR, "chembl_panel_targets.csv")
    fieldnames = [
        "gene",
        "uniprot_accession",
        "chembl_target_id",
        "target_pref_name",
        "target_type",
        "organism",
        "n_activities_raw",
        "n_activities_filtered",
        "n_mechanisms",
        "resolution_status",
    ]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in resolution_rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"Wrote {len(resolution_rows)} rows to {out_path}")
    return out_path


def write_bioactivities_csv(bioactivity_rows: List[Dict]):
    out_path = os.path.join(DATA_DIR, "chembl_panel_bioactivities.csv")
    fieldnames = [
        "gene",
        "chembl_target_id",
        "molecule_chembl_id",
        "molecule_pref_name",
        "standard_type",
        "standard_relation",
        "standard_value",
        "standard_units",
        "pchembl_value",
        "assay_chembl_id",
        "assay_type",
        "assay_description",
        "confidence_score",
        "document_chembl_id",
        "src_id",
        "data_validity_comment",
    ]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in bioactivity_rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"Wrote {len(bioactivity_rows)} rows to {out_path}")
    return out_path


def write_mechanisms_csv(mechanism_rows: List[Dict]):
    out_path = os.path.join(DATA_DIR, "chembl_panel_mechanisms.csv")
    fieldnames = [
        "gene",
        "chembl_target_id",
        "molecule_chembl_id",
        "molecule_pref_name",
        "mechanism_of_action",
        "action_type",
        "direct_interaction",
        "mechanism_comment",
        "max_phase",
    ]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in mechanism_rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"Wrote {len(mechanism_rows)} rows to {out_path}")
    return out_path


def write_ppar_compounds_csv(molecule_ids: List[str]):
    out_path = os.path.join(DATA_DIR, "chembl_ppar_compounds.csv")
    molecules = get_molecules_batch(molecule_ids)

    fieldnames = [
        "molecule_chembl_id",
        "pref_name",
        "max_phase",
        "first_approval",
        "molecule_type",
        "canonical_smiles",
        "full_mwt",
        "alogp",
        "psa",
        "hba",
        "hbd",
        "rtb",
        "ro5_violations",
        "qed_weighted",
    ]

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for mol_id in molecule_ids:
            mol = molecules.get(mol_id) or {}
            props = mol.get("molecule_properties") or {}
            structures = mol.get("molecule_structures") or {}
            writer.writerow(
                {
                    "molecule_chembl_id": mol_id,
                    "pref_name": mol.get("pref_name", ""),
                    "max_phase": mol.get("max_phase", ""),
                    "first_approval": mol.get("first_approval", ""),
                    "molecule_type": mol.get("molecule_type", ""),
                    "canonical_smiles": structures.get("canonical_smiles", ""),
                    "full_mwt": props.get("full_mwt", ""),
                    "alogp": props.get("alogp", ""),
                    "psa": props.get("psa", ""),
                    "hba": props.get("hba", ""),
                    "hbd": props.get("hbd", ""),
                    "rtb": props.get("rtb", ""),
                    "ro5_violations": props.get("num_ro5_violations", ""),
                    "qed_weighted": props.get("qed_weighted", ""),
                }
            )
    print(f"Wrote {len(molecule_ids)} rows to {out_path}")
    return out_path


def main():
    parser = argparse.ArgumentParser(
        description="ChEMBL PPAR-axis + DR gene panel bioactivity scraper"
    )
    parser.add_argument(
        "--genes", help="Comma-separated gene symbols to subset (default: whole panel)"
    )
    args = parser.parse_args()

    genes_filter = [g.strip() for g in args.genes.split(",")] if args.genes else None
    panel_rows = load_gene_panel(genes_filter)

    resolution_rows = []
    bioactivity_rows = []
    mechanism_rows = []
    target_by_gene: Dict[str, str] = {}

    for panel_row in panel_rows:
        gene = panel_row["gene"]
        print(f"Resolving {gene}...")
        accession, target, status = resolve_gene(gene)

        row = {
            "gene": gene,
            "uniprot_accession": accession or "",
            "chembl_target_id": "",
            "target_pref_name": "",
            "target_type": "",
            "organism": "",
            "n_activities_raw": "",
            "n_activities_filtered": "",
            "n_mechanisms": "",
            "resolution_status": status,
        }

        if target:
            target_id = target["target_chembl_id"]
            target_by_gene[gene] = target_id
            row["chembl_target_id"] = target_id
            row["target_pref_name"] = target.get("pref_name", "")
            row["target_type"] = target.get("target_type", "")
            row["organism"] = target.get("organism", "")

            n_activities_raw = count_activities(target_id)
            n_mechanisms = count_mechanisms(target_id)
            row["n_activities_raw"] = n_activities_raw
            row["n_mechanisms"] = n_mechanisms

            n_activities_filtered = 0
            if n_activities_raw > 0:
                activities = fetch_activities(target_id)
                n_activities_filtered = len(activities)
                molecule_ids_needed = {
                    a.get("molecule_chembl_id")
                    for a in activities
                    if a.get("molecule_chembl_id")
                }
                molecules = get_molecules_batch(list(molecule_ids_needed))
                for a in activities:
                    mol_id = a.get("molecule_chembl_id", "")
                    mol = molecules.get(mol_id) or {}
                    bioactivity_rows.append(
                        {
                            "gene": gene,
                            "chembl_target_id": target_id,
                            "molecule_chembl_id": mol_id,
                            "molecule_pref_name": mol.get("pref_name", ""),
                            "standard_type": a.get("standard_type", ""),
                            "standard_relation": a.get("standard_relation", ""),
                            "standard_value": a.get("standard_value", ""),
                            "standard_units": a.get("standard_units", ""),
                            "pchembl_value": a.get("pchembl_value", ""),
                            "assay_chembl_id": a.get("assay_chembl_id", ""),
                            "assay_type": a.get("assay_type", ""),
                            "assay_description": a.get("assay_description", ""),
                            "confidence_score": a.get("confidence_score", ""),
                            "document_chembl_id": a.get("document_chembl_id", ""),
                            "src_id": a.get("src_id", ""),
                            "data_validity_comment": a.get("data_validity_comment", ""),
                        }
                    )

            row["n_activities_filtered"] = n_activities_filtered
            if n_activities_filtered == 0:
                row["resolution_status"] = "no_activities"

            if n_mechanisms > 0:
                mechanisms = fetch_mechanisms(target_id)
                molecule_ids_needed = {
                    m.get("molecule_chembl_id")
                    for m in mechanisms
                    if m.get("molecule_chembl_id")
                }
                for mol_id in molecule_ids_needed:
                    get_molecule_cached(mol_id)
                for m in mechanisms:
                    mol_id = m.get("molecule_chembl_id", "")
                    mol = MOLECULE_CACHE.get(mol_id, {})
                    mechanism_rows.append(
                        {
                            "gene": gene,
                            "chembl_target_id": target_id,
                            "molecule_chembl_id": mol_id,
                            "molecule_pref_name": mol.get("pref_name", ""),
                            "mechanism_of_action": m.get("mechanism_of_action", ""),
                            "action_type": m.get("action_type", ""),
                            "direct_interaction": m.get("direct_interaction", ""),
                            "mechanism_comment": m.get("mechanism_comment", ""),
                            "max_phase": mol.get("max_phase", ""),
                        }
                    )

        resolution_rows.append(row)

    # Regression guard: the resolver must reproduce the three verified PPAR targets
    for gene, expected_target in PPAR_EXPECTED_TARGETS.items():
        if gene in target_by_gene and target_by_gene[gene] != expected_target:
            raise RuntimeError(
                f"PPAR resolver regression: {gene} resolved to {target_by_gene[gene]}, "
                f"expected {expected_target}."
            )

    write_targets_csv(resolution_rows)
    write_bioactivities_csv(bioactivity_rows)
    write_mechanisms_csv(mechanism_rows)

    ppar_molecule_ids = sorted(
        {r["molecule_chembl_id"] for r in bioactivity_rows if r["gene"] in PPAR_GENES}
        | {r["molecule_chembl_id"] for r in mechanism_rows if r["gene"] in PPAR_GENES}
    )
    write_ppar_compounds_csv(ppar_molecule_ids)

    # Report
    print("\n=== Resolution table ===")
    header = (
        f"{'gene':10s} {'uniprot':10s} {'chembl_target':15s} {'type':16s} "
        f"{'n_act_raw':>10s} {'n_act_filt':>10s} {'n_mech':>8s} {'status':15s}"
    )
    print(header)
    for row in resolution_rows:
        print(
            f"{row['gene']:10s} {row['uniprot_accession']:10s} {row['chembl_target_id']:15s} "
            f"{row['target_type']:16s} {str(row['n_activities_raw']):>10s} "
            f"{str(row['n_activities_filtered']):>10s} {str(row['n_mechanisms']):>8s} "
            f"{row['resolution_status']:15s}"
        )

    print("\n=== Per-gene activity counts (filtered) ===")
    for row in resolution_rows:
        print(f"  {row['gene']}: {row['n_activities_filtered'] or 0} activities")

    effector_genes = [r["gene"] for r in panel_rows if r.get("role") == "ppar_effector"]
    resolved_with_activities = [
        r
        for r in resolution_rows
        if r["gene"] in effector_genes
        and r["resolution_status"] == "resolved"
        and int(r["n_activities_filtered"] or 0) > 0
    ]
    print(
        f"\n{len(resolved_with_activities)} of {len(effector_genes)} ppar_effector genes "
        f"resolved to a ChEMBL target with >0 activities."
    )


if __name__ == "__main__":
    main()
