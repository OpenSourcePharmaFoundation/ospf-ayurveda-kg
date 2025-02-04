# Import dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut
import json
import csv
import os
import re

# Medicinal plants csv paths
med_plants_csv="data/processed/medicinal_plants.csv"
med_plants_uses_csv="data/processed/medicinal_plants_with_uses.csv"

# Scientific names of plants to match
matching_plants = [
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
  "Adhatoda vasica"
]

def create_medplant_db_data_csv():
    """
    Grab basic data from medicinal plant database (no "uses" column):
        -   Name of Plant
        -   Family
        -   Common Name
        -   Link (to the plant-specific page - to scrape "uses" from)
    Write data to {med_plants_csv} csv file.
    """
    # Make request to page with all the Ayurvedic formations to get data on (it returns HTML)
    print("Grabbing raw HTML from medicinal plant database...")
    r = requests.get("https://bsi.gov.in/page/en/medicinal-plant-database")

    # Convert HTML response from URL to parseable object (for scraping)
    print("Parsing raw HTML...")
    soup = beaut(r.content, 'html.parser')

    # Create & open CSV file for writing
    print("Creating CSV file from return data...")
    with open(med_plants_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write headers to CSV file
        writer.writerow(['Name of the Plant', 'Family', 'Common Name', 'Link'])

        # Find all table rows
        rows = soup.find_all('tr')

        # Loop through each row and extract required data
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                # Extract the plant name (including species name)
                plant_name = cols[1].get_text(separator=" ").strip()

                # Extract family name
                family_name = cols[2].get_text(separator=" ").strip()

                # Extract common name
                common_name = cols[3].get_text(separator=" ").strip()

                # Extract link
                link_tag = cols[4].find('a', href=True)
                if link_tag:
                    full_link = link_tag['href']
                else:
                    full_link = ''

                # Write row to CSV
                writer.writerow([plant_name, family_name, common_name, full_link])

    print(f"Data has been written to {med_plants_csv}")

def check_plant_name(plant_name):
    """
    Use regex to look for any exact match of the plant name within the string.

    @param {string} plant_name Example: Abelmoschus manihot  (L.) Medik.
    @return {boolean} True if a match is found, false if not.
    """
    for plant in matching_plants:
        # Escape special characters and add word boundaries to ensure full match
        if re.search(rf'\b{re.escape(plant)}\b', plant_name, re.IGNORECASE):
            return True
    return False

def extract_uses(link):
    """
    Grab the "uses" block from the medicinal plant info (herbarium) page at
    the given URL.
    """
    print(f"Grabbing 'uses' data from {link}...")
    try:
        # Send a GET request to the URL
        page = requests.get(link)
        soup = beaut(page.content, 'html.parser')

        # Find the <p> tags and search for the one containing "Uses:"
        uses_block = None
        for p_tag in soup.find_all('p'):
            strong_tag = p_tag.find('strong')
            if strong_tag and 'Uses:' in strong_tag.get_text():
                uses_block = p_tag
                break

        if uses_block:
            # Get the text following the <strong>Uses:</strong> tag
            uses_text = uses_block.get_text(strip=True).replace('Uses:', '').strip()
            return uses_text
        else:
            return 'Uses not found'

    except Exception as e:
        return f'Error retrieving uses: {str(e)}'

def process_and_write_csv_row_by_row(input_csv, output_csv):
    """
    Process the previously downloaded medicinal plants database CSV (at {med_plants_csv}).
    Adds a "uses" column, by getting the data for it from the remote URL in the "Link" column.
    Filters out unwanted rows.

    Write result into a new csv, at {med_plants_uses_csv}.
    """
    with open(input_csv, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        # Read the header from the input CSV
        header = next(reader)

        # Exit with error if the output CSV exists and has content.
        if not os.path.exists(output_csv):
            print(f"No {med_plants_uses_csv} file found. Creating...")
        else:
            print(f"Error: {med_plants_uses_csv} exists. Remove before running this script.")
            exit()

        # Open the output CSV in append mode to write row-by-row
        with open(output_csv, mode='a', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            # Write headers to CSV file
            writer.writerow(['Name of the Plant', 'Family', 'Common Name', 'Link', 'Uses'])

            # Current row count for logging purposes
            current_row = 0

            # Loop through each row in the input CSV
            for row in reader:
                plant_name, family, common_name, link = row

                current_row = current_row + 1
                print(f"\nProcessing plant #{current_row} - {plant_name}")

                is_matching_plant = check_plant_name(plant_name)

                # Extract the "Uses" block content from the page at the link.
                # If plant_name doesn't match item in matching_plants, don't do the "uses" fetch.
                uses_text = extract_uses(link) if is_matching_plant else 'UNKNOWN USE'

                # Replace line breaks with spaces
                uses_text = uses_text.replace('\n', ' ').replace('\r', ' ')

                # Escape commas by surrounding the text with quotes
                uses_text = f'"{uses_text}"'

                print(f"Uses block for {plant_name}: {uses_text}")

                # Write the row to the output CSV with the extracted "Uses" content
                writer.writerow(row + [uses_text])
                print(f"#{current_row} Processed: {plant_name}")

def main():
    create_medplant_db_data_csv()
    process_and_write_csv_row_by_row(med_plants_csv, med_plants_uses_csv)
    print(f"All 'Uses' data has been gathered and written to {med_plants_uses_csv}")

if __name__ == "__main__":
    main()
