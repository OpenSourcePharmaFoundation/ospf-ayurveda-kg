import json
from bs4 import BeautifulSoup as beaut
import requests
import pandas as pd
from imppat_processing import ayur_form_to_IMPPAT_url_chem
import csv
import glob 
import os


# map name to IMPPAT ID, PubChem ID and PubChem url for each phytochemical
def phytochem_to_IMPPAT_id_PubChem_id_url(url_list_imppat, csv_path):
    phytochem_dict={}
    for url in url_list_imppat:
        r = requests.get(url) 
        
        # parsing html
        soup = beaut(r.content, 'html.parser') 
        table_phytochem = soup.find('table',id='table_id')
        for j in table_phytochem.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            if row[3] not in phytochem_dict.keys():
                imppatid = row[2]
                name = row[3]
                
                url_phytochem = 'https://cb.imsc.res.in/imppat/phytochemical-detailedpage/' + imppatid
                p = requests.get(url_phytochem) 

                # parsing html
                soup2 = beaut(p.content, 'html.parser')
                summary = soup2.find('div',{"class":"col-8 pt-0 mt-0 ml-2 pl-2"})
                url_data = summary.find_all('a', href=True)
                url = (url_data[0]['href'])

                url_split = url.split('/')
                pubchemid = url_split[-1]
                phytochem_dict[name]=[name, imppatid, url, pubchemid]
    
    file = open(csv_path, 'w+', newline ='')
    with file:  
        fieldnames = ['Name','IMPPAT ID', 'PubChem URL', 'PubChem ID']
        writer = csv.writer(file)
        writer.writerow(fieldnames)  
        for key, value in phytochem_dict.items():
            writer.writerow(value)
    return

# download chemical-target interaction csv's based on pubchem compound urls 
def chem_target_csv_from_url(urls_path, output_dir):
    file_df = pd.read_csv(urls_path, index_col=False)
    for index, row in file_df.iterrows():
        url = row[2]
        id=url.split('/')[-1]
        scraping_url = "https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=csv&query={%22download%22:%22*%22,%22collection%22:%22consolidatedcompoundtarget%22,%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10000000,%22downloadfilename%22:%22pubchem_cid_"+id+"_consolidatedcompoundtarget%22,%22where%22:{%22ands%22:[{%22cid%22:%22"+id+"%22}]}}"
        #data = requests.get(scraping_url)
        try:
            df = pd.read_csv(scraping_url, delimiter=',', quotechar='"')   
            df.to_csv(output_dir+"/"+id+'_target_interactions.csv')
        except:
            print(id)
            continue

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
                'protein_name' : row['protname'],
                'protein_id' : row['protacxn'],
                'gene_name' : row['genename'],
                'action' : row['action'],
                'evidences' : row['evids'],
                'evidence_urls' : row['evurls']}
                dictionary_list.append(new_row)
    neo4j_df = pd.DataFrame.from_dict(dictionary_list)                
    neo4j_df.to_csv(output_path)

'''## scraping phytochemical IMPPAT ID, PubChem ID and PubChem url data
url_list_chem = ayur_form_to_IMPPAT_url_chem('data/raw/ayurvedic_formulation.csv')
phytochem_to_IMPPAT_id_PubChem_id_url(url_list_chem, 'data/processed/phytochem_imppatid_pubchem_id_url.csv')
'''
## downloading chemical-target interaction data from PubChem into csv's (separate for each compound)
interim_files_dir = 'data/interim/new_pubchem_target_interactions'
if not os.path.exists(interim_files_dir):
    os.mkdir(interim_files_dir)
chem_target_csv_from_url('data/processed/phytochem_imppatid_pubchem_id_url.csv', interim_files_dir)


## compiling neo4j input file from chemical-target csv's downloaded above
'''pubchem_target_csv_compilation('data/interim/new_pubchem_target_interactions', 'pubchem_chemical_target_interactions.csv')
'''