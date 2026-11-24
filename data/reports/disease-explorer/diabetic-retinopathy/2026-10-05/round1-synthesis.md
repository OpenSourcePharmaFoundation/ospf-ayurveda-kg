# Round 1 Synthesis — Diabetic Retinopathy (BLINDED RUN)
Orchestrator synthesis of six Phase 1 domain agents. 2026-10-05.

Agents: Medicinal Chemist · Pharmacokinetics/ADMET · Molecular Target Analyst ·
DR Biology Specialist · Clinical Landscape Researcher · Traditional Medicine Expert.
Phase 0: Disease Research Agent + PPARα Candidate Scout.
Total agent output: ~7,400 lines across 8 reports.

---

## 1. THE HEADLINE: the question changed

The run opened with the Phase 0 scout's objection — free fenofibric acid sits ~2 log₁₀
below the PPARα EC50 in plasma, the retina has no uptake transporter, therefore retinal
PPARα agonism cannot be the mechanism. Four agents then dismantled, rebuilt and relocated
that argument. The question is no longer *"does PPARα agonism help DR?"* It is:

> **Which of two mechanistically distinct limbs does any of the work — hepatic/systemic
> lipoprotein lowering, or retinal receptor engagement? They favour different molecules,
> different stages, different trial designs, and they are not distinguishable by the
> candidate set as originally constructed.**

### What survived, what did not

| Claim | Status after Round 1 |
|---|---|
| Retinal **neural** PPARα engagement is achievable orally | **DEAD.** Kp,uu cannot exceed 1; even total barrier failure leaves fenofibric acid 10–100× below free EC50. Not a late-arrival problem — it never arrives. |
| Retinal **endothelial / RPE** PPARα engagement is achievable | **CORRECTED — see §2.1.** The compartment claim holds (these pools sit on the blood side of the inner BRB, one membrane not a barrier), but the engagement margin does not. Fenofibric acid's endothelial margin is **−3.0 to −1.1 log, midpoint −2.0** — not materially different from the scout's original figure. The ADMET agent's own reading: *"Not robust engagement anywhere; a small, chronic, partial transcriptional nudge is arguable."* |
| **Hepatic** PPARα engagement is achievable | **CERTAIN.** OATP1B1/1B3 concentrate fibrate anions 10–100× in liver. Not in dispute by any agent. |
| The ~2-log exposure gap | **Partly corrected, but the endothelial position is still ~2 logs short.** The scout's *method* was inconsistent (free plasma against a nominal EC50 measured in serum-containing medium), and fixing it closes 0.5–1.5 log of the comparison. **That is a correction to the scout's arithmetic, not to the conclusion** — after correction, fenofibric acid still sits −3.0 to −1.1 log below free EC50 at the endothelium. This synthesis originally reported the correction without the residual margin. |
| ANGPTL4 is a fatal wrong-sign limb | **DEMOTED to stage-restricted safety flag.** |
| Potency buys engagement | **FALSE.** See §3. |
| Traditional medicine contributes a candidate | **NULL, with quantitative backing.** See §5. |

---

## 2. THE STRUCTURAL FINDING — why this is not fixable by picking a different fibrate

The Medicinal Chemist supplied the deepest result of the round. Retinal occupancy is:

```
occupancy  ∝  fu × C_plasma × Kp,uu / EC50
```

Across the fibrate series from fenofibric acid to pemafibrate, medicinal chemistry
optimised the **denominator by 4–5 logs** while degrading **every term in the numerator**.
This is not coincidence: **the lipophilic bulk that fills PPARα's arms II/III is the same
recognition element that albumin site II and the hepatic OATP1B transporters bind.**

`[DATA]` across that progression: MW 318.76 → 490.56 · aLogP 3.81 → 5.55 · RTB 5 → 13 ·
QED 0.85 → 0.24.

**CORRECTION (Devil's Advocate, verified by the orchestrator against `p1-admet.md` §3.2).**
This synthesis originally claimed the ADMET agent produced "the same result from the other
direction — potency rank is the exact reverse of retinal-access rank." That conflated a
**term** with the **product**.

- The *Kp,uu term alone* IS reversed against potency — that is ADMET's §6.1 Table 1, which is
  explicitly headed "Rank by retinal access (Kp,uu)."
- The *occupancy product* — `fu × C_plasma × Kp,uu / EC50`, which is what determines
  engagement — is **not** reversed. ADMET's own §3.2 endothelial margins:

  | Compound | Endothelial margin vs free EC50 |
  |---|---|
  | **Elafibranor** | **−0.7 to +0.4 log** |
  | Pemafibrate | −1.6 to −0.2 log |
  | Fenofibric acid | −3.0 to −1.1 log |

  **That is the same order as potency, not its reverse.** ADMET's own wording is that potency
  is "nearly **orthogonal** to engagement" in this series — not inversely correlated.

The chemist's equation and its structural explanation stand: potency was bought by degrading
`fu` and `Kp,uu`, and those individual terms do move against potency. **What does not follow —
and what this synthesis wrongly asserted — is that the net occupancy ordering inverts.**

**Consequence — this resolves the round's loudest conflict at a level beneath it.** The
scout called pemafibrate's hepatoselectivity a bug; the Target Analyst called it a feature.
Neither framing matters, because **within this chemotype the property is not optional.**
Hepatoselectivity is the direct consequence of the potency strategy, not a separable design
choice. Therefore:

> ~~**No molecule in the fibrate class can test the retina-intrinsic PPARα hypothesis.**~~
>
> **RETRACTED.** This was the synthesis's single most emphatic structural conclusion and it is
> contradicted by the run's own data. **Elafibranor's endothelial margin is −0.7 to +0.4 log**
> — the ADMET agent calls it *"the only Group A compound that plausibly reaches or exceeds its
> free EC50 at the retinal endothelium… the cleanest pharmacological probe."* **The run had a
> probe for the retinal limb in its own candidate set and declared the question structurally
> untestable.**
>
> The retraction is partial, not total. Elafibranor carries two real confounds: PPARδ
> co-agonism muddies the isoform question, and a Michael-acceptor enone at 120 mg/day is a
> genuine liability for lifelong dosing. ADMET also flags its Cmax as **the lowest-confidence
> number in that report**, so the probe rests on the weakest input. **But "confounded and
> uncertain" is a different claim from "structurally impossible," and this synthesis asserted
> the latter.**
>
> **Consequence:** elafibranor should be reinstated — not as a chronic therapeutic candidate,
> where its safety profile is poor, but as a **short-duration (≈12-week) mechanistic probe** of
> whether endothelial PPAR engagement does anything in this disease.

The Traditional Medicine agent found the same anti-correlation in an unrelated chemical
series — across the natural products, retinal access and PPARα affinity are anti-correlated
(linalool, geraniol and melatonin pass every penetration criterion and have no potency; the
fatty acids have real binding evidence and fail on ionisation, lipophilicity and protein
binding). Two chemotypes, one constraint.

---

## 3. THE STAGE OFFSET — the mechanism and the need are misaligned

From the DR Biology Specialist, and it is the most consequential strategic finding:

- PPARα's **exposure-robust limb** (lowering systemic apoB/remnant supply) is **mechanically
  inoperative at S0** — with an intact barrier there is no extravasation to prevent. It
  only produces retinal benefit once the barrier already leaks, i.e. **S1–S3**.
- PPARα's **right-stage limb** (retinal FAO, ceramide/DAG control at S0–S1) is precisely the
  limb the exposure arithmetic most undermines.

> **The best-exposed mechanism acts at the wrong stage; the right-stage mechanism has the
> worst exposure case.**

**This narrows the opportunity and corrects the brief.** Unmet need #1 as written names the
S0 preclinical window. The honest development target is **S1–S2**, not S0.

For the systemic arm specifically, the "bootstrapping paradox" **dissolves rather than
bites**: a leaky barrier is the *indication* for a supply-lowering mechanism, not an
obstacle to it.

---

## 4. ANGPTL4 — resolved by three agents independently

The Target Analyst found the structural argument, and the ADMET and Disease agents reached
it independently:

> ANGPTL4 induction is **PPRE-driven transactivation — the same machinery the exposure
> objection says is unavailable.** If retinal occupancy is too low to induce CPT1A/HMGCS2
> and help, it is too low to induce ANGPTL4 and harm. If it is high enough to induce
> ANGPTL4, the exposure objection has collapsed. **One of the two arguments must be
> abandoned; the scout's §7 treats ANGPTL4 as *sharpening* the exposure objection, and it
> is in fact in tension with it.**

**But the risk relocated rather than vanished.** The ADMET agent identified the surviving
path, and it is the inverse of the naive expectation: **hepatic PPARα *is* fully engaged**,
so hepatic ANGPTL4 induction raises **circulating** ANGPTL4, which acts on retinal
endothelium **from the luminal side** — the one compartment that needs no barrier crossing.

**Operational consequences:**
- Score impact ≈ −2 at S4–S5, ≈ 0 at S0–S2. Stage-restrict, don't exclude.
- **Plasma ANGPTL4 is a mandatory, measurable biomarker for any fibrate trial in DR.**
- Prespecify a safety readout: no excess progression to proliferative disease, no excess
  centre-involving macular edema in the treated arm.

### The one experiment that discriminates the whole hypothesis

Chronic oral fibrate in a diabetic rodent; measure retinal CPT1A/ACOX1/ANGPTL4 (transactivation)
against retinal ICAM1/TNF/leukostasis (transrepression).
- Transrepression **down** without transactivation **up** → confirms the dissociated-ligand
  model in §6 and the ANGPTL4 demotion.
- Robust retinal FAO-gene induction → the low-occupancy model is wrong, ANGPTL4 risk is live.

This should be the programme's top preclinical priority. It is cheap and it is decisive.

---

## 5. WHAT THE CANDIDATE SET CANNOT DO — and the control added to fix it

**Four agents independently converged on the same worry**, phrased most sharply by the
Target Analyst:

> *"The entire PPARα hypothesis may be a **lipid-lowering hypothesis wearing a receptor's
> name**, and the candidate set as constructed cannot tell the difference."*

Every lipid-lowering candidate in the original 15 is also a PPAR ligand. The PPARδ arm
(seladelpar) **cannot serve as the isoform control** — the Target Analyst showed PPARδ is
the most abundant retinal PPAR, is pro-angiogenic, is at least as strong an ANGPTL4 inducer
as PPARα, and shares identical transrepression machinery, so both a positive and a negative
seladelpar result are ambiguous.

**Added to the set: E1 — Ezetimibe (CHEMBL1138).** NPC1L1 cholesterol-absorption inhibitor,
lowers apoB, **zero PPAR activity**, oral, generic, well tolerated in diabetics.

> **If a matched apoB-lowering non-PPAR agent produces the same retinal benefit, the
> receptor is not what is doing the work.**

*Stated limitation:* the match is partial. Fibrates lower TG-rich remnants; ezetimibe lowers
predominantly LDL-C. Since the disease model identifies the toxic species as the **modified
apoB particle** (hard exudates are retained glycated-and-oxidised apoB lipoproteins, not
"fat"), the comparison is informative but not clean.

> **CORRECTION (Phase 2, Drug Repurposing Strategist).** This section originally stated that
> "no non-PPAR remnant-lowering generic exists to do better." That was wrong in substance.
> **Olezarsen**, an apoC-III antisense oligonucleotide, lowers apoC-III 70-85% and
> triglycerides 50-70% with **zero PPAR activity**. ApoC-III repression is *precisely the
> node through which PPARα lowers remnants* — so it is the same mechanism with the receptor
> deleted, which is exactly what a discriminating arm requires. It is not a generic, which is
> the only sense in which the original claim held, and that qualifier made the statement
> misleading rather than true.
>
> **Revised control design:** keep ezetimibe (E1) as a cheap, widely available *partial*
> control, and treat an **apoC-III-directed arm as the real discriminator**. A null with
> ezetimibe is uninterpretable because it is the wrong particle; a null with apoC-III
> suppression would be decisive. `[knowledge-based]`

---

## 6. THE LIMB THAT SURVIVES — a pharmacokinetically dissociated ligand

The Target Analyst's §4, and the most interesting constructive idea in the round:

**Transrepression** of NF-κB/AP-1 is PPRE-independent and plausibly operates at **1–2 log₁₀
lower fractional occupancy** than transactivation — the principle the entire dissociated-ligand
/ SEGRM / SPPARM field rests on. **That is exactly the size of the gap the scout identified.**

> At low retinal occupancy, the retina sees a **pharmacokinetically dissociated PPARα
> ligand** — anti-inflammatory transrepression (ICAM1, TNF, IL6, VCAM1 → leukostasis, the
> central early DR lesion) **without** metabolic transactivation and **without** ANGPTL4
> induction.

This is elegant, testable, and it is the only reading under which a retinal contribution
survives the exposure arithmetic. It is also **unproven** — the occupancy differential is
reasoned from receptor pharmacology, not measured for PPARα in retina.

---

## 7. SCORE MATRIX

Generated table: `round1-score-matrix.txt`.

```
candidate                 admet  chemist clinical  disease    ethno   target   mean  spread
-------------------------------------------------------------------------------------------
Pemafibrate                 6.0      5.0      5.0      7.0       NA      7.5   6.10     2.5
Fenofibric acid             4.0      6.0      7.0      6.5       NA      7.0   6.10     3.0
Candesartan cilexetil       6.0      5.0      5.0      6.0       NA      6.0   5.60     1.0
Fenofibrate                 4.0      4.0      7.0      6.0       NA      6.5   5.50     3.0
Icosapent ethyl             3.0      4.0      6.0      6.0      5.0      5.5   4.92     3.0
Melatonin                   5.0      5.0      5.0      5.5      4.0      4.5   4.83     1.5
Dimethyl fumarate           5.0      4.0      3.0      7.0       NA      5.0   4.80     4.0
Elafibranor                 7.0      4.0      3.0      5.5       NA      4.0   4.70     4.0
Epalrestat                  6.0      3.0      4.0      4.0       NA      2.0   3.80     4.0
Minocycline                 3.0      3.0      3.0      5.5       NA      3.5   3.60     2.5
Seladelpar                  5.0      3.0      2.0      4.0       NA      2.5   3.30     3.0
Alpha-linolenic acid        2.0      2.0      1.0      3.5      2.0      4.5   2.50     3.5
Linalool                     NA      2.0      1.0      3.5      3.0      3.0   2.50     2.5
Linoleic acid               2.0      2.0      1.0      2.0      2.0      3.0   2.00     2.0
Quercetin                   1.0      2.0      2.0      2.5      2.0      2.0   1.92     1.5
```

### THE MEAN IS NOT A RANKING — read this before using the table

**The six agents scored six different quantities**, by instruction:

| Agent | Axis |
|---|---|
| admet | achievable target engagement for the proposed mechanism |
| chemist | structural / medicinal-chemistry merit for this indication |
| clinical | clinical and developmental viability — explicitly NOT efficacy |
| disease | disease-biology fit (pathway x stage x compartment) |
| ethno | traditional-use evidence contribution (9 NAs — correct, not missing) |
| target | target validity and druggability |

Averaging across orthogonal axes is **not** a composite score, and the Clinical agent
stated the correct operation explicitly: **these must be MULTIPLIED with mechanism scores,
not averaged.** A candidate that is developmentally unviable (clinical 1-3) is not rescued
by excellent biology; a candidate that cannot engage its target (admet low) is not rescued
by cheapness. The mean column is a convenience for spotting *agreement*, nothing more.

**Spread is the more informative column.** Low spread means independent agents scoring
different things converged. High spread means the candidate is good at one thing and bad at
another — which the lexicographic-gate architecture, not an average, must resolve.

**Pemafibrate and fenofibric acid tie at 6.10 from opposite directions.** Pemafibrate is
carried by target biology (7.5) and disease fit (7.0) and held down by chemistry, clinical
viability and engagement. Fenofibric acid is carried by clinical viability (7.0), target
(7.0) and disease fit (6.5), and held down hardest by **engagement (4.0)** — the ADMET
agent's axis, and the one that matters most for the retinal limb. They are not
interchangeable and the tie is an artifact of averaging.

**The natural products collapsed under agreement, which validates the controls.** Quercetin
sits at 1.92 with a spread of 1.5 — the tightest consensus in the matrix, and the lowest
score. It was the top compound in the raw target-count data. Every agent independently
rejected it once evidence quality replaced row count.

### The disagreements that drive Phase 2 and the debate

| Candidate | Spread | High | Low | Nature of the conflict |
|---|---|---|---|---|
| **Dimethyl fumarate** | 4.0 | Disease 7.0 | Clinical 3.0 | Hits the upstream ROS/NRF2 node the model calls highest-leverage, acts from S0, best BRB physicochemistry in the set, and its covalent cumulative KEAP1 alkylation is **the one mechanism the free-drug/EC50 arithmetic does not govern** — **versus** PML risk, lymphopenia and mandatory monitoring, the wrong profile for treating asymptomatic people. |
| **Elafibranor** | 4.0 | ADMET 7.0 | Clinical 3.0 | **Best exposure margin in Group A** (free plasma ~ free EC50 at endothelium) — **versus** a Michael-acceptor enone dosed at 120 mg/day for life, and two years of market history. The engagement axis strips out the safety penalty that the clinical axis exists to apply. |
| **Epalrestat** | 4.0 | ADMET 6.0 | Target 2.0 | Free plasma = 2.4x IC50, the best acid in the set on engagement — **versus** AKR1B1 carrying **negative human clinical validation**: the mechanism was tried in DR and failed. Engagement without a target worth engaging. |
| **Alpha-linolenic acid** | 3.5 | Target 4.5 | Clinical 1.0 | Genuine data-backed PPARα binding — **versus** a dietary nutrient with no regulatory vehicle, no valid placebo, and (per the Ethnobotany agent) a plasma concentration already at its own EC50, making it **not dose-movable**. |
| **Fenofibric acid / Fenofibrate** | 3.0 | Clinical 7.0 | ADMET 4.0 | Cheap, universally available, decades of chronic diabetic exposure — **versus** 1.1-3.0 logs short of free EC50 at the endothelium. The central tension of the whole run in one row. |
| **Seladelpar** | 3.0 | ADMET 5.0 | Clinical 2.0 | Engages its target comfortably — **versus** being a confounded control (§5) with a PPARδ carcinogenicity question and a minimal chronic database. |

## 8. CROSS-CUTTING: what the project data could not do

- **No drug→target affinity exists anywhere in this project.** ChEMBL mechanism (11 rows),
  target (44) and bioactivity tables are near-empty test extracts with **zero PPAR content**.
- **No measured PK of any kind.** `logd`, `cx_logd`, `permeability`, `molecular_species`,
  `bioavailability_score` are empty for all 3,276 drug rows.
- **The 27-gene DR panel contains all three PPAR receptors and zero PPAR effector genes**
  (no ANGPTL4, CPT1A, ACOX1, HMGCS2, LPL, APOA1, ABCA1, FGF21). **The pathway this run is
  about is invisible to the run's own data.** Orchestrator error — see findings §10.
- **Only 5 of 15 candidates appear in the target matrix, and all 5 are natural products.**
  Any target-count-weighted ranking would favour polyphenols over drugs as a pure database
  artifact — see findings §11.
- **No DisGeNET gene-disease data for DR.** Every gene-disease link is knowledge-based.

**What the data genuinely supplied:** fenofibrate→fenofibric acid conversion by esterases
with renal glucuronide elimination; acyl-glucuronide formation attested across 16 rows of
the fibrate/NSAID acid class; quercetin as a **dual ABCB1/ABCG2 efflux substrate** (a
data-backed BRB disqualifier) and an SLCO1B1 inhibitor (a real DDI in a statin-treated
population); linalool's PPARA-**dependent** SLC27A4 induction, abolished in PPARA mutant —
the only genetic-dependency engagement evidence in the set.

---

## 9. QUESTIONS ROUTED TO PHASE 2

1. **Pathway Analyst** — The set covers only the *afferent* half of the lipid axis. All 16
   compounds reduce what arrives; none accelerates what leaves (LXR→ABCA1/ABCG1→ApoA1/ApoE
   efflux; CD36/OLR1/MSR1 scavenger blockade). Is the efflux arm druggable, and would it
   combine with a supply-lowering agent?
2. **Safety Pharmacologist** — Acyl glucuronide reactivity under lifelong dosing; fibrate +
   statin myopathy in a universally statin-treated population; renal elimination in a
   CKD-dominant population; and whether the creatinine rise is a **functional unblinding
   hazard** in a trial that monitors renal function.
3. **Drug Repurposing Strategist** — Given that no fibrate can test the retinal limb, is
   there an approved non-acidic PPARα ligand, or a molecule reaching retinal endothelium
   with PPARα activity, anywhere outside this set?
4. **SAR Analyst** — The chemist's scaffold-hop: can AF-2 helix-12 engagement be retained
   without a permanently anionic head? What would such a molecule look like, and is the
   acid genuinely required or merely conventional?
5. **Literature Reviewer** — Normal blinded operation, **plus** a strictly segregated
   `## POST-HOC UNBLINDING (EXCLUDED FROM SCORING)` section. This is the benchmark's
   unblinding checkpoint.

---

## 10. BLINDING STATUS

All six agents filed compliance statements. No agent read the holdout key or the unblinded
source file. Two disclosed knowledge-adjacent judgments honestly:

- The **scout** noted Group D's mechanism categories were inherited from the orchestrator's
  brief and are themselves canonical DR development axes — so that subset is not
  independently blind. Recorded as a limitation.
- The **scout** also noticed `[REDACTED-HOLDOUT]` markers, declined to identify which rows
  they belonged to, and disclosed the count rather than the contents. The blinding was
  hardened in response and the tree regenerated with no markers.

**The unavoidable residual:** dataset blinding removes the project's data signal, not the
model's pretrained knowledge. This run measures mechanistic-path plausibility under data
blinding, not naive rediscovery. The scoring step must read it that way.
