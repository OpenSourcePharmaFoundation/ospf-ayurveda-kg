#!/usr/bin/env python3
"""
IMPPAT Scraper for Ayurvedic Plant Phytochemical and Therapeutic Use Data

Scrapes the IMPPAT (Indian Medicinal Plants, Phytochemistry And Therapeutics)
database for phytochemical composition and therapeutic uses of plants found in
Ayurvedic formulations relevant to Oral Mucositis.

Input:  data/raw/ayurvedic_formulation_good_candidates_oral_mucositis.csv
Output: data/processed/imppat_plant_part_phytochemicals.json
        data/processed/imppat_plant_therapeutic_uses.json
"""

import argparse
import json
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut

# Resolve paths relative to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

DEFAULT_INPUT = os.path.join(RAW_DIR, "ayurvedic_formulation_good_candidates_oral_mucositis.csv")


def build_imppat_urls(csv_path, url_type="phytochemical"):
    """Build IMPPAT URLs from plant scientific names in the formulations CSV.

    Args:
        csv_path: Path to the ayurvedic formulations CSV.
        url_type: Either "phytochemical" or "therapeutics".

    Returns:
        List of IMPPAT URLs to scrape.
    """
    url_list = []
    file_df = pd.read_csv(csv_path)
    for row in file_df.iterrows():
        sci_name = row[1]["Scientific name of the ingredient"]
        sci_name_split = sci_name.split(" ")
        url = f"https://cb.imsc.res.in/imppat/{url_type}/{sci_name_split[0]}%20{sci_name_split[1]}"
        url_list.append(url)
    return url_list


def scrape_phytochemicals(url_list, json_path):
    """Scrape phytochemical and plant part data from IMPPAT."""
    phytochem_dict = {}

    for url in url_list:
        r = requests.get(url)
        plant_url = url.split("/")[-1]
        plant_name = plant_url.split("%")[0] + " " + plant_url.split("20")[-1]

        soup = beaut(r.content, "html.parser")
        table_phytochem = soup.find("table", id="table_id")
        phytochem_list = []
        for j in table_phytochem.find_all("tr")[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            phytochem_list.append((row[1], row[3]))
        phytochem_dict[plant_name] = phytochem_list

    d = [{"plant": key, "phytochemicals": value} for key, value in phytochem_dict.items()]
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w") as file:
        json.dump(d, file)

    print(f"Scraped phytochemicals for {len(phytochem_dict)} plants -> {json_path}")


def scrape_therapeutic_uses(url_list, json_path):
    """Scrape therapeutic use data from IMPPAT."""
    ther_dict = {}

    for url in url_list:
        r = requests.get(url)
        plant_url = url.split("/")[-1]
        plant_name = plant_url.split("%")[0] + " " + plant_url.split("20")[-1]

        soup = beaut(r.content, "html.parser")
        table_phytochem = soup.find("table", id="table_id")
        therapeutic_list = []
        for j in table_phytochem.find_all("tr")[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            therapeutic_list.append((row[2], row[4]))
        ther_dict[plant_name] = therapeutic_list

    d = [{"plant": key, "therapeutic_use": value} for key, value in ther_dict.items()]
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w") as file:
        json.dump(d, file)

    print(f"Scraped therapeutic uses for {len(ther_dict)} plants -> {json_path}")


def main():
    parser = argparse.ArgumentParser(description="Scrape IMPPAT for plant phytochemical and therapeutic data")
    parser.add_argument("--input", help="Path to ayurvedic formulations CSV", default=DEFAULT_INPUT)
    parser.add_argument("--chem-only", action="store_true", help="Only scrape phytochemical data")
    parser.add_argument("--ther-only", action="store_true", help="Only scrape therapeutic use data")
    args = parser.parse_args()

    chem_output = os.path.join(PROCESSED_DIR, "imppat_plant_part_phytochemicals.json")
    ther_output = os.path.join(PROCESSED_DIR, "imppat_plant_therapeutic_uses.json")

    scrape_both = not args.chem_only and not args.ther_only

    if args.chem_only or scrape_both:
        url_list_chem = build_imppat_urls(args.input, "phytochemical")
        scrape_phytochemicals(url_list_chem, chem_output)

    if args.ther_only or scrape_both:
        url_list_ther = build_imppat_urls(args.input, "therapeutics")
        scrape_therapeutic_uses(url_list_ther, ther_output)


if __name__ == "__main__":
    main()
