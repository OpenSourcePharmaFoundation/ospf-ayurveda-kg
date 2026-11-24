# Disease Model — Diabetic Retinopathy (incl. Diabetic Macular Edema)

**Agent:** Disease Biology Research Specialist
**Date:** 2026-10-05
**Run:** BLINDED benchmark run (`data/processed-blinded-diabetic-retinopathy/`)
**Audience:** ~15 downstream drug-discovery agents. This is the foundation document.

---

## 0. Blinding Compliance Statement

This model was built under the holdout blinding protocol
(`.../2026-10-05/blinding-protocol.md`).

- Project data read **only** from `data/processed-blinded-diabetic-retinopathy/`.
- `data/processed/chembl_approved_drugs.csv`, `data/holdout/**`, and any `answer-key*`
  file were **not** read. Git history was not used to recover redacted values.
- Standard of care is described at **modality and mechanism-class level only**
  (intravitreal anti-VEGF, intravitreal corticosteroid, panretinal photocoagulation,
  focal/grid laser, vitrectomy, systemic glycemic / blood-pressure / lipid control).
- **No specific systemic or oral drug is named anywhere in this document** in connection
  with retinopathy outcomes — not in Section 4, not in Section 5, not in the PPARA
  assessment. Where the PPARα ligand space is discussed, it is discussed as *target
  pharmacology* and via the phytochemical probes actually present in the blinded
  PubChem table. Section 4's "failed approaches" lists failed **mechanisms** and
  **ocular/intravitreal agents** only.
- No `[REDACTED-HOLDOUT]` cell was encountered in the files used for this model
  (the redaction is confined to `chembl_approved_drugs.csv` indication columns, which
  this model does not depend on).

### Confidence marker key

| Marker | Meaning |
|---|---|
| `[ESTABLISHED]` | Textbook / replicated across independent human datasets. Safe to score against. |
| `[CURRENT CONSENSUS]` | Field broadly agrees; supported by human data but with live methodological debate. |
| `[EMERGING]` | Active research. Mostly animal/cell data or small human series. Hypothesis-generating. |
| `[UNCERTAIN]` | Contested, conflicting, or extrapolated. Do not weight heavily. |

---

## 1. Disease Overview

**Full name:** Diabetic retinopathy (DR) — a chronic, progressive microvascular and
neurodegenerative complication of diabetes mellitus affecting the neurosensory retina.
**Diabetic macular edema (DME)** is the principal vision-threatening complication and
can occur at *any* DR severity stage.

### 1.1 Coding

| System | Codes |
|---|---|
| ICD-10-CM | `E08.3x` (DM due to underlying condition), `E09.3x` (drug/chemical-induced), `E10.3x` (T1DM), `E11.3x` (T2DM), `E13.3x` (other specified DM). Fourth/fifth characters encode severity and macular edema: `.311` unspecified DR **with** macular edema, `.319` unspecified DR **without**, `.321/.329` mild NPDR ±ME, `.331/.339` moderate NPDR, `.341/.349` severe NPDR, `.351/.359` PDR, `.37x` diabetic macular edema with traction, `.36` combined traction retinal detachment / rhegmatogenous detachment. Laterality is a sixth character. `[ESTABLISHED]` |
| ICD-9-CM (legacy) | 362.01–362.07 `[ESTABLISHED]` |
| ICD-11 | Classified under disorders of the retinal vasculature (9B71 block), with diabetic retinopathy and diabetic maculopathy as distinct entities. Exact stem characters vary by release — verify before regulatory use. `[UNCERTAIN]` on exact stem |
| SNOMED CT | 4855003 (retinopathy due to diabetes mellitus); 312912001 (DME) `[ESTABLISHED]` |
| MeSH | D003930 (Diabetic Retinopathy); D008269 (Macular Edema) `[ESTABLISHED]` |
| EFO / MONDO | EFO_0000399 / MONDO_0005badge-family diabetic retinopathy `[UNCERTAIN]` on exact MONDO id |

### 1.2 Epidemiology

- Global DR prevalence among people with diabetes: **~22–35%**; pooled modern estimate
  **~22.3%**, with **~103 million** adults affected in 2020, projected to
  **~160 million by 2045**. `[CURRENT CONSENSUS]`
- **Vision-threatening DR (VTDR** = severe NPDR, PDR, or DME**): ~6–7%** of people with
  diabetes, roughly **28–30 million** worldwide. `[CURRENT CONSENSUS]`
- **DME prevalence: ~5–7%** of all people with diabetes; rises to **~15–20%** in those
  with ≥20 years duration. DME is the **leading cause of vision loss** in DR because it
  attacks the fovea directly. `[ESTABLISHED]`
- **Leading cause of preventable blindness in working-age adults (20–74 years)** in
  industrialized countries. `[ESTABLISHED]`
- Prevalence is strongly duration-dependent: in T1DM, DR is near-universal
  (**>90%**) after 20 years; in T2DM, **~60%** at 20 years but **~20–30% already have DR
  at the moment of T2DM diagnosis** because of the long pre-diagnostic hyperglycemic
  window. `[ESTABLISHED]` — *This last fact is strategically central: a large fraction of
  T2DM patients enter care with retinal disease already underway, so any agent that only
  prevents incident disease addresses a smaller market than one that halts progression.*
- Incidence of **PDR** in the modern treatment era has fallen substantially relative to
  historical cohorts, attributed to better systemic risk-factor control. The residual
  burden has shifted toward **DME and chronic, repeatedly-treated maculopathy**.
  `[CURRENT CONSENSUS]`

### 1.3 Morbidity and burden

- Vision loss trajectory: contrast sensitivity and color discrimination decline before
  Snellen acuity; central acuity loss from DME is usually gradual, whereas PDR can cause
  **sudden** loss via vitreous hemorrhage or tractional detachment. `[ESTABLISHED]`
- DR independently predicts **systemic** outcomes: presence and severity of DR associate
  with incident nephropathy, cardiovascular events, stroke and all-cause mortality.
  The retina is a visible readout of generalized microvascular disease.
  `[CURRENT CONSENSUS]`
- Quality-of-life impact is large and under-measured: loss of driving, reading, and
  independent living; depression prevalence roughly doubles; treatment itself (repeat
  intravitreal injection) carries meaningful anxiety and time burden.
  `[CURRENT CONSENSUS]`

### 1.4 Subtypes and how the biology differs

| Subtype | Defining features | Dominant biology | Why it matters for drug scoring |
|---|---|---|---|
| **Preclinical / subclinical DR** (diabetic retinal neurodegeneration, DRN) | No visible lesions; abnormal mfERG implicit times, reduced pattern ERG, GCL-IPL and RNFL thinning on OCT, blunted flicker-induced vasodilation | Neuroretinal apoptosis, Müller glial activation, loss of neurovascular coupling, microglial priming | **Zero approved therapy.** The single largest unmet need. Only a systemic/oral agent is deployable here. |
| **Mild NPDR** | Microaneurysms only | Pericyte dropout, basement-membrane thickening, early inner-BRB loosening | Target: pericyte survival, AR/polyol flux, PKCβ |
| **Moderate NPDR** | MAs + dot-blot hemorrhages, hard exudates, cotton-wool spots | Leukostasis, capillary occlusion begins, inflammatory amplification, lipoprotein extravasation | Target: ICAM1/integrin leukostasis, inflammasome, lipid handling |
| **Severe NPDR** | 4-2-1 rule (hemorrhages in 4 quadrants, venous beading in 2, IRMA in 1) | **Ischemic switch**: widespread capillary nonperfusion → HIF stabilization | Target: HIF/VEGF axis, capillary preservation. High-value prevention point. |
| **PDR** | Retinal/disc neovascularization, preretinal/vitreous hemorrhage | Pathological angiogenesis on a vitreous scaffold; VEGF + Ang2 + plasma kallikrein | Anti-VEGF and PRP already effective — lower unmet need, but non-responders exist |
| **DME (center-involving vs non-CI)** | Retinal thickening at/near fovea | Inner **and** outer BRB failure, Müller cell swelling, VEGF-dependent **and** VEGF-independent permeability | The commercial and clinical centre of gravity. ~40% incomplete responders. |
| **— DME, exudative/lipid phenotype** | Hard exudate plaques, circinate rings, often subfoveal lipid | Lipoprotein extravasation + intraretinal lipid modification; associates with dyslipidemia | **Directly addressed by the lipid axis (Section 2.P8).** Hard exudate is poorly responsive to anti-VEGF and causes permanent subfoveal fibrosis. |
| **— DME, inflammatory phenotype** | Hyperreflective foci, subretinal fluid, high vitreous IL-6/MCP-1 | Cytokine/inflammasome-driven permeability | Steroid-responsive, anti-VEGF-suboptimal |
| **— DME, ischemic/mixed** | DRIL, enlarged FAZ, macular nonperfusion | Capillary dropout in the perifoveal arcade | **No therapy exists.** Anti-VEGF may worsen perfusion in some eyes. |
| **Diabetic macular ischemia (DMI)** | FAZ enlargement, perifoveal capillary loss on OCT-A | Irreversible capillary and neuronal loss | **No therapy.** Major unmet need. |
| **Advanced / tractional disease** | Fibrovascular proliferation, tractional RD, neovascular glaucoma | Angio-fibrotic switch: TGFβ/CTGF dominance after VEGF withdrawal | Surgical domain; pharmacology mostly failed here |

**Disease category:** chronic metabolic–microvascular–neuroinflammatory complication.
For scoring purposes treat DR as a **three-component disease** — vascular, neural, and
glial/metabolic — not a pure angiogenesis disease. Anti-angiogenesis addresses the late
vascular component only.

---

## 2. Pathobiology Model

### 2.0 Chosen structure — and why

**I use a three-axis hybrid model.**

- **Axis A — Clinical stage (S0 → S5).** DR has a genuinely validated clinical staging
  system (ETDRS / ICDR severity scale) that predicts progression and is what trials
  enroll and endpoint against (the ≥2-step or ≥3-step DRSS change). A model that ignores
  stage cannot speak to trial design. `[ESTABLISHED]`
- **Axis B — Pathway modules (P1 → P9).** The biochemical drivers are *concurrent, not
  sequential*. Polyol flux, AGE/RAGE, PKC, hexosamine and oxidative stress all run from
  day one of hyperglycemia and all persist through PDR. Assigning a pathway to a single
  stage would be biologically false. `[ESTABLISHED]`
- **Axis C — Anatomical compartment.** Inner BRB (retinal capillary endothelium +
  pericyte + glial sheath), outer BRB (RPE/Bruch's), neural retina, and the
  vitreoretinal interface each fail by different mechanisms and have different drug
  access. A target's value depends on which compartment it sits in. `[ESTABLISHED]`

**Why a pure stage model fails:** it hides the fact that the same pathway (e.g. lipid
handling) manifests as hard exudate at S2 and as photoreceptor membrane failure at S0.
**Why a pure pathway model fails:** it cannot tell a downstream agent *when* to
intervene or what endpoint to measure. The hybrid lets a scoring agent ask the two
questions that actually matter: *which pathway does this compound hit* and *at which
clinical stage would that pathway's inhibition change the trajectory*.

Each downstream agent should score a candidate as a **(pathway, stage, compartment)**
triple. A compound hitting P8/lipid at S0–S2 in the neural+outer-BRB compartment via
oral dosing is a fundamentally different asset from a compound hitting P7/VEGF at S4 in
the inner-BRB compartment via intravitreal dosing — even if both "treat DR".

---

### Axis A — Clinical stage model

#### S0 — Preclinical diabetic retinal neurodegeneration

**Status: `[CURRENT CONSENSUS]` that it exists and precedes microangiopathy;
`[EMERGING]` on whether it is causal for later vascular disease or parallel.**

Biology:
- **Retinal ganglion cell (RGC) and amacrine cell apoptosis** begins within months–years
  of hyperglycemia, before any ophthalmoscopically visible lesion. Mechanism: loss of
  constitutive insulin/IRS-1→PI3K→AKT survival signaling in the retina, shift in
  BAX:BCL2 ratio, CASP3 and CASP9 activation, PARP activation. `[CURRENT CONSENSUS]`
- **Müller cell (the principal retinal macroglia) reactive gliosis**: GFAP
  upregulation — the earliest and most reproducible marker in diabetic retina.
  Functional consequences: (i) loss of **glutamine synthetase (GLUL)** → glutamate
  accumulation → NMDA-receptor excitotoxicity of RGCs; (ii) loss of glutamate
  transporter **SLC1A3 (GLAST)**; (iii) **Kir4.1 (KCNJ10)** channel mislocalization from
  endfeet → loss of spatial potassium buffering → osmotic Müller swelling; (iv) **AQP4**
  polarity loss → failure of water clearance. The Kir4.1/AQP4 uncoupling is the
  mechanistic bridge from gliosis to **cytotoxic (cellular) edema**, which is distinct
  from and additive to vasogenic (leak-driven) edema. `[CURRENT CONSENSUS]`
- **Loss of neurovascular coupling**: flicker-light-induced retinal arteriolar
  dilation is blunted in diabetes before lesions appear. This is a functional
  readout of the Müller–endothelium–pericyte unit and depends on NO (NOS3/NOS1),
  EETs and K+ signalling. It is a **clinically measurable early endpoint**.
  `[CURRENT CONSENSUS]`
- **Microglial activation**: ramified → amoeboid transition, migration to the outer
  retina, release of TNF, IL1B, CCL2. Microglia are the inflammatory amplifier that
  converts metabolic stress into vascular injury. `[CURRENT CONSENSUS]`
- **Loss of endogenous neuroprotective tone**: retinal **somatostatin (SST)** and
  **PEDF (SERPINF1)** — both constitutively produced by the RPE/neuroretina and both
  anti-angiogenic and neuroprotective — fall early in diabetes. This is a *loss-of-brake*
  mechanism distinct from gain-of-VEGF. `[EMERGING]`

**Targets — S0**

| Target | Role in S0 | Therapeutic direction |
|---|---|---|
| GLUL (glutamine synthetase) | Lost in Müller cells → glutamate excitotoxicity | Inducer / activity preservation |
| SLC1A3 (GLAST) | Glutamate reuptake, downregulated | Inducer |
| GRIN1/GRIN2B (NMDAR) | Mediates excitotoxic RGC death | Antagonist (low-affinity, use-dependent) |
| KCNJ10 (Kir4.1) | K+ buffering; mislocalized → Müller swelling | Activator / localization restorer |
| AQP4 | Water clearance; depolarized | Modulator (direction context-dependent) |
| SERPINF1 (PEDF) | Lost neuroprotective + anti-angiogenic brake | Inducer / replacement |
| SST / SSTR2 | Lost neuroprotective peptide tone | Agonist |
| BDNF / NTRK2 | Neurotrophic support of RGC | Agonist / inducer |
| GLP1R | Expressed in retina; neuroprotective signalling | Agonist `[EMERGING]` |
| CASP3, CASP9, BAX | Executioner apoptosis in RGC | Inhibitor (CASP), antagonist (BAX) |
| BCL2 | Survival counterweight | Inducer |
| SIRT1 | NAD+-dependent deacetylase; lost in diabetic retina; governs NFKB1 and PGC1A | Activator |
| PRKAA1/2 (AMPK) | Energy sensor; suppressed; upstream of SIRT1, PGC1A, FAO | Activator |

**Current therapy at S0:** **none.** Systemic glycemic control is the only intervention
and it is risk-factor management, not retinal therapy. **This is the single largest
therapeutic gap in the disease.**

**Gaps:** no neuroprotective agent; no agent given at this stage at all; endpoints are
not regulatorily qualified (DRSS cannot move from a stage with no lesions — trials would
need ERG/OCT-layer-thickness/neurovascular-coupling endpoints, which regulators have not
accepted). *A downstream regulatory-strategy agent should treat S0 as high-value but
high-endpoint-risk.*

---

#### S1 — Mild NPDR (microaneurysms only)

Biology:
- **Pericyte dropout** is the classic first structural lesion `[ESTABLISHED]`. Retinal
  capillaries have the **highest pericyte:endothelial ratio in the body (~1:1)**, so
  they are uniquely vulnerable to pericyte loss. Mechanisms: (i) loss of
  **PDGFB→PDGFRB** survival signalling from endothelium to pericyte; (ii) **ANGPT2**
  antagonism of **TEK/TIE2**, which destabilizes pericyte–endothelial adhesion and
  primes endothelium for VEGF responsiveness; (iii) polyol/AGE-driven apoptosis;
  (iv) ceramide-mediated apoptosis (see P8). `[CURRENT CONSENSUS]`
- **Microaneurysm** = focal outpouching of a capillary that has lost pericyte support.
  MAs are leaky and are the quantitative substrate of the "MA turnover rate" biomarker.
  `[ESTABLISHED]`
- **Basement membrane thickening**: accumulation of fibronectin, collagen IV, laminin
  with reduced turnover, driven by TGFB1 and hyperglycemic ECM gene induction.
  Thickened BM impairs pericyte–endothelial contact and paracrine signalling and alters
  drug diffusion. `[ESTABLISHED]`
- **First inner-BRB loosening is partly VEGF-independent**: PKCβ phosphorylates
  **occludin (OCLN)** at Ser490, triggering its ubiquitination and removal from the tight
  junction, and redistributes **ZO-1 (TJP1)**; **CLDN5** is transcriptionally
  downregulated. `[CURRENT CONSENSUS]`
- **Loss of retinal autoregulation**: the retina normally autoregulates blood flow
  independent of systemic pressure. Diabetes abolishes this, so systemic blood-pressure
  excursions are transmitted directly to capillaries. This is the mechanistic reason
  blood-pressure control matters for DR. `[ESTABLISHED]`

**Targets — S1**

| Target | Role | Direction |
|---|---|---|
| PDGFB / PDGFRB | Pericyte recruitment & survival; lost | Agonist / inducer (note: PDGF *inhibition* was tried for other reasons and failed — see §4) |
| ANGPT2 | Destabilizes Tie2, detaches pericytes, sensitizes to VEGF | Antagonist |
| TEK (TIE2) | Vessel stabilization | Agonist (direct, or via PTPRB/VE-PTP inhibition) |
| PTPRB (VE-PTP) | Dephosphorylates and silences Tie2 | Inhibitor |
| AKR1B1 (aldose reductase) | Highly expressed in pericytes; polyol-driven pericyte death | Inhibitor |
| PRKCB (PKCβ) | Phosphorylates occludin, drives permeability + abnormal flow | Inhibitor |
| CLDN5, OCLN, TJP1 | Tight-junction integrity | Inducer / stabilizer |
| TGFB1 | BM thickening | Antagonist (dose-careful; TGFβ is also homeostatic) |

**Current therapy at S1:** observation + systemic risk-factor control (glycemic, blood
pressure, lipid control, at class-of-intervention level). No ocular therapy is indicated.
**Gap:** nothing halts progression S1→S2.

---

#### S2 — Moderate NPDR (leukostasis and the inflammatory amplifier)

Biology:
- **Leukostasis** `[ESTABLISHED]` — the best-validated inflammatory mechanism in DR.
  Diabetic retinal endothelium upregulates **ICAM1** (and VCAM1, P/E-selectin);
  circulating neutrophils and monocytes upregulate **CD11a/CD18 (ITGAL/ITGB2)**. The
  resulting firm adhesion physically plugs capillaries whose lumen is barely wider than
  a leukocyte. Two consequences: (i) **transient and then permanent capillary
  nonperfusion**; (ii) **FAS/FASLG-mediated endothelial apoptosis** by the adherent
  leukocyte. ICAM1 or CD18 blockade (or knockout) prevents both leukostasis and BRB
  breakdown in animal models — this is one of the cleanest causal chains in the field.
- **Acellular capillaries** (basement-membrane tubes with neither endothelium nor
  pericyte) are the histological endpoint and the quantitative substrate of ischemia.
  `[ESTABLISHED]`
- **Cytokine milieu**: vitreous and aqueous from DR patients show elevated **IL6, IL8
  (CXCL8), CCL2/MCP-1, TNF, IL1B, VEGFA, ANGPT2, ICAM1**, and complement components.
  IL-6 and MCP-1 correlate with DME severity and with anti-VEGF non-response.
  `[CURRENT CONSENSUS]`
- **NLRP3 inflammasome** in Müller cells, microglia and RPE: activated by hyperglycemia,
  AGEs, oxidized lipids and ATP via P2X7; caspase-1 cleaves pro-IL-1β → mature IL1B,
  which acts back on Müller cells in an autocrine amplification loop and on endothelium
  to increase permeability. `[EMERGING → CURRENT CONSENSUS]`
- **Hard exudate formation begins** — see P8. Clinically visible lipid is the signature
  of S2.
- Cotton-wool spots = nerve fibre layer infarcts from precapillary arteriolar occlusion
  (axoplasmic stasis). `[ESTABLISHED]`

**Targets — S2**

| Target | Role | Direction |
|---|---|---|
| ICAM1 | Endothelial leukocyte adhesion → capillary plugging | Antagonist / expression inhibitor |
| ITGB2 / ITGAL (CD18/CD11a) | Leukocyte counter-receptor | Antagonist |
| SELE / SELP / VCAM1 | Rolling and adhesion | Antagonist |
| TNF | Drives ICAM1, permeability, apoptosis | Antagonist |
| IL1B / NLRP3 / CASP1 / P2RX7 | Inflammasome amplification | Inhibitor |
| IL6 / IL6R | Permeability, anti-VEGF resistance marker | Antagonist |
| CCL2 / CCR2 | Monocyte recruitment | Antagonist |
| NFKB1 / RELA | Master transcriptional hub for all of the above | Inhibitor |
| FAS / FASLG | Leukocyte-mediated endothelial apoptosis | Antagonist |
| PTGS2 | PGE2 → permeability, VEGF induction | Inhibitor |
| ALOX5 / LTA4H | LTB4 → leukocyte chemotaxis and adhesion | Inhibitor |

**Current therapy at S2:** still observation + systemic risk-factor control; treat DME if
present. **Gap:** no anti-inflammatory agent is approved for NPDR; intravitreal steroid
is effective against inflammation but cannot be given prophylactically for years because
of cataract and IOP.

---

#### S3 — Severe NPDR / the ischemic switch

Biology:
- Accumulated acellular capillaries cross a threshold and produce **confluent capillary
  nonperfusion**, best seen on ultra-widefield FA as peripheral nonperfusion.
  `[ESTABLISHED]`
- **HIF1A stabilization**: under normoxia, prolyl hydroxylases (EGLN1/2/3) hydroxylate
  HIF-1α, enabling VHL-mediated degradation. Hypoxia (and, importantly,
  **pseudohypoxia** from NADH/NAD+ imbalance due to polyol flux, plus ROS and
  methylglyoxal) inhibits this, so HIF-1α accumulates and transactivates **VEGFA,
  ANGPT2, EPO, SLC2A1, CXCL12/SDF-1, LOX, PDK1**. `[ESTABLISHED]`
- Severe NPDR carries a high short-term risk of conversion to PDR; this is the stage
  where DRSS-based trials show the largest treatable effect.
- Note the coupling: **ischemia is produced by inflammation (leukostasis) and produces
  angiogenesis (VEGF)**. Anti-VEGF given here suppresses the output without repairing
  the capillary bed — perfusion does not return. `[CURRENT CONSENSUS]`

**Targets — S3**

| Target | Role | Direction |
|---|---|---|
| HIF1A | Master hypoxia transcription factor | Inhibitor (translational or stabilization-blocking) |
| EGLN1/2/3 (PHD) | HIF degradation control | **Context-dependent**: PHD inhibition *raises* HIF — undesirable in retina despite being beneficial in anemia. Flag as a liability for any PHD inhibitor. |
| EPAS1 (HIF2A) | Endothelial-biased hypoxia TF | Inhibitor |
| VEGFA | Principal HIF output | Antagonist |
| ANGPT2 | Co-output; destabilizes vessels | Antagonist |
| SLC2A1 (GLUT1) | HIF output; also the inner-BRB glucose transporter — paradoxically *downregulated* in diabetic retina, worsening neuronal fuel supply | Context-dependent `[UNCERTAIN]` |
| CXCL12 / CXCR4 | Recruits bone-marrow-derived endothelial progenitors to neovascular sites | Antagonist |

**Current therapy at S3:** anti-VEGF (modality) can regress DRSS severity by ≥2 steps in
a substantial fraction; PRP may be considered in high-risk patients. **Gap:** no therapy
*reperfuses* nonperfused retina. Reperfusion is arguably the field's holy grail.

---

#### S4 — Proliferative DR

Biology:
- **Retinal neovascularization** sprouts from venules at the junction of perfused and
  nonperfused retina (NVD at the disc, NVE elsewhere), breaches the internal limiting
  membrane, and grows **on the posterior hyaloid face** — the vitreous provides the
  physical scaffold, which is why vitreous detachment or vitrectomy is protective.
  `[ESTABLISHED]`
- New vessels are **pericyte-poor and tight-junction-poor** → they leak profusely and
  bleed on vitreoretinal traction → preretinal and vitreous hemorrhage. `[ESTABLISHED]`
- **VEGF-independent permeability and hemorrhage via the kallikrein–kinin system**:
  plasma prekallikrein (**KLKB1**) and Factor XII (**F12**) extravasate into the
  vitreous, are activated, and generate bradykinin acting on **BDKRB1/BDKRB2** →
  vasodilation, permeability, and hemorrhage. Vitreous kallikrein activity is elevated in
  DR and this pathway is **not** blocked by anti-VEGF — a leading explanation for the
  anti-VEGF non-responder fraction. `[EMERGING → CURRENT CONSENSUS]`
- **MMP2/MMP9** degrade the ILM and vascular basement membrane, enabling sprouting;
  MMP9 also degrades tight junctions directly (occludin cleavage). `[CURRENT CONSENSUS]`
- **Erythropoietin (EPO)** is markedly elevated in PDR vitreous and is angiogenic
  independent of VEGF. `[CURRENT CONSENSUS]`
- **Neovascular glaucoma** occurs when VEGF diffuses anteriorly and drives iris/angle
  neovascularization — a blinding, painful endpoint.

**Targets — S4**

| Target | Role | Direction |
|---|---|---|
| VEGFA / KDR (VEGFR2) | Principal angiogenic driver and permeability signal | Antagonist / inhibitor |
| FLT1 (VEGFR1) | Decoy and monocyte-recruiting receptor; soluble sFlt-1 is a natural sink | Agonist of the decoy function / antagonist of monocyte arm — context-dependent |
| PGF (PlGF) | FLT1 ligand; inflammatory angiogenesis | Antagonist |
| ANGPT2 / TEK | Vessel destabilization vs stabilization | Antagonist / agonist |
| KLKB1, F12, BDKRB1, BDKRB2 | VEGF-independent permeability & hemorrhage | Inhibitor / antagonist |
| MMP9, MMP2 | ECM/ILM degradation, junction cleavage | Inhibitor |
| EPO / EPOR | VEGF-independent angiogenesis in PDR vitreous | Antagonist (but EPO is neuroprotective at low dose — **biphasic, flag carefully**) `[UNCERTAIN]` |
| NOTCH1 / DLL4 | Tip/stalk cell specification | Modulator |
| ROCK1/2 | Endothelial cytoskeleton, leukostasis, permeability | Inhibitor |

**Current therapy at S4:** intravitreal anti-VEGF and/or panretinal photocoagulation
(PRP); vitrectomy for non-clearing hemorrhage. **Both work.** This is the lowest-unmet-
need stage.

---

#### S5 — Fibrovascular proliferation and tractional sequelae

Biology:
- **The angio-fibrotic switch** `[CURRENT CONSENSUS]`: as VEGF drive falls (naturally, or
  after anti-VEGF), the neovascular membrane's balance shifts to **TGFB1 → CTGF/CCN2**
  dominance, myofibroblast transdifferentiation (endothelial-to-mesenchymal transition,
  EndMT), and collagen deposition. The membrane contracts, exerting tangential and
  anteroposterior traction → **tractional retinal detachment**.
- Clinically this produces the **"crunch" phenomenon**: rapid anti-VEGF-induced
  contraction of a fibrovascular membrane precipitating detachment — an *iatrogenic*
  consequence of effective anti-angiogenesis. Any new anti-VEGF-class agent inherits
  this liability. `[ESTABLISHED]`
- **SERPINE1 (PAI-1)** suppresses fibrinolysis, stabilizing the fibrin scaffold of the
  membrane. `[CURRENT CONSENSUS]`

**Targets — S5**

| Target | Role | Direction |
|---|---|---|
| TGFB1 / TGFBR1 (ALK5) | Fibrotic master switch, EndMT | Antagonist / inhibitor |
| CTGF (CCN2) | TGFβ effector; ratio CTGF:VEGF predicts fibrosis | Antagonist |
| SERPINE1 (PAI-1) | Fibrin scaffold stabilization | Inhibitor |
| LOX / LOXL2 | Collagen crosslinking, membrane stiffening | Inhibitor |
| ROCK1/2 | Myofibroblast contraction | Inhibitor |
| SMAD3 | TGFβ transcriptional arm | Inhibitor |

**Current therapy at S5:** pars plana vitrectomy with membrane delamination ± endolaser;
pharmacology has essentially nothing. **Gap:** no anti-fibrotic is approved for the eye.

---

#### DME — the cross-cutting complication

DME is **not a stage**; it is a failure mode that can appear at S1–S5.

**Inner BRB failure (vasogenic/paracellular):**
VEGFA → KDR → SRC/YES1 → phosphorylation of **VE-cadherin (CDH5)** at Y658/Y685 →
internalization of adherens junctions; parallel **PRKCB**-mediated occludin Ser490
phosphorylation and **CLDN5** transcriptional repression (via FOXO1/β-catenin). Also
**transcellular** leak via increased caveolin-1 (CAV1)-dependent vesicular transcytosis
and **PLVAP** induction (acquired fenestration-like phenotype). `[CURRENT CONSENSUS]`
— *The transcellular component is often forgotten and may explain leak persisting after
tight junctions are pharmacologically restored.* `[EMERGING]`

**Outer BRB failure:**
The RPE is the outer barrier and an active pump moving fluid from retina → choroid via
**ATP1A1 (Na/K-ATPase)**, **AQP1**, **CFTR/bestrophin** chloride transport and the
**SLC16A/MCT** lactate-coupled flux. Diabetes impairs RPE tight junctions (CLDN19,
OCLN, TJP1) and pump capacity, producing **subretinal fluid** — a DME feature that is
relatively anti-VEGF-resistant and steroid-responsive. `[EMERGING → CURRENT CONSENSUS]`

**Cytotoxic (cellular) edema:** Müller cell swelling from Kir4.1/AQP4 uncoupling
(see S0). This component is invisible to anti-permeability drugs entirely, and is a
plausible contributor to the ~40% incomplete-response fraction. `[EMERGING]`

**DRIL (disorganization of retinal inner layers)** on OCT is the imaging correlate of
inner-retinal (Müller/bipolar/amacrine) architectural failure and is the strongest
single OCT predictor of poor visual outcome in DME. It marks the neural, not vascular,
component. `[CURRENT CONSENSUS]`

---

### Axis B — Concurrent pathway modules

> All of P1–P5 are **unified by the Brownlee hypothesis** `[ESTABLISHED]`:
> hyperglycemia-driven mitochondrial electron-transport-chain superoxide overproduction
> inhibits **GAPDH** (via PARP-mediated poly-ADP-ribosylation), backing up glycolytic
> intermediates into the polyol, hexosamine, AGE and PKC branches simultaneously.
> **Strategic consequence: blocking one branch downstream is leaky; blocking the
> upstream ROS node, or restoring the antioxidant/NRF2 arm, hits all four.**

---

#### P1 — Polyol / aldose reductase pathway

`[ESTABLISHED]` mechanism; `[UNCERTAIN]` clinical translatability.

Under hyperglycemia, hexokinase saturates and glucose enters the polyol pathway:
**AKR1B1 (aldose reductase)** reduces glucose → sorbitol (consuming NADPH), then
**SORD (sorbitol dehydrogenase)** oxidizes sorbitol → fructose (producing NADH).
Four consequences: (i) **NADPH depletion** → glutathione reductase cannot regenerate
GSH → collapse of the main retinal antioxidant buffer; (ii) **sorbitol osmotic stress**
in pericytes and lens; (iii) **NADH/NAD+ ratio rise = "pseudohypoxia"** → stabilizes
HIF1A even without true ischemia and inhibits GAPDH; (iv) **fructose → fructose-3-
phosphate → 3-deoxyglucosone**, a potent AGE precursor, linking P1 directly to P2.

AKR1B1 is highly expressed in **retinal pericytes, Müller cells and the lens**, which is
why the polyol pathway has outsized relevance in exactly the cells that die first.

| Target | Role | Direction |
|---|---|---|
| AKR1B1 | Rate-limiting; NADPH drain, sorbitol, pseudohypoxia | **Inhibitor** |
| SORD | NADH generation, fructose production | Inhibitor `[UNCERTAIN]` — may worsen sorbitol accumulation |
| AKR1B10 | Paralog; off-target liability for AR inhibitors | Selectivity consideration |
| GSR / G6PD | NADPH-dependent GSH regeneration | Inducer |

*Note for downstream agents:* aldose-reductase inhibition has a long and largely
disappointing clinical history in diabetic complications. Treat AKR1B1 activity in a
candidate as **supportive but not sufficient** evidence.

---

#### P2 — AGE / RAGE axis

`[ESTABLISHED]`

Non-enzymatic glycation of long-lived proteins, accelerated by dicarbonyls
(**methylglyoxal**, glyoxal, 3-deoxyglucosone), produces advanced glycation end-products
(CML, pentosidine, MG-H1). Two arms:
1. **Structural**: crosslinking of collagen IV and laminin in the capillary basement
   membrane → stiffening, thickening, impaired pericyte adhesion. Irreversible.
2. **Receptor-mediated**: **AGER (RAGE)** on endothelium, pericytes, Müller cells and
   microglia. RAGE is a pattern-recognition receptor with multiple ligands relevant
   here — AGEs, **S100 proteins, HMGB1, and amyloid/oxidized lipid species**. RAGE
   ligation → NADPH oxidase (NOX1/2/4) activation → ROS → NFKB1 → ICAM1, VCAM1, TNF,
   IL6, VEGFA. RAGE also **upregulates itself** via NF-κB, creating a feed-forward loop.

**GLO1 (glyoxalase-1)** is the principal methylglyoxal detoxifier; its activity falls in
diabetes and GLO1 overexpression is protective in models. GLO1 is **NRF2-inducible**,
tying P2 to P5.

| Target | Role | Direction |
|---|---|---|
| AGER (RAGE) | Signal transducer of AGE/S100/HMGB1 | **Antagonist** |
| GLO1 | Methylglyoxal detoxification; depressed in diabetes | **Inducer / activator** |
| HMGB1 | RAGE/TLR4 alarmin released by stressed retina | Antagonist |
| S100B | Müller-derived RAGE ligand | Antagonist |
| NOX1/NOX2 (CYBB)/NOX4 | ROS generation downstream of RAGE | Inhibitor |
| TLR4 | Parallel innate receptor for the same alarmins | Antagonist |

AGE formation itself can be blocked by **dicarbonyl scavenging** and **transition-metal
chelation** — a mechanism many polyphenols possess and a legitimate route for a
natural-product candidate to engage P2 without being a classical receptor antagonist.
`[CURRENT CONSENSUS]`

---

#### P3 — Protein kinase C (notably PKCβ)

`[ESTABLISHED]` mechanistically; `[CURRENT CONSENSUS]` that isolated PKCβ inhibition is
insufficient clinically.

Glycolytic backup raises dihydroxyacetone phosphate → glycerol-3-phosphate →
**de novo diacylglycerol (DAG)** synthesis, which activates conventional PKC isoforms,
predominantly **PRKCB (PKCβ1/β2)** in vascular tissue, with **PRKCD** contributing to
pericyte apoptosis via SHP-1/PDGFRβ dephosphorylation.

Downstream effects — unusually broad for one node:
- Phosphorylates **occludin Ser490** → tight junction disassembly → permeability
- Induces **VEGFA** and potentiates **KDR** signalling
- Activates **NFKB1** → ICAM1/leukostasis
- Increases **EDN1** (endothelin-1) and decreases **NOS3**-derived NO → vasoconstriction,
  abnormal retinal blood flow (an early, measurable DR abnormality)
- Induces **TGFB1**, **SERPINE1**, fibronectin → BM thickening
- Activates NADPH oxidase

DAG is also generated from **lipid sources** (PLD/PLC action on membrane phospholipids),
so P3 is a direct mechanistic bridge between the **lipid axis (P8)** and classical
hyperglycemic signalling. `[CURRENT CONSENSUS]` — *this bridge is worth flagging: an
agent that normalizes retinal lipid handling can reduce PKC activation without being a
kinase inhibitor.*

| Target | Role | Direction |
|---|---|---|
| PRKCB | Permeability, VEGF, flow, inflammation, fibrosis | **Inhibitor** |
| PRKCD | Pericyte apoptosis via SHP-1/PDGFRβ | Inhibitor |
| PRKCZ | Atypical isoform; tight junction assembly | Modulator |
| DGKA (DAG kinase) | Consumes DAG, terminating signal | Activator |
| EDN1 / EDNRA | Vasoconstriction, capillary closure | Antagonist |
| NOS3 | Vasodilation, NO tone; uncoupled in diabetes (see P5) | Agonist / recoupling |

---

#### P4 — Hexosamine biosynthetic pathway

`[CURRENT CONSENSUS]`

Excess fructose-6-phosphate is shunted via **GFPT1/GFAT** to UDP-GlcNAc, which **OGT**
uses to O-GlcNAcylate serine/threonine residues (removed by **OGA/MGEA5**). In the
diabetic retina, O-GlcNAcylation of **SP1** increases transcription of **TGFB1** and
**SERPINE1**; O-GlcNAcylation of eNOS at Ser1177 (the Akt site) blocks activation,
contributing to NO deficiency; O-GlcNAc modification of mitochondrial and apoptotic
proteins promotes Müller and RGC stress. Hexosamine flux also acts as a nutrient-surplus
sensor that suppresses AMPK/SIRT1 signalling.

| Target | Role | Direction |
|---|---|---|
| GFPT1 (GFAT) | Rate-limiting hexosamine entry | Inhibitor |
| OGT | O-GlcNAc transferase | Inhibitor |
| MGEA5 (OGA) | O-GlcNAc removal | Activator |
| SP1 | O-GlcNAc-sensitive TF driving TGFB1/SERPINE1 | Modulator |

*Druggability caution:* OGT/OGA are globally pleiotropic; systemic inhibition is likely
toxic. Rate this pathway **mechanistically important, pharmacologically unattractive**
for a systemic agent.

---

#### P5 — Oxidative and nitrosative stress; the NRF2 axis

`[ESTABLISHED]`

The retina is exceptionally vulnerable: highest oxygen consumption per gram of any
tissue, intense light exposure, and the most polyunsaturated membrane lipid composition
in the body — i.e. maximal substrate for lipid peroxidation (ties directly to P8).

Sources of ROS/RNS in diabetic retina:
- Mitochondrial complex I/III superoxide from substrate overload `[ESTABLISHED]`
- **NADPH oxidases** NOX1, NOX2 (CYBB, microglia/leukocytes), NOX4 (endothelium)
- **Uncoupled NOS3**: BH4 (tetrahydrobiopterin) oxidation and L-arginine depletion by
  upregulated **ARG1/ARG2** cause eNOS to produce superoxide instead of NO — converting
  a protective enzyme into a damaging one. Superoxide + NO → **peroxynitrite** →
  protein nitrotyrosine, mitochondrial damage, PARP activation. `[CURRENT CONSENSUS]`
- **NOS2 (iNOS)** induction in Müller cells and microglia — high-output NO
- Xanthine oxidase (**XDH**) and myeloperoxidase (**MPO**) from recruited leukocytes

Antioxidant defence is simultaneously impaired:
- **SOD2 (MnSOD)** activity falls; the *SOD2* promoter becomes **epigenetically silenced**
  (H3K9me, DNMT1-mediated methylation) in diabetic retina — a core part of
  **"metabolic memory"**, the phenomenon where retinopathy continues to progress for
  years after glycemia is normalized. `[CURRENT CONSENSUS]`
- **CAT**, **GPX1**, **GSR** and the GSH pool all fall (NADPH drain from P1)
- **NFE2L2 (NRF2)** — the master antioxidant transcription factor — shows *impaired
  nuclear translocation* in diabetic retina despite normal or raised total protein,
  because **KEAP1** binding is increased and Nrf2's partner machinery is disrupted.
  NRF2 drives **HMOX1, NQO1, GCLC/GCLM, GSR, TXN, SRXN1, GLO1**, and also
  anti-inflammatory programs by directly repressing *IL6*/*IL1B* transcription.
  `[CURRENT CONSENSUS]`
- **Mitochondrial dysfunction and mtDNA damage**: damaged mtDNA D-loop, reduced
  POLG-mediated repair, impaired **TFAM**-driven biogenesis, fragmented mitochondria
  (DRP1/FIS1 up, MFN2/OPA1 down), defective mitophagy. Damaged mitochondria produce
  more ROS — a self-sustaining loop that persists after euglycemia (metabolic memory).
  `[CURRENT CONSENSUS]`

| Target | Role | Direction |
|---|---|---|
| NFE2L2 (NRF2) | Master antioxidant/anti-inflammatory TF; functionally deficient | **Activator / inducer** (via KEAP1 inhibition) |
| KEAP1 | NRF2 repressor | Inhibitor |
| SOD2 | Mitochondrial superoxide dismutation; epigenetically silenced | Inducer / mimetic |
| CAT, GPX1, GSR, TXN | Peroxide clearance | Inducer |
| HMOX1, NQO1, GCLC | NRF2 effectors | Inducer |
| NOX1, CYBB (NOX2), NOX4 | ROS generation | Inhibitor |
| NOS2 | High-output NO → peroxynitrite | Inhibitor |
| NOS3 | Protective NO when coupled; damaging when uncoupled | **Recoupling** (BH4 repletion, GCH1 induction) |
| ARG2 | L-arginine depletion → eNOS uncoupling | Inhibitor |
| PARP1 | Consumes NAD+, inhibits GAPDH, drives inflammation | Inhibitor |
| SIRT1 | NAD+-dependent; deacetylates NRF2, FOXO, NFKB, PGC1A | Activator |
| PPARGC1A (PGC-1α) | Mitochondrial biogenesis and antioxidant program | Inducer |
| DNMT1 / HDACs | Mediate SOD2 silencing and metabolic memory | Inhibitor `[EMERGING]` |

---

#### P6 — Inflammation and leukostasis

Detailed under S2. Summary framing for scoring: DR is now understood as a
**low-grade chronic inflammatory disease of the retina** `[CURRENT CONSENSUS]`, in which
the inflammation is **para-inflammatory** (resident-cell-driven, Müller + microglia +
RPE) rather than classically immune. Clinical proof: intravitreal corticosteroid — a
broad, non-VEGF-targeted anti-inflammatory modality — is effective in DME, including
in some anti-VEGF non-responders. That is the strongest clinical validation that a
non-angiogenic mechanism carries real therapeutic weight in this disease.

Key hub: **NFKB1/RELA**, which integrates RAGE, TLR4, PKC, ROS and cytokine receptor
inputs and outputs ICAM1, VCAM1, TNF, IL1B, IL6, NOS2, PTGS2, MMP9 and VEGFA.
NF-κB is counter-regulated by **SIRT1** (deacetylates RelA K310), **NFE2L2**, and
**PPARA/PPARG** (transrepression). *This is the mechanistic basis for the claim that a
PPARα agonist is simultaneously a metabolic and an anti-inflammatory agent.*

Complement: **C3, C5, CFB, C5aR1** and reduced CD55/CD59 regulation are reported in
diabetic retina and in DR vitreous. `[EMERGING]`

---

#### P7 — VEGF / HIF angiogenic and permeability axis

Detailed under S3/S4. Framing for scoring:
- **VEGFA is both an angiogenic and a permeability factor**, and the permeability
  function is operative long before neovascularization — it is the principal validated
  driver of DME. `[ESTABLISHED]`
- VEGFA signalling in retina is mostly via **KDR (VEGFR2)** → PLCγ/PKC, SRC → VE-cadherin,
  and PI3K/AKT/eNOS. **FLT1 (VEGFR1)** has higher affinity but weaker kinase output and
  acts largely as a decoy; soluble FLT1 is an endogenous VEGF sink. **PGF** is a
  FLT1-selective ligand driving inflammatory (monocyte-mediated) angiogenesis.
- **VEGF is also neurotrophic and required for retinal and choriocapillaris
  maintenance.** Chronic complete VEGF suppression is associated with geographic-
  atrophy-like outer retinal and RPE changes and possible macular nonperfusion.
  `[EMERGING]` — a real ceiling on indefinite anti-VEGF therapy and part of why an
  upstream or non-VEGF mechanism is attractive.
- **Redundancy is the clinical problem**: ANGPT2, PGF, EPO, plasma kallikrein, IL-6 and
  prostanoids all drive permeability in parallel. Hence ~40% of DME eyes have an
  incomplete anatomic response to VEGF blockade alone. `[CURRENT CONSENSUS]`

---

#### P8 — Lipid handling, lipoprotein extravasation, hard exudate, and retinal lipid peroxidation

> **This axis is the analytical focus of this run and is under-covered in standard DR
> models. It is developed in more depth than the others deliberately.**

##### P8.1 Lipoprotein extravasation and hard exudate formation `[ESTABLISHED → CURRENT CONSENSUS]`

Hard exudates are **not** "fat deposits". They are **extravasated plasma lipoproteins
and lipoprotein-derived lipid**, together with lipid-laden macrophages, deposited
preferentially in the **outer plexiform layer (Henle fibre layer)** because that is where
the loosely-packed oblique photoreceptor axons offer least resistance to fluid movement.

The sequence:
1. Inner BRB fails (P3/P6/P7) → plasma enters the retinal interstitium.
2. Water and small solutes are cleared relatively efficiently by RPE pumping and by
   Müller cell aquaporin-mediated transport. **ApoB-containing lipoproteins (LDL, VLDL
   remnants, and in particular small dense LDL) are not**: they are large, and once in
   the retina they have no efficient egress route. Lipid therefore **concentrates** as
   water is resorbed.
3. Extravasated lipoproteins are **glycated and oxidized in situ** (the retina's
   oxidative environment, plus AGE chemistry from P2) to **"gly-oxLDL"**, which is far
   more cytotoxic than native LDL.
4. Macrophages and activated microglia take up modified lipoprotein via **CD36, OLR1
   (LOX-1), MSR1/SR-A**, becoming foam cells. They cannot efficiently efflux the
   cholesterol (see P8.3), so they die, releasing their lipid and amplifying
   inflammation.
5. The result is a persistent, slowly-resorbing lipid plaque. **Subfoveal hard exudate
   is the single worst local prognostic sign in DME**: it organizes into a fibrotic
   subretinal plaque causing permanent central scotoma even if the edema is successfully
   dried. `[ESTABLISHED]`

**Clinically critical and often missed:** anti-VEGF therapy dries the retina but does
**not** reliably clear hard exudates, and paradoxical *increase* in exudate has been
described as fluid resorbs and lipid concentrates. **Hard exudate is a therapeutic gap
that the dominant modality does not address.** `[CURRENT CONSENSUS]`

##### P8.2 Modified lipoproteins as direct retinal toxins `[CURRENT CONSENSUS → EMERGING]`

Gly-oxLDL applied to retinal cells produces, at concentrations achievable in diabetic
retina:
- **Pericytes**: apoptosis (the cell type that dies first in DR)
- **Retinal capillary endothelium**: ER stress (**ATF4, ATF6, DDIT3/CHOP, XBP1s**),
  oxidative stress, inflammasome activation, barrier loss
- **Müller cells**: ER stress → **VEGFA** induction, gliosis, inflammatory cytokines
- **RPE**: ER stress, autophagy impairment, lipid droplet accumulation, barrier failure

**This resolves a long-standing clinical paradox.** Plasma LDL cholesterol correlates
only weakly with DR severity, which historically argued against a lipid mechanism. But
the toxic species is not plasma LDL — it is **intraretinal modified LDL**, whose
concentration depends on *barrier permeability × lipoprotein particle number ×
oxidative/glycative modification capacity*, not on plasma cholesterol concentration.
Accordingly, **apoB particle number, LDL particle size (small dense LDL), ApoB:ApoA1
ratio, and triglyceride-rich remnant concentration** track DR and hard exudate better
than LDL-C does. `[CURRENT CONSENSUS]`

*Scoring implication: a candidate that reduces apoB-particle number, reduces remnant
lipoproteins, raises functional HDL/ApoA1, or blocks oxidative modification/uptake of
retained lipoprotein, has a mechanistically coherent path to DR benefit that is
independent of, and additive to, VEGF blockade.*

##### P8.3 Retinal cholesterol handling and reverse cholesterol transport `[EMERGING]`

The retina has both local cholesterol synthesis and uptake, and must export it —
there is no lymphatic drainage. Efflux depends on **ABCA1** and **ABCG1** transferring
cholesterol to **APOA1/APOE** acceptors, under transcriptional control of the liver X
receptors **NR1H3 (LXRα)** and **NR1H2 (LXRβ)**. Side-chain oxidation by **CYP46A1**
(24S-hydroxycholesterol) and **CYP27A1** (27-hydroxycholesterol) generates species that
can cross membranes and also act as LXR ligands.

In diabetes this system fails: ABCA1 and LXR target genes are downregulated in diabetic
retina and in diabetic human donor eyes; cholesterol and cholesterol ester accumulate in
Müller cells, microglia and RPE; LXR agonism restores efflux and reduces retinal
inflammation and neovascularization in models. **ApoA1 mimetic peptides** are protective
in diabetic retinopathy models. `[EMERGING]`

Separately, **Bruch's membrane** accumulates esterified cholesterol and apoB-lipoprotein
with age and with diabetes, impairing outer-BRB transport — a shared mechanism with
age-related macular degeneration.

##### P8.4 Retinal fatty acid composition and VLC-PUFA biology `[EMERGING]`

The retina has the **highest DHA (22:6n-3) content of any human tissue**; photoreceptor
outer segment discs are ~50% DHA by fatty acid. Beyond DHA, photoreceptors synthesize
**very-long-chain PUFAs (≥C28)** via **ELOVL4**, which are essential for disc membrane
curvature and function — *ELOVL4* mutations cause autosomal dominant Stargardt-like
macular dystrophy, which is hard genetic proof that this lipid class is critical to
macular survival. `[ESTABLISHED]` for the genetics; `[EMERGING]` for the DR link.

In diabetes, retinal DHA and VLC-PUFA content falls and the n-6:n-3 ratio shifts toward
arachidonate. Consequences: reduced generation of **specialized pro-resolving mediators**
(resolvins D1/D2, neuroprotectin D1/NPD1, maresins) which actively terminate
inflammation; increased substrate for pro-inflammatory eicosanoids. **Failure of
inflammation *resolution*, not just excess initiation**, is an attractive and
under-exploited framing for DR. `[EMERGING]`

**Mechanistic targets:** ELOVL4 (inducer), FADS1/FADS2 (desaturases), ACSL6 (retinal
DHA-preferring acyl-CoA synthetase), ADIPOR1 (required for retinal DHA uptake/retention;
*Adipor1* loss causes DHA depletion and photoreceptor degeneration — a striking link
between adiponectin signalling and retinal lipid status) `[EMERGING]`.

##### P8.5 Ceramide and sphingolipid signalling `[EMERGING]`

Palmitate-driven de novo ceramide synthesis (**SPTLC1/2 → CERS2/CERS6 → DEGS1**) and
sphingomyelin hydrolysis by acid sphingomyelinase (**SMPD1**) raise retinal ceramide in
diabetes. Ceramide is directly pro-apoptotic in **pericytes and endothelium**, forms
membrane platforms that cluster death receptors, and activates **PP2A → Akt
inactivation**. Acid-sphingomyelinase inhibition and acid-ceramidase (**ASAH1**)
augmentation are protective in diabetic retina models.

The counter-arm, **sphingosine-1-phosphate** (made by **SPHK1/2**, acting on
**S1PR1-3**), is barrier-protective via S1PR1 but pro-permeability and pro-fibrotic via
S1PR2/3 — a receptor-subtype-selective opportunity. `[EMERGING]`

##### P8.6 Eicosanoids and oxylipins `[CURRENT CONSENSUS]`

- **PLA2G4A (cPLA2) / PLA2G2A / PLA2G7 (Lp-PLA2)** liberate arachidonate. **PLA2G7**
  is lipoprotein-associated, travels with LDL, generates lysoPC and oxidized fatty acids
  at sites of lipoprotein retention — i.e. exactly at hard exudates — and is a
  mechanistically attractive node linking P8.1 to inflammation. `[EMERGING]`
- **PTGS2 (COX-2) → PGE2** → EP receptors → permeability and VEGFA induction.
- **ALOX5 + ALOX5AP → LTB4** → leukocyte chemotaxis and adhesion (ties to P6/leukostasis);
  **LTA4H** is the terminal synthase.
- **ALOX12 / ALOX15 → 12-HETE and 15-HETE**: 12/15-lipoxygenase products are among the
  better-validated lipid mediators in DR models — they induce VEGF, cause pericyte loss,
  trigger ER stress in Müller cells, and 12/15-LOX deletion is protective.
  `[EMERGING → CURRENT CONSENSUS]`
- **CYP epoxygenase → EETs** are vasodilatory and barrier-protective; **EPHX2 (soluble
  epoxide hydrolase)** degrades them, so sEH inhibition is protective in several models.
  Note a genuine conflict: in other retinal models sEH-derived products from
  photoreceptor DHA metabolism were implicated in *causing* pericyte loss. Mark as
  **`[UNCERTAIN]` — direction of effect is model-dependent.**

##### P8.7 Lipid peroxidation products as effectors, not just markers `[CURRENT CONSENSUS]`

Because of the retina's PUFA load, peroxidation generates high concentrations of
reactive aldehydes:
- **4-hydroxynonenal (4-HNE)** (n-6 derived) — adducts proteins, inhibits mitochondrial
  enzymes, activates JNK
- **Malondialdehyde (MDA)**, **acrolein** — protein and DNA adducts
- **Carboxyethylpyrrole (CEP)** adducts, formed specifically from **DHA** oxidation —
  immunogenic, generate autoantibodies, activate TLR2, and are **directly angiogenic**
  via a VEGF-independent route. `[EMERGING]`
- **Isoprostanes (8-iso-PGF2α)** — non-enzymatic AA peroxidation products that are both
  biomarkers and vasoconstrictors via TP receptors
- **Oxysterols (7-ketocholesterol)** — drive RPE and Müller inflammation and apoptosis

Detoxification depends on **ALDH2, AKR1B1 (again — aldose reductase also reduces HNE),
GSTs and GPX4**. **GPX4** specifically reduces phospholipid hydroperoxides and is the
master suppressor of **ferroptosis**, an iron-dependent lipid-peroxidation cell death now
implicated in diabetic retinal cell loss. `[EMERGING]`

##### P8.8 Retinal fatty-acid oxidation, lipotoxicity and energy metabolism `[EMERGING]`

Fuel use in the retina is compartmentalized: **photoreceptors are intensely glycolytic**
(aerobic glycolysis, Warburg-like), while the **RPE** oxidizes fatty acids — notably the
DHA-rich lipids phagocytosed daily from shed photoreceptor outer segments — via β-oxidation
and ketogenesis (**HMGCS2**), exporting ketones back to photoreceptors. Müller cells sit
between, handling glucose and lactate.

In diabetes this metabolic ecology breaks down: substrate oversupply with impaired
**CPT1A**-mediated mitochondrial fatty-acid import and reduced **ACOX1** peroxisomal
oxidation produces **lipid droplet accumulation in RPE and Müller cells**, incomplete
β-oxidation intermediates (acylcarnitines), ceramide/DAG accrual, and lipotoxic ER and
mitochondrial stress. Impaired RPE β-oxidation also starves photoreceptors of ketone
fuel. **FABP4** (adipocyte FABP, elevated in DR serum and vitreous) and **FABP5** are
lipid chaperones whose induction correlates with retinal inflammation and angiogenesis.

**PPARA is the principal transcriptional governor of this entire module** (CPT1A, ACOX1,
HMGCS2, FABPs, FGF21, LPL, APOA1/APOA5, and the LXR/ABCA1 interface). This is why PPARα
is the convergence point for the lipid axis — see Section 5.2.

##### P8 target table

| Target | Role in DR lipid biology | Direction |
|---|---|---|
| **PPARA** | Master regulator of FAO, lipid clearance, retinal anti-inflammation, endothelial and neurovascular protection | **Agonist** |
| PPARG | Adipogenic/anti-inflammatory; retinal expression lower; anti-angiogenic in models | Agonist (with systemic fluid-retention caution) |
| PPARD | FAO and endothelial function; retinal role least characterized | Agonist `[EMERGING]` |
| CPT1A | Mitochondrial FA import; PPARα target | Inducer |
| ACOX1 | Peroxisomal β-oxidation of VLCFA; PPARα target | Inducer |
| HMGCS2 | RPE ketogenesis supplying photoreceptors | Inducer |
| FABP4 | Lipid chaperone; raised in DR; pro-angiogenic, pro-inflammatory | **Inhibitor** |
| FABP5 | Retinal lipid chaperone | Modulator |
| APOA1 | HDL acceptor; retinal reverse cholesterol transport | Inducer / mimetic |
| ABCA1 / ABCG1 | Cholesterol efflux; downregulated in diabetic retina | Inducer |
| NR1H3 / NR1H2 (LXRα/β) | Transcriptional control of efflux | Agonist |
| CYP46A1 / CYP27A1 | Cholesterol side-chain oxidation for export | Inducer |
| CD36 / OLR1 (LOX-1) / MSR1 | Uptake of oxidized/modified lipoprotein → foam cells | **Antagonist** |
| ELOVL4 | VLC-PUFA synthesis for photoreceptor membranes | Inducer / substrate supply |
| ADIPOR1 | Required for retinal DHA retention | Agonist |
| FADS1 / FADS2 / ACSL6 | n-3 PUFA synthesis and retinal esterification | Inducer |
| CERS2 / CERS6 / SPTLC1/2 | Ceramide synthesis → pericyte & endothelial apoptosis | Inhibitor |
| SMPD1 (ASMase) | Sphingomyelin → ceramide | Inhibitor |
| ASAH1 (acid ceramidase) | Ceramide clearance | Activator |
| SPHK1 / S1PR1 / S1PR2-3 | Barrier protection (S1PR1) vs permeability/fibrosis (S1PR2/3) | Subtype-selective |
| PLA2G4A / PLA2G7 (Lp-PLA2) | AA liberation; lipoprotein-associated lysoPC generation | Inhibitor |
| PTGS2 | PGE2 → permeability, VEGF | Inhibitor |
| ALOX5 / ALOX5AP / LTA4H | LTB4 → leukostasis | Inhibitor |
| ALOX12 / ALOX15 | 12/15-HETE → pericyte loss, VEGF, ER stress | **Inhibitor** |
| EPHX2 (sEH) | Degrades protective EETs | Inhibitor `[UNCERTAIN]` — model-dependent |
| GPX4 | Phospholipid hydroperoxide reduction; ferroptosis brake | Activator |
| ALDH2 | 4-HNE/acrolein detoxification | Activator |
| ACAT1/SOAT1 | Cholesterol esterification → ester droplets | Inhibitor `[EMERGING]` |

---

#### P9 — Neurovascular unit degeneration

Developed under S0. The organizing concept for downstream agents: the retinal
**neurovascular unit** = neurons (RGC, bipolar, amacrine, photoreceptor) + macroglia
(Müller, astrocytes) + microglia + pericytes + endothelium, coupled into a functional
module. DR is best understood as **progressive failure of this unit**, in which the
vascular lesions ophthalmoscopists score are the late, visible manifestation of an
earlier, invisible neuro-glial failure.

Two practical consequences:
1. **Visual function does not track vascular anatomy.** Eyes can be anatomically dry on
   OCT with poor acuity (DRIL, photoreceptor disruption, macular ischemia). A candidate
   that improves anatomy without improving function will fail on BCVA endpoints.
2. **The photoreceptor is a major source of the oxidative and inflammatory burden**, not
   merely a victim: it is the most metabolically active and most PUFA-laden cell, and
   models in which photoreceptors are absent or their oxidative output is suppressed show
   markedly less vascular disease. `[EMERGING]` *This is the mechanistic reason an agent
   acting on photoreceptor/outer-retinal lipid and redox biology could have vascular
   benefit — which is counterintuitive and worth flagging to downstream agents.*

---

## 3. Patient Population Profile

### 3.1 Demographics
- Any adult with diabetes; peak burden age **45–75**. Working-age blindness is the
  defining societal cost. `[ESTABLISHED]`
- Duration of diabetes is the strongest non-modifiable predictor. `[ESTABLISHED]`
- Higher prevalence and severity in **South Asian, African/African-Caribbean, Hispanic
  and Indigenous** populations, from a mix of genetic, metabolic and access factors.
  `[CURRENT CONSENSUS]` — *relevant to this project: the South Asian signal intersects
  with the Ayurvedic corpus and with where an inexpensive oral agent would matter most.*
- Male sex associates with modestly higher DR risk in several cohorts.
  `[UNCERTAIN]`
- Pregnancy causes **rapid DR acceleration** in T1DM — a specific high-risk window and a
  population in which any systemic agent is contraindicated by default.
  `[ESTABLISHED]`

### 3.2 T1D vs T2D — biologically different enough to matter

| Feature | T1DM | T2DM |
|---|---|---|
| DR at diagnosis | ~0% | **~20–30%** (long undiagnosed window) |
| Lifetime DR | >90% by 20 yr | ~60% by 20 yr |
| Dominant phenotype | More **PDR**; proliferative endpoint | More **DME/maculopathy**; exudative endpoint |
| Metabolic context | Insulinopenia, glycemic variability, often lean | Insulin resistance, **atherogenic dyslipidemia** (high TG, low HDL, small dense LDL), hypertension, obesity, hepatic steatosis |
| Lipid axis relevance | Present but less dominant | **Strongly relevant** — the apoB-remnant/small-dense-LDL phenotype is exactly the lipoprotein profile that extravasates and is modified in retina |
| Inflammation | Autoimmune background | Metabolic/adipose-derived (TNF, IL-6, FABP4, low adiponectin) |

`[CURRENT CONSENSUS]`

**Scoring implication:** a lipid-axis / PPARα-type mechanism has a stronger prior in
**T2DM with atherogenic dyslipidemia and exudative maculopathy** than in lean T1DM with
proliferative disease. Downstream agents should consider population enrichment, not an
all-comers DR population.

### 3.3 Comorbidities (near-universal, and they shape drug choice)

| Comorbidity | Prevalence in DR populations | Drug-development consequence |
|---|---|---|
| **Diabetic kidney disease / CKD** | Very high; DR and nephropathy are strongly concordant, especially in T1DM | **Renal clearance is impaired.** Any renally-eliminated agent needs dose adjustment; this is the single most important PK consideration for an oral DR drug. Also raises risk for agents causing creatinine elevation. |
| **Diabetic peripheral and autonomic neuropathy** | ~30–50% | Shared neurodegenerative biology; a neuroprotective agent may have dual benefit (and dual endpoints) |
| **Cardiovascular disease** | High; DR independently predicts MACE | A CV-neutral-or-better profile is close to mandatory; CV outcome data would be a major asset |
| **Dyslipidemia** | Very high in T2DM | **Directly on-pathway** for the lipid axis; also means patients are already on lipid-modifying therapy — see 3.4 |
| **Hypertension** | ~60–80% of T2DM | On-pathway (autoregulation failure); also means polypharmacy |
| **Obesity / metabolic syndrome / MASLD** | High in T2DM | Hepatic impairment affects clearance; MASLD is a shared PPARα-relevant tissue |
| **Anemia** | Common with CKD | Interacts with retinal oxygenation; relevant to any HIF-modulating agent |
| **Obstructive sleep apnea** | High; associates with DR and DME severity | Intermittent hypoxia → HIF axis activation |
| **Cataract** | Accelerated in diabetes, and *caused* by intravitreal steroid | A reason intravitreal steroid is second-line in phakic eyes |
| **Depression / cognitive impairment** | Elevated | Adherence risk for any chronic oral therapy |

### 3.4 Concurrent medication **classes** (for downstream DDI analysis)

*Stated at class level, as permitted. No specific agents are named.*

| Class | Prevalence | DDI / safety considerations for a new oral agent |
|---|---|---|
| Insulins | Universal in T1DM, common in long-standing T2DM | Hypoglycemia risk if the new agent improves insulin sensitivity |
| Oral and injectable glucose-lowering agents (multiple mechanistic classes) | Near-universal in T2DM | Additive hypoglycemia; some classes have renal dosing limits; several have their own ocular-relevant signals |
| Lipid-lowering agents (multiple classes) | Very high | **Highest-attention interaction for a lipid-axis candidate**: overlapping myopathy risk, shared CYP/transporter handling, pharmacodynamic additivity, and shared hepatic enzyme elevation |
| Antihypertensives — RAS-acting, calcium channel blockers, diuretics, beta-blockers | Very high | Renal function effects compound; hyperkalemia risk with some combinations |
| Antiplatelet / anticoagulant | High (CV comorbidity) | **Vitreous hemorrhage risk in PDR** is the ocular-specific concern; also relevant before vitrectomy |
| Diuretics | High | Volume status interacts with any agent causing fluid retention — note that **PPARγ agonism causes fluid retention and can worsen macular edema**, a class liability PPARα does not share to the same degree `[CURRENT CONSENSUS]` |
| Analgesics incl. NSAIDs | Common (neuropathy) | Renal risk additive; COX inhibition overlaps with the eicosanoid arm of P8 |
| Neuropathic pain agents (anticonvulsant, SNRI classes) | Common | CNS additive effects; hepatic metabolism |
| Thyroid replacement, PPI, antidepressants | Common background | Absorption and CYP considerations |
| Intravitreal therapy (anti-VEGF, corticosteroid) | In treated DME/PDR | Minimal systemic DDI, but **systemic VEGF suppression is measurable** after intravitreal anti-VEGF; relevant if combining with a systemic vascular agent |

**Organ function summary for downstream ADMET/safety agents:**
Assume a 60-year-old with eGFR 45–70, possible hepatic steatosis, on 6–10 concurrent
medications, with CV disease. **Prefer:** non-renally-cleared or renally-forgiving,
low-CYP-interaction, no hypoglycemia potentiation, no fluid retention, no QT signal, no
myopathy signal, and a long enough half-life for once-daily dosing. **Penalize heavily:**
anything requiring therapeutic drug monitoring, anything with hepatotoxicity signal,
anything causing fluid retention or weight gain.

### 3.5 Quality-of-life burden
Vision loss from DME is insidious and bilateral; reading and driving loss dominate
patient-reported outcomes. The **treatment** also carries burden: monthly-to-quarterly
intravitreal injections for years, each requiring clinic attendance, with associated
anxiety, cost and caregiver time. **Real-world loss-to-follow-up in DR populations is
very high (on the order of a quarter of patients within a year in several health
systems)** and is associated with irreversible vision loss. `[CURRENT CONSENSUS]`
*This is the strongest health-services argument for an oral agent.*

---

## 4. Current Standard of Care

*Described at modality and mechanism-class level only, per the blinding protocol.
No specific agent is named.*

### 4.1 By stage

| Stage | First line | Second line | Refractory |
|---|---|---|---|
| **Preclinical / DRN** | **Nothing.** Systemic glycemic, blood-pressure and lipid control (class-of-intervention level) + screening | — | — |
| **Mild–moderate NPDR, no DME** | Observation + systemic risk-factor control; interval screening | — | — |
| **Severe NPDR, no DME** | Observation, or **intravitreal anti-VEGF** to reduce progression risk, or **PRP** in selected high-risk eyes | PRP | — |
| **Center-involving DME with vision loss** | **Intravitreal anti-VEGF** (modality) | **Intravitreal corticosteroid** (implant or suspension) — preferred in pseudophakic eyes, in inflammatory-phenotype DME, and in anti-VEGF non-responders | Switch within/between classes; **focal/grid laser** for persistent extrafoveal leak; combination; vitrectomy if vitreomacular traction present |
| **Non-center-involving DME** | Observation or **focal laser** | — | — |
| **PDR** | **Intravitreal anti-VEGF** and/or **PRP** | Combination | **Pars plana vitrectomy** for non-clearing vitreous hemorrhage or tractional detachment |
| **Tractional RD / fibrovascular disease** | **Vitrectomy** with delamination ± endolaser ± pre-operative anti-VEGF | — | — |
| **Neovascular glaucoma** | Anti-VEGF + PRP + IOP-lowering + glaucoma surgery | — | Cyclodestruction |

### 4.2 Limitations — ranked by how much they constrain outcomes

1. **No therapy whatsoever for early or preclinical disease.** Patients are watched
   until they are sick enough to inject. For a disease with a 10–20 year runway, this is
   a spectacular missed window. `[ESTABLISHED]`
2. **Treatment burden of repeat intravitreal injection.** Years of monthly-to-quarterly
   clinic visits, each an intraocular procedure. Drives the very high real-world
   loss-to-follow-up, and real-world visual outcomes are consistently **worse than trial
   outcomes** largely because patients receive fewer injections than protocol.
   `[ESTABLISHED]`
3. **The non- and partial-responder fraction in DME: roughly 30–50% have an incomplete
   anatomic or functional response to anti-VEGF.** Mechanistic explanations (all in this
   model): inflammatory-phenotype DME, plasma-kallikrein-driven permeability, Müller
   cytotoxic edema, outer-BRB/RPE pump failure, macular ischemia, and lipid/hard-exudate
   burden. `[CURRENT CONSENSUS]`
4. **Laser is intrinsically destructive.** PRP ablates viable peripheral retina to save
   the macula — it trades peripheral visual field, night vision and (sometimes) macular
   edema worsening for reduced neovascular risk. Focal/grid laser causes atrophic scars
   that can enlarge over years. No modern therapy repairs what laser removes.
   `[ESTABLISHED]`
5. **No neuroprotection.** Nothing on the market targets RGC or photoreceptor survival,
   Müller function, or neurovascular coupling. This is why anatomic success does not
   always deliver functional success. `[ESTABLISHED]`
6. **No oral option.** Every DR-specific therapy is a procedure. `[ESTABLISHED]`
7. **No therapy for macular ischemia / capillary nonperfusion.** No agent reperfuses
   closed capillaries. `[ESTABLISHED]`
8. **No therapy clears hard exudate**, and subfoveal lipid causes permanent loss even in
   anatomically dried eyes. `[CURRENT CONSENSUS]`
9. **No anti-fibrotic** for the proliferative/tractional endpoint; anti-VEGF can
   precipitate contraction. `[ESTABLISHED]`
10. **Corticosteroid class toxicity** — cataract (near-universal in phakic eyes with
    sustained exposure) and IOP rise/glaucoma — caps the use of the one modality that
    works on the inflammatory axis. `[ESTABLISHED]`
11. **Cost and access.** Intravitreal therapy requires a retina specialist, sterile
    procedure capacity, and OCT. Most of the world's 100M+ people with DR cannot access
    this. `[ESTABLISHED]`
12. **Possible long-term consequences of chronic VEGF suppression** — outer retinal and
    RPE atrophy, choriocapillaris effects. `[EMERGING]`

### 4.3 Unmet needs — ranked for this analysis

| Rank | Unmet need | Why it ranks here |
|---|---|---|
| **1** | **Disease-modifying therapy for early (S0–S2) DR, deliverable systemically** | Largest population, longest runway, zero competition, and the only way to reach the global burden. Highest value, highest endpoint risk. |
| **2** | **A non-VEGF mechanism for DME that addresses the incomplete-responder fraction** | Large, well-defined, commercially proven population; clear regulatory path (BCVA/CST endpoints) |
| **3** | **Neuroprotection / preservation of visual function independent of anatomy** | Explains the function-anatomy gap; no competition; endpoint-definable via ERG + microperimetry + DRIL |
| **4** | **Therapy that reduces treatment burden** (oral adjunct reducing injection frequency) | Clinically and economically compelling; a *combination* endpoint (injection-count reduction) is regulatorily tractable |
| **5** | **Resolution/prevention of hard exudate and intraretinal lipid** | Mechanistically neglected; directly addressable by the P8 axis; measurable on colour photos and OCT hyperreflective foci |
| **6** | **Reperfusion of nonperfused retina / treatment of macular ischemia** | Highest scientific value, hardest to achieve, no validated path |
| **7** | **Anti-fibrotic for proliferative/tractional disease** | Smaller population; surgical alternative exists |
| **8** | **Therapy deployable without specialist infrastructure in LMIC settings** | Cross-cutting; favours cheap, stable, oral, generic-compatible chemistry |

### 4.4 Known failed or disappointing approaches — **mechanisms and ocular agents only**

*(Per blinding Rule 4, this lists failed mechanisms and intravitreal/ocular agents. No
oral repurposing candidates are named.)*

| Approach (mechanism / ocular class) | Outcome | Lesson for scoring |
|---|---|---|
| **Aldose reductase inhibition** (P1) | Multiple programmes; no convincing effect on DR progression in humans despite strong animal data | Single-branch blockade downstream of the ROS node is insufficient. Treat AKR1B1 activity as supportive only. |
| **PKCβ inhibition** (P3) | Reduced some functional endpoints; did not meet primary DR-progression endpoints convincingly; not approved for DR | Same lesson: one branch, late in a redundant network |
| **Intravitreal anti-PDGF-B combined with anti-VEGF** | Failed to add benefit over anti-VEGF alone in neovascular retinal disease | Pericyte-axis modulation is harder than the biology suggests; combination logic does not automatically translate |
| **Intravitreal integrin antagonists** (e.g. small-molecule integrin/RGD-class) | Mixed-to-disappointing in DME; several discontinued | Adhesion-axis targeting has not yet delivered |
| **Intravitreal anti-TNF (systemic biologic class used off-label intravitreally)** | Small studies; inflammatory signal but poor ocular tolerability and no registration | Single-cytokine blockade may be too narrow for a para-inflammatory disease |
| **Intravitreal / systemic broad antioxidant and vitamin supplementation** | Repeatedly negative or null for DR progression | Non-specific antioxidants do not reach retinal concentrations or do not act at the right compartment. **Penalize candidates whose only claim is "antioxidant".** |
| **Growth hormone / IGF-1 axis suppression (historically, pituitary ablation)** | Effective but unacceptable; later pharmacologic attempts not pursued | Shows the axis is real but untreatable at acceptable cost |
| **Intravitreal plasma kallikrein inhibition** | Encouraging mechanistic rationale; clinical results to date have been mixed, with benefit suggested in specific subgroups rather than all-comers | Supports the VEGF-independent permeability concept but argues for **phenotype enrichment** |
| **Intravitreal Ang2/Tie2-axis modulation as monotherapy** | Dual VEGF/Ang2 blockade has succeeded; Ang2-axis monotherapy has not established itself | Ang2 is an amplifier, not an independent driver |
| **Vitreolytic enzymatic agents for vitreomacular traction** | Narrow efficacy, safety concerns, commercially withdrawn in places | Mechanical mechanisms are narrow |
| **Topical delivery of posterior-segment drugs** | Repeated failures to achieve therapeutic retinal concentrations | **Strong prior against any topical DR candidate** absent exceptional data |
| **PPARγ agonism** (as a mechanism) | Class causes **fluid retention and is associated with worsening macular edema**; also weight gain, CV and bone concerns | **Important negative control for this run:** PPARγ and PPARα must be scored separately. Do not transfer PPARγ liabilities to PPARα, and do not transfer putative PPARα benefits to PPARγ. `[ESTABLISHED]` |

---

## 5. Key Molecular Targets

### 5.1 Consolidated master table

**Druggability key:** `KD` = known druggable (approved drugs or clinical-stage chemical
matter exist against this protein class/target); `TD` = theoretically druggable (tractable
class — enzyme, GPCR, NHR, ion channel — but no established ligand for this use);
`HARD` = low tractability (PPI, TF, structural); `UNK` = unknown.

**Validation key:** `G` genetic (human genetics/Mendelian/GWAS), `C` clinical (human
trial or human ocular tissue/vitreous evidence), `P` preclinical (animal/cell models),
`CP` computational (inferred from network/interaction data, incl. this project's PubChem
table).

| # | Target (gene) | Pathway | Role in DR | Druggability | Validation |
|---|---|---|---|---|---|
| 1 | **VEGFA** | P7 | Principal permeability + angiogenic driver; HIF output | KD | **C** (modality efficacy), P, G |
| 2 | **KDR** (VEGFR2) | P7 | Main signalling receptor: SRC→VE-cadherin, PKC, permeability | KD | C, P |
| 3 | **FLT1** (VEGFR1) | P7 | Decoy receptor; monocyte-recruiting arm; sFlt-1 is endogenous sink | KD | C, P |
| 4 | **PGF** (PlGF) | P7 | FLT1 ligand; inflammatory angiogenesis | KD | C, P |
| 5 | **ANGPT2** | P7/S1 | Destabilizes Tie2, detaches pericytes, sensitizes to VEGF | KD | **C** (dual-blockade efficacy), P |
| 6 | **TEK** (TIE2) | P7/S1 | Vessel stabilization receptor | KD | C, P |
| 7 | **PTPRB** (VE-PTP) | P7 | Silences Tie2; inhibition activates Tie2 | TD | P |
| 8 | **HIF1A** | P5/P7 | Master hypoxia/pseudohypoxia TF; drives VEGFA, ANGPT2, EPO | HARD (TF; translation-level tractable) | C (vitreous), P |
| 9 | **EPAS1** (HIF2A) | P7 | Endothelial-biased hypoxia TF | TD | P |
| 10 | **AKR1B1** | P1/P8.7 | Polyol flux, NADPH drain, pericyte death; also detoxifies 4-HNE | KD | **C (negative trials)**, P |
| 11 | **PRKCB** | P3 | Occludin phosphorylation, VEGF induction, flow abnormality | KD | **C (equivocal trials)**, P |
| 12 | **PRKCD** | P3 | Pericyte apoptosis via SHP-1/PDGFRβ | TD | P |
| 13 | **AGER** (RAGE) | P2 | AGE/S100/HMGB1 receptor → NOX → NF-κB | TD | C (tissue), P, **CP** (23 rows) |
| 14 | **GLO1** | P2 | Methylglyoxal detox; depressed in diabetes; NRF2-inducible | TD | P, G |
| 15 | **TNF** | P6 | ICAM1 induction, permeability, apoptosis | KD | C (vitreous), P, **CP** (724 rows) |
| 16 | **IL6** | P6 | Permeability; marker of anti-VEGF non-response | KD | **C** (vitreous correlates), P, CP (411) |
| 17 | **IL1B** | P6 | NLRP3 output; Müller autocrine amplification | KD | C, P, CP (425) |
| 18 | **NLRP3** | P6 | Inflammasome scaffold | TD | P |
| 19 | **ICAM1** | P6/S2 | **Leukostasis → capillary occlusion + endothelial apoptosis** | TD | C (tissue/vitreous), **P (causal, KO)**, CP (76) |
| 20 | **ITGB2** (CD18) | P6 | Leukocyte counter-receptor | TD | P (causal, KO) |
| 21 | **NFKB1/RELA** | P6 | Master inflammatory hub integrating P2/P3/P5/P8 | HARD (TF) | C, P, CP (85) |
| 22 | **NFE2L2** (NRF2) | P5 | Master antioxidant + anti-inflammatory TF; functionally deficient | TD (via KEAP1) | P, CP (250) |
| 23 | **KEAP1** | P5 | NRF2 repressor; covalent-ligand tractable | KD | P |
| 24 | **SOD2** | P5 | Mitochondrial superoxide; **epigenetically silenced = metabolic memory** | TD (mimetics) | P, CP (115) |
| 25 | **CAT** | P5 | H2O2 clearance | TD | P, CP (511) |
| 26 | **GPX4** | P5/P8.7 | Phospholipid hydroperoxide reduction; ferroptosis brake | TD | P |
| 27 | **NOS2** (iNOS) | P5 | High-output NO → peroxynitrite | KD | P |
| 28 | **NOS3** (eNOS) | P5/P3 | Protective NO; **uncoupled** in diabetes → superoxide | TD (recoupling, BH4/GCH1) | C, P, CP (84) |
| 29 | **ARG2** | P5 | Arginine depletion → eNOS uncoupling | TD | P |
| 30 | **NOX4 / CYBB / NOX1** | P2/P5 | NADPH-oxidase ROS downstream of RAGE/PKC | TD | P |
| 31 | **PARP1** | P5 | NAD+ depletion, GAPDH inhibition, inflammation | KD | P |
| 32 | **EDN1 / EDNRA** | P3 | Vasoconstriction, capillary closure, flow abnormality | KD | C, P, CP (39) |
| 33 | **MMP9** | S4/P6 | ILM/BM degradation; direct occludin cleavage | TD | C (vitreous), P, CP (116) |
| 34 | **TGFB1** | S1/S5 | BM thickening; **angio-fibrotic switch** | HARD/TD | C, P, CP (141) |
| 35 | **CTGF (CCN2)** | S5 | TGFβ effector; CTGF:VEGF ratio predicts fibrosis | TD | C (vitreous), P |
| 36 | **SERPINE1** (PAI-1) | S5/P4 | Fibrin scaffold stabilization | TD | C, P, CP (40) |
| 37 | **CASP3** | S0/P9 | Executioner apoptosis in RGC, pericytes, endothelium | TD | P, CP (594) |
| 38 | **BAX** | S0/P9 | Pro-apoptotic | HARD | P, CP (345) |
| 39 | **BCL2** | S0/P9 | Anti-apoptotic counterweight | KD (inhibitors exist; **inducers** are the need here) | P, CP (362) |
| 40 | **SLC2A1** (GLUT1) | P7 | Inner-BRB glucose transporter; HIF target; paradoxically down in diabetic retina | TD | P, CP (31) — direction `[UNCERTAIN]` |
| 41 | **PPARA** | **P8** | **Master lipid/FAO/anti-inflammatory/neurovascular regulator — see 5.2** | **KD** | P, **CP (143 rows, 39 compounds)** |
| 42 | **PPARG** | P8/P6 | Anti-inflammatory NHR; **class causes fluid retention/ME — liability** | KD | **C (negative ocular signal)**, P, CP (196) |
| 43 | **PPARD** | P8 | FAO, endothelial function; retinal role least defined | KD | P, CP (31) |
| 44 | **CPT1A** | P8.8 | Mitochondrial FA import; PPARα target | TD | P |
| 45 | **ACOX1** | P8.8 | Peroxisomal β-oxidation; PPARα target | TD | P |
| 46 | **FABP4** | P8.8 | Raised in DR serum/vitreous; pro-angiogenic, pro-inflammatory | TD | C (biomarker), P |
| 47 | **APOA1** | P8.3 | HDL acceptor for retinal cholesterol efflux; ApoA1 mimetics protective | TD (mimetic peptide) | P |
| 48 | **ABCA1 / ABCG1** | P8.3 | Cholesterol efflux; downregulated in diabetic retina | TD (via LXR) | P, G |
| 49 | **NR1H3 / NR1H2** (LXRα/β) | P8.3 | Transcriptional control of efflux; agonism protective in models | KD | P |
| 50 | **CD36 / OLR1** | P8.1 | Uptake of modified lipoprotein → foam cells | TD | P |
| 51 | **ELOVL4** | P8.4 | VLC-PUFA synthesis; **Mendelian macular dystrophy gene** | HARD (inducer/substrate only) | **G**, P |
| 52 | **ADIPOR1** | P8.4 | Required for retinal DHA retention; loss → photoreceptor degeneration | TD | **G**, P |
| 53 | **CERS2 / CERS6** | P8.5 | Ceramide synthesis → pericyte/endothelial apoptosis | TD | P |
| 54 | **SMPD1** (ASMase) | P8.5 | Sphingomyelin → ceramide; inhibition protective | KD (FIASMA chemotype) | P |
| 55 | **SPHK1 / S1PR1-3** | P8.5 | Barrier protection vs permeability/fibrosis, subtype-split | KD | P |
| 56 | **PLA2G4A / PLA2G7** | P8.6 | AA liberation; lipoprotein-associated lysoPC at exudate sites | TD | P |
| 57 | **PTGS2** (COX-2) | P8.6 | PGE2 → permeability, VEGF induction | KD | P |
| 58 | **ALOX5 / ALOX5AP / LTA4H** | P8.6 | LTB4 → leukostasis | KD | P |
| 59 | **ALOX12 / ALOX15** | P8.6 | 12/15-HETE → pericyte loss, VEGF, Müller ER stress | TD | **P (strong, KO-validated)** |
| 60 | **EPHX2** (sEH) | P8.6 | Degrades protective EETs | KD | P — direction `[UNCERTAIN]` |
| 61 | **SIRT1** | P5/P6 | Deacetylates RelA, NRF2, FOXO, PGC1A; depressed in diabetic retina | TD | P |
| 62 | **PRKAA1/PRKAA2** (AMPK) | P5/P8.8 | Energy sensor; upstream of SIRT1, PGC1A, FAO; suppressed | KD | P |
| 63 | **MTOR** | P9 | Autophagy suppression, HIF translation, Müller/RGC stress | KD | P |
| 64 | **KLKB1 / F12** | S4/DME | Plasma kallikrein → bradykinin; **VEGF-independent permeability** | KD | **C (vitreous + trials)**, P |
| 65 | **BDKRB1 / BDKRB2** | S4/DME | Bradykinin receptors; permeability, vasodilation | KD | C, P |
| 66 | **Local retinal RAS: AGT, REN, ACE, AGTR1, ACE2, MAS1** | cross-cutting | **The retina has a complete local renin–angiotensin system** independent of plasma RAS. Ang II via AGTR1 on Müller, endothelium and ganglion cells → NOX activation, VEGF induction, inflammation, neuronal loss. The counter-regulatory **ACE2 → Ang-(1-7) → MAS1** arm is protective and is suppressed in diabetic retina. | KD (AGTR1, ACE); TD (MAS1, ACE2) | C (tissue expression), P, **G (modest)** |
| 67 | **CLDN5 / OCLN / TJP1 / CDH5** | DME | Inner-BRB tight and adherens junction proteins | HARD (structural; tractable indirectly) | **C (human tissue)**, P |
| 68 | **CAV1 / PLVAP** | DME | Transcellular/vesicular leak arm | TD | P `[EMERGING]` |
| 69 | **KCNJ10 (Kir4.1) / AQP4** | S0/DME | Müller K+/water handling; cytotoxic edema | TD | **C (human tissue)**, P |
| 70 | **SERPINF1** (PEDF) | S0/P7 | Endogenous neuroprotective + anti-angiogenic brake; lost early | TD (protein/gene therapy) | C, P |
| 71 | **SST / SSTR2** | S0 | Lost retinal neuroprotective peptide tone | KD | C (human retina), P |
| 72 | **GLUL / SLC1A3 / GRIN2B** | S0 | Glutamate handling and excitotoxicity | TD | P |
| 73 | **EPO / EPOR** | S4 | VEGF-independent angiogenesis in PDR vitreous; **biphasic** — neuroprotective at low dose | KD | **C (vitreous)**, P — `[UNCERTAIN]` direction |
| 74 | **CCL2 / CCR2** | P6 | Monocyte recruitment; vitreous marker of DME severity | KD | C, P |
| 75 | **PPARGC1A** (PGC-1α) | P5/P8.8 | Mitochondrial biogenesis + antioxidant program | HARD | P |

> **Project-data note for downstream agents:** the `CP` validation flags above with row
> counts come from this run's blinded `pubchem_phytochem_target_interactions.csv`
> (60,521 rows). **These rows are largely CTD *expression-level* associations
> ("results in increased expression of X mRNA"), not binding affinities.** A compound
> appearing against a target in that file is a **hypothesis**, not demonstrated target
> engagement. Weight `CP` evidence accordingly — below `P`, far below `C`.
> `ANGPT2` has only **1** row and `KDR`/`PRKCB` only 16–18; absence of a compound–target
> row is therefore **not** evidence of absence.

### 5.2 PPARA — deep assessment (focus target of the downstream analysis)

**Honest verdict up front:** PPARα is a **well-validated, genuinely druggable nuclear
receptor whose retinal biology is real but whose retinal *expression level* is modest and
whose mechanism of retinal benefit is probably only partly retina-intrinsic.** It is a
strong but not airtight target. The honest uncertainties are stated below.

**(a) Retinal expression — the weakest link.** `[EMERGING / partly UNCERTAIN]`
PPARα is a nuclear receptor most abundant in liver, heart, kidney cortex, skeletal
muscle and brown adipose — tissues with high fatty-acid oxidation. Its expression in
**neural retina and RPE is detectable but low to moderate**, with reports across Müller
cells, RPE, ganglion cells, photoreceptors (inner segments), vascular endothelium and
retinal microglia. Critically, **retinal PPARα expression is reported to be *decreased*
in diabetes**, in both rodent models and human diabetic donor retina — meaning the
diabetic retina is in a state of relative PPARα deficiency, which is the classic setup
for an agonist to restore rather than supraphysiologically stimulate a pathway.
`[EMERGING]`
*Honest caveat:* some expression reports rest on antibodies of variable specificity, and
single-cell transcriptomic atlases of human retina do not show PPARA as a prominent
retinal transcript. **Do not over-claim retinal abundance.** The strongest argument for
retinal relevance is **conditional/tissue-restricted genetic evidence** — PPARα knockout
mice develop retinal vascular and neural abnormalities and show worse experimental
diabetic retinopathy, and retina-targeted PPARα expression is protective, which
collectively support a retina-intrinsic component rather than purely systemic action.
`[EMERGING]`

**(b) Role in retinal lipid metabolism.** `[CURRENT CONSENSUS]` for PPARα biology
generally; `[EMERGING]` for its retinal instantiation.
PPARα is the transcriptional governor of fatty-acid catabolism. Its direct target genes
cover essentially every node of P8.8: **CPT1A** (mitochondrial FA import), **ACOX1**
(peroxisomal β-oxidation of VLCFA), **HMGCS2** (ketogenesis — the RPE's mechanism for
converting photoreceptor-derived lipid into fuel it exports back to photoreceptors),
**FABP1/4/5**, **LPL**, **APOA1/APOA2/APOA5**, **ANGPTL4**, and **FGF21**. It also
raises **ABCA1** and intersects the LXR efflux axis (P8.3). Functionally, PPARα
activation is expected to (i) increase retinal and RPE fatty-acid oxidation, reducing
lipid droplet and ceramide/DAG accumulation and therefore lipotoxic ER stress;
(ii) improve RPE ketogenic support of photoreceptors; (iii) improve clearance and
handling of extravasated and modified lipoprotein; (iv) systemically lower
triglyceride-rich remnants and apoB particle number and raise ApoA1/HDL — which, per
P8.1/P8.2, reduces the *supply* of the lipoprotein that extravasates and is modified in
retina. **That last point is important: a meaningful share of a PPARα agonist's
plausible retinal benefit may be systemic (reducing the lipid load presented to a leaky
barrier) rather than retina-intrinsic.** This is not a weakness of the hypothesis — it
is the mechanism — but downstream agents should not assume retinal target engagement is
required for benefit. `[EMERGING]`

**(c) Endothelial function.** `[EMERGING]`
PPARα activation in vascular endothelium increases **NOS3** expression and activity and
improves NO bioavailability, reduces **EDN1**, reduces **ICAM1/VCAM1** induction (via
NF-κB transrepression, see below), suppresses NADPH-oxidase-derived ROS, reduces
**SERPINE1**, and improves endothelial progenitor function. In retinal endothelial cells
specifically, PPARα activation reduces VEGF-induced permeability and reduces tube
formation. There is also evidence that PPARα activation **inhibits Wnt/β-catenin
signalling**, a pathway that is overactivated in diabetic retina and drives VEGF, ICAM1
and inflammation — this is a credible retina-relevant downstream mechanism. `[EMERGING]`

**(d) Inflammation.** `[CURRENT CONSENSUS]` for the mechanism; `[EMERGING]` in retina.
PPARα is a *transrepressor*: ligand-bound PPARα physically interacts with and inhibits
**NFKB1/RELA** and **AP-1**, and promotes **IκBα** expression. This suppresses the exact
S2 output set — TNF, IL6, IL1B, ICAM1, VCAM1, CCL2, NOS2, PTGS2, MMP9. PPARα also
induces **catalase (CAT)** and other peroxisomal antioxidant genes and intersects with
**NFE2L2**, and PPARα-driven **FGF21** has independent metabolic and anti-inflammatory
effects. Mechanistically, **a PPARα agonist is simultaneously a lipid-handling agent and
an anti-inflammatory agent acting on the leukostasis hub** — which maps onto two of this
disease's three core axes at once. That dual action is the strongest argument for the
target.

**(e) Neurovascular and neuroprotective effects.** `[EMERGING]`
Reported in models: reduced RGC apoptosis, preserved ERG amplitudes, reduced Müller
gliosis (GFAP), reduced microglial activation, preserved pericyte coverage, reduced
acellular capillary formation, reduced BRB leakage, and reduced retinal neovascularization
in oxygen-induced retinopathy. Proposed mediators include AMPK/SIRT1/PGC-1α activation,
improved mitochondrial function, Wnt inhibition, and reduced ceramide load. The breadth
of these reports is both the attraction and the caution: **a target reported to improve
everything in animal models warrants scepticism** about effect size and about publication
bias. Mark effect magnitude as `[UNCERTAIN]`.

**(f) Druggability.** `[ESTABLISHED]`
PPARα is a **ligand-activated nuclear receptor with a large, well-characterized,
crystallographically mapped hydrophobic ligand-binding pocket** that accommodates
carboxylic-acid-bearing lipophilic ligands. It is one of the most tractable target
classes in medicinal chemistry: multiple chemotypes bind it, co-crystal structures are
abundant, selective and pan-PPAR agonists exist, SPPARMα (selective PPARα modulator)
design is a mature concept, and the natural ligands are **endogenous fatty acids and
fatty-acid derivatives** — meaning natural-product chemical space is intrinsically
privileged for this target. **Druggability: known druggable (KD), high confidence.**

**(g) What the blinded project data actually shows for PPARA.**
143 PPARA rows across **39 unique compounds** in the blinded PubChem table. The quality
distribution matters:
- **Genuine direct-binding evidence** (evidence strings stating "binds to and results in
  increased activity of PPARA protein"): **alpha-linolenic acid, oleic acid, linoleic
  acid, stearic acid, octanoic acid, lauric acid, myristic acid** — i.e. the endogenous
  fatty-acid ligand class. This is real but unsurprising: it confirms the pocket accepts
  fatty acids, which is textbook.
- **Annotated agonist/activator calls:** isoflavone (DrugBank "Agonist"), prasterone
  (DHEA, "Activator"), geraniol / citronellol / nonanoic acid ("increases activity").
- **Expression-level / protective-of-expression associations only:** quercetin, rutin,
  naringenin, myricetin, apigenin, catechin, melatonin, nicotinic acid,
  tetramethylpyrazine. **These are the weakest class of evidence** — "compound X prevents
  the decrease in PPARA mRNA caused by metabolic insult" is not target engagement.
- One **negative modulator**: gedunin ("decreases PPARA activity").

**Honest read:** the project's PPARA evidence base is dominated by (i) trivially expected
fatty-acid binding and (ii) weak CTD expression associations for polyphenols. **The data
supports "PPARα is a lipid-ligand-accepting receptor that many dietary phytochemicals
perturb" — it does not, by itself, nominate a potent, selective, drug-like PPARα agonist
from the natural-product set.** Downstream agents should not treat quercetin's PPARA row
as equivalent to a binding affinity. The compounds with the widest DR-target coverage
(quercetin 26 targets, apigenin 21, rutin 19, melatonin 19, naringenin 18, geraniol 18)
are promiscuous polyphenols — their breadth is as much an assay/annotation artifact and a
PAINS/pan-assay-interference risk as it is genuine polypharmacology. **Flag promiscuity
as a liability, not a feature, unless a specific multi-target rationale is argued.**

**(h) Net assessment of PPARA as a target for DR**

| Dimension | Assessment |
|---|---|
| Mechanistic fit to DR biology | **Strong** — hits P8 (lipid, the under-served axis), P6 (NF-κB/leukostasis), P5 (CAT, AMPK/SIRT1), and plausibly P9 (neuroprotection). Addresses unmet needs #1, #2, #3, #5 simultaneously. |
| Retinal expression | **Modest and partly contested.** The weakest link. `[EMERGING]` |
| Retina-intrinsic vs systemic mechanism | **Probably both; proportion unknown.** `[UNCERTAIN]` |
| Druggability | **High — known druggable NHR with a lipophilic acid-binding pocket.** `[ESTABLISHED]` |
| Route | **Orally tractable** — the pocket favours lipophilic carboxylic acids, which is compatible with oral dosing (though see Section 6 on what acids do to BRB penetration). |
| Stage applicability | Plausibly **S0–S3**, i.e. exactly the early window with zero competition; mechanistically weakest at S4/S5 |
| Phenotype enrichment | **T2DM, atherogenic dyslipidemia, exudative/hard-exudate DME** |
| Principal risks | Effect size may be modest; retinal penetration of acidic ligands is uncertain; class liabilities of PPAR agonism generally (hepatic enzyme elevation, creatinine elevation, myopathy signal when combined with other lipid-modifying classes); PPARγ's macular-edema liability must not be assumed absent in a non-selective ligand |
| Verdict | **High-priority target. Recommend full downstream workup.** The single most important question to resolve downstream is **retinal exposure after oral dosing**, not target validity. |

---

## 6. Route of Administration Considerations

### 6.1 The blood–retinal barrier

**Inner BRB** `[ESTABLISHED]` — retinal capillary endothelium with:
- Continuous, non-fenestrated endothelium with **high-resistance tight junctions**
  (CLDN5 dominant, plus OCLN, TJP1/ZO-1) and adherens junctions (CDH5)
- **The highest pericyte:endothelial ratio in the body (~1:1)**, with a glial sheath of
  Müller endfeet and astrocytes completing the unit
- Very low rates of vesicular transcytosis (actively suppressed by MFSD2A-type programs
  in CNS-like barriers)
- **Active efflux**: **ABCB1 (P-gp)**, **ABCG2 (BCRP)**, **ABCC1/4/5 (MRPs)** on the
  luminal membrane pump xenobiotics back into blood

**Outer BRB** `[ESTABLISHED]` — the RPE monolayer:
- Tight junctions (CLDN19 prominent in RPE, OCLN, TJP1) sealing the choroid–retina
  interface. The choriocapillaris beneath is **fenestrated**, so a drug reaches the
  *basal* RPE easily; the RPE itself is the barrier.
- Expresses the same efflux pumps **plus** a rich set of **uptake transporters** —
  **SLC16A/MCT1/3/4** (lactate/monocarboxylate), **SLCO/OATP** family, **SLC19A1**
  (reduced folate carrier), **SLC6A6** (TauT), **SLC2A1** (GLUT1), amino-acid and
  nucleoside transporters. **These are an exploitable route: a molecule resembling a
  monocarboxylate, folate, or amino-acid substrate can be actively carried across the
  RPE.** `[CURRENT CONSENSUS]`
- **Melanin binding** in RPE and choroid sequesters basic/lipophilic drugs. This is
  double-edged: it creates a depot that can prolong local exposure, but it also reduces
  free drug and makes exposure hard to predict.

**Disease modifies the barrier.** In DR the BRB is, by definition, compromised. A drug
that cannot cross an intact BRB may still reach **edematous, leaking retina** — meaning
penetration data from healthy animals can *underestimate* exposure in diseased eyes.
`[EMERGING]` — a genuinely important and often-missed point for scoring an oral candidate.

### 6.2 Physicochemical predictors of retinal penetration after oral dosing

The BRB behaves like the blood–brain barrier plus efflux plus melanin. Working heuristics
`[CURRENT CONSENSUS]`, to be used as a scoring rubric, not a law:

| Property | Favourable | Rationale |
|---|---|---|
| MW | **< 500 Da, ideally < 400** | Passive transcellular diffusion falls steeply above this |
| cLogP | **~2–4** | Too polar → no membrane partitioning; too lipophilic (>5) → trapped in membranes/melanin, high PPB, poor free fraction |
| TPSA | **< 90 Å², ideally < 70** | CNS-like rule; strongly predictive of passive permeability |
| H-bond donors | **≤ 2–3** | Each donor costs desolvation energy |
| Rotatable bonds | **≤ 8** | Flexibility penalizes permeability |
| Ionization | **Neutral or weak base favoured** | **Carboxylic acids are anionic at pH 7.4, which markedly reduces passive BRB penetration and makes them MRP/OATP substrates.** `[CURRENT CONSENSUS]` |
| Efflux liability | **Not a P-gp/BCRP substrate** | Efflux ratio > 2 in a bidirectional assay is a serious negative |
| Plasma protein binding | **Moderate (< ~98%)** | Only free drug crosses; >99% PPB is a common reason potent compounds fail to reach retina |
| Melanin binding | Moderate | Depot effect vs reduced free fraction |

> **⚠ The critical tension for this run.** The PPARα ligand pocket strongly favours
> **lipophilic carboxylic acids** — and carboxylic acids are exactly the chemotype the
> rubric above penalizes for BRB penetration (anionic at physiological pH, MRP/OATP
> substrates, high PPB). **This is the central ADMET question of the whole analysis and
> downstream agents must confront it directly, not assume it away.** Possible resolutions
> to evaluate: (i) the diseased, leaky BRB admits more than the intact one; (ii) ocular
> exposure data may exist for specific chemotypes; (iii) an active uptake transporter may
> carry the acid in; (iv) **acid bioisosteres** or ester/amide prodrugs could preserve
> PPARα binding while improving permeability; (v) a non-acidic PPARα agonist chemotype;
> (vi) the benefit may be predominantly systemic (reducing the lipoprotein load presented
> to the barrier), in which case retinal penetration is **not required**. Resolution (vi)
> is a legitimate and under-appreciated answer and should not be dismissed.

### 6.3 Route comparison

| Route | Retinal exposure | Burden / risk | Best use |
|---|---|---|---|
| **Oral / systemic** | Limited by BRB + efflux + PPB; typically low single-digit % of plasma free concentration `[CURRENT CONSENSUS]` | **Lowest procedural burden**; systemic exposure means systemic toxicity must be acceptable for years | **Chronic early-stage disease (S0–S2), bilateral, population-scale.** The only route that can reach the global burden. |
| **Intravitreal** | **Highest — direct, bypasses BRB** | Procedure per dose; endophthalmitis ~1 in 2,000–5,000 injections, retinal tear/detachment, IOP spike, vitreous hemorrhage, cataract (steroids); specialist + sterile facility required; high loss-to-follow-up | Established modality for DME/PDR. Small molecules clear from vitreous in **hours to a day or two**; proteins in **~4–9 days** — so a small molecule needs sustained release to be viable. |
| **Suprachoroidal** | High at chorioretina, spares anterior segment | Procedure; specialized microneedle | Attractive for corticosteroid-class agents (lower IOP/cataract exposure) and for depots targeting outer retina |
| **Periocular / sub-Tenon** | Modest and variable; sclera is permeable but conjunctival/choroidal clearance removes most drug | Lower risk than IVT | Largely superseded |
| **Topical (drops)** | **Essentially nil for the posterior pole for most molecules** — corneal barrier, rapid tear turnover, and the conjunctival/choroidal "clearance sink" `[ESTABLISHED]` | Lowest burden of all | **Strong prior against.** Penalize any topical DR claim heavily absent exceptional PK data. |
| **Sustained-release intraocular implant / depot** | High and prolonged (months) | Implantation procedure; non-removable biodegradable vs removable; steroid class toxicities | Reduces injection burden — a direct answer to unmet need #4 |
| **Port delivery / refillable reservoir** | High, continuous | Surgical implantation; refill procedures; conjunctival erosion risk | Burden reduction for chronic anti-VEGF |
| **Gene therapy (intravitreal or subretinal AAV)** | Potentially permanent local expression | One-time procedure; irreversibility; inflammation; subretinal surgery for subretinal route | For sustained anti-angiogenic or neurotrophic factor expression |

### 6.4 Why an oral agent would be transformative

1. **Bilateral by default.** DR is a bilateral disease; intravitreal therapy treats one
   eye per procedure.
2. **It is the only route deployable at the stage where the most patients are.** Over
   100 million people have DR; a small minority have VTDR requiring injections. The
   S0–S2 population is enormous, untreated, and unreachable by any procedure-based
   therapy.
3. **It collapses the infrastructure requirement.** No retina specialist, no sterile
   procedure room, no OCT per visit. This is the only route with a realistic path to the
   LMIC burden, where most DR blindness occurs.
4. **It solves the adherence/loss-to-follow-up problem** that makes real-world outcomes
   worse than trial outcomes — though it substitutes a different adherence problem
   (daily pill-taking in a polypharmacy population).
5. **It can treat the systemic disease and the retinal complication with one agent**,
   which is specifically plausible for a lipid-axis mechanism.
6. **Combination value:** even if an oral agent cannot replace anti-VEGF in established
   DME, reducing injection frequency is a clinically meaningful, regulatorily tractable
   endpoint.

**Counterweight to state honestly:** chronic systemic exposure in a comorbid,
polypharmacy, renally-impaired population sets a very high safety bar, and the
regulatory endpoint for early-stage DR (where the oral opportunity is greatest) is
**not established**, which is a major development risk — arguably larger than the
pharmacological risk.

---

## 7. Traditional Medicine Relevance

### 7.1 Ayurveda `[CURRENT CONSENSUS]` on the textual tradition; `[UNCERTAIN]` on efficacy

- **Diabetes is extensively described** in the classical corpus as **prameha** (a group
  of ~20 urinary disorders) and specifically **madhumeha** ("honey-urine"), with
  recognized long-term complications. `[ESTABLISHED]` as a textual fact.
- **Ophthalmology is a formal branch** — *Shalakya Tantra* — with a developed
  nosology of vision loss: **timira** (progressive dimming, mapped by modern Ayurvedic
  scholarship onto retinal/optic-nerve disease), **kacha**, and **linganasha**
  (blindness, classically cataract). Modern Ayurvedic clinical literature explicitly maps
  **"madhumehajanya timira"** onto diabetic retinopathy. `[CURRENT CONSENSUS]` that this
  mapping is made; `[UNCERTAIN]` that it was an ancient recognition of DR specifically.
- The category of **Chakshushya** (eye-benefiting) and **Rasayana** (rejuvenative)
  dravyas is directly relevant. Frequently cited: **Triphala** (*Terminalia chebula*,
  *T. bellirica*, *Phyllanthus emblica*), **Yashtimadhu** (*Glycyrrhiza glabra*),
  **Guduchi** (*Tinospora cordifolia*), **Haridra** (*Curcuma longa*), **Punarnava**
  (*Boerhavia diffusa*), **Shatavari** (*Asparagus racemosus*), **Saptamrita Lauha** and
  **Mahatriphala Ghrita** (compound formulations traditionally used for eye disorders).
- Antidiabetic dravyas with modern pharmacological literature: **Gymnema sylvestre**
  (gurmar), **Pterocarpus marsupium**, **Momordica charantia**, **Salacia reticulata**,
  **Trigonella foenum-graecum**, **Syzygium cumini**.
- **Evidence quality: weak.** Small, usually unblinded, single-centre studies; outcomes
  often symptom- or vision-based without standardized DRSS/OCT endpoints. No trial would
  meet modern regulatory standards. Treat as **hypothesis-generating only.**

### 7.2 Traditional Chinese Medicine `[CURRENT CONSENSUS]` that trials exist; `[UNCERTAIN]` that they are reliable

TCM has the **largest formal clinical trial literature of any traditional system for
DR specifically** — this is the most clinically developed traditional-medicine signal in
this disease.
- **Compound Danshen-type formulations** (*Salvia miltiorrhiza* + *Panax notoginseng* +
  borneol) have been studied in NPDR with reported improvements in microaneurysm counts
  and visual acuity.
- **Qiming granule**, **Hexue Mingmu tablet**, **Fufang Xueshuantong** (*Panax
  notoginseng*, *Astragalus*, *Salvia*, *Scrophularia*) have multiple Chinese RCTs.
- Isolated constituents with mechanistic literature: **puerarin** (*Pueraria*),
  **tanshinone IIA** and **salvianolic acid B** (*Salvia*), **notoginsenosides**,
  **astragaloside IV**, **berberine**, **calycosin**.
- **Systematic reviews (incl. Cochrane) consistently conclude the evidence is
  insufficient** due to small size, poor randomization/blinding, short follow-up,
  non-standardized outcomes and publication bias concentrated in one country.
  `[ESTABLISHED]` that this is the review verdict.

### 7.3 Western / European herbal `[CURRENT CONSENSUS]` tradition, `[UNCERTAIN]` efficacy

- **Bilberry (*Vaccinium myrtillus*) anthocyanins** — the canonical "capillary fragility
  and night vision" tradition; anthocyanins are credible antioxidants and have reported
  effects on endothelial permeability. Human DR evidence is thin.
- **French maritime pine bark extract (*Pinus pinaster*, oligomeric proanthocyanidins)**
  — several small European studies in early DR reporting reduced retinal leakage. Small,
  mostly open-label.
- ***Ginkgo biloba*** — ocular blood flow rationale; weak DR evidence.
- **Grape seed proanthocyanidins**; **lutein/zeaxanthin** (macular carotenoids, with the
  strongest nutritional-science base of this group, though their main evidence is in AMD);
  **saffron (*Crocus sativus*, crocin/crocetin)** with a growing retinal literature.
- **Chemical note:** this entire Western group is **flavonoid/anthocyanin/proanthocyanidin
  chemistry** — the same chemical class that dominates this project's PubChem
  phytochemical hits (quercetin, rutin, apigenin, naringenin, catechin, myricetin). The
  traditional and computational signals converge on one chemotype, which is either
  meaningful convergence or shared bias toward well-studied, highly-assayed, promiscuous
  polyphenols. **Treat with appropriate scepticism — flavonoids are notorious
  pan-assay-interference compounds and have poor oral bioavailability.** `[CURRENT CONSENSUS]`

### 7.4 What this project's blinded data actually contains

| Source | Finding |
|---|---|
| `imppat_plant_therapeutic_uses.json` | **Only 13 plants** — very thin. But **8 of 13 carry eye and/or diabetes therapeutic uses**: *Azadirachta indica* (conjunctiv/ophthalm/eye disease/vision/diabetes — all five), *Cassia fistula* (four), *Terminalia chebula* (eye disease/ophthalm/diabetes), *Glycyrrhiza glabra* (conjunctiv/ophthalm/diabetes), *Cyperus rotundus* (conjunctiv/ophthalm/diabetes), *Trichosanthes dioica* (diabetes), *Alstonia scholaris* (vision), *Santalum album* (vision). Several of these (*Terminalia chebula*, *Glycyrrhiza glabra*) are exactly the Chakshushya/Rasayana dravyas named in 7.1 — **independent convergence between the classical corpus and the project's own database.** |
| `medicinal_plants_with_uses.csv` | **⚠ QC WARNING for downstream agents:** a case-insensitive grep for "eye" returns **4 rows, all of which are common-name artifacts** — *Adonis aestivalis* ("Summer Pheasant's **Eye**"), *Euphrasia officinalis* ("**Eye**bright"), *Phaseolus adenanthus*, *Thunbergia alata* ("Black-**Eye**d Susan") — and **all four carry `"UNKNOWN USE"`**. There are **zero** rows matching "diabet". **This file contributes no DR ethnobotany evidence. Do not let a naive keyword search manufacture a signal here.** (*Euphrasia* does have a genuine European eyebright tradition, but this file does not record it.) |
| `pubchem_phytochem_target_interactions.csv` | 60,521 rows — **the project's richest asset by far**, and the only file capable of linking plant chemistry to DR targets. Caveat per §5.1: largely CTD expression-level associations. |
| `disgenet__OM_*` | Oral Mucositis only. **No DR gene–disease data in the project.** All gene–disease associations in this model are knowledge-based. |

### 7.5 Verdict — should the Ethnobotany agent be run?

**YES — run it.** Rationale:

1. There is a **genuine, documented traditional corpus** for both the antecedent disease
   (prameha/madhumeha) and for eye disease (Shalakya Tantra, Chakshushya dravyas), and
   TCM has an actual, if low-quality, DR-specific clinical trial literature. This is not
   a case of retrofitting tradition onto a modern disease.
2. **The project's own IMPPAT data independently converges** on plants the classical
   corpus names for eye and diabetes use (*Terminalia chebula*, *Glycyrrhiza glabra*,
   *Azadirachta indica*, *Cassia fistula*, *Cyperus rotundus*) — 8 of 13 plants carry
   relevant uses.
3. The **PubChem phytochemical–target table is the project's primary evidence asset**,
   and the compounds with the widest DR-target coverage are plant secondary metabolites.
   An ethnobotany agent is the right instrument to interrogate it.
4. **Chemical-class convergence:** Ayurvedic, TCM and Western herbal DR traditions all
   centre on polyphenol/flavonoid/terpenoid chemistry, which is also the dominant
   chemotype in the project's PPARA and DR-target hits.

**Constraints to hand the Ethnobotany agent:**
- **Evidence quality is uniformly low.** Weight traditional use as hypothesis-generating,
  never as efficacy evidence.
- **Do not trust `medicinal_plants_with_uses.csv` keyword hits** (see the QC warning
  above).
- **Flavonoid promiscuity is a liability.** Quercetin hitting 26 DR targets is more
  likely assay promiscuity + annotation bias than genuine designed polypharmacology.
  Require a specific mechanistic argument.
- **Oral bioavailability is the Achilles heel** of this entire chemical class
  (extensive phase-II conjugation, low plasma free fraction, poor BRB penetration).
  Any natural-product candidate must be scored against Section 6.2 honestly.
- IMPPAT coverage here is **13 plants**, not the full database — do not treat absence as
  evidence of absence.

---

## 8. Summary for Downstream Agents

**Score every candidate as a (pathway, stage, compartment, route) tuple.**

- **Pathway:** which of P1–P9 does it engage, with what evidence quality?
- **Stage:** at which of S0–S5 (or which DME phenotype) would that engagement change the
  trajectory?
- **Compartment:** inner BRB / outer BRB / neural retina / glia / vitreoretinal interface?
- **Route:** can it get there, given Section 6.2?

**Highest-value profile given the unmet-need ranking:** an **orally bioavailable agent
engaging the lipid (P8) and inflammatory (P6) axes at stages S0–S3**, with a neurovascular
(P9) component, acceptable for chronic use in a renally-impaired polypharmacy population.
That is precisely the profile a PPARα-class mechanism would have **if** the retinal
exposure question (§6.2) can be answered — which is the critical path item for this
analysis.

**Things that should lose points:** "antioxidant" as the sole mechanism (repeatedly
failed); single-branch blockade downstream of the ROS node (P1/P3 precedent); topical
delivery claims; promiscuous polyphenols without a specific mechanistic argument;
mechanisms that only act at S4/S5 where effective therapy exists; anything causing fluid
retention (PPARγ class precedent), hypoglycemia potentiation, myopathy signal, or
requiring therapeutic drug monitoring.

