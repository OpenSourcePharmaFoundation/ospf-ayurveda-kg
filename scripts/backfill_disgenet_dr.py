#!/usr/bin/env python3
"""
Backfill DisGeNET gene-disease associations for Diabetic Retinopathy.

The project's DisGeNET data is scoped to Oral Mucositis only (the original
target disease). This script fetches DR associations using the same scraper
module, producing:
    data/processed/disgenet__DR_biomarkers.csv
    data/processed/disgenet__DR_genvars.csv
    data/processed/disgenet__DR_altexps.csv

Two modes:
    --api     Pull from the DisGeNET REST API (requires DISGENET_API_KEY env var).
              Register for a key at https://disgenet.com/ (free tier available).

    --input FILE   Process a manually downloaded DisGeNET export (xlsx/tsv/csv).
              To download: go to https://disgenet.com/, search for
              "Diabetic Retinopathy" (UMLS C0011884), export the GDA table.

If neither flag is given, prints instructions and exits.

UMLS CUIs used:
    C0011884  Diabetic Retinopathy
    C0730285  Diabetic Macular Edema
"""

import argparse
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "src", "scrapers", "disgenet"))

from disgenet_scraper import process_disgenet, process_disgenet_api

DISEASE_SLUG = "DR"
DISEASE_NAME = "Diabetic Retinopathy"
DISEASE_CUIS = ["C0011884", "C0730285"]

PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")


def check_existing():
    """Report what DR gene-disease data already exists."""
    files = {
        "DisGeNET DR biomarkers": os.path.join(PROCESSED_DIR, "disgenet__DR_biomarkers.csv"),
        "DisGeNET DR genvars": os.path.join(PROCESSED_DIR, "disgenet__DR_genvars.csv"),
        "DisGeNET DR altexps": os.path.join(PROCESSED_DIR, "disgenet__DR_altexps.csv"),
        "Open Targets DR (alternate source)": os.path.join(PROCESSED_DIR, "opentargets__DR_gene_disease.csv"),
    }
    print("Existing DR gene-disease data:")
    any_disgenet = False
    for label, path in files.items():
        if os.path.exists(path):
            lines = sum(1 for _ in open(path)) - 1
            print(f"  ✅ {label}: {lines} records")
            if "DisGeNET" in label:
                any_disgenet = True
        else:
            print(f"  ❌ {label}: not found")
    return any_disgenet


def main():
    parser = argparse.ArgumentParser(
        description="Fetch DisGeNET gene-disease associations for Diabetic Retinopathy"
    )
    parser.add_argument(
        "--api", action="store_true",
        help="Pull from the DisGeNET REST API (requires DISGENET_API_KEY env var)"
    )
    parser.add_argument(
        "--input",
        help="Path to a manually downloaded DisGeNET export file (xlsx/tsv/csv)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show existing data status and exit"
    )
    args = parser.parse_args()

    has_disgenet = check_existing()

    if args.dry_run:
        if has_disgenet:
            print("\nDisGeNET DR data already exists. Re-run without --dry-run to overwrite.")
        else:
            print("\nNo DisGeNET DR data found. Run with --api or --input to fetch it.")
        return

    if not args.api and not args.input:
        print(
            "\nUsage — pick one:\n"
            "\n"
            "  API mode (needs a key):\n"
            "    export DISGENET_API_KEY='your-key-here'\n"
            "    python scripts/backfill_disgenet_dr.py --api\n"
            "\n"
            "  Offline mode (download the file first):\n"
            "    1. Go to https://disgenet.com/\n"
            "    2. Search for 'Diabetic Retinopathy' (UMLS C0011884)\n"
            "    3. Export the Gene-Disease Associations table\n"
            "    4. Run:\n"
            "       python scripts/backfill_disgenet_dr.py --input path/to/download.xlsx\n"
        )
        return

    if has_disgenet:
        print("\n⚠️  DisGeNET DR data already exists and will be overwritten.")

    if args.api:
        api_key = os.environ.get("DISGENET_API_KEY")
        if not api_key:
            print(
                "\n❌ DISGENET_API_KEY environment variable not set.\n"
                "Register for a free key at https://disgenet.com/\n"
                "Then: export DISGENET_API_KEY='your-key-here'",
                file=sys.stderr,
            )
            sys.exit(2)

        print(f"\nFetching DR associations from DisGeNET API...")
        print(f"  Disease: {DISEASE_NAME}")
        print(f"  CUIs: {', '.join(DISEASE_CUIS)}")
        process_disgenet_api(DISEASE_SLUG, DISEASE_NAME, DISEASE_CUIS)

    elif args.input:
        if not os.path.exists(args.input):
            print(f"❌ File not found: {args.input}", file=sys.stderr)
            sys.exit(1)

        print(f"\nProcessing offline DisGeNET export: {args.input}")
        process_disgenet(raw_path=args.input, disease_slug=DISEASE_SLUG)

    print("\nDone. Output files:")
    for suffix in ("biomarkers", "genvars", "altexps"):
        path = os.path.join(PROCESSED_DIR, f"disgenet__{DISEASE_SLUG}_{suffix}.csv")
        if os.path.exists(path):
            lines = sum(1 for _ in open(path)) - 1
            print(f"  {path} ({lines} records)")


if __name__ == "__main__":
    main()
