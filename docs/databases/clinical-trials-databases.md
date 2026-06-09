# Clinical Trials Databases

Catalog of clinical trials registries and databases relevant to the OSPF Ayurveda Knowledge Graph project. Organized by scope, with notes on data access and relevance to Oral Mucositis research.

**Last updated:** 2026-06-08

---

## Table of Contents

- [Major Global Registries](#major-global-registries)
- [Regional / National Registries](#regional--national-registries)
- [Disease-Specific & Specialized](#disease-specific--specialized)
- [Industry & Pharma Registries](#industry--pharma-registries)
- [Results & Literature Databases](#results--literature-databases)
- [OM Project Relevance](#om-project-relevance)

---

## Major Global Registries

| Database | Scope | Notes |
|----------|-------|-------|
| **ClinicalTrials.gov** | US & international | Largest single registry; maintained by NLM/NIH |
| **WHO ICTRP** | Global | Meta-registry aggregating 17+ national registries |
| **EU Clinical Trials Register (EUCTR)** | European Union | EMA-maintained; being replaced by CTIS |
| **Clinical Trials Information System (CTIS)** | EU | New EU register under Clinical Trials Regulation |
| **ISRCTN Registry** | International | Originally UK-focused, now global; BMC-managed |

---

## Regional / National Registries

| Database | Region |
|----------|--------|
| **ANZCTR** (Australian New Zealand Clinical Trials Registry) | Australia / NZ |
| **CTRI** (Clinical Trials Registry - India) | India |
| **ChiCTR** (Chinese Clinical Trial Registry) | China |
| **DRKS** (German Clinical Trials Register) | Germany |
| **JPRN** (Japan Primary Registries Network) | Japan |
| **IRCT** (Iranian Registry of Clinical Trials) | Iran |
| **REBEC** (Brazilian Clinical Trials Registry) | Brazil |
| **PACTR** (Pan African Clinical Trials Registry) | Africa |
| **SLCTR** (Sri Lanka Clinical Trials Registry) | Sri Lanka |
| **TCTR** (Thai Clinical Trials Registry) | Thailand |
| **CRiS** (Clinical Research Information Service) | South Korea |
| **RPCEC** (Cuban Public Registry of Clinical Trials) | Cuba |
| **LBCTR** (Lebanese Clinical Trials Registry) | Lebanon |
| **REPEC** (Peruvian Clinical Trials Registry) | Peru |

---

## Disease-Specific & Specialized

| Database | Focus |
|----------|-------|
| **NCI Cancer Trials (PDQ)** | Cancer-specific trials from the National Cancer Institute |
| **NIAID HIV/AIDS Clinical Trials** | HIV/AIDS trials |
| **Cochrane CENTRAL** | Systematic review of controlled trials across all diseases |
| **AACT** (Aggregate Analysis of ClinicalTrials.gov) | Structured relational database mirror of ClinicalTrials.gov; downloadable as PostgreSQL dump |

---

## Industry & Pharma Registries

| Database | Operator |
|----------|----------|
| **GSK Clinical Study Register** | GlaxoSmithKline |
| **Roche Clinical Trial Results** | Roche |
| **Novartis Clinical Trial Results** | Novartis |
| **Pfizer Clinical Trials** | Pfizer |
| **Lilly Trial Guide** | Eli Lilly |
| **AstraZeneca Clinical Trials** | AstraZeneca |
| **PhRMA Clinical Trial Results** | Industry consortium |

---

## Results & Literature Databases

| Database | Purpose |
|----------|---------|
| **PubMed / MEDLINE** | Published trial results (not a registry, but essential for trial outcomes) |
| **Cochrane Library** | Systematic reviews of trial evidence |
| **OpenTrials** | Open-data aggregator linking trials across registries |
| **TrialTrove** (Citeline) | Commercial competitive intelligence on trials |
| **Cortellis Clinical Trials** (Clarivate) | Commercial trial analytics platform |
| **GlobalData Clinical Trials** | Commercial trial tracking |

---

## OM Project Relevance

The most actionable databases for the Oral Mucositis knowledge graph:

1. **ClinicalTrials.gov / AACT** — AACT provides a PostgreSQL dump of ClinicalTrials.gov, making it far easier to programmatically query for OM-related trials than scraping the website directly.
2. **NCI PDQ** — Since OM is primarily a side effect of cancer treatment (chemotherapy and radiation), NCI's cancer-specific registry contains high-relevance trials.
3. **WHO ICTRP** — Catches trials registered only in regional registries, especially CTRI for Ayurvedic and traditional medicine trials conducted in India.
4. **CTRI** — India's clinical trials registry is particularly relevant for this project given its focus on Ayurvedic compounds; many traditional medicine trials are registered here and may not appear in ClinicalTrials.gov.
