import pandas as pd

def import_df():
    df1 = pd.read_csv('disgenet_vdas/C0038362-Table 1.csv')
    df2 = pd.read_csv('disgenet_vdas/C1568868-Table 1.csv')

    df = pd.concat([df1, df2])
    return df

df = import_df()
# print(df)

# remove duplicate PMIDs
def remove_duplicate_pmids(df):
    pmid_list=[]
    i=0
    while i<len(df.index):
        row = df.iloc[i]    
        if row['PMID'] in pmid_list:
            df=df.drop(df.index[i])
        else:
            pmid_list.append(row['PMID'])
            i+=1
    return df

df = remove_duplicate_pmids(df)
# print(df)

df_biomarker = df.loc[df['Association_Type'] == 'Biomarker']
df_genvar = df.loc[df['Association_Type'] == 'GeneticVariation']
df_altexp = df.loc[df['Association_Type'] == 'AlteredExpression']

df_biomarker.to_csv('disgenet_vdas/disgenet__OM_biomarkers.csv')
df_genvar.to_csv('disgenet_vdas/disgenet__OM_genvars.csv')
df_altexp.to_csv('disgenet_vdas/disgenet__OM_altexps.csv')

