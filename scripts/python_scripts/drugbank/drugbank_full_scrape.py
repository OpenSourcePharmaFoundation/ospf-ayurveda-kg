import pandas as pd
import requests
import cloudscraper
import json
from bs4 import BeautifulSoup as beaut
from pprint import pprint

from drugbank_get_identification_data import get_dd_identification_data
from dd_get_pharmacology_data import extract_pharmacology_data, scrape_all_associated_conditions

GRAB_THIRD_AND_FOURTH_PAGE_ONLY = True

# Grab all drug list pages - from 1 to 120
#   Page general format:
#     https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=1
#     ...
#     https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=120
#

# Definitions
# -----------
# query_result_page: A single page of results from a drug search query.
# basic_drug_data: A single drug's data from a query result page. Contains the
#                  drug name, weight, description, categories, image_url, and url only.
# query_result_page_data: The data from a single query result page.
#                         Contains a list of basic_drug_data objects.
# drug_data: Comprehensive data on a drug, taken from the dedicated drug page.
#            These pages are found at the URLs in the basic_drug_data objects.


def get_drug_list_urls():
    """
    Returns a list of URLs for all drug search results pages on DrugBank.
    These pages link to every drug in drugbank (through the results table).

    As of 2025-04-28 there are 120 in total.

    :returns: list of URLs. e.g. [
      'https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=1',
      'https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=2',
      ...]
    """
    url_list = []
    for i in range(3, 121):
        url = 'https://go.drugbank.com/drugs?approved=1&c=name&d=up&page='+str(i)
        url_list.append(url)
    return url_list

def get_single_drug_data(drug):
    """
    CALLED LIKE THIS:
      get_single_drug_data(drugs[0]['url'])
    Scrape data from a single drug page.
    Args:
        url (str): URL of the drug page.
    """
    print("drug:")
    print(drug)
    scraper = cloudscraper.create_scraper()
    res_data = scraper.get(drug['url'])

    # Container for extracted drug data
    drug_data = {}

    soup = beaut(res_data.text, 'html.parser')

    drug_card_content = soup.select("div.card-content")
    # print("drug_card_content[0]:", drug_card_content[0])

    description = drug_card_content[0].select_one(".description").text.strip()

    drug_data = get_dd_identification_data(res_data.text)
    drug_data["description"] = description

    # print(drug_data)

    # For Associated Conditions - if you need to scrape additional pages
    base_url = "https://www.drugbank.com"
    # TODO: Get this from the drug data
    # drug_id = "DB09278"  # Example drug ID
    drug_data = extract_pharmacology_data(res_data.text)

    # CURRENTLY IT WORKS UP TO THE END OF THE PHARMACOLOGY DATA

    # NOTE: BELOW IS PROBLEMATIC - IT ONLY GETS 5 ASSOCIATED CONDITIONS,
    # AND NOT NECESSARILY THE FIRST 5.
    # all_conditions = scrape_all_associated_conditions(base_url, drug_id)
    # print("drug_data.keys():")
    # pprint(drug_data.keys())
    # drug_data['Associated Conditions'].extend(all_conditions)

    ## TODO GET THE REST OF THE ASSOCIATED CONDITIONS
    # PSEUDOCODE:
    # - Get the number of associated conditions from the drug data
    # - Check if there are more than 5 associated conditions
    # - If so, scrape the additional pages of associated conditions:
    #   Until end reached, repeat the following:
    #   - Use the base URL and drug ID to construct the URL for the next page of conditions
    #   - Make a request to the URL
    #   - Parse the response to extract the additional conditions
    #   - Add the additional conditions to the drug_data['Associated Conditions'] list

    # TODO
    #   GET THE REST OF THE ASSOCIATED CONDITIONS (past the first 5)
    #   - See note above for this
    #   TREAT THE DATA WE HAVE FROM THE DRUG DATA PAGE AS "COMPLETE" FOR NOW
    #   - We can get more data later if needed
    #   - For now, we can use the data we have in some initial Neo4j analyses
    #   CONTINUE FROM HERE [2025-05-26]

    # Extract the "Type" from the drug card (e.g. "Small Molecule")

    return drug_data

def get_query_result_page_data(url, drugs):
    """
    Get drug table data from a single drug query results page.
    Will not scrape data from all query results pages - just a single page.

    i.e. all basic drug data directly available at a URL like e.g.
    https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=2

    :returns: list of objects with basic drug data - all drugs on a single query
              drug query results page. Format (example):
    ```
    [
      {
        "name": "Abarelix",
        "weight": 156.269,
        "description": "For palliative treatment of advanced prostate cancer",
        "categories": ["Antioxidants", "Tocopherols"],
        "image_url": "https://go.drugbank.com/structures/DB00106/image.svg",
        "url": "https://go.drugbank.com/drugs/DB00106"
      },
      {...}
      ...
    ]
    ```
    """
    scraper = cloudscraper.create_scraper()
    res_data = scraper.get(url)

    soup = beaut(res_data.text, 'html.parser')

    table_rows = soup.select("table.table tbody tr")
    for row in table_rows:
      name_tag = row.select_one(".drug-name a")
      name = name_tag.text.strip()
      url = "https://go.drugbank.com" + name_tag["href"]

      weight_td = row.select_one(".weight-value")
      weight = weight_td.text.strip().split("\n")[0] if weight_td else None
      image_url = row.select_one(".image-value img")["src"] if row.select_one(".image-value img") else None

      description = row.select_one(".description-value").text.strip()

      # Multiple categories can exist, separated by <span class="text-muted"> / </span>
      category_tags = row.select(".categories-value a")
      categories = [cat.text.strip() for cat in category_tags]

      drugs.append({
          "name": name,
          "weight": weight,
          "description": description,
          "categories": categories,
          "image_url": image_url,
          "url": url
      })
    return drugs

def main():
    """
    Main function to scrape drug data from DrugBank.
    """
    url_list = get_drug_list_urls()
    print(url_list)

    # Container for all extracted drugs
    basic_drug_data = []

    # Loop through each query result page URL, and scrape basic drug data
    count = 1
    for url in url_list:
        count = count + 1
        if GRAB_THIRD_AND_FOURTH_PAGE_ONLY and count > 3: break
        print("Processing URL:", url)
        get_query_result_page_data(url, basic_drug_data)

    # Full drug data will be stored here (with data from each dedicated drug page)
    drugs = []

    # Loop through each drug in the list and scrape detailed data by grabbing
    # all data from the drug URL
    drug_count = 1
    for basic_drug in basic_drug_data:
        drug_count = drug_count + 1
        if (drug_count > 4): break
        # Get the drug data from the drug page
        drug_data = get_single_drug_data(basic_drug)
        drugs.append(drug_data)

    pprint(drugs)

main()
