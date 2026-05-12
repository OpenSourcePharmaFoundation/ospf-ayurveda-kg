# Oral Mucositis in Breast Cancer: Drug Repurposing & Ayurvedic Bridge Analysis

**Analysis Date:** 2026-05-03
**Data Sources:** ChemBL, DisGeNET, TTD, IMPPAT, PubChem, DrugBank (via Neo4j knowledge graph)
**Focus:** Identifying treatment candidates for chemotherapy-induced oral mucositis (OM) in breast cancer patients, including Ayurvedic bridge compounds

---

## Executive Summary

Oral mucositis is one of the most debilitating side effects of breast cancer chemotherapy — painful ulceration of the oral mucosa that can force dose reductions or treatment interruptions. This analysis cross-references the project's scraped drug databases to identify repurposing candidates, breast cancer-specific intersections, OM-relevant biomarkers, and Ayurvedic medicinal plants with traditional use for oral/mucosal conditions.

**Key Findings:**
- Only **4 drugs** in TTD have direct OM indications — the field is severely underserved
- **131 approved drugs** match the oral mucosal delivery fingerprint but aren't currently indicated for OM
- **11 candidates** are already indicated for breast cancer, enabling dual-purpose use
- **Glycyrrhiza glabra** (Licorice) emerges as the strongest Ayurvedic bridge candidate
- **Cimetidine** is a practical "hidden gem" — cheap, available, ideal molecular profile, and already used in cancer patients

---

## 1. Current State: Approved OM Treatments (TTD Data)

The Therapeutic Target Database contains only **4 drugs** with direct Oral Mucositis indications:

| Drug | Target Gene | Target Protein | Reference |
|------|-------------|----------------|-----------|
| Palifermin | FGFR2 | Fibroblast growth factor receptor 2 | PMID: 19456212 |
| Hebervis | EGF | Epidermal growth factor | Leadership in BioBusiness |
| Lactermin | — | — | PMID: 16261254 |
| AG-013 | TFF1 | Trefoil factor-1 | PMID: 20542722 |

**Context:** Palifermin (Kepivance) is the *only* FDA-approved drug specifically for OM, and only in the hematopoietic stem cell transplant setting — not general chemotherapy. This underscores why repurposing is essential.

---

## 2. The Oral/Mucosal Drug Fingerprint (ChemBL Analysis)

### Statistical Profile (n=113 drugs currently treating oral/mucosal conditions)

| Property | Mean | Std Dev | Min | Max | Optimal Range |
|----------|------|---------|-----|-----|---------------|
| Molecular Weight (Da) | 353.2 | 186.0 | 18.0 | 914.2 | 167 - 539 |
| LogP (lipophilicity) | 2.23 | 2.04 | -1.41 | 7.64 | 0.2 - 4.3 |
| Polar Surface Area (Å²) | 88.4 | — | — | — | 50 - 130 |
| H-Bond Donors | 2.1 | — | — | — | 1 - 4 |
| H-Bond Acceptors | 5.1 | — | — | — | 3 - 7 |

### Why These Properties Matter for Topical Oral Delivery

1. **LogP 0.2-4.3 (Moderate Lipophilicity)** — Allows penetration through oral mucosa's lipid membranes while remaining soluble enough for aqueous formulation (gels, rinses). Too hydrophilic (LogP < 0) = won't penetrate; too lipophilic (LogP > 5) = won't release from formulation.

2. **PSA 50-130 Å²** — Balances membrane permeability with tissue retention. Higher PSA molecules stay in aqueous compartments; lower PSA molecules pass through too quickly.

3. **Molecular Weight < 500 Da** — Oral mucosa is thin (3-5 cell layers vs 15+ for skin), so smaller molecules diffuse more easily. Aligns with Lipinski's Rule of Five.

4. **H-Bond Donors/Acceptors (2/5)** — Moderate H-bonding allows water solubility for formulation without blocking membrane penetration.

---

## 3. Top Repurposing Candidates

### Tier 1: Strongest Candidates (Already Treat Mucosal Inflammation)

| Rank | Drug | ChemBL ID | MW | LogP | PSA | Current Indications | Rationale |
|------|------|-----------|-----|------|-----|---------------------|-----------|
| 1 | **MESALAMINE** | CHEMBL704 | 153.1 | 0.67 | 83.6 | Ulcerative colitis, IBD, Crohn's | Already treats mucosal inflammation; ideal molecular profile for oral rinse |
| 2 | **AZATHIOPRINE** | CHEMBL1542 | 277.3 | 1.15 | 115.4 | RA, ulcerative colitis, dermatitis | Immunomodulator proven in mucosal disease |
| 3 | **TOFACITINIB** | CHEMBL221959 | 312.4 | 1.54 | 88.9 | RA, ulcerative colitis | JAK inhibitor; blocks IL-6/IFN-γ cytokine signaling implicated in OM |
| 4 | **NALTREXONE** | CHEMBL19019 | 341.4 | 1.53 | 70.0 | Alcohol/nicotine dependence | Low-dose naltrexone shows anti-inflammatory effects on mucosa |

### Tier 2: Anti-Inflammatory Candidates

| Rank | Drug | ChemBL ID | MW | LogP | PSA | Current Indications | Rationale |
|------|------|-----------|-----|------|-----|---------------------|-----------|
| 5 | **NEPAFENAC** | CHEMBL1021 | 254.3 | 1.53 | 86.2 | Eye inflammation | NSAID proven on mucosal tissue (ocular) |
| 6 | **PIROXICAM** | CHEMBL527 | 331.4 | 1.58 | 99.6 | RA, eye inflammation, OA | NSAID with mucosal experience |
| 7 | **CANTHARIDIN** | CHEMBL48449 | 196.2 | 0.64 | 52.6 | RA, inflammation | Natural product; anti-inflammatory |
| 8 | **AMINOSALICYLIC ACID** | CHEMBL1169 | 153.1 | 0.67 | 83.6 | Ulcerative colitis, Crohn's | Same scaffold as mesalamine |

### Tier 3: JAK Inhibitor Family (Emerging Class)

| Rank | Drug | ChemBL ID | MW | LogP | PSA | Current Indications | Rationale |
|------|------|-----------|-----|------|-----|---------------------|-----------|
| 9 | **ABROCITINIB** | CHEMBL3655081 | 323.4 | 1.25 | 91.0 | Atopic eczema, psoriasis | JAK1 selective; less immunosuppressive |
| 10 | **RITLECITINIB** | CHEMBL4085457 | 285.4 | 1.94 | 73.9 | RA, ulcerative colitis, Crohn's | JAK3/TEC family inhibitor |
| 11 | **PEFICITINIB** | CHEMBL3137308 | 326.4 | 2.01 | 104.0 | RA, ulcerative colitis | Pan-JAK inhibitor |
| 12 | **FILGOTINIB** | CHEMBL3301607 | 425.5 | 1.98 | 96.7 | RA, ulcerative colitis, Crohn's | JAK1 selective |

---

## 4. The Breast Cancer Intersection

These **11 candidate drugs** are already indicated for breast cancer, meaning they're already in the treatment regimen and could potentially serve dual purpose — treating the cancer while also addressing OM:

| Drug | ChemBL ID | LogP | MW | Role in Breast Cancer | OM Potential |
|------|-----------|------|----|----------------------|--------------|
| **LETROZOLE** | CHEMBL1444 | 2.66 | 285.3 | Aromatase inhibitor (1st-line hormonal therapy) | Natural product; fits oral delivery profile |
| **CAPSAICIN** | CHEMBL294199 | 3.79 | 305.4 | Pain management in cancer patients | Topical analgesic; could address OM pain directly |
| **CIMETIDINE** | CHEMBL30 | 0.60 | 252.4 | Immune modulation in breast cancer | H2 blocker with anti-inflammatory properties; ideal MW/LogP |
| **BINIMETINIB** | CHEMBL3187723 | 3.01 | 441.2 | MEK inhibitor (targeted therapy) | Targets MAPK cascade — relevant to OM pathogenesis |
| **LEFLUNOMIDE** | CHEMBL960 | 3.25 | 270.2 | Anti-proliferative, immunomodulator | Pyrimidine synthesis inhibitor; anti-inflammatory |
| **SUNITINIB** | CHEMBL1567 | 3.33 | 398.5 | Multi-kinase inhibitor (targeted therapy) | Anti-angiogenic; could reduce OM-associated inflammation |
| **CARMUSTINE** | CHEMBL513 | 1.16 | 214.1 | Alkylating agent (chemotherapy) | Natural product with ideal molecular properties |
| **MELPHALAN** | CHEMBL852 | 1.93 | 305.2 | Alkylating agent (chemotherapy) | Already used in cancer; fits mucosal delivery profile |
| **CEPHALEXIN** | CHEMBL1200544 | 0.44 | 347.4 | Infection management | Antibiotic; addresses secondary OM infections |
| **RANITIDINE** | CHEMBL1790041 | 1.46 | 314.4 | GI side effect management | H2 blocker; anti-inflammatory potential on mucosa |
| **LANSOPRAZOLE** | CHEMBL480 | 3.52 | 369.4 | GI protection during treatment | PPI with emerging anti-inflammatory evidence |

### Spotlight: Cimetidine as a Hidden Gem

Cimetidine stands out as a particularly practical candidate:
- **Ideal physicochemical profile**: LogP 0.60, MW 252, PSA 88.9 — near-perfect match for the oral mucosal fingerprint
- **Already given to cancer patients** for GI side effects
- **Natural product** with documented immune-modulatory effects
- **Cheap and widely available** worldwide
- **Low toxicity profile** — well-tolerated long-term
- **Breast cancer studies** have shown immunomodulatory benefit (enhances NK cell activity)

---

## 5. DisGeNET Biomarkers — The Molecular Basis of OM

The DisGeNET dataset reveals **51 gene associations** with oral mucositis/stomatitis across three categories:

### Biomarkers (n=51)

Key inflammatory and repair-related biomarkers:

| Gene | Gene ID | Association | Evidence |
|------|---------|-------------|----------|
| **IL17A** | 3605 | Biomarker | Salivary IL-17 elevated in acute leukemia patients with OM during chemotherapy |
| **CSF2 (GM-CSF)** | 1437 | Biomarker | GM-CSF mouthwash studied as OM intervention in head & neck cancer radiotherapy |
| **CASP8** | 841 | Biomarker | Caspase-8 delivery via VLP induces apoptosis in breast cancer cells; connected to stomatitis |
| **CXCR2** | 3579 | Altered Expression | CXCR2 overexpression in mesenchymal stem cells enhances radiation-induced OM treatment |

### Genetic Variants Predicting OM Severity

| Gene | Variant | Evidence |
|------|---------|----------|
| **GHRL** (Ghrelin) | AA genotype | Associated with risk of more severe OM in head & neck cancer patients receiving RT |
| **SLC19A1** | G80A (rs775144154) | Trend toward reduced stomatitis in patients with variants |

### Therapeutic Target Implications

The biomarker data suggests OM pathogenesis involves:
1. **Pro-inflammatory cytokine cascades** (IL-17, TNF, IL-6) — targeted by JAK inhibitors (tofacitinib, abrocitinib)
2. **Apoptotic pathways** (CASP8) — modulated by immunomodulators (azathioprine)
3. **Mucosal repair signaling** (GM-CSF, CXCR2, EGF) — targeted by palifermin, growth factor therapies
4. **Oxidative stress** — addressed by antioxidants (mesalamine, ascorbic acid)

---

## 6. The Ayurvedic Bridge — Medicinal Plants for Oral/Mucosal Conditions

### IMPPAT Data: Plants with Traditional Oral/Mucosal Use

| Plant | Scientific Name | Traditional Use | Ayurvedic Name | Significance |
|-------|----------------|-----------------|----------------|--------------|
| **Licorice** | Glycyrrhiza glabra | Oral ulcer, stomach ulcer | Yashtimadhu | Most studied for mucosal protection; NF-κB inhibition |
| **Haritaki** | Terminalia chebula | Stomatitis | Haritaki | Part of Triphala; strong antioxidant activity |
| **Nutgrass** | Cyperus rotundus | Aphthous stomatitis | Musta | Anti-inflammatory; traditional mouth ulcer remedy |
| **Neem** | Azadirachta indica | Gingivitis, ulcers | Nimba | Broad antimicrobial + anti-inflammatory |
| **Sandalwood** | Santalum album | Ulcers | Chandana | Cooling, anti-inflammatory |
| **Golden Shower** | Cassia fistula | Ulcers | Aragvadha | Purgative with anti-inflammatory properties |
| **Devil Tree** | Alstonia scholaris | Ulcers | Saptaparna | Alkaloid-rich; anti-inflammatory |

### Spotlight: Glycyrrhiza glabra (Licorice) as Strongest Bridge Candidate

Glycyrrhiza glabra represents the ideal Ayurvedic bridge compound for OM:

- **Traditional use**: Explicitly used for oral ulcers in Ayurvedic medicine (Yashtimadhu)
- **Active compound**: Glycyrrhizin — documented anti-inflammatory activity through NF-κB inhibition, the same pathway implicated in OM pathogenesis
- **Clinical evidence**: Licorice root extract mouthwashes have been studied in clinical settings for chemotherapy-induced OM
- **Mechanism alignment**: Anti-inflammatory + mucosal protective + antioxidant — addresses multiple OM pathogenesis phases
- **Formulation**: Water-soluble glycyrrhizin readily formulated as oral rinse
- **Safety**: Generally well-tolerated; main concern is mineralocorticoid effect at high systemic doses (less relevant for topical oral use)

---

## 7. Formulation Considerations

Based on the molecular fingerprint, optimal formulations for OM would include:

### Oral Rinse/Mouthwash
- **Best for:** Water-soluble drugs (LogP < 2)
- **Candidates:** Mesalamine, Aminosalicylic acid, Cimetidine, Glycyrrhiza glabra extract
- **Advantages:** Easy application, covers entire oral cavity, patient-friendly

### Mucoadhesive Gel
- **Best for:** Moderate lipophilicity (LogP 1-3)
- **Candidates:** Tofacitinib, Nepafenac, Piroxicam
- **Advantages:** Prolonged contact time, localized delivery to ulcerated areas

### Dissolvable Tablet/Lozenge
- **Best for:** Stable compounds with moderate solubility
- **Candidates:** Azathioprine, Naltrexone, Capsaicin
- **Advantages:** Controlled release, patient compliance, portable

---

## 8. Proposed Multi-Pronged Treatment Strategy

Based on the combined data analysis, a rational approach for OM in breast cancer:

| Phase | Intervention | Rationale |
|-------|-------------|-----------|
| **Prevention** | Mesalamine or cimetidine mouthwash before chemotherapy cycles | Mucosal pre-conditioning; anti-inflammatory priming |
| **Acute treatment** | Tofacitinib mucoadhesive gel for active lesions | JAK inhibition blocks cytokine cascade driving tissue damage |
| **Pain management** | Capsaicin topical (already indicated for breast cancer pain) | Dual-purpose; desensitizes nociceptors in oral mucosa |
| **Ayurvedic adjunct** | Glycyrrhiza glabra (licorice) mouthwash | Traditional use + NF-κB mechanism + clinical evidence |
| **Mucosal repair** | GM-CSF (CSF2) mouthwash | Growth factor stimulation of mucosal regeneration |
| **Infection control** | Cephalexin (if secondary infection) | Already indicated in breast cancer; addresses OM complication |

### Safety Caveat

This is a computational analysis based on molecular properties, target overlap, and traditional use data — not clinical evidence. Critical considerations before advancement:

- **Immunosuppression risk**: Azathioprine and JAK inhibitors may compound chemotherapy-induced immunosuppression
- **Drug interactions**: All candidates must be evaluated against active breast cancer regimens (anthracyclines, taxanes, HER2 inhibitors)
- **Topical vs. systemic**: Topical oral formulations may mitigate systemic interaction concerns
- **Patient population**: Breast cancer patients on chemotherapy represent a uniquely vulnerable immunocompromised population

---

## 9. Unified Query

This single Cypher query performs the entire analysis in one pass:
1. Identifies drugs already treating oral/mucosal conditions (exclusion set)
2. Finds repurposing candidates matching the mucosal delivery fingerprint
3. Flags breast cancer intersection candidates
4. Finds DisGeNET biomarker overlap via gene associations
5. Traces Ayurvedic plant-compound-target pathways to OM
6. Collects ChemBL mechanism-of-action data for each candidate

```cypher
// ============================================================================
// Unified Oral Mucositis in Breast Cancer: Drug Repurposing & Ayurvedic Bridge
// ============================================================================
//
// This query performs the full analysis pipeline in a single pass:
//   Part 1: Exclude drugs already indicated for oral/mucosal conditions
//   Part 2: Find candidates matching the mucosal delivery fingerprint
//   Part 3: Enrich with breast cancer flags, biomarker overlap, mechanisms,
//           and Ayurvedic plant-compound-target pathways
//
// Schema relationships used:
//   Drug -[:TREATS_INDICATION]-> Indication          (ChemBL)
//   Drug -[:TREATS]-> Disease                        (DrugBank/TTD)
//   Drug -[:TARGETS]-> Protein                       (DrugBank)
//   Drug -[:HAS_MECHANISM]-> Mechanism -[:ACTS_ON]-> Target  (ChemBL)
//   Target -[:SAME_AS]-> Protein                     (ChemBL-to-DrugBank)
//   Target -[:ENCODED_BY]-> Gene                     (ChemBL)
//   Gene -[:BIOMARKER]-> Disease                     (DisGeNET)
//   Gene -[:EXPRESSION_ASSOCIATION]-> Disease         (DisGeNET)
//   Gene -[:VARIANT_ASSOCIATION]-> Disease            (DisGeNET)
//   Gene -[:TRANSLATION]-> Protein
//   Plant -[:PRODUCES]-> Compound -[:TARGETS]-> Gene/Protein  (IMPPAT/PubChem)
//   Formulation -[:CONTAINS]-> Plant                 (Ayurvedic)
//   Plant -[:TREATS]-> Therapeutic_Area               (IMPPAT)
// ============================================================================

// ── Part 1: Build the exclusion set ─────────────────────────────────────────
// Collect ChemBL IDs of drugs already indicated for oral/mucosal conditions
// so we only surface genuinely novel repurposing candidates.

MATCH (already:Drug)-[:TREATS_INDICATION]->(oral_ind:Indication)
WHERE toLower(oral_ind.name) CONTAINS 'mucositis'
   OR toLower(oral_ind.name) CONTAINS 'oral'
   OR toLower(oral_ind.name) CONTAINS 'stomatitis'
   OR toLower(oral_ind.name) CONTAINS 'gingivitis'
   OR toLower(oral_ind.name) CONTAINS 'pharyngitis'
   OR toLower(oral_ind.name) CONTAINS 'mouth'
WITH collect(DISTINCT already.chembl_id) AS oral_drug_ids

// ── Part 2: Collect OM-associated genes from DisGeNET ───────────────────────
// These are genes linked to Oral Mucositis via biomarker, expression, or
// variant associations — used later to score candidates by target overlap.

OPTIONAL MATCH (om_gene:Gene)-[:BIOMARKER|EXPRESSION_ASSOCIATION|VARIANT_ASSOCIATION]->(om_disease:Disease {name: 'Oral mucositis'})
WITH oral_drug_ids,
     collect(DISTINCT om_gene.name) AS om_gene_names

// ── Part 3: Find fingerprint-matching candidates ────────────────────────────
// Apply the oral mucosal delivery fingerprint derived from 113 existing
// oral/mucosal drugs (see Section 2 of this document).
//
// Optimal ranges:
//   MW:   167–539 Da    (mucosal diffusion)
//   LogP: 0.2–4.3       (lipid membrane penetration + aqueous solubility)
//   PSA:  50–130 Å²     (permeability/retention balance)
//   HBD:  0–4           (moderate H-bonding)
//   HBA:  1–8           (moderate H-bonding)

MATCH (candidate:Drug)-[:TREATS_INDICATION]->(ind:Indication)
WHERE NOT candidate.chembl_id IN oral_drug_ids
  AND candidate.molecular_weight IS NOT NULL
  AND candidate.alogp IS NOT NULL
  AND candidate.psa IS NOT NULL
  AND candidate.molecular_weight >= 167 AND candidate.molecular_weight <= 539
  AND candidate.alogp >= 0.2 AND candidate.alogp <= 4.3
  AND candidate.psa >= 50 AND candidate.psa <= 130
  AND candidate.hbd >= 0 AND candidate.hbd <= 4
  AND candidate.hba >= 1 AND candidate.hba <= 8

// Collect all indications per candidate
WITH candidate, om_gene_names,
     collect(DISTINCT ind.name) AS all_indications

// ── Part 4: Flag breast cancer intersection ─────────────────────────────────
// Check if any of the candidate's indications involve breast cancer,
// enabling dual-purpose treatment identification.

WITH candidate, om_gene_names, all_indications,
     any(i IN all_indications WHERE
         toLower(i) CONTAINS 'breast cancer'
         OR toLower(i) CONTAINS 'breast carcinoma'
         OR toLower(i) CONTAINS 'breast neoplasm'
     ) AS has_breast_cancer_indication

// ── Part 5: Enrich with mechanism of action (ChemBL) ────────────────────────
// Pull the drug's mechanism(s) and their molecular targets so we can
// assess whether the candidate acts on OM-relevant pathways.

OPTIONAL MATCH (candidate)-[:HAS_MECHANISM]->(mech:Mechanism)-[:ACTS_ON]->(target:Target)
WITH candidate, om_gene_names, all_indications, has_breast_cancer_indication,
     collect(DISTINCT {
       action: mech.action_type,
       mechanism: mech.mechanism_of_action,
       target_name: target.name,
       target_type: target.target_type
     }) AS mechanisms

// ── Part 6: Check DisGeNET biomarker overlap ────────────────────────────────
// See if the drug targets proteins/genes that are associated with OM
// in DisGeNET. This is the "mechanistic rationale" score.
//
// Path 1: Drug -[:TARGETS]-> Protein <-[:TRANSLATION]- Gene (in om_gene_names)
// Path 2: Drug -[:HAS_MECHANISM]-> Mechanism -[:ACTS_ON]-> Target -[:ENCODED_BY]-> Gene (in om_gene_names)

OPTIONAL MATCH (candidate)-[:TARGETS]->(prot:Protein)<-[:TRANSLATION]-(g1:Gene)
WHERE g1.name IN om_gene_names
WITH candidate, om_gene_names, all_indications, has_breast_cancer_indication,
     mechanisms,
     collect(DISTINCT g1.name) AS direct_om_gene_hits

OPTIONAL MATCH (candidate)-[:HAS_MECHANISM]->(:Mechanism)-[:ACTS_ON]->(t:Target)-[:ENCODED_BY]->(g2:Gene)
WHERE g2.name IN om_gene_names
WITH candidate, all_indications, has_breast_cancer_indication,
     mechanisms, direct_om_gene_hits,
     collect(DISTINCT g2.name) AS mech_om_gene_hits,
     apoc.coll.union(direct_om_gene_hits, collect(DISTINCT g2.name)) AS all_om_gene_hits

// ── Part 7: Find Ayurvedic plant-compound connections ───────────────────────
// Check if any medicinal plant produces a compound that targets the same
// protein(s) as this candidate drug. This is the "Ayurvedic bridge" —
// a plant whose phytochemicals converge on the same molecular target.
//
// Path: Plant -[:PRODUCES]-> Compound -[:TARGETS]-> Protein <-[:TARGETS]- Drug

OPTIONAL MATCH (candidate)-[:TARGETS]->(shared_prot:Protein)<-[:TARGETS]-(compound:Compound)<-[:PRODUCES]-(plant:Plant)
WITH candidate, all_indications, has_breast_cancer_indication,
     mechanisms, all_om_gene_hits,
     collect(DISTINCT {
       plant: plant.scientificName,
       plant_sanskrit: plant.sanskritName,
       compound: compound.name,
       shared_target: shared_prot.name
     }) AS ayurvedic_bridges

// ── Part 8: Check Ayurvedic plant traditional uses for oral conditions ──────
// See if any bridging plant also has traditional therapeutic use for
// oral/mucosal conditions (validating the ethnobotanical rationale).

OPTIONAL MATCH (bridge_plant:Plant)-[:TREATS]->(ta:Therapeutic_Area)
WHERE bridge_plant.scientificName IN [b IN ayurvedic_bridges | b.plant]
  AND (toLower(ta.name) CONTAINS 'oral'
       OR toLower(ta.name) CONTAINS 'stomatitis'
       OR toLower(ta.name) CONTAINS 'ulcer'
       OR toLower(ta.name) CONTAINS 'mouth'
       OR toLower(ta.name) CONTAINS 'gingiv'
       OR toLower(ta.name) CONTAINS 'aphthous')
WITH candidate, all_indications, has_breast_cancer_indication,
     mechanisms, all_om_gene_hits, ayurvedic_bridges,
     collect(DISTINCT {
       plant: bridge_plant.scientificName,
       traditional_use: ta.name
     }) AS traditional_oral_uses

// ── Part 9: Check if candidate is in existing Ayurvedic formulations ────────
// See if the candidate drug's protein targets overlap with compounds
// found in known Ayurvedic formulations (Formulation -[:CONTAINS]-> Plant).

OPTIONAL MATCH (form:Formulation)-[:CONTAINS]->(form_plant:Plant)
WHERE form_plant.scientificName IN [b IN ayurvedic_bridges | b.plant]
WITH candidate, all_indications, has_breast_cancer_indication,
     mechanisms, all_om_gene_hits, ayurvedic_bridges,
     traditional_oral_uses,
     collect(DISTINCT {
       formulation: form.name,
       plant: form_plant.scientificName
     }) AS relevant_formulations

// ── Part 10: Compute composite scores and return ────────────────────────────
// Score each candidate across multiple dimensions:
//   - Fingerprint fit (already filtered — all pass)
//   - Breast cancer relevance (boolean flag)
//   - OM biomarker overlap (count of DisGeNET gene hits)
//   - Ayurvedic bridge strength (count of plant-compound-target paths)
//   - Traditional use validation (count of ethnobotanical corroborations)
//   - Formulation integration (count of existing Ayurvedic formulations)

RETURN
  candidate.chembl_name AS drug_name,
  candidate.chembl_id AS chembl_id,

  // Physicochemical properties
  candidate.molecular_weight AS MW,
  candidate.alogp AS LogP,
  candidate.psa AS PSA,
  candidate.hbd AS HBD,
  candidate.hba AS HBA,
  candidate.natural_product AS is_natural_product,

  // Breast cancer flag
  has_breast_cancer_indication,

  // Current indications
  all_indications,

  // Mechanisms of action
  mechanisms,

  // DisGeNET OM biomarker overlap
  all_om_gene_hits AS om_biomarker_gene_overlap,
  size(all_om_gene_hits) AS om_gene_overlap_count,

  // Ayurvedic bridge data
  ayurvedic_bridges,
  size(ayurvedic_bridges) AS ayurvedic_bridge_count,

  // Traditional oral/mucosal use validation
  traditional_oral_uses,
  size(traditional_oral_uses) AS traditional_use_count,

  // Ayurvedic formulation integration
  relevant_formulations,
  size(relevant_formulations) AS formulation_count,

  // Composite ranking score (higher = more promising)
  // Weights: breast cancer (3), OM gene overlap (2 per gene),
  //          ayurvedic bridge (1 per path), traditional use (2 per use),
  //          formulation (1 per formulation)
  (CASE WHEN has_breast_cancer_indication THEN 3 ELSE 0 END)
  + (size(all_om_gene_hits) * 2)
  + size(ayurvedic_bridges)
  + (size(traditional_oral_uses) * 2)
  + size(relevant_formulations)
  AS composite_score

ORDER BY
  // Primary: composite score (multi-dimensional relevance)
  (CASE WHEN has_breast_cancer_indication THEN 3 ELSE 0 END)
  + (size(all_om_gene_hits) * 2)
  + size(ayurvedic_bridges)
  + (size(traditional_oral_uses) * 2)
  + size(relevant_formulations)
  DESC,
  // Secondary: LogP ascending (better mucosal delivery first)
  candidate.alogp ASC
```

### How to Read the Results

The query returns one row per candidate drug, scored across five dimensions:

| Column | Description |
|--------|-------------|
| `drug_name`, `chembl_id` | Drug identification |
| `MW`, `LogP`, `PSA`, `HBD`, `HBA` | Physicochemical fingerprint (all within optimal range) |
| `has_breast_cancer_indication` | `true` if the drug is already indicated for breast cancer |
| `all_indications` | Complete list of the drug's current therapeutic indications |
| `mechanisms` | ChemBL mechanism(s) of action with target details |
| `om_biomarker_gene_overlap` | DisGeNET OM genes that this drug's targets map to |
| `ayurvedic_bridges` | Plant-compound-target paths linking to Ayurvedic medicine |
| `traditional_oral_uses` | Bridging plants with ethnobotanical oral/mucosal uses |
| `relevant_formulations` | Known Ayurvedic formulations containing bridging plants |
| `composite_score` | Weighted multi-criteria ranking score |

**Composite Score Weights:**
- Breast cancer indication: +3 points (dual-purpose value)
- OM biomarker gene overlap: +2 per gene (mechanistic rationale)
- Ayurvedic bridge: +1 per plant-compound-target path (traditional medicine connection)
- Traditional oral use: +2 per validated ethnobotanical use (strongest form of Ayurvedic evidence)
- Formulation integration: +1 per existing Ayurvedic formulation (practical advancement)

### APOC Dependency Note

This query uses `apoc.coll.union()` to merge gene hit lists from two different traversal paths. Ensure the APOC plugin is installed (see `scripts/cypher_scripts/apoc.conf`). If APOC is unavailable, replace:

```cypher
apoc.coll.union(direct_om_gene_hits, collect(DISTINCT g2.name)) AS all_om_gene_hits
```

with the following pure-Cypher alternative (collects both lists separately and deduplicates in the RETURN):

```cypher
collect(DISTINCT g2.name) AS mech_om_gene_hits
// Then in RETURN, use:
// [x IN direct_om_gene_hits + mech_om_gene_hits WHERE x IS NOT NULL | x] AS all_om_gene_hits
```

---

## Appendix A: Data Quality Notes

- **Drugs Analyzed:** 3,274 ChemBL approved drugs
- **Indications:** 2,328 unique indications (after splitting semicolon-separated values)
- **OM Candidates Identified:** 131 drugs matching mucosal delivery fingerprint
- **Breast Cancer Intersection:** 11 drugs with both fingerprint match and breast cancer indication
- **DisGeNET Biomarkers:** 51 gene-disease associations for stomatitis/OM
- **Mechanism/Target Data:** Currently limited (test data) — full scrape recommended for complete target overlap analysis
- **Natural Products:** 1,744 drugs flagged as natural products (53% of dataset)
- **IMPPAT Plants:** 13 plants with detailed phytochemical and therapeutic use data imported
- **TTD OM Drugs:** 4 drugs with direct Oral Mucositis indication

## Appendix B: Data Source Descriptions

| Source | Description | Records Used |
|--------|-------------|-------------|
| **ChemBL** | Approved drug physicochemical properties, indications, mechanisms, warnings | 3,274 drugs |
| **DisGeNET** | Gene-disease associations (biomarkers, genetic variants, altered expression) | 51 OM associations |
| **TTD** | Therapeutic Target Database — curated drug-target-disease relationships | 4 OM drugs |
| **IMPPAT** | Indian Medicinal Plants, Phytochemistry And Therapeutics | 13 plants |
| **PubChem** | Chemical-gene and chemical-protein interactions | Phytochemical targets |
| **DrugBank** | Drug-target interactions with protein/gene identifiers | Drug targets |
| **MedPlantDB** | BSI medicinal plant database with therapeutic uses | Plant uses |

---

*Analysis performed using OSPF Ayurveda Knowledge Graph*
*Neo4j database: ospf-ayurveda-kg*
