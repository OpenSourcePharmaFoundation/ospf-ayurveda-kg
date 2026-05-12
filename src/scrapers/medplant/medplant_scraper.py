#!/usr/bin/env python3
"""
Medicinal Plant Database Scraper

Scrapes the Botanical Survey of India (BSI) Medicinal Plant Database for plant
data and therapeutic uses. Two-phase process:
  1. Scrape the main plant listing for names, families, and detail page links
  2. For plants matching our Ayurvedic formulation ingredients, scrape the
     "Uses" block from each plant's detail page

Input:  BSI Medicinal Plant Database (https://bsi.gov.in/page/en/medicinal-plant-database)
Output: data/processed/medicinal_plants.csv (basic plant data)
        data/processed/medicinal_plants_with_uses.csv (with therapeutic uses)
"""

import argparse
import csv
import os
import re

import requests
from bs4 import BeautifulSoup as beaut

# Resolve paths relative to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

# Output file paths
MED_PLANTS_CSV = os.path.join(PROCESSED_DIR, "medicinal_plants.csv")
MED_PLANTS_USES_CSV = os.path.join(PROCESSED_DIR, "medicinal_plants_with_uses.csv")

# Scientific names of plants to match (from Ayurvedic formulations)
MATCHING_PLANTS = [
    "Alstonia scholaris",
    "Vetiveria zizanioides",
    "Trichosanthes dioica",
    "Cyperus rotundus",
    "Terminalia chebula",
    "Picrorhiza kurrooa",
    "Glycyrrhiza glabra",
    "Cassia fistula",
    "Santalum album",
    "Trichosanthes dioica",
    "Azadirachta indica",
    "Solanum xanthocarpum",
    "Tinspora cordifolia",
    "Adhatoda vasica",
]


def create_medplant_db_data_csv():
    """Scrape basic plant data from the BSI medicinal plant database.

    Fetches: Name, Family, Common Name, Link (to detail page).
    """
    print("Grabbing raw HTML from medicinal plant database...")
    r = requests.get("https://bsi.gov.in/page/en/medicinal-plant-database")

    print("Parsing raw HTML...")
    soup = beaut(r.content, "html.parser")

    print("Creating CSV file from return data...")
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    with open(MED_PLANTS_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name of the Plant", "Family", "Common Name", "Link"])

        rows = soup.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 4:
                plant_name = cols[1].get_text(separator=" ").strip()
                family_name = cols[2].get_text(separator=" ").strip()
                common_name = cols[3].get_text(separator=" ").strip()

                link_tag = cols[4].find("a", href=True)
                full_link = link_tag["href"] if link_tag else ""

                writer.writerow([plant_name, family_name, common_name, full_link])

    print(f"Data has been written to {MED_PLANTS_CSV}")


def check_plant_name(plant_name):
    """Check if a plant name matches any of the target Ayurvedic plants."""
    for plant in MATCHING_PLANTS:
        if re.search(rf"\b{re.escape(plant)}\b", plant_name, re.IGNORECASE):
            return True
    return False


def extract_uses(link):
    """Scrape the 'Uses' block from a plant's detail page."""
    print(f"Grabbing 'uses' data from {link}...")
    try:
        page = requests.get(link)
        soup = beaut(page.content, "html.parser")

        uses_block = None
        for p_tag in soup.find_all("p"):
            strong_tag = p_tag.find("strong")
            if strong_tag and "Uses:" in strong_tag.get_text():
                uses_block = p_tag
                break

        if uses_block:
            uses_text = uses_block.get_text(strip=True).replace("Uses:", "").strip()
            return uses_text
        else:
            return "Uses not found"

    except Exception as e:
        return f"Error retrieving uses: {str(e)}"


def process_and_write_csv_row_by_row(input_csv, output_csv):
    """Add 'Uses' column by scraping each plant's detail page.

    Only fetches uses for plants matching the target Ayurvedic formulation
    ingredients. All other plants get 'UNKNOWN USE'.
    """
    with open(input_csv, mode="r", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        header = next(reader)

        if os.path.exists(output_csv):
            print(f"Error: {output_csv} exists. Remove before running this script.")
            return

        with open(output_csv, mode="a", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Name of the Plant", "Family", "Common Name", "Link", "Uses"])

            current_row = 0
            for row in reader:
                plant_name, family, common_name, link = row
                current_row += 1
                print(f"\nProcessing plant #{current_row} - {plant_name}")

                is_matching_plant = check_plant_name(plant_name)
                uses_text = extract_uses(link) if is_matching_plant else "UNKNOWN USE"
                uses_text = uses_text.replace("\n", " ").replace("\r", " ")
                uses_text = f'"{uses_text}"'

                print(f"Uses block for {plant_name}: {uses_text}")
                writer.writerow(row + [uses_text])
                print(f"#{current_row} Processed: {plant_name}")


def main():
    parser = argparse.ArgumentParser(description="Scrape BSI Medicinal Plant Database for plant data and uses")
    parser.add_argument("--listing-only", action="store_true", help="Only scrape the main plant listing (skip uses)")
    parser.add_argument("--uses-only", action="store_true", help="Only scrape uses (requires existing listing CSV)")
    args = parser.parse_args()

    run_all = not args.listing_only and not args.uses_only

    if args.listing_only or run_all:
        create_medplant_db_data_csv()

    if args.uses_only or run_all:
        process_and_write_csv_row_by_row(MED_PLANTS_CSV, MED_PLANTS_USES_CSV)
        print(f"All 'Uses' data has been gathered and written to {MED_PLANTS_USES_CSV}")


if __name__ == "__main__":
    main()
