# Bridging the Gap: From Project Goals to Current Codebase

> Generated: 2026-04-02

This document maps each project goal to what the codebase can actually deliver today, identifies the specific gaps, and lays out the concrete steps to close them.

---

## How to Read This Document

Each section follows the same pattern:
1. **The Goal** - what the project should be able to do (from PROJECT-GOALS.md)
2. **What Works Today** - what the codebase actually delivers right now
3. **What's Missing** - the specific gaps preventing the goal from being met
4. **Steps to Close the Gap** - ordered, actionable work items

---

## Goal 1: Identifying Drug Repurposing Candidates

> *"Query the graph: which approved drugs target genes associated with oral mucositis?"*

### What Works Today
- 3,276 approved drugs loaded in Neo4j with molecular properties (weight, logP, PSA, HBD/HBA, SMILES, InChI)
- DisGeNET gene-disease associations for OM loaded (biomarkers, genetic variations, altered expression)
- DrugBank and TTD drug-target data loaded (small datasets)
- Basic analysis queries exist (`analysis_queries.txt`)
- An initial candidate list exists (`data/analysis/oral_mucositis_candidates.csv`)

### What's Missing
- **ChemBL mechanism data is test-only (10 records)** - Can't answer "how does this drug work?" for 99.7% of drugs
- **ChemBL target data is test-only (43 records)** - Can't link most drugs to their protein targets
- **ChemBL indication data is test-only (79 records)** - Can't filter by therapeutic relevance
- **ChemBL warning data is test-only (9 records)** - Can't assess safety for candidates
- **No ranking/scoring system** - Candidates are identified but not prioritized

### Steps to Close the Gap

| # | Step | What to Do | Depends On | Effort |
|---|------|-----------|------------|--------|
| 1.1 | Run full ChemBL mechanisms collection | `python src/scrapers/chembl/chembl_scraper.py --mechanisms-only` | None | ~2 hrs compute |
| 1.2 | Run full ChemBL targets collection | `python src/scrapers/chembl/chembl_scraper.py --targets-only` | None | ~2 hrs compute |
| 1.3 | Run full ChemBL indications collection | `python src/scrapers/chembl/chembl_scraper.py --indications-only` | None | ~2 hrs compute |
| 1.4 | Run full ChemBL warnings collection | `python src/scrapers/chembl/chembl_scraper.py --warnings-only` | None | ~1 hr compute |
| 1.5 | Run full ChemBL bioactivities collection | `python src/scrapers/chembl/chembl_scraper.py --bioactivities-only` | None | ~2 hrs compute |
| 1.6 | Run full ChemBL toxicity collection | `python src/scrapers/chembl/chembl_scraper.py --toxicity-only` | None | ~1 hr compute |
| 1.7 | Validate all new CSV files | Run `src/analysis/neo4j_csv_validator.py` on each new file | 1.1-1.6 | 15 min |
| 1.8 | Re-import into Neo4j | Run Cypher scripts 4-8 with full data (clear existing ChemBL data first) | 1.7 | 1-2 hrs |
| 1.9 | Verify import | Run `9_chembl_test_import.txt` validation queries | 1.8 | 15 min |
| 1.10 | Re-run candidate analysis | Update `oral_mucositis_candidates.csv` with full data | 1.9 | 1 hr |

**Steps 1.1-1.6 can all run in parallel** (or use `collect_all_chembl_data.sh`).

---

## Goal 2: Scientific Validation of Ayurvedic Formulations

> *"Trace the path: formulation -> plant -> phytochemical -> protein target -> OM-associated gene"*

### What Works Today
- Ayurvedic formulations with plant ingredients loaded (`ayurvedic_formulation_good_candidates_oral_mucositis.csv`, 15 formulations)
- IMPPAT plant-phytochemical mappings collected (`imppat_plant_part_phytochemicals.json`)
- PubChem phytochemical-target interactions collected (60,521 interactions, 30,425 human-only)
- DisGeNET OM gene associations loaded
- Neo4j has the node types and relationships to represent this path
- ChemBL-IMPPAT mapper prototype exists (`src/integration/chembl_imppat_mapper.py`)

### What's Missing
- **ChemBL-IMPPAT compound mapping only run on sample data** - The bridge between "this phytochemical" and "this approved drug mechanism" hasn't been built at scale
- **Mapping relies solely on exact InChI Key match** - Many valid matches are missed because the same compound may have slightly different representations across databases
- **PubChem target interaction data not cross-referenced with ChemBL targets** - Two datasets describe targets independently but aren't linked
- **MedPlant database not integrated into Neo4j** - 1,915 plant species with therapeutic uses exist in CSV but aren't in the graph
- **No end-to-end path query** - No Cypher query traces the full formulation-to-gene chain

### Steps to Close the Gap

| # | Step | What to Do | Depends On | Effort |
|---|------|-----------|------------|--------|
| 2.1 | Run full ChemBL-IMPPAT mapping | Modify `chembl_imppat_mapper.py` to use full datasets instead of `*_sample.csv`, remove the `max_requests=100` limit, execute | Goal 1 complete (1.1-1.6) | 2-4 hrs compute |
| 2.2 | Add SMILES/fingerprint similarity matching | Extend the mapper to use chemical fingerprint similarity (Tanimoto coefficient) in addition to exact InChI Key matching, using RDKit | 2.1 | 1-2 days dev |
| 2.3 | Cross-reference PubChem and ChemBL targets | Write a mapper that links PubChem protein targets to ChemBL targets via UniProt IDs and gene names (both datasets have these identifiers) | Goal 1 complete | 1 day dev |
| 2.4 | Import MedPlant data into Neo4j | Write Cypher import script for `medicinal_plants_with_uses.csv`, create Plant nodes with therapeutic use properties, link to existing Plant nodes by name | None | 0.5 day dev |
| 2.5 | Write end-to-end path query | Create Cypher queries that traverse: `(Formulation)-[:CONTAINS]->(Plant)-[:CONTAINS]->(Compound)-[:TARGETS]->(Protein)<-[:TRANSLATES]-(Gene)-[:ASSOCIATED_WITH]->(Disease {name: "Oral Mucositis"})` | 2.1-2.4 | 0.5 day dev |
| 2.6 | Generate formulation validation report | For each of the 15 Ayurvedic formulations, run the path query and document which compounds have scientifically supported paths to OM targets | 2.5 | 1 day analysis |

---

## Goal 3: Prioritizing Research Directions

> *"Rank candidates by how many OM-relevant targets they hit, their safety profiles, and their drug-likeness properties"*

### What Works Today
- Molecular properties exist for all 3,276 drugs (weight, logP, PSA, HBD/HBA - Lipinski's Rule of Five data)
- Drug warnings exist (at test scale)
- Basic candidate list exists (unranked)

### What's Missing
- **No scoring algorithm** - No code ranks candidates by any criteria
- **No pathway data** - Can't assess how many OM biological pathways a candidate affects
- **No multi-criteria ranking** - Target count, safety, bioavailability, and literature support aren't combined
- **Drug-likeness assessment not applied** - Lipinski's data exists but isn't used to filter or score

### Steps to Close the Gap

| # | Step | What to Do | Depends On | Effort |
|---|------|-----------|------------|--------|
| 3.1 | Create candidate scoring module | Build `src/analysis/candidate_scorer.py` that queries Neo4j and computes a composite score per drug/compound based on: target count for OM genes, safety warnings, Lipinski compliance, bioavailability | Goals 1 & 2 complete | 2-3 days dev |
| 3.2 | Add pathway data (KEGG) | Build `src/scrapers/kegg/` scraper to fetch pathway-gene mappings for OM-associated genes. Create `Pathway` nodes and `PARTICIPATES_IN` relationships in Neo4j | None | 2-3 days dev |
| 3.3 | Incorporate pathway coverage into scoring | Extend scorer to count how many distinct OM pathways a candidate's targets participate in | 3.1, 3.2 | 0.5 day dev |
| 3.4 | Apply drug-likeness filter | Add Lipinski Rule of Five filtering/scoring to the candidate scorer using existing molecular property data | 3.1 | 0.5 day dev |
| 3.5 | Generate ranked candidate report | Run scorer, produce ranked output with explanations (why each candidate scored high/low) | 3.1-3.4 | 1 day |

---

## Goal 4: Network Pharmacology

> *"Analyze whether a formulation's compounds work synergistically across multiple OM pathways"*

### What Works Today
- Formulations with multiple plant ingredients exist
- Plants mapped to multiple phytochemicals
- Phytochemicals mapped to multiple protein targets
- The graph structure supports multi-hop traversal

### What's Missing
- **No pathway data** - Can't determine which pathways are being hit
- **No protein-protein interaction data** - Can't model how targets interact with each other
- **No synergy analysis** - No code evaluates whether compounds in a formulation complement each other
- **No polypharmacology scoring** - No metric for "how many different mechanisms does this formulation cover?"
- **No visualization** - Complex multi-target networks are hard to interpret without visual tools

### Steps to Close the Gap

| # | Step | What to Do | Depends On | Effort |
|---|------|-----------|------------|--------|
| 4.1 | Integrate KEGG pathway data | Same as step 3.2 above | None | 2-3 days dev |
| 4.2 | Add STRING protein-protein interactions | Build `src/scrapers/string/` scraper for PPI data. Create `INTERACTS_WITH` relationships between Protein nodes with confidence scores | None | 2-3 days dev |
| 4.3 | Build network pharmacology analyzer | Create `src/analysis/network_pharmacology.py` that, given a formulation, computes: number of unique targets, number of unique pathways covered, target-target interaction density, pathway complementarity score | 4.1, 4.2, Goal 2 complete | 3-4 days dev |
| 4.4 | Compare formulations to single-drug approaches | Run the analyzer on each formulation and compare multi-target coverage vs. individual approved drugs | 4.3 | 1 day analysis |
| 4.5 | Add basic visualization | Use PyVis or NetworkX to generate interactive HTML network graphs showing formulation -> compound -> target -> pathway relationships | 4.3 | 1-2 days dev |

---

## Goal 5: The Translation (End-to-End)

> *"Turn 'this plant has been used for mouth sores' into 'this plant contains compound X, which inhibits protein Y, which is overexpressed in OM tissue'"*

This goal is the culmination of Goals 1-4. It requires all layers to be working together.

### What Works Today
- Each individual layer of data exists in some form
- Neo4j graph connects some of the pieces

### What's Missing
- **The layers aren't fully connected** - Goals 1-4 gaps prevent end-to-end traversal at scale
- **No hypothesis generation tooling** - No code that automatically generates natural-language explanations of graph paths
- **No evidence aggregation** - Individual PMIDs and scores exist but aren't combined into a coherent evidence package
- **No output format suitable for researchers** - Results are raw Cypher query outputs, not formatted reports

### Steps to Close the Gap

| # | Step | What to Do | Depends On | Effort |
|---|------|-----------|------------|--------|
| 5.1 | Complete Goals 1-4 | All steps above | - | Weeks |
| 5.2 | Build hypothesis generator | Create `src/analysis/hypothesis_generator.py` that traverses the graph and produces structured hypotheses: compound, target, evidence path, supporting literature (PMIDs), confidence score | 5.1 | 2-3 days dev |
| 5.3 | Build report formatter | Create `src/reporting/` module that takes hypotheses and generates markdown/HTML reports with: ranked candidates, evidence chains, molecular diagrams (optional), literature citations | 5.2 | 2-3 days dev |
| 5.4 | Validate with known examples | Test the system against the 4 known OM drugs (Palifermin, Hebervis, Lactermin, AG-013) - can it "rediscover" them from the graph? | 5.2 | 1 day |
| 5.5 | Generate first batch of novel hypotheses | Run the full pipeline and produce a report of the top 20 drug repurposing candidates with evidence chains | 5.3, 5.4 | 1-2 days |

---

## Infrastructure & Technical Debt

These aren't directly tied to a single goal but are needed for all of them to work reliably.

### Codebase Cleanup

| # | Step | What to Do | Effort |
|---|------|-----------|--------|
| I.1 | Migrate DisGeNET scraper | Move `scripts/python_scripts/disgenet_processing.py` to `src/scrapers/disgenet/` following the ChemBL module pattern | 0.5 day |
| I.2 | Migrate IMPPAT scraper | Move `scripts/python_scripts/imppat_processing.py` to `src/scrapers/imppat/` | 0.5 day |
| I.3 | Migrate PubChem scraper | Move `scripts/python_scripts/pubchem_processing.py` to `src/scrapers/pubchem/` | 0.5 day |
| I.4 | Migrate MedPlant scraper | Move `scripts/python_scripts/medplantdatabase_processing.py` to `src/scrapers/medplant/` | 0.5 day |
| I.5 | Remove deprecated DrugBank code | Delete or archive `scripts/python_scripts/drugbank/` (DrugBank is proprietary, code is non-functional) | 0.5 hr |
| I.6 | Remove legacy ChemBL scraper | Delete or archive `scripts/python_scripts/chembl/` (superseded by `src/scrapers/chembl/`) | 0.5 hr |

### Testing

| # | Step | What to Do | Effort |
|---|------|-----------|--------|
| I.7 | Add pytest and test infrastructure | Create `tests/` directory, add pytest to `requirements.txt`, create conftest.py | 0.5 day |
| I.8 | Write scraper unit tests | Test data parsing, CSV generation, and error handling with mocked API responses | 1-2 days |
| I.9 | Write data validation tests | Automated checks for record counts, schema consistency, required fields | 1 day |
| I.10 | Write Neo4j import tests | Verify node/relationship counts after import against expected values | 0.5 day |

### Environment & Automation

| # | Step | What to Do | Effort |
|---|------|-----------|--------|
| I.11 | Add RDKit to dependencies | Needed for SMILES/fingerprint similarity matching (step 2.2). Add to `requirements.txt` | 0.5 hr |
| I.12 | Add neo4j driver to dependencies | Needed for Python-based graph queries. Currently listed nowhere but used by `setup_neo4j.py` | 0.5 hr |
| I.13 | Create Makefile | Common operations: `make setup`, `make scrape-test`, `make scrape-full`, `make validate`, `make import`, `make analyze` | 0.5 day |
| I.14 | Docker Compose for Neo4j | Reproducible Neo4j environment with APOC pre-installed, import directory mounted | 1 day |

---

## Suggested Execution Order

Work in this order to build on each previous step:

### Phase 1: Complete the Data (1-2 weeks)
> Focus: Get the graph to full power with existing code

1. Run full ChemBL secondary collections (steps 1.1-1.6) - parallel, mostly compute time
2. Validate CSVs (1.7)
3. Re-import Neo4j (1.8-1.9)
4. Import MedPlant data (2.4)
5. Re-run candidate analysis (1.10)

### Phase 2: Build the Bridge (1-2 weeks)
> Focus: Connect Ayurvedic and Western pharmacology data

1. Run full ChemBL-IMPPAT mapping (2.1)
2. Cross-reference PubChem and ChemBL targets (2.3)
3. Write end-to-end path queries (2.5)
4. Migrate legacy scrapers (I.1-I.6)
5. Add missing dependencies (I.11-I.12)

### Phase 3: Enable Analysis (2-3 weeks)
> Focus: Turn data into ranked, actionable candidates

1. Add KEGG pathway data (3.2 / 4.1)
2. Build candidate scoring module (3.1, 3.3, 3.4)
3. Generate ranked candidate report (3.5)
4. Build hypothesis generator (5.2)
5. Validate against known OM drugs (5.4)

### Phase 4: Network Pharmacology & Reporting (2-3 weeks)
> Focus: Multi-target analysis and research output

1. Add STRING protein-protein interactions (4.2)
2. Build network pharmacology analyzer (4.3)
3. Build report formatter (5.3)
4. Generate first batch of novel hypotheses (5.5)
5. Add basic visualization (4.5)

### Phase 5: Harden (Ongoing)
> Focus: Reliability and reproducibility

1. Add test infrastructure (I.7)
2. Write tests (I.8-I.10)
3. Create Makefile (I.13)
4. Docker Compose (I.14)
5. Add SMILES/fingerprint similarity matching (2.2)

---

## Summary: What's Between Here and There

| Goal | Current Readiness | Biggest Blocker | Phase to Address |
|------|------------------|-----------------|-----------------|
| Drug repurposing candidates | ~30% | Secondary ChemBL data at test size | Phase 1 |
| Ayurvedic validation | ~40% | ChemBL-IMPPAT mapping not run at scale | Phase 2 |
| Research prioritization | ~15% | No scoring system, no pathway data | Phase 3 |
| Network pharmacology | ~10% | No pathway data, no PPI data, no synergy analysis | Phase 4 |
| End-to-end translation | ~20% | All of the above + no hypothesis generation tooling | Phase 3-4 |
