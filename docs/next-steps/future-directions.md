# OSPF Ayurveda Knowledge Graph - Future Directions

> Generated: 2026-04-02 | Based on comprehensive codebase & data review

---

## Table of Contents

1. [Project State Summary](#1-project-state-summary)
2. [Critical Gaps](#2-critical-gaps)
3. [Future Direction: Complete the Foundation](#3-future-direction-complete-the-foundation)
4. [Future Direction: Expand the Graph](#4-future-direction-expand-the-graph)
5. [Future Direction: Analysis & Machine Learning](#5-future-direction-analysis--machine-learning)
6. [Future Direction: LLM & Intelligent Query](#6-future-direction-llm--intelligent-query)
7. [Future Direction: Visualization & Presentation](#7-future-direction-visualization--presentation)
8. [Future Direction: Automation & DevOps](#8-future-direction-automation--devops)
9. [Proposed Skills & Agents](#9-proposed-skills--agents)

---

## 1. Project State Summary

### What Exists

| Layer | Status | Details |
|-------|--------|---------|
| **ChemBL Approved Drugs** | Production | 3,276 drugs with full molecular properties, structures, approval data |
| **ChemBL Secondary Datasets** | Test only | Mechanisms (10), Indications (79), Targets (43), Bioactivities (23), Warnings (9), Toxicity (1) - all at sample size |
| **DisGeNET OM Genes** | Complete | 3 association types (biomarkers, genetic variations, altered expression) |
| **IMPPAT Plants/Phytochemicals** | Complete | Plant-part-phytochemical mappings + therapeutic uses for Ayurvedic formulations |
| **PubChem Target Interactions** | Complete | 60,521 phytochemical-target interactions (30,425 human-only) |
| **Medicinal Plants DB** | Partial | 1,915 species but many with "UNKNOWN USE"; only 14 deeply scraped |
| **DrugBank** | Deprecated | Proprietary - limited scraping done, not reliable going forward |
| **TTD (OM-specific drugs)** | Minimal | Only 4 approved drugs for OM (Palifermin, Hebervis, Lactermin, AG-013) |
| **Neo4j Graph** | Operational | Schema defined, import pipeline working, analysis queries available |
| **ChemBL-IMPPAT Mapping** | Prototype | InChI Key-based mapping exists but only run on sample data |
| **Candidate Analysis** | Early | oral_mucositis_candidates.csv exists with initial drug candidates |
| **Code Architecture** | Mixed | Production code in `/src`, legacy scripts in `/scripts` (technical debt) |

### What's Planned (from docs/todos)

- Classic ML analysis (KNN, SVM, Random Forest, MLP)
- Local LLM with Graph-aware RAG (detailed 8-week plan in docs/notes)
- Drug candidate narrowing based on OM-relevant effects
- MedPlant data integration
- Script migration from `/scripts` to `/src`
- Setup automation and usage guide

---

## 2. Critical Gaps

These are the most impactful problems limiting the project's potential.

### Gap 1: Secondary ChemBL Data is Test-Only
**Impact: HIGH** - The graph has 3,276 drugs but only 10 mechanism records, 79 indications, 43 targets. Without full mechanism/indication/target data, the graph can't answer "which drugs target proteins involved in OM?" at scale.

**Fix**: Run full ChemBL collection for all secondary datasets (~4-8 hours total).

### Gap 2: No Pathway Data
**Impact: HIGH** - The graph connects drugs to targets and genes to diseases, but has no biological pathway information. OM involves specific inflammatory cascades (NF-kB, TNF-alpha, IL-1/IL-6 signaling). Without pathways, you can't trace *how* a compound might affect OM biology.

**Fix**: Integrate KEGG or Reactome pathway data to connect genes/proteins to biological processes.

### Gap 3: Phytochemical-to-Drug Bridge is Weak
**Impact: HIGH** - The ChemBL-IMPPAT mapper exists but was only run on sample data. The full mapping that connects Ayurvedic plant compounds to known drug mechanisms hasn't been executed.

**Fix**: Run `chembl_imppat_mapper.py` on full datasets, expand to use SMILES/fingerprint similarity in addition to exact InChI Key matching.

### Gap 4: Only 4 Known OM Drugs
**Impact: MEDIUM** - The TTD data only lists 4 drugs approved for OM. This is actually the *point* of the project (finding more candidates), but it means the "ground truth" for validation is very small.

**Fix**: Supplement with clinical trial data from ClinicalTrials.gov for OM treatments (including off-label use and experimental compounds).

### Gap 5: No Automated Testing or Validation
**Impact: MEDIUM** - No test suite. Data quality depends on manual inspection. No way to detect regressions in scrapers or data processing.

**Fix**: Add pytest-based tests for scrapers, data validators, and Neo4j import verification.

---

## 3. Future Direction: Complete the Foundation

Priority actions to make the existing pipeline fully operational.

### 3.1 Run Full ChemBL Secondary Collections
Run the production scraper for all datasets beyond the initial 10-record test:
- Mechanisms of action (~2,500 records expected)
- Drug indications (~15,000+ records)
- Drug targets (~5,000+ records)
- Bioactivities (large dataset, may need time limits)
- Drug warnings (~1,000+ records)
- Drug metabolism (already has 10K records)
- Toxicity data

**Effort**: 8-12 hours of collection time (automated), 1-2 hours of setup/monitoring.

### 3.2 Run Full ChemBL-IMPPAT Compound Mapping
Execute `chembl_imppat_mapper.py` against the full approved drugs + natural products datasets instead of sample data. This creates the crucial bridge between Ayurvedic compounds and modern pharmacology.

**Effort**: 2-4 hours (PubChem API rate limited).

### 3.3 Migrate Legacy Scrapers to /src
Move these from `scripts/python_scripts/` to `src/scrapers/`:
- `disgenet_processing.py` -> `src/scrapers/disgenet/`
- `imppat_processing.py` -> `src/scrapers/imppat/`
- `pubchem_processing.py` -> `src/scrapers/pubchem/`
- `medplantdatabase_processing.py` -> `src/scrapers/medplant/`

Follow the pattern established by `src/scrapers/chembl/`. This consolidates the codebase and reduces technical debt.

**Effort**: 1-2 days of refactoring.

### 3.4 Re-import Neo4j with Full Data
Once secondary ChemBL datasets are complete, re-run the full Neo4j import pipeline with all data. Verify with `9_chembl_test_import.txt` validation queries.

**Effort**: 1-2 hours.

---

## 4. Future Direction: Expand the Graph

New data sources and relationships that would significantly enhance the knowledge graph.

### 4.1 Biological Pathway Integration (KEGG / Reactome)
**Why**: OM is driven by specific biological pathways (NF-kB activation, pro-inflammatory cytokine cascades, epithelial barrier disruption). Pathway data connects individual gene targets to the broader biological mechanisms.

**What to add**:
- KEGG pathway API: Gene-to-pathway mappings
- Reactome: Reaction-level detail for pathway steps
- New nodes: `Pathway`, `BiologicalProcess`
- New relationships: `PARTICIPATES_IN`, `PART_OF_PATHWAY`

**Impact**: Enables queries like "which Ayurvedic compounds affect the NF-kB pathway?"

### 4.2 Clinical Trial Data (ClinicalTrials.gov)
**Why**: Only 4 approved OM drugs exist, but many more are in clinical trials. This data shows what's being tested, what has failed, and what's promising.

**What to add**:
- ClinicalTrials.gov API scraper for OM-related trials
- New nodes: `ClinicalTrial`
- New relationships: `TESTED_IN`, `HAS_OUTCOME`
- Trial phase, status, interventions, outcomes

**Impact**: Expands the "ground truth" beyond 4 drugs and identifies experimental approaches.

### 4.3 Adverse Event / Side Effect Data (SIDER / FAERS)
**Why**: Drug repurposing needs safety context. Some drugs that target OM genes might have unacceptable side effects, or conversely, drugs with "side effects" beneficial for OM (e.g., increased mucus production) could be candidates.

**What to add**:
- SIDER database: Known side effects for approved drugs
- FDA FAERS: Real-world adverse event reports
- New relationships: `HAS_SIDE_EFFECT`, `REPORTED_ADVERSE_EVENT`

**Impact**: Filters drug candidates by safety profile and finds serendipitous candidates.

### 4.4 Protein-Protein Interaction Networks (STRING)
**Why**: Drug targets don't work in isolation. STRING provides protein interaction networks showing which proteins physically or functionally interact. This reveals indirect effects of targeting a specific protein.

**What to add**:
- STRING API: Protein-protein interaction scores
- New relationships: `INTERACTS_WITH` (with confidence scores)

**Impact**: Enables network pharmacology - understanding how targeting one protein cascades through the interaction network.

### 4.5 Gene Expression Data for OM (GEO / ArrayExpress)
**Why**: Know which genes are actually up/down-regulated in OM tissue vs. healthy tissue. This prioritizes targets that are genuinely active in the disease.

**What to add**:
- Curated gene expression datasets for oral mucositis
- Differential expression results (fold change, p-value)
- New node properties or relationships for expression context

**Impact**: Prioritizes targets that are actually dysregulated in OM.

### 4.6 Literature Mining (PubMed)
**Why**: Published research contains relationships not yet in structured databases. PubMed abstracts can reveal compound-disease associations, mechanism insights, and clinical observations.

**What to add**:
- PubMed API scraper for OM + Ayurveda + drug repurposing literature
- NLP-extracted relationships (co-occurrence, semantic parsing)
- New node: `Publication`; new relationships: `MENTIONED_IN`, `SUPPORTS`

**Impact**: Captures knowledge that's "in the literature" but not in any database.

---

## 5. Future Direction: Analysis & Machine Learning

### 5.1 Classic ML for Drug-Target Prediction (Already Planned)
As noted in `todo.md`, the team wants to explore:
- **K-Nearest Neighbours**: Find drugs similar to known OM treatments
- **SVM**: Classify compounds as potential OM treatments
- **Random Forest**: Feature importance for what makes a good OM drug candidate
- **Multilayer Perceptron**: Non-linear pattern recognition in drug properties

**Feature engineering from graph**: Molecular properties (weight, logP, PSA, HBD/HBA), target counts, pathway involvement, similarity to known OM drugs.

### 5.2 Graph Embeddings (Node2Vec / GraphSAGE)
**Why**: Convert the knowledge graph into vector representations that capture structural relationships. Nodes that are "close" in the graph get similar embeddings.

**Applications**:
- Drug similarity based on graph topology (not just chemical structure)
- Link prediction: predict missing drug-target or compound-disease edges
- Cluster analysis: find groups of related compounds/drugs

**Tools**: PyTorch Geometric, DGL, or Neo4j Graph Data Science library.

### 5.3 Network Pharmacology Analysis
**Why**: Ayurvedic formulations contain multiple plants with multiple compounds hitting multiple targets. This "multi-target" approach is the basis of network pharmacology.

**Analyses**:
- Target overlap between Ayurvedic compounds and approved drugs
- Pathway coverage analysis (how many OM pathways does a formulation hit?)
- Synergy prediction between compounds in the same formulation
- Polypharmacology scoring

### 5.4 Drug Repurposing Score
**Why**: Combine multiple signals into a single prioritization score for each drug candidate.

**Components**:
- Target relevance to OM (from DisGeNET gene scores)
- Pathway involvement in OM biology
- Chemical similarity to known effective compounds
- Safety profile (warnings, toxicity)
- Bioavailability and drug-likeness (Lipinski's rules)
- Literature evidence strength

**Output**: Ranked list of drug repurposing candidates with explainable scores.

---

## 6. Future Direction: LLM & Intelligent Query

### 6.1 Graph-Aware RAG System (Already Planned)
The `local-llm-implementation-plan.md` outlines an 8-week plan for:
- Ollama-based local LLM (Llama 3.1 or Mistral)
- Natural language to Cypher translation
- Context-aware response generation from graph results
- Entity extraction and intent classification

This is the most detailed existing plan and should be a primary focus.

### 6.2 Hypothesis Generation Agent
**Why**: Beyond answering questions, an LLM could actively generate hypotheses by traversing the graph.

**Capability**:
- "Given compound X targets protein Y, and protein Y is involved in pathway Z which is dysregulated in OM, compound X may have therapeutic potential for OM through pathway Z modulation."
- Automatically generate and rank hypotheses
- Cross-reference with literature for supporting evidence

### 6.3 Research Assistant Interface
**Why**: Make the knowledge graph accessible to researchers who don't know Cypher.

**Features**:
- Natural language queries ("What plants contain compounds that target TNF-alpha?")
- Conversational exploration ("Tell me more about Glycyrrhiza glabra's compounds")
- Export results to publications/presentations
- Citation tracking (which PMIDs support each finding)

---

## 7. Future Direction: Visualization & Presentation

### 7.1 Interactive Graph Visualization (Web UI)
**Why**: A visual interface makes the knowledge graph explorable by non-technical researchers and useful for presentations/publications.

**Options**:
- **Neovis.js**: Direct Neo4j visualization in the browser
- **D3.js force-directed graph**: Custom interactive visualization
- **Streamlit + PyVis**: Quick Python-based dashboard
- **Neo4j Bloom**: Commercial but powerful graph exploration

**Features**:
- Click-to-explore node expansion
- Filter by node type, relationship type, data source
- Highlight paths between compounds and diseases
- Export subgraphs for publications

### 7.2 Drug Candidate Dashboard
**Why**: Present analysis results in an accessible format for the research team.

**Features**:
- Ranked candidate list with scores
- Molecular property distributions
- Target network visualization for each candidate
- Comparison view (Ayurvedic vs. synthetic candidates)
- Pathway coverage heatmap

### 7.3 Publication-Ready Figures
**Why**: Generate figures suitable for academic papers and presentations.

**Outputs**:
- Knowledge graph schema diagram
- Data source integration overview
- Top candidate compound profiles
- Network pharmacology visualizations

---

## 8. Future Direction: Automation & DevOps

### 8.1 Automated Data Refresh Pipeline
**Why**: Databases like ChemBL, DisGeNET, and PubChem update regularly. An automated pipeline keeps the graph current.

**Components**:
- Scheduled scraper runs (weekly/monthly)
- Incremental updates (only fetch new/changed records)
- Data diff reports (what changed since last run)
- Automated Neo4j re-import

### 8.2 Data Quality Monitoring
**Why**: Scrapers can silently fail, APIs can change, data can degrade.

**Components**:
- Record count validation (expected vs. actual)
- Schema consistency checks
- Completeness tracking over time
- Alert on anomalies (sudden drops in record counts)

### 8.3 Test Suite
**Why**: No automated tests currently exist. Critical for reliability.

**Components**:
- Unit tests for data processing functions
- Integration tests for API scrapers (with mocked responses)
- Neo4j import validation tests
- Data quality assertion tests
- CI pipeline (GitHub Actions)

### 8.4 Reproducible Environment
**Why**: Setup is currently manual and platform-dependent.

**Components**:
- Docker Compose for Neo4j + Python environment
- Makefile or task runner for common operations
- Environment variable management
- One-command setup (`make setup && make import`)

---

## 9. Proposed Skills & Agents

The following are Claude Code skills and agents that could accelerate development on this project. **These are proposals for review - select which ones to implement.**

### Skills (User-Invocable Commands)

| # | Skill Name | Purpose | What It Does |
|---|-----------|---------|-------------|
| S1 | `/scrape` | Run data collection | Orchestrates scraper execution for any supported database (ChemBL, IMPPAT, PubChem, etc.) with mode selection (test/full), progress tracking, and result validation |
| S2 | `/validate-data` | Check data integrity | Runs Neo4j CSV validator on all processed files, checks record counts, reports completeness, flags issues |
| S3 | `/neo4j-import` | Import data to graph | Executes Cypher import scripts in correct order against a running Neo4j instance, with pre-import validation and post-import verification |
| S4 | `/analyze-candidates` | Drug candidate analysis | Runs analytical Cypher queries to identify and rank drug repurposing candidates, generates a report |
| S5 | `/data-stats` | Dataset statistics | Generates statistics across all datasets (record counts, completeness, relationships, coverage gaps) |
| S6 | `/migrate-script` | Migrate legacy code | Scaffolds migration of a legacy script from `/scripts` to `/src` following the established module pattern |
| S7 | `/add-datasource` | Add new data source | Scaffolds a new scraper module in `/src/scrapers/` with boilerplate (rate limiting, CSV output, error handling, documentation) |
| S8 | `/graph-query` | Natural language graph query | Translates a natural language question into a Cypher query, runs it against Neo4j, and formats results |
| S9 | `/pipeline` | Run end-to-end pipeline | Executes the full data pipeline: scrape -> validate -> import -> analyze, with checkpoints and rollback |
| S10 | `/explore-compound` | Deep-dive on a compound | Given a compound name or ID, retrieves all known information across all datasets (targets, pathways, plants, formulations, literature) |

### Agents (Autonomous Background Workers)

| # | Agent Name | Purpose | What It Does |
|---|-----------|---------|-------------|
| A1 | **Data Collection Agent** | Automated scraping | Orchestrates multi-source data collection with rate limiting, retry logic, progress tracking, and error recovery. Handles the 8-12 hour full collection runs autonomously. |
| A2 | **Graph Builder Agent** | Neo4j management | Manages schema evolution, handles data imports, validates graph integrity, generates import reports. Prevents duplicate nodes/relationships. |
| A3 | **Drug Discovery Agent** | Candidate identification | Traverses the knowledge graph to identify drug repurposing candidates using multi-criteria scoring (target relevance, safety, bioavailability, pathway coverage). Generates ranked candidate reports. |
| A4 | **Literature Mining Agent** | PubMed research | Searches PubMed for publications relevant to identified candidates, extracts key findings, and annotates graph nodes with literature evidence. |
| A5 | **Data Quality Agent** | Continuous validation | Monitors data files for completeness, consistency, and correctness. Runs on schedule or before imports. Reports anomalies and suggests fixes. |
| A6 | **ML Experiment Agent** | Machine learning | Prepares feature matrices from graph data, runs ML experiments (KNN, SVM, RF, MLP), tracks results, and reports findings with feature importance analysis. |
| A7 | **Compound Profiler Agent** | Deep compound analysis | Given a compound, pulls together all available information across databases, generates a comprehensive profile, and identifies research gaps. |
| A8 | **Graph Explorer Agent** | Interactive research | Answers natural language questions about the knowledge graph by generating and executing Cypher queries, with conversational follow-up capability. |
| A9 | **Scaffold Agent** | Code generation | Creates new scraper modules, data processors, or analysis scripts following established project patterns and architecture conventions. |
| A10 | **Report Generator Agent** | Research reporting | Compiles analysis results, candidate lists, and graph statistics into formatted reports suitable for team meetings, advisor updates, or publication drafts. |

### Recommended Implementation Priority

**Phase 1 - Foundation** (implement first):
- S1 `/scrape` - Immediately useful for completing secondary ChemBL data
- S2 `/validate-data` - Needed before any import
- S5 `/data-stats` - Quick wins for understanding current state
- A5 Data Quality Agent - Catches issues early

**Phase 2 - Analysis** (implement after data is complete):
- S4 `/analyze-candidates` - Core research value
- S10 `/explore-compound` - Research workflow support
- A3 Drug Discovery Agent - The main analytical capability
- A6 ML Experiment Agent - Supports the planned ML work

**Phase 3 - Intelligence** (implement for advanced features):
- S8 `/graph-query` - Natural language interface
- A8 Graph Explorer Agent - Conversational research
- A4 Literature Mining Agent - Evidence enrichment
- A10 Report Generator Agent - Research output

**Phase 4 - Automation** (implement for long-term sustainability):
- S9 `/pipeline` - End-to-end automation
- A1 Data Collection Agent - Automated refresh
- A2 Graph Builder Agent - Schema management
- S7 `/add-datasource` - Extensibility

---

## Appendix: Data Source Expansion Candidates

Potential new databases to integrate, ranked by relevance to the project's goals:

| Database | Type | Relevance | API Available | Notes |
|----------|------|-----------|---------------|-------|
| **KEGG** | Pathways | Critical | REST API | Biological pathway data connecting genes to processes |
| **Reactome** | Pathways | Critical | REST API | Detailed reaction-level pathway data |
| **ClinicalTrials.gov** | Clinical | High | REST API | OM clinical trials, experimental treatments |
| **STRING** | PPI Networks | High | REST API | Protein-protein interactions with confidence scores |
| **SIDER** | Side Effects | High | Download | Known side effects for approved drugs |
| **UniProt** | Proteins | Medium | REST API | Detailed protein data, GO annotations |
| **GEO** | Expression | Medium | REST API | Gene expression datasets for OM tissue |
| **Open Targets** | Drug-Disease | Medium | GraphQL | Aggregated evidence for drug-disease associations |
| **ChEBI** | Chemistry | Medium | REST API | Chemical ontology, compound classification |
| **HMDB** | Metabolomics | Low-Medium | REST API | Human metabolome, endogenous compounds |
