# Data Inventory — Diabetic Retinopathy (BLINDED RUN)
Generated: 2026-10-05 · Supersedes the earlier inventory in this directory (see Correction)

**Pipeline input directory: `data/processed-blinded-diabetic-retinopathy/`**
Do NOT read `data/processed/chembl_approved_drugs.csv` or
`data/holdout/diabetic-retinopathy/` — these hold the un-blinded answer key.

## Correction to the previous inventory

The earlier version of this file reported "ChemBL Drug Indications — Hits for DR: 0" and
concluded no DR indication data existed in the project. That was wrong. It grepped only
`chembl_drug_indications.csv` (80 rows, genuinely 0 DR hits) and missed
`chembl_approved_drugs.csv` (3,276 rows), where 44 drugs carry retinopathy/macular-edema
terms in the free-text `indication_class` and `therapeutic_areas` columns — including
both PPARα agonists in the dataset. Those 44 are the holdout target and are now redacted.

## File-by-file

| File | Rows | Status for this run |
|---|---|---|
| `chembl_approved_drugs.csv` | 3,276 | **REDACTED** — 154 cells across 79 drugs. Structures, properties, non-ocular indications intact |
| `pubchem_phytochem_target_interactions.csv` | 60,521 | Untouched — primary evidence source |
| `pubchem-target-interactions/..._human_only.csv` | subset | Untouched — human-only interactions |
| `chembl_drug_targets.csv` | 44 | Untouched but **thin**; 0 PPAR entries |
| `chembl_drug_mechanisms.csv` | 11 | Untouched but **near-empty test extract**; 0 PPAR entries |
| `chembl_drug_indications.csv` | 80 | Untouched; 0 DR rows before or after blinding |
| `disgenet__OM_*.csv` | — | Oral Mucositis only. **No DR gene-disease data** |
| `imppat_*` | 13 plants | Plant/phytochemical context. Only **6 of 13** carry eye or diabetes uses (not 8 — see findings §7); 4 have zero use records |
| `medicinal_plants_with_uses.csv` | 1,915 | **99.6% is the literal string "UNKNOWN USE".** Only 8 real rows, none mentioning eye, vision or diabetes. Effectively empty — see findings §6 |

**Implication:** ChEMBL mechanism and target tables are too thin to support target-level
drug reasoning. PubChem chemical-target interactions carry this analysis.

## PPARα (PPARA) evidence available — the requested focus

143 PPARA interaction rows in PubChem; 39 unique compounds. Direct binders/activators
with evidence strings stating binding or increased activity:

| Compound | Evidence in data | Sources |
|---|---|---|
| Alpha-linolenic acid | binds to and increases activity of PPARA | CTD, DrugBank, T3DB |
| Stearic acid | binds to and increases activity of PPARA | CTD, DrugBank, T3DB |
| Octanoic acid | binds to and increases activity of PPARA | CTD, DrugBank |
| Lauric acid | binds to PPARA | CTD, DrugBank, T3DB |
| Myristic acid | binds to PPARA | CTD, DGIdb, DrugBank, T3DB |
| Oleic / linoleic / palmitic acid | activity and expression modulation | CTD, DGIdb, T3DB |
| Isoflavone | Agonist | DrugBank |
| Geraniol, citronellol, nonanoic acid | increases activity of PPARA | CTD |
| Prasterone (DHEA) | Activator | CTD, DrugBank |
| Nicotinic acid | increases PPARA mRNA and protein | CTD |
| Quercetin, rutin, naringenin, myricetin, apigenin, catechin | protect PPARA expression against metabolic/toxic insult | CTD |
| Gedunin | decreases PPARA activity (negative modulator) | CTD |

PPARα-class approved drugs visible in the blinded file (indications blinded, chemistry intact):
fenofibrate, fenofibric acid, choline fenofibrate, pemafibrate, ciprofibrate, clofibrate,
gemfibrozil, elafibranor; PPARγ comparators pioglitazone, rosiglitazone, troglitazone.

## DR-relevant target coverage in PubChem (interaction row counts)

TNF 724 · CASP3 594 · CAT 511 · IL1B 425 · IL6 411 · BCL2 362 · BAX 345 · NFE2L2 250 ·
PPARG 196 · **PPARA 143** · TGFB1 141 · MMP9 116 · SOD2 115 · VEGFA 102 · HIF1A 85 ·
NFKB1 85 · NOS3 84 · ICAM1 76 · SERPINE1 40 · EDN1 39 · AKR1B1 38 · PPARD 31 ·
SLC2A1 31 · AGER 23 · KDR 18 · PRKCB 16 · ANGPT2 1

## Compounds hitting PPARA plus the widest DR-target set

> **CORRECTION (added after Phase 1).** The table below is retained for provenance but
> **must not be read as polypharmacology**. A random set of 20 compounds covers >=26 of
> these 27 genes with probability 0.58; catalogue size correlates with hit count at
> r = 0.911; ascorbic acid alone covers 23 of 27. The ranking measures study effort in
> the Comparative Toxicogenomics Database, not breadth of action. See
> `data-quality-findings.md` §8.

| Compound | DR targets hit | Notable |
|---|---|---|
| Quercetin | 26 | PPARA+PPARG+PPARD, VEGFA, KDR, AKR1B1, AGER, PRKCB |
| Apigenin | 21 | all three PPARs, VEGFA, KDR, AKR1B1 |
| Rutin | 19 | PPARA/G/D, VEGFA, PRKCB, AGER |
| Melatonin | 19 | PPARA, VEGFA, KDR, HIF1A |
| Naringenin | 18 | PPARA/G, VEGFA, PRKCB, SERPINE1 |
| Geraniol | 18 | PPARA activator, VEGFA, KDR |
| Nicotinic acid | 16 | PPARA/G, ANGPT2 (only compound hitting ANGPT2), VEGFA, KDR |
| Tetramethylpyrazine | 15 | PPARA/G, VEGFA, HIF1A, EDN1 |
| Alpha-linolenic acid | 8 | direct PPARA agonist |

## Gaps

1. No DisGeNET gene-disease data for DR — gene associations are knowledge-based.
2. ChEMBL mechanism/target tables effectively empty; drug-target links for approved drugs
   must come from PubChem or training knowledge.
3. No retinal-tissue pharmacokinetic data anywhere in the project.
4. PubChem evidence is largely CTD expression-level associations, not binding affinities.
   "Results in increased expression of PPARA mRNA" is weak evidence of target engagement.
