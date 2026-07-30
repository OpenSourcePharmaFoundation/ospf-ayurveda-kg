# Drug Data Scraping Master Plan

> Created: 2026-07-30

Comprehensive plan to scrape **all** relevant drug, target, pathway, and compound databases for the OSPF Ayurveda Knowledge Graph. Covers database inventory, scraper architecture, concurrency strategy, data aggregation, Neo4j import, and execution instructions.

---

## Table of Contents

1. [Database Inventory](#1-database-inventory)
2. [What We Already Have](#2-what-we-already-have)
3. [Scraper Architecture](#3-scraper-architecture)
4. [Concurrency Strategy](#4-concurrency-strategy)
5. [Dependency Graph](#5-dependency-graph)
6. [Per-Database Scraping Plans](#6-per-database-scraping-plans)
7. [Data Aggregation Pipeline](#7-data-aggregation-pipeline)
8. [Neo4j Schema Expansion](#8-neo4j-schema-expansion)
9. [Cypher Import Scripts](#9-cypher-import-scripts)
10. [Execution Instructions](#10-execution-instructions)
11. [Estimated Timeline & Resource Requirements](#11-estimated-timeline--resource-requirements)

---

## 1. Database Inventory

Every publicly accessible drug/target/pathway database relevant to Oral Mucositis drug repurposing and Ayurvedic compound validation, organized by tier.

### Tier 1: Critical (Must Scrape)

These directly answer the project's core question: *"Which drugs and natural compounds target OM-associated genes, and through what mechanisms?"*

| # | Database | Type | Access | Rate Limit | Status | Est. Records |
|---|----------|------|--------|------------|--------|-------------|
| 1 | **ChemBL** | Drugs, mechanisms, targets | REST API | ~10 req/s | **Partial** (test-only secondary data) | ~4,400 drugs, ~15K indications |
| 2 | **KEGG DRUG + Pathway** | Drug-target + biological pathways | REST API | ~10 req/s | **Not started** | ~12K drugs, ~550 pathways |
| 3 | **STRING** | Protein-protein interactions | REST API + TSV download | 1 req/s (API) | **Not started** | ~20K interactions (for our targets) |
| 4 | **UniProt** | Protein function, GO terms | REST API | ~25 req/s | **Not started** | ~2K proteins (our target set) |
| 5 | **Open Targets** | Aggregated drug-disease evidence | GraphQL API | ~10 req/s | **Not started** | ~5K associations for OM-relevant targets |
| 6 | **DrugCentral** | Open drug database (DrugBank alternative) | PostgreSQL dump | N/A (download) | **Not started** | ~4,700 active drugs |
| 7 | **DGIdb** | Drug-gene interactions (meta-aggregator) | REST API | Generous | **Not started** | ~100K interactions |

### Tier 2: High Value

| # | Database | Type | Access | Rate Limit | Status | Est. Records |
|---|----------|------|--------|------------|--------|-------------|
| 8 | **Reactome** | Detailed pathway reactions | REST API | ~10 req/s | **Not started** | ~2,700 human pathways |
| 9 | **ClinicalTrials.gov** | OM clinical trials | REST API v2 | ~3 req/s | **Not started** | ~500 OM-related trials |
| 10 | **SIDER** | Drug side effects | TSV download | N/A | **Not started** | ~140K drug-side effect pairs |
| 11 | **BindingDB** | Binding affinities | REST API + download | ~5 req/s | **Not started** | ~2.9M binding measurements |
| 12 | **PharmGKB** | Pharmacogenomics | REST API (CC-BY) | ~5 req/s | **Not started** | ~700 drug-gene pairs |
| 13 | **COCONUT** | Natural product structures | Download (MongoDB dump) | N/A | **Not started** | ~400K natural products |
| 14 | **GEO** | OM gene expression | REST API (Entrez) | 3 req/s | **Not started** | ~10-50 relevant datasets |

### Tier 3: Supplementary

| # | Database | Type | Access | Rate Limit | Status | Est. Records |
|---|----------|------|--------|------------|--------|-------------|
| 15 | **ChEBI** | Chemical ontology | REST API | ~10 req/s | **Not started** | ~60K chemical entities |
| 16 | **WikiPathways** | Community-curated pathways | REST API | Generous | **Not started** | ~800 human pathways |
| 17 | **NPACT** | Anti-cancer natural products | Download | N/A | **Not started** | ~1,500 compounds |
| 18 | **Human Protein Atlas** | Protein expression | REST API | ~10 req/s | **Not started** | Tissue-level for our targets |
| 19 | **PubMed** | Literature | REST API (Entrez) | 3 req/s (10 with API key) | **Not started** | ~5K OM-related papers |
| 20 | **Europe PMC** | Open access literature | REST API | ~10 req/s | **Not started** | Supplement PubMed |

### Tier 4: Specialized / Long-tail

| # | Database | Type | Access | Status |
|---|----------|------|--------|--------|
| 21 | **LOTUS** | Natural products online | SPARQL/Download | Not started |
| 22 | **TCMSP** | Traditional Chinese Medicine | Web scraping | Not started |
| 23 | **SuperDRUG2** | Approved/experimental drugs | Download | Not started |
| 24 | **STITCH** | Chemical-protein interactions | Download | Not started |
| 25 | **BioGRID** | Protein-protein interactions | Download | Not started |
| 26 | **IntAct** | Molecular interactions | REST API | Not started |
| 27 | **ClinVar** | Clinical variants | REST API | Not started |
| 28 | **FDA FAERS** | Adverse events | Download | Not started |
| 29 | **GTEx** | Tissue-specific expression | REST API | Not started |
| 30 | **Dr. Duke's** | Phytochemical database | Web scraping | Not started |
| 31 | **Gene Ontology** | Function ontology | Download | Not started |
| 32 | **ATC Classification** | Drug classification | Part of KEGG/WHO | Not started |

### Already Scraped (Existing)

| # | Database | Status | Records |
|---|----------|--------|---------|
| A | **ChemBL** (approved drugs) | Complete | 3,276 drugs |
| B | **DisGeNET** | Complete | OM biomarkers, genvars, altexps |
| C | **IMPPAT** | Complete | Phytochemicals + therapeutic uses |
| D | **PubChem** | Complete | 60,521 target interactions |
| E | **MedPlant (BSI)** | Complete | 1,915 plant species |
| F | **TTD** | Minimal | 4 OM drugs |
| G | **DrugBank** | Deprecated | Proprietary, non-functional |

---

## 2. What We Already Have

### Existing Data Summary

```
data/processed/
├── chembl_approved_drugs.csv          (3,276 drugs, full molecular properties)
├── chembl_bioactivities.csv           (23 records — TEST ONLY)
├── chembl_drug_indications.csv        (79 records — TEST ONLY)
├── chembl_drug_mechanisms.csv         (10 records — TEST ONLY)
├── chembl_drug_metabolism.csv         (10K records)
├── chembl_drug_targets.csv            (43 records — TEST ONLY)
├── chembl_drug_warnings.csv           (9 records — TEST ONLY)
├── chembl_natural_products.csv        (natural product flags)
├── chembl_toxicity.csv                (1 record — TEST ONLY)
├── disgenet__OM_biomarkers.csv        (complete)
├── disgenet__OM_genvars.csv           (complete)
├── disgenet__OM_altexps.csv           (complete)
├── drugbank_drug_targets.csv          (small, deprecated source)
├── imppat_plant_part_phytochemicals.json  (complete)
├── imppat_plant_therapeutic_uses.json     (complete)
├── medicinal_plants_with_uses.csv     (1,915 species)
├── phytochem_imppatid_pubchem_id_url.csv  (phytochem-to-PubChem mapping)
├── pubchem_phytochem_target_interactions.csv  (60,521 interactions)
└── ttd_drug_target_genes.csv          (4 drugs)
```

### Existing Scraper Modules

```
src/scrapers/
├── chembl/chembl_scraper.py       # Production, full-featured, resumable
├── disgenet/disgenet_scraper.py   # Excel processor (not a true scraper)
├── imppat/imppat_scraper.py       # BeautifulSoup web scraper
├── medplant/medplant_scraper.py   # BeautifulSoup web scraper
└── pubchem/pubchem_scraper.py     # Multi-stage pipeline scraper
```

### Existing Neo4j Node Types

```
Nodes: Disease, Gene, Drug, Compound, Plant, Formulation, Protein, Therapeutic_Area
Relationships: TARGETS, TRANSLATES, CONTAINS, TREATS, ASSOCIATED_WITH
```

### Identifiers Available for Cross-Referencing

These existing identifiers in our data enable cross-database lookups:

| Identifier | Where We Have It | What It Unlocks |
|------------|-----------------|-----------------|
| ChemBL ID | chembl_approved_drugs.csv | UniProt, Open Targets, BindingDB |
| PubChem CID | phytochem_imppatid_pubchem_id_url.csv | STITCH, BindingDB, PubChem BioAssay |
| Gene Name | disgenet CSVs | KEGG, STRING, DGIdb, GEO |
| UniProt Accession | (partial, from PubChem targets) | STRING, Reactome, IntAct |
| InChI Key | chembl_approved_drugs.csv | Cross-database compound matching |
| SMILES | chembl_approved_drugs.csv | Structural similarity search |
| MeSH ID | (via DisGeNET disease terms) | PubMed, ClinicalTrials.gov |

---

## 3. Scraper Architecture

### Design Principles

1. **Vertical slices**: Each database gets its own module in `src/scrapers/<dbname>/`
2. **Shared base class**: Common patterns (rate limiting, retry, progress, CSV output) in `src/scrapers/base/`
3. **Async-first**: New scrapers use `asyncio` + `aiohttp` for concurrent requests within rate limits
4. **Resumable**: All scrapers support checkpoint/resume for long-running jobs
5. **Self-contained**: Each scraper can run independently; no cross-scraper imports
6. **Standardized output**: All scrapers produce CSVs in `data/processed/` with consistent naming

### Module Structure

```
src/scrapers/
├── base/
│   ├── __init__.py
│   ├── async_scraper.py          # AsyncBaseScraper with rate limiting, retry, progress
│   ├── sync_scraper.py           # SyncBaseScraper for simple download-and-parse
│   └── utils.py                  # Shared utilities (CSV escaping, path resolution)
│
├── # ─── Existing (upgrade to use base class) ───
├── chembl/                       # Already production-quality
├── disgenet/                     # Already complete
├── imppat/                       # Already complete
├── medplant/                     # Already complete
├── pubchem/                      # Already complete
│
├── # ─── Tier 1: Critical (New) ───
├── kegg/
│   ├── __init__.py
│   ├── kegg_drug_scraper.py      # KEGG DRUG entries
│   └── kegg_pathway_scraper.py   # KEGG Pathway gene mappings
├── string/
│   ├── __init__.py
│   └── string_scraper.py         # Protein-protein interactions
├── uniprot/
│   ├── __init__.py
│   └── uniprot_scraper.py        # Protein function and GO terms
├── opentargets/
│   ├── __init__.py
│   └── opentargets_scraper.py    # Drug-disease-target evidence
├── drugcentral/
│   ├── __init__.py
│   └── drugcentral_scraper.py    # Parse PostgreSQL dump
├── dgidb/
│   ├── __init__.py
│   └── dgidb_scraper.py          # Drug-gene interactions
│
├── # ─── Tier 2: High Value (New) ───
├── reactome/
│   ├── __init__.py
│   └── reactome_scraper.py       # Pathway reactions
├── clinicaltrials/
│   ├── __init__.py
│   └── clinicaltrials_scraper.py # OM clinical trials
├── sider/
│   ├── __init__.py
│   └── sider_scraper.py          # Drug side effects (download + parse)
├── bindingdb/
│   ├── __init__.py
│   └── bindingdb_scraper.py      # Binding affinities
├── pharmgkb/
│   ├── __init__.py
│   └── pharmgkb_scraper.py       # Pharmacogenomics
├── coconut/
│   ├── __init__.py
│   └── coconut_scraper.py        # Natural products (download + parse)
├── geo/
│   ├── __init__.py
│   └── geo_scraper.py            # OM gene expression datasets
│
├── # ─── Tier 3: Supplementary (New) ───
├── chebi/
│   ├── __init__.py
│   └── chebi_scraper.py
├── wikipathways/
│   ├── __init__.py
│   └── wikipathways_scraper.py
├── npact/
│   ├── __init__.py
│   └── npact_scraper.py
├── hpa/
│   ├── __init__.py
│   └── hpa_scraper.py            # Human Protein Atlas
├── pubmed/
│   ├── __init__.py
│   └── pubmed_scraper.py         # Literature mining
│
└── orchestrator.py               # Runs multiple scrapers in parallel
```

### Base Scraper Classes

```python
# src/scrapers/base/async_scraper.py (conceptual)

class AsyncBaseScraper:
    """Base class for async scrapers with built-in rate limiting and retry."""

    def __init__(self, name, rate_limit_per_sec, max_concurrent, output_dir):
        self.name = name
        self.rate_limit = rate_limit_per_sec
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.output_dir = output_dir
        self.checkpoint_file = f"{output_dir}/.{name}_checkpoint.json"

    async def fetch(self, url, params=None):
        """Rate-limited, retrying HTTP GET."""
        # Semaphore for concurrency control
        # Token bucket for rate limiting
        # Exponential backoff on 429/5xx
        # Returns parsed JSON or raises after max retries

    def save_checkpoint(self, state):
        """Persist progress for resume capability."""

    def load_checkpoint(self):
        """Resume from last checkpoint."""

    def write_csv(self, filename, rows, headers):
        """Write standardized CSV output."""
```

---

## 4. Concurrency Strategy

### Three Levels of Parallelism

#### Level 1: Inter-Scraper Parallelism (Process-Level)

Run **independent scrapers simultaneously** as separate processes. Since each scraper hits a different API with its own rate limits, they don't interfere with each other.

```
┌─────────────────────────────────────────────────────┐
│                 Orchestrator Process                  │
│                                                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│
│  │ ChemBL   │ │ KEGG     │ │ STRING   │ │ UniProt  ││
│  │ Worker   │ │ Worker   │ │ Worker   │ │ Worker   ││
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘│
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│
│  │ Open     │ │ DGIdb    │ │ Drug     │ │ Reactome ││
│  │ Targets  │ │ Worker   │ │ Central  │ │ Worker   ││
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘│
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│
│  │ Clinical │ │ SIDER    │ │ BindingDB│ │ PharmGKB ││
│  │ Trials   │ │ Worker   │ │ Worker   │ │ Worker   ││
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘│
└─────────────────────────────────────────────────────┘
```

**Implementation**: Python `multiprocessing.Pool` or `concurrent.futures.ProcessPoolExecutor`. Each worker is a scraper's `main()` function.

#### Level 2: Intra-Scraper Concurrency (Async I/O)

Within each scraper, use `asyncio` + `aiohttp` to make multiple API requests concurrently while respecting rate limits.

```
┌──────────────── KEGG Scraper Process ──────────────────┐
│                                                         │
│  asyncio event loop                                     │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Semaphore(10)  ←── max concurrent requests     │   │
│  │  TokenBucket(10/sec) ←── rate limit             │   │
│  │                                                  │   │
│  │  Task 1: GET /pathway/hsa04010  ──→ parse ──→ ✓│   │
│  │  Task 2: GET /pathway/hsa04064  ──→ parse ──→ ✓│   │
│  │  Task 3: GET /pathway/hsa04668  ──→ waiting...  │   │
│  │  Task 4: GET /pathway/hsa04630  ──→ waiting...  │   │
│  │  ...                                             │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  Progress: ████████░░░░░░░░ 234/550 pathways           │
└─────────────────────────────────────────────────────────┘
```

#### Level 3: Batch Downloads (Bulk Data)

Some databases offer bulk downloads (SIDER, DrugCentral, COCONUT, STITCH). These are download-once, parse-locally operations — no rate limiting needed, just disk I/O.

```
SIDER:     curl download → gunzip → parse TSV → CSV
DrugCentral: wget dump → parse SQL/TSV → CSV
COCONUT:   wget dump → parse → CSV
```

### Rate Limit Configuration

| Database | Requests/sec | Max Concurrent | Strategy |
|----------|-------------|----------------|----------|
| ChemBL | 10 | 5 | Token bucket + semaphore |
| KEGG | 10 | 5 | Token bucket + semaphore |
| STRING | 1 | 1 | Sequential with delay |
| UniProt | 25 | 10 | Token bucket + semaphore |
| Open Targets | 10 | 5 | GraphQL batching + token bucket |
| DGIdb | 20 | 10 | Token bucket + semaphore |
| Reactome | 10 | 5 | Token bucket + semaphore |
| ClinicalTrials.gov | 3 | 2 | Conservative token bucket |
| BindingDB | 5 | 3 | Token bucket + semaphore |
| PharmGKB | 5 | 3 | Token bucket + semaphore |
| PubMed/Entrez | 3 (10 w/ key) | 3 | Entrez guidelines |
| GEO/Entrez | 3 (10 w/ key) | 3 | Entrez guidelines |
| SIDER | N/A | N/A | Bulk download |
| DrugCentral | N/A | N/A | Bulk download |
| COCONUT | N/A | N/A | Bulk download |

---

## 5. Dependency Graph

### What Can Run in Parallel

Almost everything — because our existing data provides seed identifiers for lookups.

```
                    ┌─── SEED DATA (already collected) ───┐
                    │                                       │
                    │  ChemBL IDs  ←── chembl_approved_drugs│
                    │  Gene Names  ←── disgenet CSVs        │
                    │  PubChem CIDs ←── pubchem mapping     │
                    │  Plant Names ←── IMPPAT/MedPlant      │
                    │                                       │
                    └───────────────┬───────────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                       │
              ▼                     ▼                       ▼
    ┌── WAVE 1 (all parallel) ──────────────────────────────────┐
    │                                                            │
    │  ChemBL secondary    (uses: ChemBL IDs)                   │
    │  KEGG Drug+Pathway   (uses: Gene Names, drug names)       │
    │  STRING              (uses: Gene/Protein Names)           │
    │  UniProt             (uses: Gene/Protein Names)           │
    │  Open Targets        (uses: Gene Names, ChemBL IDs)      │
    │  DrugCentral         (download, no deps)                  │
    │  DGIdb               (uses: Gene Names)                   │
    │  Reactome            (uses: Gene/Protein Names)           │
    │  ClinicalTrials.gov  (uses: MeSH terms for OM)           │
    │  SIDER               (download, no deps)                  │
    │  BindingDB           (uses: ChemBL IDs, PubChem CIDs)    │
    │  PharmGKB            (uses: Gene Names, drug names)       │
    │  COCONUT             (download, no deps)                  │
    │  GEO                 (uses: Gene Names, MeSH for OM)     │
    │  ChEBI               (uses: InChI Keys)                   │
    │  WikiPathways         (uses: Gene Names)                  │
    │  PubMed              (uses: MeSH terms, gene names)       │
    │                                                            │
    └────────────────────────────┬───────────────────────────────┘
                                 │
                                 ▼
    ┌── WAVE 2 (after Wave 1) ──────────────────────────────────┐
    │                                                            │
    │  Cross-Reference Aggregator                                │
    │    - Unify drug entities across ChemBL + DrugCentral       │
    │    - Map proteins: UniProt ↔ STRING ↔ PubChem targets      │
    │    - Link pathways: KEGG ↔ Reactome ↔ WikiPathways         │
    │    - Bridge compounds: ChemBL ↔ PubChem ↔ IMPPAT ↔ COCONUT│
    │    - Merge side effects: SIDER + ChemBL warnings           │
    │                                                            │
    └────────────────────────────┬───────────────────────────────┘
                                 │
                                 ▼
    ┌── WAVE 3 (after aggregation) ─────────────────────────────┐
    │                                                            │
    │  Neo4j Import                                              │
    │    - Load new node types (Pathway, ClinicalTrial, etc.)   │
    │    - Create new relationships                              │
    │    - Validate graph integrity                              │
    │                                                            │
    └────────────────────────────────────────────────────────────┘
```

### Key Insight

**Wave 1 is the bottleneck — and it's entirely parallelizable.** All 17 scrapers can run simultaneously because each hits a different API. The total wall-clock time is determined by the slowest scraper, not the sum of all scrapers.

---

## 6. Per-Database Scraping Plans

### 6.1 ChemBL — Complete Secondary Data

**Already have**: Scraper exists and works. Just needs to run in full (non-test) mode.

**What to collect**:
- Mechanisms of action (full, not test-10)
- Drug-target links (full)
- Drug indications (full)
- Drug warnings (full)
- Bioactivities (full)
- Toxicity data (full)

**Command**:
```bash
python src/scrapers/chembl/chembl_scraper.py --approved-drugs-only
```

**Expected runtime**: 4-8 hours
**Output**: Updates existing `chembl_*.csv` files in `data/processed/`

---

### 6.2 KEGG DRUG + Pathway

**API**: `https://rest.kegg.jp/`

**What to collect**:
1. **KEGG DRUG**: All drug entries with targets, pathways, and ATC codes
   - `GET /list/drug` → list of all drug IDs
   - `GET /get/D00001` → full entry for each drug (includes TARGETS, PATHWAY)
2. **KEGG Pathway**: Human biological pathways with gene membership
   - `GET /list/pathway/hsa` → list of all human pathway IDs
   - `GET /get/hsa04010` → full pathway entry (includes GENE list)
   - `GET /link/hsa/pathway:hsa04010` → gene-pathway links

**Output files**:
```
data/processed/kegg_drugs.csv                # drug_id, name, targets, formula, atc_codes
data/processed/kegg_drug_targets.csv         # drug_id, target_gene, target_name
data/processed/kegg_pathways.csv             # pathway_id, name, description, class
data/processed/kegg_pathway_genes.csv        # pathway_id, gene_id, gene_name
data/processed/kegg_drug_pathway_links.csv   # drug_id, pathway_id
```

**Concurrency**: Parse the drug/pathway list first, then fetch details with async semaphore(5).

**Expected runtime**: 2-3 hours (12K drugs + 550 pathways × ~0.5s each)

---

### 6.3 STRING

**API**: `https://string-db.org/api/`

**Strategy**: Use our OM-associated genes (from DisGeNET) + drug targets (from ChemBL) as input. Fetch protein-protein interactions for this target set.

**What to collect**:
- `POST /api/json/network` with our protein list → interaction network
- `POST /api/json/interaction_partners` → extended network (1 hop out)
- Include confidence scores (combined_score ≥ 400 = medium confidence)

**Output files**:
```
data/processed/string_ppi_network.csv        # protein_a, protein_b, combined_score, experimental, database, textmining
data/processed/string_protein_info.csv       # protein_id, preferred_name, annotation
```

**Concurrency**: Batch API supports up to 2,000 proteins per request. Our target set is likely <500 proteins, so this may be 1-3 bulk requests.

**Expected runtime**: 5-15 minutes (bulk API)

---

### 6.4 UniProt

**API**: `https://rest.uniprot.org/`

**Strategy**: Fetch detailed protein records for all targets in our graph (from PubChem interactions + ChemBL targets + DisGeNET genes).

**What to collect**:
- Protein function descriptions
- GO term annotations (Molecular Function, Biological Process, Cellular Component)
- Subcellular location
- Tissue specificity
- Disease associations
- Cross-references (PDB, Pfam, InterPro)

**Output files**:
```
data/processed/uniprot_proteins.csv          # accession, name, gene_name, function, subcellular_location
data/processed/uniprot_go_annotations.csv    # accession, go_id, go_term, aspect (F/P/C)
data/processed/uniprot_disease_assoc.csv     # accession, disease_name, disease_id
```

**Concurrency**: UniProt's new REST API supports batch queries via `POST /idmapping/run`. Submit all IDs at once, poll for results.

**Expected runtime**: 15-30 minutes

---

### 6.5 Open Targets

**API**: `https://api.platform.opentargets.org/api/v4/graphql`

**Strategy**: Query for all evidence linking our OM-associated genes to known drugs. Open Targets aggregates evidence from ChemBL, ClinicalTrials, literature, and more into a single score.

**What to collect**:
- Disease-target associations (for Oral Mucositis and related conditions)
- Drug-target evidence (all drugs targeting our gene set)
- Overall association scores
- Evidence type breakdown

**Output files**:
```
data/processed/opentargets_disease_targets.csv    # disease_id, target_id, score, datatypes
data/processed/opentargets_drug_evidence.csv      # drug_id, target_id, evidence_type, score, source
data/processed/opentargets_target_safety.csv      # target_id, safety_liability, tissue
```

**Concurrency**: GraphQL supports batching multiple queries in a single request.

**Expected runtime**: 30-60 minutes

---

### 6.6 DrugCentral

**Access**: PostgreSQL data dump from https://drugcentral.org/

**Strategy**: Download the latest data dump, extract relevant tables, convert to CSVs.

**What to collect**:
- Approved drug data (complementary to ChemBL)
- Drug-target interactions with action types
- Drug-indication mappings
- ATC classification
- FDA approval data
- Bioactivity data

**Output files**:
```
data/processed/drugcentral_drugs.csv             # drug_id, name, cas_number, smiles, inchi_key
data/processed/drugcentral_drug_targets.csv      # drug_id, target_name, target_uniprot, action_type
data/processed/drugcentral_indications.csv       # drug_id, indication, snomed_id, source
data/processed/drugcentral_atc_codes.csv         # drug_id, atc_code, atc_name
```

**Concurrency**: Single download + local parsing. No API rate limits.

**Expected runtime**: 10-20 minutes (download + parse)

---

### 6.7 DGIdb (Drug-Gene Interaction Database)

**API**: `https://dgidb.org/api/v2/`

**Strategy**: DGIdb is a meta-aggregator — it pulls drug-gene interactions from 40+ sources (including PharmGKB, DrugBank, ChemBL, TTD, etc.). This is extremely high-value because it gives us interactions we'd miss from individual databases.

**What to collect**:
- All drug-gene interactions for our OM gene set
- Interaction types (inhibitor, agonist, antagonist, etc.)
- Source databases for each interaction
- Drug attributes (approved, immunotherapy, antineoplastic, etc.)

**Output files**:
```
data/processed/dgidb_interactions.csv        # gene_name, drug_name, interaction_type, sources, pmids
data/processed/dgidb_drug_attributes.csv     # drug_name, attribute_name, attribute_value
data/processed/dgidb_gene_categories.csv     # gene_name, category (druggable genome, kinase, etc.)
```

**Concurrency**: Batch API accepts multiple genes per request.

**Expected runtime**: 10-20 minutes

---

### 6.8 Reactome

**API**: `https://reactome.org/ContentService/`

**Strategy**: Fetch detailed pathway data for all OM-associated genes. Reactome provides reaction-level detail that KEGG doesn't.

**What to collect**:
- Pathway hierarchy for human
- Gene/protein participation in pathways
- Reaction details (inputs, outputs, catalysts)
- Pathway-pathway relationships

**Output files**:
```
data/processed/reactome_pathways.csv             # pathway_id, name, species, parent_pathway
data/processed/reactome_pathway_genes.csv        # pathway_id, gene_name, uniprot_id, role
data/processed/reactome_reactions.csv            # reaction_id, pathway_id, name, type
```

**Concurrency**: Reactome has a bulk analysis endpoint (`/AnalysisService/identifiers/`) that accepts a list of genes and returns all pathways at once.

**Expected runtime**: 20-40 minutes

---

### 6.9 ClinicalTrials.gov

**API**: `https://clinicaltrials.gov/api/v2/`

**Strategy**: Search for all clinical trials related to Oral Mucositis. This reveals what treatments are being tested and their outcomes.

**What to collect**:
- All OM-related trials (search: "oral mucositis" OR "stomatitis" + cancer/radiation context)
- Trial phase, status, interventions, outcomes
- Drug names and mechanisms being tested
- Study results where available

**Output files**:
```
data/processed/clinicaltrials_om_trials.csv          # nct_id, title, phase, status, start_date
data/processed/clinicaltrials_interventions.csv      # nct_id, intervention_type, intervention_name
data/processed/clinicaltrials_outcomes.csv           # nct_id, outcome_type, measure, result
data/processed/clinicaltrials_conditions.csv         # nct_id, condition, mesh_term
```

**Concurrency**: Paginated search results. Use async for fetching individual study details.

**Expected runtime**: 15-30 minutes

---

### 6.10 SIDER

**Access**: Download TSV files from http://sideeffects.embl.de/

**Strategy**: Download pre-computed files, parse into CSV format.

**What to collect**:
- Drug-side effect pairs with frequency data
- Drug-indication pairs
- MedDRA term mappings

**Output files**:
```
data/processed/sider_drug_side_effects.csv       # drug_stitch_id, side_effect, meddra_id, frequency
data/processed/sider_drug_indications.csv        # drug_stitch_id, indication, meddra_id
data/processed/sider_id_mapping.csv              # stitch_id, drug_name, atc_code, pubchem_cid
```

**Concurrency**: N/A — single download, local parse.

**Expected runtime**: 5-10 minutes

---

### 6.11 BindingDB

**API**: `https://bindingdb.org/axis2/services/BDBService/`

**Strategy**: For our target proteins, fetch binding affinity data. This tells us HOW STRONGLY a compound binds to its target — critical for ranking candidates.

**What to collect**:
- Ki, Kd, IC50, EC50 values for compound-target pairs
- Only for our target set (OM-associated proteins)
- Compound identifiers (ChemBL, PubChem, InChI)

**Output files**:
```
data/processed/bindingdb_affinities.csv      # target_uniprot, compound_name, ki, kd, ic50, ec50, pubchem_cid, chembl_id
```

**Concurrency**: Async with rate limiting. ~5 req/s.

**Expected runtime**: 1-3 hours (depends on target set size)

---

### 6.12 PharmGKB

**API**: `https://api.pharmgkb.org/v1/data/`

**Strategy**: Fetch pharmacogenomic relationships for our drug and gene sets.

**What to collect**:
- Drug-gene relationships with evidence levels
- Clinical annotations
- Dosing guidelines (if relevant to OM drugs)

**Output files**:
```
data/processed/pharmgkb_relationships.csv    # drug_name, gene_name, relationship_type, evidence_level, pmids
data/processed/pharmgkb_clinical_ann.csv     # drug_name, gene_name, phenotype, significance
```

**Concurrency**: Moderate rate limits. Async with semaphore(3).

**Expected runtime**: 20-40 minutes

---

### 6.13 COCONUT (Natural Products)

**Access**: Download from https://coconut.naturalproducts.net/

**Strategy**: Download the full natural products database, filter for compounds with known biological activity relevant to our targets.

**What to collect**:
- Natural product structures (SMILES, InChI)
- Taxonomic source (plant species)
- Known biological activities
- Cross-references to PubChem, ChemBL

**Output files**:
```
data/processed/coconut_natural_products.csv      # coconut_id, name, smiles, inchi_key, molecular_formula
data/processed/coconut_taxonomy.csv              # coconut_id, organism, family, genus, species
data/processed/coconut_activities.csv            # coconut_id, activity_type, target, value
```

**Concurrency**: N/A — download + parse.

**Expected runtime**: 30-60 minutes (large dataset parsing)

---

### 6.14 GEO (Gene Expression Omnibus)

**API**: Entrez E-utilities (`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`)

**Strategy**: Search for OM-related gene expression datasets, download processed expression matrices, identify differentially expressed genes.

**What to collect**:
- Datasets studying OM gene expression (search: "oral mucositis" + expression profiling)
- Sample metadata (OM vs. control, treatment conditions)
- Pre-computed differential expression if available (GEO2R results)

**Output files**:
```
data/processed/geo_om_datasets.csv               # geo_id, title, organism, sample_count, platform
data/processed/geo_om_diff_expression.csv        # geo_id, gene_name, log2fc, pvalue, adj_pvalue
```

**Concurrency**: Entrez has strict rate limits (3/sec without API key, 10/sec with key). Register for an API key.

**Expected runtime**: 30-60 minutes

---

### 6.15-6.20 Tier 3 Databases (Brief Plans)

**ChEBI**: REST API, fetch classification and ontology terms for our compounds. ~30 min.

**WikiPathways**: REST API, fetch community-curated pathways for our gene set. Supplements KEGG/Reactome. ~15 min.

**NPACT**: Download TSV of anti-cancer natural products. Filter for OM-relevant targets. ~5 min.

**Human Protein Atlas**: REST API, fetch tissue expression data for our target proteins. Shows where targets are expressed. ~20 min.

**PubMed**: Entrez E-utilities, search for OM + drug repurposing literature. Extract PMIDs, titles, abstracts for evidence tagging. ~30-60 min.

**Europe PMC**: REST API, supplements PubMed with full-text mining where available. ~30 min.

---

## 7. Data Aggregation Pipeline

After Wave 1 (all scrapers complete), run the aggregation pipeline to cross-reference and unify entities.

### 7.1 Entity Resolution

The same drug/protein/gene appears across databases with different identifiers. The aggregator resolves these.

```
src/aggregation/
├── __init__.py
├── entity_resolver.py           # Cross-database entity matching
├── drug_aggregator.py           # Unify drug records
├── target_aggregator.py         # Unify protein/gene targets
├── pathway_aggregator.py        # Merge KEGG + Reactome + WikiPathways
├── compound_aggregator.py       # Bridge natural products across IMPPAT/COCONUT/PubChem
├── evidence_aggregator.py       # Combine evidence from all sources
└── neo4j_csv_generator.py       # Generate final Neo4j-ready CSVs
```

### 7.2 Cross-Reference Keys

| Entity | Primary Key | Cross-Reference Keys |
|--------|------------|---------------------|
| Drug | ChemBL ID | DrugCentral ID, KEGG ID, PubChem CID, InChI Key, drug name |
| Protein | UniProt Accession | Gene Name, STRING ID, ChemBL Target ID, Ensembl ID |
| Gene | Gene Symbol (HGNC) | Entrez ID, Ensembl ID, UniProt Accession |
| Compound | PubChem CID | IMPPAT ID, InChI Key, SMILES, ChemBL ID, COCONUT ID |
| Pathway | KEGG ID | Reactome ID, WikiPathways ID, GO terms |
| Disease | MeSH ID | EFO ID, OMIM ID, SNOMED ID, ICD code |

### 7.3 Aggregated Output Files

```
data/aggregated/
├── master_drugs.csv                 # Unified drug table with all cross-references
├── master_targets.csv               # Unified protein/gene target table
├── master_compounds.csv             # Unified compound table (drugs + natural products)
├── master_pathways.csv              # Unified pathway table
├── master_drug_target_interactions.csv   # All drug-target interactions with sources
├── master_compound_target_interactions.csv  # All compound-target interactions
├── master_target_pathway_memberships.csv   # Gene/protein → pathway mappings
├── master_ppi_network.csv           # Protein-protein interaction network
├── master_drug_indications.csv      # All drug-indication pairs with sources
├── master_side_effects.csv          # All drug-side effect pairs
├── master_clinical_trials.csv       # OM clinical trial data
├── master_expression_data.csv       # OM gene expression data
└── master_evidence_scores.csv       # Aggregated evidence for each drug-target-disease triple
```

### 7.4 Deduplication Rules

1. **Drugs**: Match by InChI Key first, then by ChemBL ID, then by exact name match
2. **Proteins**: Match by UniProt Accession first, then by gene symbol
3. **Compounds**: Match by InChI Key first, then by PubChem CID, then by SMILES canonical form
4. **Pathways**: Match by database-specific ID; cross-link via shared gene membership (Jaccard similarity > 0.5)

---

## 8. Neo4j Schema Expansion

### New Node Types

```
(:Pathway {id, name, source, description, class})
(:ClinicalTrial {nct_id, title, phase, status, start_date, completion_date})
(:SideEffect {meddra_id, name, meddra_level})
(:Publication {pmid, title, journal, year, doi})
(:GOTerm {go_id, name, aspect})
(:BiologicalProcess {id, name, description})
```

### New Relationship Types

```
(Gene)-[:PARTICIPATES_IN]->(Pathway)
(Protein)-[:PARTICIPATES_IN]->(Pathway)
(Drug)-[:TESTED_IN {role, dose}]->(ClinicalTrial)
(Drug)-[:HAS_SIDE_EFFECT {frequency, source}]->(SideEffect)
(Protein)-[:INTERACTS_WITH {score, experimental, database}]->(Protein)
(Drug)-[:CITED_IN]->(Publication)
(Compound)-[:CITED_IN]->(Publication)
(Protein)-[:HAS_FUNCTION]->(GOTerm)
(Protein)-[:INVOLVED_IN]->(BiologicalProcess)
(Drug)-[:CLASSIFIED_AS {atc_code}]->(Therapeutic_Area)
(Compound)-[:STRUCTURALLY_SIMILAR {tanimoto}]->(Compound)
(Drug)-[:HAS_BINDING_AFFINITY {ki, kd, ic50}]->(Protein)
```

### Updated Schema Diagram

```
                                    ┌──────────────┐
                                    │  Publication │
                                    └──────┬───────┘
                                           │ CITED_IN
                                           │
┌──────────┐    CONTAINS    ┌──────────┐   │    ┌──────────────┐
│Formulation├──────────────►│  Plant   │   │    │   Pathway    │
└──────────┘                └────┬─────┘   │    └──────┬───────┘
                                 │ CONTAINS │          │ PARTICIPATES_IN
                                 ▼          │          │
┌──────────┐    TARGETS     ┌──────────┐   │    ┌─────▼────────┐     ASSOCIATED_WITH    ┌──────────┐
│  Drug    ├───────────────►│ Protein  │◄──┘    │    Gene      ├───────────────────────►│ Disease  │
└──┬───┬───┘                └──┬──┬────┘        └──────────────┘                        └──────────┘
   │   │                       │  │
   │   │ HAS_SIDE_EFFECT       │  │ INTERACTS_WITH (PPI)
   │   ▼                       │  ▼
   │ ┌──────────┐              │ ┌──────────┐
   │ │SideEffect│              │ │ Protein  │ (other proteins in network)
   │ └──────────┘              │ └──────────┘
   │                           │
   │ TESTED_IN                 │ HAS_FUNCTION
   ▼                           ▼
┌──────────────┐          ┌──────────┐
│ClinicalTrial │          │  GOTerm  │
└──────────────┘          └──────────┘
```

---

## 9. Cypher Import Scripts

### New Script Numbering

Extending the existing numbered sequence:

```
scripts/cypher_scripts/
├── 1_uniqueness_constraints.txt              # (existing)
├── 2_formulation_plant_compound_target.txt   # (existing)
├── 3_disease_drug_target.txt                 # (existing)
├── 4-8_chembl_*.txt                          # (existing)
│
├── # ─── New scripts ───
├── 11_new_constraints.txt                    # Constraints for new node types
├── 12_kegg_pathways.txt                      # Pathway nodes + gene-pathway links
├── 13_string_ppi.txt                         # Protein-protein interaction edges
├── 14_uniprot_proteins.txt                   # Enrich existing Protein nodes
├── 15_opentargets_evidence.txt               # Evidence scores as relationship properties
├── 16_drugcentral_drugs.txt                  # Merge with existing Drug nodes + new data
├── 17_dgidb_interactions.txt                 # Drug-gene interactions (new edges)
├── 18_reactome_pathways.txt                  # Additional pathway data
├── 19_clinicaltrials.txt                     # ClinicalTrial nodes + TESTED_IN edges
├── 20_sider_side_effects.txt                 # SideEffect nodes + HAS_SIDE_EFFECT edges
├── 21_bindingdb_affinities.txt               # HAS_BINDING_AFFINITY edges
├── 22_pharmgkb.txt                           # Pharmacogenomic annotations
├── 23_coconut_natural_products.txt           # Enrich Compound nodes with COCONUT data
├── 24_geo_expression.txt                     # Gene expression properties
├── 25_literature_pubmed.txt                  # Publication nodes + CITED_IN edges
└── 30_cross_database_links.txt               # Cross-reference edges between databases
```

### Example: 11_new_constraints.txt

```cypher
// Constraints for new node types

CREATE CONSTRAINT pathway_unique IF NOT EXISTS
FOR (p:Pathway) REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT clinical_trial_unique IF NOT EXISTS
FOR (ct:ClinicalTrial) REQUIRE ct.nct_id IS UNIQUE;

CREATE CONSTRAINT side_effect_unique IF NOT EXISTS
FOR (se:SideEffect) REQUIRE se.meddra_id IS UNIQUE;

CREATE CONSTRAINT publication_unique IF NOT EXISTS
FOR (pub:Publication) REQUIRE pub.pmid IS UNIQUE;

CREATE CONSTRAINT go_term_unique IF NOT EXISTS
FOR (go:GOTerm) REQUIRE go.go_id IS UNIQUE;

// Indexes for performance
CREATE INDEX pathway_name_index IF NOT EXISTS
FOR (p:Pathway) ON (p.name);

CREATE INDEX drug_kegg_id_index IF NOT EXISTS
FOR (d:Drug) ON (d.kegg_id);

CREATE INDEX drug_drugcentral_id_index IF NOT EXISTS
FOR (d:Drug) ON (d.drugcentral_id);

CREATE INDEX protein_uniprot_id_index IF NOT EXISTS
FOR (p:Protein) ON (p.uniprot_id);
```

### Example: 12_kegg_pathways.txt

```cypher
// Load KEGG pathways
LOAD CSV WITH HEADERS FROM 'file:///kegg_pathways.csv' AS row
MERGE (p:Pathway {id: row.pathway_id})
SET p.name = row.name,
    p.description = row.description,
    p.class = row.class,
    p.source = 'KEGG';

// Link genes to pathways
LOAD CSV WITH HEADERS FROM 'file:///kegg_pathway_genes.csv' AS row
MATCH (g:Gene {name: row.gene_name})
MATCH (p:Pathway {id: row.pathway_id})
MERGE (g)-[:PARTICIPATES_IN {source: 'KEGG'}]->(p);

// Link drugs to pathways via KEGG drug-pathway mappings
LOAD CSV WITH HEADERS FROM 'file:///kegg_drug_pathway_links.csv' AS row
MATCH (d:Drug) WHERE d.kegg_id = row.drug_id OR toLower(d.name) = toLower(row.drug_name)
MATCH (p:Pathway {id: row.pathway_id})
MERGE (d)-[:ACTS_IN_PATHWAY {source: 'KEGG'}]->(p);
```

### Example: 13_string_ppi.txt

```cypher
// Load protein-protein interactions from STRING
LOAD CSV WITH HEADERS FROM 'file:///string_ppi_network.csv' AS row
WITH row WHERE toInteger(row.combined_score) >= 400
MATCH (p1:Protein {name: row.protein_a})
MATCH (p2:Protein {name: row.protein_b})
MERGE (p1)-[r:INTERACTS_WITH]->(p2)
SET r.combined_score = toInteger(row.combined_score),
    r.experimental = toFloat(row.experimental),
    r.database = toFloat(row.database_score),
    r.textmining = toFloat(row.textmining),
    r.source = 'STRING';
```

---

## 10. Execution Instructions

### Prerequisites

```bash
# 1. Activate virtual environment
cd /path/to/ospf-ayurveda-kg
source venv/bin/activate

# 2. Install new dependencies
pip install -r requirements.txt
# New additions needed: aiohttp, aiofiles, tqdm

# 3. Set API keys (optional but recommended)
export NCBI_API_KEY="your_ncbi_api_key"  # For PubMed/GEO (10x rate limit boost)
# Most other APIs are keyless
```

### Step 1: Complete Existing Scraping

```bash
# Run full ChemBL secondary data collection (can take 4-8 hours)
python src/scrapers/chembl/chembl_scraper.py --approved-drugs-only
```

### Step 2: Run All New Scrapers (Wave 1 — Parallel)

Use the orchestrator to run all scrapers simultaneously:

```bash
# Run all Tier 1+2 scrapers in parallel
python src/scrapers/orchestrator.py --tiers 1,2

# Or run individual scrapers manually (each in its own terminal):
python src/scrapers/kegg/kegg_drug_scraper.py &
python src/scrapers/kegg/kegg_pathway_scraper.py &
python src/scrapers/string/string_scraper.py &
python src/scrapers/uniprot/uniprot_scraper.py &
python src/scrapers/opentargets/opentargets_scraper.py &
python src/scrapers/drugcentral/drugcentral_scraper.py &
python src/scrapers/dgidb/dgidb_scraper.py &
python src/scrapers/reactome/reactome_scraper.py &
python src/scrapers/clinicaltrials/clinicaltrials_scraper.py &
python src/scrapers/sider/sider_scraper.py &
python src/scrapers/bindingdb/bindingdb_scraper.py &
python src/scrapers/pharmgkb/pharmgkb_scraper.py &
python src/scrapers/coconut/coconut_scraper.py &
python src/scrapers/geo/geo_scraper.py &

# Monitor progress
python src/scrapers/orchestrator.py --status
```

### Step 3: Aggregate Data (Wave 2)

```bash
# Run cross-database aggregation
python src/aggregation/entity_resolver.py
python src/aggregation/drug_aggregator.py
python src/aggregation/target_aggregator.py
python src/aggregation/pathway_aggregator.py
python src/aggregation/compound_aggregator.py
python src/aggregation/neo4j_csv_generator.py

# Or run all at once:
python src/aggregation/run_all.py
```

### Step 4: Import to Neo4j (Wave 3)

```bash
# 1. Copy all CSVs to Neo4j import directory
cp data/processed/*.csv /path/to/neo4j/import/
cp data/aggregated/*.csv /path/to/neo4j/import/

# 2. Run Cypher scripts in order (in Neo4j Browser or via cypher-shell)
# Existing scripts first (if re-importing):
#   1-10 (existing)

# Then new scripts:
#   11_new_constraints.txt
#   12_kegg_pathways.txt
#   13_string_ppi.txt
#   14_uniprot_proteins.txt
#   15_opentargets_evidence.txt
#   16_drugcentral_drugs.txt
#   17_dgidb_interactions.txt
#   18_reactome_pathways.txt
#   19_clinicaltrials.txt
#   20_sider_side_effects.txt
#   21_bindingdb_affinities.txt
#   22_pharmgkb.txt
#   23_coconut_natural_products.txt
#   24_geo_expression.txt
#   25_literature_pubmed.txt
#   30_cross_database_links.txt

# 3. Validate import
# Run the validation queries from analysis_queries.txt
```

### Step 5: Validate

```bash
# Run data validation
python src/aggregation/validate.py

# Run analysis queries to verify the graph is complete
# (in Neo4j Browser)
MATCH (n) RETURN labels(n), count(n) ORDER BY count(n) DESC;
MATCH ()-[r]->() RETURN type(r), count(r) ORDER BY count(r) DESC;
```

---

## 11. Estimated Timeline & Resource Requirements

### Time Estimates (Wall-Clock)

| Phase | What | Time | Notes |
|-------|------|------|-------|
| **Scraper Development** | Write base classes + all new scrapers | 3-5 days | ~20 scraper modules |
| **Wave 1 Scraping** | Run all scrapers in parallel | 4-8 hours | Bottleneck = ChemBL or BindingDB |
| **Wave 2 Aggregation** | Cross-reference + entity resolution | 1-2 hours | Mostly local compute |
| **Cypher Script Writing** | Write 15 new import scripts | 1-2 days | Template from existing scripts |
| **Wave 3 Import** | Load everything into Neo4j | 2-4 hours | Depends on graph size |
| **Validation** | Verify completeness + correctness | 2-4 hours | Manual + automated checks |

**Total: ~1-2 weeks development + 1 day execution**

### Disk Space

| Data Source | Estimated Size |
|-------------|---------------|
| Existing data | ~25 MB |
| ChemBL (full secondary) | ~50-100 MB |
| KEGG | ~20 MB |
| STRING | ~10 MB |
| UniProt | ~30 MB |
| Open Targets | ~50 MB |
| DrugCentral | ~100 MB (dump) |
| DGIdb | ~20 MB |
| Reactome | ~30 MB |
| ClinicalTrials.gov | ~10 MB |
| SIDER | ~50 MB |
| BindingDB | ~200 MB (filtered) |
| COCONUT | ~500 MB (full dump) |
| Others | ~100 MB |
| **Total** | **~1-1.5 GB** |

### Network Requirements

- Stable internet connection for 4-8 hours
- No VPN required (all databases are publicly accessible)
- NCBI API key recommended (free registration, 10x rate limit boost)

### Neo4j Resource Requirements

After full import, the graph will contain approximately:

| Metric | Estimated Count |
|--------|----------------|
| Total Nodes | ~50,000-80,000 |
| Total Relationships | ~500,000-1,000,000 |
| Node Types | ~15 |
| Relationship Types | ~20 |
| Neo4j Disk Usage | ~2-4 GB |
| Recommended RAM | 4-8 GB allocated to Neo4j |

---

## Appendix A: New Dependencies

Add to `requirements.txt`:

```
# Existing
beautifulsoup4==4.12.3
bs4==0.0.2
pandas==2.2.3
requests==2.32.3

# New - async HTTP
aiohttp>=3.9.0
aiofiles>=23.2.0

# New - progress display
tqdm>=4.66.0

# New - data processing
openpyxl>=3.1.0        # Excel file support (already implicit dep)

# Optional - chemical similarity
# rdkit-pypi>=2024.3.1  # Uncomment if using structural similarity matching
```

## Appendix B: API Registration Requirements

| Database | Registration Required? | Cost | Notes |
|----------|----------------------|------|-------|
| ChemBL | No | Free | |
| KEGG | No | Free (academic) | Commercial use requires license |
| STRING | No | Free | |
| UniProt | No | Free | |
| Open Targets | No | Free | |
| DrugCentral | No | Free | CC-BY-SA 4.0 |
| DGIdb | No | Free | |
| Reactome | No | Free | CC0 |
| ClinicalTrials.gov | No | Free | |
| SIDER | No | Free | CC-BY-NC-SA |
| BindingDB | No | Free | |
| PharmGKB | Yes (free) | Free | CC-BY-SA, requires account for API |
| COCONUT | No | Free | CC0 |
| NCBI (PubMed/GEO) | Recommended | Free | API key boosts rate limit 3→10/sec |

## Appendix C: Licensing Summary

All databases in this plan are freely available for academic/non-commercial use. Key license requirements:

- **CC-BY**: Attribution required (ChEBI, Open Targets, PharmGKB)
- **CC-BY-SA**: Attribution + share-alike (DrugCentral)
- **CC-BY-NC**: Non-commercial only (SIDER)
- **CC0**: No restrictions (Reactome, COCONUT, WikiPathways)
- **Custom academic**: Free for academic use, commercial requires license (KEGG, STRING)

Since OSPF is a non-commercial open-source project, all listed databases are usable.
