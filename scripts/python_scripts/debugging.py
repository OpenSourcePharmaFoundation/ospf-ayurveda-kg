import pandas as pd
import csv

df = pd.read_csv('data/processed/pubchem_phytochem_target_interactions.csv')
print(df['protein_name'].nunique())
