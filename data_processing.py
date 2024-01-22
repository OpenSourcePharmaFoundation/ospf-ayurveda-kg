# import dependencies
import pandas as pd
import os
from bs4 import BeautifulSoup as beaut
import requests
import json

# turns local .csv files into pandas dataframes
def load_into_pd(local_file_paths):
    file_df_dict = {}
    for file_path in local_file_paths:
        file_df = pd.read_csv(file_path)
        file_df_dict[os.path.basename(file_path).split('.')[0]] = file_df
    return file_df_dict

# prepares IMPPAT urls for scraping taking in the path name for the 'ayurvedic formulations' csv
def ayur_form_to_IMPPAT_url(csv_path):
    url_list = []
    file_df = pd.read_csv(csv_path)
    for row in file_df.iterrows():
        sci_name = row[1]['Scientific name of the ingredient']
        sci_name_split = sci_name.split(' ')
        url = 'https://cb.imsc.res.in/imppat/phytochemical/'+sci_name_split[0]+'%20'+sci_name_split[1]
        url_list.append(url)
    return(url_list)

# scrape data based on list of urls from IMPPAT
def url_IMPPAT_to_json(url_list, json_path):
    phytochem_dict={}
    
    for url in url_list:
        r = requests.get(url) 
        plant_url = url.split('/')[-1]
        plant_name = plant_url.split('%')[0] + ' ' + plant_url.split('20')[-1]
        
        # parsing html
        soup = beaut(r.content, 'html.parser') 
        table_phytochem = soup.find('table',id='table_id')
        phytochem_list=[]
        for j in table_phytochem.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            phytochem_list.append(row[3])
        phytochem_dict[plant_name]=phytochem_list
    
    # write json
    with open(json_path, "w") as file:
        json.dump(phytochem_dict, file)
# cleaning and processing data 

# data structure

# graph

## scraping IMPPAT data based on taxonomical plant names
url_list = ayur_form_to_IMPPAT_url('./ayurvedic_formulation.csv')
url_IMPPAT_to_json(url_list, 'plant_phytochemicals.json')

# local_file_paths = ['./ayurvedic_formulation.csv']


