# ChemBL Data Collection Statistics Report

**Generated:** 2025-12-08 20:24:04
**Project:** OSPF Ayurveda Knowledge Graph

---

## 📊 Executive Summary

| Metric | Value |
|--------|-------|
| Total Datasets | 9 |
| Total Records | 14,565 |
| Total Storage | 6.44 MB |
| Unique Approved Drugs | 3,274 |


## 📁 Dataset Overview

| Dataset | Records | Size | Status |
|---------|---------|------|--------|
| Approved Drugs | 4,375 | 3.47 MB | ✅ Production |
| Natural Products | 25 | 12.7 KB | ⚠️ Test Data |
| Drug Mechanisms | 10 | 1.9 KB | ⚠️ Test Data |
| Drug Indications | 79 | 17.4 KB | ⚠️ Test Data |
| Drug Targets | 43 | 3.6 KB | ⚠️ Test Data |
| Bioactivities | 23 | 4.8 KB | ⚠️ Test Data |
| Drug Metabolism | 10,000 | 2.93 MB | ⚠️ Test Data |
| Drug Warnings | 9 | 2.6 KB | ⚠️ Test Data |
| Toxicity | 1 | 399 B | ⚠️ Test Data |


## 💊 Approved Drugs Analysis (Production Data)

### Key Metrics

- **Total Records:** 4,375
- **Unique ChemBL IDs:** 3,274
- **Unique Drug Names:** 3,274
- **File Size:** 3.47 MB
- **Columns:** 35
- **Approval Year Range:** 1934 - 2024
- **Drugs with Approval Year:** 4,094
- **Withdrawn Drugs:** 463


### Molecule Type Distribution

| Type | Count |
|------|-------|
| Small molecule | 4,375 |


### Approvals by Decade

| Decade | Count |
|--------|-------|
| 1930s | 9 |
| 1940s | 67 |
| 1950s | 259 |
| 1960s | 259 |
| 1970s | 329 |
| 1980s | 816 |
| 1990s | 576 |
| 2000s | 521 |
| 2010s | 802 |
| 2020s | 456 |


### Molecular Weight Statistics

- **Min:** 4.0 Da
- **Max:** 1793.12 Da
- **Mean:** 389.15 Da
- **Median:** 357.44 Da


### Column Completeness

| Column | Completeness |
|--------|--------------|
| chembl_id | ✅ 100.0% |
| pref_name | ✅ 100.0% |
| oral_bioavailability | ✅ 100.0% |
| natural_product | ✅ 100.0% |
| polymer_flag | ✅ 100.0% |
| molecule_type | ✅ 100.0% |
| max_phase | ✅ 100.0% |
| withdrawn_flag | ✅ 100.0% |
| molecular_formula | ✅ 98.4% |
| molecular_weight | ✅ 98.4% |
| synonyms | ✅ 98.1% |
| smiles | ✅ 94.1% |
| inchi | ✅ 94.1% |
| inchi_key | ✅ 94.1% |
| first_approval | ✅ 93.6% |
| alogp | ✅ 89.0% |
| hba | ✅ 89.0% |
| hbd | ✅ 89.0% |
| psa | ✅ 89.0% |
| rtb | ✅ 89.0% |
| ro5_violations | ✅ 89.0% |
| aromatic_rings | ✅ 89.0% |
| heavy_atoms | ✅ 89.0% |
| qed_weighted | ✅ 89.0% |
| therapeutic_areas | ⚠️ 79.7% |
| indication_class | ⚠️ 79.5% |
| logd | ❌ 0.0% |
| cx_logp | ❌ 0.0% |
| cx_logd | ❌ 0.0% |
| molecular_species | ❌ 0.0% |
| bioavailability_score | ❌ 0.0% |
| permeability | ❌ 0.0% |
| withdrawn_reason | ❌ 0.0% |
| withdrawn_year | ❌ 0.0% |
| withdrawn_country | ❌ 0.0% |


## 📋 Secondary Datasets (Test Data)

*Note: These datasets contain test data only (10-25 records each, except metabolism).*

*Full production runs needed for: natural products, mechanisms, indications, targets, bioactivities, warnings, toxicity.*


### Mechanisms

- Records: 10
- Unique Drugs: 7
- Unique Targets: 6
- Action Types: {'INHIBITOR': 7, 'RELEASING AGENT': 2, 'AGONIST': 1}
- Target Types: {'PROTEIN COMPLEX': 7, 'SINGLE PROTEIN': 2, 'PROTEIN FAMILY': 1}


### Indications

- Records: 79
- Unique Drugs: 10


### Targets

- Records: 43
- Unique Targets: 43
- Target Types: {'ORGANISM': 18, 'SINGLE PROTEIN': 13, 'PROTEIN FAMILY': 6, 'PROTEIN COMPLEX': 3, 'UNCHECKED': 1}


### Warnings

- Records: 9
- Unique Drugs: 5
- Warning Classes: {'neurotoxicity': 3, 'musculoskeletal toxicity': 2, 'gastrointestinal toxicity': 1, 'cardiotoxicity': 1, 'misuse': 1}


### Bioactivities

- Records: 23
- Unique Drugs: 4
- Activity Types: {'Ki': 8, 'IC50': 8, 'Kd': 4, 'EC50': 3}


### Drug Metabolism (Rich Dataset)

- **Records:** 10,000
- **File Size:** 2.93 MB
- **Unique Drugs:** 152
- **Unique Metabolites:** 699
- **Unique Enzymes:** 97
- **Top Enzymes:** ['CYP3A4', 'CYP2C9', 'CYP2D6', 'Cytochrome P450s', 'CYP1A2']


## 🔗 Neo4j Import Readiness

### Required Node Types

| Node Type | Source Dataset | Status |
|-----------|---------------|--------|
| Drug | approved_drugs | ✅ Ready (Production) |
| NaturalProduct | natural_products | ⚠️ Needs Full Run |
| Target | targets | ⚠️ Needs Full Run |
| Mechanism | mechanisms | ⚠️ Needs Full Run |
| Indication | indications | ⚠️ Needs Full Run |
| Warning | warnings | ⚠️ Needs Full Run |


### Key Relationships to Create

- `Drug -[HAS_MECHANISM]-> Mechanism`
- `Mechanism -[TARGETS]-> Target`
- `Drug -[TREATS]-> Indication`
- `Drug -[HAS_WARNING]-> Warning`
- `Drug -[METABOLIZED_BY]-> Enzyme`


## 📌 Recommendations

1. **Run full collection** for secondary datasets (natural products, mechanisms, etc.)
2. **Validate CSV compatibility** with Neo4j LOAD CSV
3. **Create IMPPAT-ChemBL mapping** after natural products full run
4. **Update Cypher scripts** for new node types and relationships

