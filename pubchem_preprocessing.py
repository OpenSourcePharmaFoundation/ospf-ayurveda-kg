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
    '''file = open('phytochem_name_to_id.csv', 'w+', newline ='')
    with file:    
        w = csv.writer(file)
        w.writerows(phytochem_dict.items())
    print('done')
    '''
    url_id_dict={}
    url_id_dict_final={}
    for id in phytochem_dict.values():
        url = 'https://cb.imsc.res.in/imppat/phytochemical-detailedpage/' + id
        imppat_url_list_detail.append(url)
        url_id_dict[url]=id

    url_list = []
    print(len(url_id_dict))
    print(len(imppat_url_list_detail))
    for imppat_url in imppat_url_list_detail:
        r = requests.get(imppat_url) 
        if r.status_code!=200:
            print(imppat_url)
            print(r)

        # parsing html
        soup = beaut(r.content, 'html.parser')
        summary = soup.find('div',{"class":"col-8 pt-0 mt-0 ml-2 pl-2"})
        url_data = summary.find_all('a', href=True)
        url_list.append(url_data[0]['href'])
        url_id_dict_final[url_data[0]['href']]=url_id_dict[imppat_url]
    
    file = open('pubchem_url_to_imppat_id.csv', 'w+', newline ='')
    with file:    
        w = csv.writer(file)
        w.writerows(url_id_dict_final.items())

    return(url_list)''

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

# get pubchem url list based on list of plants (imppat listed pubchem url basically)
url_list_chem = ayur_form_to_IMPPAT_url_chem('./ayurvedic_formulation.csv')
url_list = phytochem_to_pubchem_url(url_list_chem,'./phytochemicals_cleaned.csv')
'''file = open('pubchem_urls.csv', 'w+', newline ='')
with file:    
    write = csv.writer(file)
    for val in url_list:
        write.writerow([val])

file_df = pd.read_csv('pubchem_urls.csv', header=None, index_col=False, sep='/n', engine='python')
url_list_new=[]
for index, row in file_df.iterrows():
    url_list_new.append(row[0].replace(',',''))
file = open('pubchem_urls_new.csv', 'w')
with file:    
    write = csv.writer(file)
    for val in url_list_new:
        write.writerow([val])
'''
        

