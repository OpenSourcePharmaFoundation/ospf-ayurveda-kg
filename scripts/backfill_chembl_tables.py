#!/usr/bin/env python3
"""
One-time backfill of ChEMBL drug mechanism, indication, and target records.

These tables were only ever populated by a test-mode run (10 drugs) and cover
a tiny fraction of the 3,276 approved drugs: mechanisms (11 rows), targets
(44 rows), indications (80 rows). This script fetches the missing data for
each table and merges the results into the corresponding main CSV.

Standalone script: does not import from src/scrapers/chembl/chembl_scraper.py.

Run order (default, no flags): mechanisms, then indications, then targets
(targets needs the target_chembl_id values discovered via mechanisms).
"""

import argparse
import csv
import os
import sys
from time import sleep

import requests

API_BASE = "https://www.ebi.ac.uk/chembl/api/data"
ORIGIN = "https://www.ebi.ac.uk"
RATE_LIMIT_DELAY = 0.5
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}

MAX_RETRIES = 4
RETRY_BACKOFF = [2, 5, 15, 30]

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed"
)
APPROVED_DRUGS_FILE = os.path.join(DATA_DIR, "chembl_approved_drugs.csv")

MAIN_MECHANISMS_FILE = os.path.join(DATA_DIR, "chembl_drug_mechanisms.csv")
BACKFILL_MECHANISMS_FILE = os.path.join(DATA_DIR, "chembl_drug_mechanisms_backfill.csv")

MAIN_INDICATIONS_FILE = os.path.join(DATA_DIR, "chembl_drug_indications.csv")
BACKFILL_INDICATIONS_FILE = os.path.join(DATA_DIR, "chembl_drug_indications_backfill.csv")

MAIN_TARGETS_FILE = os.path.join(DATA_DIR, "chembl_drug_targets.csv")
BACKFILL_TARGETS_FILE = os.path.join(DATA_DIR, "chembl_drug_targets_backfill.csv")

PROGRESS_FILE = os.path.join(DATA_DIR, "chembl_tables_backfill_progress.txt")

MECHANISMS_FIELDNAMES = [
    "chembl_id", "drug_name", "mechanism_of_action", "action_type",
    "target_chembl_id", "target_name", "target_type", "binding_site",
    "direct_interaction", "molecular_mechanism", "disease_efficacy",
    "mechanism_comment", "selectivity_comment", "references",
]

INDICATIONS_FIELDNAMES = [
    "chembl_id", "drug_name", "mesh_id", "mesh_heading",
    "efo_id", "efo_term", "max_phase_for_ind", "indication_refs",
]

TARGETS_FIELDNAMES = [
    "target_chembl_id", "pref_name", "target_type", "organism",
    "tax_id", "gene_names", "uniprot_accessions", "target_components",
    "target_family", "target_class", "protein_class",
]

session = requests.Session()
session.headers.update(HEADERS)

# Populated as mechanism target lookups happen; reused by the targets stage
# so we don't re-fetch the same /target/{id} record twice in one run.
_target_detail_cache = {}


def make_request(url):
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = session.get(url, timeout=60)
            sleep(RATE_LIMIT_DELAY)
            if response.status_code == 200:
                return response.json()
            if response.status_code >= 500 and attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF[attempt]
                print(f"⚠️  {response.status_code} on attempt {attempt + 1}, retrying in {wait}s...")
                sleep(wait)
                continue
            print(f"❌ Error {response.status_code} for URL: {url}")
            return None
        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF[attempt]
                print(f"⚠️  {type(e).__name__} on attempt {attempt + 1}, retrying in {wait}s...")
                sleep(wait)
                continue
            print(f"❌ Request failed after {MAX_RETRIES + 1} attempts: {e}")
            return None


def get_paginated_results(initial_url, data_key):
    results = []
    url = initial_url
    page_failures = 0
    while url:
        data = make_request(url)
        if not data:
            page_failures += 1
            if page_failures >= 2:
                print(f"⚠️  Two consecutive page failures, returning {len(results)} records collected so far")
                break
            continue
        page_failures = 0
        results.extend(data.get(data_key, []))
        page_meta = data.get("page_meta", {})
        url = page_meta.get("next")
        if url and url.startswith("/"):
            url = ORIGIN + url
    return results


def refs_to_string(refs, key="ref_id"):
    ref_strings = []
    for ref in refs or []:
        if isinstance(ref, dict):
            val = ref.get(key)
            ref_strings.append(str(val) if val is not None else str(ref))
        else:
            ref_strings.append(str(ref))
    return "; ".join(ref_strings)


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def load_approved_drugs():
    drugs = []
    with open(APPROVED_DRUGS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            drugs.append({"chembl_id": row["chembl_id"], "pref_name": row.get("pref_name", "")})
    return drugs


def load_progress():
    """Returns dict: table_name -> set of chembl_ids already queried for that table."""
    progress = {"mechanisms": set(), "indications": set(), "targets": set()}
    if not os.path.exists(PROGRESS_FILE):
        return progress
    with open(PROGRESS_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            table, chembl_id = line.split(":", 1)
            if table in progress:
                progress[table].add(chembl_id)
    return progress


def append_progress(table, chembl_id):
    with open(PROGRESS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{table}:{chembl_id}\n")


def remove_progress_lines(table):
    if not os.path.exists(PROGRESS_FILE):
        return
    with open(PROGRESS_FILE, encoding="utf-8") as f:
        lines = [line for line in f if not line.startswith(f"{table}:")]
    if lines:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            f.writelines(lines)
    else:
        os.remove(PROGRESS_FILE)


def ids_already_in_csv(path, column):
    ids = set()
    if not os.path.exists(path):
        return ids
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            val = row.get(column)
            if val:
                ids.add(val)
    return ids


def merge_csv_files(main_file, backfill_file, fieldnames, sort_key):
    if not os.path.exists(backfill_file):
        print(f"ℹ️  No backfill file found at {backfill_file} - nothing to merge.")
        return

    rows = []
    for path in (main_file, backfill_file):
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows.extend(reader)

    rows.sort(key=lambda r: r.get(sort_key, "") or "")

    with open(main_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

    os.remove(backfill_file)
    print(f"✅ Merged backfill into {main_file} ({len(rows)} rows total)")


# ---------------------------------------------------------------------------
# Target detail lookup (shared by mechanisms stage and targets stage)
# ---------------------------------------------------------------------------

def get_target_details(target_chembl_id):
    if target_chembl_id in _target_detail_cache:
        return _target_detail_cache[target_chembl_id]
    url = f"{API_BASE}/target/{target_chembl_id}"
    data = make_request(url)
    _target_detail_cache[target_chembl_id] = data
    return data


# ---------------------------------------------------------------------------
# Mechanisms
# ---------------------------------------------------------------------------

def get_mechanisms(chembl_id):
    url = f"{API_BASE}/mechanism?molecule_chembl_id={chembl_id}&limit=1000"
    return get_paginated_results(url, "mechanisms")


def row_from_mechanism(mech, chembl_id, drug_name):
    target_id = mech.get("target_chembl_id") or ""
    target_name = ""
    target_type = ""
    if target_id:
        target_data = get_target_details(target_id)
        if target_data:
            target_name = target_data.get("pref_name", "")
            target_type = target_data.get("target_type", "")

    return {
        "chembl_id": chembl_id,
        "drug_name": drug_name,
        "mechanism_of_action": mech.get("mechanism_of_action", ""),
        "action_type": mech.get("action_type", ""),
        "target_chembl_id": target_id,
        "target_name": target_name,
        "target_type": target_type,
        "binding_site": mech.get("binding_site_comment", ""),
        "direct_interaction": mech.get("direct_interaction", ""),
        "molecular_mechanism": mech.get("molecular_mechanism", ""),
        "disease_efficacy": mech.get("disease_efficacy", ""),
        "mechanism_comment": mech.get("mechanism_comment", ""),
        "selectivity_comment": mech.get("selectivity_comment", ""),
        "references": refs_to_string(mech.get("mechanism_refs", [])),
    }


def fetch_missing_mechanisms(missing_drugs):
    backfill_exists = os.path.exists(BACKFILL_MECHANISMS_FILE)
    with open(BACKFILL_MECHANISMS_FILE, "a", newline="", encoding="utf-8") as bf:
        writer = csv.DictWriter(bf, fieldnames=MECHANISMS_FIELDNAMES)
        if not backfill_exists:
            writer.writeheader()

        total = len(missing_drugs)
        total_rows = 0
        for i, drug in enumerate(missing_drugs):
            chembl_id = drug["chembl_id"]
            drug_name = drug.get("pref_name", "")

            mechanisms = get_mechanisms(chembl_id)
            for mech in mechanisms:
                writer.writerow(row_from_mechanism(mech, chembl_id, drug_name))
            total_rows += len(mechanisms)
            bf.flush()

            append_progress("mechanisms", chembl_id)

            if (i + 1) % 50 == 0 or (i + 1) == total:
                print(f"  [mechanisms {i + 1}/{total}] {chembl_id}: {len(mechanisms)} records ({total_rows} total rows so far)")


# ---------------------------------------------------------------------------
# Indications
# ---------------------------------------------------------------------------

def get_indications(chembl_id):
    url = f"{API_BASE}/drug_indication?molecule_chembl_id={chembl_id}&limit=1000"
    return get_paginated_results(url, "drug_indications")


def row_from_indication(ind, chembl_id, drug_name):
    return {
        "chembl_id": chembl_id,
        "drug_name": drug_name,
        "mesh_id": ind.get("mesh_id", ""),
        "mesh_heading": ind.get("mesh_heading", ""),
        "efo_id": ind.get("efo_id", ""),
        "efo_term": ind.get("efo_term", ""),
        "max_phase_for_ind": ind.get("max_phase_for_ind", ""),
        "indication_refs": refs_to_string(ind.get("indication_refs", [])),
    }


def fetch_missing_indications(missing_drugs):
    backfill_exists = os.path.exists(BACKFILL_INDICATIONS_FILE)
    with open(BACKFILL_INDICATIONS_FILE, "a", newline="", encoding="utf-8") as bf:
        writer = csv.DictWriter(bf, fieldnames=INDICATIONS_FIELDNAMES)
        if not backfill_exists:
            writer.writeheader()

        total = len(missing_drugs)
        total_rows = 0
        for i, drug in enumerate(missing_drugs):
            chembl_id = drug["chembl_id"]
            drug_name = drug.get("pref_name", "")

            indications = get_indications(chembl_id)
            for ind in indications:
                writer.writerow(row_from_indication(ind, chembl_id, drug_name))
            total_rows += len(indications)
            bf.flush()

            append_progress("indications", chembl_id)

            if (i + 1) % 50 == 0 or (i + 1) == total:
                print(f"  [indications {i + 1}/{total}] {chembl_id}: {len(indications)} records ({total_rows} total rows so far)")


# ---------------------------------------------------------------------------
# Targets
# ---------------------------------------------------------------------------

def collect_target_ids_from_mechanisms():
    ids = set()
    for path in (MAIN_MECHANISMS_FILE, BACKFILL_MECHANISMS_FILE):
        ids |= ids_already_in_csv(path, "target_chembl_id")
    ids.discard("")
    return ids


def row_from_target(target_data):
    target_id = target_data.get("target_chembl_id", "")
    components = target_data.get("target_components", []) or []
    gene_names = []
    uniprot_ids = []
    protein_classes = []
    for comp in components:
        if comp.get("gene_name"):
            gene_names.append(comp["gene_name"])
        if comp.get("accession"):
            uniprot_ids.append(comp["accession"])

    protein_class = target_data.get("protein_class", "")
    if isinstance(protein_class, list):
        protein_class = "; ".join(protein_class)

    target_family = target_data.get("target_family", "")
    target_class = target_data.get("target_class", "")

    return {
        "target_chembl_id": target_id,
        "pref_name": target_data.get("pref_name", ""),
        "target_type": target_data.get("target_type", ""),
        "organism": target_data.get("organism", ""),
        "tax_id": target_data.get("tax_id", ""),
        "gene_names": "; ".join(gene_names),
        "uniprot_accessions": "; ".join(uniprot_ids),
        "target_components": len(components),
        "target_family": target_family,
        "target_class": target_class,
        "protein_class": protein_class,
    }


def fetch_missing_targets(missing_target_ids):
    backfill_exists = os.path.exists(BACKFILL_TARGETS_FILE)
    with open(BACKFILL_TARGETS_FILE, "a", newline="", encoding="utf-8") as bf:
        writer = csv.DictWriter(bf, fieldnames=TARGETS_FIELDNAMES)
        if not backfill_exists:
            writer.writeheader()

        total = len(missing_target_ids)
        for i, target_id in enumerate(missing_target_ids):
            target_data = get_target_details(target_id)
            if target_data:
                writer.writerow(row_from_target(target_data))
            bf.flush()

            append_progress("targets", target_id)

            if (i + 1) % 50 == 0 or (i + 1) == total:
                print(f"  [targets {i + 1}/{total}] {target_id}")


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def print_final_stats(main_file, label):
    if not os.path.exists(main_file):
        print(f"ℹ️  {label}: file does not exist yet.")
        return
    with open(main_file, newline="", encoding="utf-8") as f:
        total_rows = sum(1 for _ in csv.DictReader(f))
    print(f"✅ {label}: {total_rows} rows in {main_file}")


# ---------------------------------------------------------------------------
# Per-table orchestration
# ---------------------------------------------------------------------------

def run_mechanisms(approved_drugs, progress, dry_run, merge_only):
    done_ids = ids_already_in_csv(MAIN_MECHANISMS_FILE, "chembl_id") | progress["mechanisms"]
    missing_drugs = [d for d in approved_drugs if d["chembl_id"] not in done_ids]
    print(f"mechanisms: {len(approved_drugs) - len(missing_drugs)} drugs already done, {len(missing_drugs)} to fetch")

    if dry_run:
        return
    if merge_only:
        merge_csv_files(MAIN_MECHANISMS_FILE, BACKFILL_MECHANISMS_FILE, MECHANISMS_FIELDNAMES, "chembl_id")
        remove_progress_lines("mechanisms")
        print_final_stats(MAIN_MECHANISMS_FILE, "mechanisms")
        return

    if missing_drugs:
        fetch_missing_mechanisms(missing_drugs)
    else:
        print("ℹ️  No missing drugs to fetch for mechanisms.")

    merge_csv_files(MAIN_MECHANISMS_FILE, BACKFILL_MECHANISMS_FILE, MECHANISMS_FIELDNAMES, "chembl_id")
    remove_progress_lines("mechanisms")
    print_final_stats(MAIN_MECHANISMS_FILE, "mechanisms")


def run_indications(approved_drugs, progress, dry_run, merge_only):
    done_ids = ids_already_in_csv(MAIN_INDICATIONS_FILE, "chembl_id") | progress["indications"]
    missing_drugs = [d for d in approved_drugs if d["chembl_id"] not in done_ids]
    print(f"indications: {len(approved_drugs) - len(missing_drugs)} drugs already done, {len(missing_drugs)} to fetch")

    if dry_run:
        return
    if merge_only:
        merge_csv_files(MAIN_INDICATIONS_FILE, BACKFILL_INDICATIONS_FILE, INDICATIONS_FIELDNAMES, "chembl_id")
        remove_progress_lines("indications")
        print_final_stats(MAIN_INDICATIONS_FILE, "indications")
        return

    if missing_drugs:
        fetch_missing_indications(missing_drugs)
    else:
        print("ℹ️  No missing drugs to fetch for indications.")

    merge_csv_files(MAIN_INDICATIONS_FILE, BACKFILL_INDICATIONS_FILE, INDICATIONS_FIELDNAMES, "chembl_id")
    remove_progress_lines("indications")
    print_final_stats(MAIN_INDICATIONS_FILE, "indications")


def run_targets(progress, dry_run, merge_only):
    discovered_ids = collect_target_ids_from_mechanisms()
    done_ids = (
        ids_already_in_csv(MAIN_TARGETS_FILE, "target_chembl_id")
        | ids_already_in_csv(BACKFILL_TARGETS_FILE, "target_chembl_id")
        | progress["targets"]
    )
    missing_target_ids = sorted(discovered_ids - done_ids)
    print(f"targets: {len(discovered_ids & done_ids)} targets already done, {len(missing_target_ids)} to fetch "
          f"(discovered {len(discovered_ids)} unique target ids from mechanisms data)")

    if dry_run:
        return
    if merge_only:
        merge_csv_files(MAIN_TARGETS_FILE, BACKFILL_TARGETS_FILE, TARGETS_FIELDNAMES, "target_chembl_id")
        remove_progress_lines("targets")
        print_final_stats(MAIN_TARGETS_FILE, "targets")
        return

    if missing_target_ids:
        fetch_missing_targets(missing_target_ids)
    else:
        print("ℹ️  No missing targets to fetch.")

    merge_csv_files(MAIN_TARGETS_FILE, BACKFILL_TARGETS_FILE, TARGETS_FIELDNAMES, "target_chembl_id")
    remove_progress_lines("targets")
    print_final_stats(MAIN_TARGETS_FILE, "targets")


def main():
    parser = argparse.ArgumentParser(description="Backfill missing ChEMBL mechanism, indication, and target data.")
    parser.add_argument("--dry-run", action="store_true", help="Print stats only, no API calls.")
    parser.add_argument("--merge-only", action="store_true", help="Skip fetching, just merge backfill file(s) into main.")
    parser.add_argument("--mechanisms-only", action="store_true", help="Only backfill the mechanisms table.")
    parser.add_argument("--indications-only", action="store_true", help="Only backfill the indications table.")
    parser.add_argument("--targets-only", action="store_true", help="Only backfill the targets table.")
    args = parser.parse_args()

    only_flags = [args.mechanisms_only, args.indications_only, args.targets_only]
    run_mechanisms_stage = args.mechanisms_only or not any(only_flags)
    run_indications_stage = args.indications_only or not any(only_flags)
    run_targets_stage = args.targets_only or not any(only_flags)

    approved_drugs = load_approved_drugs()
    progress = load_progress()

    if run_mechanisms_stage:
        run_mechanisms(approved_drugs, progress, args.dry_run, args.merge_only)
    if run_indications_stage:
        run_indications(approved_drugs, progress, args.dry_run, args.merge_only)
    if run_targets_stage:
        run_targets(progress, args.dry_run, args.merge_only)


if __name__ == "__main__":
    sys.exit(main())
