# P1 — Pharmacokinetics / ADMET Specialist
## Retinal Exposure, Chronic Safety, and the Go/No-Go on the PPARα Hypothesis
### Diabetic Retinopathy — BLINDED RUN — 2026-10-05

---

## 0. Provenance key and the honesty contract for every number below

The blinded dataset's PK-relevant columns are **empty for every one of its 3,276 approved-drug
rows**. Verified directly:

| Column | Populated |
|---|---|
| `logd` | **0 / 3276** |
| `cx_logp` | **0 / 3276** |
| `cx_logd` | **0 / 3276** |
| `molecular_species` | **0 / 3276** |
| `bioavailability_score` | **0 / 3276** |
| `permeability` | **0 / 3276** |
| `alogp` | 2973 / 3276 |
| `psa` | 2973 / 3276 |
| `molecular_weight` | 3239 / 3276 |

**Consequence: there is not one measured distribution, permeability, protein-binding or
bioavailability value in this project.** Every Cmax, every fraction unbound, every EC50, every
Vd and every Kp,uu in this report is **knowledge-based and approximate**. I have tagged each
number:

- **`[DATA]`** — read from the blinded dataset (structure, MW, aLogP, PSA, HBD/HBA, RTB,
  Ro5 violations, QED, SMILES, curated metabolism rows).
- **`[KB]`** — general (non-DR) pharmacology knowledge. Approximate, order-of-magnitude.
- **`[CALC]`** — arithmetic performed here on `[DATA]` and `[KB]` inputs.

Where I give a range it is a genuine uncertainty range, not false precision. Where a conclusion
turns on a number whose uncertainty could flip it, I say so explicitly rather than hiding it in
a point estimate. **Every `[KB]` PK number in this report should be treated as ±0.5 log, and the
protein-binding correction in §4.1 as ±1 log.**

---

## 1. EXECUTIVE VERDICT

**The PPARα hypothesis survives the exposure question — but only in two of the four anatomical
compartments, by a mechanism the scout did not identify, and with a reversal of which arm
carries the wrong-sign risk.**

Six findings, in order of consequence:

1. **The scout's arithmetic is correct but the comparison is inconsistent.** It compares a
   *free* plasma concentration against a *nominal* transactivation EC50 measured in
   serum-containing medium — where the ligand is itself heavily bound. Correcting both sides to
   free drug closes roughly **1 log (range 0.5–1.5)** of the claimed two-order-of-magnitude gap.
   The direction of the conclusion is unchanged; the magnitude is overstated.

2. **The compartment matters more than the barrier.** PPARα in the **retinal vascular
   endothelium** sits on the *blood* side of the inner BRB, and PPARα in the **RPE** faces the
   *fenestrated* choriocapillaris. Neither target requires crossing the barrier — only crossing
   one plasma membrane. **Estimated Kp,uu for these compartments is ~0.2–0.7, versus ~0.01–0.15
   for neural retina — roughly a 10-fold difference.** And those two accessible compartments are
   precisely where the P6 (leukostasis/ICAM1/VCAM1) and P8 (lipid handling, HMGCS2 ketogenesis)
   mechanisms live. **This is the single most important correction in this report.**

3. **Potency does not buy engagement.** Pemafibrate is ~4.8 logs more potent than fenofibric
   acid but circulates at ~4 logs lower free concentration (350-fold lower dose × 5-fold lower
   fu). After consistent protein correction its margin at the endothelium is **~1 log better,
   not ~5 logs better.** The free-drug hypothesis eats almost the entire potency gain. Any
   ranking that treats "sub-nanomolar" as decisive is mis-ranking the set.

4. **The bootstrapping paradox is overstated as a paradox and understated as a problem.**
   Barrier breakdown drives Kp,uu *toward* 1 and can never exceed it. Reaching the free EC50 in
   neural retina would require **Kp,uu of 10–100** — i.e. concentrative uptake, which the retina
   does not have for this chemotype. **Even total, complete BRB failure leaves fenofibric acid
   10–100× below its free EC50 in neural retina.** The drug does not arrive too late; it never
   arrives in sufficient quantity at any stage. Meanwhile, for the *systemic* lipid mechanism the
   leaky barrier is the **indication**, not the obstacle — so for that arm the paradox dissolves
   completely.

5. **The wrong-sign risk is in the systemic arm, not the retinal arm — the inverse of the naive
   expectation.** ANGPTL4 induction is a transcriptional PPARα response requiring the *same*
   occupancy as the therapeutic transactivation responses. If retinal occupancy is too low to
   induce CPT1A and HMGCS2, it is equally too low to induce retinal ANGPTL4. But **hepatic**
   PPARα *is* fully engaged (OATP1B1/1B3 concentrates fibrates in liver 10–100×), so hepatic
   ANGPTL4 induction raising *circulating* ANGPTL4 — which then acts on retinal endothelium from
   the luminal side — is the real exposure-weighted wrong-sign path. **Plasma ANGPTL4 is a
   measurable, mandatory biomarker for any fibrate trial in this disease.**

6. **The exposure control fires, and it fires against the whole set.** Melatonin ranks #1 on
   retinal access by a wide margin — and *still* cannot reach the concentrations at which its
   putative antioxidant/anti-apoptotic/PPARα effects are observed (3–5 logs short). It engages
   only MT1/MT2, sub-nanomolar receptors. **The set contains no compound that has both access and
   potency for the hypothesised mechanism.** Access is necessary and not sufficient; affinity is
   necessary and not sufficient; nothing in this candidate set has both.

**Bottom line for the ranker:** *score systemic lipid/lipoprotein lowering as the primary,
exposure-defensible mechanism; score endothelial and RPE PPARα transrepression as a secondary,
marginal-but-arguable mechanism; score neural-retina PPARα engagement as **not achievable** by
any oral molecule in this set.*

---

## 2. What the project data could and could not supply

### 2.1 What it supplied (genuinely `[DATA]`)

| Finding | File | Why it matters to ADMET |
|---|---|---|
| `CHEMBL672 FENOFIBRATE → FENOFIBRIC ACID`, enzyme **Esterases**, De-esterification, Liver; *"Fenofibrate is more or less completely converted into this metabolite… Mainly excreted in the urine as a glucuronide conjugate"* | `chembl_drug_metabolism.csv` | Proves A2 has **no independent PK identity** from A1, and establishes renal glucuronide elimination |
| `CHEMBL981 FENOFIBRIC ACID → REDUCED FENOFIBRIC ACID`; *"minor metabolite, but has similar activity… Mainly excreted as its glucuronide conjugate in urine"* | same | Confirms an **active** secondary metabolite and the renal route |
| `REDUCED FENOFIBRIC ACID → …GLUCURONIDE`, *"Glucuronide conjugation to the carboxylic acid forming an ester"* | same | Explicit **acyl glucuronide** formation for the fibrate scaffold |
| 16 distinct acyl/ester-glucuronide rows — diflunisal, ketoprofen, salicylic acid, celecoxib acid metabolite, oxaprozin, isonicotinic acid | same | The reactive-AG structural class is **attested in the project's own data**, not just asserted |
| Quercetin ⇄ **ABCB1** (*"ABCB1 protein results in increased transport of quercetin"*; *"abcb1 protein results in decreased abundance of quercetin"*) and **ABCG2** (*"ABCG2 protein affects the export of quercetin"*) | `pubchem_phytochem_target_interactions.csv` | Quercetin is a **dual efflux substrate** — a direct, data-backed BRB-penetration disqualifier |
| Quercetin **inhibits SLCO1B1-mediated atorvastatin import** (PMID 22394605); also inhibits SLCO2B1, ABCB1, ABCC1/4/5, SLC16A1 | same | A concrete, data-backed DDI in a **universally statin-treated** population |
| Quercetin is an **OATP substrate** — uptake by SLCO1A2, 1B1, 1B3, 2A1, 2B1, 5A1 (PMID 24947867) | same | Establishes that the OATP family carries this chemotype class — relevant to §4.4 |
| Linoleic acid **decreases activity of SLC22A6 (OAT1) and SLC22A8 (OAT3)** (PMID 29045746) | same | Fatty acids are recognised by OATs — but as inhibitors, with no directional information |
| Melatonin **inhibits SLC22A8 (OAT3)** and SLC22A2 (OCT2) | same | Minor DDI note; confirms OAT recognition |
| Linalool → SLC27A4 induction is **PPARA-dependent** (abolished in PPARA mutant, PMID 24752549) | same | The only genetic-dependency engagement evidence in the set |
| SMILES for all Group A compounds | `chembl_approved_drugs.csv` | Enables the acyl-glucuronide reactivity SAR in §8 |

### 2.2 What it could not supply

- **No measured PK of any kind** (see §0).
- **`chembl_drug_mechanisms.csv` = 10 rows, `chembl_drug_targets.csv` = 43 rows,
  `chembl_bioactivities.csv` = 23 rows, and `grep -ci PPAR` returns **0** in all three.** There is
  no drug→target affinity anywhere in this project. Every potency value below is `[KB]`.
- **`chembl_toxicity.csv` = 1 data row. `chembl_drug_warnings.csv` = 9 rows, none matching any
  candidate.** The project contributes **zero** toxicity or warning evidence for this analysis.
- **`chembl_natural_products.csv` = 25 rows.** Quercetin, linoleic acid, α-linolenic acid and
  linalool have **no physicochemical descriptors in this project at all** — their MW/logP/PSA
  below are `[KB]`.
- `chembl_drug_metabolism.csv` is **10× duplicated** with a corrupt `drug_name` column, as
  `data-quality-findings.md` reports. I deduplicated on
  (substrate, metabolite, enzyme, conversion) before reading it.

### 2.3 Two provenance traps in the dataset

**Trap 1 — Fenofibrate (A2).** `[DATA]` MW 360.84, aLogP 4.68, PSA 52.60, **HBD 0, neutral
ester**. On the model §6.2 rubric this is a *good* BRB profile — better than the acid on
ionization, HBD and PSA. **It is unusable.** The project's own metabolism row proves complete
presystemic esterase conversion. Intact fenofibrate is not a circulating species. Scoring A2 on
its tabulated descriptors scores a molecule that does not exist in vivo.

**Trap 2 — Dimethyl fumarate (D2).** `[DATA]` MW 144.13, aLogP −0.11, PSA 52.60, HBD 0, Ro5v 0 —
the smallest, most neutral molecule in the set. But DMF is hydrolysed by gut and plasma esterases
to **monomethyl fumarate (MMF)**, MW 130.1, a **carboxylic acid** `[KB]`. The circulating species
is anionic, not neutral. Unlike Trap 1 this one is **not** flagged anywhere in the project data —
there are no DMF metabolism rows. An agent relying on the descriptor table alone would rank DMF
as the best BRB penetrant in the set. It is not.

---

## 3. (a) THE RETINAL EXPOSURE MODEL

### 3.1 The compartment correction — stated before the arithmetic, because it changes it

Axis C of the disease model distinguishes four compartments. **They are not equally hard to
reach, and three of the four do not require crossing the blood–retinal barrier at all.**

| Compartment | Position relative to the barrier | What a systemically dosed drug must cross | Est. Kp,uu `[CALC/KB]` |
|---|---|---|---|
| **Inner-BRB endothelium** (capillary EC, the P6 leukostasis cell) | **Luminal — bathed in plasma** | One plasma membrane, against luminal MRP/BCRP efflux | **0.2–0.7** |
| **RPE / outer BRB** (the P8 lipid-handling, HMGCS2 ketogenic cell) | **Basal side faces the *fenestrated* choriocapillaris** | Free diffusion to basal membrane, then one plasma membrane | **0.2–0.6** |
| **Pericyte / glial endfoot** (abluminal side of inner BRB) | Behind the tight junction | Full transcellular barrier passage | **0.05–0.3** |
| **Neural retina** (Müller soma, RGC, photoreceptor, microglia) | Fully behind both barriers | Full barrier + diffusion through neuropil, against MRP/OAT3 efflux | **0.01–0.15** |

> **This is the correction the scout's analysis missed.** The scout treated "retinal exposure" as
> one number gated by the BRB. It is four numbers, and the two compartments that host the two
> strongest PPARα mechanisms (endothelial NF-κB transrepression; RPE fatty-acid oxidation and
> ketogenesis) are on the **blood side** of the barrier. The drug reaches the basal RPE and the
> luminal endothelium **whether or not it can cross the BRB.**

The same logic rescues candesartan (§7.9): its AT1R target on retinal endothelium is luminal, so
a di-anionic molecule with Vd 0.13 L/kg still engages it fully.

### 3.2 The arithmetic — Group A, laid out step by step

All PPB, Cmax, Vd and EC50 values `[KB]`, ±0.5 log. Structural descriptors `[DATA]`.
Cavg,ss taken as 0.65 × Cmax for once-daily agents `[CALC]`. Free EC50 is the nominal
transactivation EC50 corrected for binding in serum-containing assay medium — see §4.1 for why
this correction is mandatory and why it carries ±1 log.

#### A1 / A2 — Fenofibric acid (from fenofibrate 145 mg od, or fenofibric acid 135 mg od)

```
STRUCTURE [DATA]   MW 318.76 | aLogP 3.81 | PSA 63.60 | HBD 1 | HBA 3 | RTB 5
                   Ro5 violations 0 | QED 0.85 (best in class) | monocarboxylic acid

 1. Dose                                      145 mg fenofibrate od            [KB]
 2. Steady-state Cmax, TOTAL                  10–15 µg/mL = 31–47 µM           [KB/CALC]
 3. Cavg,ss, TOTAL  (× 0.65)                  20–31 µM                         [CALC]
 4. Fraction unbound (fu), ~99–99.5% bound    0.005–0.010                      [KB]
 5. FREE PLASMA Cavg,ss  (3 × 4)              0.10–0.31 µM                     [CALC]
 6. Vd                                        ~0.9 L/kg  ≈ extracellular water [KB]
 7. PPARα transactivation EC50, NOMINAL       ~30 µM (lit. range 18–55)        [KB]
 8. EC50 corrected to FREE drug (§4.1)        3–30 µM                          [CALC, ±1 log]
 9. EC90 free  (Hill = 1 ⇒ 9 × EC50)          27–270 µM                        [CALC]

10. ENDOTHELIUM / RPE free (5 × Kp,uu 0.3–0.7)   0.03–0.22 µM                  [CALC]
      margin vs free EC50 ................... 0.001 – 0.073  →  −3.0 to −1.1 log
11. NEURAL RETINA free (5 × Kp,uu 0.03–0.15)     0.003–0.047 µM                [CALC]
      margin vs free EC50 ................... 0.0001 – 0.016 →  −4.0 to −1.8 log
      margin vs free EC90 ................... 1e-5 – 0.0017  →  −5.0 to −2.8 log
```

**Reading.** In the accessible compartments, at the most favourable end of every range,
fenofibric acid reaches ~7% of its free EC50 — i.e. roughly **EC7**, ~7% of maximal
transcriptional output. In neural retina, ~1.6% at best. **Not robust engagement anywhere; a
small, chronic, partial transcriptional nudge in the endothelium and RPE is arguable.**

**Independent confirmation from Vd (line 6), which the scout did not use.** Fenofibric acid's
volume of distribution is ~0.9 L/kg — close to total body water and barely above extracellular
fluid volume. **A drug with a Vd this low is, by definition, not distributing into tissue.** This
is a direct empirical statement about the molecule's tissue partitioning that requires no
barrier modelling at all, and it independently corroborates the low Kp,uu estimates. It is the
cleanest single piece of evidence in the whole exposure argument.

#### A3 — Pemafibrate (0.2 mg bid = 0.4 mg/day)

```
STRUCTURE [DATA]   MW 490.56 | aLogP 5.55 | PSA 94.26 | HBD 1 | HBA 7 | RTB 13
                   Ro5 violations 1 | QED 0.24 (worst in Group A) | carboxylic acid

 1. Dose                                      0.4 mg/day  (362× lower than A1) [KB]
 2. Cmax, TOTAL                               5–10 ng/mL = 10–20 nM            [KB/CALC]
 3. Cavg,ss, TOTAL                            6–12 nM                          [CALC]
 4. fu  (>99.8% bound)                        ≤0.002                           [KB]
 5. FREE PLASMA Cavg,ss                       12–24 pM                         [CALC]
 6. Hepatic handling                 OATP1B1/1B3 substrate — hepatoselective BY DESIGN [KB]
 7. PPARα EC50, NOMINAL                       ~0.4–1 nM (sub-nM class)         [KB]
 8. EC50 corrected to FREE drug      0.02–0.1 nM (larger correction: aLogP 5.55) [CALC, ±1 log]

 9. ENDOTHELIUM / RPE free (5 × Kp,uu 0.2–0.5)   2.4–12 pM                     [CALC]
      margin vs free EC50 ................... 0.024 – 0.6   →  −1.6 to −0.2 log
10. NEURAL RETINA free (5 × Kp,uu 0.01–0.05)     0.12–1.2 pM                   [CALC]
      margin vs free EC50 ................... 0.001 – 0.06  →  −3.0 to −1.2 log
```

**Reading — and the key comparative result.** Pemafibrate is **~60,000× more potent** than
fenofibric acid but circulates at **~13,000× lower free concentration.** After applying the same
protein correction to both compounds, its endothelial margin is **~1 log better than fenofibric
acid's — not 4.8 logs better.** The free-drug hypothesis consumes almost the entire potency gain,
because the potency was bought with lipophilicity (aLogP 5.55 `[DATA]`), which drove fu down and
allowed a 362-fold dose reduction.

**Corollary for the ranker: in this chemical series, potency is nearly orthogonal to engagement.
Choose between fibrates on safety, formulation and elimination route — not on EC50.**

#### A4 — Elafibranor (120 mg od) — the best margin, the worst structural alert

```
STRUCTURE [DATA]   MW 384.50 | aLogP 5.16 | PSA 63.60 | HBD 1 | RTB 7 | Ro5v 1 | QED 0.41
SMILES    [DATA]   CSc1ccc(C(=O)/C=C/c2cc(C)c(OC(C)(C)C(=O)O)c(C)c2)cc1
                   ↑ C(=O)/C=C/  — an α,β-unsaturated ketone: MICHAEL ACCEPTOR
                   ↑ OC(C)(C)C(=O)O — quaternary α-carbon (low acyl-glucuronide reactivity)
                   ↑ CSc1 — thioanisole, oxidised to sulfoxide/sulfone

 1. Cmax, TOTAL (parent)              ~1–2 µg/mL ≈ 2.6–5.2 µM     [KB, LOW CONFIDENCE]
 2. fu (>99% bound)                   ~0.005                      [KB]
 3. FREE PLASMA                       ~13–26 nM                   [CALC]
 4. PPARα EC50 nominal / free         ~45 nM / 5–15 nM            [KB/CALC]
 5. ENDOTHELIUM free (Kp,uu 0.2–0.5)  2.6–13 nM
      margin vs free EC50 ..........  0.2 – 2.6  →  −0.7 to +0.4 log
```

**Reading.** On this arithmetic elafibranor is the **only Group A compound that plausibly reaches
or exceeds its free EC50 at the retinal endothelium.** That makes it the cleanest *pharmacological
probe* of whether endothelial PPAR engagement does anything in this disease — at the cost of
(i) PPARδ co-agonism confounding the isoform question and (ii) a Michael-acceptor enone at a
120 mg daily dose, which is a genuine reactive-metabolite liability for lifelong use (§8.4).
The Cmax figure is my lowest-confidence number in the report.

#### A5 — Seladelpar (10 mg od) — the control that is better-engaged than the test arm

```
STRUCTURE [DATA]   MW 444.47 | aLogP 5.05 | PSA 64.99 | HBD 1 | RTB 11 | Ro5v 1 | QED 0.49
SMILES    [DATA]   CCO[C@H](COc1ccc(C(F)(F)F)cc1)CSc1ccc(OCC(=O)O)c(C)c1
                   ↑ OCC(=O)O — an UNSUBSTITUTED aryloxy-ACETIC acid. See §8.3.

 1. Cmax, TOTAL                       ~100–200 ng/mL = 0.22–0.45 µM   [KB, low confidence]
 2. fu                                ~0.01                            [KB]
 3. FREE PLASMA                       2.2–4.5 nM                       [CALC]
 4. PPARδ EC50 nominal / free         ~2 nM / 0.2–0.6 nM               [KB/CALC]
      margin in plasma vs PPARδ ....  4 – 22×  →  ABOVE its EC50
 5. PPARα free EC50 (>500× selective) ~100–300 nM
      margin vs PPARα ..............  0.01–0.04  →  −2.0 to −1.4 log
```

**Reading — and this is important for the falsification design.** Seladelpar at clinical dose
plausibly achieves free concentrations **above** its PPARδ EC50, while every PPARα agonist in the
set sits **below** its PPARα EC50. **The isoform falsification control is better target-engaged
than the arm it is controlling.** That makes it unusually informative:

- Seladelpar inert, fibrates active → **supports α-specificity despite the α exposure deficit.**
- Both active → δ or non-PPAR pharmacology is doing the work; the α hypothesis fails.
- Both inert → **uninterpretable**, because the α arm was never dosed to engagement.

It also exposes a limit of my own axis: **exposure is isoform-blind.** Seladelpar, elafibranor
and pemafibrate are near-identical on every physicochemical BRB descriptor. An exposure-driven
ranking therefore *cannot* discriminate PPARα from PPARδ, which means exposure can never be the
property that makes PPARα special.

### 3.3 Summary exposure table — all 15, free retinal concentration vs own target potency

All values `[CALC]` from `[KB]` PK and `[DATA]` structure. "Margin" = log₁₀(free concentration in
the most accessible DR-relevant compartment ÷ free potency for that compound's own primary
target). Positive = engaged.

| # | Compound | Free plasma (Cavg,ss) | Own target & free potency | Best-compartment margin | Engaged? |
|---|---|---|---|---|---|
| C2 | **Melatonin** | 0.5–10 nM | **MT1/MT2 Ki 0.08–0.4 nM** | **+0.7 to +2.0** | **YES** (MT1/2 only) |
| C2 | Melatonin — *antioxidant/PPARα limb* | 0.5–10 nM | 10–1000 µM in vitro | **−3.0 to −5.0** | no |
| D4 | **Candesartan** (from cilexetil) | 1–2 nM | **AT1R Ki 0.2–1 nM, luminal** | **+0.0 to +1.0** | **YES** (vascular only) |
| D4 | Candesartan — *neural retina* | 1–2 nM | AT1R Ki 0.2–1 nM | −1.3 to −0.5 | no |
| A4 | **Elafibranor** | 13–26 nM | PPARα free EC50 5–15 nM | **−0.7 to +0.4** | **MARGINAL** |
| A5 | **Seladelpar** | 2.2–4.5 nM | **PPARδ** free EC50 0.2–0.6 nM | **+0.6 to +1.3** | **YES** (δ, the control) |
| D1 | **Epalrestat** | ~0.17 µM | **AKR1B1 IC50 ~72 nM** | **−1.0 to −0.3** | near-threshold |
| D2 | **MMF** (from DMF) | ~9 µM | KEAP1 — **covalent, cumulative** | n/a (not equilibrium) | **plausible** |
| D3 | **Minocycline** | 1.1–2.2 µM | microglial endpoints 1–50 µM | −2.0 to −1.0 | no |
| A3 | **Pemafibrate** | 12–24 pM | PPARα free EC50 0.02–0.1 nM | −1.6 to −0.2 | no (close) |
| A1 | **Fenofibric acid** | 0.10–0.31 µM | PPARα free EC50 3–30 µM | −3.0 to −1.1 | no |
| A2 | **Fenofibrate** | *= A1 exactly* | *= A1* | *= A1* | no |
| B4 | **Icosapent ethyl / EPA** | free EPA nM–low µM | PPARα free EC50 tens of µM | −2.5 to −1.0 | no (but see §6.3) |
| B2 | **α-Linolenic acid** | homeostatic set point | PPARα free EC50 tens of µM | −2 to −1, **not dose-movable** | no |
| B1 | **Linoleic acid** | homeostatic set point | PPARα free EC50 tens of µM | −2 to −1, **not dose-movable** | no |
| B3 | **Linalool** | no deliverable dose | unmeasured, likely ≫ µM | undefined | unknown |
| C1 | **Quercetin** | free aglycone **<10–50 nM** | all activities 10–100 µM | **−3.0 to −4.0** | **no — worst in set** |

---

## 4. (b) INTERROGATING THE SCOUT'S CENTRAL CLAIM

> **Scout §6.1 / §7:** *"~0.1–0.4 µM free fenofibric acid against a tens-of-micromolar EC50 …
> roughly two orders of magnitude below the EC50, and that is in plasma, before any
> blood–retinal-barrier attenuation at all. … The retina has no analogous uptake system."*

**Verdict in one line: the arithmetic is right, one of its two inputs is wrong, the net
correction is ~1 log in the hypothesis's favour, and three arguments the scout did not make
push back the other way by more than that. Net: CONFIRM the direction, REFINE the magnitude,
and REFUTE one specific sub-claim ("the retina has no analogous uptake system") as too strong.**

I took the five challenges in turn.

### 4.1 Free vs total — is free the right comparison? ❌ **The scout's comparison is inconsistent. This is the real flaw.**

Using *free* plasma concentration is correct in principle. At steady state, for a passively
permeable compound, free plasma = free interstitial = free cytosolic (the free-drug hypothesis),
so a free plasma concentration is the right quantity to compare against an intracellular
receptor's potency.

**But the EC50 is not a free concentration.** A PPARα transactivation EC50 is reported as the
*nominal* concentration added to a cell culture well — and that well contains serum. Charcoal-
stripping (used in PPAR assays to remove endogenous fatty-acid ligands) removes lipids but
**leaves albumin intact**. Fenofibric acid is ~99% bound at plasma albumin (~600 µM); in 10% FBS
(~10-fold less albumin) it would still be perhaps 85–95% bound. **The nominal 30 µM EC50
therefore corresponds to a free EC50 of roughly 1.5–4.5 µM — and in assays run with less serum,
proportionally higher.**

Comparing a rigorously free plasma concentration against a nominal serum-containing EC50 is
apples-to-oranges, and it **systematically inflates the apparent deficit**. Correcting both
sides consistently:

```
Scout's comparison:     0.1–0.4 µM free   vs  30 µM nominal   →  ~100×  (−2.0 log)
Consistent comparison:  0.10–0.31 µM free vs  3–30 µM free    →  10–300× (−1.0 to −2.5 log)
```

The correction is worth **~1 log, with ±1 log of its own uncertainty** — which makes it the
single largest uncertainty in this entire report. **It does not reverse the conclusion. It does
mean "two orders of magnitude" should be stated as "one to two-and-a-half orders of magnitude,
dominated by an unmeasured protein-binding correction."**

**Actionable fix, and it is cheap:** re-run the PPARα transactivation assay for fenofibric acid
and pemafibrate in the presence of **4% human serum albumin**, and report a free-drug-corrected
EC50. One experiment collapses the biggest uncertainty in the whole pipeline. I am flagging this
as data gap #1.

### 4.2 Transactivation EC50 vs binding Kd — which is the right potency measure? ⚠️ **Neither; the right measure is lower than both.**

Fenofibric acid's PPARα *binding* Kd (TR-FRET/SPA displacement) is reported in the low-µM range
`[KB]`, meaningfully tighter than its tens-of-µM transactivation EC50 — the gap reflecting
cell penetration, coactivator recruitment efficiency, and partial agonism.

**I decline to use Kd.** Occupancy without coactivator recruitment produces no transcription;
for a nuclear receptor the transcriptional EC50 is the physiologically meaningful number, and
substituting Kd would flatter the hypothesis dishonestly.

**But there is a legitimate softening that cuts deeper than the Kd question, and the disease
model supplies it.** Model §5.2(a) states that retinal PPARα expression is *decreased* in
diabetes — "the classic setup for an agonist to **restore rather than supraphysiologically
stimulate**." If the therapeutic goal is restoration of basal transcriptional tone rather than
maximal induction, **the relevant benchmark is EC10–EC20, not EC50.** For a Hill-1 curve,
EC20 = EC50/4 and EC10 = EC50/9 — worth a further **0.6–1.0 log**.

Stated plainly: at the retinal endothelium, fenofibric acid plausibly reaches **EC5–EC7**. Five
to seven percent of maximal PPARα target-gene induction, sustained continuously for a decade, in
a tissue that is PPARα-*deficient*, is not obviously nothing. It is also not something I can
claim as demonstrated. **`[UNCERTAIN]` — and this is the strongest honest pro-hypothesis argument
available.**

### 4.3 Does intracellular accumulation occur via ion trapping? ❌ **No — the sign is wrong, and it slightly worsens the picture.**

Ion trapping concentrates **bases in acidic compartments** and **acids in alkaline
compartments**. Cytosolic pH (~7.2) is *more acidic* than plasma pH (7.4). By pH-partition, a
fully ionised monoacid distributes to cytosol at ≈ 10^(7.2−7.4) = **0.63 of its free plasma
concentration** — i.e. ion trapping removes ~37%, it does not add anything.

**The scout did not mention ion trapping; it would not have helped if he had.** It is a small
correction in the *pessimistic* direction and it applies to every acid in the set (A1–A5, B1, B2,
B4, D1, D4, and MMF).

**One genuine intracellular-accumulation mechanism does exist, and it is not ion trapping:
FABP-mediated nuclear channelling.** Retina expresses FABP5 and FABP7; FABP4/5 physically
shuttle fatty-acid ligands to PPARs and are documented to raise the *effective* ligand
concentration at the receptor above bulk free cytosolic concentration `[KB, EMERGING]`. Note the
discipline required here: **a binding sink raises *total* intracellular drug but not *free*
intracellular drug at equilibrium** — only active channelling to the nuclear receptor does
anything. This is a real possible modifier worth perhaps a small factor, **not orders of
magnitude**, and it is unquantified.

### 4.4 Is there a retinal organic-anion uptake transporter that could concentrate a fibrate? ⚠️ **The scout's "no analogous uptake system" is too strong. Refined — but the refinement does not rescue the hypothesis.**

Four transporter families, assessed separately:

**OATP1A2 (SLCO1A2) / OATP2B1 (SLCO2B1) — the scout's claim is overstated here.**
OATP1A2 is expressed at the human BBB luminal membrane and is reported in human retina and RPE
`[KB, EMERGING]`; SLCO2B1 is reported in RPE. Fibrates *are* OATP substrates — pemafibrate is
explicitly an OATP1B1/1B3 substrate. And this project's own data `[DATA]` shows the OATP family
carrying this broad chemotype: quercetin is taken up by **SLCO1A2, 1B1, 1B3, 2A1, 2B1 and 5A1**
(PMID 24947867). **So "the retina has no OATP" is factually wrong.** What is true, and what the
scout should have said, is: *these are low-abundance, low-capacity extrahepatic family members,
not the hepatic OATP1B1/1B3 system whose expression level produces 10–100× hepatic concentration.
No fibrate has been shown to be an OATP1A2 substrate.* **Refined, not refuted — and insufficient.**

**OAT1 (SLC22A6) / OAT3 (SLC22A8) — runs the wrong way.**
At the BBB and RPE, OAT3 operates in the **efflux** direction (CNS→blood, retina→blood) as part
of the organic-anion clearance machinery `[KB]`. This project's data `[DATA]` confirms only
chemotype *recognition*, not direction: linoleic acid decreases OAT1 and OAT3 activity
(PMID 29045746); melatonin inhibits OAT3. **Net: OATs at the BRB are more likely to remove a
fibrate than deliver one.**

**MCT1/3/4 (SLC16A1/3/4) — real, concentrative, and chemically incompatible with fibrates.**
MCTs are abundant at RPE (apical MCT1, basolateral MCT3) and Müller cells, and they *are*
genuinely concentrative for monocarboxylates. Fibrates *are* monocarboxylic acids. **But MCT1's
substrate pocket requires a small, unbranched, sterically unhindered aliphatic monocarboxylate
(lactate, pyruvate, β-hydroxybutyrate).** Fenofibric acid is an α,α-dimethyl *aryloxy*-isobutyric
acid — far too bulky and too hindered. Project data `[DATA]` shows quercetin *inhibiting*
MCT1-mediated benzoic acid uptake (PMID 17976262), which confirms recognition-as-blocker, not
transport. **Verdict: a real exploitable route for small monocarboxylates, closed to this
chemotype.** This is the most specific refutation in this section — and it immediately suggests a
design solution (§9.3b).

**MRP1/4/5 (ABCC1/4/5) and BCRP (ABCG2) — pump outward.**
Luminal at the inner BRB and present on RPE `[KB]`. They export organic anions and, critically,
**glucuronide conjugates** — so any acyl glucuronide formed in retina is actively removed. Net
efflux ratio for an acidic fibrate is >1.

> **Refined claim, replacing the scout's:** *The retina's dominant organic-anion transport vector
> at both barriers runs **outward** (MRP/BCRP/OAT3). The one inward route that exists
> (OATP1A2/2B1) is low-abundance, low-capacity, and unproven for the fibrate chemotype. There is
> no hepatic-grade concentrative uptake for an aryloxy-isobutyric acid. **Retinal free
> concentration will be at or below free plasma — never above it.*** Kp,uu ≤ 1 is therefore a
> hard ceiling, which is the fact that decides §5.

**The one genuine exception — and it belongs to Group B.** The retina possesses a **dedicated,
high-capacity, concentrative uptake system for long-chain ω-3 PUFAs**: **MFSD2A** at the inner
BRB (which transports lysophosphatidylcholine-esterified DHA/EPA) plus FATP/CD36/FABP machinery
at the RPE `[KB, CURRENT CONSENSUS]`. Retinal DHA content is the highest of any tissue in the
body, maintained against a gradient. **This is the single real counterexample to "the retina has
no concentrative uptake transporter" — and it serves exactly the fatty-acid chemotype that this
project's data `[DATA]` identifies as the only genuine direct-binding PPARα ligand class
(linoleic acid, α-linolenic acid, with coactivator recruitment across ≥4 PMIDs).**
That coincidence is the most interesting thing in this analysis and I develop it in §6.3 and §9.3c.

### 4.5 Does chronic steady-state dosing change the picture versus single-dose Cmax? ❌ **It makes it slightly worse, in two independent ways.**

**(i) Cmax overstates average exposure.** The scout used Cmax. Fenofibric acid's t½ is ~20 h
`[KB]`, so once-daily dosing is relatively flat, but Cavg,ss is still ≈0.65 × Cmax. **Using Cmax
flatters the hypothesis by ~1.5×.** And because nuclear-receptor output is a time-integrated
transcriptional response, **Cavg,ss — not Cmax — is the correct exposure metric here.** I used
Cavg,ss throughout §3.2.

**(ii) No tissue accumulation occurs with repeated dosing.** This is where chronic dosing could
in principle have rescued the argument — slow partitioning into a deep tissue compartment
building up over weeks. It does not happen, and **Vd ~0.9 L/kg proves it** (§3.2, line 6). A drug
whose steady-state volume of distribution is barely above extracellular fluid has no deep tissue
compartment to accumulate into. Steady state is reached in ~4 days and nothing further happens
for the next ten years.

**(iii) One real chronic-dosing effect that goes the *other* way, and it is population-specific.**
Diabetic nephropathy with nephrotic-range proteinuria produces **hypoalbuminemia**. For a
99%-bound drug, halving albumin roughly doubles fu. **In advanced diabetic kidney disease, free
fenofibric acid rises — so retinal exposure is genuinely better in exactly the patients with the
worst disease.** This is real and worth ~0.3 log. It is also double-edged: the same rise in free
drug raises myopathy and hepatic toxicity risk, in patients who already cannot clear the renally
eliminated glucuronide (§7.1). **It is a toxicity mechanism as much as an exposure mechanism.**

### 4.6 Net verdict on the scout's claim

| Element of the claim | Verdict | Direction | Magnitude |
|---|---|---|---|
| "~0.1–0.4 µM free fenofibric acid" | **Correct** | — | confirmed; Cavg,ss 0.10–0.31 µM |
| "tens of µM EC50" | **Correct as reported, but it is a *nominal* EC50** | ✅ pro-hypothesis | **+1.0 log** (±1.0) |
| "~two orders of magnitude below" | **Overstated** | ✅ pro-hypothesis | becomes 1.0–2.5 logs |
| "before any BRB attenuation" | **Correct, but compartment-blind** | ✅ pro-hypothesis | **+1.0 log** for endothelium/RPE |
| EC50 is the right benchmark | **Too strict for restoring deficient tone** | ✅ pro-hypothesis | **+0.6–1.0 log** (EC10–EC20) |
| "retina has no analogous uptake system" | **Too strong — OATP1A2/2B1 exist; MFSD2A is a real concentrative route for ω-3** | ✅ pro-hypothesis | unquantified, small for fibrates |
| Ion trapping could help | **Not raised; would not have — wrong sign** | ❌ anti | −0.2 log |
| Cmax used instead of Cavg,ss | **Not raised; flatters the hypothesis** | ❌ anti | −0.2 log |
| Vd ~0.9 L/kg | **Not raised; strongest single anti-argument** | ❌ anti | corroborates low Kp,uu |
| "pemafibrate partly escapes by potency" | **Wrong — potency is cancelled by free fraction** | ❌ anti | reduces 4.8 log to ~1 log |
| "pemafibrate for the retinal-engagement arm" | **Backwards on exposure; right on safety** | ❌ anti | see §7.2 |

**CONFIRMED, WITH REFINEMENT.** The scout's conclusion — *if a PPARα agonist helps this retina,
retinal PPARα agonism in the neural retina is probably not the reason* — **survives, and I
endorse it for the neural-retina compartment.** But the scout overstated the gap by roughly a
log, and more importantly treated "the retina" as one compartment. **In the two compartments
that actually host the strongest PPARα mechanisms — vascular endothelium and RPE — the deficit
is 1.1–3.0 logs rather than 1.8–4.0, and at the favourable end of the range it reaches EC5–EC7
of a receptor the disease has rendered deficient. That is marginal, not absent.**

**Where I disagree outright:** the scout's claim that pemafibrate "partly escapes by potency" is
wrong. Potency bought with lipophilicity does not escape the free-drug constraint — it trades
EC50 for fu at close to a 1:1 exchange rate. Pemafibrate's real advantages are its elimination
route and its sub-milligram daily burden (§7.2, §8.3), not its EC50.

---

## 5. (c) THE BOOTSTRAPPING PARADOX — QUANTIFIED

> **The paradox as posed:** retinal drug exposure rises as the blood–retinal barrier breaks down,
> so the drug arrives in useful amounts only once disease is advanced — but the mechanism is
> only suited to early disease.

### 5.1 How much barrier breakdown would be needed?

Work backwards from the requirement. To reach the free EC50 in **neural retina**:

```
Required retinal free concentration   =  free EC50            =  3–30 µM      [CALC]
Available free plasma concentration   =  Cavg,ss free          =  0.10–0.31 µM [CALC]
Required Kp,uu  (ratio of the two)    =  3 / 0.31  …  30 / 0.10
                                      =  10 – 300             [CALC]
```

**The required Kp,uu is 10–300. Barrier breakdown cannot deliver it, for a reason of principle:**

> **A barrier is a *resistance*, not a *pump*. Removing a resistance drives Kp,uu toward 1. It
> can never drive it above 1. Only a concentrative uptake transporter — consuming energy to move
> drug against its gradient — can produce Kp,uu > 1, and §4.4 establishes that the retina has no
> such transporter for this chemotype.**

So the achievable gain from barrier failure is bounded:

| Barrier state | Kp,uu (neural retina) | Retinal free, fenofibric acid | Margin vs free EC50 |
|---|---|---|---|
| Intact (S0, normoglycaemic control) | 0.01–0.05 | 1–16 nM | −3.5 to −2.3 log |
| Early DR (S1–S2, subclinical leak) | 0.03–0.15 | 3–47 nM | −3.0 to −1.8 log |
| Established DME (S3–S4, frank leak) | 0.2–0.5 | 20–155 nM | −2.2 to −1.3 log |
| **Total barrier failure (theoretical ceiling)** | **1.0** | **0.10–0.31 µM** | **−1.5 to −1.0 log** |

**Maximum achievable gain from complete barrier destruction: ~1.2–1.5 logs (Kp,uu 0.03 → 1.0).**

**And at that ceiling, fenofibric acid is still 10–100× below its free EC50.**

### 5.2 Verdict: the paradox is overstated as a paradox, and understated as a problem

**It is not a paradox, because the premise of the trade-off is false.** The paradox implies a
genuine tension — "if only the barrier would break down, we would have exposure." The arithmetic
says there is no trade to make: **even a completely absent barrier is insufficient.** The problem
is not that the drug arrives too late. It is that it never arrives in sufficient quantity at any
stage, under any barrier condition. The bootstrapping framing misdirects attention onto a
variable (barrier integrity, worth 1.2 logs) and away from the variable that actually decides it
(free plasma concentration relative to free potency, short by 1.0–2.5 logs *at best*).

**Three corollaries:**

**(i) For the systemic lipid mechanism, the paradox inverts completely — barrier failure is the
*indication*, not the obstacle.** If the operative mechanism is reducing the circulating
remnant/apoB lipoprotein *supply* that extravasates through a leaky barrier (model §5.2b, P8.1/
P8.2), then no retinal drug exposure is required at all, and the mechanism is **most valuable
precisely when the barrier leaks** — the lipid/exudative DME phenotype with hard exudate. The
stage profile flips from "only useful early" to "useful whenever lipoprotein is extravasating."
**This single observation dissolves the paradox and is the strategic core of my recommendation.**

**(ii) For the endothelial and RPE compartments, the paradox never applied.** Those cells are on
the blood side (§3.1). Their exposure does not depend on barrier integrity at all — barrier
breakdown neither helps nor hurts them. **The compartments where the mechanism is most plausible
are exactly the compartments the paradox does not describe.**

**(iii) For a compound whose free plasma concentration already exceeds its target potency, the
question is moot.** Melatonin (MT1/MT2), candesartan (luminal AT1R) and seladelpar (PPARδ) are
all engaged in plasma. The barrier debate only bites for compounds that are short anyway.

**Overall: OVERSTATED as a paradox; the real constraint is upstream of it and is not fixable by
disease progression. Score the barrier question as a 1.2-log modifier, not as a gate.**

---

## 6. (d) RANKING ALL 15 BY RETINAL BIOAVAILABILITY

Ranked by **retinal access** (estimated Kp,uu, i.e. free retina ÷ free plasma), **not by
potency**, as instructed. Table 2 then re-ranks by the decision-relevant quantity — access
*times* achievable dose *relative to that compound's own target*.

### 6.1 Table 1 — Rank by retinal access (Kp,uu)

| Rank | Compound | MW | aLogP | PSA | HBD | RTB | Ro5v | Ionisation at pH 7.4 | Est. Kp,uu | Basis |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **Melatonin** (C2) | 232.28 | 1.86 | 54.12 | 2 | 4 | 0 | **neutral** | **~1.0** `+ synthesis` | `[DATA]` descriptors; `[KB]` BBB |
| **2** | **Linalool** (B3) | 154.25 | ~2.8 | ~20.2 | 1 | 4 | 0 | **neutral** | **~1.0** | all `[KB]` — absent from project NP file |
| **3** | **Icosapent ethyl → EPA** (B4) | 330.51 | 6.47 | 26.30 | 0 | 14 | 1 | acid (as EPA) | **≥1.0 (total ≫1)** | `[DATA]` + MFSD2A/FATP `[KB]` |
| **4** | **α-Linolenic acid** (B2) | 278.4 | ~6.5 | 37.3 | 1 | 14 | 1 | acid | **~0.5** | `[KB]` — not preferred retinal substrate |
| **5** | **Linoleic acid** (B1) | 280.4 | ~6.8 | 37.3 | 1 | 14 | 1 | acid | **~0.5** | `[KB]` |
| **6** | **Minocycline** (D3) | 457.48 | 0.19 | **164.63** | 5 | 3 | 0 | **zwitterion/amphoteric** | **0.1–0.3** | `[DATA]`; CNS-penetrant tetracycline `[KB]` |
| **7** | **MMF** (from DMF, D2) | 130.1 | ~0.1 | ~63 | 1 | 2 | 0 | acid | **0.1–0.3** | `[KB]` — *not* the `[DATA]` row (Trap 2) |
| **8** | **Epalrestat** (D1) | 319.41 | 2.92 | 57.61 | 1 | 4 | 0 | acid | **0.05–0.2** | `[DATA]` + `[KB]` |
| **9** | **Fenofibric acid** (A1) | 318.76 | 3.81 | 63.60 | 1 | 5 | 0 | acid | **0.03–0.15** | `[DATA]`; Vd 0.9 L/kg `[KB]` |
| **10** | **Fenofibrate** (A2) | 360.84 | 4.68 | 52.60 | 0 | 6 | 0 | *(neutral ester — never circulates)* | **= A1 exactly** | `[DATA]` metabolism row |
| **11** | **Elafibranor** (A4) | 384.50 | 5.16 | 63.60 | 1 | 7 | 1 | acid | **0.02–0.1** | `[DATA]` + `[KB]` |
| **12** | **Seladelpar** (A5) | 444.47 | 5.05 | 64.99 | 1 | 11 | 1 | acid | **0.02–0.08** | `[DATA]` + `[KB]` |
| **13** | **Pemafibrate** (A3) | 490.56 | 5.55 | **94.26** | 1 | **13** | 1 | acid | **0.01–0.05** | `[DATA]`; OATP hepatoselective `[KB]` |
| **14** | **Candesartan cilexetil** (D4) | **610.67** | 6.32 | **143.34** | 1 | 10 | **3** | **di-anion** (active moiety) | **0.01–0.03** | `[DATA]`; Vd 0.13 L/kg `[KB]` |
| **15** | **Quercetin** (C1) | 302.2 | ~1.5 | **131** | **5** | 1 | 0 | phenol; **circulates conjugated** | **≤0.01** | `[DATA]` ABCB1/ABCG2 efflux; `[KB]` F<2% |

**Note the inversion against Group A's potency order.** Potency rank within Group A is
pemafibrate ≫ elafibranor > seladelpar ≫ fenofibric acid. Retinal-access rank is the **exact
reverse**: fenofibric acid > elafibranor > seladelpar > pemafibrate. This is not coincidence —
it is the same lipophilicity axis read in two directions. **Every step up in PPARα potency in
this series was bought with MW, aLogP, rotatable bonds and protein binding, which is to say it
was bought by paying the retinal-access price.** `[DATA]`: MW 318.76 → 490.56, aLogP 3.81 →
5.55, RTB 5 → 13, QED 0.85 → 0.24 across that progression.

### 6.2 Table 2 — Re-ranked by achievable engagement (the decision-relevant order)

| Rank | Compound | Engagement verdict | Why it moved |
|---|---|---|---|
| 1 | **Melatonin** (MT1/MT2 only) | **Engaged** | Access #1 *and* a sub-nanomolar receptor |
| 2 | **Seladelpar** (PPARδ) | **Engaged** | Modest access, but a 2 nM target and adequate dose |
| 3 | **Candesartan** (luminal AT1R) | **Engaged** | Access #14, but the target is on the blood side |
| 4 | **Elafibranor** (PPARα/δ) | **Marginal — best in Group A** | Access #11, but free plasma ≈ free EC50 |
| 5 | **MMF** (KEAP1) | **Plausible — covalent** | Cumulative adduction escapes the equilibrium argument |
| 6 | **Epalrestat** (AKR1B1) | **Near-threshold** | Free plasma = 2.4 × IC50; best acid in the set |
| 7 | **Pemafibrate** (PPARα) | **Below, close** | −0.2 to −1.6 log at endothelium |
| 8 | **Minocycline** | Below | −1 to −2 log |
| 9 | **Fenofibric acid** (PPARα) | **Below** | −1.1 to −3.0 log |
| 10 | **Fenofibrate** | = #9 | identical molecule in vivo |
| 11 | **Icosapent ethyl / EPA** | Delivered but not engaged | Total retinal ω-3 rises; free ligand does not |
| 12–13 | **Linoleic / α-linolenic acid** | **Not dose-movable** | Already at homeostatic set point |
| 14 | **Linalool** | Undefined | Perfect access, no deliverable dose |
| 15 | **Quercetin** | **Not engaged, by 3–4 logs** | Worst in set on every axis |

### 6.3 What the three designed controls actually tell us

**MELATONIN (C2) — the exposure control. It fires, and it fires against the whole set.**

Melatonin is the cleanest possible positive control for retinal access: MW 232.28, aLogP 1.86,
PSA 54.12, HBD 2, Ro5v 0, QED 0.84 `[DATA]` — every descriptor inside the model §6.2 favourable
band, **neutral at pH 7.4**, not a P-gp substrate, with brain Kp,uu ~0.5–1 `[KB]`. It is
additionally **synthesised in situ** by retinal photoreceptors (AANAT/ASMT), so local nocturnal
retinal concentration is independent of, and can exceed, plasma. **It lands at #1 and nothing
else is close.**

**And it still fails.** Oral melatonin has F ~3–15% (massive CYP1A2 first-pass) and t½ 30–60 min
`[KB]`; 3–10 mg gives plasma Cmax ~1–20 nM, free ~0.5–10 nM. Against:

- **MT1/MT2 (Ki 0.08–0.4 nM):** engaged, 5–100× over Ki. ✅
- **Antioxidant / anti-apoptotic effects (10–1000 µM in vitro):** **3–5 logs short.** ❌
- **PPARα:** no measured EC50; the project's PPARA rows for melatonin are CTD
  "protects-expression-against-an-insult" associations, not engagement `[DATA]`, and the required
  concentration is certainly ≫ µM. **≥4 logs short.** ❌
- Even heroic dosing (50–100 mg, reaching ~1 µM `[KB]`) remains 1–3 logs below the antioxidant
  range, and buys daytime sedation.

> **What melatonin's position means — the central result of this section.**
> **Access is necessary and not sufficient.** The one compound with unambiguous retinal access
> can only engage the one target in its profile that happens to be sub-nanomolar. Its 19/27
> DR-target matrix row `[DATA]` is a CTD-expression artifact describing effects at concentrations
> it cannot reach. **Melatonin's real pharmacology at achievable exposure is MT1/MT2-mediated
> chronobiology and receptor-dependent neuroprotection — not the antioxidant/PPARα story the
> matrix row implies.**
>
> **And the complement:** combining melatonin's result with Group A's, **the candidate set
> contains no compound that has both retinal access and sufficient potency for the hypothesised
> mechanism.** Group A has potency without access; melatonin has access without potency. That is
> the gap a medicinal chemistry programme would have to close (§9.3), and no amount of
> re-ranking the existing 15 closes it.

**DIMETHYL FUMARATE (D2) — informative in a way the brief did not anticipate.**

Its `[DATA]` row (MW 144.13, PSA 52.60, HBD 0, Ro5v 0) is the best in the set — **and it is the
wrong molecule** (Trap 2, §2.3). The circulating species MMF is an acid (MW 130.1, fu ~0.6,
Cmax ~15 µM after 240 mg `[KB]`), giving free plasma ~9 µM and, at Kp,uu 0.1–0.3, retinal free
~1–3 µM. **That is a genuinely substantial retinal concentration — the highest absolute free
retinal concentration of any candidate in this set.**

But the reason DMF is informative is different and more important: **its mechanism is covalent
and cumulative.** KEAP1 cysteine alkylation is irreversible; the pharmacological effect
integrates total adduct formation over time rather than tracking instantaneous free
concentration. **DMF is the only candidate in the set for which the entire free-drug/EC50
argument that governs §3–§5 simply does not apply.** Every equilibrium-binding candidate is
judged against a potency threshold; a covalent one is judged against a cumulative dose.

Honest counterweight: DMF is itself a Michael acceptor, and **most of the administered dose is
consumed by glutathione in gut wall and plasma before any reaches retina** `[KB]`, which is also
why it causes GSH depletion and flushing. The retinal fraction is small but the mechanism is
unforgiving of small. And the brief's scoring prior — *"antioxidant as the sole mechanism —
repeatedly null in DR"* — bears directly on the Nrf2 limb.

**MINOCYCLINE (D3) — good access, disqualified downstream.**

Access rank #6 and genuinely impressive for a 457-Da molecule with **PSA 164.63 and HBD 5**
`[DATA]` — a flat Veber failure that nevertheless penetrates CNS, because minocycline is the most
lipophilic tetracycline, amphoteric rather than permanently charged, and a poor P-gp substrate
`[KB]`. Free plasma 1.1–2.2 µM, retinal free ~0.1–1 µM, against microglial endpoints at 1–50 µM
— **1–2 logs short, which is better than any Group A compound achieves.**

**It is nonetheless the clearest "no" in the set on chronic-dosing grounds** (§7.8), and one of
its liabilities is specifically ophthalmic.

### 6.4 The Group B exception that deserves elevating

**Icosapent ethyl (B4) is the only candidate with a credible *concentrative* retinal uptake
route.** `[DATA]`: MW 330.51, PSA 26.30, HBD 0 — the lowest PSA in the entire set. `[KB]`: the
ethyl ester is hydrolysed to EPA, and EPA/DHA are actively transported into retina via
**MFSD2A** (as LPC-ω3) and RPE FATP/CD36, maintaining the highest ω-3 content of any tissue
against a concentration gradient. Oral ω-3 supplementation measurably raises retinal EPA/DHA.

**And the chemotype coincidence is real:** this project's `[DATA]` identifies linoleic acid and
α-linolenic acid as the *only* compounds among 143 PPARA rows with binding **plus** activation
**plus** coactivator recruitment (NCOA1/NCOA2/CREBBP) across ≥4 PMIDs. **The one ligand class
with genuine direct-binding PPARα evidence in this dataset is also the one class with a
dedicated concentrative retinal transporter.**

**The honest deflation:** retinal *total* ω-3 rises, but free (non-esterified, non-FABP-bound)
EPA does not — it is immediately esterified into membrane phospholipid and buffered by FABPs.
**PPARα responds to free ligand, and free EPA stays 1–2.5 logs below the tens-of-µM EC50 of the
fatty-acid ligand class.** So B4 delivers the molecule and not the pharmacology. It is still the
most interesting exposure result in the set, and it is the empirical proof-of-concept behind the
delivery recommendation in §9.3c.

### 6.5 Why Group B compounds cannot be dosed into relevance at all

**Linoleic acid (B1) and α-linolenic acid (B2) have the strongest PPARα engagement evidence in
the project `[DATA]` and are the least deliverable compounds in the set — for a reason that has
nothing to do with the barrier.**

They are **endogenous constituents sitting at a homeostatically defended set point.** Plasma
total linoleic acid is ~2–3 mM, overwhelmingly esterified and albumin-bound; free LA is nM–low
µM and tightly buffered. Aggressive dietary manipulation moves plasma LA by **less than 2-fold**
`[KB]`. **PPARα in vivo is already continuously exposed to these ligands at their physiological
concentration; administering more does not create a new pharmacological state.** No formulation,
prodrug or delivery system changes this — the constraint is homeostasis, not permeability.

**Wrong-sign risk for B1 specifically.** Linoleic acid is the precursor of **HODEs and 4-HNE**,
the dominant lipid-peroxidation products of ω-6 `[KB]`. Supplying additional ω-6 substrate to a
hyperglycaemic, oxidatively stressed retina (P5) is plausibly **net harmful**. B1 is the
compound with the best mechanistic evidence and the worst risk-benefit in the entire set.

---

## 7. (e) CHRONIC-DOSING ADMET IN THE ACTUAL PATIENT POPULATION

**Population constraints driving every assessment below** (brief §5, model §3.3–3.4): diabetic
adults, **renal impairment is the norm not the exception**, plus near-universal statin, metformin,
RAS blocker and antiplatelet therapy, frequently SGLT2i/GLP-1, sulfonylurea, insulin, diuretic,
and in CKD a phosphate binder and oral iron. **Dosing is lifelong**, starting in asymptomatic
disease — which sets the safety bar at the level of a preventive agent, not a therapeutic one.

### 7.0 The class warning that frames Group A: gemfibrozil, and why it does not transfer

The scout correctly excluded gemfibrozil. The reason is worth stating precisely, because it is
the reference hazard for this entire class **and because it is isolated to one member**:

> **Gemfibrozil 1-O-β-glucuronide is a mechanism-based (irreversible) inactivator of CYP2C8,
> and gemfibrozil itself inhibits OATP1B1 and UGT-mediated statin glucuronidation** `[KB]`. The
> combined effect raises repaglinide exposure ~8-fold and simvastatin acid ~3-fold, producing
> the rhabdomyolysis signal that defines the fibrate class's reputation. In this population —
> universally statin-treated, frequently on a sulfonylurea or glinide — gemfibrozil would be
> close to contraindicated.
>
> **Critically, this does NOT transfer to fenofibrate/fenofibric acid, which inhibits neither
> CYP2C8 nor OATP1B1 and has a markedly lower statin-myopathy signal `[KB]`.** The exclusion of
> gemfibrozil is correct; using it to down-score the class would be a category error. This is
> the ADMET analogue of the brief's isoform-discipline instruction.
>
> **It transfers in the opposite direction to pemafibrate, which is a CYP2C8 *substrate*:**
> see §7.2.

### 7.1 Fenofibric acid (A1) / fenofibrate (A2) — Tier **C**, population-mismatched

**ABSORPTION.** `[DATA]` MW 318.76, aLogP 3.81, PSA 63.60, HBD 1, HBA 3, RTB 5, **Ro5v 0,
QED 0.85 — the best drug-likeness in Group A and among the best in the whole set.**
Classic micronised fenofibrate has a **large positive food effect** (up to ~35% higher
absorption fed) `[KB]`; nanocrystal fenofibrate, **choline fenofibrate** and fenofibric acid
tablets are food-independent. `[DATA]` confirms choline fenofibrate (CHEMBL1201745) carries
identical descriptors to CHEMBL981 — same active moiety, different salt.
**Recommendation: in an elderly polypharmacy population with irregular meals, use a
food-independent formulation and skip the esterase step entirely — i.e. A1, not A2.**

**DISTRIBUTION.** ~99–99.5% albumin bound; **Vd ~0.9 L/kg** `[KB]` — essentially extracellular
water, confirming negligible tissue distribution (§3.2). **Albumin-displacement interactions are
real:** fenofibric acid displaces warfarin and, combined with CYP2C9 inhibition, produces
clinically significant INR elevation. In **nephrotic-range proteinuria** (common in diabetic
nephropathy) hypoalbuminaemia raises fu — more free drug, more exposure, more toxicity (§4.5iii).

**METABOLISM.** `[DATA]`: esterase de-esterification (fenofibrate→fenofibric acid, liver,
"more or less completely converted"), then **UGT acyl glucuronidation** as the dominant route;
a minor reductive metabolite with similar activity, also glucuronidated. UGT1A9/1A3/2B7 `[KB]`.
Minimal CYP oxidation of the drug itself — **but it is a moderate inhibitor of CYP2C9, CYP2C19
and CYP2A6** `[KB]`.
> **Population-specific DDI the scout did not flag: CYP2C9 inhibition + a sulfonylurea.**
> Glipizide, glibenclamide and glimepiride are CYP2C9 substrates. Fenofibrate raises their
> exposure and **potentiates hypoglycaemia** — which the brief (§4) lists explicitly as a
> scoring negative. Also warfarin (INR), phenytoin.

**EXCRETION.** **Renal — >60% of dose as the glucuronide conjugate** `[DATA]` corroborates the
route ("mainly excreted in the urine as a glucuronide conjugate"). `[KB]`: **dose-reduce in
eGFR 30–59; contraindicated below 30.**

> **This is the decisive problem, and it compounds.** eGFR <60 is extremely common in a
> retinopathy population — retinopathy and nephropathy are the same microvascular disease in two
> organs and they track together. **The patients with the most retinopathy have the most
> nephropathy and therefore receive the lowest dose — of a drug whose exposure margin is already
> 1–3 logs short.** The dose reduction directly attacks the only variable that was keeping the
> hypothesis alive. A large fraction of the target population is excluded outright.

**Also:** reversible **10–20% serum creatinine rise** `[KB]` — not true nephrotoxicity, but it
**confounds eGFR monitoring in a nephropathy population**, where distinguishing a drug effect
from disease progression is exactly what you need to be able to do. Plus **homocysteine elevation
(~20–40%)** of uncertain significance in a high-CV-risk group. Plus cholelithiasis (increased
biliary cholesterol saturation), transaminase elevation, and rare myopathy.

**VERDICT C.** Best drug-likeness, highest free plasma concentration of any PPARα agonist here,
cheapest, once-daily, decades of chronic-use safety data, and the lowest-reactivity acyl
glucuronide in Group A (§8.2). **Undone by a renal elimination route that is squarely mismatched
to this population**, plus a CYP2C9-mediated hypoglycaemia interaction and a creatinine rise
that sabotages the monitoring you most need.

### 7.2 Pemafibrate (A3) — Tier **B**, best chronic-safety fit, worst retinal access

**ABSORPTION.** `[DATA]` MW 490.56, aLogP 5.55, PSA 94.26, RTB 13, Ro5v 1, **QED 0.24 — worst in
Group A**. 0.2 mg bid; no major food effect `[KB]`. Twice-daily dosing is a mild adherence
negative against fenofibrate's once-daily.

**DISTRIBUTION.** >99.8% bound, low Vd, and **OATP1B1/1B3-mediated hepatic uptake by design**
`[KB]`. Hepatoselectivity is the molecule's defining feature: it concentrates where its
transcriptional work is wanted and is actively kept out of everywhere else.

**METABOLISM.** CYP2C8 and CYP2C9 oxidation plus UGT conjugation `[KB]`.
> **Population-specific DDI the scout did not flag: clopidogrel.** Clopidogrel's **acyl
> glucuronide metabolite is a potent mechanism-based inactivator of CYP2C8** `[KB]` — the same
> mechanism as gemfibrozil's. **Clopidogrel is an antiplatelet, a drug class the brief lists as
> near-universal in this population.** Co-administration raises pemafibrate exposure
> substantially. Gemfibrozil co-administration is frankly contraindicated for the same reason.
> This is a real, specific, population-relevant interaction.

**EXCRETION.** **Hepatobiliary; renal excretion negligible. No dose adjustment required in
moderate CKD** `[KB]`. **This is the single most valuable ADMET property of any compound in this
analysis for this population** — it is the only Group A member that can actually be given, at
full dose, to the patients who have the disease.

**TOXICITY.** Minimal creatinine rise (so eGFR monitoring stays interpretable — the inverse of
fenofibrate's problem), minimal homocysteine effect, low statin-myopathy signal, routine ALT
monitoring. **And at 0.4 mg/day the total daily covalent burden from any reactive metabolite is
~360× lower than fenofibrate's — below any plausible idiosyncratic-toxicity threshold (§8.3).**

**VERDICT B — and the clearest ADMET recommendation in this report, with a caveat about *why*.**
Pemafibrate is the right molecule for this population. **But the scout's justification for it
was wrong.** The scout chose it as "the only molecule potent and selective enough to actually
test the [retinal] hypothesis." §3.2 and §4.6 show potency does not buy engagement — pemafibrate
beats fenofibric acid at the endothelium by ~1 log, not ~5 — and §6.1 ranks its retinal access
**last in Group A**, by design. **If the mechanism is retina-intrinsic, pemafibrate is the worst
available probe, and a negative result with it would be uninterpretable. If the mechanism is
systemic/hepatic, pemafibrate is the best available drug and its hepatoselectivity is a feature.
The right pick, for the opposite reason.**

### 7.3 Elafibranor (A4) — Tier **D** for chronic use

`[DATA]` aLogP 5.16, Ro5v 1, QED 0.41. **Structural alert: the SMILES carries an α,β-unsaturated
ketone** (`C(=O)/C=C/`) — a **Michael acceptor**, flagged under PAINS in the skill rubric. At
80–120 mg/day this is a substantial daily electrophile load (contrast pemafibrate's 0.4 mg),
with GSH adduction and idiosyncratic hepatotoxicity risk over a lifetime of dosing `[KB]`. The
thioanisole adds sulfoxide/sulfone metabolites. PPARδ co-agonism introduces an uncharacterised
second axis. **A creatinine-rise signal in a CKD population is an additional specific negative.**
Best exposure margin in Group A (§3.2) and the worst chronic-safety profile — a genuinely
awkward pairing. **Use as a pharmacological probe, not as a chronic preventive agent.**

### 7.4 Seladelpar (A5) — Tier **C**, and a control rather than a candidate

`[DATA]` aLogP 5.05, RTB 11, Ro5v 1. PPARδ-selective, so it is not the hypothesis. Hepatic
elimination with ALT monitoring `[KB]`. **Structural alert: `OCC(=O)O` — an unsubstituted
aryloxy-acetic acid, the most acyl-glucuronide-reactive scaffold in Group A (§8.3).** Its
exposure profile is physicochemically indistinguishable from the other acid fibrates, which is
itself the informative observation (§3.2, §6.1).

### 7.5 Icosapent ethyl (B4) — Tier **B** on ADMET, with two population-specific hazards

**A:** 2 g bid = **4 g/day, four 1-g capsules**, with food. Pill burden is a real adherence
problem in a population already taking 8–12 medications `[KB]`.
**D:** EPA distributes into plasma lipoproteins and membrane phospholipid; retinal uptake is
concentrative (§6.4).
**M:** **β-oxidation, not CYP — essentially zero CYP-mediated DDI potential.** In a polypharmacy
CKD population this is a genuine and underrated advantage; it is the cleanest metabolic profile
in the entire candidate set.
**E:** no renal adjustment required.
**T — two specific hazards for *this* population:**
1. **Bleeding.** EPA prolongs bleeding time and inhibits platelet aggregation. **Antiplatelet
   therapy is near-universal here** (brief §5). Additive bleeding risk is the principal concern.
2. **Atrial fibrillation.** A consistent class signal for high-dose ω-3 `[KB]`, in a population
   with high baseline AF prevalence and, on anticoagulation, compounding hazard 1.

**VERDICT B.** Excellent metabolic and renal profile, unique concentrative retinal delivery,
weak target engagement (§6.4), and two real bleeding/arrhythmia liabilities.

### 7.6 Melatonin (C2) — Tier **B**, with one diabetes-specific liability

**A:** oral F 3–15%, enormous inter-individual variability from CYP1A2 first-pass; t½ 30–60 min
IR `[KB]`. **A sustained-release formulation is mandatory** for anything other than sleep onset.
**M:** CYP1A2 → 6-hydroxymelatonin → sulfate. **DDI: fluvoxamine raises melatonin ~20×; smoking
(CYP1A2 induction) lowers it; oral contraceptives and ciprofloxacin raise it** `[KB]`.
**E:** renal excretion of the inactive sulfate — no meaningful CKD adjustment.
**T:** exceptionally benign. **One real, mechanism-grounded, diabetes-specific caveat:**
> **MTNR1B (the MT2 receptor) is an established T2D risk locus, and melatonin acutely impairs
> glucose tolerance — particularly in risk-allele carriers and when dosed near a meal** `[KB],
> general endocrinology, not DR`. Giving a melatonin receptor agonist chronically to a diabetic
> population is not pharmacologically neutral. **Dose at bedtime, well separated from food, and
> treat HbA1c as a monitored safety endpoint.**

### 7.7 Dimethyl fumarate (D2) — Tier **C**, two liabilities that specifically bite in CKD

**A:** delayed-release; the food effect is used deliberately to blunt flushing. **Flushing (>30%)
and GI intolerance are the dominant discontinuation drivers** `[KB]`.
**M:** presystemic esterase hydrolysis to MMF, which enters the TCA cycle and is exhaled as CO₂.
**Zero CYP involvement — outstanding in polypharmacy.**
**E:** negligible renal excretion of parent; **no renal dose adjustment** — good for CKD.
**T — the two that matter here:**
1. **Lymphopenia**, dose-limiting, requiring periodic CBC, with **PML risk in prolonged severe
   lymphopenia** `[KB]`. Lifelong immunosuppression in a diabetic population with elevated
   baseline infection risk is a poor trade for an asymptomatic indication.
2. **Fumarate-associated proteinuria and Fanconi-type proximal tubulopathy** `[KB]` — reported
   for the fumarate class and specifically unwelcome in diabetic nephropathy, where proteinuria
   is the disease-progression marker you are trying to read.

### 7.8 Minocycline (D3) — Tier **D/F** for chronic use. Disqualified.

**A:** good oral F, **but chelated by Ca²⁺/Mg²⁺/Fe²⁺/Al³⁺** `[KB]`. **CKD patients take calcium
acetate, sevelamer, lanthanum and oral iron** — a direct and frequent absorption DDI in exactly
this population.
**E:** predominantly hepatic/biliary — **the one tetracycline not requiring renal dose
adjustment**, a genuine advantage.
**T — and this is where it ends:** vestibular toxicity (dizziness/vertigo, 10–20%); **permanent
blue-grey pigmentation of skin, sclera, conjunctiva, teeth, nail beds and bone on chronic use**
(the retina/choroid melanin depot that aids penetration is the same mechanism); drug-induced
lupus; autoimmune hepatitis; DRESS; and **benign intracranial hypertension with papilledema**.
> **That last one is disqualifying on its own.** A chronic oral agent for a *vision-preserving*
> indication that can itself cause papilledema and visual-field loss has an unacceptable
> risk-benefit in an asymptomatic population — and it is a general, non-DR drug-safety fact.

**VERDICT D/F — good retinal access, unusable chronically.** Minocycline's position is the mirror
image of melatonin's: both reach the retina, and neither can be given at a dose and duration that
would matter.

### 7.9 Candesartan cilexetil (D4) — Tier **B** on safety, near-zero incremental value

`[DATA]` MW 610.67, aLogP 6.32, PSA 143.34, **Ro5v 3, QED 0.14** — the worst descriptors in the
set, but they describe the **ester prodrug**, hydrolysed in gut wall to candesartan `[KB]`.
**A:** ~15% F. **D:** >99% bound, **Vd ~0.13 L/kg — essentially plasma-confined**, a di-anion
(tetrazole + carboxylate). It is the least tissue-distributed molecule here, which does not
matter, because **its AT1R target on retinal endothelium is luminal** (§3.1) and it binds
insurmountably with a slow off-rate. **M:** minimal CYP. **E:** ~2/3 biliary, 1/3 renal.
**T:** hyperkalaemia and acute eGFR decline in diabetic CKD; AKI with NSAIDs or volume depletion;
contraindicated in pregnancy.

> **The decisive objection is not safety — it is redundancy.** RAS blockade is already standard
> of care for diabetic nephropathy and hypertension, so **most of the target population is
> already taking an ARB or an ACE inhibitor.** Dual RAS blockade increases hyperkalaemia and AKI
> with no benefit and is contraindicated. **Candesartan's mechanism is already deployed in this
> population; its incremental value as a new DR therapy is close to zero.** This is a purely
> practical, non-DR-specific argument and it is, I think, decisive.

### 7.10 Epalrestat (D1) — Tier **C**

`[DATA]` MW 319.41, aLogP 2.92, PSA 57.61, Ro5v 0, QED 0.68 — clean. **Best free-concentration-
to-own-target-potency ratio of any acid in the set** (free plasma ~0.17 µM vs AKR1B1 IC50
~72 nM `[KB]`; AKR1B1 is abundant in Müller cells and pericytes). Against that: **the SMILES
carries a rhodanine core** (`SC(=S)N` + thiocarbonyl) — explicitly listed under PAINS in the
skill rubric, with frequent-hitter and reactivity implications; an **N-substituted glycine
carboxylic acid with an unsubstituted α-carbon**, i.e. the reactive acyl-glucuronide tier (§8.3);
hepatotoxicity reports; tid dosing; partial renal elimination; and limited availability outside
Japan/India/China `[KB]`. The brief's prior against single-branch blockade downstream of the ROS
node (the P1 class precedent) applies directly.

### 7.11 Quercetin (C1) — Tier **F**

Oral F **<2%**; circulates almost entirely as quercetin-3-glucuronide and 3'-sulfate, with free
aglycone typically **below assay limits** `[KB]`. **`[DATA]` dual efflux substrate: ABCB1
("ABCB1 protein results in increased transport of quercetin"; "abcb1 protein results in decreased
abundance of quercetin") and ABCG2 ("ABCG2 protein affects the export of quercetin").** Catechol
B-ring → COMT methylation, auto-oxidation to a redox-cycling ortho-quinone — the skill rubric's
catechol PAINS alert. **3–4 logs between achievable free concentration and every reported
activity, before the barrier is even considered.**
> **And a concrete, data-backed DDI in exactly this population: `[DATA]` quercetin inhibits
> SLCO1B1-mediated atorvastatin import (PMID 22394605), plus SLCO2B1, ABCB1, ABCC1/4/5 and
> CYP3A4/2C9.** OATP1B1 inhibition is the canonical statin-myopathy mechanism, in a universally
> statin-treated population. **A supplement-grade compound with a transporter-mediated statin
> interaction and no achievable exposure is a liability, not a candidate.**

### 7.12 Linalool (B3), linoleic acid (B1), α-linolenic acid (B2)

**Linalool:** physicochemically the best passive BRB profile in the set (`[KB]` MW ~154, neutral,
PSA ~20) and **no oral drug product, no clinical PK, rapid oxidative and glucuronide clearance,
volatility, and hydroperoxide oxidation products that are established contact allergens.** Its
PPARA-mutant genetic-dependency evidence `[DATA]` is the best engagement evidence in Group B, and
there is no dose to give. **Access without a deliverable dose is worth nothing.**

**B1/B2:** see §6.5 — the constraint is homeostasis, not ADMET, and no formulation changes it.
B1 additionally carries wrong-sign oxidation chemistry. Both are safe, both are food.

---

## 8. (f) ACYL GLUCURONIDE REACTIVITY AND LIFELONG DOSING

### 8.1 The mechanism, and why it is the right question to ask of this class

An acyl glucuronide (AG) is an **ester** between the drug's carboxylate and glucuronic acid.
Unlike ether (O-) glucuronides of phenols and alcohols, acyl esters are chemically reactive by
two routes `[KB]`:

1. **Intramolecular acyl migration.** The 1-O-β-acyl glucuronide migrates to the 2-, 3- and 4-OH
   positions. The migrated isomers exist in equilibrium with **open-chain aldehyde** forms, which
   condense with protein lysine ε-amino groups to form a Schiff base that undergoes **Amadori
   rearrangement** into a stable, glycation-like covalent adduct.
2. **Direct transacylation.** The intact ester acylates protein nucleophiles (Lys, Ser, Cys)
   directly, transferring the drug onto protein.

Both routes generate **drug–protein neoantigens**, the leading mechanistic hypothesis for
idiosyncratic hepatotoxicity and hypersensitivity among carboxylic-acid drugs — the class that
produced the benoxaprofen, ibufenac, zomepirac, tolmetin and oral-bromfenac withdrawals `[KB]`.
**Eleven of the fifteen candidates here carry a carboxylic acid** (A1–A5, B1, B2, B4 as EPA, D1,
D4 as candesartan, and MMF from D2). This is therefore the correct question to ask of this set.

**The project's own data attests the class.** `[DATA]`: 16 distinct acyl/ester-glucuronide
formation rows in `chembl_drug_metabolism.csv`, including the canonical reactive-AG reference
compounds **diflunisal** ("Glucuronide conjugation at the carboxylic acid forming an ester") and
**ketoprofen** ("Glucuronide acid conjugates to the hydroxyl of the carboxylic acid group"),
plus salicylic acid, oxaprozin, celecoxib's acid metabolite — and **reduced fenofibric acid
("Glucuronide conjugation to the carboxylic acid forming an ester")**. The fibrate scaffold's AG
formation is documented in this project, not merely asserted.

### 8.2 The reactivity SAR — α-carbon substitution is the controlling variable

AG degradation half-life (the standard reactivity proxy — shorter t½ = faster migration = more
reactive) is governed principally by **steric hindrance at the carbon α to the carboxyl** `[KB]`:

| Tier | α-carbon | Example class | AG t½ | Reactivity |
|---|---|---|---|---|
| **I — most reactive** | **Unsubstituted** (–CH₂–COOH) | acetic acids: zomepirac, tolmetin, diclofenac; **aryloxyacetic acids** | ~0.3–1 h | **High** |
| **II — intermediate** | **Mono-substituted** (–CHR–COOH) | 2-arylpropionic acids (profens): ketoprofen, ibuprofen | ~1–2 h | Moderate |
| **III — least reactive** | **Di-substituted / quaternary** (–CR₂–COOH) | α,α-dimethyl acids | many hours | **Low** |

**I applied this SAR directly to the SMILES strings in the blinded dataset `[DATA]`.**

### 8.3 Per-compound assessment, read off the structures

| Compound | Acid substructure `[DATA]` | α-carbon | Tier | Daily dose | **Daily covalent burden** | Verdict |
|---|---|---|---|---|---|---|
| **Fenofibric acid** (A1/A2) | `...Oc1ccc(...)cc1)C(=O)O` with `C(C)(C)` | **Quaternary** | **III** | 145 mg | moderate × low reactivity | **LOW concern** |
| **Pemafibrate** (A3) | `CC[C@@H](Oc1...)C(=O)O` | **Mono-sub (α-ethyl)** | **II** | **0.4 mg** | **negligible** | **LOW concern** |
| **Elafibranor** (A4) | `OC(C)(C)C(=O)O` | **Quaternary** | **III** | 120 mg | low *from the AG* | **LOW (AG); HIGH from the enone** |
| **Seladelpar** (A5) | **`OCC(=O)O`** | **UNSUBSTITUTED** | **I** | 10 mg | low dose, high reactivity | **ELEVATED — highest AG tier in Group A** |
| **Epalrestat** (D1) | `N(CC(=O)O)` + rhodanine | **UNSUBSTITUTED** | **I** | 150 mg | **high dose × high reactivity** | **ELEVATED** |
| **Candesartan** (D4) | aryl `C(=O)O` (benzimidazole-7-carboxylic) | aryl-attached | II–III | 8–32 mg | low | LOW (decades of use) |
| **MMF** (D2) | fumarate half-ester | n/a — Michael acceptor, not an AG | — | 480 mg | **high, by design** | see §7.7 |
| **EPA** (B4) | long-chain fatty acid | — | β-oxidised, not glucuronidated | 4 g | n/a | none |

**Three non-obvious conclusions fall out of this:**

**(i) Fenofibric acid is exonerated — on structure, not on faith.** Its α,α-dimethyl
aryloxy-isobutyric acid has a **fully substituted quaternary α-carbon**, which sterically blocks
acyl migration. By the established SAR it sits in the *least* reactive tier, and this is
independently corroborated by 30+ years of mass chronic exposure without an idiosyncratic
hepatotoxicity signal of the zomepirac/benoxaprofen type `[KB]`. **Acyl glucuronide reactivity is
not a reason to reject fenofibric acid.** (Its renal elimination of that glucuronide in CKD
remains a separate and real problem — §7.1.)

**(ii) Pemafibrate is exonerated by dose, which is the more powerful argument.** Its α-ethyl
aryloxypropionic acid is structurally *profen-like* — **Tier II, intrinsically more reactive than
fenofibric acid's.** But reactive-metabolite risk scales with **total daily covalent body
burden**, and the ~10 mg/day threshold is one of the more robust empirical rules in idiosyncratic
DILI `[KB]`. **At 0.4 mg/day, pemafibrate's daily burden is ~360× lower than fenofibrate's and
roughly 25× below the 10 mg heuristic — far beneath any plausible threshold, regardless of
intrinsic reactivity.** For a drug intended for lifelong administration to an asymptomatic
population, this is a substantial and underrated advantage, and it is the second independent
reason (after hepatobiliary elimination) that pemafibrate is the right chronic molecule.

**(iii) Seladelpar and epalrestat carry genuine, structure-derived alerts.** Seladelpar's
`OCC(=O)O` is an unsubstituted aryloxy**acetic** acid — Tier I, **the most AG-reactive scaffold
in Group A**, a distinction visible only from the SMILES column and not from any other field in
the dataset. Its low 10 mg dose mitigates but does not eliminate the concern, and it carries an
independent hepatic-monitoring requirement. Epalrestat combines a Tier I N-glycine acid with a
**rhodanine PAINS core and a thiocarbonyl** at 150 mg/day — the worst combination in the set, and
consistent with its documented hepatotoxicity reports `[KB]`.

### 8.4 One non-AG electrophile that outranks all of these

**Elafibranor's α,β-unsaturated ketone** (`C(=O)/C=C/`, visible in `[DATA]`) is a **Michael
acceptor** — a *directly* electrophilic, GSH-adducting functional group, not a conditionally
reactive conjugate. At 80–120 mg/day over a lifetime this is a larger reactive-metabolite concern
than any acyl glucuronide in this set. **For elafibranor, the AG is the lesser alert.**

### 8.5 Verdict on (f)

**Acyl glucuronide reactivity does not disqualify the PPARα class for lifelong dosing — but it
discriminates sharply within it, in a direction opposite to the naive "fibrate AGs are reactive,
be careful" reading.** The two compounds a general class warning would most implicate
(fenofibric acid, by dose; pemafibrate, by chemotype) are the two the structure–dose analysis
**clears**. The two it clears (seladelpar and epalrestat, by their small size and low dose) are
the two it **flags**. The analysis is derived entirely from the SMILES column of the blinded
dataset plus published AG-reactivity SAR, and it is falsifiable: **measure AG degradation
half-lives at pH 7.4 and 37 °C, and quantify covalent protein adduct formation in human
hepatocytes.**

---

## 9. (g) WHAT DELIVERY STRATEGY WOULD RESCUE THE MECHANISM

Assessed honestly against disease-model §6.3, including its finding that **topical
posterior-segment delivery has repeatedly failed** and the brief's instruction to penalise
topical claims heavily.

### 9.1 Sustained-release intravitreal implant — technically feasible, strategically self-defeating

Highest retinal exposure of any route; bypasses the BRB entirely; a fibrate's lipophilicity
(aLogP 3.81 `[DATA]`) suits a PLGA or polyimide depot. Model §6.3 notes small molecules clear
vitreous in **hours to a day or two**, so a genuine sustained-release depot — not a bolus — is
mandatory. All of that is achievable.

**And it destroys the entire value proposition.** The brief's unmet need #1 is *"disease-modifying
therapy for early S0–S2 DR, **deliverable systemically**."* The value of a PPARα agonist is that
it is an oral pill for a disease whose every existing therapy is a procedure (model §6.4). You
cannot implant **both eyes** of an asymptomatic patient with 20/20 vision and mild NPDR; the
endophthalmitis risk alone (1 in 2,000–5,000 per injection, model §6.3) exceeds any plausible
benefit in a population with no symptoms, and the S0–S2 population is in the **tens of millions**.
**Converting this mechanism into a procedure turns a potentially transformative oral agent into
a worse version of therapies that already exist and already work at S4–S5.** Reject for the
primary indication.

### 9.2 Suprachoroidal — the best invasive route, same strategic objection

Microneedle delivery to the suprachoroidal space targets **chorioretina and RPE** while sparing
the anterior segment (model §6.3). This is **mechanistically the best-matched invasive route for
this specific hypothesis**: the RPE is the outer-BRB lipid-handling and ketogenic compartment
(P8.8, HMGCS2), and suprachoroidal delivery deposits drug on the **basal/choroidal side of the
RPE** — the same side the drug would naturally arrive from via the fenestrated choriocapillaris
(§3.1), just at a far higher concentration.

**Legitimate niche: established exudative/hard-exudate DME**, where a procedure is already part
of the standard of care, the lipid phenotype is the one the P8 mechanism targets, and the
risk-benefit calculus is entirely different from asymptomatic early disease. **Not a route for
unmet need #1.**

### 9.3 Retina-targeted prodrug — the scientifically right answer, with three designs of unequal merit

**(a) Neutral ester/amide prodrug, cleaved by a retina-enriched enzyme. Correct idea, hard
execution.** Masking the carboxylate removes the anionic penalty that §4.4 identifies as the core
problem. The dataset even shows what the unmasked profile looks like: **fenofibrate `[DATA]`
PSA 52.60, HBD 0, neutral** versus fenofibric acid's PSA 63.60, HBD 1, anionic. Ophthalmic
precedent exists (latanoprost isopropyl ester, dipivefrin).

**And the project's own data shows exactly why the naive version fails:** `[DATA]`
`CHEMBL672 → CHEMBL981, Esterases, Liver, "more or less completely converted."` Systemic
esterases hydrolyse a simple ester long before it reaches the eye. A working design must be
**systemically esterase-resistant yet cleaved by a retina-enriched activator** — candidates
include RPE65 (RPE-specific isomerohydrolase), retina-enriched carboxylesterase isoforms, or
NQO1-triggered self-immolative linkers `[KB, speculative]`. **This is a multi-year medicinal
chemistry programme producing a new chemical entity — it forfeits the repurposing advantage,
the generic cost structure and the known-safety argument that make this hypothesis attractive
in the first place.** High scientific merit, poor strategic fit.

**(b) MCT-targeted design — elegant and probably chemically impossible.** §4.4 establishes that
**MCT1/3/4 are abundant at the RPE and Müller cells and are genuinely concentrative** for
monocarboxylates — the one inward, energy-coupled route at the outer BRB. Fibrates *are*
monocarboxylic acids. **But MCT1's substrate pocket demands a small, unbranched, unhindered
aliphatic acid, while the PPARα pocket demands a bulky lipophilic scaffold.** The two
pharmacophores are close to mutually exclusive. Worth one round of computational assessment;
expect it to fail.

**(c) The LPC-ω3 / MFSD2A route — the highest-value delivery hypothesis in this analysis.**
This is the one that is not speculative, because the transporter is characterised, retina/brain-
selective, genuinely **concentrative**, and has a natural ligand class that **overlaps the PPARα
pharmacophore** (§4.4, §6.4):

- **MFSD2A** at the inner BRB transports **lysophosphatidylcholine-esterified** ω-3 fatty acids
  (LPC-DHA, LPC-EPA) into retina and brain against a gradient `[KB, CURRENT CONSENSUS]`.
- **LPC conjugation is an established delivery strategy** for ferrying cargo across MFSD2A-
  expressing barriers `[KB, EMERGING]`.
- The cargo class it evolved to carry — long-chain fatty acids — is **precisely the ligand class
  this project's data `[DATA]` identifies as the only genuine direct-binding PPARα agonists**
  (linoleic acid, α-linolenic acid, with coactivator recruitment across ≥4 PMIDs).

**An LPC-conjugated PPARα agonist is the single delivery concept that attacks the actual
constraint — the absence of concentrative uptake (§4.4) — rather than working around it. It is
the only proposal here capable of producing Kp,uu > 1, which §5.1 shows is the arithmetic
requirement.** And **icosapent ethyl (B4) is its crude, approved, already-available proxy** —
which is a concrete reason to keep B4 in the set despite its weak potency: it is the cheapest
available empirical test of whether this transport route delivers anything useful to a retina.

### 9.4 Systemic nanoparticle carrier — oversold; reject

Honest assessment: **systemically administered nanoparticles do not cross an intact BRB.** The
barrier actively suppresses vesicular transcytosis (model §6.1 — MFSD2A-type programs), which is
exactly the mechanism a nanocarrier would need. What systemic nanoparticles actually do is
(i) extend circulation time, (ii) exploit **leaky** vasculature via an EPR-like effect — which
reintroduces the bootstrapping problem §5 just dismantled, and (iii) get phagocytosed by
microglia and RPE. **The one honest nanoparticle use case here is as an intravitreal depot
formulation (i.e. §9.1), not as a systemic targeting strategy.** There is no convincing
precedent for systemic nano-targeting of the posterior segment. Score low.

### 9.5 Topical drops — reject, and not as a formulation problem

Model §6.3: *"essentially nil for the posterior pole for most molecules"* `[ESTABLISHED]`; brief
§4: penalise heavily. For a 99%-albumin-bound anion crossing cornea → aqueous → (lens, vitreous)
→ retina against tear turnover and the conjunctival/choroidal clearance sink, posterior
concentrations would be **orders of magnitude below even the oral route — which is itself already
1–3 logs short.** I argue no exception. **The repeated failures the model cites are not a
formulation problem awaiting a better vehicle; they are anatomy.**

### 9.6 The resolution that requires no rescue at all — and is my recommendation

**Do not rescue the retinal mechanism. Pursue the systemic one.**

Model §6.2 lists this as resolution (vi) and adds that it *"is a legitimate and
under-appreciated answer and should not be dismissed."* The exposure analysis in this report
converts that from a possibility into the **leading** option:

| Property | Retinal-engagement arm | **Systemic lipid arm** |
|---|---|---|
| Required exposure | Kp,uu 10–300 (unachievable, §5.1) | **None beyond plasma — the target organ is liver** |
| Target-organ concentration | 1–3 logs below free EC50 | **OATP1B1/1B3 concentrates fibrates 10–100× hepatically `[KB]`** |
| Exposure uncertainty | ±1 log protein correction + ±1 log Kp,uu | **Low — hepatic engagement is not in doubt** |
| Route | Oral preserved | **Oral preserved** |
| Stage applicability | S0–S2 only | **Any stage where lipoprotein extravasates — S1–S4** |
| Bootstrapping paradox | Binding, and unfixable | **Inverted — barrier leak is the indication** |
| Best molecule | none adequate | **Pemafibrate** (hepatoselectivity = feature; CKD-safe; 0.4 mg/day) |

**The mechanism:** lower circulating triglyceride-rich remnants and apoB particle number, raising
ApoA1/HDL — reducing the **supply** of lipoprotein available to extravasate through a leaky
barrier and be modified intraretinally (model P8.1/P8.2, §5.2b). **No retinal drug exposure is
required.** It directly addresses unmet need #5 (prevention of hard exudate and intraretinal
lipid) and plausibly #1.

**The honest test this arm must pass, and it is a hard one.** This population is **already
universally statin-treated**. The systemic arm therefore cannot simply claim "lipid lowering
helps" — it must argue that **triglyceride-rich remnant and apoC-III lowering adds something
beyond the LDL-C lowering already achieved.** That is exactly the residual-risk-after-statin
rationale of the fibrate class, it is a legitimate non-DR argument, and it **predicts a
phenotype-enriched population**: diabetic patients with elevated triglycerides and low HDL
despite a statin. That prediction matches the disease model's own phenotype enrichment
(§5.2h: *"T2DM, atherogenic dyslipidemia, exudative/hard-exudate DME"*). **The coherence is a
point in its favour, and the prediction is falsifiable.**

---

## 10. THE ANGPTL4 WRONG-SIGN RISK, CORRECTED FOR EXPOSURE

The brief (§7) requires any agent scoring a PPARα candidate highly to address this. I score
pemafibrate 7, so I must.

**ANGPTL4 is a direct PPARα target gene and a potent pro-permeability, pro-angiogenic factor in
ischaemic retina.** Agonism predicts its induction, which could be net harmful at S4–S5.

**The exposure arithmetic applies symmetrically, and that produces a counterintuitive result:**

**(i) In the retina, the wrong-sign risk is attenuated in exactly the same proportion as the
benefit.** ANGPTL4 induction is a **transcriptional** PPARα response requiring the same receptor
occupancy as CPT1A, ACOX1, HMGCS2 and CAT induction. If retinal free drug reaches only EC5–EC7
(§3.2), it induces retinal ANGPTL4 to ~5–7% of maximum too. **You cannot simultaneously argue
that retinal exposure is too low for benefit and high enough for harm.** Any agent scoring the
wrong-sign risk highly while accepting this report's exposure analysis is double-counting.

**(ii) The real risk is hepatic, and it is not attenuated at all.** Hepatic PPARα **is** fully
engaged — OATP1B1/1B3 concentrates fibrates in hepatocytes 10–100× above plasma `[KB]`, which is
the entire basis of the systemic arm in §9.6. **Hepatic ANGPTL4 induction raises *circulating*
ANGPTL4, which then reaches retinal endothelium from the luminal side without needing to cross
any barrier at all** (§3.1).

> **So the wrong-sign risk is concentrated in the *systemic* arm — the arm this report
> recommends — and is largely absent from the retinal arm, which is the inverse of the naive
> expectation.** This is the most important caveat on my own recommendation and I want it
> carried forward prominently.

**(iii) It is worse for pemafibrate than for fenofibric acid, for the same reason pemafibrate is
otherwise attractive.** Hepatoselectivity maximises hepatic PPARα occupancy per unit systemic
exposure. The molecule best suited to the systemic mechanism is also the one that maximises the
hepatic transcriptional output that drives the wrong-sign path.

**(iv) Direction is genuinely uncertain.** Circulating ANGPTL4 is an **LPL inhibitor**, so
PPARα-driven ANGPTL4 would partly *oppose* the triglyceride lowering that is the mechanism's
whole point — and fibrates are reported both to raise and to lower ANGPTL4 depending on tissue
and context `[KB, UNCERTAIN]`.

**Operational requirement: plasma ANGPTL4 must be a measured biomarker in any fibrate study in
this disease, stratified by DR stage, with pre-specified stopping rules for proliferative
progression.** It is cheap, it is directly on the causal path, and it is the single measurement
that could falsify the systemic arm. **It is also the one thing that would distinguish benefit
from harm in the ischaemic/proliferative subgroup where the mechanism is least suited anyway
(model §5.3).**

---

## 11. SCORES AND FALSIFICATION CRITERIA

**Scoring axis:** ADMET viability for **chronic oral dosing in this specific population**,
weighted by whether the compound can reach a concentration engaging its own target in a
DR-relevant **compartment**. This is deliberately **not** a target-validity score — the pathway
analyst and literature reviewer own that axis, and a high score here means "this molecule can be
given and will arrive," not "this mechanism will work."

| Score | Compound | One-line ADMET verdict |
|---|---|---|
| **7** | Pemafibrate (A3) | Only Group A member safely dosable at full dose in CKD; negligible covalent burden; worst retinal access, which only matters if the mechanism is retina-intrinsic |
| **6** | Fenofibric acid (A1) | Best drug-likeness and highest free plasma concentration in class; renal elimination squarely mismatched to a nephropathy population |
| **6** | Icosapent ethyl (B4) | Only candidate with concentrative retinal uptake; cleanest metabolic profile in the set; weak engagement; bleeding + AF |
| **6** | Melatonin (C2) | The exposure control, and it passes — engaging only MT1/MT2; 3–5 logs short of its putative antioxidant/PPARα mechanisms |
| **5** | Dimethyl fumarate (D2) | Covalent mechanism escapes the free-drug argument; lymphopenia + proteinuria bite specifically in diabetic CKD |
| **5** | Epalrestat (D1) | Best free-concentration-to-own-potency ratio of any acid here; rhodanine PAINS, Tier-I acyl glucuronide, hepatotoxicity |
| **4** | Elafibranor (A4) | Best exposure margin in Group A, worst electrophile burden; a probe, not a chronic preventive |
| **4** | Fenofibrate (A2) | Data-backed complete presystemic conversion → zero independent PK identity; strictly A1 plus an unnecessary esterase step |
| **3** | Seladelpar (A5) | Does its job as the isoform control and is better target-engaged than the arm it controls; Tier-I acyl glucuronide; not the hypothesis |
| **3** | α-Linolenic acid (B2) | Endogenous, homeostatically buffered, no achievable pharmacological concentration; safe; a mechanism anchor, not a drug |
| **3** | Candesartan cilexetil (D4) | Luminal target engaged despite terrible descriptors; functionally **redundant** — most target patients already take a RAS blocker |
| **2** | Linoleic acid (B1) | Best PPARα binding evidence in the project data, least deliverable compound, plus HODE/4-HNE wrong-sign risk |
| **2** | Minocycline (D3) | Genuinely good retinal access; disqualified for lifelong use, including by an ophthalmic adverse effect (papilledema) |
| **2** | Linalool (B3) | Best passive BRB descriptors in the set; no oral product, no clinical PK, no deliverable dose |
| **1** | Quercetin (C1) | <2% F, circulates conjugated, data-backed dual efflux substrate, 3–4 logs short before the barrier, plus a data-backed statin-transporter DDI |

### Falsification criteria for every score ≥ 6 (brief §10 requires this at 7+; I supply them at 6+)

**Pemafibrate — 7. Falsified by any of:**
1. A pigmented-animal ocular PK study showing **retina:plasma unbound < 0.02** would confirm it
   can never test the retinal arm, and the score should then be read as applying *only* to the
   systemic arm.
2. Failure to lower remnant cholesterol or apoC-III **beyond background statin therapy** in a
   diabetic dyslipidaemic population kills the systemic arm, which is the arm carrying the score.
3. A measured increase in **plasma ANGPTL4** accompanied by any signal of accelerated
   proliferative progression (§10) would invert the sign.
4. Clinically meaningful CYP2C8-mediated exposure increase on **clopidogrel** co-administration
   in real-world use would compromise the safety advantage that justifies the 7.

**Fenofibric acid — 6. Falsified by:** demonstration that the eGFR-banded dose reduction required
in moderate CKD drops free plasma concentration below ~0.05 µM (which would take even the
endothelial margin past −3 logs); or a measurable sulfonylurea-hypoglycaemia signal in routine
co-administration.

**Icosapent ethyl — 6. Falsified by:** failure to detect a rise in **retinal** (not plasma) ω-3
content after chronic oral dosing in a pigmented model — which would refute the MFSD2A delivery
premise that is the entire basis of the score; or a bleeding event rate on background antiplatelet
therapy exceeding the benefit margin.

**Melatonin — 6. Falsified by:** demonstration that any proposed retinal benefit requires
concentrations above ~1 µM (unreachable orally without sedation), which would reduce the score to
2–3; or a measurable HbA1c deterioration on chronic bedtime dosing.

---

## 12. DATA GAPS — ranked by how much they would change this analysis

1. **A free-drug-corrected PPARα EC50.** The single largest uncertainty in this report (±1 log,
   §4.1) and the cheapest to close: re-run the transactivation assay in **4% human serum albumin**
   and report a free EC50. Everything in §3–§5 is bounded by this one unmeasured number.
2. **Ocular PK in a pigmented animal** — retina, vitreous and RPE/choroid unbound concentrations
   at steady state for fenofibric acid and pemafibrate, in normal and diabetic eyes. This is the
   measurement the entire pipeline is currently guessing at. Pigmented, because melanin binding
   (model §6.1) makes albino data unrepresentative.
3. **Compartment-resolved Kp,uu** — endothelium vs RPE vs neural retina. §3.1 is the pivotal
   correction in this report and it rests entirely on `[KB]` anatomy, not measurement.
4. **Whether a fibrate is an OATP1A2 or OATP2B1 substrate.** §4.4 refutes the scout's absolute
   claim but cannot quantify the inward route. A straightforward transfected-cell uptake assay.
5. **Acyl glucuronide degradation half-lives** at pH 7.4/37 °C for all Group A acids, to test the
   §8.3 structural predictions — particularly the seladelpar Tier-I prediction.
6. **Plasma and, if obtainable, vitreous ANGPTL4** under PPARα agonism, stratified by stage (§10).
7. **Any measured PK in the project at all.** Six PK-relevant columns are 100% empty across 3,276
   rows (§0). Populating `logd`, `molecular_species` and `bioavailability_score` from ChEMBL would
   materially improve every future ADMET pass; **`molecular_species` alone would have let the
   pipeline flag "acid at pH 7.4" automatically** instead of requiring manual SMILES inspection.
8. **Protein binding and Vd** for all 15. Currently 100% `[KB]`. These two numbers drive the whole
   analysis and neither is in the dataset.

---

## 13. BLINDING COMPLIANCE STATEMENT

**Files read.** `disease-brief.md`; `disease-model.md` §5.2 and §6 (full); `agents/p0-ppara-scout.md`
§6, §7, §8, §9; `.claude/skills/admet-predictor/SKILL.md`; and from the blinded data directory
only: `data/processed-blinded-diabetic-retinopathy/chembl_approved_drugs.csv`,
`chembl_natural_products.csv`, `chembl_drug_metabolism.csv`, `chembl_drug_warnings.csv`,
`chembl_toxicity.csv`, `chembl_drug_mechanisms.csv`, `chembl_drug_targets.csv`,
`chembl_bioactivities.csv`, `pubchem_phytochem_target_interactions.csv`,
`drugbank_drug_targets.csv`; plus the pre-computed evidence pack
`evidence/ppar-class-drug-properties.tsv` and `evidence/compound-dr-target-matrix.tsv`.

**I did not read** `data/processed/chembl_approved_drugs.csv`, anything under `data/holdout/`, or
any `answer-key*` file. I did not consult git history, git objects, or any other route to recover
redacted values. **I did not search for, count, or attempt to identify `[REDACTED-HOLDOUT]`
tokens**, and I did not infer any candidate's redaction status by elimination.

**Disclosures — honest, including negative decisions.**

1. **I know DR/DME-specific trial evidence exists for more than one compound in this candidate
   set, and I deliberately excluded all of it.** This exclusion cut **against** my own
   conclusions at several points: in §4.6, §5.2 and §9.6 I had to reason the systemic-versus-
   retinal mechanism question purely from exposure arithmetic and the disease model, where
   DR-specific outcome data would have constrained the answer considerably. I report this as a
   limitation of the output, not a hedge.

2. **The melatonin-as-exposure-control framing came from the brief (§8, C2) and the scout, not
   from me.** My contribution was the quantification (§6.3) and the conclusion that it fires
   against the entire set. No DR-specific melatonin knowledge was used.

3. **Non-DR clinical safety knowledge was used freely and is permitted under §1.3.** Specifically:
   fibrate protein binding, elimination routes and CKD dosing; gemfibrozil's CYP2C8
   mechanism-based inactivation; clopidogrel's CYP2C8 inactivation; DMF lymphopenia and PML;
   minocycline vestibular toxicity, pigmentation and **benign intracranial hypertension**;
   MTNR1B/melatonin glucose-tolerance effects; ω-3 bleeding and atrial-fibrillation signals; ARB
   hyperkalaemia and dual-blockade contraindication. **None of these is a DR indication claim.**

4. **Minocycline's papilledema is an *ophthalmic* adverse effect and I used it to down-score the
   compound.** I judged this permissible because it is general drug-safety knowledge about an
   adverse event, not knowledge of minocycline's status in DR. **Flagging it explicitly because
   it is the closest call in this report** — a scorer may wish to review it.

5. **I used the fenofibrate→fenofibric acid conversion and the renal glucuronide elimination
   route as `[DATA]`**, read from `chembl_drug_metabolism.csv`. These are metabolism annotations,
   not indication annotations. The `therapeutic_areas` column in the blinded files lists many
   indications for several candidates; **I read that column only to confirm oral approval status
   and did not use any listed indication as evidence for or against any score.**

6. **No DR-specific efficacy, trial, guideline or approval knowledge influenced any score in
   §11.** Every score derives from physicochemistry in the blinded dataset, general
   pharmacokinetics, and the exposure arithmetic in §3–§5.

7. **Where my conclusions diverge from the scout's** (§4.6, §7.2 on pemafibrate; §5.2 on the
   bootstrapping paradox; §4.4 on retinal uptake transporters), the divergence rests on general
   PK principles — the free-drug hypothesis, pH partitioning, volume of distribution, barrier
   physics — and on the compartment anatomy in disease-model §6.1. **No DR-specific knowledge
   was involved in any disagreement.**

---

## SCOREBLOCK

SCORE|Elafibranor|7|low|mixed|Only Group A compound plausibly at or above free EC50 at endothelium
SCORE|Pemafibrate|6|moderate|mixed|Closest potent fibrate at endothelium; hepatic engagement unambiguous for systemic arm
SCORE|Epalrestat|6|moderate|mixed|Free plasma 2.4x AKR1B1 IC50; target abundant in Muller cells, pericytes
SCORE|Candesartan cilexetil|6|high|mixed|Luminal AT1R fully engaged from blood; no barrier crossing required
SCORE|Seladelpar|5|moderate|mixed|PPARdelta engaged above EC50, but delta is the control, not hypothesis
SCORE|Melatonin|5|high|mixed|MT1/MT2 engaged; nominated antioxidant and PPARalpha mechanisms 3-5 logs unreachable
SCORE|Dimethyl fumarate|5|moderate|mixed|Covalent cumulative KEAP1 alkylation escapes the equilibrium free-drug exposure argument
SCORE|Fenofibric acid|4|moderate|mixed|Reaches only EC5-EC7 at endothelium and RPE; partial transcriptional nudge
SCORE|Fenofibrate|4|high|data-backed|Complete presystemic esterase conversion; pharmacokinetically identical to fenofibric acid, no advantage
SCORE|Minocycline|3|high|mixed|Retinal free 0.1-1 uM, one to two logs below microglial endpoints
SCORE|Icosapent ethyl|3|moderate|mixed|Concentratively delivered via MFSD2A, but free EPA stays below class EC50
SCORE|Alpha-linolenic acid|2|high|mixed|Endogenous at homeostatic set point; dosing cannot move free ligand concentration
SCORE|Linoleic acid|2|high|mixed|Not dose-movable; plus wrong-sign HODE and 4-HNE peroxidation chemistry
SCORE|Quercetin|1|high|mixed|Free aglycone three to four logs short before barrier; dual efflux substrate
SCORE|Linalool|NA|low|knowledge-based|No deliverable dose and unmeasured EC50; engagement arithmetic cannot be constructed
