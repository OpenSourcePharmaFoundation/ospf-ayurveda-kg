# Drug-Indication Mechanisms of Action

Comprehensive mapping of mechanisms of action for each indication across the major drug candidates identified by the OSPF Ayurveda Knowledge Graph project. Organized by candidate tier, with OM pathobiology phase annotations and clinical trial database references for validation.

**Last updated:** 2026-06-08
**Data sources:** ChemBL (3,276 drugs), DisGeNET (51 OM biomarkers), TTD, IMPPAT, PubChem, DrugBank
**Cross-reference:** [Clinical Trials Databases](clinical-trials-databases.md) for trial validation sources

---

## Table of Contents

- [How to Read This Document](#how-to-read-this-document)
- [Consensus-Ranked OM Candidates (Top 8)](#consensus-ranked-om-candidates-top-8)
- [Currently Approved OM Drugs (TTD)](#currently-approved-om-drugs-ttd)
- [Breast Cancer Intersection Candidates](#breast-cancer-intersection-candidates)
- [Additional Repurposing Candidates](#additional-repurposing-candidates)
- [Eliminated Candidates](#eliminated-candidates)
- [Ayurvedic Plant Compounds](#ayurvedic-plant-compounds)
- [OM Phase Coverage Summary](#om-phase-coverage-summary)
- [Clinical Trial Validation Sources](#clinical-trial-validation-sources)

---

## How to Read This Document

Each drug entry lists:
- **Current approved indications** with the mechanism of action specific to that indication
- **Proposed OM mechanism** — how the drug could work against oral mucositis specifically
- **OM Phase** — which phase(s) of the Sonis 5-phase OM pathobiology model the drug addresses:
  - Phase 1: Initiation (ROS, DNA damage)
  - Phase 2: Upregulation (NF-κB, cytokine cascade)
  - Phase 3: Amplification (ceramide/sphingomyelin, positive feedback)
  - Phase 4: Ulceration (bacterial colonization, tissue breakdown)
  - Phase 5: Healing (epithelial proliferation, mucosal repair)
- **Safety verdict** from the multi-agent consensus analysis (GREEN / YELLOW / ORANGE / RED)

---

## Consensus-Ranked OM Candidates (Top 8)

### #1: Dexamethasone — Score: 72/100

**Class:** Corticosteroid | **Safety:** YELLOW (Conditional) | **Status:** Already in clinical use (benchmark)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Oral lichen planus | Glucocorticoid receptor (GR) agonist → suppresses T-cell-mediated mucosal autoimmunity | GR → NF-κB suppression |
| Inflammation (general) | GR agonist → inhibits phospholipase A2 → blocks prostaglandin/leukotriene synthesis | GR, COX-2, PLA2 |
| Chemotherapy-induced nausea | Central and peripheral anti-emetic via GR-mediated suppression of prostaglandins and substance P | GR, NK1 pathway |
| Cerebral edema | Reduces capillary permeability and vasogenic edema via GR-mediated anti-inflammatory effects | GR, vascular endothelium |
| Allergic conditions | Suppresses IgE-mediated mast cell degranulation and eosinophil recruitment | GR → IL-4, IL-5, IL-13 |
| **Proposed OM mechanism** | **Suppresses NF-κB → reduces TNF-α, IL-1β, IL-6 in oral mucosa. Validated in SWISH trial (0.1 mg/mL swish-and-spit)** | **GR → NF-κB, Phase 2** |

**OM Phases:** Phase 2 (primary), partial Phase 3
**Key risk for OM patients:** Immunosuppression → oral candidiasis in neutropenic patients

---

### #2: Budesonide — Score: 67.5/100

**Class:** Corticosteroid | **Safety:** YELLOW (Conditional) | **Recommended form:** Orodispersible tablet or mucoadhesive paste

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Asthma | Inhaled GR agonist → reduces airway inflammation and mucus hypersecretion | GR → NF-κB, eosinophils |
| Crohn's disease (ileal/ascending colon) | Oral GR agonist with high first-pass metabolism (90%) → local GI anti-inflammatory with minimal systemic effects | GR → NF-κB, mucosal T-cells |
| Eosinophilic esophagitis (Jorveza) | Orodispersible GR agonist → suppresses eosinophilic infiltration and esophageal remodeling | GR → IL-5, eotaxin-3 |
| Allergic rhinitis | Intranasal GR agonist → reduces nasal mucosal edema and inflammatory cell recruitment | GR → NF-κB, mast cells |
| Ulcerative colitis | Rectal/oral GR agonist → reduces colonic mucosal inflammation | GR → NF-κB, TNF-α |
| **Proposed OM mechanism** | **Superior mucosal selectivity over dexamethasone: 90% first-pass hepatic metabolism limits systemic immunosuppression. Same NF-κB suppression locally. 505(b)(2) path via Jorveza precedent** | **GR → NF-κB, Phase 2** |

**OM Phases:** Phase 2 (primary)
**SAR advantage:** Budesonide > dexamethasone for mucosal selectivity (SAR Analyst finding)
**Key risk for OM patients:** CYP3A4 interaction with azole antifungals (mandatory in neutropenic patients)

---

### #3: Mesalamine (5-Aminosalicylic Acid) — Score: 62.5/100

**Class:** Aminosalicylate | **Safety:** GREEN | **ChemBL:** CHEMBL704 | **MW:** 153.1 | **LogP:** 0.67

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Ulcerative colitis | Topical mucosal anti-inflammatory → inhibits NF-κB and COX-2; scavenges ROS; inhibits IL-1 and TNF-α production in colonic epithelium | NF-κB, COX-2, LOX, ROS |
| Inflammatory bowel disease (IBD) | Same as UC — local mucosal action; inhibits prostaglandin E2 and leukotriene B4 synthesis | COX, 5-LOX |
| Crohn's disease (colonic) | Mucosal anti-inflammatory; less effective than in UC due to transmural inflammation beyond mucosal reach | NF-κB, COX-2 |
| **Proposed OM mechanism** | **Direct NF-κB/COX inhibition on oral mucosa. Anti-inflammatory WITHOUT immunosuppression (critical advantage). Ideal physicochemical profile for oral rinse (LogP 0.67, MW 153.1, PSA 83.6)** | **NF-κB, COX-2, Phase 2** |

**OM Phases:** Phase 2 (primary), indirect Phase 5 (mucosal healing properties)
**ADMET score:** 9/10 — ideal topical profile
**Key caveat:** Zero binding data against any OM-specific target (mechanism unvalidated for OM)

---

### #4: Melatonin — Score: 61/100

**Class:** Neurohormone / Antioxidant | **Safety:** GREEN | **Recommended form:** 3-5% mucoadhesive oral gel (night-time)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Insomnia / sleep disorders | MT1/MT2 melatonin receptor agonist → entrains circadian rhythm; promotes sleep onset | MT1, MT2 receptors |
| Jet lag | MT1/MT2 agonist → resets suprachiasmatic nucleus circadian clock | MT1, MT2 |
| **Proposed OM mechanism** | **Phase 1 ROS scavenging (direct free radical neutralization); NRF2 pathway activation (upregulates endogenous antioxidant enzymes: SOD, GPx, catalase). Unique property: radioprotective for NORMAL tissue while radiosensitizing TUMOR tissue — the only candidate that actively helps cancer treatment** | **ROS, NRF2, Phase 1** |

**OM Phases:** Phase 1 (primary — only strong Phase 1 candidate)
**Unique value:** Cancer-synergistic (radioprotective for normal tissue, radiosensitizing for tumors)
**Key risk:** Mixed clinical evidence from prior underpowered trials

---

### #5: N-Acetylcysteine (NAC) — Score: 59.5/100

**Class:** Mucolytic / Antioxidant | **Safety:** GREEN | **Recommended form:** 1-5% oral rinse

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Acetaminophen overdose | Replenishes hepatic glutathione stores → detoxifies NAPQI (toxic metabolite) | Glutathione synthesis |
| Mucolytic (respiratory) | Breaks disulfide bonds in mucus glycoproteins → reduces mucus viscosity | Mucin disulfide bonds |
| Oral mucositis (existing indication) | Direct antioxidant + glutathione precursor → reduces oxidative damage to mucosal epithelium | ROS, glutathione |
| **Proposed OM mechanism** | **Glutathione precursor → restores cellular antioxidant capacity. Direct Phase 1 ROS scavenger. Immediately deployable (OTC, no regulatory barriers)** | **Glutathione, ROS, Phase 1** |

**OM Phases:** Phase 1 (primary)
**Developability:** 9/10 — OTC, no regulatory barriers
**Key risk:** Sulfurous taste/smell → severe compliance issue (solve taste or stop development)

---

### #6: Pentoxifylline — Score: 58/100

**Class:** Methylxanthine derivative | **Safety:** Safe (systemic) | **Recommended form:** 0.5-2% oral rinse or systemic 400mg TID

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Peripheral vascular disease / intermittent claudication | Nonselective phosphodiesterase inhibitor → increases cAMP → improves erythrocyte deformability and reduces blood viscosity; inhibits platelet aggregation | PDE (nonselective), cAMP |
| Radiation fibrosis (off-label) | TNF-α suppression + microvascular flow improvement → reduces fibrotic tissue remodeling | TNF-α, microvascular endothelium |
| **Proposed OM mechanism** | **Direct TNF-α suppression (Phase 2 cytokine cascade). Improves microvascular blood flow to damaged mucosa. New discovery from Drug Repurposing Strategist (score 82). Complements mesalamine (different mechanism on same phase)** | **TNF-α, PDE, Phase 2-3** |

**OM Phases:** Phase 2 (primary), partial Phase 3 (microvascular)
**Discovery:** New find from drug repurposing analysis — not previously considered for OM
**Key risk:** Systemic GI side effects in patients who may already be unable to eat

---

### #7: Apremilast — Score: 57.5/100

**Class:** PDE4 inhibitor | **Safety:** Safe | **Recommended form:** Systemic (30mg BID oral)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Psoriasis | Selective PDE4 inhibition → increases intracellular cAMP → reduces TNF-α, IL-17, IL-23; increases IL-10 (anti-inflammatory) | PDE4 → cAMP → NF-κB |
| Psoriatic arthritis | Same PDE4 inhibition → reduces synovial and entheseal inflammation | PDE4, TNF-α, IL-17 |
| Behcet's oral ulcers (FDA-approved) | PDE4 inhibition → suppresses T-cell and monocyte inflammatory responses in oral mucosa | PDE4 → TNF-α, IL-17, IL-23 |
| **Proposed OM mechanism** | **Strongest phenotypic analog — FDA-approved for oral ulcers (Behcet's). PDE4 inhibition reduces the same cytokine cascade driving OM (TNF-α, IL-17). Anti-inflammatory without immunosuppression** | **PDE4, Phase 2** |

**OM Phases:** Phase 2 (primary)
**Phenotypic relevance:** Only candidate with FDA approval for oral ulcers (different etiology but same tissue)
**Key risk:** On-patent, expensive ($15K+/yr), systemic dosing only

---

### #8: Glycyrrhizin (Yashtimadhu) — Score: 56.5/100

**Class:** Triterpene saponin (natural product) | **Safety:** YELLOW (Conditional) | **Recommended form:** Standardized extract oral rinse (8% glycyrrhizic acid)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Oral ulcers (Ayurvedic traditional) | Mucosal protection via anti-inflammatory and demulcent properties; NF-κB pathway inhibition | NF-κB, HMGB1 |
| Stomach ulcers (Ayurvedic/traditional) | Increases prostaglandin E2 in gastric mucosa → enhances mucosal barrier; anti-H. pylori activity | PGE2, mucosal barrier |
| Hepatoprotection (traditional) | HMGB1 inhibition → reduces hepatic inflammatory signaling | HMGB1, NF-κB |
| **Proposed OM mechanism** | **Unique HMGB1 inhibition (underserved OM target, GDA 0.01) + NF-κB suppression + CASP3 blockade (anti-apoptotic). Glycoside form preferred over aglycone for topical OM (better mucoadhesion via sugar moieties, lower systemic absorption). Strongest Ayurvedic bridge candidate** | **HMGB1, NF-κB, CASP3, Phase 2-3** |

**OM Phases:** Phase 2 (NF-κB), Phase 3 (HMGB1/CASP3)
**Ayurvedic bridge score:** 8/10 (highest)
**SAR finding:** Glycoside form > aglycone for topical OM application
**Key risk:** Pseudoaldosteronism at high systemic doses (K+ monitoring, dose-limit 14 days)
**Regulatory path:** AYUSH (India) — 12-18 months, $500K-1.5M

---

## Currently Approved OM Drugs (TTD)

Only **4 drugs** have direct Oral Mucositis indications — the field is severely underserved.

### Palifermin (Kepivance)

**Class:** Recombinant human KGF | **ICD-10:** K12.3 | **Status:** Only FDA-approved drug for OM (HSCT setting only)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Oral mucositis (HSCT) | Recombinant keratinocyte growth factor → FGFR2 agonist → stimulates basal epithelial cell proliferation, differentiation, and migration; thickens mucosal epithelium pre-chemotherapy | FGFR2 (Gene: FGF7, GDA 0.06) |

**OM Phase:** Phase 5 (healing) — given prophylactically to thicken epithelium before damage occurs
**Limitation:** Approved only for hematopoietic stem cell transplant, not general chemotherapy; $5-8K/course

### Hebervis

**Class:** Recombinant human EGF | **ICD-10:** K12.3

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Oral mucositis | EGF receptor agonist → activates EGFR/MAPK/ERK signaling → promotes mucosal epithelial proliferation and wound healing | EGF → EGFR (Gene: EGF, GDA 0.02) |

**OM Phase:** Phase 5 (healing)

### Lactermin

**Class:** Recombinant human intestinal trefoil factor | **ICD-10:** K12.3

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Oral mucositis | Trefoil factor-mediated mucosal restitution → promotes epithelial cell migration across wound bed without requiring cell proliferation | TFF family |

**OM Phase:** Phase 5 (healing)

### AG-013

**Class:** Engineered Lactococcus secreting TFF1 | **ICD-10:** K12.3

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Oral mucositis | Genetically modified Lactococcus lactis delivers TFF1 (trefoil factor-1) directly to oral mucosa → mucosal protection, wound healing, and anti-apoptotic signaling | TFF1 (Gene: TFF1) |

**OM Phase:** Phase 4-5 (protection + healing)

---

## Breast Cancer Intersection Candidates

These 11 drugs are already indicated for breast cancer, enabling potential dual-purpose treatment — managing cancer while also addressing OM.

### Cimetidine — "Hidden Gem"

**Class:** H2 receptor antagonist | **ChemBL:** CHEMBL30 | **MW:** 252.4 | **LogP:** 0.60

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Gastric/duodenal ulcer | Competitive H2 receptor antagonist → blocks histamine-stimulated acid secretion by parietal cells | H2 receptor |
| GERD | Same H2 blockade → reduces gastric acid reflux | H2 receptor |
| Breast cancer (immunomodulatory) | H2 blockade on T-regulatory cells → enhances NK cell cytotoxicity and reduces tumor immune evasion | H2 receptor on Tregs, NK cells |
| **Proposed OM mechanism** | **Anti-inflammatory H2 blockade on mucosal immune cells; near-perfect oral mucosal fingerprint (LogP 0.60, MW 252, PSA 88.9). Cheap, widely available, low toxicity, already given to cancer patients** | **H2R, mucosal immune cells** |

### Letrozole

**Class:** Aromatase inhibitor | **ChemBL:** CHEMBL1444 | **MW:** 285.3 | **LogP:** 2.66

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Breast cancer (1st-line hormonal) | Competitive aromatase (CYP19A1) inhibitor → blocks estrogen synthesis → starves ER+ tumor cells | CYP19A1 (aromatase) |
| Ovulation induction (off-label) | Same aromatase inhibition → increases FSH via reduced estrogen negative feedback | CYP19A1 → hypothalamic-pituitary axis |

### Capsaicin

**Class:** TRPV1 agonist | **ChemBL:** CHEMBL294199 | **MW:** 305.4 | **LogP:** 3.79

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Neuropathic pain | TRPV1 receptor agonist → initial excitation then prolonged desensitization of C-fiber nociceptors; depletes substance P | TRPV1 |
| Cancer pain (topical) | Same TRPV1 desensitization → reduces pain signal transmission | TRPV1 |
| **Proposed OM mechanism** | **Topical nociceptor desensitization could address OM pain directly (dual-purpose in breast cancer patients)** | **TRPV1** |

### Binimetinib

**Class:** MEK inhibitor | **ChemBL:** CHEMBL3187723 | **MW:** 441.2 | **LogP:** 3.01

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Melanoma (BRAF-mutant) | Selective MEK1/2 inhibition → blocks Ras/Raf/MEK/ERK proliferative signaling cascade | MEK1 (MAP2K1), MEK2 (MAP2K2) |
| Breast cancer | Same MAPK pathway inhibition → anti-proliferative | MEK1/2 |
| **Proposed OM mechanism** | **MAPK/ERK cascade is implicated in OM pathogenesis (Phase 2 amplification). MEK inhibition could reduce inflammatory signaling. However, may impair mucosal healing (Phase 5)** | **MEK1/2 → MAPK/ERK** |

### Leflunomide

**Class:** DHODH inhibitor | **ChemBL:** CHEMBL960 | **MW:** 270.2 | **LogP:** 3.25

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Rheumatoid arthritis | Active metabolite (teriflunomide) inhibits dihydroorotate dehydrogenase (DHODH) → blocks de novo pyrimidine synthesis → selective anti-proliferative effect on rapidly dividing lymphocytes | DHODH |
| **Proposed OM mechanism** | **Immunomodulatory anti-inflammatory via pyrimidine synthesis inhibition. Caution: may compound chemotherapy-induced immunosuppression** | **DHODH** |

### Sunitinib

**Class:** Multi-kinase inhibitor | **ChemBL:** CHEMBL1567 | **MW:** 398.5 | **LogP:** 3.33

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Renal cell carcinoma | Multi-kinase inhibition: VEGFR1-3, PDGFRα/β, KIT, FLT3, RET → anti-angiogenic + anti-proliferative | VEGFR, PDGFR, KIT, FLT3, RET |
| GIST | KIT and PDGFRα inhibition → blocks oncogenic kinase signaling | KIT, PDGFRα |
| **Proposed OM mechanism** | **Anti-angiogenic properties could reduce OM-associated vascular inflammation. However, sunitinib itself CAUSES stomatitis as a side effect — likely counterproductive** | **VEGFR, PDGFR** |

### Carmustine

**Class:** Alkylating agent | **ChemBL:** CHEMBL513 | **MW:** 214.1 | **LogP:** 1.16

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Brain tumors / lymphoma | DNA alkylation → interstrand and intrastrand cross-links → replication arrest → cell death; also carbamoylates proteins | DNA |
| **Note:** Carmustine causes OM as a side effect — not a viable OM treatment candidate despite matching the mucosal delivery fingerprint | | |

### Melphalan

**Class:** Alkylating agent | **ChemBL:** CHEMBL852 | **MW:** 305.2 | **LogP:** 1.93

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Multiple myeloma / breast cancer | Nitrogen mustard → DNA alkylation → interstrand cross-links → replication arrest | DNA |
| **Note:** Melphalan is a major CAUSE of oral mucositis — included for completeness but not a treatment candidate | | |

### Cephalexin

**Class:** Beta-lactam antibiotic | **ChemBL:** CHEMBL1200544 | **MW:** 347.4 | **LogP:** 0.44

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Bacterial infections (UTI, skin, respiratory) | Binds penicillin-binding proteins (PBPs) → inhibits bacterial cell wall transpeptidation → cell lysis | PBPs (bacterial) |
| **Proposed OM mechanism** | **Addresses Phase 4 secondary bacterial colonization of OM ulcers. Already used in breast cancer patients for infection management** | **PBPs, Phase 4** |

### Ranitidine

**Class:** H2 receptor antagonist | **ChemBL:** CHEMBL1790041 | **MW:** 314.4 | **LogP:** 1.46

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Gastric ulcer / GERD | Competitive H2 receptor antagonist → reduces basal and stimulated acid secretion | H2 receptor |
| **Proposed OM mechanism** | **Similar to cimetidine — anti-inflammatory potential on mucosal immune cells. Note: ranitidine withdrawn in many markets (NDMA contamination concern)** | **H2R** |

### Lansoprazole

**Class:** Proton pump inhibitor | **ChemBL:** CHEMBL480 | **MW:** 369.4 | **LogP:** 3.52

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Gastric ulcer / GERD | Irreversible inhibition of H+/K+-ATPase (proton pump) in gastric parietal cells → near-complete acid suppression | H+/K+-ATPase |
| H. pylori eradication (with antibiotics) | Acid suppression → raises gastric pH → enhances antibiotic efficacy against H. pylori | H+/K+-ATPase |
| **Proposed OM mechanism** | **Emerging anti-inflammatory evidence beyond acid suppression: inhibits neutrophil adhesion, reduces IL-8 production, scavenges ROS. Already given to cancer patients for GI protection** | **H+/K+-ATPase, IL-8, ROS** |

---

## Additional Repurposing Candidates

### Tier 1: Mucosal Inflammation Experience

| Drug | Class | Current Indications | Mechanism of Action | OM Relevance |
|---|---|---|---|---|
| **Azathioprine** (CHEMBL1542) | Purine analog | RA, ulcerative colitis, dermatitis | Metabolized to 6-mercaptopurine → inhibits de novo purine synthesis → suppresses T/B lymphocyte proliferation | Immunomodulator proven in mucosal disease; caution: compounds chemo-induced immunosuppression |
| **Naltrexone** (CHEMBL19019) | Opioid antagonist | Alcohol/opioid dependence, ulcerative colitis | At standard dose: μ-opioid receptor competitive antagonist. At low dose (1-4.5mg): paradoxical anti-inflammatory via transient opioid blockade → upregulates endorphins and OGF-OGFr axis | Low-dose anti-inflammatory effect on mucosa demonstrated in UC |

### Tier 2: Anti-Inflammatory

| Drug | Class | Current Indications | Mechanism of Action | OM Relevance |
|---|---|---|---|---|
| **Nepafenac** (CHEMBL1021) | NSAID prodrug | Eye inflammation, cataract surgery | Prodrug → converted to amfenac by intraocular hydrolases → COX-1/COX-2 inhibition in target tissue | NSAID proven effective on mucosal tissue (ocular); topical application model |
| **Piroxicam** (CHEMBL527) | NSAID (oxicam) | RA, OA, eye inflammation | Non-selective COX-1/COX-2 inhibitor → blocks prostaglandin synthesis; also inhibits neutrophil aggregation and proteoglycanase activity | NSAID with mucosal application experience |
| **Aminosalicylic acid** (CHEMBL1169) | Aminosalicylate | UC, Crohn's | Same scaffold as mesalamine → COX/5-LOX inhibition; NF-κB modulation | Functionally identical to mesalamine for OM purposes |

### Tier 3: JAK Inhibitor Family

**Safety note:** All JAK inhibitors FAIL the "leaky mucosa test" — systemic absorption through Grade 3-4 OM ulcerated mucosa could cause dangerous systemic immunosuppression. Included for completeness but not recommended for OM.

| Drug | Class | Current Indications | Mechanism of Action | JAK Selectivity |
|---|---|---|---|---|
| **Abrocitinib** (CHEMBL3655081) | JAK1 selective | Atopic eczema, psoriasis | JAK1 inhibition → blocks IL-4, IL-13, IL-31 signaling → reduces Th2-driven inflammation | JAK1 (less immunosuppressive) |
| **Ritlecitinib** (CHEMBL4085457) | JAK3/TEC | RA, UC, Crohn's | JAK3/TEC family kinase inhibition → blocks γc cytokine receptor signaling (IL-2, IL-4, IL-7, IL-9, IL-15, IL-21) | JAK3 + TEC |
| **Peficitinib** (CHEMBL3137308) | Pan-JAK | RA, UC | Non-selective JAK1/2/3 inhibition → broad cytokine suppression | Pan-JAK (highest risk) |
| **Filgotinib** (CHEMBL3301607) | JAK1 selective | RA, UC, Crohn's | JAK1-selective inhibition → preferentially blocks type I/II cytokine receptor signaling | JAK1 |

---

## Eliminated Candidates

These drugs were evaluated but removed from the pipeline due to unacceptable safety risks.

### Colchicine — RED (NO-GO)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Gout (acute flares) | Binds tubulin → prevents microtubule assembly → inhibits neutrophil migration and NLRP3 inflammasome activation → blocks IL-1β processing | Tubulin, NLRP3, IL-1β |
| Familial Mediterranean Fever | Same tubulin binding → reduces neutrophil-driven inflammatory episodes | Tubulin, NLRP3 |
| Pericarditis | NF-κB inhibition via tubulin disruption → reduces pericardial inflammation | NF-κB (indirect via tubulin) |
| **OM rationale was:** | Root-cause NF-κB/NLRP3 mechanism (Disease Modeler score: 8/10) | NF-κB, NLRP3 |
| **ELIMINATED because:** | **Fatal DDI with azole antifungals (fluconazole, etc.) which are MANDATORY in neutropenic OM patients. Narrow therapeutic index. No antidote. Tubulin inhibition = additive myelosuppression** | |

**SAR alternative:** Demecolcine (wider therapeutic index) or MCC950 (pure NLRP3 inhibitor)

### Tofacitinib — RED (NO-GO)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Rheumatoid arthritis | JAK1/3 inhibition → blocks IL-6, IFN-γ, IL-2, IL-4, IL-7, IL-9, IL-15, IL-21 signaling | JAK1, JAK3 |
| Ulcerative colitis | Same JAK1/3 inhibition → reduces mucosal T-cell inflammatory response | JAK1, JAK3 |
| Psoriatic arthritis | JAK1/3 inhibition → blocks Th1/Th17 cytokine signaling | JAK1, JAK3 |
| **ELIMINATED because:** | **3 simultaneous FDA Black Box Warnings. JAK3 selectivity = direct lymphocyte suppression. QED 0.93 (highest drug-likeness) is irrelevant when safety is this adverse. Oral mucosa absorbs too much systemically, especially through ulcerated tissue** | |

### Ruxolitinib — ORANGE (High Risk)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Myelofibrosis | JAK1/2 inhibition → reduces inflammatory cytokine signaling → shrinks spleen, improves symptoms | JAK1, JAK2 |
| Polycythemia vera | JAK2 inhibition → controls erythrocyte overproduction | JAK2 |
| Graft-vs-host disease | JAK1/2 inhibition → suppresses alloreactive T-cell responses | JAK1, JAK2 |
| Atopic dermatitis (topical) | Topical JAK1/2 inhibition → reduces skin Th2 inflammation | JAK1, JAK2 |
| **HIGH RISK because:** | **Systemic JAK1/2 absorption likely through Grade 3-4 ulcerated oral mucosa. Could antagonize filgrastim (G-CSF) rescue — JAK2 is in the G-CSF signaling pathway** | |

### Curcumin — DEPRIORITIZED (Score: 53.5)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Anti-inflammatory (traditional) | NF-κB inhibition, COX-2 inhibition, ROS scavenging, modulates multiple inflammatory transcription factors | NF-κB, COX-2, AP-1, STAT3 |
| **DEPRIORITIZED because:** | **PAINS compound (pan-assay interference). 120+ clinical trials, 0 FDA approvals = evidence of failure, not precedent. Retained for orthogonal target validation only (distinguish real NF-κB binding from assay artifacts)** | |

### Kaempferol — DEPRIORITIZED (Score: 47)

| Indication | Mechanism of Action | Target(s) |
|---|---|---|
| Anti-inflammatory (traditional) | Reported 12+ targets including NF-κB, COX-2, JNK, MAPK, caspases | Multi-target (alleged) |
| **DEPRIORITIZED because:** | **90% of "12+ targets" are CTD text-mining artifacts, not experimental binding data. JNK activation is COUNTERPRODUCTIVE for OM. SAR shows apigenin > kaempferol for genuine anti-inflammatory activity** | |

---

## Ayurvedic Plant Compounds

Active phytochemicals from plants in the Sapthachadadi Kashayam and Panchathikthaka Ghrita formulations with known mechanisms.

| Plant | Ayurvedic Name | Active Compound(s) | Mechanism of Action | OM Phase |
|---|---|---|---|---|
| **Glycyrrhiza glabra** | Yashtimadhu | Glycyrrhizin, glabridin | HMGB1 inhibition + NF-κB suppression + CASP3 blockade; mucosal demulcent | Phase 2-3 |
| **Terminalia chebula** | Haritaki | Gallic acid, chebulagic acid, ellagic acid | Potent antioxidant (ROS scavenging); astringent (tannin-mediated tissue contraction); broad-spectrum antimicrobial | Phase 1, 4 |
| **Picrorhiza kurrooa** | Katuki | Apocynin | NADPH oxidase (NOX) inhibitor → blocks superoxide generation at source (upstream of ROS) | Phase 1 |
| **Azadirachta indica** | Nimba | Nimbolide, azadirachtin | NF-κB inhibition; broad antimicrobial; immunomodulatory | Phase 2, 4 |
| **Tinospora cordifolia** | Guduchi | Berberine, palmatine | AMPK activation → NF-κB inhibition; mitochondrial ROS modulation | Phase 1-2 |
| **Cyperus rotundus** | Musta | Sesquiterpenes (α-cyperone) | Anti-inflammatory (COX/LOX inhibition); direct stomatitis indication in IMPPAT | Phase 2 |
| **Santalum album** | Chandana | α-Santalol, β-santalol | Cooling anti-inflammatory; inhibits COX-2 and 5-LOX | Phase 2 |
| **Cassia fistula** | Aragvadha | Proanthocyanidins | Antioxidant; anti-inflammatory; wound healing promotion | Phase 1, 5 |
| **Alstonia scholaris** | Saptaparna | Betulinic acid, echitamine | Anti-inflammatory alkaloids; NF-κB modulation | Phase 2 |

### Proposed Ayurvedic Combination: Yashtimadhu-Haritaki Kavala

| Component | Standardization | Mechanisms | OM Phases Covered |
|---|---|---|---|
| Glycyrrhiza glabra extract | 8% glycyrrhizic acid | NF-κB + HMGB1 + CASP3 | Phase 2, 3 |
| Terminalia chebula extract | 40% tannins | Antioxidant + astringent + antimicrobial | Phase 1, 4, partial 5 |
| **Combined coverage** | | **Natural tannin mucoadhesion (solves saliva washout); pleasant licorice taste (compliance advantage)** | **Phase 1, 2, 3, 4, partial 5** |

---

## OM Phase Coverage Summary

| OM Phase | Mechanism | Best Candidates | Coverage Status |
|---|---|---|---|
| **Phase 1: Initiation** | ROS generation, DNA damage, NRF2 | Melatonin (NRF2), NAC (glutathione), Terminalia (gallic/ellagic acid), Picrorhiza (apocynin/NOX) | COVERED |
| **Phase 2: Upregulation** | NF-κB activation, TNF-α/IL-1β/IL-6 | Budesonide, mesalamine, glycyrrhizin, pentoxifylline, apremilast, dexamethasone | OVERCOVERED (11/13 candidates) |
| **Phase 3: Amplification** | Ceramide/sphingomyelin pathway, HMGB1, positive feedback | Glycyrrhizin (HMGB1), pentoxifylline (partial) | **CRITICAL GAP** — ceramide pathway unaddressed |
| **Phase 4: Ulceration** | Bacterial colonization, tissue breakdown | Terminalia chebula (astringent + antimicrobial), cephalexin (antibiotic) | PARTIAL (Track 2 only) |
| **Phase 5: Healing** | Epithelial proliferation, mucosal repair | Palifermin (FGFR2), Hebervis (EGF), AG-013 (TFF1) | WEAK — approved drugs limited in availability/cost |

### Critical Gap: Phase 3 Ceramide Pathway

No candidate meaningfully addresses the ceramide/sphingomyelin amplification loop. Future investigation suggested:
- **Amitriptyline** — functional inhibitor of acid sphingomyelinase (FIASMA)
- **Lithium chloride** — GSK3β inhibitor for Wnt/β-catenin healing pathway
- Natural product sphingomyelinase inhibitors from unexplored plant sources

---

## Clinical Trial Validation Sources

Cross-referencing with [Clinical Trials Databases](clinical-trials-databases.md), the most actionable registries for validating these mechanisms in OM:

| Database | Why Relevant | Priority Searches |
|---|---|---|
| **ClinicalTrials.gov / AACT** | Largest registry; AACT provides PostgreSQL dump for programmatic querying | Search each candidate drug + "oral mucositis" or "stomatitis" |
| **NCI PDQ** | OM is primarily a cancer treatment side effect; NCI contains high-relevance trials | Cancer-specific OM intervention trials; palifermin, dexamethasone, budesonide |
| **WHO ICTRP** | Catches trials in regional registries not mirrored to ClinicalTrials.gov | Especially for glycyrrhizin, Ayurvedic formulations, melatonin (non-US trials) |
| **CTRI (India)** | India's registry is uniquely relevant for Ayurvedic compound trials | Yashtimadhu, Haritaki, Triphala, Sapthachadadi Kashayam for oral conditions |
| **Cochrane CENTRAL** | Systematic reviews aggregate evidence across trials | "Oral mucositis prevention" and "oral mucositis treatment" systematic reviews |
| **EU Clinical Trials Register** | European trials for budesonide (Jorveza precedent is European) | Budesonide orodispersible, mesalamine topical |

### Recommended Search Strategy

For each candidate, query in this order:
1. **AACT** (structured data, programmable) — `intervention_name LIKE '%[drug]%' AND condition LIKE '%mucositis%'`
2. **ClinicalTrials.gov** (broader search with free text) — `[drug] AND (oral mucositis OR stomatitis OR oral ulcer)`
3. **CTRI** (Ayurvedic compounds only) — `[Ayurvedic name] AND (mukha roga OR stomatitis OR oral)`
4. **PubMed/MEDLINE** — `[drug] AND oral mucositis[MeSH]` for published trial results

---

*Data compiled from OSPF Ayurveda Knowledge Graph multi-agent consensus analysis (2026-05-04), ChemBL drug repurposing analysis (2026-05-03), and molecular fingerprint profiling (2026-01-29).*
