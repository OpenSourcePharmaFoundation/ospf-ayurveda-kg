# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OSPF Ayurveda Knowledge Graph - A Neo4j-based knowledge graph integrating Ayurvedic and Western medicine pathways for treating Oral Mucositis (OM). The project combines data from multiple biomedical databases to help repurpose Ayurvedic formulations through scientific understanding of their mechanisms.

## Commands

### Environment Setup
```bash
# Activate virtual environment
source ./venv/bin/activate

# Install dependencies
python3 -m pip install -r ./requirements.txt
```

### Data Processing
```bash
# Process individual databases (30-40 min runtime due to API limits)
python scripts/python_scripts/disgenet_processing.py
python scripts/python_scripts/imppat_processing.py
python scripts/python_scripts/pubchem_processing.py
python scripts/python_scripts/chembl/chembl_drug_data_scrape.py

# Format Python code
black scripts/python_scripts/
```

### Testing
No automated test suite currently exists. Manual validation through:
- Checking output files in `data/processed/`
- Verifying Neo4j import success
- Running analysis queries in Neo4j

## Architecture

### Data Pipeline
1. **Collection**: Web scraping scripts in `scripts/python_scripts/` fetch data from DisGeNET, DrugBank, IMPPAT, PubChem, ChemBL, and TTD
2. **Processing**: Data cleaned and formatted for Neo4j import, stored in `data/processed/`
3. **Graph Creation**: Cypher scripts in `scripts/cypher_scripts/` load data into Neo4j with defined relationships
4. **Analysis**: Query the knowledge graph to find connections between Ayurvedic compounds and disease targets

### Key Components
- **Data Sources Integration**: Each database has dedicated processing scripts that handle API calls, rate limiting, and data formatting
- **Neo4j Schema**: Nodes include Disease, Gene, Drug, Compound, Plant, Formulation; relationships capture therapeutic targets, gene associations, and chemical interactions
- **APOC Plugin Required**: Extended Neo4j functionality for complex data loading operations

### Important Patterns
- Processing scripts use pandas for data manipulation
- BeautifulSoup for HTML parsing when APIs unavailable
- Rate limiting implemented with time.sleep() to respect API limits
- Data stored as CSV files optimized for Neo4j's LOAD CSV command
- Cypher scripts numbered to indicate execution order

## Development Notes

- Current active development on ChemBL integration (branch: scraping-chembl)
- Processing scripts can take significant time due to API rate limits
- Neo4j Desktop setup requires manual configuration of APOC plugin and apoc.conf file
- Data files in `data/raw/` should not be modified directly - use processing scripts to regenerate `data/processed/` files