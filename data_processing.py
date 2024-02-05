# import dependencies
import pandas as pd
import os
from bs4 import BeautifulSoup as beaut
import requests
import json
import csv

# turns local .csv files into pandas dataframes
def load_into_pd(local_file_paths):
    file_df_dict = {}
    for file_path in local_file_paths:
        file_df = pd.read_csv(file_path)
        file_df_dict[os.path.basename(file_path).split('.')[0]] = file_df
    return file_df_dict

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

# prepares IMPPAT urls for scraping therapeutic use data taking in the path name for the 'ayurvedic formulations' csv
def ayur_form_to_IMPPAT_url_ther(csv_path):
    url_list = []
    file_df = pd.read_csv(csv_path)
    for row in file_df.iterrows():
        sci_name = row[1]['Scientific name of the ingredient']
        sci_name_split = sci_name.split(' ')
        url = 'https://cb.imsc.res.in/imppat/therapeutics/'+sci_name_split[0]+'%20'+sci_name_split[1]
        url_list.append(url)
    return(url_list)

# prepares pubchem urls for scraping taking in the path name for the phytochemicals csv
def phytochem_to_pubchem_url(url_list_imppat, csv_path):
    phytochem_dict={}
    for url in url_list_imppat:
        r = requests.get(url) 
        
        # parsing html
        soup = beaut(r.content, 'html.parser') 
        table_phytochem = soup.find('table',id='table_id')
        for j in table_phytochem.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            phytochem_dict[row[3]]=row[2]
    imppat_url_list_detail = []
    for id in phytochem_dict.values():
        url = 'https://cb.imsc.res.in/imppat/phytochemical-detailedpage/' + id
        imppat_url_list_detail.append(url)

    url_list = []
    for imppat_url in imppat_url_list_detail:
        r = requests.get(imppat_url) 

        # parsing html
        soup = beaut(r.content, 'html.parser')
        summary = soup.find('div',{"class":"col-8 pt-0 mt-0 ml-2 pl-2"})
        url_data = summary.find_all('a', href=True)
        url_list.append(url_data[0]['href'])
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

# scrape therapeutic use data based on list of urls from IMPPAT
def url_IMPPAT_ther_to_json(url_list, json_path):
    ther_dict={}
    
    for url in url_list:
        r = requests.get(url) 
        plant_url = url.split('/')[-1]
        plant_name = plant_url.split('%')[0] + ' ' + plant_url.split('20')[-1]
        
        # parsing html
        soup = beaut(r.content, 'html.parser') 
        table_phytochem = soup.find('table',id='table_id')
        therapeutic_list=[]
        for j in table_phytochem.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            therapeutic_list.append((row[2], row[4]))
        ther_dict[plant_name]=therapeutic_list
    
    # write json
    d = [{ 
    "plant": key,
    "therapeutic_use": value
    } for key, value in ther_dict.items()]
    with open(json_path, "w") as file:
        json.dump(d, file)

# scrape chemical-gene target interaction data based on list of urls from pubchem
'''def url_pubchem_chem_target_json(url_path, csv_path):
    file_df = pd.read_csv(url_path)
    for row in file_df.iterrows():
        r = requests.get(url) 
        if r.status_code!=200:
            print(url)
        else:
            print('success')
            
'''

## scraping IMPPAT phytochemical data based on taxonomical plant names
'''url_list_chem = ayur_form_to_IMPPAT_url_chem('./ayurvedic_formulation.csv')
url_IMPPAT_chem_to_json(url_list_chem, 'plant_phytochemicals.json', "phytochemicals")
'''

## scraping IMPPAT therapeutic use data based on taxonomical plant names
'''url_list = ayur_form_to_IMPPAT_url_ther('./ayurvedic_formulation.csv')
url_IMPPAT_ther_to_json(url_list, 'plant_therapeutic_use.json')
'''

# local_file_paths = ['./ayurvedic_formulation.csv']

# cleaning phytochemicals.csv
'''
df = pd.read_csv("phytochemicals.csv", header=None) 
df_new = pd.DataFrame()
for index, row in df.iterrows():
    chem_name = row[0]
    df_new.loc[index, 0]=chem_name[1:-1]
    print(df_new.loc[index, 0])
df_new.to_csv("phytochemicals_cleaned.csv", header=None, index=None) 
'''

## scraping pubchem chemical-target interaction data based on phytochemical names
url_list_chem = ayur_form_to_IMPPAT_url_chem('./ayurvedic_formulation.csv')
url_list = phytochem_to_pubchem_url(url_list_chem,'./phytochemicals_cleaned.csv')
 
# opening the csv file in 'w+' mode
file = open('pubchem_urls.csv', 'w+', newline ='')
with file:    
    write = csv.writer(file)
    write.writerows(url_list)

#url_pubchem_chem_target_json('pubchem_urls.csv', 'phytochem_gene_interactions.csv')
