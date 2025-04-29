import pandas as pd
import requests
import cloudscraper
from bs4 import BeautifulSoup as beaut

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
    for i in range(1, 121):
        url = 'https://go.drugbank.com/drugs?approved=1&c=name&d=up&page='+str(i)
        url_list.append(url)
    return url_list

def get_single_drug_data(url):
    """
    CALLED LIKE THIS:
      get_single_drug_data(drugs[0]['url'])
    Scrape data from a single drug page.
    Args:
        url (str): URL of the drug page.
    """
    scraper = cloudscraper.create_scraper()
    res_data = scraper.get(url)

    soup = beaut(res_data.text, 'html.parser')

    # Container for extracted drug data
    drug_data = {}

    # TODO CONTINUE FROM HERE - GET DATA FROM THE DRUG PAGE FOUND IN THE LINK


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

    # Container for all extracted drugs
    drugs = []

    # Loop through each query result page URL, and scrape basic drug data
    count = 1
    for url in url_list:
        count = count + 1
        if (count > 3): break
        print("Processing URL:", url)
        get_query_result_page_data(url, drugs)

    print(drugs)

main()
