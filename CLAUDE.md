# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OSPF Ayurveda Knowledge Graph - A Neo4j-based knowledge graph integrating Ayurvedic and Western medicine pathways for treating Oral Mucositis (OM). The project combines data from multiple biomedical databases to help repurpose existing drugs and Ayurvedic formulations through scientific understanding of their mechanisms.

## Commands

### Environment Setup
```bash
# Create virtual environment (if not exists)
python3 -m venv ./venv

# Activate virtual environment
source ./venv/bin/activate

# Install dependencies
python3 -m pip install -r ./requirements.txt
```

### Data Processing
```bash
# Process individual databases (WARNING: runtime can from 30 min to several hours due to API rate limits) 
python scripts/python_scripts/disgenet_processing.py
python scripts/python_scripts/imppat_processing.py
python scripts/python_scripts/pubchem_processing.py
python scripts/python_scripts/chembl/chembl_drug_data_scrape.py
python scripts/python_scripts/drugbank/drugbank_processing.py
python scripts/python_scripts/medplantdatabase_processing.py

# Format Python code
black scripts/python_scripts/
```

### Neo4j Setup
```bash
# Neo4j Desktop configuration steps:
# 1. Create new DBMS
# 2. Install APOC plugin through Neo4j Desktop UI
# 3. Copy scripts/cypher_scripts/apoc.conf to DBMS Configuration folder
# 4. Copy all data/processed/*.csv and data/raw/*.csv files to DBMS Import folder
# 5. Start DBMS and run numbered Cypher scripts in order:
#    - 1_uniqueness_constraints.txt
#    - 2_formulation_plant_compound_target.txt
#    - 3_disease_drug_target.txt
#    - analysis_queries.txt (for exploration)
```

### Testing
No automated test suite currently exists. Manual validation through:
- Checking output files in `data/processed/`
- Verifying Neo4j import success
- Running analysis queries in Neo4j

## Architecture

### Data Pipeline
1. **Collection**: Web scraping scripts in `scripts/python_scripts/` fetch data from DisGeNET, DrugBank, IMPPAT, PubChem, ChemBL, MedPlantDatabase, and TTD
2. **Processing**: Data cleaned and formatted for Neo4j import, stored in `data/processed/`
3. **Graph Creation**: Cypher scripts in `scripts/cypher_scripts/` load data into Neo4j with defined relationships
4. **Analysis**: Query the knowledge graph to find connections between existing drugs (including Ayurvedic compounds), and disease targets

### Key Components

#### Data Sources & Processing Scripts
- **DisGeNET** (`disgenet_processing.py`): Gene-drug associations for Oral Mucositis and Stomatitis
- **DrugBank** (`drugbank/`): Drug target information for OM-related indications
  - Deprecated - it's proprietary and not easily available for public scraping
- **IMPPAT** (`imppat_processing.py`): Indian (as in the country of India) medicinal plants, phytochemicals, and therapeutic uses
- **PubChem** (`pubchem_processing.py`): Chemical-gene and chemical-protein interactions
- **ChemBL** (`chembl/chembl_drug_data_scrape.py`): Approved small molecule drugs with mechanisms and targets
- **MedPlantDatabase** (`medplantdatabase_processing.py`): Additional medicinal plant data
- **TTD**: Therapeutic target database (manual compilation in `data/processed/`)

#### Neo4j Schema
- **Nodes**: Disease, Gene, Drug, Compound, Plant, Formulation, Protein, Therapeutic_Area
- **Relationships**: TARGETS, TRANSLATES, CONTAINS, TREATS, ASSOCIATED_WITH
- **Constraints**: Unique constraints on key identifiers for each node type

### Important Patterns
- Processing scripts use pandas for data manipulation
- BeautifulSoup for HTML parsing when APIs unavailable
- Rate limiting implemented with `time.sleep()` to respect API limits (0.2-1s delays)
  - ...but not everywhere. Check databases' rules for this first to determine if this is necessary
- Data stored as CSV/JSON files optimized for Neo4j's LOAD CSV command
- Cypher scripts numbered to indicate execution order
- CSV field escaping utility in `chembl/utils/escape_csv_field.py` for handling commas in data

## Development Notes

### Current Status
- Active development on ChemBL integration (branch: scraping-chembl)
- Some ChemBL data fields need comma escaping (indications, warnings, synonyms, mechanisms)

### Important Warnings
- Processing scripts can take 30minutes to several hours due to API rate limits (and the quantity of data to download and process)
- Neo4j Desktop requires manual APOC plugin installation and apoc.conf configuration
- Do NOT re-run successful Cypher functions - can cause node/relationship duplication
- Data files in `data/raw/` should not be modified directly - use processing scripts

### File Structure
```
data/
├── raw/                    # Original data files (do not modify)
├── processed/              # Neo4j-ready CSV files
├── interim/                # Intermediate processing files
└── archive (old files)/    # Historical PubChem target interactions

scripts/
├── python_scripts/         # Data collection and processing
│   ├── chembl/            # ChemBL drug data scraping
│   ├── drugbank/          # DrugBank web scraping
│   └── *.py               # Database-specific processors
├── cypher_scripts/        # Neo4j graph creation scripts
│   ├── 1_uniqueness_constraints.txt
│   ├── 2_formulation_plant_compound_target.txt
│   ├── 3_disease_drug_target.txt
│   ├── analysis_queries.txt
│   └── apoc.conf          # APOC configuration
└── setup/                 # Environment setup scripts

docs/
├── databases/             # Database-specific documentation
├── todos/todo.md         # Active development tasks
└── project-info.md       # Project background information
```

### Dependencies
- Python 3.x with virtualenv
- beautifulsoup4==4.12.3
- pandas==2.2.3
- requests==2.32.3
- black (for code formatting)
- Neo4j Desktop with APOC plugin

