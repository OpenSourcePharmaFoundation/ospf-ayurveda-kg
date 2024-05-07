import json

'''
IMPORTANT: Can only be run after the imppat_processing.py script has already been run.
'''

# create list of phytochemicals using pre-scraped IMPPAT data
def list_phytochemicals(json_path):
    imppat_json = open(json_path)
    imppat_dict = json.load(imppat_json) 

    phytochems=set()
    for item in imppat_dict:
        if len(item['phytochemicals'])!=0:
            for chem in item['phytochemicals']:
                phytochems.add(chem[1])
        
    return phytochems


phytochems = list_phytochemicals("data/processed/imppat_plant_part_phytochemicals.json")