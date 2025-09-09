# ChemBL Data Scraping Plan for Drug Repurposing & Ayurvedic Formulation

## Overview
This plan outlines a comprehensive approach to scraping ChemBL data relevant for drug repurposing and Ayurvedic formulation mapping, with a focus on oral mucositis treatment pathways.

## Phase 1: Core Drug & Molecule Data Collection

### 1.1 Approved & Clinical Stage Drugs
- **Endpoint**: `/molecule?max_phase=4` (approved drugs)
- **Data to collect**:
  - ChEMBL ID, name, synonyms
  - SMILES, InChI, molecular formula
  - Molecular weight, LogP, LogD
  - Bioavailability, permeability
  - Rule of Five violations
  - First approval year, indication areas
  - Natural product classification

### 1.2 Natural Products & Plant-Derived Compounds
- **Endpoint**: `/molecule?natural_product=1`
- **Rationale**: Critical for Ayurvedic compound mapping
- **Additional filters**: 
  - Include semi-synthetic derivatives
  - Cross-reference with IMPPAT compound IDs where possible

## Phase 2: Pharmacological Data

### 2.1 Drug Mechanisms
- **Endpoint**: `/mechanism`
- **Data to collect**:
  - Mechanism of action descriptions
  - Target interactions (agonist/antagonist/inhibitor)
  - Action type classifications
  - References/citations

### 2.2 Drug Indications
- **Endpoint**: `/drug_indication`
- **Data to collect**:
  - Therapeutic areas
  - Disease/condition mappings
  - EFO (Experimental Factor Ontology) terms
  - Clinical phase for each indication

### 2.3 Metabolism & Pharmacokinetics
- **Endpoint**: `/metabolism`
- **Data to collect**:
  - Metabolizing enzymes (CYP450s)
  - Metabolite information
  - Half-life, clearance rates
  - Drug-drug interaction potential

## Phase 3: Target & Activity Data

### 3.1 Drug Targets
- **Endpoint**: `/target`
- **Filter**: Targets linked to approved drugs
- **Data to collect**:
  - Target name, type (protein/enzyme/receptor)
  - UniProt accessions
  - Organism (focus on human)
  - Target family classifications

### 3.2 Bioactivity Data
- **Endpoint**: `/activity`
- **Filters**: 
  - Standard activity types (IC50, EC50, Ki, Kd)
  - Human targets primarily
  - Confidence score ≥ 7
- **Data to collect**:
  - Activity values and units
  - Assay descriptions
  - Target-compound relationships

## Phase 4: Safety & Adverse Effects

### 4.1 Drug Warnings
- **Endpoint**: `/drug_warning`
- **Data to collect**:
  - Black box warnings
  - Withdrawn drugs and reasons
  - Safety classifications

### 4.2 Side Effects & Toxicity
- **Endpoint**: Query molecules with toxicity flags
- **Data to collect**:
  - hERG inhibition
  - Cytotoxicity markers
  - Genotoxicity indicators

## Phase 5: Structural & Chemical Properties

### 5.1 Structural Alerts
- **Endpoint**: `/molecule_form`
- **Data to collect**:
  - PAINS (Pan-Assay Interference) flags
  - Reactive group alerts
  - Aggregator predictions

### 5.2 Physicochemical Properties
- **Data to collect** (selective, not exhaustive):
  - Polar surface area (PSA)
  - Hydrogen bond donors/acceptors
  - Rotatable bonds
  - Aromatic rings count
  - Solubility classifications

## Implementation Strategy

### Technical Approach:
1. **Rate Limiting**: Implement 0.2-1s delays between API calls
2. **Pagination**: Handle large result sets with offset/limit parameters
3. **Error Handling**: Retry logic for failed requests
4. **Data Format**: Request JSON format for easier processing

### Data Processing Pipeline:
1. **Initial Collection**: Start with approved drugs (max_phase=4)
2. **Enrichment**: For each drug, collect associated mechanisms, targets, activities
3. **Natural Product Mapping**: Cross-reference with existing Ayurvedic compound databases
4. **CSV Generation**: Format for Neo4j import with proper escaping

### Priority Filtering for Oral Mucositis Relevance:
- Anti-inflammatory agents
- Immunomodulators
- Mucosal protectants
- Antimicrobials
- Growth factors & healing promoters
- Pain management compounds

## Output Structure
```
data/processed/
├── chembl_approved_drugs.csv
├── chembl_natural_products.csv
├── chembl_drug_targets.csv
├── chembl_drug_mechanisms.csv
├── chembl_drug_indications.csv
├── chembl_bioactivities.csv
└── chembl_drug_warnings.csv
```

## Estimated Data Volume & Timeline
- **Approved drugs**: ~2,500 compounds
- **Natural products**: ~5,000 compounds
- **Processing time**: 4-6 hours with rate limiting
- **Storage requirement**: ~500MB processed CSVs

## Next Steps

### Phase 1: Setup & Testing
- [ ] Review existing ChemBL scraping script at `scripts/python_scripts/chembl/chembl_drug_data_scrape.py`
- [ ] Test ChemBL API connectivity with a simple request to `/status` endpoint
- [ ] Verify rate limiting works (0.2-1s delays between requests)
- [ ] Test pagination handling with `/molecule?max_phase=4&limit=10&offset=0`
- [ ] Ensure CSV escaping utility at `scripts/python_scripts/chembl/utils/escape_csv_field.py` works correctly

### Phase 2: Core Drug Data Collection
- [ ] Create function to fetch approved drugs (`/molecule?max_phase=4`)
- [ ] Add fields: ChEMBL ID, pref_name, synonyms
- [ ] Add SMILES and InChI representations
- [ ] Add molecular properties (weight, LogP, LogD, Rule of Five)
- [ ] Add bioavailability and permeability data
- [ ] Add first approval year and indication areas
- [ ] Test with 10 sample drugs first
- [ ] Run full collection (~2,500 approved drugs)
- [ ] Save to `data/processed/chembl_approved_drugs.csv`

### Phase 3: Natural Products Collection
- [ ] Create function to fetch natural products (`/molecule?natural_product=1`)
- [ ] Include semi-synthetic derivatives
- [ ] Add natural product classification fields
- [ ] Test with 10 sample compounds
- [ ] Run full collection (~5,000 compounds)
- [ ] Save to `data/processed/chembl_natural_products.csv`

### Phase 4: Pharmacological Data
- [ ] Fetch drug mechanisms from `/mechanism` endpoint
- [ ] Link mechanisms to drug ChEMBL IDs
- [ ] Fetch drug indications from `/drug_indication` endpoint
- [ ] Include EFO terms and therapeutic areas
- [ ] Fetch metabolism data from `/metabolism` endpoint (if available)
- [ ] Save to `data/processed/chembl_drug_mechanisms.csv`
- [ ] Save to `data/processed/chembl_drug_indications.csv`

### Phase 5: Target Data
- [ ] Fetch targets for approved drugs from `/target` endpoint
- [ ] Filter for human targets primarily
- [ ] Include UniProt accessions and target types
- [ ] Link targets to drugs via activities
- [ ] Save to `data/processed/chembl_drug_targets.csv`

### Phase 6: Bioactivity Data
- [ ] Fetch activities from `/activity` endpoint for approved drugs
- [ ] Filter for standard activity types (IC50, EC50, Ki, Kd)
- [ ] Apply confidence score filter (≥ 7)
- [ ] Include assay descriptions
- [ ] Save to `data/processed/chembl_bioactivities.csv`

### Phase 7: Safety Data
- [ ] Fetch drug warnings from `/drug_warning` endpoint
- [ ] Include black box warnings and withdrawal reasons
- [ ] Check for toxicity flags in molecule properties
- [ ] Save to `data/processed/chembl_drug_warnings.csv`

### Phase 8: Data Integration
- [ ] Create mapping table between ChemBL and IMPPAT compound IDs
- [ ] Identify overlapping compounds between databases
- [ ] Generate summary statistics of collected data
- [ ] Validate all CSV files for Neo4j compatibility

### Phase 9: Neo4j Import Preparation
- [ ] Update Cypher scripts to include new ChemBL node types
- [ ] Define relationships between ChemBL drugs and existing nodes
- [ ] Test import with subset of data
- [ ] Document any data quality issues found

