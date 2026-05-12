# Drug Discovery Agents & Skills Roadmap

A collaborative agent pipeline for finding optimal drug candidates for Oral Mucositis through the OSPF Ayurveda Knowledge Graph.

## Design Philosophy

Real drug discovery teams have specialists — medicinal chemists, pharmacologists, oncologists, ethnobotanists, toxicologists. Each reasons deeply in their domain, then a project lead synthesizes their input. This agent architecture mirrors that structure: narrow, deep skills orchestrated by a ranker.

## Agent Architecture

### Skills vs. Agents — Two Layers

The system has two distinct layers:

1. **Skills** (`.claude/skills/*/SKILL.md`) — Domain knowledge bases. Each skill file contains frameworks, scoring rubrics, data source locations, and output formats for a specific discipline. Think of these as each agent's "education."

2. **Agents** — Autonomous workers spawned by the `drug-discovery-pipeline` orchestrator. Each agent reads a skill file to acquire its expertise, then applies that expertise to the specific research question. Multiple agents run in parallel and their findings are synthesized through structured debate.

### Multi-Round Collaboration Protocol

```
┌──────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                              │
│                /drug-discovery-pipeline                      │
└──────────────────────┬───────────────────────────────────────┘
                       │
    ┌──────────────────┼──────────────────────┐
    │           PHASE 1: Analysis             │
    │          (6 agents in parallel)          │
    │                                         │
    │  Chemist ─────────┐                     │
    │  Cancer Researcher ┤                    │
    │  Ethnobotany ──────┤  All run          │
    │  Target Profiler ──┤  simultaneously    │
    │  ADMET Predictor ──┤  on the same      │
    │  Disease Modeler ──┘  candidates        │
    └──────────────────┬──────────────────────┘
                       │ Round 1 findings
    ┌──────────────────┼──────────────────────┐
    │     ORCHESTRATOR SYNTHESIS #1            │
    │  • Tabulate scores across agents        │
    │  • Identify agreements and conflicts     │
    │  • Route cross-agent questions           │
    └──────────────────┬──────────────────────┘
                       │
    ┌──────────────────┼──────────────────────┐
    │         PHASE 2: Deep Dives             │
    │        (4 agents in parallel)            │
    │  Informed by Round 1 conflicts           │
    │                                         │
    │  Pathway Analyst ─────┐                  │
    │  Safety Pharmacologist ┤                │
    │  Drug Repurposing ─────┤                │
    │  SAR Analyst ──────────┘                │
    └──────────────────┬──────────────────────┘
                       │ Round 2 findings
    ┌──────────────────┼──────────────────────┐
    │        DEBATE ROUND                     │
    │       (2 agents in parallel)             │
    │                                         │
    │  Devil's Advocate ── Attacks consensus  │
    │  Integration Agent ── Resolves conflicts │
    └──────────────────┬──────────────────────┘
                       │ Refined positions
    ┌──────────────────┼──────────────────────┐
    │      PHASE 3: Final Evaluation          │
    │        (3 agents in parallel)            │
    │                                         │
    │  Candidate Ranker ── Final scoring      │
    │  Combination Designer ── Best combos    │
    │  Clinical Feasibility ── Path to patients│
    └──────────────────┬──────────────────────┘
                       │
    ┌──────────────────┼──────────────────────┐
    │      FINAL SYNTHESIS (Orchestrator)      │
    │  Consensus report with:                 │
    │  • Ranked candidates                    │
    │  • Expert agreement map                 │
    │  • Resolved conflicts                   │
    │  • Recommended combination              │
    │  • Path to patients                     │
    │  • Remaining uncertainties              │
    └─────────────────────────────────────────┘
```

### Execution Modes

| Mode | Agents | Rounds | Duration | Use When |
|------|--------|--------|----------|----------|
| **Quick** | 6 + Ranker | 1 | 3-5 min | Initial screening, "quick look at X" |
| **Standard** | 6 + 4 + 2 + 3 | 4 | 10-20 min | Evaluating a known candidate set |
| **Deep** | Scout + 6 + 4 + 2 + 3 + Literature | 5+ | 20-40 min | "Find the best possible drug for OM" |

## Existing Skills

| Skill | Focus |
|-------|-------|
| **chemist** | SMILES parsing, SAR, physicochemical properties, drug-likeness, structural similarity |
| **cancer-researcher** | Oncology trials, biomarkers, resistance mechanisms, drug classes, clinical feasibility |
| **graphrag-expert** | Neo4j queries, Cypher, embedding strategies, RAG retrieval |

---

## Proposed Skills

### Tier 1 — Target & Disease Intelligence

#### 1. `target-profiler`
**Focus:** Deep analysis of a specific molecular target (gene/protein).
**What it does:**
- Aggregates everything the KG knows about a target: associated diseases, known drugs, pathway membership, expression data, druggability assessment
- Answers: "Is this target worth pursuing for OM?"
- Queries Neo4j and cross-references ChemBL mechanism data

**Relationship to existing skills:** Complements cancer-researcher (which reasons broadly about cancer) by zooming into individual targets.

**Data sources:** `chembl_drug_targets.csv`, `chembl_drug_mechanisms.csv`, `disgenet_gene_disease.csv`, `pubchem_phytochem_target_interactions.csv`

---

#### 2. `pathway-analyst`
**Focus:** Biological pathway and network-level analysis.
**What it does:**
- Maps how targets relate within signaling cascades (NF-κB, MAPK/ERK, PI3K/AKT/mTOR, Wnt, JAK/STAT)
- Identifies pathway-level vulnerabilities and combination opportunities
- Evaluates whether a candidate addresses one pathway node or multiple

**Why it matters for OM:** Oral mucositis involves overlapping inflammatory, apoptotic, and wound-healing pathways. A pathway-level view reveals intervention points that single-target analysis misses.

**Data sources:** Target-pathway mappings from ChemBL mechanisms, PubChem interactions, literature knowledge

---

#### 3. `disease-modeler`
**Focus:** OM-specific pathobiology modeling.
**What it does:**
- Maintains a structured model of the 5-phase Sonis model (initiation → upregulation → signal amplification → ulceration → healing)
- Maps which OM phase each candidate drug addresses
- Identifies which phases are underserved by current therapies
- Connects disease biology to specific molecular targets

**Why it matters:** Ensures candidates are evaluated against actual disease biology, not just generic "anti-inflammatory" labels.

---

### Tier 2 — Compound Discovery & Evaluation

#### 4. `ethnobotany-expert`
**Focus:** Traditional medicine knowledge and Ayurvedic formulation reasoning.
**What it does:**
- Reasons about *why* traditional formulations combine specific plants (synergy, bioavailability enhancement, side-effect mitigation)
- Bridges IMPPAT/MedPlant data to modern pharmacology
- Translates "used for mouth sores in Ayurveda" into testable mechanistic hypotheses
- Evaluates Rasa Shastra (Ayurvedic pharmacology) principles

**Why it matters:** This is the project's unique differentiator. Neither chemist nor cancer-researcher covers the traditional medicine reasoning that justifies investigating these compounds.

**Data sources:** `imppat_plant_part_phytochemicals.json`, `imppat_therapeutic_uses.csv`, `medplant_*.csv`

---

#### 5. `admet-predictor`
**Focus:** ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) prediction.
**What it does:**
- Predicts oral bioavailability, metabolic stability, CYP450 interactions, hERG liability, hepatotoxicity risk from molecular structure
- Acts as the go/no-go gatekeeper: great target activity + terrible ADMET = dead end
- Special focus on plant-derived compound challenges (high MW, poor bioavailability, polyphenol metabolism)

**Relationship to existing skills:** Spins out of chemist's ADMET mention into deep, dedicated analysis. Chemist identifies structural features; admet-predictor evaluates their pharmacokinetic consequences.

**Data sources:** Physicochemical descriptors in `chembl_approved_drugs.csv`, `chembl_natural_products.csv`

---

#### 6. `sar-analyst` (Structure-Activity Relationship)
**Focus:** Systematic SAR reasoning and analog comparison.
**What it does:**
- Deep-dives into structure-activity relationships beyond chemist's general analysis
- Systematic comparison of structural analogs
- Identifies pharmacophores (minimal structural features required for activity)
- Suggests structural modifications to improve potency/selectivity/ADMET
- Evaluates scaffold hopping opportunities

**Relationship to existing skills:** Spins out of chemist's SAR framework into dedicated, deeper analysis. Chemist does broad structural reasoning; SAR-analyst does systematic analog-by-analog comparison.

**Data sources:** SMILES strings and descriptors from all ChemBL CSVs

---

#### 7. `natural-product-scout`
**Focus:** Lead compound identification from natural product sources.
**What it does:**
- Scans ChemBL natural products, IMPPAT phytochemicals, and PubChem interactions to surface compounds hitting OM-relevant targets
- Applies filters: known safety profile, structural novelty, plant source availability
- Generates initial hit lists that feed into the evaluation pipeline
- Identifies "privileged scaffolds" — natural product frameworks with known drug-like properties

**Data sources:** `chembl_natural_products.csv`, `imppat_plant_part_phytochemicals.json`, `pubchem_phytochem_target_interactions.csv`

---

### Tier 3 — Comparative Analysis & Ranking

#### 8. `drug-repurposing-strategist`
**Focus:** Systematic repurposing hypothesis generation.
**What it does:**
- Compares approved drugs' known targets against OM-relevant targets from DisGeNET
- Ranks candidates by: number of relevant targets, existing safety data, route of administration compatibility (topical/oral for OM), patent status
- Identifies "low-hanging fruit" — approved drugs that could be repurposed with minimal new clinical data

**Relationship to existing skills:** Bridges cancer-researcher (drug class knowledge) and chemist (structural knowledge) into actionable repurposing hypotheses.

**Data sources:** `chembl_approved_drugs.csv`, `chembl_drug_mechanisms.csv`, `chembl_drug_indications.csv`, `disgenet_gene_disease.csv`

---

#### 9. `candidate-ranker`
**Focus:** Multi-criteria decision analysis and final candidate prioritization.
**What it does:**
- Takes all candidate compounds and scores across dimensions:
  - Target relevance (from target-profiler)
  - Structural drug-likeness (from chemist)
  - ADMET prediction (from admet-predictor)
  - Clinical precedent (from cancer-researcher)
  - Traditional use evidence (from ethnobotany-expert)
  - Pathway coverage (from pathway-analyst)
  - Disease phase coverage (from disease-modeler)
- Produces a ranked shortlist with clear rationale for each score
- Identifies gaps: "No candidate addresses the ulceration phase"

**Role:** The orchestrator — consumes output from all other skills and produces the final recommendation.

---

#### 10. `combination-designer`
**Focus:** Rational multi-compound strategy design.
**What it does:**
- Identifies synergistic combinations (e.g., NF-κB blocker + epithelial healing promoter)
- Evaluates whether traditional multi-plant formulations have rational pharmacological bases
- Checks for drug-drug interaction risks (critical for cancer patients on complex regimens)
- Designs combinations targeting multiple OM phases simultaneously

**Why it matters:** Ayurvedic formulations are inherently combinations. This skill evaluates whether that traditional wisdom has a mechanistic basis.

---

### Tier 4 — Validation & Evidence

#### 11. `literature-reviewer`
**Focus:** Systematic evidence gathering and appraisal.
**What it does:**
- For any compound-target-disease hypothesis, summarizes supporting/contradicting evidence
- Assigns evidence levels (in vitro → animal model → clinical case report → RCT)
- Prevents the pipeline from generating hypotheses that have already been tested and failed
- Identifies knowledge gaps where new research is most needed

---

#### 12. `clinical-feasibility-assessor`
**Focus:** Practical development pathway evaluation.
**What it does:**
- For top candidates: regulatory path, estimated cost/timeline, existing formulations
- OM-specific considerations: cancer patients undergoing chemo/radiation, immunocompromised, route of administration
- Evaluates whether a candidate could realistically reach patients

**Relationship to existing skills:** Spins out of cancer-researcher's trial design and FDA pathway knowledge, focused on practical "Could this actually get to patients?" questions.

---

#### 13. `safety-pharmacologist`
**Focus:** Toxicity and drug interaction risk assessment.
**What it does:**
- Evaluates known toxicities, drug-drug interactions, contraindications, therapeutic window
- Cancer patient-specific concerns: immunocompromised status, hepatic/renal impairment from treatment, polypharmacy
- Goes beyond ADMET prediction into clinical safety context

---

## Collaboration Architecture

```
                    ┌──────────────────┐
                    │  candidate-ranker │  ← Final output: ranked shortlist
                    └────────┬─────────┘
                             │ consumes scores from ↓
          ┌──────────────────┼──────────────────────┐
          │                  │                       │
  ┌───────┴────────┐  ┌─────┴──────┐  ┌────────────┴───────────┐
  │ target-profiler │  │ ADMET-     │  │ clinical-feasibility-  │
  │ pathway-analyst │  │ predictor  │  │ assessor               │
  │ disease-modeler │  │ safety-    │  │ literature-reviewer    │
  └───────┬────────┘  │ pharmacol. │  └────────────────────────┘
          │           └─────┬──────┘
          │                 │
  ┌───────┴─────────────────┴──────┐
  │  Candidate Generation Layer    │
  │  ┌─────────────────────────┐   │
  │  │ natural-product-scout   │   │
  │  │ drug-repurposing-strat. │   │
  │  │ ethnobotany-expert      │   │
  │  │ SAR-analyst             │   │
  │  │ combination-designer    │   │
  │  └─────────────────────────┘   │
  └────────────────────────────────┘
          │
  ┌───────┴────────┐
  │  Existing KG   │  ← ChemBL, DisGeNET, IMPPAT, PubChem, MedPlant
  │  (Neo4j + CSV) │
  └────────────────┘
```

## Build Priority

| Priority | Skill | Rationale |
|----------|-------|-----------|
| **1** | `candidate-ranker` | Orchestrator — no point generating candidates without ranking them |
| **2** | `ethnobotany-expert` | Project's unique differentiator — no other tool does this |
| **3** | `target-profiler` | Foundational for all downstream target-based reasoning |
| **4** | `admet-predictor` | Critical go/no-go gate; spins naturally from chemist |
| **5** | `drug-repurposing-strategist` | Directly serves the project's core mission |
| **6** | `pathway-analyst` | Unlocks combination and multi-target reasoning |
| **7** | `disease-modeler` | Ensures OM-specific evaluation |
| **8** | `natural-product-scout` | Lead generation from existing data |
| **9** | `sar-analyst` | Deep structural optimization |
| **10** | `combination-designer` | Multi-compound strategies |
| **11** | `literature-reviewer` | Evidence validation |
| **12** | `clinical-feasibility-assessor` | Practical pathway evaluation |
| **13** | `safety-pharmacologist` | Safety gate for final candidates |

## Infrastructure Skills

These skills support the pipeline rather than performing drug discovery reasoning directly.

### `frontend-developer`
**Focus:** Prototype web UI to display pipeline outputs and knowledge graph data.
**What it does:**
- Builds a Vite + React prototype that displays pre-generated Claude analysis reports (scorecards, ADMET profiles, pathway maps)
- Interactive browsing of knowledge graph data (drugs, compounds, targets, plants)
- OM phase timeline visualization showing candidate coverage
- Pathway diagrams with drug candidate overlay
- Compound explorer with filtering and sorting

**Stack:** Vite + React + TypeScript + Tailwind CSS + Recharts/D3.js

**Data integration:** Reads directly from `data/processed/` CSVs and `data/reports/` JSON files. No backend needed.

---

### `data-scraper`
**Focus:** Build and run scrapers for new biomedical data sources.
**What it does:**
- Follows established scraper patterns from `src/scrapers/` (ChemBL, DisGeNET, IMPPAT, PubChem, MedPlant)
- Produces Neo4j-ready CSV output to `data/processed/`
- Includes rate limiting, test mode, raw data preservation, and resumability

**High-priority new data sources:**
1. **TTD** (Therapeutic Target Database) — drug-target-disease mappings
2. **DrugBank** — comprehensive drug pharmacology and interaction data
3. **UniProt** — protein function, pathway, and expression data
4. **KEGG** — structured pathway-gene mappings
5. **ClinicalTrials.gov** — OM-related clinical trials and interventions
6. **Open Targets** — target-disease associations with evidence scores

**Medium-priority sources:** STRING (protein interactions), Reactome (pathway detail), NPACT (plant anticancer compounds), TCMSP (traditional Chinese medicine)
