# import dependencies
import pandas as pd
import os

# turns local .csv files into pandas dataframes
def load_into_pd(local_file_paths):
    file_df_dict = {}
    for file_path in local_file_paths:
        file_df = pd.read_csv(file_path)
        file_df_dict[os.path.basename(file_path).split('.')[0]] = file_df
    return file_df_dict

# loads ayurvedic_formulation.csv into neo4j
def load_ayurvedic_formulation():
    

# loads all files necessary into neo4j
def load_into_neo4j():
    load_ayurvedic_formulation()

# scraping data

# cleaning and processing data 

# data structure

# graph

local_file_paths = ['./ayurvedic_formulation.csv']
