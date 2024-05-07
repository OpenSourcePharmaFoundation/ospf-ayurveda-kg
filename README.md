# About this project
## Objective
The purpose of this project was to build a knowledge graph integrating pathways from Ayurveda and Western medicine relevant to the treatment of Oral Mucositis or Stomatitis (OM). It was created by Smiti Mittal under the mentorship of Dr. Nibedita Rath to aide the Open Source Pharma Foundation (OSPF)'s ongoing efforts to repurpose Ayurvedic formulations. The graph provides insights into possible mechanisms of action for existing use-cases of the included Ayurvedic formulations and can be used to generate novel hypotheses. We hope this project adds to the relatively new field of literature understanding Ayurvedic medicine through a data-driven, scientific lens.
## Repository Overview 
This repository contains four parts. The 'scripts' folder contains Python code to scrape and process input data into a form suitable for loading into our graph in Neo4j Desktop. The 'data_files' folder contains both raw and processed data files that can be directly imported into Neo4j Desktop. Some of the processed data files don't have a corresponding raw data file. This is because the data is scraped by a script, formatted, and directly written into the processed file without saving any raw version. The 'knowledge_graph' folder contains Cypher scripts to load this data into a graph in Neo4j Desktop. The 'analysis' folder contains Cypher scripts to analyze the resulting graph and pull out the most significant hypotheses. 
All scripts are written as a series of functions, trying to maximize reusability and customisability of these mini functions for other similar projects.
## Data Sources
### Ayurvedic Formulation Data
This contains ayurvedic formulation-plant species-phytochemical data and was provided by Dr. Nibedita Rath. We used the plant composition provided by her. The phytochemicals in this original dataset were not used. Instead, we scraped phytochemical data from the IMPPAT database described below.
### IMPPAT

### DisGeNET
This provides gene-drug associations compiled from several sources. For this project, our raw data was the download of all gene-drug associations for 'Oral Mucositis' and 'Stomatitis.' This can be downloaded from here: https://www.disgenet.org/browser/0/1/1/C1568868::C0038362/_a/_b./ in .xlsx format.