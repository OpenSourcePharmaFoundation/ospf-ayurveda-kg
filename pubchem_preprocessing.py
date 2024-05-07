# import dependencies
import pandas as pd
import os
from bs4 import BeautifulSoup as beaut
import requests
import json
import csv

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

    return(url_list)

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
        

