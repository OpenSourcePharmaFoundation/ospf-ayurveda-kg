#!/usr/bin/env python3
"""
DisGeNET Data Processor for Oral Mucositis Gene-Disease Associations

Reads the DisGeNET gene-disease association Excel file and splits it into
separate CSVs by association type (Biomarker, GeneticVariation, AlteredExpression).

Input:  data/raw/disgenet_gdas.xlsx
Output: data/processed/disgenet__OM_biomarkers.csv
        data/processed/disgenet__OM_genvars.csv
        data/processed/disgenet__OM_altexps.csv
"""

import argparse
import os
import pandas as pd

# Resolve paths relative to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")


def process_disgenet(raw_path=None):
    """Process DisGeNET Excel file into per-association-type CSVs."""
    if raw_path is None:
        raw_path = os.path.join(RAW_DIR, "disgenet_gdas.xlsx")

    data = pd.read_excel(raw_path, sheet_name=None)
    all_data = pd.concat(list(data.values()))
    unique_df = all_data.drop_duplicates(subset=["PMID"])

    df_biomarker = unique_df.loc[unique_df["Association_Type"] == "Biomarker"]
    df_genvar = unique_df.loc[unique_df["Association_Type"] == "GeneticVariation"]
    df_altexp = unique_df.loc[unique_df["Association_Type"] == "AlteredExpression"]

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    df_biomarker.to_csv(os.path.join(PROCESSED_DIR, "disgenet__OM_biomarkers.csv"))
    df_genvar.to_csv(os.path.join(PROCESSED_DIR, "disgenet__OM_genvars.csv"))
    df_altexp.to_csv(os.path.join(PROCESSED_DIR, "disgenet__OM_altexps.csv"))

    print(f"Processed {len(unique_df)} unique records from DisGeNET")
    print(f"  Biomarkers: {len(df_biomarker)}")
    print(f"  Genetic Variations: {len(df_genvar)}")
    print(f"  Altered Expression: {len(df_altexp)}")


def main():
    parser = argparse.ArgumentParser(description="Process DisGeNET gene-disease associations for Oral Mucositis")
    parser.add_argument("--input", help="Path to DisGeNET Excel file", default=None)
    args = parser.parse_args()

    process_disgenet(raw_path=args.input)


if __name__ == "__main__":
    main()
