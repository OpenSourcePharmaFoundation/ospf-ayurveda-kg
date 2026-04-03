# About this project

## Objective
The purpose of this project was to build a knowledge graph integrating pathways from Ayurveda and Western medicine relevant to the treatment of Oral Mucositis or Stomatitis (OM). It was created by Smiti Mittal under the mentorship of Dr. Nibedita Rath to aide the Open Source Pharma Foundation (OSPF)'s ongoing efforts to repurpose Ayurvedic formulations. The graph provides insights into possible mechanisms of action for existing use-cases of the included Ayurvedic formulations and can be used to generate novel hypotheses. We hope this project adds to the relatively new field of literature understanding Ayurvedic medicine through a data-driven, scientific lens.

---

## Summary

This is a **drug repurposing engine for Oral Mucositis (OM)** - a painful side effect of chemotherapy that currently has only 4 approved treatments. It finds existing compounds, both pharmaceutical drugs and Ayurvedic plant-derived compounds, that could treat OM.

The project bridges two medical traditions:

- The **Western pharmacology side** has 3,276 approved drugs with known molecular targets, mechanisms, and safety data (from ChemBL, DisGeNET, DrugBank, TTD)
- The **Ayurvedic medicine side** has formulations containing plants with 60,000+ documented phytochemical-protein interactions (from IMPPAT, PubChem, MedPlant DB)
- The **Neo4j knowledge graph** connects them through shared molecular targets and genes

The core hypothesis: if an Ayurvedic plant compound hits the same protein target as an approved drug that treats inflammation, and that protein is linked to OM through gene-disease associations, then that compound is a repurposing candidate worth investigating.

### What this enables

- **Drug repurposing** - Surface hundreds of candidates from 3,276 approved drugs by querying which ones target OM-associated genes
- **Scientific validation of Ayurvedic formulations** - Trace the path from formulation -> plant -> phytochemical -> protein target -> OM-associated gene, giving traditional medicine a molecular-level evidence base
- **Research prioritization** - Rank candidates by target relevance, safety profile, and drug-likeness instead of testing compounds randomly
- **Network pharmacology** - Analyze whether a multi-compound Ayurvedic formulation's ingredients work synergistically across multiple OM pathways

In short, this project translates *"this plant has been used in Ayurveda for mouth sores for centuries"* into *"this plant contains compound X, which inhibits protein Y, which is overexpressed in oral mucositis tissue, and approved drug Z works through the same mechanism"* - turning traditional knowledge into testable scientific hypotheses.

---

## Repository Overview
This repository contains four parts. The scripts/python_scripts folder contains Python code to scrape and process input data into a form suitable for loading into our graph in Neo4j Desktop. The 'data_files' folder contains both raw and processed data files that can be directly imported into Neo4j Desktop. Some of the processed data files don't have a corresponding raw data file. This is because the data is scraped by a script, formatted, and directly written into the processed file without saving any raw version. The scripts/cypher_scripts folder contains Cypher scripts to load this data into a graph in Neo4j Desktop and analyze the resulting grap to pull out significant hypotheses.

---

## Data Sources
### Ayurvedic Formulation Data
This contains ayurvedic formulation-plant species-phytochemical data and was provided by Dr. Nibedita Rath. We used the plant composition provided by her. The phytochemicals in this original dataset were not used. Instead, we scraped phytochemical data from the IMPPAT database described below.

### DisGeNET
This provides gene-drug associations compiled from several sources. For this project, our raw data was the download of all gene-drug associations for 'Oral Mucositis' and 'Stomatitis.' This can be downloaded from here: https://www.disgenet.org/browser/0/1/1/C1568868::C0038362/_a/_b./ in .xlsx format.

### DrugBank
This contains information on the therapeutic targets of various drugs. We used it to extract the drug targets of existing drugs for 4 indications similar to Oral Mucositis. Raw data is not available since it was scraped from the web programmatically.

### Indian Medicinal Plants, Phytochemistry And Therapeutics (IMPPAT)
This contains information on the phytochemicals in different plant parts and therapeutic uses of plants commonly used in Indian Ayurveda. Raw data is not available since it was scraped from the web programmatically.

### PubChem
We used PubChem to extract information on the chemical-gene and chemical-protein interactions associated with each phytochemical. For a given phytochemical-target interaction, if a protein and gene form are both listed, the interaction is represented as phytochemical-targets->protein, and gene-translates->protein. If only a gene form is mentioned, the interaction is represented as the phytochemical-targets->gene.
We could not find a simple way to determine through webscraping whether a given phytochemical-target interaction takes place at the protein level or by interference in transcription and translation (epigenetic level). So, a mapping from a phytochemical to a protein target may mechanistically be mediated by the corresponding gene. This information is not captured with full accuracy in the knowledge graph.
The scraped chemical-target interaction data is available in data/interim/pubchem_target_interactions with one file (labelled by PubChem ID) corresponding to each compound.

### Therapeutic Target Database (TTD)
This contains information on the therapeutic target genes of various drugs. We used it to extract the drug targets of existing drugs linked to Oral Mucositis. The data was compiled through manual search on the TTD website and is available at data/processed.

---

## Creating the Neo4j graph
The Cypher queries required to put all the processed data together and create a graph are in the scripts/cypher_scripts folder. These can be run in AuraDB or on Neo4j Desktop. Free instances of AuraDB get auto-deleted in 30 days if they are not used, so we preferred to use Neo4j Desktop for early development. The instructions for creating the graph are as follows:
1.  Create a new DBMS in Neo4j, following [these instructions](https://neo4j.com/docs/desktop-manual/current/operations/create-dbms/#:~:text=When%20you%20first%20open%20Neo4j,dropdown%20menu%20in%20your%20Project).
1.  Add all the files in the data/processed and data/raw folders to the 'import' folder of the Neo4j DBMS in question, following [these instructions](https://neo4j.com/docs/desktop-manual/current/operations/import-csv/#:~:text=Start%20by%20selecting%20a%20project,to%20access%20the%20Import%20folder). We will run the 'LOAD CSV' commands mentioned on this link in Step 4.
2.  Install the APOC plugin for the DBMS you have created, following [these instructions](https://neo4j.com/docs/apoc/current/installation/).
3.  Open the 'Configuration' folder (in the same menu as the 'Import' folder) and copy-paste the 'apoc.conf' file from scripts/cypher_scripts in this repository into the DBMS Configuration folder.
4.  Start the DBMS and open the instance. Run the numbered scripts in the cypher_scripts folder in ascending order. The whole script can be copy-pasted into Neo4j desktop and run at once.
    -   Note: In case a script fails, do not re-run the functions that ran successfully. Re-run the code starting from the failed function. Re-running functions can lead to duplication of nodes and relationships in the graph.

Once the graph has been created, you may run analytical queries on top of the graph. Examples of queries I have already run that generate interesting ranked lists and visuals are included in 'analysis_queries.txt'

If you would like to learn more about the hypotheses our team has generated from this data, our next steps, or our process, please reach out to Smiti Mittal at smitimittal@gmail.com or smiti@berkeley.edu, or Dr. Nibedita Rath at nibedita.rath@ospfound.org.

---
## Setup

1. Clone the repo.

2. Navigate into the repo folder (in the terminal), and set up a virtual environment:
```
python3 -m venv ./venv
```

3. Activate the virtual environment:
```
source ./venv/bin/activate
```

4. Install required packages:
```
python3 -m pip install -r ./requirements.txt
```
