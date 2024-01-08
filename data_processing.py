# import dependencies
import pandas as pd
import os

# turns local .csv files into pandas dataframes
def load_data(local_file_paths):
    file_df_dict = {}
    for file_path in local_file_paths:
        file_df = pd.read_csv(file_path)
        file_df_dict[os.path.basename(file_path)] = file_df
    return file_df_dict

# scraping data

# cleaning and processing data 

# data structure

# graph

local_file_paths = ['./ayurvedic_formulation.csv']
file_df_dict = load_data(local_file_paths)
print(file_df_dict['ayurvedic_formulation'])
