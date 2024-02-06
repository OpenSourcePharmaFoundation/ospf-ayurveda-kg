import pandas as pd
import glob 
import requests
from bs4 import BeautifulSoup as beaut
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
'''
# scrape chemical-gene target interaction data based on list of urls from pubchem
 def url_pubchem_chem_target_csv(url_path, output_path):
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

                 
# selenium version
def pubchem_chem_target_csv(driver, url_path, output_path):
    file_df = pd.read_csv(url_path, header=None, index_col=False)
    #for index, row in file_df.iterrows():
        #url = row[0]
    url = 'https://pubchem.ncbi.nlm.nih.gov/compound/1107'
    try:
        driver.get(url)
    except:
        #break
        exit
    chem_tar_elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable("xpath",'//section[@id="Chemical-Target-Interactions"]//button'))
    chem_tar_elem.click()
    WebDriverWait(driver,10)
    print(chem_tar_elem.text)
    #interaction = chem_tar_elem.find_element("xpath",'//div[@class="sm:table-row-group"]/div[1]/div[4]')
    #print(interaction.text)
    exit
        
# get pubchem chemical-target interaction data based on pubchem url's
cService = webdriver.ChromeService(executable_path='/Users/smiti/Downloads/chromedriver')
driver = webdriver.Chrome(service = cService)
pubchem_chem_target_csv(driver, 'pubchem_urls_new.csv', 'phytochem_gene_interactions.csv')
'''

# download chemical-target interaction csv based on pubchem compound urls 
'''def chem_tar_csv_from_url(urls_path):
    file_df = pd.read_csv(urls_path, header=None, index_col=False)
    for index, row in file_df.iterrows():
        if(index>100):
            url = row[0]
            id=url.split('/')[-1]
            print(index)
            scraping_url = "https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=csv&query={%22download%22:%22*%22,%22collection%22:%22consolidatedcompoundtarget%22,%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10000000,%22downloadfilename%22:%22pubchem_cid_"+id+"_consolidatedcompoundtarget%22,%22where%22:{%22ands%22:[{%22cid%22:%22"+id+"%22}]}}"
            #data = requests.get(scraping_url)
            try:
                df = pd.read_csv(scraping_url, delimiter=',', quotechar='"')   
                df.to_csv("target_interactions/"+id+'_target_interactions.csv')
            except:
                continue
            

chem_tar_csv_from_url('pubchem_urls_new.csv')
'''

# create neo4j ready csv based on downloaded chemical-target interaction csv's from pubchem
def pubchem_target_csv_compilation(csv_folder_path, output_path):
    dictionary_list=[]
    files = glob.glob(csv_folder_path + "/*.csv") 
    for j in range(0, len(files)):
        
        filename = files[j]
        print(j)

        df = pd.read_csv(filename, index_col=None) 
        if df.empty:
            continue
        for index, row in df.iterrows():
            # filter out non-human interactions
            if(row['taxid']=='9606' or row['taxid']==9606):
                new_row={
                'interaction_id' : row['id'],
                'cid' : row['cid'],
                'info_source': row['dsn'],
                'pubchem_name' : row['cmpdname'],
                'source_cmpnd_name' : row['srccmpdname'],
                'source_gene_name' : row['srctargetname'],
                'gene_name' : row['genename'],
                'action' : row['action'],
                'evidences' : row['evids'],
                'evidence_urls' : row['evurls']}
                dictionary_list.append(new_row)
    neo4j_df = pd.DataFrame.from_dict(dictionary_list)                
    neo4j_df.to_csv(output_path)

pubchem_target_csv_compilation('target_interactions', 'neo4j_target_interactions.csv')

