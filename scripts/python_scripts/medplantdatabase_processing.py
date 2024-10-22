# Import dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as beaut
import json
import csv

# Prepares urls from medicinal plant database of India for scraping to gather
# phytochemical data, taking in the path name for the 'ayurvedic formulations' csv.
# def ayur_form_to_medplantdata_url(csv_path):
#     url_list = []
#     file_df = pd.read_csv(csv_path)
#     print(file_df)
#     for row in file_df.iterrows():
#         sci_name = row[1]['Scientific name of the ingredient']
#         sci_name_split = sci_name.split(' ')
#         print("sci_name:")
#         print(sci_name)

def get_data():
    r = requests.get("https://bsi.gov.in/page/en/medicinal-plant-database")
    soup = beaut(r.content, 'html.parser')

    # Open CSV file for writing
    with open('medicinal_plants.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write headers to CSV
        writer.writerow(['Name of the Plant', 'Family', 'Common Name', 'Link'])
        
        # Find all table rows
        rows = soup.find_all('tr')
        
        # Loop through each row and extract required data
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                # Extract the plant name (including species name)
                plant_name = cols[1].get_text(separator=" ").strip()
                
                # Extract family name
                family_name = cols[2].get_text(separator=" ").strip()
                
                # Extract common name
                common_name = cols[3].get_text(separator=" ").strip()
                
                # Extract link
                link_tag = cols[4].find('a', href=True)
                if link_tag:
                    link = link_tag['href']
                    full_link = "https://archive.bsi.gov.in" + link
                else:
                    full_link = ''

                # Write row to CSV
                writer.writerow([plant_name, family_name, common_name, full_link])

    print("Data has been written to medicinal_plants.csv")

def main():
    get_data()
    # ayur_form_to_medplantdata_url()
    # Grab the content of the URL: https://bsi.gov.in/page/en/medicinal-plant-database
    #   Put it into BeautifulSoup
    #   Get each data point:
    #     Known information:
    #     - Each row section starts with <tr><td scope="row">{number}</td>
    #     - Example row:
    #       <tr>
    #         <td scope="row">
    #           1
    #         </td>
    #         <td class="text">
    #           <p class="MsoNormal"><em>
    #             Abelmoschus esculentus</em> (L.) Moench
    #           </p>
    #         </td>
    #         <td class="text">
    #           MALVACEAE
    #         </td>
    #         <td>
    #           Bhindi, Bhindi tori
    #         </td>
    #         <td>
    #           <a href="https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000003881&column=szBarcode" target="_blank" rel="noopener"> <img src="../../../../uploads/logos/Medilogo.png" alt="View Document" width="30" height="30"></a>
    #         </td>
    #       </tr>
    #     - 
    #   Grab <td scope="row">
    # 

if __name__ == "__main__":
    main()
