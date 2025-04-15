import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut

# Returns dictionary in format {drug name : (id, target id)}
def drugs_from_indication_urls(url_list):
    row_list=[]
    # drug name : [id, target id]
    for url in url_list:
        res_data = requests.get(url)

        print("Response data:")
        print(res_data)

        disease_name = 'Oral mucositis'

        # parsing html
        soup = beaut(res_data.content, 'html.parser')
        table_drug_targets = soup.find('div',id="targets")
        for j in table_drug_targets.find_all('tr')[1:]:
            new_row = []
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            new_row = [row[1], row[0], row[2], row_data[2].find('a')['href'].split('/')[-1]]
            row_list.append(new_row)
    df = pd.DataFrame(row_list, columns=['Drug_name','Drug_ID','Target_name','Target_ID'])

    return(df)

# get target information from drugbank
def get_target_info(df):
    for i, row in df.iterrows():
        url = 'https://go.drugbank.com/bio_entities/'+row['Target_ID']
        r = requests.get(url)
        soup = beaut(r.content, 'html.parser')
        details = soup.find('dl')
        kind = details.find_all('dd')[1]
        if kind.text == 'protein':
            table = details.find('table')
            columns = table.find_all('td')
            uniprot_id = columns[1].text
            df.loc[i, "Target_uniprot"] = uniprot_id

            url_protein = 'https://go.drugbank.com/polypeptides/'+uniprot_id
            p = requests.get(url_protein)
            psoup = beaut(p.content, 'html.parser')
            pdetails = psoup.find('dl')
            pgene = pdetails.find_all('dd')[2]
            df.loc[i, "Gene"] = pgene.text

            psynonyms = pdetails.find_all('dd')[1]
            p_synonym_list = [i.text for i in psynonyms.find_all('li')]
            df.loc[i, "Target_synons"] = ', '.join(p_synonym_list)

    return(df)

url_list = ['https://go.drugbank.com/indications/DBCOND0060314',
            'https://go.drugbank.com/indications/DBCOND0020359',
            'https://go.drugbank.com/indications/DBCOND0054816',
            'https://go.drugbank.com/indications/DBCOND0031602']

drug_target_df = drugs_from_indication_urls(url_list)
print(drug_target_df)
updated_drug_target_df = get_target_info(drug_target_df)
updated_drug_target_df.to_csv('data/processed/drugbank_drug_targets.csv')
