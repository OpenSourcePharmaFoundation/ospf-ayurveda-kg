#!/usr/bin/env python3
"""
DisGeNET Data Processor for Gene-Disease Associations

Offline mode (default): reads a DisGeNET gene-disease association export
(xlsx/tsv/csv, as manually downloaded from the DisGeNET website) and splits
it into separate CSVs by association type (Biomarker, GeneticVariation,
AlteredExpression).

API mode (--api): calls the DisGeNET v1 REST API directly. This requires a
registered API key (DISGENET_API_KEY env var) - see https://disgenet.com/.
The legacy, unauthenticated DisGeNET API has been retired.

Default (no args) reproduces the original Oral Mucositis behaviour exactly:
Input:  data/raw/disgenet_gdas.xlsx
Output: data/processed/disgenet__OM_biomarkers.csv
        data/processed/disgenet__OM_genvars.csv
        data/processed/disgenet__OM_altexps.csv
"""

import argparse
import os
import sys
import time

import pandas as pd
import requests

# Resolve paths relative to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

DEFAULT_DISEASE_SLUG = "OM"
DEFAULT_DISEASE_NAME = "Oral Mucositis"
DEFAULT_DISEASE_CUIS = ["C0038362", "C1568868"]

API_BASE_URL = "https://api.disgenet.com/api/v1/gda/summary"
API_REGISTRATION_URL = "https://disgenet.com/"
RATE_LIMIT_DELAY = 0.3

# Column schema shared between offline and API modes
GDA_COLUMNS = [
    "Disease",
    "Disease_id",
    "Gene",
    "Gene_id",
    "Score_gda",
    "Association_Type",
    " Type",
    "Original_DB",
    "Sentence",
    "PMID",
    "PMID_Year",
]

DEDUPE_SUBSET = ["PMID", "Gene", "Disease_id", "Association_Type"]


def _load_offline_input(raw_path):
    """Load a DisGeNET export file (xlsx, tsv, or csv) into a single DataFrame."""
    ext = os.path.splitext(raw_path)[1].lower()
    if ext in (".xlsx", ".xls"):
        data = pd.read_excel(raw_path, sheet_name=None)
        return pd.concat(list(data.values()))
    elif ext == ".tsv":
        return pd.read_csv(raw_path, sep="\t")
    else:
        return pd.read_csv(raw_path)


def _dedupe(all_data):
    """
    Deduplicate GDA records.

    The original implementation deduped on PMID alone, which silently
    discarded every gene after the first for any multi-gene paper. The
    correct dedupe key includes Gene/Disease_id/Association_Type so that
    distinct gene-disease-association records from the same paper are all
    kept.
    """
    subset = [c for c in DEDUPE_SUBSET if c in all_data.columns]

    old_style_unique = (
        len(all_data.drop_duplicates(subset=["PMID"]))
        if "PMID" in all_data.columns
        else len(all_data)
    )
    new_style_unique = (
        len(all_data.drop_duplicates(subset=subset)) if subset else len(all_data)
    )

    print(f"Dedup comparison - old style (PMID only): {old_style_unique} unique rows")
    print(f"Dedup comparison - new style ({subset}): {new_style_unique} unique rows")

    return all_data.drop_duplicates(subset=subset) if subset else all_data


def _write_outputs(unique_df, disease_slug):
    df_biomarker = unique_df.loc[unique_df["Association_Type"] == "Biomarker"]
    df_genvar = unique_df.loc[unique_df["Association_Type"] == "GeneticVariation"]
    df_altexp = unique_df.loc[unique_df["Association_Type"] == "AlteredExpression"]

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    biomarkers_path = os.path.join(
        PROCESSED_DIR, f"disgenet__{disease_slug}_biomarkers.csv"
    )
    genvars_path = os.path.join(PROCESSED_DIR, f"disgenet__{disease_slug}_genvars.csv")
    altexps_path = os.path.join(PROCESSED_DIR, f"disgenet__{disease_slug}_altexps.csv")

    df_biomarker.to_csv(biomarkers_path)
    df_genvar.to_csv(genvars_path)
    df_altexp.to_csv(altexps_path)

    print(f"Processed {len(unique_df)} unique records from DisGeNET")
    print(f"  Biomarkers: {len(df_biomarker)}")
    print(f"  Genetic Variations: {len(df_genvar)}")
    print(f"  Altered Expression: {len(df_altexp)}")


def process_disgenet(raw_path=None, disease_slug=DEFAULT_DISEASE_SLUG):
    """Process a DisGeNET export file into per-association-type CSVs."""
    if raw_path is None:
        raw_path = os.path.join(RAW_DIR, "disgenet_gdas.xlsx")

    all_data = _load_offline_input(raw_path)
    unique_df = _dedupe(all_data)
    _write_outputs(unique_df, disease_slug)


def _fetch_api_page(api_key, disease_cuis, page_number):
    headers = {"Authorization": api_key}
    params = {
        "disease": ",".join(f"UMLS_{c}" for c in disease_cuis),
        "page_number": page_number,
    }
    response = requests.get(API_BASE_URL, headers=headers, params=params, timeout=30)
    return response


def process_disgenet_api(disease_slug, disease_name, disease_cuis):
    """
    Pull gene-disease associations from the live DisGeNET API and map them
    into the same column schema as the offline mode.
    """
    api_key = os.environ.get("DISGENET_API_KEY")
    if not api_key:
        print(
            "ERROR: DisGeNET API mode requires a registered API key.\n"
            "Set the DISGENET_API_KEY environment variable to your key.\n"
            f"Register for a key at: {API_REGISTRATION_URL}",
            file=sys.stderr,
        )
        sys.exit(2)

    records = []
    page_number = 0
    while True:
        response = _fetch_api_page(api_key, disease_cuis, page_number)

        if response.status_code == 401:
            print(
                f"ERROR: DisGeNET API rejected the key (HTTP 401): {response.text}\n"
                f"Check DISGENET_API_KEY or re-register at: {API_REGISTRATION_URL}",
                file=sys.stderr,
            )
            sys.exit(2)

        if response.status_code != 200:
            print(
                f"ERROR: DisGeNET API returned HTTP {response.status_code}: {response.text}",
                file=sys.stderr,
            )
            sys.exit(1)

        payload = response.json()
        page_records = payload.get("payload", [])
        if not page_records:
            break

        for r in page_records:
            records.append(
                {
                    "Disease": disease_name,
                    "Disease_id": r.get("diseaseid", ""),
                    "Gene": r.get("symbolOfGene", r.get("gene_symbol", "")),
                    "Gene_id": r.get("geneNcbiID", r.get("gene_id", "")),
                    "Score_gda": r.get("score", ""),
                    "Association_Type": r.get(
                        "assocType", r.get("association_type", "")
                    ),
                    " Type": r.get("geneDiseaseType", ""),
                    "Original_DB": r.get("source", ""),
                    "Sentence": "",
                    "PMID": r.get("pmid", ""),
                    "PMID_Year": r.get("year", ""),
                }
            )

        page_number += 1
        time.sleep(RATE_LIMIT_DELAY)

    all_data = pd.DataFrame(records, columns=GDA_COLUMNS)
    unique_df = _dedupe(all_data)
    _write_outputs(unique_df, disease_slug)


def main():
    parser = argparse.ArgumentParser(
        description="Process DisGeNET gene-disease associations"
    )
    parser.add_argument(
        "--input", help="Path to DisGeNET export file (xlsx/tsv/csv)", default=None
    )
    parser.add_argument(
        "--disease-slug",
        default=DEFAULT_DISEASE_SLUG,
        help="Short slug used in output filenames (e.g. OM, DR)",
    )
    parser.add_argument(
        "--disease-name",
        default=DEFAULT_DISEASE_NAME,
        help="Human-readable disease label",
    )
    parser.add_argument(
        "--disease-cui",
        action="append",
        dest="disease_cuis",
        default=None,
        help="UMLS CUI for the disease (repeatable)",
    )
    parser.add_argument(
        "--api",
        action="store_true",
        help="Pull data from the live DisGeNET API instead of an offline file",
    )
    args = parser.parse_args()

    disease_cuis = args.disease_cuis if args.disease_cuis else DEFAULT_DISEASE_CUIS

    if args.api:
        process_disgenet_api(args.disease_slug, args.disease_name, disease_cuis)
    else:
        process_disgenet(raw_path=args.input, disease_slug=args.disease_slug)


if __name__ == "__main__":
    main()
