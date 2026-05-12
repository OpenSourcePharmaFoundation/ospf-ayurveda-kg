# Drug & Biomedical Database Catalog

Comprehensive catalog of databases for expanding the OSPF Ayurveda Knowledge Graph for Oral Mucositis drug repurposing. Each entry includes access method, data format, authentication requirements, and relevance to the project.

**Last updated:** 2026-05-11

---

## Table of Contents

- [Current Data Sources](#current-data-sources)
- [Drug & Target Databases](#drug--target-databases)
- [Pathway Databases](#pathway-databases)
- [Natural Product & Traditional Medicine Databases](#natural-product--traditional-medicine-databases)
- [Adverse Event & Safety Databases](#adverse-event--safety-databases)
- [Protein Interaction Databases](#protein-interaction-databases)
- [Gene Expression & Genomics Databases](#gene-expression--genomics-databases)
- [Metabolite & Pharmacogenomics Databases](#metabolite--pharmacogenomics-databases)
- [Chemical Structure Databases](#chemical-structure-databases)
- [Integration Priority Recommendations](#integration-priority-recommendations)

---

## Current Data Sources

These sources already have scrapers in `src/scrapers/` or manually compiled data in `data/processed/`.

| Source | Scraper Location | Status | Records |
|--------|-----------------|--------|---------|
| ChemBL | `src/scrapers/chembl/` | Approved drugs complete (3,274). Secondary datasets (mechanisms, targets, indications, warnings, bioactivities) at test size only. | ~3,274 drugs + test-size secondary |
| PubChem | `src/scrapers/pubchem/` | Complete | 60,521 interactions |
| DisGeNET | `src/scrapers/disgenet/` | Complete | Biomarkers, genetic variations, altered expression for OM |
| IMPPAT | `src/scrapers/imppat/` | Complete | Plant phytochemicals + therapeutic uses (JSON) |
| MedPlant (BSI) | `src/scrapers/medplant/` | Complete but not in Neo4j | 1,915 plant species |
| TTD | Manual (`data/processed/ttd_drug_target_genes.csv`) | Minimal | 4 known OM drugs |

**Immediate gap:** ChemBL secondary datasets need full collection runs (~8-12 hours) to unlock drug-to-target-to-gene linkages at scale.

---

## Drug & Target Databases

### DrugBank

- **URL:** https://go.drugbank.com/
- **API Docs:** https://docs.drugbank.com/v1/
- **Contains:** Drug-target interactions, drug indications, metabolism, pharmacokinetics, adverse events, drug-drug interactions, clinical data
- **Access Method:** REST API (3,000 requests/month dev key, unlimited production) + bulk XML download
- **Authentication:** API key required (academic keys available)
- **Formats:** JSON (API), XML (bulk), CSV (select datasets)
- **License:** Free for academic non-commercial use; commercial license required for redistribution
- **OM Relevance:** High — approved drugs with mechanisms, off-label uses, adverse event profiles. Drug Repurposing Data Package available.
- **Integration Approach:** REST API scraper with API key management. Rate limit: 3,000 req/month on dev tier. Bulk XML download likely more practical for full dataset.
- **Note:** We already have a small manual file at `data/processed/drugbank_drug_targets.csv` (2.9 KB). A full scraper would dramatically expand this.

### DGIdb (Drug Gene Interaction Database)

- **URL:** https://dgidb.org/
- **API Docs:** https://dgidb.org/api
- **Contains:** Drug-gene interactions aggregated from 40+ sources, gene categories, interaction claims
- **Access Method:** GraphQL API + TSV bulk downloads
- **Authentication:** None
- **Formats:** JSON (GraphQL), TSV (downloads)
- **License:** Free
- **OM Relevance:** High — identifies druggable genes in OM pathways. Aggregates data from many sources we'd otherwise scrape individually.
- **Integration Approach:** GraphQL queries for targeted OM gene lookups, or bulk TSV download for complete dataset. GraphQL is newer (replaced REST in DGIdb 5.0).

### DrugCentral

- **URL:** https://drugcentral.org/
- **Contains:** Drug-target interactions, pharmacological action, indications, adverse events, FDA label data
- **Access Method:** Web application + relational database download (PostgreSQL dump)
- **Authentication:** None
- **Formats:** SQL dump, web interface
- **License:** Free
- **OM Relevance:** High — bridges drug-target interactions with pharmacological action and FDA label text.
- **Integration Approach:** Download PostgreSQL dump, extract relevant tables to CSV. Alternatively scrape web interface for targeted queries.

### BindingDB

- **URL:** https://www.bindingdb.org/
- **Contains:** 3.2M binding affinity measurements, 1.4M compounds, 11.4K targets. IC50, Ki, Kd, EC50 values.
- **Access Method:** TSV bulk downloads + web search + KNIME workflows
- **Authentication:** None
- **Formats:** TSV
- **License:** Free (academic and commercial)
- **OM Relevance:** Medium-High — quantitative binding data for drug-target pairs. Useful for ranking candidates by binding strength.
- **Integration Approach:** Bulk TSV download, filter to OM-relevant targets. Large dataset (3.2M measurements) so filtering is essential.

### STITCH (Search Tool for Interacting Chemicals)

- **URL:** http://stitch.embl.de/
- **Contains:** Chemical-protein interactions from metabolic pathways, crystal structures, binding experiments, drug-target relationships. 430K+ chemicals, 9.6M+ proteins.
- **Access Method:** REST API + full database download
- **Authentication:** None
- **Formats:** TSV (downloads), JSON (API)
- **License:** Free (CC BY 4.0)
- **OM Relevance:** Medium — chemical-protein interaction prediction, mechanism of action discovery. Overlaps significantly with STRING for the protein side.
- **Integration Approach:** REST API for targeted compound lookups, or bulk download filtered to human proteins. Note: STITCH is closely related to STRING and shares infrastructure.

### ClinicalTrials.gov

- **URL:** https://clinicaltrials.gov/
- **API Docs:** https://clinicaltrials.gov/data-api/api (v2.0, OpenAPI 3.0)
- **Contains:** Clinical trial metadata — study status, conditions, interventions, outcomes, sponsors, eligibility, results
- **Access Method:** REST API v2.0 (classic API retired June 2024)
- **Authentication:** None
- **Formats:** JSON
- **License:** Public domain
- **OM Relevance:** High — find all trials testing drugs for oral mucositis, identify which drugs have been tried, what endpoints were used, and outcomes. Critical for understanding what's already been tested.
- **Integration Approach:** REST API queries filtering by condition="Oral Mucositis" and condition="Stomatitis". Pagination required for bulk retrieval. Python wrapper `pytrials` available.
- **Note:** `docs/next-steps/future-directions.md` already identifies this as a priority gap (only 4 known OM drugs in TTD).

### DDinter (Drug-Drug Interaction Database)

- **URL:** https://ddinter.scbdd.com/
- **Contains:** 236,834 DDI associations across 1,833 approved drugs
- **Access Method:** Web interface + downloads
- **Authentication:** None
- **Formats:** Web/downloads
- **License:** Free
- **OM Relevance:** Medium — assessing drug interaction risks when repurposing drugs for cancer patients already on chemotherapy regimens.
- **Integration Approach:** Bulk download, filter to drugs in our candidate list.

### HIT 2.0 (Herbal Ingredients' Targets)

- **URL:** http://hit2.badd-cao.net/
- **Contains:** 1,237 herbal ingredients, 2,208 targets, 10,031 compound-target pairs with quality indicators
- **Access Method:** Web interface + search
- **Authentication:** None
- **Formats:** Web interface
- **License:** Free
- **OM Relevance:** High — maps traditional herbal ingredients to molecular targets with quality scores. Cross-links to TTD, DrugBank, KEGG, UniProt.
- **Integration Approach:** Web scraping with BeautifulSoup (no API). Rate-limited requests to extract compound-target pairs.

---

## Pathway Databases

### KEGG (Kyoto Encyclopedia of Genes and Genomes)

- **URL:** https://www.kegg.jp/
- **KEGG DRUG:** https://www.genome.jp/kegg/drug/
- **API Docs:** https://www.kegg.jp/kegg/rest/keggapi.html
- **Contains:** Metabolic pathways, disease pathways, drug information, molecular interaction networks, therapeutic targets. 8,000+ approved drugs in KEGG DRUG.
- **Access Method:** REST API (academic use) + R package (KEGGREST) + Python (kegg_pull)
- **Authentication:** Academic institutional access
- **Formats:** KGML (pathway XML), JSON, plain text
- **License:** Free for academic use only
- **OM Relevance:** Critical — comprehensive pathway data for understanding OM mechanisms (NF-kB, TNF, apoptosis, wound healing pathways). Already identified as a priority gap in `docs/next-steps/bridging-the-gap.md` and `docs/next-steps/future-directions.md`.
- **Integration Approach:** REST API to fetch pathway-gene mappings for OM-relevant pathways. Start with known OM pathways (NF-kB signaling, TNF signaling, apoptosis, p53 signaling). Map our gene list to KEGG pathways.

### Reactome

- **URL:** https://reactome.org/
- **API Docs:** https://reactome.org/dev/content-service
- **Contains:** 2,500+ manually curated biological pathways, reactions, molecular events, protein interactions
- **Access Method:** REST API + Neo4j graph database download + MySQL dump + web interface + R package
- **Authentication:** None
- **Formats:** BioPAX, OWL, JSON, flat files, MySQL, Neo4j
- **License:** Creative Commons (free)
- **OM Relevance:** Critical — detailed molecular pathways for inflammation, epithelial damage, wound healing. Native Neo4j format is a huge advantage for our graph.
- **Integration Approach:** Download Reactome's Neo4j database and merge relevant pathway subgraphs into our knowledge graph. REST API for targeted pathway lookups. The Neo4j native format makes this the most natural pathway database for our stack.

### WikiPathways

- **URL:** https://www.wikipathways.org/
- **Contains:** 1,000+ community-curated biological pathways for drug targets, metabolic processes, signaling cascades
- **Access Method:** REST API (27M requests served) + R package (rWikiPathways) + Python (pywikipathways) + SPARQL endpoint + Cytoscape plugin
- **Authentication:** None
- **Formats:** GPML, GMT, JSON, RDF
- **License:** CC0 (public domain)
- **OM Relevance:** Medium — community-curated pathways complement Reactome's expert curation. Good for less-studied pathways.
- **Integration Approach:** REST API or Python package to fetch pathway-gene mappings. GMT format is compact and easy to parse.

### PathBank

- **URL:** https://pathbank.org/
- **Contains:** 600,000+ machine-readable pathways including metabolic, signaling, and disease pathways
- **Access Method:** Web interface + downloads
- **Authentication:** None
- **Formats:** Downloads available
- **License:** Free for academic use
- **OM Relevance:** Medium — large pathway collection, but less curated than Reactome.
- **Integration Approach:** Bulk download, filter to human pathways relevant to OM.

### Pathway Commons

- **URL:** https://www.pathwaycommons.org/
- **Contains:** Aggregated pathway data from freely available sources (Reactome, KEGG, WikiPathways, and others)
- **Access Method:** Web interface + downloads + Cytoscape plugin
- **Authentication:** None
- **Formats:** BioPAX, SIF
- **License:** Free
- **OM Relevance:** Medium — useful as an aggregator if we want pathway data from multiple sources in one download.
- **Integration Approach:** SIF (Simple Interaction Format) downloads are easy to parse. Could serve as a single-source alternative to integrating Reactome + WikiPathways separately.

---

## Natural Product & Traditional Medicine Databases

### Dr. Duke's Phytochemical and Ethnobotanical Databases

- **URL:** https://phytochem.nal.usda.gov/
- **Bulk Data:** https://data.nal.usda.gov/dataset/dr-dukes-phytochemical-and-ethnobotanical-databases (Duke-Source-CSV.zip)
- **Contains:** Phytochemicals, plant species, ethnobotanical uses, biological activities. 7,000+ plant species, 40,000+ phytochemical compounds.
- **Access Method:** Web search interface + CSV bulk download (no API)
- **Authentication:** None
- **Formats:** CSV
- **License:** CC0 (public domain)
- **OM Relevance:** High — traditional plant compounds and their documented uses. Complements IMPPAT with Western/global ethnobotanical data. Biological activity data can bridge to modern pharmacology.
- **Integration Approach:** Download Duke-Source-CSV.zip, parse CSV files, cross-reference compounds with our IMPPAT phytochemical list and PubChem IDs. Map biological activities to OM-relevant mechanisms.

### COCONUT (COlleCtion of Open Natural prodUcTs)

- **URL:** https://coconut.naturalproducts.net/
- **Contains:** Large collection of natural products with structures, properties, and source organisms
- **Access Method:** Web interface + downloads
- **Authentication:** None
- **Formats:** Various download formats
- **License:** Free
- **OM Relevance:** Medium — broad natural product coverage for identifying novel leads.
- **Integration Approach:** Bulk download, filter by structural similarity to known OM-active compounds using SMILES/InChI matching.

### NPAtlas (Natural Products Atlas)

- **URL:** https://www.npatlas.org/
- **Downloads:** https://www.npatlas.org/download
- **Contains:** 24,594 microbial natural products with structures, source organisms, total syntheses
- **Access Method:** Web search (substructure, name, features) + downloadable data
- **Authentication:** None
- **Formats:** SDF, SMILES, CSV
- **License:** CC BY-NC 4.0
- **OM Relevance:** Medium — microbial natural products as potential leads. Less directly relevant than plant-derived compounds but could surface novel scaffolds.
- **Integration Approach:** Download CSV, cross-reference with OM target list via PubChem/ChemBL identifiers.

### TCMBank

- **URL:** https://tcmbank.cn/
- **Contains:** Comprehensive Traditional Chinese Medicine database — herbs, ingredients, targets, diseases
- **Access Method:** Web interface + downloads
- **Authentication:** None
- **Formats:** Downloadable datasets
- **License:** Free (non-commercial)
- **OM Relevance:** Medium-High — TCM has extensive oral health formulations. TCM and Ayurveda share many medicinal plants, so cross-referencing could validate hypotheses.
- **Integration Approach:** Bulk download, map TCM ingredients to our phytochemical list via PubChem CID or InChI key matching.

### TCMSID (TCM Simplified Integrated Database)

- **URL:** https://tcm.scbdd.com/
- **Contains:** 499 herbs, 20,015 ingredients, 3,270 targets
- **Access Method:** Web interface + downloads
- **Authentication:** None
- **Formats:** Standardized database format
- **License:** Free
- **OM Relevance:** Medium — smaller but more structured than TCMBank. Ingredient-target mappings are directly useful.
- **Integration Approach:** Download ingredient-target mapping tables, merge with our target gene list.

### TCM Database@Taiwan

- **URL:** http://tcm.cmu.edu.tw/
- **Contains:** 20,000+ pure compounds from 453 TCM ingredients with 2D and 3D structures
- **Access Method:** Web interface + structure downloads
- **Authentication:** None
- **Formats:** 2D/3D structure files
- **License:** Free (non-commercial)
- **OM Relevance:** Medium — structural data for virtual screening of TCM compounds against OM targets.
- **Integration Approach:** Download structures, perform virtual screening or structural similarity analysis against known OM drugs.

### GRAYU (Graph-based Ayurvedic Resource)

- **URL:** https://www.graphayurveda.com/ (if available)
- **Contains:** 12,000+ medicinal plants, 130,000+ phytochemicals, 1,000+ Ayurvedic formulations, 13,000+ diseases
- **Access Method:** Web-based with visualization tools
- **Authentication:** Unknown
- **Formats:** Web interface with some downloadable data
- **License:** Freely available
- **OM Relevance:** Very High — directly maps Ayurvedic formulations to phytochemicals, targets, and diseases using a systems pharmacology framework. Most directly aligned with our project goals.
- **Integration Approach:** Investigate data export options. Web scraping may be needed. Cross-reference formulations with our `data/raw/ayurvedic_formulation_good_candidates_oral_mucositis.csv`.

---

## Adverse Event & Safety Databases

### OpenFDA Drug Adverse Events

- **URL:** https://open.fda.gov/
- **Adverse Events API:** https://open.fda.gov/apis/drug/event/
- **Contains:** FDA Adverse Event Reporting System (FAERS) data — adverse reactions, medication errors, product quality issues
- **Access Method:** REST API + bulk downloads + web dashboard
- **Authentication:** None
- **Formats:** JSON
- **License:** Public domain
- **OM Relevance:** High — real-world adverse event data. Search for drugs that cause oral mucositis (negative signal) or drugs used alongside chemotherapy with no OM signal (positive signal for protective effect).
- **Integration Approach:** REST API queries filtering by `patient.reaction.reactionmeddrapt` = "Stomatitis" or "Oral mucositis". Max 1,000 records per call, pagination required. ~3-month data lag.
- **Note:** FAERS data has limitations — reports are voluntary, no causal proof, duplicate reports possible. Use for hypothesis generation, not definitive conclusions.

### SIDER (Side Effect Resource)

- **URL:** http://sideeffects.embl.de/
- **Contains:** 1,430 drugs, 5,880 adverse drug reactions, 140,064 drug-ADR pairs extracted from package inserts
- **Access Method:** Web interface + downloadable flat files (SIDER 4.1)
- **Authentication:** None
- **Formats:** TSV
- **License:** Free
- **OM Relevance:** High — structured side effect profiles. Can identify drugs known to cause stomatitis/OM (contraindicated for our use case) vs. drugs with anti-inflammatory side effect profiles (potentially beneficial).
- **Integration Approach:** Download TSV files, parse drug-ADR pairs, flag drugs associated with "Stomatitis" or "Mouth ulceration" MedDRA terms. Cross-reference with our approved drugs list.

---

## Protein Interaction Databases

### STRING (Search Tool for Retrieval of Interacting Genes/Proteins)

- **URL:** https://string-db.org/
- **API Docs:** https://string-db.org/help/api/
- **Contains:** 14.9M protein-protein interaction predictions — known interactions (experimental, databases) and predicted interactions (gene neighborhood, co-expression, text mining)
- **Access Method:** REST API (free, anonymous or registered) + Cytoscape plugin + R/Bioconductor + bulk downloads
- **Authentication:** None required (registered key enables monitoring)
- **Formats:** JSON, TSV (API), tab-delimited (downloads)
- **License:** CC BY 4.0
- **OM Relevance:** Critical — protein interaction networks around OM targets. Identifies hub proteins, network vulnerabilities, and multi-target drug opportunities. Already identified as priority in `docs/next-steps/bridging-the-gap.md` (Goal 4: Network Pharmacology).
- **Integration Approach:** REST API to fetch interaction networks for our DisGeNET OM gene list. Bulk download of human PPI network for comprehensive coverage. Import as INTERACTS_WITH relationships in Neo4j.

### BioGRID

- **URL:** https://thebiogrid.org/
- **Downloads:** https://downloads.thebiogrid.org/
- **Contains:** Curated protein-protein, chemical-protein, and genetic interactions with evidence codes
- **Access Method:** REST API + tab-delimited downloads + PSI-MI XML
- **Authentication:** None
- **Formats:** TSV, PSI-MI XML, MITAB
- **License:** MIT License (fully free)
- **OM Relevance:** Medium — experimentally validated interactions (higher confidence than predicted). Complements STRING's broader but noisier predictions.
- **Integration Approach:** Bulk download human interactions, filter to OM gene list. MITAB format is standardized and easy to parse.

### UniProt

- **URL:** https://www.uniprot.org/
- **API Docs:** https://www.uniprot.org/api-documentation
- **Contains:** Protein sequences, functions, post-translational modifications, interactions, disease associations, subcellular localization
- **Access Method:** REST API (free, no auth) + web search + ID Mapping tool
- **Authentication:** None
- **Formats:** JSON, XML, FASTA, TSV
- **License:** CC BY 4.0
- **OM Relevance:** Medium — target protein characterization. Enriches our Drug/Gene nodes with protein function, family, and localization data.
- **Integration Approach:** REST API for batch lookups of UniProt accessions already in our ChemBL target data. TSV format for bulk retrieval.

---

## Gene Expression & Genomics Databases

### GEO (Gene Expression Omnibus)

- **URL:** https://www.ncbi.nlm.nih.gov/geo/
- **Contains:** Gene expression microarray data, RNA-seq, DNA methylation profiles from community submissions
- **Access Method:** Entrez E-Utils API + GEOquery (R) + GEOparse (Python) + web tools
- **Authentication:** None (API key recommended for higher rate limits)
- **Formats:** SOFT, MINiML, CSV, FASTQ
- **License:** Public domain
- **OM Relevance:** Medium-High — search for oral mucositis gene expression studies to identify differentially expressed genes, validate our DisGeNET gene list, and discover new OM-associated genes.
- **Integration Approach:** Search GEO for "oral mucositis" datasets, download expression matrices, identify DEGs. Use GEOparse Python library. Cross-reference DEGs with our DisGeNET gene list.

### OMIM (Online Mendelian Inheritance in Man)

- **URL:** https://www.omim.org/
- **Contains:** 7,000+ genetic disorders, 15,000+ genes, gene-disease associations, phenotype descriptions
- **Access Method:** Web interface + programmatic access via NCBI
- **Authentication:** None
- **Formats:** Text, available through Harmonizome
- **License:** Free for academic use
- **OM Relevance:** Low-Medium — OM is not primarily a genetic disorder, but genetic susceptibility factors could be relevant.
- **Integration Approach:** NCBI E-Utils queries for OM-associated genes. Low priority compared to other sources.

### GeneCards

- **URL:** https://www.genecards.org/
- **Contains:** Comprehensive gene information from 150+ sources — disease associations, drug interactions, expression, pathways
- **Access Method:** Web interface + API access
- **Authentication:** Registration for bulk access
- **Formats:** Web, TSV exports
- **License:** Free version available (limited bulk access)
- **OM Relevance:** Medium — aggregates gene data from many sources. Useful for enriching gene nodes but may duplicate data from sources we already integrate.
- **Integration Approach:** Web API for targeted gene lookups to enrich our DisGeNET gene nodes with additional annotations.

### Harmonizome

- **URL:** https://maayanlab.cloud/Harmonizome/
- **Downloads:** https://maayanlab.cloud/Harmonizome/download
- **Contains:** 138 datasets from 79 resources — 83M+ gene-attribute associations across disease/phenotype, genomics, physical interactions, proteomics, annotations, transcriptomics
- **Access Method:** Web interface + API + Python downloader (harmonizomedownloader.py)
- **Authentication:** None
- **Formats:** JSON (API), TSV (downloads)
- **License:** Free
- **OM Relevance:** Medium — meta-resource aggregating many databases. Could be a shortcut for pulling gene annotations from multiple sources in one download.
- **Integration Approach:** Use Python downloader to fetch specific datasets. Filter to OM gene list. Useful as a "one-stop shop" for gene annotations rather than integrating 79 sources individually.

### miRTarBase

- **URL:** https://mirtarbase.cuhk.edu.cn/
- **Contains:** 3.8M+ experimentally validated microRNA-target interactions from 13,690+ articles
- **Access Method:** Web interface + downloads
- **Authentication:** None
- **Formats:** Downloadable datasets
- **License:** Free
- **OM Relevance:** Low-Medium — miRNA regulation of OM-associated genes. Advanced use case for understanding post-transcriptional regulation.
- **Integration Approach:** Download interaction tables, filter to our OM gene list. Lower priority — pursue after core databases are integrated.

---

## Metabolite & Pharmacogenomics Databases

### HMDB (Human Metabolome Database)

- **URL:** https://www.hmdb.ca/
- **Contains:** 220,945 metabolite entries, 8,610 linked protein sequences, 130 data fields per metabolite. Related to DrugBank, T3DB (toxins), SMPDB (pathways), FooDB (food).
- **Access Method:** Web search + downloads + extensive search tools (text, structure, MS, NMR)
- **Authentication:** None
- **Formats:** XML, CSV, SDF
- **License:** Free
- **OM Relevance:** Medium — metabolic pathways and biomarkers. Drug metabolism data complements our ChemBL metabolism dataset.
- **Integration Approach:** Bulk XML download, filter to metabolites associated with OM-relevant drugs and pathways.

### PharmGKB (Pharmacogenomics Knowledge Base)

- **URL:** https://www.pharmgkb.org/
- **Contains:** Drug-gene interactions, pharmacogenomic relationships, clinical annotations, dosing guidelines, drug labels
- **Access Method:** API (registration required) + web interface + data downloads
- **Authentication:** Free registration required
- **Formats:** XML, JSON, TSV
- **License:** Free for research use
- **OM Relevance:** Medium — pharmacogenomic factors affecting drug response. Relevant for understanding why some patients develop OM from chemotherapy and others don't.
- **Integration Approach:** Register for API access, query for drugs in our candidate list. Download clinical annotations for OM-relevant drugs.

---

## Chemical Structure Databases

### ZINC

- **URL:** https://zinc.docking.org/
- **Contains:** 230M+ purchasable compounds, 120M+ drug-like compounds, organized by property categories
- **Access Method:** Downloads by category (drug-like, lead-like, clean) + API (XML/JSON) + command line (curl/wget)
- **Authentication:** None
- **Formats:** SMILES, mol2, 3D SDF, DOCK flexibase
- **License:** Free
- **OM Relevance:** Low — primarily for virtual screening campaigns. Not directly useful for knowledge graph but relevant if we move to computational docking.
- **Integration Approach:** Not recommended for immediate integration. Relevant only when the project expands to structure-based drug discovery.

### ChemSpider

- **URL:** https://www.chemspider.com/
- **Contains:** 35M+ chemical structures, 9,700+ natural products, metadata from 100+ sources
- **Access Method:** Web interface + API
- **Authentication:** API key required
- **Formats:** Various chemical formats
- **License:** Free version available
- **OM Relevance:** Low — chemical structure aggregator. Our ChemBL and PubChem data already cover structure needs.
- **Integration Approach:** Not recommended unless we need to resolve chemical identifiers across databases.

---

## Multi-Source Aggregators

### NCBI Entrez APIs

- **URL:** https://www.ncbi.nlm.nih.gov/home/develop/api/
- **Contains:** Gateway to PubMed, Gene, Protein, Nucleotide, Taxonomy, and 30+ other NCBI databases
- **Access Method:** E-utilities REST API + R (rentrez) + Python (Biopython) + command line (Entrez Direct)
- **Authentication:** API key recommended (3 req/sec without, 10 req/sec with key)
- **Formats:** XML, JSON
- **License:** Public domain
- **OM Relevance:** Medium — not a database itself but the programmatic gateway to many NCBI resources. Useful for PubMed literature mining and cross-referencing gene/protein data.
- **Integration Approach:** Use Biopython's Entrez module. Register for API key for higher rate limits. Use for literature mining (PubMed) and gene annotation (Gene database).

---

## Integration Priority Recommendations

### Tier 1 — High Priority (Integrate Next)

These fill critical gaps identified in `docs/next-steps/bridging-the-gap.md`:

| Database | Why | Effort | Gap Filled |
|----------|-----|--------|------------|
| **STRING** | PPI network for OM targets; REST API is straightforward | Medium | Network Pharmacology (Goal 4) |
| **Reactome** | Native Neo4j format; detailed pathway data | Medium | Pathway data (Goal 3) |
| **ClinicalTrials.gov** | Free JSON API, no auth; find OM trial outcomes | Low | Clinical evidence gap |
| **SIDER** | Simple TSV download; side effect profiles | Low | Safety assessment |
| **OpenFDA** | Free JSON API; real-world adverse event signal | Low-Medium | Safety assessment |
| **DGIdb** | Aggregates 40+ drug-gene sources; GraphQL API | Low-Medium | Drug-target completeness |

### Tier 2 — Medium Priority (Builds Depth)

| Database | Why | Effort | Gap Filled |
|----------|-----|--------|------------|
| **KEGG** | Pathway-gene mappings for mechanistic understanding | Medium | Pathway data (alternative/complement to Reactome) |
| **DrugBank** | Comprehensive drug data but requires API key management | Medium | Drug-target completeness |
| **Dr. Duke's** | CC0 CSV download; ethnobotanical activity data | Low | Plant compound evidence |
| **HIT 2.0** | Herbal ingredient-target pairs with quality scores | Medium (scraping) | Ayurvedic compound targets |
| **BindingDB** | Quantitative binding data for candidate ranking | Medium | Binding affinity data |
| **GEO** | OM gene expression studies for target validation | Medium-High | Gene expression evidence |

### Tier 3 — Lower Priority (Nice to Have)

| Database | Why | Effort |
|----------|-----|--------|
| **WikiPathways** | Supplements Reactome pathways | Low |
| **BioGRID** | Higher-confidence PPI (experimental only) | Low-Medium |
| **TCMBank / TCMSID** | TCM-Ayurveda cross-validation | Medium |
| **COCONUT / NPAtlas** | Novel natural product scaffolds | Medium |
| **PharmGKB** | Pharmacogenomic context | Medium |
| **DDinter** | Drug interaction risk assessment | Low |
| **HMDB** | Metabolite pathways | Medium |
| **Harmonizome** | Gene annotation aggregator | Low-Medium |
| **UniProt** | Protein enrichment for existing targets | Low |
| **GRAYU** | Ayurvedic systems pharmacology (if data exportable) | Unknown |

### Integration Architecture

All new scrapers should follow the established pattern in `src/scrapers/`:

```
src/scrapers/{source_name}/
    {source_name}_scraper.py    # Main scraper with argparse CLI
    __init__.py                 # Module init (if needed)
```

**Standard conventions:**
- Path resolution: `PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))`
- Output to: `data/processed/{source_name}_*.csv`
- CLI flags: `--test` (small run), source-specific mode flags
- Rate limiting: `time.sleep(0.5)` minimum between API calls
- CSV escaping: use `src/utils/escape_csv_field.py`
- Error handling: try/except with graceful degradation
- Dependencies: add to `requirements.txt`

### Suggested Build Order

1. **STRING** + **Reactome** (in parallel — fills the two biggest gaps: PPI and pathways)
2. **ClinicalTrials.gov** + **SIDER** (in parallel — clinical evidence and safety data)
3. **DGIdb** + **OpenFDA** (in parallel — drug-gene aggregation and adverse events)
4. **Dr. Duke's** + **KEGG** (in parallel — ethnobotany and pathway complement)
5. **DrugBank** + **BindingDB** (in parallel — comprehensive drug data and binding affinities)
6. Remaining Tier 2 and Tier 3 as needed
