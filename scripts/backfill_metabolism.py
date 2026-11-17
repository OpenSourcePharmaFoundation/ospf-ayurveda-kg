#!/usr/bin/env python3
"""
One-time backfill of ChEMBL drug metabolism records.

The metabolism scrape in src/scrapers/chembl/chembl_scraper.py only covers
185 of 3,276 approved drugs (the rest were never correctly queried before
the drug_chembl_id filter bug was fixed). This script fetches metabolism
data ONLY for the drugs still missing it, then merges the results into the
main chembl_drug_metabolism.csv.

Standalone script: does not import from chembl_scraper.py.
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

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed"
)
APPROVED_DRUGS_FILE = os.path.join(DATA_DIR, "chembl_approved_drugs.csv")
MAIN_METABOLISM_FILE = os.path.join(DATA_DIR, "chembl_drug_metabolism.csv")
BACKFILL_FILE = os.path.join(DATA_DIR, "chembl_drug_metabolism_backfill.csv")
PROGRESS_FILE = os.path.join(DATA_DIR, "chembl_drug_metabolism_backfill_progress.txt")

FIELDNAMES = [
    "drug_chembl_id", "requested_chembl_id", "drug_name",
    "substrate_chembl_id", "substrate_name",
    "metabolite_chembl_id", "metabolite_name", "enzyme_name", "enzyme_tid",
    "organism", "pathway_id", "pathway_key", "met_conversion",
    "met_comment", "references",
]

session = requests.Session()
session.headers.update(HEADERS)


def make_request(url):
    try:
        response = session.get(url, timeout=30)
        sleep(RATE_LIMIT_DELAY)
        if response.status_code == 200:
            return response.json()
        print(f"❌ Error {response.status_code} for URL: {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None


def get_paginated_results(initial_url, data_key):
    results = []
    url = initial_url
    while url:
        data = make_request(url)
        if not data:
            break
        results.extend(data.get(data_key, []))
        page_meta = data.get("page_meta", {})
        url = page_meta.get("next")
        if url and url.startswith("/"):
            url = ORIGIN + url
    return results


def get_metabolism_unfiltered_total():
    url = f"{API_BASE}/metabolism?limit=1"
    data = make_request(url)
    if not data:
        return None
    return data.get("page_meta", {}).get("total_count")


def get_metabolism_raw_total(chembl_id):
    url = f"{API_BASE}/metabolism?drug_chembl_id={chembl_id}&limit=1"
    data = make_request(url)
    if not data:
        return None
    return data.get("page_meta", {}).get("total_count")


def get_metabolism(chembl_id):
    url = f"{API_BASE}/metabolism?drug_chembl_id={chembl_id}&limit=1000"
    records = get_paginated_results(url, "metabolisms")

    matched = [r for r in records if r.get("drug_chembl_id") == chembl_id]
    dropped = len(records) - len(matched)

    if dropped > 0:
        print(
            f"⚠️  WARNING: {dropped}/{len(records)} metabolism records "
            f"for requested drug_chembl_id={chembl_id} had a mismatching "
            f"drug_chembl_id and were dropped."
        )

    if records and dropped > len(records) / 2:
        raise RuntimeError(
            f"More than half of the metabolism records returned for "
            f"{chembl_id} did not match the requested drug_chembl_id "
            f"({dropped}/{len(records)} mismatched). This is the "
            f"signature of the API silently ignoring the filter - "
            f"stop and investigate."
        )

    return matched


def load_approved_drugs():
    drugs = []
    with open(APPROVED_DRUGS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            drugs.append(
                {"chembl_id": row["chembl_id"],
                 "pref_name": row.get("pref_name", "")}
            )
    return drugs


def load_done_ids(*csv_paths):
    done = set()
    for path in csv_paths:
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                req_id = row.get("requested_chembl_id")
                if req_id:
                    done.add(req_id)
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    done.add(line)
    return done


def row_from_metabolism(metab, chembl_id, drug_name):
    refs = metab.get("metabolism_refs", []) or []
    ref_strings = []
    for ref in refs:
        if isinstance(ref, dict):
            ref_strings.append(ref.get("ref_id", str(ref)))
        else:
            ref_strings.append(str(ref))

    return {
        "drug_chembl_id": metab.get("drug_chembl_id", ""),
        "requested_chembl_id": chembl_id,
        "drug_name": drug_name,
        "substrate_chembl_id": metab.get("substrate_chembl_id", ""),
        "substrate_name": metab.get("substrate_name", ""),
        "metabolite_chembl_id": metab.get("metabolite_chembl_id", ""),
        "metabolite_name": metab.get("metabolite_name", ""),
        "enzyme_name": metab.get("enzyme_name", ""),
        "enzyme_tid": metab.get("target_chembl_id", ""),
        "organism": metab.get("organism", ""),
        "pathway_id": metab.get("pathway_id", ""),
        "pathway_key": metab.get("pathway_key", ""),
        "met_conversion": metab.get("met_conversion", ""),
        "met_comment": metab.get("met_comment", ""),
        "references": "; ".join(ref_strings),
    }


def fetch_missing(missing_drugs):
    backfill_exists = os.path.exists(BACKFILL_FILE)
    with open(BACKFILL_FILE, "a", newline="", encoding="utf-8") as bf, \
         open(PROGRESS_FILE, "a", encoding="utf-8") as pf:
        writer = csv.DictWriter(bf, fieldnames=FIELDNAMES)
        if not backfill_exists:
            writer.writeheader()

        unfiltered_total = get_metabolism_unfiltered_total()
        print(f"ℹ️  Unfiltered /metabolism total_count sentinel: {unfiltered_total}")
        checked_sentinel = False

        total = len(missing_drugs)
        for i, drug in enumerate(missing_drugs):
            chembl_id = drug["chembl_id"]
            drug_name = drug.get("pref_name", "")

            metabolisms = get_metabolism(chembl_id)

            if not checked_sentinel:
                checked_sentinel = True
                if (unfiltered_total is not None
                        and get_metabolism_raw_total(chembl_id) == unfiltered_total):
                    raise RuntimeError(
                        f"Metabolism filter regression detected: the filtered "
                        f"total_count for drug_chembl_id={chembl_id} equals the "
                        f"unfiltered /metabolism total_count ({unfiltered_total}). "
                        f"The API is silently ignoring the drug_chembl_id filter "
                        f"again - re-check the filter field name before proceeding."
                    )

            for metab in metabolisms:
                writer.writerow(row_from_metabolism(metab, chembl_id, drug_name))
            bf.flush()

            pf.write(chembl_id + "\n")
            pf.flush()

            if (i + 1) % 100 == 0 or (i + 1) == total:
                print(f"  [{i + 1}/{total}] Processing {chembl_id}... {len(metabolisms)} metabolism records")


def merge_backfill_into_main():
    if not os.path.exists(BACKFILL_FILE):
        print("ℹ️  No backfill file found - nothing to merge.")
        return

    rows = []
    for path in (MAIN_METABOLISM_FILE, BACKFILL_FILE):
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows.extend(reader)

    rows.sort(key=lambda r: r.get("drug_chembl_id", ""))

    with open(MAIN_METABOLISM_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELDNAMES})

    os.remove(BACKFILL_FILE)
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)
    print(f"✅ Merged backfill into {MAIN_METABOLISM_FILE} ({len(rows)} rows total)")


def print_final_stats():
    total_rows = 0
    drugs_covered = set()
    drugs_with_records = set()
    with open(MAIN_METABOLISM_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rows += 1
            req_id = row.get("requested_chembl_id")
            if req_id:
                drugs_covered.add(req_id)
                drugs_with_records.add(req_id)

    all_drugs = load_approved_drugs()
    all_ids = {d["chembl_id"] for d in all_drugs}
    zero_record_drugs = all_ids - drugs_with_records

    print(f"✅ Total rows: {total_rows}")
    print(f"✅ Total drugs covered (queried, recorded in file): {len(drugs_covered)}")
    print(f"✅ Drugs with zero metabolism records: {len(zero_record_drugs)}")


def main():
    parser = argparse.ArgumentParser(description="Backfill missing ChEMBL drug metabolism data.")
    parser.add_argument("--dry-run", action="store_true", help="Print stats only, no API calls.")
    parser.add_argument("--merge-only", action="store_true", help="Skip fetching, just merge the backfill file into main.")
    args = parser.parse_args()

    approved_drugs = load_approved_drugs()
    done_ids = load_done_ids(MAIN_METABOLISM_FILE, BACKFILL_FILE)

    missing_drugs = [d for d in approved_drugs if d["chembl_id"] not in done_ids]

    print(f"{len(approved_drugs) - len(missing_drugs)} drugs already done, {len(missing_drugs)} to fetch")

    if args.dry_run:
        return

    if args.merge_only:
        merge_backfill_into_main()
        print_final_stats()
        return

    if missing_drugs:
        fetch_missing(missing_drugs)
    else:
        print("ℹ️  No missing drugs to fetch.")

    merge_backfill_into_main()
    print_final_stats()


if __name__ == "__main__":
    sys.exit(main())
