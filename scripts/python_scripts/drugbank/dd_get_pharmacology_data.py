import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd


def extract_pharmacology_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    data = {
        "Indication": "",
        "Associated Conditions": [],
        "Pharmacodynamics": "",
        "Mechanism of action": "",
        "Absorption": "",
        "Volume of distribution": "",
        "Protein binding": "",
        "Metabolism": "",
        "Route of elimination": "",
        "Half-life": "",
        "Clearance": "",
        "Toxicity": "",
        "Pathways": "",
        "Pharmacogenomic Effects/ADRs": "",
    }

    # Extract Indication
    indication = soup.find(id="indication")
    if indication:
        data["Indication"] = (
            indication.find_next_sibling("dd")
            .get_text(strip=True)
            .split("Reduce drug development")[0]
            .strip()
        )

    # Extract Associated Conditions
    associated_conditions = soup.find(id="associated-conditions")
    if associated_conditions:
        table = associated_conditions.find_next("table")
        if table:
            rows = table.find_all("tr")[1:]  # Skip header row
            for row in rows:
                cols = row.find_all(["td", "th"])
                if len(cols) >= 3:
                    condition = {
                        "Indication Type": cols[0].get_text(strip=True),
                        "Indication": cols[1].get_text(strip=True),
                        "Combined Product Details": cols[2].get_text(strip=True),
                    }
                    data["Associated Conditions"].append(condition)

    # Extract other pharmacology sections
    sections = [
        "pharmacodynamics",
        "mechanism-of-action",
        "absorption",
        "volume-of-distribution",
        "protein-binding",
        "metabolism",
        "route-of-elimination",
        "half-life",
        "clearance",
        "toxicity",
        "pathways",
        "pharmacogenomic-effects-adrs",
    ]

    for section in sections:
        element = soup.find(id=section)
        if element:
            dd = element.find_next_sibling("dd")
            if dd:
                text = dd.get_text(strip=True)
                # Remove locked content markers if present
                text = text.split("Improve decision support")[0].strip()
                text = text.split("Unlock the secrets")[0].strip()
                data[section.replace("-", " ").title()] = text

    return data


def scrape_all_associated_conditions(base_url, drug_id):
    scraper = cloudscraper.create_scraper()
    all_conditions = []
    page = 1
    per_page = 100  # Max per page

    while True:
        url = f"{base_url}/drugs/{drug_id}/drug_associated_conditions.json?page={page}&per_page={per_page}"
        response = scraper.get(url)

        if response.status_code != 200:
            break

        json_data = response.json()
        if not json_data.get("data"):
            break

        all_conditions.extend(json_data["data"])

        # Check if we've got all pages
        if len(all_conditions) >= json_data.get("recordsTotal", 0):
            break

        page += 1

    return all_conditions
