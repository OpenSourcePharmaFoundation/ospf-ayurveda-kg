# import dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut
import json
import csv

# prepares IMPPAT urls for scraping phytochemical data taking in the path name for the 'ayurvedic formulations' csv
def ayur_form_to_IMPPAT_url_chem(csv_path):
    url_list = []
    file_df = pd.read_csv(csv_path)
    for row in file_df.iterrows():
        sci_name = row[1]['Scientific name of the ingredient']
        sci_name_split = sci_name.split(' ')
        url = 'https://cb.imsc.res.in/imppat/phytochemical/'+sci_name_split[0]+'%20'+sci_name_split[1]
        url_list.append(url)
    return(url_list)    

# scrape phytochemical data based on list of urls from IMPPAT
def url_IMPPAT_chem_pn(url_list, json_path, data_name):
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
    d = [{ 
    "plant": key,
    data_name: value
    } for key, value in phytochem_dict.items()]
    with open(json_path, "w") as file:
        json.dump(d, file)

# scrape phytochemical-part data based on list of urls from IMPPAT
def url_IMPPAT_chem_part(url_list, json_path, data_name):
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
            phytochem_list.append((row[1],row[3]))
        phytochem_dict[plant_name]=phytochem_list
    
    # write json
    d = [{ 
    "plant": key,
    data_name: value
    } for key, value in phytochem_dict.items()]
    with open(json_path, "w") as file:
        json.dump(d, file)

## scraping IMPPAT phytochemical data based on taxonomical plant names
url_list_chem = ayur_form_to_IMPPAT_url_chem('./ayurvedic_formulation.csv')
url_IMPPAT_chem_part(url_list_chem, 'plant_phytochemicals_parts.json', "phytochemicals")

        

