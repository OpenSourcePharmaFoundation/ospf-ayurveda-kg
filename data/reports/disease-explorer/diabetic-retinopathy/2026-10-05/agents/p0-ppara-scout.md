# P0 — PPARα Candidate Scout: Diabetic Retinopathy

**Agent:** PPARα Candidate Scout
**Date:** 2026-10-05
**Run mode:** BLINDED BENCHMARK (holdout protocol active)
**Data root:** `data/processed-blinded-diabetic-retinopathy/` only
**Deliverable:** candidate set for downstream ranking, Groups A–D

---

## 0. Blinding posture and data provenance

Every project-data fact below comes from `data/processed-blinded-diabetic-retinopathy/`. I did not open
`data/processed/chembl_approved_drugs.csv`, anything under `data/holdout/`, any `answer-key*` file, or git
history. No candidate is justified here by its DR or DME indication, approval, or trial record. Full
compliance statement in §8.

### 0.1 Data-quality findings that constrain this analysis

Three problems materially limit what the project data can support, and the downstream ranker should know
about all three:

**(a) The curated target/mechanism tables are Oral-Mucositis legacy files and contain no PPAR data.**

| File | Rows | PPAR content | Disease scope |
|---|---:|---|---|
| `chembl_drug_mechanisms.csv` | 11 | none | antibiotics, nicotine, indomethacin, amphetamine |
| `chembl_drug_targets.csv` | 44 | none | bacterial organisms, adrenergic/cholinergic receptors |
| `ttd_drug_target_genes.csv` | 5 | none | Oral mucositis only (palifermin, Hebervis, AG-013) |
| `drugbank_drug_targets.csv` | ~18 | none | chlorhexidine, palifermin, diphenhydramine |
| `disgenet__OM_*.csv` | 3 files | n/a | **Oral Mucositis gene–disease associations, not DR** |

Consequence: there is **no curated drug→PPARα mechanism edge anywhere in the project data**. The entire
PPARα evidence base available to me is (i) structural/physicochemical rows in the blinded approved-drugs
table and (ii) the CTD-dominated `pubchem_phytochem_target_interactions.csv`. The DisGeNET gene–disease
files are for Oral Mucositis and are **not usable** for DR target prioritisation; the DR gene panel used
in Group C is supplied by the task brief, not derived from project data.

**(b) `chembl_drug_metabolism.csv` has a broken join.** The `drug_name` column is index-misaligned against
`drug_chembl_id`. Example row: `drug_chembl_id=CHEMBL672`, `drug_name=PRAZOSIN`,
`substrate_name=FENOFIBRATE`, `metabolite_name=FENOFIBRIC ACID`. The same three genuine fenofibrate
metabolism facts are replicated across ten wrong `drug_name` values, inflating 3 facts into 30 rows. The
`chembl_id`, `substrate_*`, `metabolite_*`, `enzyme_name`, `met_conversion` and `met_comment` columns are
internally consistent and usable; **`drug_name` in this file must be ignored.** Any downstream agent
counting rows in this file will overcount by ~10×.

**(c) `chembl_natural_products.csv` is 26 rows and is also mis-joined** (PRAZOSIN is listed with
`natural_product=1`). Unusable for natural-product scouting.

**(d) Coverage gap:** **bezafibrate** — the pan-PPAR fibrate — is absent from the blinded approved-drugs
table (3,276 rows) despite appearing repeatedly inside CTD action strings in the PubChem file as a
reference PPARα agonist. This is a dataset gap, not evidence of anything about bezafibrate.

**(e)** Six `[REDACTED-HOLDOUT]` tokens occur across three rows of the approved-drugs file. I did not
determine which drugs those rows belong to. Identifying the redacted rows would invert the blind and
recover the answer key, so I deliberately stopped. None of the candidates I characterised below showed a
redacted value in any field I printed.

---

## 1. GROUP A — Direct PPARα agonists (approved drugs)

### 1.1 Raw mine

Pattern `fibrate|glitazar|glitazone|fibranor|fibrozil|fibric` over `pref_name` + `synonyms` returned
**13 hits** from 3,276 rows. A second sweep for `bezafibrate|saroglitazar|lanifibranor|seladelpar|
aleglitazar|muraglitazar|tesaglitazar|chiglitazar|pirinixic|lobeglitazone|…` added **seladelpar** (and its
lysine salt), which the first pattern missed.

| ChEMBL | Name | MW | aLogP | PSA | HBA | HBD | RTB | Ro5v | QED | Approval | Withdrawn |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| CHEMBL672 | **Fenofibrate** | 360.84 | 4.68 | 52.60 | 4 | 0 | 6 | 0 | 0.55 | 1993 | no |
| CHEMBL981 | **Fenofibric acid** | 318.76 | 3.81 | 63.60 | 3 | 1 | 5 | 0 | 0.85 | 2008 | no |
| CHEMBL1201745 | **Choline fenofibrate** | 318.76* | 3.81 | 63.60 | 3 | 1 | 5 | 0 | 0.85 | 2008 | no |
| CHEMBL247951 | **Pemafibrate** | 490.56 | 5.55 | 94.26 | 7 | 1 | 13 | 1 | 0.24 | 2017 | no |
| CHEMBL457 | **Gemfibrozil** | 250.34 | 3.57 | 46.53 | 2 | 1 | 6 | 0 | 0.78 | 1981 | no |
| CHEMBL557555 | **Ciprofibrate** | 289.16 | 3.59 | 46.53 | 2 | 1 | 4 | 0 | 0.86 | 1985 | no |
| CHEMBL565 | **Clofibrate** | 242.70 | 3.06 | 35.53 | 3 | 0 | 4 | 0 | 0.76 | 1967 | **yes** |
| CHEMBL3707395 | **Elafibranor** | 384.50 | 5.16 | 63.60 | 4 | 1 | 7 | 1 | 0.41 | 2024 | no |
| CHEMBL230158 | **Seladelpar** | 444.47 | 5.05 | — | — | — | — | — | — | 2024 | no |
| CHEMBL595 | Pioglitazone | 356.45 | 3.16 | 68.29 | 5 | 1 | 7 | 0 | 0.83 | 1999 | no |
| CHEMBL121 | Rosiglitazone | 357.44 | 2.49 | 71.53 | 6 | 1 | 7 | 0 | 0.82 | 1999 | **yes** |
| CHEMBL408 | Troglitazone | 441.55 | 4.37 | 84.86 | 6 | 2 | 5 | 0 | 0.72 | 1997 | **yes** |

\* the table reports parent-acid properties for the choline salt.

`oral_bioavailability = True` for all of the above. `bioavailability_score`, `logd`, `cx_logp`, `cx_logd`,
`permeability` and `molecular_species` are **empty for every row** in this file — so the dataset cannot
speak to ionisation state or measured permeability, and those judgements below are mine from structure.

### 1.2 Per-compound characterisation

Potency and selectivity figures below are general pharmacology knowledge, not project data, and are
labelled as such. None of them is DR-specific.

---

**FENOFIBRATE (CHEMBL672) — prodrug of the active moiety**

- *Class / selectivity:* fibric-acid derivative. Its acid metabolite is PPARα-preferring but only modestly
  so — roughly an order of magnitude over PPARγ, which is weak selectivity by modern standards. No
  meaningful PPARδ activity.
- *Potency class:* **weak**. Low-micromolar-to-tens-of-micromolar EC50 in PPARα transactivation. This is
  the single most consequential number in this report (see §6).
- *Prodrug status:* **yes, obligate.** Isopropyl ester, pharmacologically inert at PPARα until hydrolysed.
- *Active metabolite:* **fenofibric acid**, confirmed in project data —
  `chembl_drug_metabolism.csv`: `FENOFIBRATE → FENOFIBRIC ACID`, enzyme `Esterases`, conversion
  `De-esterification`, `Organ: Liver`, comment *"Fenofibrate is more or less completely converted into
  this metabolite"*. A second project-data row gives `FENOFIBRIC ACID → REDUCED FENOFIBRIC ACID`
  (*"A minor metabolite, but has similar activity to fenofibric acid"*), then
  `→ REDUCED FENOFIBRIC ACID GLUCURONIDE` (*"found in the urine"*).
- *Physicochemistry:* aLogP 4.68, PSA 52.6, HBD 0 — very lipophilic, essentially water-insoluble. QED 0.55
  is the worst of the classical fibrates, driven by the lipophilicity.
- *Oral bioavailability:* dissolution-limited with a large positive food effect; the reason micronised and
  nanocrystal formulations exist. Absorption is the formulation problem, not the permeability problem.
- *Elimination:* hepatic glucuronidation, **renal excretion of conjugates**.
- *Retinal exposure plausibility:* **the parent never matters** — it is fully converted presystemically.
  Judge the acid.

---

**FENOFIBRIC ACID (CHEMBL981) / CHOLINE FENOFIBRATE (CHEMBL1201745) — the active species**

- *Class / selectivity:* PPARα-preferring, modest isoform margin over PPARγ.
- *Potency class:* **weak** (tens of µM EC50).
- *Prodrug status:* none — this *is* the active moiety. Choline fenofibrate is a delayed-release salt that
  removes the food effect; identical pharmacology.
- *Physicochemistry:* MW 318.76, aLogP 3.81, PSA 63.6, HBD 1, Ro5 violations 0, **QED 0.85 — the best
  drug-likeness score of any PPARα agent in the file.** Carboxylic acid, pKa ≈ 3, therefore **>99.9%
  anionic at pH 7.4**.
- *Protein binding:* ~99% albumin-bound (knowledge, not in dataset). Free fraction ≈ 1%.
- *Half-life:* ~20 h, supports once-daily dosing.
- *Elimination:* **predominantly renal**, as the acyl glucuronide — the project metabolism data confirms
  the urinary glucuronide route. Accumulates as eGFR falls; requires dose reduction in moderate CKD and is
  contraindicated in severe CKD.
- *Retinal exposure plausibility:* **poor on first principles.** PPARα is an intracellular nuclear
  receptor, so the drug must cross a plasma membrane; a permanently ionised carboxylate with ~1% free
  fraction is a bad passive permeant. The liver escapes this because OATP1B1/1B3 actively concentrate
  fibrate anions hepatically — **the retina has no equivalent uptake system**, and organic-anion
  transporters at the inner BRB and RPE run in the *efflux* direction for this chemotype. The honest
  caveat on the other side: in diabetes the blood–retinal barrier is leaky, so retinal exposure will be
  higher than in healthy eye — but that makes the drug arrive only once the barrier is already damaged.

---

**PEMAFIBRATE (CHEMBL247951) — the cleanest pharmacological probe**

- *Class / selectivity:* a **SPPARMα** (selective PPARα modulator), not a classical fibrate. The
  benzoxazole + 2-aryloxy-butanoic acid architecture visible in the SMILES
  (`CC[C@@H](Oc1cccc(CN(CCCOc2ccc(OC)cc2)c2nc3ccccc3o2)c1)C(=O)O`) makes a Y-shaped ligand that fills the
  PPARα Y-cavity and recruits a distinct coactivator set.
- *Potency class:* **sub-nanomolar** EC50 at human PPARα — roughly four orders of magnitude more potent
  than fenofibric acid — with >2,000-fold selectivity over PPARγ and PPARδ. **If the pipeline wants to
  test "is PPARα agonism sufficient?", this is the molecule that actually asks the question.**
- *Prodrug status:* none. Single stereocentre, (R)-configured; the active enantiomer is dosed.
- *Physicochemistry:* MW 490.56, aLogP 5.55, PSA 94.26, **RTB 13**, **Ro5 violations 1**, **QED 0.24** —
  by far the worst drug-likeness profile in the group. High rotatable-bond count and high lipophilicity.
- *Protein binding:* >99.8% (knowledge). Free fraction ≈ 0.2%, an order of magnitude *lower* than
  fenofibric acid.
- *Elimination:* **hepatic** — CYP2C8/CYP2C9 oxidation plus glucuronidation, then **biliary/faecal**
  excretion. Negligible renal clearance.
- *Retinal exposure plausibility:* **the worst in the group, by design.** Pemafibrate was deliberately
  engineered as an OATP1B1/1B3 substrate for hepatoselective uptake — the whole point is to concentrate
  drug in liver and minimise systemic/extrahepatic exposure. That is precisely the wrong property for a
  retinal target. Its sub-nM potency partly offsets its 0.2% free fraction (free concentration lands
  perhaps 10–30× below EC50 rather than fenofibric acid's ~100×), but hepatic sequestration works against
  it. **Best engagement, best renal safety, worst tissue targeting.**

---

**GEMFIBROZIL (CHEMBL457) — carry as a cautionary comparator only**

- *Selectivity / potency:* **very weak** PPARα agonist, high-micromolar; much of its lipid effect is
  arguably not PPARα-mediated at all.
- *Physicochemistry:* MW 250.34, QED 0.78, PSA 46.53 — small and tidy, but potency is the problem.
- *Elimination:* glucuronidation, renal.
- *Disqualifying liability:* gemfibrozil glucuronide is a **potent mechanism-based inactivator of CYP2C8**
  and an OATP1B1 inhibitor, producing large statin exposure increases and a well-documented rhabdomyolysis
  risk. In a population that is almost universally statin-treated, this is a hard exclusion.
- **Recommendation: exclude from the ranked set; keep as a negative control for "fibrate ≠ PPARα agonist".**

---

**CIPROFIBRATE (CHEMBL557555)** — QED 0.86 (best in file), MW 289, Ro5 0. Weak agonist, very long
half-life (~80 h) causing accumulation, limited geographic availability. No advantage over fenofibric acid.
**Exclude.**

**CLOFIBRATE (CHEMBL565)** — `withdrawn_flag = True` in the project data. Ethyl ester prodrug of clofibric
acid; the first-generation fibrate, abandoned after an excess-mortality signal. Mechanistically a genuine
PPARα agonist (CTD rows in the PubChem file use it as a reference agonist, and gedunin's antagonism of
clofibrate's PPARα activation is one of the better pharmacological controls in that file). **Exclude as a
candidate; useful as a historical safety anchor.**

---

**ELAFIBRANOR (CHEMBL3707395) — dual PPARα/δ**

- MW 384.50, aLogP 5.16, Ro5v 1, QED 0.41, first approval 2024.
- *Selectivity:* **PPARα/δ dual agonist**, low-nanomolar at both; minimal PPARγ. Has an active metabolite
  (the alcohol reduction product) with comparable activity.
- *Why carry it:* if PPARα alone is insufficient, PPARδ adds fatty-acid oxidation in muscle and endothelium
  and has its own anti-inflammatory programme. Dual agonism is a real mechanistic variant worth ranking
  separately rather than collapsing into "fibrate".
- Chalcone-like enone (`C(=O)/C=C/`) is a mild electrophile / Michael acceptor — a covalent-reactivity flag
  the ADMET agent should look at.

**SELADELPAR (CHEMBL230158) — PPARδ-selective: carry as the isoform control**

- MW 444.47, aLogP 5.05, approval 2024. Highly PPARδ-selective.
- *Why carry it:* it is the **falsification arm**. If a PPARδ-selective agent scores as well as or better
  than a PPARα-selective agent on DR-relevant mechanism, then the user's PPARα-specific hypothesis is not
  what is doing the work. Including it is what makes the ranking informative rather than self-confirming.

**PIOGLITAZONE / ROSIGLITAZONE / TROGLITAZONE** — PPARγ thiazolidinediones, not PPARα agents.
Pioglitazone has weak ancillary PPARα activity; rosiglitazone and troglitazone are flagged
`withdrawn_flag = True` in the project data. Pioglitazone also carries a fluid-retention/oedema liability
that is specifically unattractive in a retinal-oedema context, independent of any DR knowledge. **Carry
pioglitazone as the PPARγ isoform control only; exclude the two withdrawn agents.**

Note on `therapeutic_areas` breadth: pioglitazone lists ~70 areas and rosiglitazone ~35. These fields are
aggregated from *any* registered trial, not approved labels, so they are indicators of research attention,
not of established efficacy. The ranker should not treat a long `therapeutic_areas` string as evidence.

---

## 2. GROUP B — PPARα-interacting natural products and endogenous ligands (project data)

Query returned **143 PPARA rows** from `pubchem_phytochem_target_interactions.csv`. Source composition is
overwhelmingly **Comparative Toxicogenomics Database**, with a handful of DrugBank, T3DB and DGIdb rows.

**The structural point that governs this whole section:** CTD action strings are *literature-curated
statements about experiments*, and the overwhelming majority of the PPARA rows describe **changes in PPARA
expression**, not engagement of the PPARα protein by the compound. A string of the form
`X inhibits the reaction [insult results in decreased expression of PPARA protein]` says only that an
insult lowered PPARA levels and X blunted the insult. That is compatible with X having no affinity for
PPARα whatsoever. I have graded strictly on this basis.

### 2.1 Evidence grading

**STRONG — direct binding and demonstrated receptor activation, multiple independent reports**

| Compound | Evidence | PMIDs | Caveat |
|---|---|---|---|
| **Linoleic acid** (18:2 ω-6) | `binds to and results in increased activity of PPARA`; plus `promotes the reaction [PPARA binds to NCOA2 / NCOA1]` and `affects [PPARA binds to CREBBP]` | 10403814, 15491415, 16731579, 19263263, 23843199, 35752307 | Coactivator-recruitment rows are a genuine mechanistic readout of agonism, not just expression. **Also binds and activates PPARG** — non-selective. |
| **Oleic acid** (18:1 ω-9) | `binds to and results in increased activity of PPARA` | 10403814, 15491415, 16731579, 35752307 | Also binds/activates PPARG. 19 of 27 DR-panel genes but only 3 with action strings. |
| **α-Linolenic acid** (18:3 ω-3) | `binds to and results in increased activity of PPARA` | 10403814, 16731579, 19667161 | Also activates PPARG. |

These three are the only compounds in the entire PPARA set with replicated, independent, binding-plus-
activation evidence. **All three are endogenous dietary fatty acids with micromolar affinity and no isoform
selectivity.** They establish that PPARα is a bona fide fatty-acid sensor — which is the mechanistic
foundation for §5 — but none of them is a drug candidate in its own right.

**Saturated fatty acids — strong-*looking*, but one primary source**

Lauric (C12), myristic (C14), palmitic (C16), stearic (C18) and octanoic (C8) acids all carry
`binds to PPARA protein` or `binds to and results in increased activity`. **Every one of these traces to
PMID 10403814** — a single fatty-acid/PPAR binding panel. The apparent corroboration across CTD, DrugBank
and T3DB rows is **database redundancy re-citing the same paper**, not independent replication. Octanoic
acid is the only one with a second source (16731579, 35752307). Downstream agents must not count these as
multiple lines of evidence. Palmitic acid is additionally confounded: it appears 21 times as an
*experimental lipotoxic insult* in the same file, with rows going in both directions.

**MODERATE — functional activation, limited replication**

| Compound | Evidence | PMID | Assessment |
|---|---|---|---|
| **Linalool** | `binds to and results in increased activity of PPARA`; **plus `PPARA gene mutant form results in decreased susceptibility to linalool`** and PPARα-dependent SLC27A4 induction | 24752549 | The genetic-dependency row is unusually good evidence — a receptor-mutant phenotype is much harder to explain away than an expression change. Single report, so moderate not strong. |
| **Geraniol** | `results in increased activity of PPARA protein` | 21597168 | Activation without demonstrated binding. |
| **Citronellol** | `results in increased activity of PPARA protein` | 21597168 | Same paper as geraniol — one source, two monoterpenes. |
| **Nonanoic (pelargonic) acid** | `results in increased activity of PPARA protein` | 23391484 | Medium-chain FA, consistent with the FA-sensor story. |
| **Prasterone (DHEA)** | DrugBank `Activator`; CTD mechanism is `[DHEA → increased PPP2CA] → decreased phosphorylation of PPARA` | 18079279, 17591676 | **Indirect** — post-translational modulation via a phosphatase, not ligand binding. Downgrade from the DrugBank label. |
| **Isoflavone** | DrugBank `Agonist` | 12730403 | **"Isoflavone" is a chemical class, not a compound** — a curation defect. The same row also lists PPARG `Agonist`, so even taken at face value it is non-selective. Low information. |

**WEAK — "protects PPARA expression against an insult" / co-treatment inference**

This is the largest category and it contains most of the famous phytochemicals.

- **Quercetin (7 PPARA rows).** Every row is of the form `quercetin inhibits the reaction [streptozocin /
  glucose / dietary fats / fructose / methionine-choline deficiency results in decreased expression of
  PPARA]`. None is engagement. **And the direction of effect is internally incoherent:** PMID 18393431
  reads `Quercetin inhibits the reaction [GW 7647 results in increased activity of PPARA protein]` —
  i.e. quercetin *antagonises* a reference PPARα agonist. A compound cannot be scored as a PPARα activator
  on this record.
- **Naringenin, melatonin, rutin, apigenin, myricetin, catechin (cianidanol), scopoletin,
  tetramethylpyrazine, butyric acid** — all identical "blunts an insult-induced fall in PPARA expression"
  constructions. No engagement evidence.
- **Nicotinic acid (niacin)** — `results in increased expression of PPARA mRNA/protein` (18602814,
  24767308, 19878707). Expression induction only, and niacin's actual receptor is HCAR2/GPR109A. Weak for
  PPARα specifically.

**WRONG-DIRECTION — these *reduce* PPARα and should never be scored as agonists**

- **Oleanolic acid** — `results in decreased expression of PPARA mRNA` (23948738).
- **β-Carotene** — `results in decreased expression of PPARA mRNA` (21569430).
- **Methoxsalen** — decreased PPARA mRNA and protein (28552422).
- **Gedunin** — `results in decreased activity of PPARA protein` and
  `inhibits [clofibrate results in increased activity of PPARA]` (18812576). **Gedunin is a PPARα
  antagonist in this dataset.** Genuinely useful as a negative control.

**MIS-CLASSIFIED — PPARα is the actor, not the target**

- **Phytol** — `PPARA protein affects the metabolism of phytol`. The receptor acts on the compound.
- **Retinol** — `Vitamin A affects the reaction [PPARA protein binds to PCK1 promoter]`. Promoter-occupancy
  modulation, not receptor binding.
- **Cholesterol** — most rows are cholesterol appearing *inside* someone else's mechanism string
  (e.g. `[pirinixic acid binds to and results in increased activity of PPARA] inhibits [IL1B → decreased
  transport of cholesterol]`). Cholesterol is the *readout*, not the ligand.

**NOT COMPOUNDS AT ALL — curation artefacts in a "phytochemical" table**

**D-fructose (6 PPARA rows), sucrose (7), beta-D-glucopyranose, D-galactose** are **experimental
perturbagens** — dietary insults used to induce metabolic disease in rodents. Their presence in a table
named `pubchem_phytochem_target_interactions` is a curation defect. D-fructose scores 21/27 DR-panel genes
with **zero** action-type rows. **Any ranking that lets fructose or sucrose surface as a candidate has a
bug, not a finding.**

**VERY WEAK — DGIdb rows with no action string**

Myristic acid, linoleic acid, oleic acid each have a bare DGIdb row with empty `action` and empty
`evidences`. Zero information content. Treat as absent.

**TOXICANTS with the cleanest pharmacology in the file — note the irony**

**Dibutyl phthalate** has `binds to PPARA protein` (23843199), `results in increased activity of PPARA`
(25291543), and — critically — **two rows where the PPARα antagonist GW 6471 reverses the effect**
(33508418, 25291543). Antagonist-reversal is the best pharmacological control present anywhere in these
143 rows. Dibutyl phthalate is also a plasticiser and reproductive toxicant. The fact that the
best-controlled PPARα activation evidence in this dataset belongs to a phthalate is a direct consequence of
CTD being a **toxicology** resource: it is rich in environmental chemicals and poor in therapeutics. The
downstream ranker should internalise that this file is not a drug-discovery database.

### 2.2 What Group B actually contributes

Honest summary: **the project's natural-product data contains no credible, selective, drug-like PPARα
agonist.** What it does contain is solid, replicated evidence that **long-chain unsaturated fatty acids are
genuine PPARα ligands**. That matters, because it means the druggable version of this finding is an
approved omega-3 fatty acid product rather than a phytochemical — which is why I promote
**icosapent ethyl (CHEMBL2095209, EPA ethyl ester, approved 2012, MW 330.51, aLogP 6.47, PSA 26.30,
Ro5v 1, oral)** into the candidate set as the druggable member of this ligand class. It is an ester
prodrug hydrolysed to EPA, chemically continuous with the linoleic/linolenic acid evidence above, and is
the only way the Group B finding reaches a dosable product.

---

## 3. GROUP C — PPARα-adjacent multi-target candidates

### 3.1 The promiscuity correction

Raw DR-panel breadth (top 18), with a **breadth-of-action** correction — targets backed by a
binding/agonist/inhibitor action string, versus targets backed by any row at all:

| Compound | CTD rows | Targets (study) | Targets (action) | Action ratio |
|---|---:|---:|---:|---:|
| Quercetin | 745 | 26 | 9 | 0.35 |
| Genistein | 162 | 23 | 3 | 0.13 |
| Ascorbic Acid | 209 | 23 | 4 | 0.17 |
| Dibutyl Phthalate | 118 | 22 | 2 | 0.09 |
| D-Fructose | 123 | 21 | **0** | 0.00 |
| Apigenin | 109 | 21 | 4 | 0.19 |
| Palmitic Acid | 180 | 21 | 1 | 0.05 |
| Kaempferol | 81 | 20 | 5 | 0.25 |
| Alpha-Tocopherol | 129 | 19 | 1 | 0.05 |
| Melatonin | 249 | 19 | 3 | 0.16 |
| Rutin | 100 | 19 | 1 | 0.05 |
| Oleic Acid | 93 | 19 | 3 | 0.16 |
| Luteolin | 112 | 19 | 1 | 0.05 |
| Naringenin | 55 | 18 | **0** | 0.00 |
| Linoleic Acid | 55 | 18 | 2 | 0.11 |
| Cholesterol | 60 | 18 | 6 | 0.33 |
| Geraniol | 95 | 18 | **0** | 0.00 |
| Ellagic Acid | 59 | 17 | 1 | 0.06 |

**Read this table as a warning, not a leaderboard.** Three observations:

1. **Rank correlates with study volume, not pharmacology.** Quercetin tops the list with 745 rows — more
   than the next two combined. Ascorbic acid at 23 targets and D-fructose at 21 are not
   polypharmacological drugs; they are substances that appear in an enormous number of rodent experiments.
   Vitamin C scoring above kaempferol on "target breadth" is a *bibliometric* result.
2. **The action-ratio column collapses the distribution.** Once you demand an action string, the field goes
   from 17–26 targets down to 0–9, and the spread between compounds largely disappears. Three of the top
   eighteen have an action ratio of exactly **zero**.
3. **Quercetin is a textbook assay-frequent hitter.** The catechol B-ring redox-cycles and generates H₂O₂
   in cell media, it quenches fluorescence, it forms colloidal aggregates that nonspecifically inhibit
   enzymes, and it binds ATP pockets across unrelated kinases. Its 26-target breadth is substantially a
   catalogue of the assays people ran, and its PPARA rows (§2.1) are weak and self-contradictory.

**Breadth-of-study ≠ breadth-of-action.** The ranker should use the action-ratio column, and should treat
any compound whose breadth comes from a single CTD-heavy corpus as unranked until a binding assay exists.

### 3.2 Group C carries

- **Quercetin** — carry as the canonical polypharmacology candidate **and** as the pipeline's
  frequent-hitter control. Genuine DR-relevant breadth (NFE2L2, AKR1B1, VEGFA, ICAM1, MMP9) at the best
  action ratio in the set, but a documented promiscuity profile and oral bioavailability <2% with extensive
  first-pass glucuronidation/sulfation. **Its PPARα claim does not survive scrutiny.**
- **Melatonin** — 19 DR-panel targets, 249 rows. Weak PPARA evidence (cisplatin-protection rows only), but
  it is the **only compound in the whole set with unambiguously favourable retinal access**: MW 232,
  neutral, amphipathic, crosses the BBB and BRB freely, and the retina physiologically synthesises it. It
  is the right control for "does getting into the retina matter more than target affinity?"
- **Luteolin / Apigenin** — flavones with AKR1B1 and NF-κB coverage; apigenin lacks quercetin's catechol
  and is the cleaner chemotype. Both have PPARG binding rows and **no** PPARA binding row. Carry at most
  one; I carry neither in the final 15 to stay inside the count, and note them as the first alternates.

---

## 4. GROUP D — Non-PPARα mechanistic comparators

Derived from DR pathway logic plus the blinded approved-drugs table. These exist so the ranking has a
baseline and so "PPARα wins" is a result rather than an artefact of only testing PPARα agents.

**1. EPALRESTAT (CHEMBL56337) — aldose reductase (AKR1B1) inhibition.** MW 319.41, aLogP 2.92, PSA 57.61,
Ro5v 0, `oral_bioavailability = True`, approved 1992. `therapeutic_areas` in the blinded file reads only
"Breast Neoplasms; Charcot-Marie-Tooth Disease". **Mechanism:** chronic hyperglycaemia pushes glucose
through the polyol pathway; aldose reductase converts it to sorbitol, which accumulates intracellularly in
pericytes and Müller glia, consuming NADPH, depleting glutathione, and imposing osmotic plus oxidative
stress. AKR1B1 is in the DR gene panel and is the most mechanistically specific alternative to PPARα in the
set. **Caveat:** carboxylic acid, so it shares the ionisation/protein-binding exposure problem.

**2. DIMETHYL FUMARATE (CHEMBL2107333) — NRF2 activation.** MW 144.13, aLogP −0.11, PSA 52.60, Ro5v 0,
oral, approved 2013. **Mechanism:** Michael-acceptor modification of KEAP1 cysteines releases NFE2L2,
driving the antioxidant-response-element programme (NQO1, HMOX1, GCLC, catalase). **NFE2L2 is the most
heavily represented antioxidant node in the project interaction data.** Tiny, neutral, tissue-penetrant,
with established CNS exposure in another indication; active metabolite is monomethyl fumarate. **Safety
flag:** lymphopenia and PML risk on chronic dosing. This is the direct mechanistic rival to the "PPARα acts
via Nrf2 crosstalk" limb of the hypothesis — if Nrf2 is the operative node, hit it directly.

**3. MINOCYCLINE (CHEMBL1434) — microglial deactivation / neuroprotection.** MW 457.48, aLogP 0.19,
PSA 164.63, Ro5v 0, oral, approved 1971. **Mechanism:** suppresses microglial activation, IL-1β and TNF
release, and inhibits MMP9 — addressing the neuroinflammatory arm of the neurovascular unit rather than the
vascular arm. Despite PSA 164 it is the tetracycline with real CNS penetration. **Safety flag:**
vestibular toxicity and skin/scleral pigmentation on long-term dosing — a meaningful problem for a chronic
retinal indication.

**4. CANDESARTAN CILEXETIL (CHEMBL1014) — RAS / AT1R blockade.** MW 610.67, aLogP 6.32, PSA 143.34,
**Ro5 violations 3** as the cilexetil ester, but it is an obligate ester prodrug hydrolysed during
absorption to candesartan, which is drug-like. **Mechanism:** the retina has a complete local
renin-angiotensin system; AT1R signalling in retinal pericytes and endothelium drives VEGF expression,
oxidative stress and vascular remodelling. A vascular mechanism with zero PPAR involvement — a clean
contrast. Also renoprotective, which matters in this comorbidity profile.

**5. PENTOXIFYLLINE (CHEMBL628) — haemorheology / non-selective PDE inhibition.** MW 278.31, aLogP 0.19,
PSA 78.89, Ro5v 0, oral, approved 1984. **Mechanism:** improves erythrocyte deformability and reduces blood
viscosity and fibrinogen, while lowering TNF. Targets **capillary non-perfusion** — a distinct DR-relevant
axis that none of the other candidates addresses. Excellent tolerability. Weak effect size is the obvious
risk.

**Deliberate exclusion:** I considered intravitreal corticosteroids (fluocinolone acetonide CHEMBL989,
`therapeutic_areas` includes "Retinal Diseases"; triamcinolone; dexamethasone) and anti-VEGF agents
(pegaptanib CHEMBL1201421 is present; aflibercept, ranibizumab and bevacizumab are **absent** from the
blinded table). I **excluded all of them**, because selecting them would require me to lean on
DR/DME-specific clinical knowledge that the protocol forbids — their presence in a DR candidate set is only
defensible by reference to exactly the facts I am blinded to. Flagging this as a deliberate protocol-driven
exclusion rather than an oversight.

---

## 5. The mechanistic case for PPARα in a retinal disease

### 5.1 Why the receptor is even plausible here

The retina is the most metabolically active tissue per gram in the body and the most lipid-dense.
Photoreceptor outer segments are packed with DHA and are shed and phagocytosed daily by the RPE, which
then **oxidises those lipids via fatty-acid β-oxidation** as a genuine energy source. PPARα is the master
transcriptional regulator of mitochondrial and peroxisomal FAO, and it is expressed in RPE, Müller glia and
retinal vascular endothelium. The receptor is present, and the pathway it controls is one the tissue
actually runs. That is a better starting position than most repurposing hypotheses get.

### 5.2 DR processes PPARα could plausibly touch

**(a) Lipoprotein-mediated retinal injury — the strongest limb, and it needs no retinal drug exposure.**
Once the blood–retinal barrier is compromised, plasma lipoproteins extravasate into the neural retina.
Modified — oxidised and glycated — LDL is directly cytotoxic to pericytes, Müller cells and RPE, driving ER
stress and apoptosis. PPARα agonism lowers circulating triglyceride-rich lipoproteins and remnant particles
by inducing LPL, repressing APOC3 and inducing APOA5. **This shrinks the pool of particles available to
leak, and it happens entirely in the liver and plasma.** It is the one version of the hypothesis that
survives the exposure objection in §6 intact.

**(b) Transrepression of NF-κB and leukostasis.** Ligand-bound PPARα physically interacts with p65 and
c-Jun and tethers NCoR/SMRT corepressor complexes at inflammatory promoters, suppressing IL-6, TNF, MCP-1
and **ICAM1** without requiring a PPRE. ICAM1-driven leukostasis — leukocytes adhering to and plugging
retinal capillaries, causing endothelial apoptosis and capillary dropout — is an early, mechanistically
central DR lesion. TNF, IL6, IL1B, ICAM1 and NFKB1 are all in the DR gene panel. This limb is
mechanistically coherent, but it *does* require the drug to reach retinal endothelium.

**(c) Endothelial function.** PPARα supports eNOS-dependent vasodilation (NOS3), represses endothelin-1
(EDN1), and lowers PAI-1 (SERPINE1) — all three in the panel. Relevant to the capillary non-perfusion that
precedes ischaemia-driven neovascularisation.

**(d) Nrf2 crosstalk and oxidative stress.** PPARα and NFE2L2 reciprocally induce one another, and
**catalase (CAT) is a canonical direct PPARα target gene** — CAT and SOD2 are both in the panel. Diabetic
retina is under sustained oxidative load from mitochondrial superoxide, polyol flux and AGE/RAGE (AGER)
signalling. PPARα plausibly contributes to the antioxidant arm, though indirectly.

**(e) Apoptosis and the neurovascular unit.** PPARα activation has been linked to reduced Müller-cell and
endothelial apoptosis via AMPK/SIRT1 signalling and reduced caspase-3 activation (CASP3, BAX, BCL2 in the
panel). Retinal neurodegeneration — ganglion cell loss and inner-layer thinning — begins before visible
vasculopathy in diabetes, so a neuroprotective limb is not implausible.

**(f) ANGPTL4 — and this one cuts against the hypothesis.** ANGPTL4 is a **direct PPARα target gene**. It
is also a potent, hypoxia-inducible vascular-permeability and angiogenic factor in retina, acting partly
independently of VEGF. **PPARα agonism therefore predicts increased retinal ANGPTL4** — which in ischaemic
retina is plausibly *harmful*. Any honest mechanistic case has to carry this, and I weight it heavily in
§7.

### 5.3 DR processes PPARα could NOT plausibly touch

- **Established hypoxia-driven neovascularisation.** HIF1A-driven VEGFA transcription in ischaemic retina
  is not meaningfully suppressed by PPARα agonism. Proliferative disease needs VEGF blockade or ablation of
  the ischaemic drive; a nuclear-receptor agonist will not do it.
- **Structural lesions already formed** — microaneurysms, fibrovascular proliferation, tractional membranes,
  established capillary dropout. Transcriptional reprogramming does not reverse anatomy.
- **Cells already lost.** Dead pericytes and ganglion cells do not return. PPARα has no regenerative limb.
  This frames the mechanism as prevention/slowing, not rescue.
- **Rapid resolution of centre-involving macular oedema.** Nuclear-receptor pharmacology acts on a
  transcriptional timescale of days to weeks.
- **Glycaemia itself.** PPARα is not an insulin sensitiser — that is PPARγ. Any benefit must be
  glucose-independent, which means it must be demonstrated on top of glycaemic control, not instead of it.

**Net:** the mechanism is best suited to **slowing early, inflammatory/lipid-driven, non-proliferative
progression**, and is poorly suited to anything proliferative, structural, or acute.

---

## 6. Best combination of engagement, exposure, and safety in a renally-impaired diabetic population

This is a genuine fork, and the right answer depends on which mechanism from §5 you believe.

### 6.1 The exposure arithmetic — the number that decides it

Fenofibric acid's PPARα EC50 in transactivation is in the **tens of micromolar**. At the standard 145 mg
daily dose, steady-state total plasma Cmax is roughly 10–15 µg/mL, i.e. ~30–45 µM. But ≥99% is
albumin-bound, so the **free** concentration is approximately **0.1–0.4 µM** — roughly **two orders of
magnitude below the EC50**, and that is in *plasma*, before any blood–retinal-barrier attenuation at all.
PPARα is an intracellular nuclear receptor, so the free drug additionally has to cross a plasma membrane as
a carboxylate anion at pH 7.4.

The liver is exempt from this arithmetic because OATP1B1/1B3 actively concentrate fibrate anions
hepatically, producing intracellular concentrations far above plasma. **The retina has no analogous uptake
system**, and the organic-anion transporters at the inner BRB and RPE run in the efflux direction for this
chemotype.

Pemafibrate partly escapes by potency: sub-nanomolar EC50 against a ~0.2% free fraction puts free drug
perhaps 10–30× below EC50 rather than ~100×. But it was explicitly engineered for **hepatoselectivity** via
OATP-mediated uptake, which actively suppresses the extrahepatic exposure a retinal mechanism needs.

### 6.2 Safety in this population

Renal impairment is not an edge case here — diabetic kidney disease is highly prevalent in exactly the
population that has retinopathy, and this population is also near-universally statin-treated.

| | Fenofibric acid | Pemafibrate |
|---|---|---|
| PPARα EC50 | tens of µM (weak) | sub-nM (potent) |
| Isoform selectivity | ~10× vs PPARγ | >2,000× vs γ and δ |
| Elimination | **renal**, as acyl glucuronide | **hepatic/biliary** |
| Renal impairment | accumulates; dose-reduce in moderate CKD, contraindicated in severe | no dose adjustment needed in moderate CKD |
| Creatinine effect | reversible rise; confounds eGFR monitoring | minimal |
| Statin interaction | real myopathy/rhabdomyolysis risk | low |
| Homocysteine | raises it | minimal |
| Protein binding | ~99% | >99.8% |
| Tissue targeting | non-selective | **hepatoselective by design — wrong direction** |

### 6.3 Recommendation

**If the operative mechanism is systemic lipid/lipoprotein lowering (§5.2a):** choose
**fenofibric acid or choline fenofibrate**. No retinal exposure is required, the target organ is the liver,
QED 0.85 is the best in the class, once-daily dosing, decades of chronic-use data, and it is cheap. The
renal liability is real but **manageable** with eGFR-banded dosing, avoidance in severe CKD, and
statin-interaction monitoring.

**If the operative mechanism requires retinal PPARα engagement (§5.2b–e):** choose **pemafibrate** for the
pharmacology and the renal safety — it is the only molecule in the set potent and selective enough to
actually test the hypothesis, and the only one that is comfortable in CKD. But acknowledge that its
hepatoselective design is working against the thing you want, and that a negative result with pemafibrate
would be ambiguous between "PPARα doesn't help the retina" and "the drug never got there".

**Overall single pick: pemafibrate**, on the grounds that mechanistic cleanliness and renal safety are the
two properties this pipeline most needs, and that fenofibric acid's renal elimination profile is squarely
mismatched to a population defined by concurrent nephropathy. **But the pick is conditional, and the
condition is which mechanism in §5 you believe — the ranker should be told that explicitly rather than
handed a single name.**

---

## 7. The single strongest argument AGAINST the PPARα hypothesis for DR

**Free-drug exposure at the retina is almost certainly far below the concentration required to occupy
PPARα — so if a PPARα agonist helps a retinal disease, retinal PPARα agonism is probably not the reason.**

The arithmetic in §6.1 is the core of it: ~0.1–0.4 µM free fenofibric acid against a tens-of-micromolar
EC50, measured in plasma, with a permanently anionic molecule that must still cross a membrane and a
blood–retinal barrier to reach an intracellular receptor. The liver escapes only because OATP transporters
concentrate the drug there; the retina has no such pump. The most parsimonious reading of any retinal
benefit from a fibrate is therefore that it is **systemic** — reduced circulating remnant lipoproteins and
less lipid available to extravasate through an already-leaky barrier — or **PPARα-independent off-target
pharmacology** entirely. Both of those predict that a *more potent, more selective* PPARα agonist would not
necessarily be better, which is the opposite of what a PPARα-centric ranking assumes.

Three things sharpen the objection rather than soften it:

1. **ANGPTL4 is a direct PPARα target gene** and a potent pro-permeability, pro-angiogenic factor in
   ischaemic retina. The hypothesis predicts its induction. In proliferative or ischaemic disease, PPARα
   agonism could be **net harmful** — the mechanism is not merely weak, it has a plausible wrong-sign limb.
2. **The bootstrapping problem.** Retinal exposure improves as the blood–retinal barrier fails. The drug
   therefore arrives in useful quantity precisely when the disease is advanced enough that prevention is no
   longer the goal — and §5.3 says prevention/slowing is the only thing this mechanism is suited to.
3. **The project data cannot test any of this.** There is no curated drug→PPARα mechanism edge anywhere in
   the dataset (§0.1a), and the PPARα interaction evidence that does exist is a toxicology database in
   which the best-controlled activation evidence belongs to a phthalate plasticiser (§2.1). The hypothesis
   is being evaluated against data that was never built to evaluate it.

**Operational consequence for the pipeline:** rank on *systemic lipid-lowering plausibility* and
*anti-inflammatory transrepression* as separate axes from *retinal PPARα occupancy*, and treat the
PPARδ-selective arm (seladelpar) and the retina-penetrant non-PPAR arm (melatonin) as live falsification
tests rather than filler. If seladelpar or melatonin ranks at or above pemafibrate, the PPARα-specific
hypothesis is not what is doing the work.

---

## 8. Recommended candidate set (15 compounds)

### Group A — Direct PPARα agonists, approved (5)

| # | Compound | ChEMBL | Mechanism | Evidence quality | Source | Why included |
|---|---|---|---|---|---|---|
| A1 | **Fenofibric acid** | CHEMBL981 | PPARα agonist, weak (tens of µM), ~10× vs γ | Strong class pharmacology; **no project-data mechanism edge** | Data (structure, PK) + knowledge (potency) | Active moiety of the most-used fibrate; QED 0.85 — best drug-likeness in class; the realistic clinical vehicle |
| A2 | **Fenofibrate** | CHEMBL672 | Obligate ester prodrug → A1 | Prodrug conversion **confirmed in project data** (esterases, liver, "more or less completely converted") | Data-backed | Formulation/exposure comparator against the free acid; tests whether prodrug delivery matters |
| A3 | **Pemafibrate** | CHEMBL247951 | **SPPARMα**, sub-nM, >2,000× selective | Strongest engagement case in the set | Data (structure) + knowledge (potency, PK) | The only molecule potent and selective enough to actually test the hypothesis; safest in CKD. Offset: QED 0.24, hepatoselective by design |
| A4 | **Elafibranor** | CHEMBL3707395 | PPARα/δ **dual** agonist, low-nM | Strong class pharmacology | Data + knowledge | Tests whether δ co-agonism adds value over α alone; flag the Michael-acceptor enone |
| A5 | **Seladelpar** | CHEMBL230158 | **PPARδ-selective** | Strong class pharmacology | Data + knowledge | **Isoform falsification control.** If δ ≥ α, the PPARα-specific hypothesis fails |

*Excluded from A with reasons:* **gemfibrozil** (very weak agonist + CYP2C8 mechanism-based inactivation →
statin rhabdomyolysis risk in a statin-treated population); **ciprofibrate** (no advantage, ~80 h t½
accumulation); **clofibrate** (`withdrawn_flag = True`); **rosiglitazone/troglitazone**
(`withdrawn_flag = True`, and PPARγ not α); **pioglitazone** (PPARγ — retain only as isoform control; its
fluid-retention liability is independently unattractive in a retinal-oedema context).

### Group B — PPARα natural products and endogenous ligands (4)

| # | Compound | Mechanism | Evidence quality | Source | Why included |
|---|---|---|---|---|---|
| B1 | **Linoleic acid** | Endogenous PPARα ligand; binds + activates; recruits NCOA1/NCOA2/CREBBP | **STRONG** — only compound in 143 rows with binding + activation + coactivator recruitment across ≥4 independent PMIDs | Data-backed | Establishes PPARα as a genuine fatty-acid sensor; the mechanistic anchor for the whole hypothesis. **Non-selective (also activates PPARγ); not itself a drug** |
| B2 | **α-Linolenic acid** | Endogenous ω-3 PPARα ligand; binds + activates | **STRONG** (10403814, 16731579, 19667161) | Data-backed | ω-3 member of the same ligand class; bridges B1 to B4 |
| B3 | **Linalool** | Monoterpene; binds + activates PPARα; **PPARA-mutant alters susceptibility**; PPARα-dependent SLC27A4 induction | **MODERATE** — genetic dependency is unusually good, but single source (24752549) | Data-backed | Best non-fatty-acid natural-product PPARα evidence in the dataset; genetic-dependency evidence is hard to explain away |
| B4 | **Icosapent ethyl (EPA)** | ω-3 ethyl ester prodrug → EPA, same ligand class as B1/B2 | Moderate (class inference from B1/B2) | Data (CHEMBL2095209: MW 330.51, aLogP 6.47, PSA 26.30, oral, approved 2012) + knowledge | **The druggable form of the Group B finding** — the only way replicated fatty-acid PPARα ligand evidence reaches an approved oral product |

*Explicitly flagged as controls, not candidates:* **gedunin** (PPARα **antagonist** — antagonises
clofibrate; use as negative control); **dibutyl phthalate** (genuine binder + activator with **GW 6471
antagonist reversal** — the best-controlled activation evidence in the file, but a reproductive toxicant;
use as a mechanistic positive control only).

*Explicitly rejected:* quercetin/naringenin/melatonin/rutin/apigenin/myricetin/catechin PPARA rows (all
"protects expression against an insult", not engagement — and quercetin *antagonises* GW 7647);
oleanolic acid, β-carotene, methoxsalen (wrong direction); phytol, retinol, cholesterol (PPARα is the
actor, not the target); **D-fructose, sucrose, glucose, galactose** (experimental perturbagens, not
compounds — a curation defect); bare DGIdb rows (zero information); saturated fatty acids C12–C18 (all
trace to the single PMID 10403814 — database redundancy, not replication).

### Group C — PPARα-adjacent multi-target (2)

| # | Compound | Mechanism | Evidence quality | Source | Why included |
|---|---|---|---|---|---|
| C1 | **Quercetin** | 26/27 DR-panel genes (NFE2L2, AKR1B1, VEGFA, ICAM1, MMP9…); best action ratio (9/26 = 0.35) | **WEAK for PPARα** (contradictory); moderate for Nrf2/AR breadth | Data-backed (745 CTD rows) | The canonical polypharmacology candidate **and** the pipeline's frequent-hitter control. Breadth is largely bibliometric; oral bioavailability <2% |
| C2 | **Melatonin** | 19 DR-panel genes; antioxidant, anti-apoptotic, microglial modulation | WEAK for PPARα (cisplatin-protection rows only) | Data-backed (249 rows) + knowledge (BRB penetration) | **The exposure control.** MW 232, neutral, crosses BBB/BRB freely, physiologically synthesised in retina — the one candidate with unambiguously good retinal access. Tests whether access beats affinity |

*First alternates:* luteolin, apigenin (flavones with AKR1B1/NF-κB coverage, cleaner chemotype than
quercetin, but PPARG-binding and no PPARA-binding rows).

### Group D — Non-PPARα mechanistic comparators (4)

| # | Compound | ChEMBL | Mechanism | Evidence quality | Source | Why included |
|---|---|---|---|---|---|---|
| D1 | **Epalrestat** | CHEMBL56337 | **Aldose reductase (AKR1B1) inhibitor** — polyol pathway | Strong, established class | Data (MW 319, aLogP 2.92, Ro5v 0, oral, 1992) + knowledge | The most mechanistically specific non-PPAR alternative; AKR1B1 is in the DR panel; directly addresses pericyte osmotic/oxidative stress |
| D2 | **Dimethyl fumarate** | CHEMBL2107333 | **NRF2 activator** via KEAP1 cysteine modification | Strong, established | Data (MW 144, PSA 52.6, Ro5v 0, oral, 2013) + knowledge | NFE2L2 is the most-represented antioxidant node in the data; tests the Nrf2 limb of §5.2d **directly** rather than via PPARα crosstalk. Flag: lymphopenia |
| D3 | **Minocycline** | CHEMBL1434 | **Microglial deactivation / neuroprotection**; MMP9, IL1B, TNF | Strong, established | Data (MW 457, oral, 1971) + knowledge (CNS penetration) | Tests the neuroinflammatory/neurovascular-unit arm independently of lipid biology. Flag: vestibular toxicity, pigmentation on chronic use |
| D4 | **Candesartan cilexetil** | CHEMBL1014 | **AT1R blockade**, local retinal RAS | Strong, established | Data (ester prodrug, Ro5v 3 as cilexetil → candesartan) + knowledge | A purely vascular mechanism with zero PPAR involvement; also renoprotective in this comorbidity profile |

*Considered and dropped for count:* **pentoxifylline** (CHEMBL628 — haemorheology/capillary non-perfusion,
a genuinely distinct axis, excellent tolerability, weak effect size; **first alternate for Group D**).

*Deliberately excluded on protocol grounds:* intravitreal corticosteroids (fluocinolone acetonide,
triamcinolone, dexamethasone) and anti-VEGF agents (pegaptanib present; aflibercept/ranibizumab/bevacizumab
absent from the blinded table). Selecting these would require leaning on DR/DME-specific clinical knowledge
the protocol forbids — see §4.

---

## 9. Blinding compliance statement

**Data access.** I read only from `data/processed-blinded-diabetic-retinopathy/`. I did not open
`data/processed/chembl_approved_drugs.csv`, anything under `data/holdout/`, or any `answer-key*` file, and
I did not consult git history or git objects for redacted values.

**Redaction handling.** `grep` showed six `[REDACTED-HOLDOUT]` tokens across three rows of the blinded
approved-drugs file. **I deliberately did not determine which drugs those rows belong to.** Identifying the
redacted rows would invert the blind and reconstruct the answer key by elimination, so I stopped there and
am disclosing the count rather than the contents. None of the candidates I characterised showed a redacted
value in any field I printed.

**Reasoning basis.** Every candidate justification rests on (a) structure and physicochemistry from the
blinded data, (b) interaction rows from the blinded PubChem/CTD file, (c) general pharmacology —
PPAR isoform potency and selectivity, protein binding, elimination route, prodrug chemistry — and (d)
NON-DR physiology and disease biology. No drug in this report is recommended, ranked, or justified by any
DR or DME indication, approval, guideline position, or trial result.

### Disclosures — places where DR knowledge was adjacent and how I handled it

1. **Fenofibrate's `therapeutic_areas` field lists ~30 areas with no retinal or macular entry.** I noticed
   the absence. I did **not** treat it as a signal in either direction — not as evidence that fenofibrate
   lacks a retinal indication, and not as evidence that a redaction occurred there. It is excluded from all
   reasoning above.

2. **Group D selection is the weakest point in my compliance, and I want to be explicit about it.** The
   brief asked for comparators on "aldose reductase inhibition, PKCβ inhibition, RAGE axis,
   kallikrein-kinin, Nrf2 activation, neuroprotection, anti-VEGF alternatives". Those axes are themselves
   the canonical DR drug-development mechanisms, so the mechanism list arrives already shaped by DR trial
   history. I derived each individual pick from pathway logic (polyol flux → pericyte osmotic stress;
   NFE2L2 node density in the data; local retinal RAS; microglial activation) and from the blinded data,
   but **I cannot claim the mechanism categories themselves are blind** — they came from the brief. The
   ranker should treat Group D as a mechanism-diverse baseline, not as an independently derived hypothesis
   set.

3. **I excluded intravitreal steroids and anti-VEGF agents specifically because including them would have
   required DR-specific knowledge** (§4). This is a case where DR knowledge shaped a *negative* decision. I
   judged exclusion to be the more compliant choice than including them with a justification I could not
   legitimately give, but I am flagging it as a knowledge-influenced decision rather than a neutral one.

4. **Ruboxistaurin (PKCβ) and calcium dobesilate are absent from the blinded approved-drugs table.** I
   searched for them because the brief named PKCβ as an axis. I did not pursue why they are absent, and I
   did not substitute knowledge about them for data.

5. **The ANGPTL4 argument in §5.2f and §7 comes from retinal vascular biology**, not from any DR trial
   result. I believe it is within the "general physiology" allowance, but I note it because ANGPTL4's
   retinal role is studied predominantly in a DR/DME context and the line is genuinely thin there.

6. **No quantitative potency, protein-binding, half-life, or Cmax figure in this report came from the
   project data** — those fields (`bioavailability_score`, `logd`, `permeability`, `molecular_species`) are
   empty for every row in the blinded file. All such numbers are general pharmacology knowledge and are
   labelled as approximate throughout. They are the basis of the §6/§7 exposure argument, which is
   therefore knowledge-based reasoning, not a data-derived result.

**Overall:** I consider the analysis compliant, with disclosure 2 (Group D mechanism categories inherited
from the brief) as the one place where DR-specific framing unavoidably entered the candidate set.
