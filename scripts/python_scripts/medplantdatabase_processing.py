#import dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut
import json

#prepares urls from medicinal plant database of India for scraping to gather phytochemical data, taking in the path name for the 'ayurvedic formulations' csv.
def ayur_form_to_medplantdata_url(csv_path):
  url_list = []
  file_df = pd.read_csv(csv_path)
  for row in file_df.iterrows():
    sci_name = row[1]['Scientific name of the ingredient']
    sci_name_split = sci_name.split(' ')
    
