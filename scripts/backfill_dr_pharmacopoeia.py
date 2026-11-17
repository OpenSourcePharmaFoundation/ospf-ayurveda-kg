#!/usr/bin/env python3
"""
Backfill PubChem target-interaction data for the traditional diabetic
retinopathy (DR) pharmacopoeia compounds.

The project's phytochemical data was collected for Oral Mucositis (the
original target disease) and only covers 13 IMPPAT plants. The traditional
DR pharmacopoeia - well-studied compounds with published DR-relevant
activity - is completely absent from data/processed/pubchem_phytochem_target_interactions.csv.
This script fetches PubChem chemical-target interaction data for those
compounds using the same consolidatedcompoundtarget query the existing
scraper uses, so the output is schema-compatible and can be concatenated
with the existing file.

Standalone script: does not import from src/scrapers/pubchem/pubchem_scraper.py.

Output:
  data/processed/pubchem_dr_pharmacopoeia_interactions.csv
  data/processed/dr_pharmacopoeia_compound_ids.csv
"""

import argparse
import csv
import os
import sys
from time import sleep

import requests

RATE_LIMIT_DELAY = 0.25  # PubChem programmatic access limit: max 5 req/s
HEADERS = {"User-Agent": "ospf-ayurveda-kg-dr-pharmacopoeia-backfill", "Accept": "text/csv"}

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed"
)
INTERACTIONS_FILE = os.path.join(DATA_DIR, "pubchem_dr_pharmacopoeia_interactions.csv")
COMPOUND_IDS_FILE = os.path.join(DATA_DIR, "dr_pharmacopoeia_compound_ids.csv")
PROGRESS_FILE = os.path.join(DATA_DIR, "dr_pharmacopoeia_backfill_progress.txt")

# Same column schema as data/processed/pubchem_phytochem_target_interactions.csv
# (leading blank-named column mirrors that file's pandas-index artifact so the
# two CSVs can be concatenated directly).
FIELDNAMES = [
    "",
    "interaction_id",
    "cid",
    "info_source",
    "pubchem_name",
    "source_cmpnd_name",
    "source_gene_name",
    "protein_name",
    "protein_id",
    "gene_name",
    "action",
    "evidences",
    "evidence_urls",
]

COMPOUND_ID_FIELDNAMES = [
    "compound_name",
    "pubchem_cid",
    "source_plant",
    "traditional_use_context",
]

MAX_RETRIES = 4
RETRY_BACKOFF = [2, 5, 15, 30]

session = requests.Session()
session.headers.update(HEADERS)

# Hardcoded CID lookup table, verified against
# https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/cids/JSON
# during development.
DR_PHARMACOPOEIA_COMPOUNDS = [
    {
        "compound_name": "Curcumin",
        "pubchem_cid": 969516,
        "source_plant": "Curcuma longa (turmeric)",
        "traditional_use_context": "Ayurveda - anti-inflammatory, retinal neuroprotection",
    },
    {
        "compound_name": "Berberine",
        "pubchem_cid": 2353,
        "source_plant": "Berberis aristata / Coptis chinensis",
        "traditional_use_context": "Ayurveda/TCM - AMPK activation, microvascular protection",
    },
    {
        "compound_name": "Piperine",
        "pubchem_cid": 638024,
        "source_plant": "Piper nigrum (black pepper)",
        "traditional_use_context": "Ayurveda - bioenhancer, anti-inflammatory",
    },
    {
        "compound_name": "Puerarin",
        "pubchem_cid": 5281807,
        "source_plant": "Pueraria lobata (kudzu)",
        "traditional_use_context": "TCM - microcirculation, antioxidant",
    },
    {
        "compound_name": "Tanshinone IIA",
        "pubchem_cid": 164676,
        "source_plant": "Salvia miltiorrhiza (Danshen)",
        "traditional_use_context": "TCM - microcirculation, anti-fibrotic",
    },
    {
        "compound_name": "Salvianolic acid B",
        "pubchem_cid": 11629084,
        "source_plant": "Salvia miltiorrhiza (Danshen)",
        "traditional_use_context": "TCM - antioxidant, anti-fibrotic",
    },
    {
        "compound_name": "Astragaloside IV",
        "pubchem_cid": 13943297,
        "source_plant": "Astragalus membranaceus",
        "traditional_use_context": "TCM - anti-inflammatory, VEGF modulation",
    },
    {
        "compound_name": "Crocin",
        "pubchem_cid": 5281233,
        "source_plant": "Crocus sativus (saffron)",
        "traditional_use_context": "Persian/traditional medicine - retinal antioxidant",
    },
    {
        "compound_name": "Resveratrol",
        "pubchem_cid": 445154,
        "source_plant": "Vaccinium myrtillus (bilberry) / Vitis vinifera",
        "traditional_use_context": "Traditional - antioxidant, SIRT1 activation",
    },
    {
        "compound_name": "Cyanidin-3-glucoside",
        "pubchem_cid": 441667,
        "source_plant": "Vaccinium myrtillus (bilberry); representative anthocyanin",
        "traditional_use_context": "Traditional - retinal antioxidant, microvascular protection",
    },
]


def make_request(url):
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = session.get(url, timeout=60)
            sleep(RATE_LIMIT_DELAY)
            if response.status_code == 200:
                return response.text
            if response.status_code >= 500 and attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF[attempt]
                print(f"  {response.status_code} on attempt {attempt + 1}, retrying in {wait}s...")
                sleep(wait)
                continue
            print(f"  Error {response.status_code} for URL: {url}")
            return None
        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF[attempt]
                print(f"  {type(e).__name__} on attempt {attempt + 1}, retrying in {wait}s...")
                sleep(wait)
                continue
            print(f"  Request failed after {MAX_RETRIES + 1} attempts: {e}")
            return None


def fetch_target_interactions_csv(cid):
    """Download the raw consolidatedcompoundtarget CSV for one CID.

    Same sdqagent.cgi query pattern used by
    src/scrapers/pubchem/pubchem_scraper.py::download_target_interactions.
    """
    scraping_url = (
        "https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?"
        "infmt=json&outfmt=csv&query="
        '{"download":"*","collection":"consolidatedcompoundtarget",'
        '"order":["cid,asc"],"start":1,"limit":10000000,'
        f'"downloadfilename":"pubchem_cid_{cid}_consolidatedcompoundtarget",'
        f'"where":{{"ands":[{{"cid":"{cid}"}}]}}}}'
    )
    text = make_request(scraping_url)
    if text is None:
        return []
    reader = csv.DictReader(text.splitlines())
    return list(reader)


def load_done_cids():
    done = set()
    if os.path.exists(INTERACTIONS_FILE):
        with open(INTERACTIONS_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("cid"):
                    done.add(row["cid"])
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    done.add(line)
    return done


def row_from_interaction(raw_row, idx):
    return {
        "": idx,
        "interaction_id": raw_row.get("id", ""),
        "cid": raw_row.get("cid", ""),
        "info_source": raw_row.get("dsn", ""),
        "pubchem_name": raw_row.get("cmpdname", ""),
        "source_cmpnd_name": raw_row.get("srccmpdname", ""),
        "source_gene_name": raw_row.get("srctargetname", ""),
        "protein_name": raw_row.get("protname", ""),
        "protein_id": raw_row.get("protacxn", ""),
        "gene_name": raw_row.get("genename", ""),
        "action": raw_row.get("action", ""),
        "evidences": raw_row.get("evids", ""),
        "evidence_urls": raw_row.get("evurls", ""),
    }


def write_compound_ids_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(COMPOUND_IDS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COMPOUND_ID_FIELDNAMES)
        writer.writeheader()
        for compound in DR_PHARMACOPOEIA_COMPOUNDS:
            writer.writerow({k: compound[k] for k in COMPOUND_ID_FIELDNAMES})
    print(f"Wrote compound ID mapping ({len(DR_PHARMACOPOEIA_COMPOUNDS)} compounds) -> {COMPOUND_IDS_FILE}")


def fetch_missing(missing_compounds):
    os.makedirs(DATA_DIR, exist_ok=True)
    file_exists = os.path.exists(INTERACTIONS_FILE)
    next_idx = 0
    if file_exists:
        with open(INTERACTIONS_FILE, newline="", encoding="utf-8") as f:
            next_idx = sum(1 for _ in csv.DictReader(f))

    with open(INTERACTIONS_FILE, "a", newline="", encoding="utf-8") as outf, \
         open(PROGRESS_FILE, "a", encoding="utf-8") as pf:
        writer = csv.DictWriter(outf, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()

        total = len(missing_compounds)
        for i, compound in enumerate(missing_compounds):
            cid = compound["pubchem_cid"]
            print(f"  [{i + 1}/{total}] {compound['compound_name']} (CID {cid})...")

            raw_rows = fetch_target_interactions_csv(cid)
            for raw_row in raw_rows:
                writer.writerow(row_from_interaction(raw_row, next_idx))
                next_idx += 1
            outf.flush()

            print(f"    {len(raw_rows)} interactions")

            pf.write(str(cid) + "\n")
            pf.flush()


def main():
    parser = argparse.ArgumentParser(
        description="Backfill PubChem target-interaction data for the DR pharmacopoeia compounds."
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what will be fetched, no API calls."
    )
    args = parser.parse_args()

    done_cids = load_done_cids()
    missing = [
        c for c in DR_PHARMACOPOEIA_COMPOUNDS if str(c["pubchem_cid"]) not in done_cids
    ]

    print(f"{len(DR_PHARMACOPOEIA_COMPOUNDS)} DR pharmacopoeia compounds total:")
    for c in DR_PHARMACOPOEIA_COMPOUNDS:
        status = "done" if str(c["pubchem_cid"]) not in {str(m["pubchem_cid"]) for m in missing} else "to fetch"
        print(f"  - {c['compound_name']} (CID {c['pubchem_cid']}, {c['source_plant']}) [{status}]")
    print(f"\n{len(DR_PHARMACOPOEIA_COMPOUNDS) - len(missing)} already done, {len(missing)} to fetch")

    if args.dry_run:
        print("\n--dry-run: no API calls made, no files written.")
        return

    write_compound_ids_file()

    if missing:
        fetch_missing(missing)
    else:
        print("No missing compounds to fetch.")

    print(f"Interactions written to {INTERACTIONS_FILE}")


if __name__ == "__main__":
    sys.exit(main())
