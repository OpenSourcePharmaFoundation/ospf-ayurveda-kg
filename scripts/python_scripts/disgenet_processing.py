import pandas as pd

def main():
    
    raw_path = 'data/raw/disgenet_gdas.xlsx'
    data = pd.read_excel(raw_path, sheet_name=None)
    
    all_data = pd.concat(list(data.values()))
    
    unique_df = all_data.drop_duplicates(subset=['PMID'])

    df_biomarker = unique_df.loc[unique_df['Association_Type'] == 'Biomarker']
    df_genvar = unique_df.loc[unique_df['Association_Type'] == 'GeneticVariation']
    df_altexp = unique_df.loc[unique_df['Association_Type'] == 'AlteredExpression']

    df_biomarker.to_csv('data/processed/disgenet__OM_biomarkers.csv')
    df_genvar.to_csv('data/processed/disgenet__OM_genvars.csv')
    df_altexp.to_csv('data/processed/disgenet__OM_altexps.csv')

if __name__ == "__main__":
    main()