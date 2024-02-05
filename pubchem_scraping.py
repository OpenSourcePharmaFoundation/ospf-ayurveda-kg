import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# scrape chemical-gene target interaction data based on list of urls from pubchem
''' def url_pubchem_chem_target_csv(url_path, output_path):
    with open(output_path, 'w+') as csvfile:
        csvwriter = csv.writer(csvfile)

    file_df = pd.read_csv(url_path, header=None, index_col=False)
    for index, row in file_df.iterrows():
        #url = row[0]
        url = 'https://pubchem.ncbi.nlm.nih.gov/compound/1107'
        id=url.split('/')[-1]
        data_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{}/JSON/'
        try:
            # r = requests.get(url)
            compound_info = requests.get(data_url.format(id))
        except:
            break

        for section in compound_info.json()['Record']['Section']:
            if section['TOCHeading']=="Chemical-Target Interactions":
                print(section)
            for sub_section in section['Section']:
                if sub_section['TOCHeading'] == 'Experimental Properties':
                    for sub_sub_section in sub_section['Section']:
                        if sub_sub_section['TOCHeading']=="Odor":
                            print(sub_sub_section['Information'][0]['Value']['StringWithMarkup'][0]['String'])
                            break
            #csvwriter.writerow([url, gene, action, evidence, source])
        
        # parsing html
        try:
            soup = beaut(r.content, 'html.parser') 
            chem_target_section = soup.find('section',id="Chemical-Target-Interactions")
            print(chem_target_section)
            chem_target_table = chem_target_section.find('div', {"class":"sm:table-row-group"})
            rows = chem_target_table.find_all('div')
            print(rows[0])
        except:
            break
'''
                 
# selenium version
def pubchem_chem_target_csv(driver, url_path, output_path):
    file_df = pd.read_csv(url_path, header=None, index_col=False)
    for index, row in file_df.iterrows():
        #url = row[0]
        url = 'https://pubchem.ncbi.nlm.nih.gov/compound/1107'
        try:
            driver.get(url)
        except:
            break
        interactions = driver.find_element("xpath",'//section[@id="Chemical-Target-Interactions"]/div[2]/div')
        print(interactions)

# //section[@id="Chemical-Target-Interactions"]/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[4]/a/span
        
# get pubchem chemical-target interaction data based on pubchem url's
cService = webdriver.ChromeService(executable_path='/Users/smiti/Downloads/chromedriver')
driver = webdriver.Chrome(service = cService)
pubchem_chem_target_csv(driver, 'pubchem_urls_new.csv', 'phytochem_gene_interactions.csv')