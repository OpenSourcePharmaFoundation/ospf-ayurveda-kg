import pandas as pd
import requests
import cloudscraper
from bs4 import BeautifulSoup as beaut

# Grab all drug list pages - from 1 to 120
#   Page general format:
#     https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=1
#     ...
#     https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=120

def get_drug_list_pages():
    url_list = []
    for i in range(1, 121):
        url = 'https://go.drugbank.com/drugs?approved=1&c=name&d=up&page='+str(i)
        url_list.append(url)
    return url_list

def get_drugs_from_list(url):
    # res_data = requests.get(url)

    scraper = cloudscraper.create_scraper()
    res_data = scraper.get(url)

    soup = beaut(res_data.text, 'html.parser')

    # Container for extracted drugs
    drugs = []

    table_rows = soup.select("table.table tbody tr")
    for row in table_rows:
      name_tag = row.select_one(".drug-name a")
      name = name_tag.text.strip()
      url = "https://go.drugbank.com" + name_tag["href"]

      weight_td = row.select_one(".weight-value")
      weight = weight_td.text.strip().split("\n")[0] if weight_td else None

      description = row.select_one(".description-value").text.strip()

      # Multiple categories can exist, separated by <span class="text-muted"> / </span>
      category_tags = row.select(".categories-value a")
      categories = [cat.text.strip() for cat in category_tags]

      drugs.append({
          "name": name,
          "weight": weight,
          "description": description,
          "categories": categories,
          "url": url
      })

    # rows = soup.find_all("tr")
    print(drugs)
    # table_drug_targets = soup.find('table', id="drugs-table")
    # print(table_drug_targets)
    # for j in table_drug_targets.find_all('tr')[1:]:
    #     new_row = []
    #     row_data = j.find_all('td')
    #     row = [i.text for i in row_data]
    #     new_row = [row[1], row[0], row[2], row_data[2].find('a')['href'].split('/')[-1]]
    #     print(new_row)

def main():
    url_list = get_drug_list_pages()
    count = 1
    for url in url_list:
        count = count + 1
        if (count > 2): break
        print("Processing URL:", url)
        get_drugs_from_list(url)

main()

    # # scrape drug data based on list of urls from DrugBank
    # drug_target_df = drugs_from_indication_urls(url_list)
    # print(drug_target_df)
    # updated_drug_target_df = get_target_info(drug_target_df)
    # updated_drug_target_df.to_csv('data/processed/drugbank_drug_targets.csv')


# # Returns dictionary in format {drug name : (id, target id)}
# def drugs_from_indication_urls(url_list):
#     row_list=[]
#     # drug name : [id, target id]
#     for url in url_list:
#         res_data = requests.get(url)

#         print("Response data:")
#         print(res_data)

#         disease_name = 'Oral mucositis'

#         # parsing html
#         soup = beaut(res_data.content, 'html.parser')
#         table_drug_targets = soup.find('div',id="targets")
#         for j in table_drug_targets.find_all('tr')[1:]:
#             new_row = []
#             row_data = j.find_all('td')
#             row = [i.text for i in row_data]
#             new_row = [row[1], row[0], row[2], row_data[2].find('a')['href'].split('/')[-1]]
#             row_list.append(new_row)
#     df = pd.DataFrame(row_list, columns=['Drug_name','Drug_ID','Target_name','Target_ID'])

#     return(df)

# # get target information from drugbank
# def get_target_info(df):
#     for i, row in df.iterrows():
#         url = 'https://go.drugbank.com/bio_entities/'+row['Target_ID']
#         r = requests.get(url)
#         soup = beaut(r.content, 'html.parser')
#         details = soup.find('dl')
#         kind = details.find_all('dd')[1]
#         if kind.text == 'protein':
#             table = details.find('table')
#             columns = table.find_all('td')
#             uniprot_id = columns[1].text
#             df.loc[i, "Target_uniprot"] = uniprot_id

#             url_protein = 'https://go.drugbank.com/polypeptides/'+uniprot_id
#             p = requests.get(url_protein)
#             psoup = beaut(p.content, 'html.parser')
#             pdetails = psoup.find('dl')
#             pgene = pdetails.find_all('dd')[2]
#             df.loc[i, "Gene"] = pgene.text

#             psynonyms = pdetails.find_all('dd')[1]
#             p_synonym_list = [i.text for i in psynonyms.find_all('li')]
#             df.loc[i, "Target_synons"] = ', '.join(p_synonym_list)

#     return(df)

# url_list = ['https://go.drugbank.com/indications/DBCOND0060314',
#             'https://go.drugbank.com/indications/DBCOND0020359',
#             'https://go.drugbank.com/indications/DBCOND0054816',
#             'https://go.drugbank.com/indications/DBCOND0031602']

# drug_target_df = drugs_from_indication_urls(url_list)
# print(drug_target_df)
# updated_drug_target_df = get_target_info(drug_target_df)
# updated_drug_target_df.to_csv('data/processed/drugbank_drug_targets.csv')
