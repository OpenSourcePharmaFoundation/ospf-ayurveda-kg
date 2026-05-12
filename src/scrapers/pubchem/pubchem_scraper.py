#!/usr/bin/env python3
"""
PubChem Scraper for Phytochemical-Target Interaction Data

Maps Ayurvedic plant phytochemicals to PubChem compound IDs via IMPPAT,
then downloads chemical-target interaction data from PubChem for each compound.

Pipeline:
  1. Build IMPPAT URLs from plant names in the formulations CSV
  2. Scrape IMPPAT detail pages to extract PubChem compound IDs
  3. Download target interaction CSVs from PubChem for each compound
  4. Compile all interactions into a single Neo4j-ready CSV

Input:  data/raw/ayurvedic_formulation_good_candidates_oral_mucositis.csv
Output: data/processed/phytochem_imppatid_pubchem_id_url.csv
        data/interim/pubchem_target_interactions/*.csv
        data/processed/pubchem_phytochem_target_interactions.csv

Note: Step 3 downloads ~910 individual CSV files and takes 30-40 minutes.
      Ensure stable internet connection — failed downloads are silently skipped.
"""

import argparse
import csv
import glob
import json
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut

# Resolve paths relative to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
INTERIM_DIR = os.path.join(PROJECT_ROOT, "data", "interim")

DEFAULT_INPUT = os.path.join(RAW_DIR, "ayurvedic_formulation_good_candidates_oral_mucositis.csv")


def build_imppat_chem_urls(csv_path):
    """Build IMPPAT phytochemical page URLs from plant scientific names.

    This function was previously imported from imppat_processing.py (sideways
    dependency). Now inlined here to keep the PubChem scraper self-contained.
    """
    url_list = []
    file_df = pd.read_csv(csv_path)
    for row in file_df.iterrows():
        sci_name = row[1]["Scientific name of the ingredient"]
        sci_name_split = sci_name.split(" ")
        url = f"https://cb.imsc.res.in/imppat/phytochemical/{sci_name_split[0]}%20{sci_name_split[1]}"
        url_list.append(url)
    return url_list


def scrape_pubchem_ids(url_list_imppat, csv_path):
    """Map phytochemical names to IMPPAT IDs, PubChem IDs, and PubChem URLs.

    Scrapes IMPPAT phytochemical detail pages to extract PubChem compound links.
    """
    phytochem_dict = {}
    for url in url_list_imppat:
        r = requests.get(url)

        soup = beaut(r.content, "html.parser")
        table_phytochem = soup.find("table", id="table_id")
        for j in table_phytochem.find_all("tr")[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            if row[3] not in phytochem_dict.keys():
                imppatid = row[2]
                name = row[3]

                url_phytochem = "https://cb.imsc.res.in/imppat/phytochemical-detailedpage/" + imppatid
                p = requests.get(url_phytochem)

                soup2 = beaut(p.content, "html.parser")
                summary = soup2.find("div", {"class": "col-8 pt-0 mt-0 ml-2 pl-2"})
                url_data = summary.find_all("a", href=True)
                pubchem_url = url_data[0]["href"]

                url_split = pubchem_url.split("/")
                pubchemid = url_split[-1]
                phytochem_dict[name] = [name, imppatid, pubchem_url, pubchemid]

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    file = open(csv_path, "w+", newline="")
    with file:
        fieldnames = ["Name", "IMPPAT ID", "PubChem URL", "PubChem ID"]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        for key, value in phytochem_dict.items():
            writer.writerow(value)

    print(f"Mapped {len(phytochem_dict)} phytochemicals to PubChem IDs -> {csv_path}")


def download_target_interactions(urls_path, output_dir):
    """Download chemical-target interaction CSVs from PubChem for each compound."""
    os.makedirs(output_dir, exist_ok=True)
    file_df = pd.read_csv(urls_path, index_col=False)
    for index, row in file_df.iterrows():
        url = row[2]
        cid = url.split("/")[-1]
        scraping_url = (
            "https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?"
            "infmt=json&outfmt=csv&query="
            '{"download":"*","collection":"consolidatedcompoundtarget",'
            '"order":["cid,asc"],"start":1,"limit":10000000,'
            f'"downloadfilename":"pubchem_cid_{cid}_consolidatedcompoundtarget",'
            f'"where":{{"ands":[{{"cid":"{cid}"}}]}}}}'
        )
        attempts = 0
        while attempts < 4:
            try:
                df = pd.read_csv(scraping_url, delimiter=",", quotechar='"')
                df.to_csv(os.path.join(output_dir, f"{cid}_target_interactions.csv"))
                break
            except Exception:
                attempts += 1
                continue


def compile_target_interactions(csv_folder_path, output_path):
    """Compile all individual target interaction CSVs into one Neo4j-ready CSV."""
    dictionary_list = []
    files = glob.glob(os.path.join(csv_folder_path, "*.csv"))
    for filename in files:
        df = pd.read_csv(filename)
        if df.empty:
            continue
        for index, row in df.iterrows():
            new_row = {
                "interaction_id": row["id"],
                "cid": row["cid"],
                "info_source": row["dsn"],
                "pubchem_name": row["cmpdname"],
                "source_cmpnd_name": row["srccmpdname"],
                "source_gene_name": row["srctargetname"],
                "protein_name": row["protname"],
                "protein_id": row["protacxn"],
                "gene_name": row["genename"],
                "action": row["action"],
                "evidences": row["evids"],
                "evidence_urls": row["evurls"],
            }
            dictionary_list.append(new_row)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    neo4j_df = pd.DataFrame.from_dict(dictionary_list)
    neo4j_df.to_csv(output_path)
    print(f"Compiled {len(dictionary_list)} interactions from {len(files)} compounds -> {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Scrape PubChem for phytochemical-target interaction data")
    parser.add_argument("--input", help="Path to ayurvedic formulations CSV", default=DEFAULT_INPUT)
    parser.add_argument("--ids-only", action="store_true", help="Only scrape PubChem IDs (step 1-2)")
    parser.add_argument("--download-only", action="store_true", help="Only download target interactions (step 3)")
    parser.add_argument("--compile-only", action="store_true", help="Only compile existing CSVs (step 4)")
    args = parser.parse_args()

    ids_csv = os.path.join(PROCESSED_DIR, "phytochem_imppatid_pubchem_id_url.csv")
    interim_dir = os.path.join(INTERIM_DIR, "pubchem_target_interactions")
    compiled_csv = os.path.join(PROCESSED_DIR, "pubchem_phytochem_target_interactions.csv")

    run_all = not args.ids_only and not args.download_only and not args.compile_only

    if args.ids_only or run_all:
        url_list_chem = build_imppat_chem_urls(args.input)
        scrape_pubchem_ids(url_list_chem, ids_csv)

    if args.download_only or run_all:
        download_target_interactions(ids_csv, interim_dir)

    if args.compile_only or run_all:
        compile_target_interactions(interim_dir, compiled_csv)


if __name__ == "__main__":
    main()
