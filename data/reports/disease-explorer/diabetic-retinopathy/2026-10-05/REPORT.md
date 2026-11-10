# PPARα as a Therapeutic Target in Diabetic Retinopathy
## What is measured, what is modelled, and where a drug could still act

**Report revised** 2026-11-09 · **Original analysis** 2026-10-05
**Scope** Treatments for diabetic retinopathy (DR), with specific focus on PPARα (gene *PPARA*)

---

## PROVENANCE TAGS

Every quantitative claim in this report carries one of four tags. Conflating them —
presenting reasoning with the confidence of measurement — is the failure this report is
written to avoid.

| Tag | Meaning |
|---|---|
| **[M]** | **Measured.** Read from a primary experimental result, a regulatory label, or a structure, with the source named |
| **[C]** | **Computed.** Derived from measured values by arithmetic stated at the point of use. No new assumption |
| **[Mod]** | **Modelled.** Output of a model over distributions chosen to span a published spread. The assumptions are stated and the bounds are reported |
| **[R]** | **Reasoned.** A pharmacological argument with no computation behind it |

An untagged number in this report is an error.

---

## ABSTRACT

**Which compounds to advance against diabetic retinopathy, in what role, and with what
expectation.** The ranking is the answer; the rest of this report is why the order is not the
one the pharmacology implies.

| # | Compound | Role | Free-drug margin at retinal endothelium, Cmax | |
|---|---|---|---|---|
| **1** | **Fenofibric acid** | **Lead — systemic limb only** | **0.020** · 51× short | The compound the DR clinical evidence rests on. Certain hepatic engagement; **local engagement excluded** |
| **2** | Pemafibrate | **Downgraded** | 0.027 · 37× short | Most potent of the four and the **worst retinal drug** of them: its potency depends on a hepatic transporter the retina does not express |
| **3** | Elafibranor **+ GFT1007** | Probe, 12 wk | **0.136** · 7.3× short | Closest of the PPARα agents, and only via its active metabolite. Equal PPARδ potency makes it a **pro-angiogenic risk** in retinal vasculature |
| **4** | **Seladelpar** | **PPARδ probe** | **0.558** on PPARδ · 1.8× short | **The only compound within reach of a retinal receptor — and it is the wrong receptor.** A hazard finding before an opportunity |

Olezarsen (matched non-PPAR apoC-III suppression) and inclisiran (3–5× the apoB effect of any
fibrate) are carried as the **control and falsification arms** — they are what would make a
positive result interpretable. Fenofibrate adds an esterase step to #1 without adding
pharmacology. The stage is the same for every entry: **mild-to-moderate non-proliferative
disease**, the most robust conclusion in this report.

*Margin is free drug concentration ÷ free EC₅₀ at the compartment that faces the blood
directly; 1.0 is parity and every value here is below it. All margins modelled **[Mod]** over
23 inputs — §1 and §5.7.*

---

**Why that order, and not the ordering by potency: the local PPARα hypothesis is necessary and
unreachable, and both halves are now quantitative.**

**Necessary.** Cell-type-restricted conditional *Ppara* deletion in mouse retinal endothelium
(PMID 41485550) and microglia (PMID 36497130) each reproduce a worsened diabetic retinal
phenotype — declining ERG, retinal thinning, vascular leakage, pericyte loss — **with hepatic
PPARα, plasma triglycerides, ketogenesis and FGF21 all intact [M]**. The competing systemic
explanation is structurally absent in those animals, not statistically adjusted. Local PPARα
does something in those two compartments.

**Unreachable.** A 23-input exposure model, calibrated against the only measurement of any
fibrate in ocular tissue after systemic dosing in any species, produces the margins in the
table above — requiring dose multiples of **119×, 290× and 135×** for rows 1–3 to reach
parity. Neural retina is a further 5.3× worse: **Kp,uu = 0.059 [95% CI 0.009–0.354] [Mod]**.
The lead compound is also a weak binder at its own receptor: **median PPARα EC₅₀ 15,000 nM
across 13 determinations (95% CI 2,490–90,400), with five further records censored at
>10,000 nM [M]**.

**And the reason is mechanistic, so dose does not fix it.** Run backwards against the observed
clinical lipid effect, the model demands a hepatic concentration factor of **37–92×** — which
these drugs obtain from organic-anion uptake transporters. **OATP1B1 is 502.3 nTPM in liver and
0.0 nTPM in retina; OATP1B3 is 247.7 against 0.0 [M].** The property that makes a fibrate a
drug is the property that denies it the eye. The model recovers the four compounds'
hepatoselectivity ordering with no hepatoselectivity parameter anywhere in it.

**Why row 4 is a hazard and not a lead.** Seladelpar reaches its margin because it needs a
hepatic concentration factor of only 1.5×, so it does not depend on the missing transporter.
That margin is at **PPARδ** — the dominant isoform in every vascular and immune compartment of
human retina (microglia 2.8×, ganglion cells 1.77×, smooth muscle 1.18×, endothelium 1.15×,
pericytes 1.10× over PPARα **[M]**) and a pro-angiogenic one. **The only local receptor
engagement achievable from an oral dose in this class is at a receptor whose engagement may
worsen the disease.**

**Two mechanisms are closed.** The hepatic-to-retinal **FGF21 relay fails**: achievable plasma
FGF21 on a fibrate sits **25× below the lowest demonstrated active concentration (95% CI
6–99×) [Mod]**, and human retina does not express the obligate co-receptor β-Klotho (**KLB
0.0 nTPM, 9th percentile, against 16.6 in liver [M]**). The **restore-a-deficit framing is
unsupported**: retinal *PPARA* is not reduced in diabetes (macula +3%, periphery −6%, both
null; a ≥1.40× / ≥1.26× change would have been detected at 80% power [M]).

**The proposed escape route is costed, and it is unfavourable.** A neutral, retina-penetrant
PPARα ligand is buildable — the AF-2 cage geometry is now measured at **2.222 ± 0.064 Å between
the two engaged ligand acceptor atoms across five agonist complexes [M]** — but going neutral
raises neural-retina Kp,uu ~20× and gives back more than that in potency and efficacy. The best
neutral scaffold requires **36 g/day** for free-EC₅₀ occupancy; a lipophilicity-stripped acid
control requires 3.7 g/day and still beats every neutral by 9.7× [Mod]. **The free-drug margin
rises monotonically with logP across the whole drug-like range**, so the low-logD design
strategy is inverted: moving from logP 5.6 to 2.8 costs ≈200–350× [Mod].

**What is missing from the table, and where a drug could still act.** No compound above
accelerates lipid *clearance* from the retina; every one reduces what arrives. That is the
largest uncovered module in the disease and the one place the arithmetic favours a new agent:
**802 of 1,009 potent LXR ligands are neutral [M]**, which relieves the isoform-selectivity
requirement by **1.16 log units [Mod]** relative to an acid. No public molecule yet
demonstrates the required selectivity in a cell. And the framing that constrains all of this is
itself questionable: **DR is already treated by injection into the target compartment**, for
which the entire barrier problem does not arise.

**The single measurement that would most change the ranking:**

> **A PPARα and PPARδ EC₅₀ panel for all four compounds in one assay, at a stated and measured
> medium albumin concentration, with a parallel arm at physiological (40 g/L) albumin.**

At the endothelium and RPE — the two compartments that face the blood and where the vascular
lesion sits — **the EC₅₀ and the serum conditions it was measured in carry 69% of the output
variance; the entire barrier block carries 19% [Mod]**. It is cell culture, it takes weeks, and
it needs no animal. **If the free EC₅₀s come back 10× below the corrected values here, rows 3
and 4 reach parity and their verdicts are withdrawn.** This displaces the aqueous-humour tap
from the critical path.

---

## 1. CANDIDATE RANKING

**The full field.** The abstract gives the four compounds that carry a retinal margin; this is
all eight, with measured affinity at each of the three PPAR isoforms and the basis for every
role. The ordering criterion is **certainty of engaging a named target in a named
compartment** — not potency, and not weight of accumulated evidence. The disease stage is the
same for all of them: mild-to-moderate non-proliferative disease (§9). The evidence behind
every column is in §4–§8.

**Read it as a ranking of experimental priority, not of assets.** Several entries are
deliberately *instruments* — probes that measure whether a mechanism operates, and control
arms that make a result interpretable. A poor chronic drug can be the best available probe.

**How to read the margin column.** Margin is free drug concentration divided by free EC₅₀ at
the **retinal vascular endothelium** — the compartment that faces the blood directly and is
therefore the most favourable of the three, quoted at peak rather than average plasma
concentration. **A margin of 1.0 means free drug sits exactly at the free EC₅₀; the reciprocal
is the fold shortfall.** Every value in the column is below 1. Modelled **[Mod]** over 23
inputs; bounds, the other two compartments and the average-concentration figures are in §5.7.

| # | Compound | Role | Measured PPARα / PPARδ / PPARγ (pChEMBL) | Endothelial margin, Cmax | Basis |
|---|---|---|---|---|---|
| **1** | **Fenofibric acid** | **Lead, systemic limb only** | **4.82 median, 5.58 best** / — / 4.00 | **0.020** (51× short) | Certain hepatic engagement; the only fibrate lowering apoB particle number; the compound the DR clinical evidence actually rests on. Local engagement excluded |
| 2 | Pemafibrate | Lead alternate — **downgraded** | **9.00** / 5.80 / 5.96 | 0.027 (37× short) | Most potent and the **worst retinal drug of the four**: most dependent on a hepatic transporter the retina lacks (required liver Kp,uu 91.6×), and its selectivity excludes the PPARδ-dominant compartments where the pathology is |
| 3 | Elafibranor (**+ GFT1007**) | **Probe (12 wk)** | 8.00 / **8.00** / 6.76 | **0.136** (7.3× short, P = 0.147) | Closest of the PPARα three, and only because its active metabolite carries 3.2× the parent's exposure. Equal PPARδ potency makes it a **pro-angiogenic risk** in retinal vasculature |
| 4 | **Seladelpar** | **PPARδ probe — reclassified** | 5.82 / **8.72** / — | **0.558** on PPARδ (1.8× short, P = 0.34) | **The only compound of the four within reach of a retinal receptor**, because it needs a hepatic concentration factor of only 1.5×. At PPARα it is 1,340× short. See §11.1 — this is a hazard finding as much as an opportunity |
| 5 | Olezarsen | **Control** | — | — | Matched non-PPAR apoC-III suppression — the decisive discriminating arm |
| 6 | Inclisiran | **Falsification arm** | — | — | 3–5× the apoB effect of any fibrate; if apoB mass is the mechanism, it should work better |
| 7 | Fenofibrate | Prodrug of #1 | 6.00 / — / 6.24 | — | Adds an esterase step and a food effect without adding pharmacology; **42× worse ocular distribution than the acid by the systemic route [C]** |
| 8 | Candesartan | Comparator | — | — | Engagement certain at a luminal target; blocked by background therapy |

Affinities **[M]**, from 5,271 / 3,223 / 7,913 validity-filtered activities on human PPARA
(CHEMBL239), PPARD (CHEMBL3979) and PPARG (CHEMBL235). Margins **[Mod]**, §5.7.

**Bottom of the field, with the reason each fell:** quercetin (its apparent breadth is an
artefact of study volume — §1.2); minocycline (its papilloedema risk attacks the very endpoint
being measured); epalrestat (excellent engagement of a *falsified* target); and the dietary
fatty acids (**not dose-movable** — plasma concentrations already sit at their own EC₅₀, so
there is no dose that changes anything).

**What is absent from this table and should not be.** No compound here accelerates lipid
*clearance* from the retina; every one of them reduces what arrives. That gap is the largest
uncovered module in the disease and it is treated in §11.2.

### 1.1 Three measured corrections to the ranking's own logic

Each of these reverses something the raw pharmacology would imply, and each is why the order
above differs from an ordering by potency.

**The lead's potency is a distribution, and its median is 15 µM.** Fenofibric acid's PPARα EC₅₀
has a median of **15,000 nM over 13 determinations** with five further records censored at
>10,000 nM — i.e. five laboratories reporting no activity where the most favourable single
record sits **[M]**. Taking the minimum of that distribution as the value is worth ~5.7×. The
ranking is unchanged — it ranks on certainty of hepatic engagement, and hepatic portal
concentrations plus a 37× uptake factor engage a micromolar EC₅₀ — but the compound is a weak
binder at its own receptor.

**Potency does not buy engagement, and here it buys negative engagement.** Pemafibrate exceeds
fenofibric acid by **3.4 log units best-vs-best and 4.5 log median-vs-median [M]**
(*n = 3 for pemafibrate, all EC₅₀ — thin and not to be over-read*), and circulates at roughly
four orders lower free concentration. Its endothelial margin is **worse** than fenofibric
acid's at average concentration. **A more selective PPARα agonist is a worse retinal drug, not
a better one.**

**The route comparison favours the acid over the ester.** Systemic versus topical dosing of the
same drug in the same study gives a **42× penalty for the prodrug fenofibrate but only 3.4× for
the active metabolite fenofibric acid [C]**. *That is a route comparison, not a partition ratio
— it carries no information about the blood-to-retina ratio, and should not be used as one.*

### 1.2 Why this ranks on measured affinity rather than on target coverage

The obvious way to rank compounds against a disease is to count how many of its genes each one
is recorded as hitting. That method does not work, and the failure is large enough to invert an
ordering: **a compound's hit count against a disease gene panel, as reported by curated
interaction databases, is close to unrelated to its measured binding.** Quercetin illustrates
it **[M]**:

| Quercetin | Value |
|---|---|
| Curated interaction count, 27-gene panel | **26 of 27** |
| ChEMBL genes bound at ≤1 µM, 43-gene panel | **3** (AKR1B1 7.83, MMP9 6.76, KDR 6.55) |
| PPARα effector genes bound at ≤1 µM | **0** |

The pattern is general: of 153 compounds in the original coverage set, **15 bind any panel gene
at ≤1 µM and 3 bind any PPARα effector gene at ≤1 µM**; mean effector genes bound across the
152 matched compounds is **0.046 [M]**. Catalogue size correlates with hit count at
**r = 0.911**, and a random set of 20 compounds covers ≥26 of those 27 genes with probability
**0.58**.

**One caution that must not be dropped:** a blank is not a zero. Absence of a ChEMBL activity
means *not measured in ChEMBL*, not *no interaction*.

### 1.3 What would change this ranking

One measurement, and it is cheap. **The EC₅₀ values above were determined in media whose
protein content is mostly unstated**, which overstates them by 2.3–5.2× (§5.5), and the EC₅₀
together with those serum conditions carries **69% of the variance in the margin column**
(§5.9). A PPARα and PPARδ panel run across all four compounds in one assay at a stated,
measured albumin concentration would resolve it in weeks, in cell culture, with no animal.

**If the free EC₅₀s come back 10× below the corrected values here, elafibranor and seladelpar
reach parity at the endothelium and rows 3 and 4 change meaning entirely.** Nothing else in
this table is within a decade of moving — fenofibric acid and pemafibrate are 51× and 37×
short, and §5.8 explains why that shortfall is mechanistic rather than a dosing problem.

---

## 2. STATE OF KNOWLEDGE

| Question | Answer | Basis |
|---|---|---|
| Is PPARα expressed in human retina? | **Yes, decisively.** 7.9–68.0% of cells in every major class against a 0.00–0.1% ambient floor; 92nd percentile of the expressed transcriptome in 523 retinas | **[M]** |
| In which cells? | Rods 68.0%, RPE 64.8%, cones 54.5% — behind the barrier. Endothelium 15.4%, microglia 15.5%, Müller 18.2% — where the mechanisms are | **[M]** |
| Is it reduced in diabetes? | **No.** Null at both retinal sites, no severity gradient, power-bounded | **[M]** |
| Does PPARδ exceed PPARα in retina? | **Globally no; in every vascular and immune compartment, yes** | **[M]** |
| Is local PPARα necessary for retinal protection? | **Yes, in endothelium and microglia**, confound-free by design. Unknown for rods, cones, RPE, Müller glia | **[M]** |
| Can an oral fibrate engage it locally? | **No.** 37–1,340× short at the most favourable compartment, at peak plasma concentration | **[Mod]** |
| Why not? | Hepatoselectivity. These drugs need a 37–92× hepatic concentration step from OATP1B, which retina does not express | **[Mod] from [M]** |
| What is retinal exposure? | Neural retina Kp,uu **0.059 [0.009–0.354]**; endothelium and RPE are not behind a barrier — ceiling 1.0, median retention 0.32 | **[Mod]** |
| Does the FGF21 relay close? | **No. It fails** on concentration, on a failed 10⁴× native-hormone dose, on a missing co-receptor, and on epidemiological sign | **[Mod] + [M]** |
| Is any compound within reach of a retinal receptor? | **One.** Seladelpar, 1.8× short at Cmax — at **PPARδ**, which is pro-angiogenic | **[Mod]** |
| Can the efflux arm be drugged? | **Only through LXR.** 3,729 of 3,732 measured activities on the axis are at LXR-α/β; ABCA1, ABCG1, APOA1 and APOE have none | **[M]** |
| Can a non-acidic PPARα ligand be built? | **Yes, and it is not worth building.** Three competent neutral head groups exist; the best needs 36 g/day | **[M] + [Mod]** |
| What is the highest-variance unmeasured input? | The EC₅₀ and its assay protein concentration — 69% at the endothelium and RPE | **[Mod]** |

---

## 3. THE SCIENTIFIC QUESTION

PPARα is a ligand-activated nuclear receptor governing fatty-acid catabolism. The retina is the
most metabolically active and most lipid-dense tissue per gram in the body. Photoreceptor outer
segments are shed and phagocytosed daily by the retinal pigment epithelium, which oxidises those
lipids through fatty-acid β-oxidation as a genuine energy source. **The receptor is present and
the pathway it controls is one the tissue actually runs.**

Two framings commonly used to support this hypothesis do not survive the data.

**Retinal PPARα is not deficient in diabetes [M].** In the only public human neural-retina
series with a graded diabetic axis (GEO **GSE160306**, 79 samples from 43 donors, macular and
peripheral punches analysed separately), *PPARA* moves +0.046 log₂ in macula (p = 0.836) and
−0.096 log₂ in periphery (p = 0.367), with no correlation to retinopathy severity (ρ = +0.057
and −0.102). The minimum effect detectable at 80% power is **1.40× in macula and 1.26× in
periphery**, so this is a bounded null rather than an underpowered silence. Any agonist effect
must be **supraphysiological activation of a normally expressed receptor**, which carries a
different dose-response and a different safety argument than correcting a deficit.

**The receptor is most abundant where a drug can least reach, and least abundant where the
mechanisms live [M].** See §4.

### 3.1 Why the lipid axis is under-served

Hard exudates in DR are **not "fat."** They are retained, glycated-and-oxidised apoB
lipoproteins deposited in Henle's layer, and that modified species is directly cytotoxic to
pericytes, endothelium, Müller cells and RPE through endoplasmic-reticulum stress **[R]**.

This resolves a standing paradox: plasma LDL cholesterol tracks DR poorly, while apoB particle
number and remnant particles track it well. **If the toxic agent is the modified particle rather
than cholesterol load, the relevant intervention lowers remnant supply, not LDL.**

No current therapy clears hard exudate, and subfoveal lipid causes permanent vision loss even in
anatomically dried eyes. The lipid axis is the mechanistically neglected module of this disease.

### 3.2 Four limbs, four different experiments

| | Limb | Drug acts at | Effect appears at | Status |
|---|---|---|---|---|
| **1** | Lipoprotein supply | Hepatocyte | Plasma composition → retina | **Live by elimination.** Engagement certain; clinical evidence disfavours it as the agent of benefit |
| **2** | Humoral relay (FGF21) | Hepatocyte | FGF21 → retinal endothelium, luminal side | **Closed. Fails** — §6 |
| **3** | Local transrepression | Retinal endothelium / microglia / RPE | NF-κB → ICAM-1 → leukostasis | **Biologically necessary, pharmacologically unreachable** — §7 |
| **4** | Local transactivation | Neural retina | PPRE-driven fatty-acid-oxidation genes | **Excluded quantitatively**, ~600× short — §8 |

**The fibrate benefit observed in FIELD and ACCORD-Eye is real and is now unexplained by any of
the four.** That is the honest state of the mechanism question, and it is a sharper statement
than "unresolved."

---

## 4. THE RECEPTOR IN HUMAN RETINA

### 4.1 Expression, measured

**% of cells with ≥1 UMI.** CZ CELLxGENE Discover Census LTS release `2025-11-08`;
**4,828,235 adult non-diseased human retinal cells, 24 datasets, 16 publications**; raw counts
read and detection computed from them. All **[M]**.

| Gene | Rod | Cone | RPE | Müller | Bipolar | Amacrine | Horiz. | RGC | Astro | Endo | Peri | VSMC | Micro |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| *n cells* | 1.21M | 149k | 121k | 256k | 739k | 596k | 85k | 444k | 39k | 141k | 20k | 16k | 77k |
| **PPARA** | **67.97** | **54.51** | **64.77** | 18.17 | 12.62 | 11.76 | 7.89 | 13.04 | 20.91 | 15.39 | 19.90 | 18.97 | 15.50 |
| **PPARD** | 13.33 | 15.57 | 13.03 | 16.13 | 8.60 | 26.39 | 14.79 | 23.13 | 14.53 | 17.67 | 21.93 | 22.45 | **43.03** |
| **PPARG** | 0.29 | 3.87 | 1.56 | 1.36 | 3.77 | 5.36 | 2.51 | **46.31** | 11.22 | 3.66 | 17.17 | 23.92 | 15.15 |
| *TBP* (low-abundance housekeeping) | 6.45 | 10.64 | 6.38 | 8.47 | 8.44 | 13.46 | 11.01 | 21.47 | 7.91 | 5.27 | 4.99 | 5.63 | 4.80 |
| *KDR* (benchmark drug target) | 2.09 | 2.77 | 1.83 | 60.15 | 6.06 | 1.47 | 3.23 | 1.19 | 51.69 | 41.42 | 3.14 | 2.72 | 2.05 |
| **ALB / INS / PRM1 / KRT1 / MYH7** (negative controls) | ≤0.03 | ≤0.05 | ≤0.71 | ≤0.30 | ≤0.09 | ≤0.27 | ≤0.14 | ≤0.24 | ≤0.32 | ≤0.10 | ≤0.11 | ≤0.12 | ≤0.05 |

**How to read it.** Six negative controls set the ambient floor at **0.00–0.1%**. PPARA ranges
**7.9–68.0%**. There is no retinal cell type in which PPARA sits at the floor. In rods, cones and
RPE it exceeds the low-abundance housekeeping genes *TBP* and *POLR2A*.

Four independent cohorts agree on abundance **[M]**:

| Source | PPARA | PPARD | PPARG |
|---|---|---|---|
| **EyeGEx bulk, GEO GSE115828, n = 523 retinas** | 143.5 CPM, **92.4th percentile** of expressed genes, detected in **99.8%** of retinas | 31.7 CPM, 62.6th | 1.55 CPM, 6.4th |
| **GSE160306**, macula / periphery, control means | 129.6 / 227.5 CPM, 91.8th / 95.7th percentile | 43.3 / 47.4 CPM | 4.08 / 1.63 CPM |
| **Human Protein Atlas bulk retina** | 16.6 nTPM, 79.8th percentile (liver: 30.8) | 10.1 nTPM | 0.6 nTPM |
| **Census single-cell, rods** | 68.0% of 1.21M cells | 13.3% | 0.29% |

PPARA in human retina sits at **54% of its own level in liver [C]**. An unsupervised whole-body
single-cell clustering assigns *PPARA* to a photoreceptor/phototransduction cluster alongside
*RHO* and *NR2E3*, flagging it "cell type enhanced" in rods at 680 nCPM, **above hepatocytes
(327) [M]**.

PPARA, PPARD and PPARG are present in the feature space of **24 of 24 retina datasets [M]**, so
no zero reported here is a missing-feature artifact. Every zero is a measured non-detection.

### 4.2 The apparent antibody-versus-transcriptomics conflict is a detection artifact

Three measured mechanisms account for the impression that retinal atlases do not show *PPARA*.

**(a) Detection rate of a transcription factor is largely a measure of the assay.** Binning
whole-cell retinal cells by sequencing depth, PPARA detection swings **4.07% → 40.58%** from the
first to the tenth decile with no biology changing **[M]**. Across atlases the dependence is
near-deterministic for low-abundance genes (Spearman *TBP* detection vs median genes/cell =
**0.934, p = 1.8 × 10⁻⁹**, n = 20). The negative controls make this interpretable: *PRM1* and
*INS* stay at 0.00% across all ten deciles while PPARA climbs tenfold. **Depth recovers real
signal; it does not manufacture it.**

**(b) The transcript is nuclear-enriched, so whole-cell protocols under-report it.** Restricted
to rod photoreceptors, composition controlled, ten atlases from seven publications: whole-cell
rods **11.7–29.1%**; single-nucleus rods **53.0–82.0% [M]**. The two distributions do not
overlap, their depth ranges do, and *GAPDH* moves in the opposite direction (95–100% → 18–70%).

**(c) The comparison gene determines the conclusion.** In rods, *ACTB* is detected in only 16.8%
of cells — rods are so dominated by phototransduction transcripts that ordinary housekeeping
genes are squeezed out in CPM terms **[M]**. Benchmarking PPARA against *ACTB* in rods makes it
look abundant; against *GAPDH* in Müller glia (80.8%) makes it look absent.

The atlases that shaped the field's impression are shallow (493–1,890 genes/cell) **whole-cell**
datasets, in which PPARA in rods reads 11.7–29.1% beside *GAPDH* at 95–100%. On a dot plot that
looks like background.

**What survives is a real discordance about *which cells*, not *whether*.** The antibody
literature leads with Müller glia, endothelium, ganglion cells and microglia; those are the
compartments with the **lowest** PPARA transcript. Three explanations are live and cannot be
separated from these data: genuine protein/mRNA divergence for a long-lived nuclear receptor;
antibody specificity; or sampling bias, since immunohistochemistry resolves glia and vessels
better than densely packed outer-nuclear-layer nuclei. Decisively, **the reference antibody
resource has never stained retina for PPARα** — its retina IHC panel covers 113 proteins and
includes no PPAR isoform, and it grades PPARα immunofluorescence "Uncertain" on both its
antibodies (HPA066941, CAB075701) **[M]**.

### 4.3 The isoform split follows the neural/vascular boundary

| Cell class | PPARA % | PPARD % | **PPARD : PPARA** |
|---|---:|---:|---|
| Rod photoreceptor | 67.97 | 13.33 | 0.20 |
| RPE | 64.77 | 13.03 | 0.20 |
| Cone photoreceptor | 54.51 | 15.57 | 0.29 |
| Astrocyte / other glia | 20.91 | 14.53 | 0.69 |
| **Müller glia** | 18.17 | 16.13 | **0.89** |
| **Pericyte** | 19.90 | 21.93 | **1.10** |
| **Vascular endothelium** | 15.39 | 17.67 | **1.15** |
| **Vascular smooth muscle** | 18.97 | 22.45 | **1.18** |
| **Retinal ganglion cell** | 13.04 | 23.13 | **1.77** |
| **Amacrine cell** | 11.76 | 26.39 | **2.24** |
| **Microglia / macrophage** | 15.50 | 43.03 | **2.78** |

All **[M]**. In bulk, PPARA leads comfortably (4.5× in EyeGEx, 3–5× in GSE160306) — but that
ratio is dominated by rods, which are ~70% of retinal cells, and **it conceals a complete
reversal in the vasculature.**

**This converts isoform selectivity from a safety preference into a targeting constraint** — and,
as the ranking in §1 and the assessment in §11.1 set out, into a hazard. PPARδ is pro-angiogenic and shares the transrepression
machinery. Every local-engagement mechanism proposed for DR is sited in endothelium, pericytes,
Müller glia or microglia — each PPARδ-dominant or PPARα/PPARδ-balanced.

Separately, **PPARG is the retinal ganglion cell isoform** (46.3%, vs PPARA 13.0%) and a
vascular-mural isoform (VSMC 23.9%) **[M]** — and among 2,652 DR gene-disease associations it
ranks **9th with a genetic association score of 0.750, while PPARA ranks 66th with none at all
[M]**. That signal most plausibly propagates from type 2 diabetes susceptibility across the
disease ontology rather than from retinopathy specifically. Resolving it is a single query and
has not been run.

### 4.4 A stoichiometric limit, offered as a hypothesis

PPARα cannot transactivate except as a PPARα::RXR heterodimer. The partner is scarcer than the
receptor in exactly the cells where the receptor is most abundant **[C, from [M] detection
rates]**:

| | Rod | Cone | RPE | Müller | Endothelium |
|---|---:|---:|---:|---:|---:|
| PPARA | 67.97 | 54.51 | 64.77 | 18.17 | 15.39 |
| ΣRXR (sum of marginals — an **upper bound**) | 10.60 | 73.95 | 19.79 | 26.82 | 25.21 |
| **PPARA : ΣRXR** | **6.4 : 1** | 0.74 : 1 | 3.3 : 1 | 0.68 : 1 | 0.61 : 1 |

In rods, PPARα outnumbers its obligate partner at least 6.4 to 1. **It is a hypothesis, not a
finding** — transcript stoichiometry is not protein stoichiometry, and RXR protein is
long-lived. It has a clean test: co-immunoprecipitation or proximity ligation in donor retina.
One nominal observation points the other way and should not be buried — *RXRA* **rises** with DR
severity at both retinal sites (periphery log₂FC +0.185, p = 0.037; ρ = +0.462 vs severity,
p = 0.003) **[M, nominal; does not survive FDR]**.

---

## 5. RETINAL DRUG EXPOSURE

### 5.1 Three compartments, not one range

The barrier is not a single hurdle, and this is the correction that changes the answer before
any arithmetic.

- **Retinal vascular endothelium *is* the inner blood-retinal barrier.** Its luminal membrane is
  in contact with plasma. There is no barrier between plasma and that membrane, so its free
  exposure is the free plasma concentration reduced only by what its own pumps return to the
  lumen. **Its ceiling is 1.0, and what puts it below is efflux, not partition.**
- **The retinal pigment epithelium faces the fenestrated choriocapillaris**, so choroidal
  interstitial free concentration is plasma free concentration. Also one membrane from the blood
  side — and the one compartment that can *exceed* plasma free concentration, because it
  expresses concentrative organic-anion uptake transporters.
- **Neural retina is the only compartment genuinely behind a tight junction**, and it is behind
  two: the endothelial junctions of the inner barrier and the RPE junctions of the outer.

The transporters are measured, in human cells **[M, HPA single-cell nCPM]**:

| | Gene | Retinal endothelium | RPE | Hepatocyte |
|---|---|---:|---:|---:|
| P-gp | ABCB1 | **507.4** | — | 75.2 |
| MRP4 (anion efflux) | ABCC4 | **178.2** | — | 2.4 |
| BCRP | ABCG2 | **142.0** | — | 32.6 |
| MRP5 (anion efflux) | ABCC5 | 18.8 | **822.8** | 4.1 |
| OAT3 (anion **uptake**) | SLC22A8 | 0.5 | **464.7** | 0.2 |
| OAT1 (anion **uptake**) | SLC22A6 | 1.2 | **63.9** | 0.1 |

> **Caveat.** This is mRNA, not protein, and **no fibrate is a confirmed substrate of any of
> these pumps at any ocular barrier.** The expression data establish that the machinery is
> present and abundant; they do not establish that these molecules are moved by it. That is why
> the efflux term is carried as a 0.2–5× prior rather than a value.

**Why logD is not the answer people expect.** Passive permeability *cancels out of a
steady-state partition ratio across a purely passive barrier*: if the only way out is the way
in, the ratio is 1 however slow it is, and low permeability buys time to equilibrium rather than
a lower plateau. These drugs are taken daily for years, so time to equilibrium is not the
constraint. Permeability lowers the plateau only when it competes with a route out that is not
the way in — and for these compounds that route is the measured efflux above.

### 5.2 The calibration anchor, and the unit trap inside it

**Huang et al. 2021**, *Biology (Basel)* 10(12):1328, **PMID 34943243**, Table 1. C57BL/6J mice,
fenofibrate **2 mg/kg/day intraperitoneally for 7 days**, LC-MS 6 h after the final dose. This
is the only measurement of any fibrate in ocular tissue after systemic dosing in any species.

| Compartment | Fenofibric acid, IP arm | |
|---|---|---|
| Vitreous/retina | **0.140 ± 0.044** ng/mg total protein | **[M]** |
| Plasma | **86.304 ± 22.780** ng/mg total protein | **[M]** |

**The unit is ng/mg of *total protein*, not ng/mg of tissue.** Converting it as a per-tissue-mass
figure overstates retinal concentration by the tissue's protein content — neural retina is ~10%
protein by wet weight, so 0.140 ng/mg protein is **14 ng/g tissue, not 140 [C]**. A factor of
ten, in the optimistic direction.

A second trap sits alongside it: tissue and plasma share one header, and read as a common unit
the retina:plasma ratio is 0.0016 while read as tissue-per-protein against plasma-per-volume it
is ~0.16 — **a 60× difference**. It is resolvable from the paper's own arithmetic. The
Discussion states choroidal fenofibrate is "approximately five-fold higher than the
concentration in the peripheral blood"; the table gives choroid 8.469 and plasma 1.726, and
8.469 / 1.726 = 4.9. **The authors take the ratio directly, so the columns are on one scale**,
and the common-unit reading is correct. That reading makes retinal exposure look *worse* by 60×,
which is the reason to trust it.

Inverting the anchor keeps the phases separate, because the sample is **pooled vitreous +
retina** and vitreous carries drug but almost no protein — so treating the pooled figure as a
retinal tissue concentration overstates retinal exposure:

```
Cu,retina = M × P / (V_vitreous + V_retina / fu,retina)
Cu,plasma = M_plasma × [plasma protein] × fu,plasma
```

**Result: Kp,uu (neural retina, fenofibric acid) = 0.0594 [95% CI 0.0090 – 0.3544] [Mod]** — a
16.8× exclusion (95% CI 2.8 – 111×).

### 5.3 Independent calibration

One experiment is a point, not a calibration. The check is human studies that measured a
systemically dosed drug in aqueous humour *and* plasma in the same patients at cataract surgery.
Aqueous humour is effectively protein-free (~0.5 mg/mL against plasma's ~70), so the measured
aqueous concentration **is** a free concentration, and `Kp,uu = (C_aqueous / C_plasma,total) /
fu,plasma` converts a published ratio into the quantity the model computes **[C]**.

| Drug | Charge | Aqueous/plasma | fu plasma | **Kp,uu (free/free)** | Source |
|---|---|---:|---:|---:|---|
| Aciclovir | neutral | 0.37 | 0.78–0.91 | **0.41–0.48** | PMID 6696872 |
| Levofloxacin | zwitterion | 0.33–0.57 | 0.62–0.76 | **0.43–0.92** | PMID 15917572 |
| Pefloxacin | zwitterion | 0.50–0.89 | 0.70–0.80 | **0.62–1.27** | PMID 1955654, n = 38 |
| Indometacin | **anion**, 99% bound | below assay limit | 0.01 | **< detection** | PMID 6626018 |

**At a tight-junction ocular barrier, a drug that is *not* an anionic efflux substrate reaches
roughly half of free plasma — Kp,uu ≈ 0.4–1.3 across three drugs, three studies and three
decades.** The model places an anionic fibrate at 0.059, an order of magnitude below that, and
the measured efflux machinery is the stated reason. Had the model returned ~0.5 for a fibrate it
would be saying the pumps do not exist.

The closest structural analogue studied at the retinal barrier proper: pravastatin, an anionic
statin acid, at the rat BRB — retinal uptake below that expected from its lipophilicity, vitreal
elimination **1.66× that of the bulk-flow marker mannitol**, efflux reduced by competing anions
(**PMID 26431714**) **[M]**. Retina-to-blood transport is dominant for that chemotype.

> **Caveat.** The blood-aqueous barrier is not the blood-retinal barrier. Both are tight-junction
> barriers carrying ABC and SLC transporters, but they are different tissues. This is a
> plausibility check, not a substitute measurement.

### 5.4 Ionisation, and why it matters less than expected

No experimental pKa exists for any of the four compounds in PubChem's experimental-properties
record, in ChEMBL, or in the reachable literature; pKa is therefore assumed from the measured
values of each head group's unsubstituted parent acid. The `logd` column is empty for all 3,276
drug records in the working dataset, and the cause is upstream: **ChEMBL's API no longer serves
`cx_logd`, `cx_logp` or `cx_most_apka` — all return null for all seven fibrates queried
directly [M]**. No amount of re-scraping fills it.

| Compound | pKa (prior) | logP | **logD(7.4)** | Neutral fraction |
|---|---|---:|---:|---:|
| Fenofibric acid | 2.8–3.5 | 3.81 | **−0.44** | 5.6 × 10⁻⁵ |
| Pemafibrate | 3.0–3.7 | 5.55 | +1.50 | 8.9 × 10⁻⁵ |
| Elafibranor | 2.8–3.5 | 5.16 | +0.91 | 5.6 × 10⁻⁵ |
| Seladelpar | 2.8–3.4 | 5.05 | +0.75 | 5.0 × 10⁻⁵ |

All **[C]**, Henderson-Hasselbalch. The compounds are **99.99% ionised at pH 7.4**. The
cytosol/plasma pH-partition term is **0.50** — a factor of two, not the orders of magnitude ion
trapping gives a base in a lysosome — and it cancels from the final comparison, because the
EC₅₀ assay's receptor sat in a cytosol at the same pH offset from its own medium.

### 5.5 The serum correction

Comparing free drug against a nominal EC₅₀ double-counts protein binding. A cell assay reports
the **total** concentration added to the well; albumin in the medium bound some of it. With
binding linear in albumin — true well below saturation, where an EC₅₀ sits — `EC50_free =
EC50_nominal × fu_assay` **[C]**.

| Compound | Receptor | Median EC₅₀ overstatement | 95% CI | In logs |
|---|---|---:|---|---:|
| Fenofibric acid | PPARα | **2.3×** | 1.2 – 7.9× | 0.35 log |
| Pemafibrate | PPARα | **3.8×** | 1.3 – 30.6× | 0.58 log |
| Elafibranor / GFT1007 | PPARα | **5.2×** | 1.8 – 24.3× | 0.72 log |
| Seladelpar | PPARδ | **5.0×** | 1.5 – 33.3× | 0.70 log |

"About a log" is right at the high-serum end and a third of that at the low. **Correcting it
lowers the EC₅₀ — it runs in the compounds' favour.**

**It is also what makes the one missing measurement harmless.** Once the EC₅₀ carries the same
binding term, free fraction appears on both sides and largely cancels. A **20-fold** swing in
pemafibrate's unmeasured plasma protein binding — absent from every label and from PubMed, PMC
and Europe PMC — moves its margin only **2.3× [Mod]**. The converse is the warning: an analysis
comparing free drug against an *uncorrected* nominal EC₅₀ gets a margin scaling with the full
free-fraction range, so its conclusion is dominated by a parameter that should be nearly
irrelevant.

### 5.6 Potency, as a distribution

26 PPARα EC₅₀ determinations from independent laboratories. **The inter-laboratory spread is the
uncertainty**; quoting one paper's figure hides it, and taking the minimum of a distribution as
its value is worth several-fold. Censored records (`>`) are reported but never averaged in.
All **[M]**.

| Compound | Receptor | n (=) | Median EC₅₀ | 95% CI | GSD | Censored (>) |
|---|---|---:|---:|---|---:|---|
| Fenofibric acid | PPARα | 13 | **15,000 nM** | 2,490 – 90,400 | 2.50 | 10,000 ×4, 100,000 |
| Pemafibrate | PPARα | 3 | **1.0 nM** | 0.17 – 6.0 | 2.50† | — |
| Elafibranor | PPARα | 8 | **290.5 nM** | 12.8 – 6,610 | 4.92 | — |
| Seladelpar | **PPARδ** | 3 | **2.0 nM** | 0.33 – 12.1 | 2.50† | — |
| Seladelpar | PPARα | 1 | 1,500 nM | 249 – 9,040 | 2.50† | 1,000 |

† GSD floored at 2.5. Three laboratories agreeing to one significant figure is agreement about
the order of magnitude, not evidence that between-assay spread is zero.

### 5.7 Margins

Plasma exposure is taken from FDA labels where one exists, with **Cavg,ss derived as AUC(0–τ)/τ**
rather than taken as Cmax, because a nuclear receptor at steady state sees the average. Cmax is
reported alongside as the best case. Elafibranor's major active metabolite GFT1007 carries
**3.2× the parent's exposure**, so omitting it would discard most of elafibranor's PPARα drive;
it is modelled as a fifth compound.

**23 inputs, 200,000 draws.** Margin = free concentration ÷ free EC₅₀, with the binding term
removed from both sides. All **[Mod]**.

| Compound | Receptor | Endothelium (Cavg) | RPE (Cavg) | Neural retina (Cavg) | P(endo ≥ 1) |
|---|---|---|---|---|---:|
| Fenofibric acid | PPARα | 0.0084 [6.8e-4 – 0.110] | 0.027 [9.9e-4 – 0.736] | 0.0016 [8.7e-5 – 0.027] | 0.000 |
| Pemafibrate | PPARα | 0.0035 [2.0e-4 – 0.058] | 0.011 [3.1e-4 – 0.373] | 0.0012 [1.3e-5 – 0.043] | 0.000 |
| Elafibranor **+ GFT1007** | PPARα | **0.031** [7.2e-4 – 1.42] | 0.098 [1.3e-3 – 7.96] | 0.0090 [8.5e-5 – 0.689] | 0.038 |
| **Seladelpar** | **PPARδ** | **0.210** [0.014 – 3.26] | **0.667** [0.021 – 21.3] | 0.047 [6.9e-4 – 1.73] | **0.135** |
| Seladelpar | PPARα | 2.8e-4 [1.9e-5 – 4.3e-3] | 8.9e-4 | 6.3e-5 | 0.000 |

At **Cmax** — the most favourable reading available — the endothelial margins become fenofibric
acid **0.0198** (51× short), pemafibrate **0.0267** (37×), elafibranor + GFT1007 **0.136** (7.3×,
P = 0.147), seladelpar on PPARδ **0.558** (1.8×, P = 0.34), seladelpar on PPARα 0.00074 (1,340×).

Dose multiple required to reach margin 1 at the endothelium, at Cavg:

| Compound | Labelled dose | Median fold increase needed | 95% CI |
|---|---|---:|---|
| Fenofibric acid | 135 mg/d | **119×** | 9 – 1,480× |
| Pemafibrate | 0.2 mg/d | **290×** | 17 – 4,930× |
| Elafibranor | 80 mg/d | 135× | 3.1 – 5,620× |
| **Seladelpar (PPARδ)** | 10 mg/d | **4.8×** | 0.31 – 71× |
| Seladelpar (PPARα) | 10 mg/d | 3,570× | 230 – 53,500× |

### 5.8 The calibration that decides whether to believe any of this

A model saying free fenofibric acid sits ~100× below its free PPARα EC₅₀ has an obvious problem:
**fenofibrate demonstrably activates hepatic PPARα — triglycerides fall 30–50%.** If the model
cannot explain how the liver manages it, the model is wrong.

Run backwards, the model states the hepatic concentration factor the observed effect requires
**[Mod]**:

| Compound | Receptor | Required liver Kp,uu | 95% CI |
|---|---|---:|---|
| **Pemafibrate** | PPARα | **91.6×** | 7.5 – 1,160× |
| Elafibranor | PPARα | 42.7× | 1.2 – 1,420× |
| Fenofibric acid | PPARα | **37.5×** | 4.0 – 335× |
| GFT1007 | PPARα | 13.5× | 0.37 – 476× |
| **Seladelpar** | **PPARδ** | **1.5×** | 0.14 – 16.5× |

Three things make this a check and not a rationalisation.

1. **The mechanism is the right one.** For a compound with low passive diffusion clearance —
   which a 99.99%-ionised acid is by construction — transporter-mediated uptake dominates
   intracellular concentration and hepatic Kp,uu can exceed 1. For contrast, ketoconazole, a
   neutral drug with no concentrative uptake, has a measured hepatic Kp,uu of **0.32–4.67**
   across six methods **[M]**. Values of 37–92× require active uptake.
2. **The ordering falls out, and it is the right ordering.** Pemafibrate is marketed precisely as
   the selective PPARα modulator with enhanced hepatic targeting, and it emerges as the most
   hepatic-concentration-dependent of the four. **No hepatoselectivity parameter exists anywhere
   in the model.**
3. **The transporter that would do it is measured, and measured absent from retina [M]:**

| Gene | Liver | Retina | Retina percentile |
|---|---:|---:|---:|
| **SLCO1B1** (OATP1B1) | **502.3** nTPM | **0.0** | 9.2 |
| **SLCO1B3** (OATP1B3) | **247.7** | **0.0** | 9.2 |

In retinal vascular endothelium specifically, SLCO1B1 is 0.4 nCPM and SLCO1B3 is 0.0.

> **The mechanism that makes a fibrate a drug is the mechanism that denies it the eye.** These
> compounds are not under-dosed for the retina; they are correctly dosed for a tissue that
> concentrates them 40–90×, and the retina is not that tissue. **Raising the dose does not fix a
> missing transporter** — the same shape of conclusion as §6's missing co-receptor.

**What was not verified:** no measured hepatic Kp,uu for any fibrate was found. The 37–92×
figures are the model's *prediction*, testable against sandwich-cultured human hepatocytes. The
support above is the mechanism, the contrast case and the ordering — not a matching literature
value.

### 5.9 Where the variance actually is

Saltelli/Jansen Sobol indices on log₁₀(margin), 23 inputs, 819,200 model evaluations per
compound-compartment. Indexed by block, because the decision — where to spend measurement
effort — is made between blocks, and a per-input ranking would make the barrier look
unimportant purely because its uncertainty is spread over eighteen parameters. All **[Mod]**.

**Endothelium and RPE** — the compartments that face the blood and where the vascular lesion is:

| Input block | mean ST | range across compounds |
|---|---:|---|
| **Potency (EC₅₀ + its assay serum conditions)** | **0.694** | 0.589 – 0.818 |
| Barrier (partition ratio, all 18 inputs) | 0.194 | 0.117 – 0.260 |
| Plasma exposure (dose, PK, binding) | 0.111 | 0.055 – 0.204 |

**Neural retina:**

| Input block | mean ST | range across compounds |
|---|---:|---|
| Barrier (partition ratio, all 18 inputs) | **0.509** | 0.356 – 0.633 |
| Potency (EC₅₀ + its assay conditions) | **0.428** | 0.279 – 0.601 |
| Plasma exposure | 0.064 | 0.041 – 0.097 |

First-order indices sum to ~1.0, so the model is near-additive in log space.

**This reorders the measurement programme.** The ranked list is: (1) a PPARα/δ EC₅₀ panel at a
stated physiological protein concentration — the single highest-variance input in the two
compartments that matter, cell culture, no animal; (2) mouse plasma protein binding of
fenofibric acid, one day of equilibrium dialysis, which tightens the calibration anchor;
(3) a measured shake-flask logP for all four, none of which has one; (4) **ocular PK after oral
dosing** — still the only thing that settles the neural-retina barrier block, still worth doing,
but third or fourth on variance rather than first.

### 5.10 What has not been measured

- **No fibrate concentration in any ocular compartment after oral dosing, in any species.** One
  reported oral attempt in rat found fenofibrate and fenofibric acid **below detection** in the
  eye — a negative measurement, not silence, but traced only to a secondhand citation and not
  independently verified.
- **No human ocular fibrate measurement of any kind**, after any route.
- **No measured free fraction in retinal tissue** for any fibrate.
- **No measured logP, logD or pKa** for any of the four.
- **No measured plasma protein binding for pemafibrate** anywhere accessible.
- **No protein-level transporter measurement.** §5.1 and §5.8 are mRNA, from one consortium.
- **GFT1007's own EC₅₀** is not separately determined; it is modelled as equipotent with the
  parent, which makes the combined elafibranor margin an upper bound.
- The RPE's **net** anion transport direction is unmeasured, so its prior spans a hundredfold
  and the RPE margins are the least trustworthy numbers in §5.7. **If RPE OAT1/OAT3 concentrate
  these acids, the compartment ordering inverts** — that is the single experiment that would
  most change the framing rather than the numbers.

---

## 6. LIMB 2 — THE FGF21 RELAY FAILS

The best-evidenced-looking mechanism was a hepatic-to-retinal humoral relay: a fibrate raises
plasma FGF21, and FGF21 protects retinal vasculature. Both halves are published. They are not
the same concentration, and the retina cannot receive the hormone.

### 6.1 A unit correction that runs against the conclusion

Every retinal in-vitro result in this literature is reported as "ng/mL FGF21." It is not FGF21.
It is **PF-05231023**, a CovX-body: two modified FGF21 molecules conjugated to a humanised
IgG1κ scaffold, **2:1 stoichiometry, ~190 kDa total [M]**, against mature human FGF21 at
**19.5 kDa [M]**. The conjugate is ~90% scaffold by mass. Converting through moles **[C]**:

```
100 ng/mL PF-05231023 ÷ 190,000 g/mol × 2 arms × 19,500 g/mol = 20,526 pg/mL FGF21-equivalent
 50 ng/mL PF-05231023                                          = 10,263 pg/mL FGF21-equivalent
```

Reading the clinical and retinal literatures as the same analyte overstates the retinal dose
~5×. **Correcting it halves the apparent gap** — against the verdict below, which is why the
verdict is trustworthy.

### 6.2 Both datasets on one axis

**Achievable, human plasma [M].** Baseline in non-diabetic adults 85–235 pg/mL by study median —
with a **250-fold range across 76 healthy individuals**, so any single "normal value" is a point
on a very wide distribution. Baseline in type 2 diabetes with retinopathy 450–670 pg/mL. Fibrate
fold-change **1.28–1.61** across four human studies (fenofibrate +28%, GW590735 +39%,
pemafibrate 0.4 mg/d +61% in n = 244 over 12 weeks). **Maximum absolute concentration achieved
on any fibrate: ~1,000 pg/mL.**

Assay platforms disagree: healthy-control medians span **85–235 pg/mL, a 2.8× spread**, across
seven kits **[M]** — carried into the model rather than argued away. A sharper problem bites
harder: fibroblast activation protein cleaves circulating FGF21 after Pro-171, the
β-Klotho-binding determinant; **10–34% of circulating FGF21 is C-terminally cleaved [M]**, and
deleting the C-terminal 10 residues costs **~50× in EC₅₀ [M]**. Essentially all published assays
are *total* assays, so the measured numerator **overstates** active hormone.

**Active, retinal [M].** Protection of primary human retinal microvascular endothelial cells
against VEGF-induced permeability was demonstrated at **50 and 100 ng/mL PF-05231023 only**.
**No concentration below 50 ng/mL has ever been tested on any retinal preparation.** That is the
most load-bearing uncertainty here, and it is handled by extending the lower tail of the
active-concentration distribution to 5,000 pg/mL — below anything ever tested.

**Two independent anchors on the denominator**, agreeing within 2.2× from entirely separate
experiments **[M]**: the retinal anchor (lowest protective concentration, 10,263 pg/mL
FGF21-equivalent) and a receptor anchor (FGF21 EC₅₀ for glucose uptake in human adipocytes,
1.16 nM = 22,620 pg/mL).

**The ratio [Mod]** — 200,000 Monte-Carlo draws over the published spread of every input:

```
baseline                    550 pg/mL   [249 – 1,213]
achievable, intact FGF21    598 pg/mL   [260 – 1,378]
active concentration     15,049 pg/mL   [5,012 – 44,809]

SHORTFALL, intact     25.0×   [6.3× – 98.7×]
log10 shortfall        1.40   [0.80 – 1.99]

P(achievable >= active)        = 0.0000
P(achievable >= 10% of active) = 0.095
```

Three calibration checks **[C]**: the modelled active concentration sits 1.2× below the bottom
of the band achieved in clinical FGF21-analog trials (17,500–150,000 pg/mL), exactly where an EC
should sit relative to developer-chosen exposures; reaching the active concentration from a
550 pg/mL baseline needs a **27× rise** against a delivered **1.28–1.61×**; and endogenous FGF21
in type 2 diabetes already sits 41× below the adipocyte EC₅₀, which is why the retinal anchor
carries the argument and the receptor anchor is corroboration only.

### 6.3 Three constraints harder than the arithmetic

**1. Native hormone at ~10⁴× endogenous did not work [M].** Native FGF21 at 5 mg/kg twice daily
had **no effect** on retinal neovascularisation in mouse oxygen-induced retinopathy, while the
28-hour-half-life conjugate at 1 mg/kg daily suppressed it (**PMID 28199833**). A fibrate's +40%
cannot do what 10³–10⁴× of the native hormone failed to do.

**2. The human retina lacks the obligate co-receptor [M].** FGF21 signals only as
FGF21·β-Klotho·FGFR1c; β-Klotho is the specificity subunit.

| Gene | Retina | Liver | Retinal percentile |
|---|---:|---:|---:|
| **KLB** (obligate co-receptor) | **0.0 nTPM** | 16.6 | **9.2** |
| FGFR1 | 14.4 | 8.0 | 76.9 |
| FGF21 (ligand) | **0.0** | 79.4 | 9.2 |
| **ADIPOR1** | **125.7** | 99.2 | **98.0** |

Per cell type, the two compartments the retinal FGF21 literature implicates are precisely the
two with abundant FGFR1 and essentially no KLB: Müller glia (FGFR1 214.4 nCPM, KLB 1.0) and
vascular endothelium (116.7, KLB 1.1), against 54.1 nCPM KLB in hepatocytes **[M]**. **No plasma
concentration repairs a missing co-receptor.** Caveats: this is mRNA; a small KLB⁺ subpopulation
would be invisible in pooled bulk; whole mouse retina has reported detectable *Klb* by RT-PCR, a
lower bar in a different species. A single-cell confirmation across the 24 retina datasets has
been specified and not completed, so this rests on one consortium's two arms.

**3. The epidemiological sign is wrong [M].** Higher plasma FGF21 predicted *more* microvascular
disease (n = 9,697, **PMID 26055067**), and a larger **fenofibrate-induced** FGF21 rise predicted
*faster* glycaemic progression (HR 1.18 top tertile, n = 9,697, **PMID 28606915**). FGF21
> 554.7 pg/mL carried **> 8× the risk** of sight-threatening DR in n = 654.

Most of this is plausibly reverse causation — FGF21 is a stress hormone that rises with
metabolic disease severity. **The second finding is not.** It is the within-patient,
treatment-induced change, which is the exact quantity the relay proposes is therapeutic, and in
9,697 patients it predicted a worse outcome.

### 6.4 The strongest counter-argument, and why it does not close the gap

Duration, not amplitude, separated success from failure in the decisive in-vivo experiment:
half-life 0.4 h failed, half-life 28 h succeeded. A fibrate gives the *right kinetics* and the
*wrong amplitude*.

| | Amplitude | Duration | Retinal effect |
|---|---|---|---|
| Native FGF21, 5 mg/kg BID | ~10³–10⁴× active | t½ 0.4 h | **none [M]** |
| PF-05231023, 0.5–10 mg/kg | ~1–10× active | t½ 28 h | **protective [M]** |
| **Fibrate in humans** | **0.04× active** | **sustained for months** | **never tested** |

**The cell that matters is empty**, and that is the honest residual uncertainty. Three things
stop it rescuing the mechanism: occupancy is set by concentration, so sustained sub-threshold
exposure gives sustained sub-threshold occupancy unless the readout integrates over time, which
has not been shown for any of these endpoints; the fibrate elevation has been observed for 12
weeks at +61% for a decade with no retinal readout ever attached; and *Fgf21*−/− mice do show
increased neovascularisation **[M]**, which establishes that the hormone matters but cannot
establish that a 40% increment moves a retinal endpoint — dose-response is not recoverable from
a null allele.

### 6.5 What survives: a different relay

The retinal biology is real and is **adiponectin-mediated** — deleting adiponectin **completely
abolished** FGF21's retinal protection in two separate models (**PMID 28199833**,
**PMID 36943533**) **[M]** — and the retina is built to receive adiponectin (ADIPOR1, 98th
percentile) and not FGF21 (KLB, 9th).

| Step | Status |
|---|---|
| Fibrate → plasma FGF21 ↑ 1.28–1.61× | **established [M]** |
| FGF21 → adipocyte (KLB-rich) | plausible |
| **Fibrate → plasma adiponectin in humans** | **UNQUANTIFIED — the open gap** |
| FGF21 analog → adiponectin ↑ in humans | established [M], but only at 17,500–150,000 pg/mL |
| Adiponectin → retinal protection | established in mouse [M] |
| Retina can receive adiponectin | established [M] |

The third row is the whole question now, and even the fourth has only been demonstrated at
concentrations a fibrate cannot reach.

---

## 7. LIMB 3 — NECESSARY, AND UNREACHABLE

This is the central finding of the report, and it is two results that point in opposite
directions and are both solid.

### 7.1 Local PPARα is necessary in endothelium and microglia

**Two cell-type-restricted conditional *Ppara* deletions in mouse retina have been published
[M]**, with two different inducible Cre drivers:

| Model | Driver | Finding | Source |
|---|---|---|---|
| **Endothelial-specific** cKO, with a conditional transgenic gain-of-function arm | *Vecad-CreERT2* | Decreased postnatal retinal vascular density; enlarged avascular area and fewer endothelial progenitors in oxygen-induced retinopathy; in 6-month streptozotocin diabetes, **declined ERG amplitude, decreased retinal thickness on OCT, increased vascular leakage** vs floxed-uninduced littermates. Mechanism: endothelial mitochondrial dysfunction and senescence | *Am J Pathol* 2026;196(4):960-975, **PMID 41485550** |
| **Microglia-specific** cKO, with a conditional transgenic arm | *Cx3Cr1-CreERT2* | No baseline phenotype without diabetes; under diabetes, **decreased ERG response, exacerbated pericyte loss**, increased subretinal microglial migration, glycolytic shift, increased STING/TNFα. The gain-of-function arm **alleviated** the diabetic phenotype | *Cells* 2022;11(23):3869, **PMID 36497130** |

Both use tamoxifen-inducible Cre to avoid developmental confounds, and both include Cre-only
toxicity controls.

**Why this settles the circularity concern.** The global *Ppara* knockout carries
hypertriglyceridaemia, abolished ketogenesis and FGF21, hepatic steatosis and an altered diabetes
response, so "worse retinopathy" in that animal is fully explained by the competing systemic
hypothesis. **In both conditional models, hepatic PPARα is intact — and therefore so are plasma
triglycerides, ketogenesis and FGF21 production — and the worsened diabetic retinal phenotype
still appears [M].** The systemic confound is structurally absent rather than statistically
adjusted. Both papers state this exclusion as their explicit purpose.

**Neither paper measures ANGPTL4** (checked by full-text search; zero hits in either) **[M]**.

### 7.2 No available drug reaches it

§5.7: endothelial margins of 0.0084–0.031 at average plasma concentration and 0.020–0.136 at
peak, requiring 119–290× the labelled dose. §5.8: the deficit is mechanistic, from a hepatic
uptake transporter the retina does not express, so it is not a dosing problem.

**The two results together are the report's central finding: a local target that genetics says
matters, and that no compound in this class can engage.**

Three resolutions are live and they are distinguishable by experiment:

1. **The clinical benefit comes from the systemic limb after all**, and the conditional-knockout
   phenotypes describe a biology that is real but not the one the drug uses. The covariate
   analysis of §12.3 discriminates this at no cost.
2. **The benefit is receptor-independent.** Fenofibrate has documented receptor-independent
   effects, and much supporting in-vitro work uses concentrations above where those appear,
   without knockout or antagonist controls.
3. **The exposure model is wrong somewhere.** The named places it could be: the RPE's net anion
   transport direction (prior spans 100×), the compound-independence of endothelial retention,
   and the EC₅₀ distribution itself, which carries 69% of the variance in the compartments that
   matter.

### 7.3 What remains open, and the inversion that makes it matter

**No conditional deletion exists for RPE, Müller glia or photoreceptors [M].** Necessity is
established for the **two lowest-PPARA compartments** (endothelium 15.4%, microglia 15.5%) and
unaddressed for the **three highest** (rods 68.0%, RPE 64.8%, cones 54.5%). Findings attributed
to global-knockout photoreceptor or RPE phenotypes — including the neuroprotection and
mitochondrial-efficiency results in *PLoS One* 2019;14(2):e0208399 (**PMID 30716067**) — remain
exactly as confounded as before.

**Local PPARα is necessary in precisely the compartments where it is least abundant, where its
pro-angiogenic sibling is more abundant, and where no drug has been shown to arrive at a free
concentration near its EC₅₀.**

---

## 8. LIMB 4 — LOCAL TRANSACTIVATION, EXCLUDED QUANTITATIVELY

Three arguments bear on whether an orally dosed fibrate can drive PPRE-dependent gene expression
in neural retina. One has strengthened decisively; one has weakened; one is a hypothesis.

**Decisive — the exposure arithmetic, now calibrated.** Neural-retina Kp,uu = 0.059
[0.009–0.354], and free fenofibric acid sits roughly **600× below its free PPARα EC₅₀** there
**[Mod]**. The conclusion is robust across all 23 model inputs. This is no longer an assertion
about partition ranges; it is a calibrated ratio with an anchor, two independent external
calibrations, and a hepatic back-calculation that recovers the compounds' known
hepatoselectivity ordering.

**Weakened — the claim that the programme is absent.** The fatty-acid-oxidation effectors are
robustly expressed in human neural retina **[M]**:

| Effector | Rod | Cone | RPE | Müller | Endo | Peri | Micro | EyeGEx CPM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **CPT1A** | 34.14 | 53.60 | 26.01 | 9.81 | 25.62 | 21.55 | 15.98 | 82.6 |
| **ACADM** | 22.06 | 41.27 | 18.58 | 16.93 | 12.09 | 9.62 | 9.07 | 55.2 |
| **ACOX1** | 13.87 | 24.97 | 27.14 | 18.39 | 12.69 | 12.49 | 11.63 | 79.0 |
| **ABCG1** | 41.96 | 16.92 | 14.12 | 16.05 | 33.33 | 3.10 | 18.25 | 70.2 |
| **ABCA1** | 6.25 | 26.69 | 44.18 | 1.00 | 20.15 | 34.40 | 53.39 | 31.2 |
| **PDK4** | 0.09 | 0.10 | 12.10 | 5.75 | 26.68 | 32.97 | 30.00 | 6.7 |
| **ANGPTL4** | 1.02 | 0.95 | 5.82 | 9.17 | 12.01 | 23.06 | 2.64 | 5.9 |
| **EHHADH** | 3.08 | 7.27 | **29.78** | 2.65 | 3.48 | 1.90 | 2.97 | 4.7 |
| **HMGCS2** | 0.03 | 0.03 | **22.95** | 0.02 | 0.78 | 0.69 | 0.64 | 0.19 |
| **FGF21** | 0.00 | 0.00 | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | **0.00** |
| **APOA1 / APOA5 / FABP1** | ≤0.25 | ≤0.21 | ≤0.06 | ≤0.19 | ≤0.43 | ≤0.33 | ≤0.13 | ≤0.08 |

Limb 4's **readouts exist**. Their absence from compound-binding and gene-disease databases
reflected what has been *studied*, not the biology: six of the sixteen effectors have no ChEMBL
target at all, and the fatty-acid-oxidation genes are absent from the DR association set
entirely **[M]** — but a pathway nobody has investigated in a disease is indistinguishable, in
those datasets, from a pathway that is genuinely uninvolved.

Two of those rows are assay specifications. **HMGCS2 is RPE-specific** (23.0% of cells, ≤0.1%
elsewhere) and a direct PPARα target, which makes it the one tractable local-transactivation
readout in human eye. **FGF21 is flat zero in every retinal cell type**, so the humoral relay of
§6 is necessarily hepatic-to-retinal with no local-production escape hatch.

One nominal hint points the right way and does not survive multiple-testing correction: *PDK4*
falls in diabetic peripheral retina (log₂FC −0.62, p = 0.015) **[M, nominal]**.

**A hypothesis — the stoichiometric ceiling.** §4.4. In rods, PPARα exceeds its obligate RXR
partner by at least 6.4 to 1, which would cap transactivation independently of drug
concentration.

**Net.** Limb 4 fails on exposure, by a margin large enough that the surviving uncertainties do
not reach it.

---

## 9. STAGING

**Mild-to-moderate non-proliferative disease.** The exposure-robust limb — lowering systemic
lipoprotein supply — is mechanically inoperative before the barrier leaks, because with an
intact blood-retinal barrier there is no extravasation to prevent **[R]**.

The conditional-knockout evidence sharpens this rather than softening it: both models show **no
baseline phenotype without diabetic stress** and a phenotype that emerges under it, which is the
signature of a mechanism operating during early injury rather than at steady state **[M]**.

### 9.1 Enrichment is harder than it looks

The obvious enrichment marker — existing hard exudate — **selects patients in whom a
supply-lowering mechanism is weakest**, because an established deposit is self-renewing and
clearance-limited. The marker that finds the lipid phenotype also finds patients past the point
where the mechanism acts.

Enrich on the **rate**, not the deposit: elevated remnants despite statin therapy, and new or
worsening lesions over a prior interval, excluding organised subfoveal plaque.

---

## 10. THE WRONG-SIGN RISK

ANGPTL4 — a direct PPARα target gene and a potent pro-permeability factor in ischaemic retina —
is a bounded liability, and the measurements now locate it and largely retire it.

- **It is sited in the right compartment, which would strengthen the concern.** ANGPTL4 in
  retina is a mural and endothelial transcript: pericytes 23.1%, smooth muscle 22.9%,
  endothelium 12.0%, versus ~1% in photoreceptors **[M]**.
- **And that compartment is PPARδ-dominant [M]**, so induction there would be driven by PPARδ
  engagement at least as much as by PPARα — which makes equal-potency dual agonists the specific
  hazard, not PPARα selectivity. §11.1.
- **The two objections are mutually destructive, and the exposure side is now quantified.**
  ANGPTL4 induction requires the gene-activation machinery that §5.7 places 37–1,340× out of
  reach. **If local engagement is too weak to help, it is too weak to harm**, and that is now a
  modelled statement rather than a symmetry argument.
- **A ceiling from already-measured data.** ANGPTL4 inhibits lipoprotein lipase, so meaningful
  induction predicts triglycerides to *rise*. Observed triglycerides *fall*. Real-world induction
  is bounded above by a quantity already in hand **[M]**.
- **The surviving path is systemic.** Hepatic engagement is certain, and fenofibrate and
  pemafibrate reliably raise circulating ANGPTL4 2–4× **[M]**, acting on endothelium from the
  luminal side. **Plasma ANGPTL4 is therefore a mandatory, cheap biomarker.**
- ANGPTL4 has **no ChEMBL target [M]** — it cannot be engaged directly by a small molecule, so
  biomarker is the only available role.

Among 2,652 DR gene-disease associations ANGPTL4 ranks 273rd with a **literature score of 0.776
— higher than PPARA's own [M]**. This is a genuinely active area, not a theoretical worry.

**Intraocular ANGPTL4 stratified by fibrate exposure has never been measured, in any species** —
verified by systematic search across ten distinct query strings **[M]**. The nearest adjacent
result is an in-vitro study in which pemafibrate raised ANGPTL4 mRNA in a human RPE cell line,
but **less** than a non-selective PPARα agonist did (**PMID 39768065**); that is evidence about
the mechanism, not the measurement.

---

## 11. WHERE A DRUG COULD STILL ACT

### 11.1 PPARδ in the retinal vasculature — the live question, and a hazard

Three measured facts collide here and none of them was available a year ago.

1. **PPARδ is the dominant PPAR isoform in every vascular and immune retinal compartment** —
   microglia 2.78×, amacrine 2.24×, ganglion cells 1.77×, smooth muscle 1.18×, endothelium
   1.15×, pericytes 1.10× over PPARα **[M]**, §4.3.
2. **Seladelpar is the only compound of the four that gets within reach of a retinal receptor**
   — endothelial margin 0.558 [0.038–8.59] at Cmax, RPE 1.77, P(margin ≥ 1) = 0.34 at the
   endothelium and 0.62 at the RPE, 4.8× dose short **[Mod]**. It achieves this because it needs
   a hepatic concentration factor of only 1.5×, so it is not relying on the transporter the
   retina lacks.
3. **PPARδ is pro-angiogenic**, and shares the transrepression machinery with PPARα.

**So the only local retinal receptor engagement achievable from an oral dose in this class is at
a receptor whose engagement may worsen the disease.** That is the sharpest statement the data
supports, and it cuts two ways:

- **As a hazard:** elafibranor engages PPARα and PPARδ equally (both pChEMBL 8.00 [M]) and is
  the designated 12-week probe. In the retinal vasculature it is not a neutral dual agonist. Any
  trial of a PPARδ-active agent in DR needs an angiogenic safety readout, not only an efficacy
  one.
- **As the one open local hypothesis:** if retinal benefit is transrepression rather than
  transactivation, PPARδ in microglia and endothelium is where the receptor density and the
  achievable occupancy actually coincide. Nobody has tested it.

**What would settle it.** Measure PPARδ alongside PPARα in every retinal engagement experiment —
in microglia and the vasculature PPARδ is the more abundant receptor, so an effect attributed to
PPARα there is not safely attributable without the control. And the EC₅₀ panel of §12.1 includes
PPARδ for exactly this reason.

### 11.2 The efflux arm — the one place the arithmetic favours a new agent

Every compound considered reduces what *arrives* in the retina. **Not one accelerates what
leaves.**

The lesion is a self-renewing cycle: modified lipoprotein → scavenger uptake → transporter
downregulated → cholesterol cannot leave → inflammasome activation and foam-cell death → lipid
re-released → re-uptake. Solving it as a two-compartment system gives burden = influx ÷
clearance exactly — the recycling term cancels. **But as clearance approaches zero the system
has no steady state; it integrates.**

**There is exactly one druggable node on the whole axis [M].** Of 3,732 qualifying activities
across nine axis genes (NR1H2, NR1H3, ABCA1, ABCG1, APOA1, APOE, CD36, OLR1, MSR1), **3,729 are
at LXR-α and LXR-β and zero are at ABCA1, ABCG1, APOA1 or APOE.** The effectors are readouts,
not pockets — no small molecule binds ABCA1 and makes it pump faster. The only approved drug
with a recorded ABCA1 mechanism is **probucol, an ABCA1 *inhibitor***.

**The structural opening is real and worth a number.** The PPARα pocket mandates a lipophilic
acid; the LXR pocket does not — **802 of 1,009 potent LXR ligands are neutral (79%) [M]**. Under
the §5 model, going neutral buys a **paired median 10–12× gain in neural-retina Kp,uu (95% CI
1.9–64×, P(gain) ≈ 0.99) [Mod]**, which converts directly into a relaxed safety requirement:

| Chemotype | Kp,uu | β-selectivity needed for a 10× hepatic margin |
|---|---:|---:|
| **Neutral LXR ligand** | 0.91 | **~1.55 log** |
| **Fibrate-like acid** | 0.059 | **~2.73 log** |

**The acid pays 1.16 log units more for the same hepatic margin, purely because it reaches the
retina ~15× less well [Mod].** And the acid route is empirically unoccupied: **of 83 measured
acidic LXR ligands, zero clear the 2.73-log bar** — the most selective reaches 2.66 **[M]**.
*"It cannot be done from the liver" is recovered here as arithmetic rather than asserted.*

**But no public molecule demonstrates the required selectivity where it counts.** Of 797 potent
dual-measured LXR ligands, 8 clear the neutral bar and 5 also pass a retinal-access filter —
and all five come from **one 2018 patent, on cell-free coactivator-recruitment data run in both
agonist and antagonist mode [M]**. In the **cell-based functional tier** — the only one that
measures transactivation — the maximum β-selectivity across 106 paired molecules is **1.37 log,
below the requirement. Not one clears it [M].** The isoform selectivity that makes the top
candidates viable has never been shown in a cell by anyone.

The chemotype also has its own liability: the physicochemical filter removes 712 of 1,009
ligands, and the dominant rejection is **excess lipophilicity** — 416 carry a logD > 5 flag,
median logP 6.21. **The LXR chemotype has swapped the fibrate's ionisation problem for a
lipophilicity-and-size problem.** Every named clinical agent fails it, including bexarotene,
which is an approved drug and an acid — the fibrate failure mode again.

**And the acceptor-versus-inducer ordering is backwards, in the regime the lesion describes
[Mod].** With burden `L` governed by `dL/dt = J_in − k_t·E·L − k_a·A·L`, an inducer *multiplies*
`E` while an acceptor *adds* a term:

| Arm | Steady-state burden at E = 0 |
|---|---|
| Untreated | **∞** |
| Supply-lowering, influx cut 10× | **∞** |
| Transporter inducer, **1000×** | **∞** |
| **Direct acceptor, 0.1× healthy clearance** | **10.0** |

A 1000-fold inducer changes nothing at E = 0, not even the time course, because it scales a term
that is zero. **The inversion is conditional and the condition is honest:** the acceptor
contributes more only below `E* = k_a·A / (k_t·(F−1))`, which for an acceptor at 0.1 against a
10× inducer is E ≈ 0.011. At E = 0.02 the inducer still wins. **`E` in human diabetic retina is
not measured in any species, and it is the single number that decides between the two
programmes.** They are also complementary rather than competing: the acceptor adds, the inducer
multiplies, and in combination at E = 0.02 they beat either alone.

> **The reframing that matters most.** apoA-I mimetic peptides, reconstituted HDL and
> cyclodextrins do not cross the blood-retinal barrier, so a direct acceptor is an
> **intravitreal** proposition. That is a different development path from an oral fibrate — but
> **it is the path this disease already uses.** Intravitreal dosing is standard of care in DR.
> The barrier that disqualifies the acceptor as a systemic drug is irrelevant to the route the
> indication already takes, and the entire exposure problem of §5 does not arise for it.

**Not closed, and not to be claimed.** No molecule here has been shown to raise ABCA1 in a
retinal cell, to reach the retina in any species, or to spare the liver in vivo. The strongest
supportable statement is that **this programme is arithmetically defensible where the fibrate
programme is not** — a statement about which experiment to run, not about a drug.

### 11.3 The non-acidic PPARα ligand — buildable, and not worth building

The structural retraction stands: **the carboxylate is a convention, not a mechanism.** What
fails is the inference from "legal" to "worth building."

**The pharmacophore is tighter than described, and that is the first cost.** Across five
independent PPARα agonist complexes the two engaged ligand acceptor atoms sit **2.222 ± 0.064 Å
apart (range 2.13–2.29) [M]**, not "roughly 2.2–3.2 Å". The upper half of that range is empty,
which converts the requirement from *a bidentate pair* into a **geminal** pair. And the contact
map is not four donors onto four atoms — it is **four donors onto two atoms**, one serving
Ser280 and Tyr314 (4.25 ± 0.21 Å apart), the other serving His440 and Tyr464 (3.61 ± 0.52 Å)
**[M]**. Each engaged atom must accept **two** hydrogen bonds, which an oxygen can and an
azole or pyridine-type nitrogen cannot.

> **Two measured corrections follow, both to recommendations that had been made.** The
> **1,2,4-oxadiazol-5(4H)-one fails** — it presents one double-acceptor atom and can serve at
> most two of the four donors. And **tetrazole fails on lone-pair capacity, not footprint**: its
> charge is delocalised over four ring nitrogens each with one in-plane lone pair, so **no atom
> in a tetrazole can accept two hydrogen bonds**, at any pKa or orientation. Computed, tetrazole
> is **1.32×** the carboxylate's volume — *smaller* than the oxazolidinone that passes. The
> right conclusion, for the wrong reason.

**The footprint argument is not supported.** Head-region free volume, ligand and waters deleted
**[C from [M] coordinates]**: PPARα agonist **40.8 ± 7.1 Å³**, PPARγ **38.6 ± 1.1 Å³** — equal
within error. The discriminator is geometry, not size: PPARγ's engaged acceptors span **4.46 Å
using three atoms** while PPARα's span 2.22 Å using two. That is a real selectivity handle
against γ. **Against PPARδ it gives nothing** — δ takes the same tight pair at 2.10 Å — and δ is
the isoform that matters most for retinal safety.

**Three neutral head groups survive the screen of 25**: oxazolidin-2-one (span 2.29 Å), dimethyl
sulfone (2.52), methanesulfonamide (2.53) **[C]**.

**The efficacy tax is smaller than feared and badly determined, and the standard assay overstates
it favourably.** A two-state H12 model puts a neutral head at **Emax 92–98% in a coactivator-rich
reporter line and 57–82% [95% CI 8–95%] in a coactivator-poor tissue [Mod]**. **The same molecule
reads 92% in the primary assay and 57% in the target organ** — a systematic bias, not noise.
The interval is dominated not by chemistry but by two receptor conformational-energetics
parameters that have never been measured for PPARα (rank correlations 0.73 and 0.59 against
log Emax, versus ≤0.06 for every chemistry input).

**And the design strategy is inverted.** Sweeping logP with molecular weight fixed, **the
free-drug retinal margin rises monotonically with logP across the entire drug-like range, for
both head types [Mod]** — because potency gains ~1.0 log per logP unit at constant LLE while
free fraction loses only 0.45–0.70. Moving from logP 5.57 to 2.79 costs **≈200× for a neutral
head and ≈350× for an acid.** The field put lipophilicity where it did because that is where the
free-drug margin is.

Five scaffolds carried end to end through the §5 model **[Mod]**:

| | **OXZ-1** | **SULF-1** | **PHOS-1** | **ACID-LOW** *(control)* | **HYDX-1** |
|---|---|---|---|---|---|
| Head | oxazolidin-2-one | methyl sulfone | phosphonamidate | carboxylate | hydroxamic acid |
| logD₇.₄ | 2.66 | 3.43 | 3.50 | −1.16 | 3.14 |
| EC₅₀, derived | 64 µM | 42 µM | **3.3 µM** | **2.0 µM** | 20 µM |
| Kp,uu neural retina | 0.82 | 0.94 | **0.96** | 0.041 | 0.94 |
| Emax, tissue | 0.61 | 0.57 | **0.82** | 1.00 | 0.57 |
| **Dose for free-EC₅₀ occupancy** | **833 g/day** | 1,058 g/day | **36 g/day** | **3.7 g/day** | 541 g/day |

Potency is derived from `pEC50 = LLE + logP`, calibrated against the only neutral PPARα ligand
with a measured EC₅₀: **oleoylethanolamide, predicted 126 nM against a measured 120 nM–3 µM [C]**.
Neutral PPARα ligands sit at LLE ≈ 1.0 (OEA 1.0, linalool 1.1), two and a half log units below
pemafibrate's anionic 3.45 — so a design target that transfers an anionic LLE onto a neutral
head is internally inconsistent.

**The neutral heads do exactly what they were supposed to do, and it is not enough.** Kp,uu rises
from 0.041 to 0.82–0.96 — a **19.7× improvement**, achieved precisely as predicted, by removing
the anion the barrier's efflux transporters recognise. **And it lands in the wrong compartment:**
the endothelium is blood-facing, so its retention term is compound-independent in this model, and
the whole 19.7× appears only behind the tight junction. The vascular lesion that defines DR is at
the endothelium.

> **The single assumption most worth attacking if someone wants to rescue this route.** That
> compound-independence is a modelling choice, not a measured result. If endothelial retention
> scales with the same efflux liability as the neural retina, every neutral scaffold improves by
> up to ~20× — bringing PHOS-1 to ~1.8 g/day and OXZ-1 to ~42 g/day. **Still not a dose, so the
> verdict is unchanged, but the margin of the verdict is not.**

**Probability of technical success to a Phase 2a retinal biomarker readout: 3–8% [R, from the
above]**, conditional on the rodent experiment of §12.2 reading positive. The dominant risks, in
order: the rodent experiment reads negative and there is no local target at all; potency cannot
be recovered from the arms against a 2–3 kcal/mol acceptor deficit; PPARδ selectivity is
unachievable from a compact neutral chemotype; and no regulatory endpoint for early DR
materialises — a programme risk larger than any chemistry risk.

**What would change it:** a measured H12 closure energy ≤ 1.5 kcal/mol (raises it to ~10–15%);
a third neutral PPARα ligand with LLE > 2.5, since the entire potency argument rests on a sample
of two and is cheap to strengthen; a measured Kp,uu at the top of the §5 interval (0.35), which
improves every row ~6× and brings the acid control to ~600 mg/day, which is a dose; or a geminal
double-acceptor head with carboxylate-like basicity and no charge, which is a well-posed
chemistry question nothing in physics forbids.

---

## 12. EXPERIMENTAL PROGRAMME

### 12.1 The highest-value measurement, and it is not the one the programme was sequenced behind

> **A PPARα and PPARδ EC₅₀ panel for all four compounds in one assay, at a stated and measured
> medium albumin concentration, with a parallel arm at physiological (40 g/L) albumin.**

At the endothelium and RPE — the compartments that face the blood and where the vascular lesion
sits — **the EC₅₀ and its assay serum conditions carry 69% of the output variance; the entire
barrier block carries 19% [Mod]**, §5.9. It is cell culture, it takes weeks, it needs no animal,
and it decides whether elafibranor and seladelpar are live.

**If the free EC₅₀s come back 10× below the corrected values here, elafibranor and seladelpar
reach parity at the endothelium and the verdict on those two is withdrawn.**

Two cheap companions carry ST ≈ 0.21 in the neural retina between them: **equilibrium dialysis
for mouse fenofibric acid plasma binding** (one day; tightens the calibration anchor) and a
**measured shake-flask logP** for all four (one week; none of them has one).

### 12.2 The experiment that tests the frame

**Chronic oral fibrate in a diabetic rodent, reading transactivation against transrepression,
with paired ocular LC-MS on the same animals** — so the pharmacodynamic readout is anchored to a
measured concentration rather than an assumed one. This is the experiment that discriminates
between the three resolutions of §7.2.

| Readout class | Markers |
|---|---|
| Transactivation (gene-activation driven) | retinal CPT1A, ACOX1, **HMGCS2 in RPE specifically**, **ANGPTL4** |
| Transrepression (PPRE-independent) | retinal ICAM1, TNF, IL6; adherent-leukocyte count |

| Result | Conclusion |
|---|---|
| Transrepression ↓, transactivation flat | A pharmacokinetically dissociated effect — anti-inflammatory action without gene induction, and therefore without the wrong-sign limb |
| Transactivation robustly ↑ | The exposure model is wrong by two orders of magnitude somewhere; ANGPTL4 risk live |
| Both flat **with confirmed ocular drug concentration** | **No achievable local engagement by oral dosing** — consistent with §5, and the local chemistry programme is unjustified |

Three arms are essential and one is now free. A **receptor-knockout arm** is available off the
shelf for endothelium and microglia (the *Vecad-CreERT2* and *Cx3Cr1-CreERT2* lines of §7.1). A
**matched non-PPAR lipid-lowering arm** remains to be run, and without it a positive cannot be
distinguished from "any lipid lowering would have done this". And **PPARδ must be measured
alongside PPARα throughout** — §11.1.

### 12.3 The discriminator that needs no new experiment

**Does benefit track the lipid change?** A covariate analysis, answerable from data routinely
collected. **If benefit does not track the lipid change, the supply limb is in trouble** — and
since §5 has now excluded the local limbs for these compounds, that result would mean the
mechanism is none of the four. Costs nothing; discriminates directly; run first.

### 12.4 The necessity question, rescoped

Conditional deletion is **complete for endothelium and microglia** and both read positive. What
remains is **RPE-, photoreceptor- and Müller-glia-specific deletion** — the three compartments
with the highest PPARα expression, where every existing retinal phenotype still comes from the
confounded global knockout. A rescoped item, not a from-scratch one.

### 12.5 Sequenced

| # | Experiment | Cost | Time | Decides |
|---|---|---|---|---|
| 1 | Lipid-change covariate analysis | ~$0 | weeks | Supply limb vs everything else. **Free — run first** |
| 2 | **PPARα/δ EC₅₀ panel at stated physiological albumin**, four compounds, one assay | **~$30–60k** | 2–3 mo | **69% of the variance** at the compartments that matter. Decides elafibranor and seladelpar |
| 3 | Equilibrium dialysis (mouse fenofibric acid) + shake-flask logP ×4 | ~$15k | 1 mo | Tightens the anchor and the second-ranked neural-retina input |
| 4 | **Validated PPARα immunostain on human donor retina**, per cell type, knockout or peptide-competition controls | ~$15–30k | 2–3 mo | The only surviving part of the antibody/transcript conflict. **No such stain exists** |
| 5 | Rodent transactivation vs transrepression, with paired ocular LC-MS, the off-the-shelf knockout arms, a non-PPAR lipid arm and PPARδ controls | $150–250k | 6–9 mo | **Whether any local engagement occurs at a measured concentration** |
| 6 | **ABCA1/ABCG1 activity in human diabetic retina** (`E`) | ~$50–75k | 6 mo | **Acceptor versus inducer, outright.** Unmeasured in any species |
| 7 | ABCA1/ABCG1 transactivation in a retinal cell + SREBF1 in a hepatocyte, for the LXR candidate series | ~$40k | 3–4 mo | Moves five candidates from cell-free claim to cellular fact, or kills them |
| 8 | Human aqueous drug + ANGPTL4 at cataract surgery | $50–100k | 6–12 mo | The neural-retina barrier block, and the wrong-sign question. **Demoted from first to eighth on variance — still the only human ocular PK that would exist** |
| 9 | Lipid clearance rate constant | ~$75k | 6 mo | Whether benefit is bounded or merely delayed |
| 10 | RPE / photoreceptor-specific conditional deletion | $150–300k | 18–24 mo | Necessity in the high-expression compartments |

**Items 1–7: roughly $300–470k over 9–12 months**, and they collectively decide whether any
programme here is worth running.

### 12.6 Cheap acquisitions that would move several answers at once

- **Whether human RPE OAT1/OAT3 take up any of these four.** The RPE is the only compartment
  that can exceed plasma free concentration, its OAT3 is at 464.7 nCPM, and the model's prior on
  net direction spans a hundredfold because nobody has looked. **If the RPE concentrates these
  acids, the compartment ordering in §5 inverts.** This is the experiment that would most change
  the framing rather than the numbers.
- **Re-analysis of the Huang 2021 samples with retina and vitreous separated**, which removes the
  pooling inversion and narrows the calibration anchor directly. Cheaper than a new study if the
  tissue is banked.
- **An efflux-substrate assay** for the four compounds against ABCB1, ABCG2, ABCC4 and ABCC5 — a
  standard vesicle assay that converts a 25-fold prior into a measurement.
- **A measured hepatic Kp,uu for any fibrate** in sandwich-cultured human hepatocytes, which
  would test §5.8's 37–92× prediction directly.
- **A DFT span calculation on the phosphonamidate head** before anyone synthesises on its 2.58 Å
  MMFF figure — the cheapest possible gate on the best neutral scaffold.
- **HDX-MS or ¹⁹F-NMR on the PPARα H12 region**, matched agonist pair, plus a
  coactivator-recruitment titration against SRC-1. These two parameters carry more of the Emax
  variance than every chemistry parameter combined, and neither has ever been measured.
- **A second diabetic human retina cohort.** GSE160306 is the only public human neural-retina
  series with a diabetic axis, and nothing in a 95-gene panel survives FDR in it.
- **A single-cell atlas of diabetic human neural retina.** None exists — 13,075,889 human eye
  cells are available and zero are diabetic **[M]**.
- **Single-cell confirmation of retinal KLB**, and the PPARG ontology-propagation query.
- **An FGF21 concentration-response on retinal endothelial cells below 50 ng/mL**, never run. If
  protection persists at ~205 pg/mL FGF21-equivalent, §6's verdict is wrong and withdrawn.

### 12.7 The assay cascade that does not exist

No PPARα programme has been run against free-drug retinal exposure, so the metrics are unbuilt.
**A conventional cascade would make three independent errors, all optimistic, all compounding:**
it would report a nominal EC₅₀ from a serum-containing reporter assay (double-counting protein
binding, worth 2.3–5.2×, §5.5); a total-drug tissue concentration (uninterpretable at a barrier
with active efflux, §5.1); and an Emax of 92% for a molecule that delivers 57% in retina
(§11.3). The cascade that would be needed:

| # | Assay | Gate | Why it is not standard |
|---|---|---|---|
| **0** | HDX-MS / ¹⁹F-NMR on H12; coactivator titration | Both conformational parameters bounded to ~1 kcal/mol | Never measured for PPARα; they carry ~0.73 and ~0.59 of the Emax variance |
| 1 | SPR/ITC on purified LBD **+ GW6471 antagonist reversal** | Saturable, reversible, competed | Discriminates engagement from the membrane-perturbant artefact small neutral lipophiles give at tens of µM |
| 2 | **Free-drug-corrected EC₅₀**: reporter at ≥3 serum concentrations, extrapolated to zero binding | Extrapolation linear in free fraction | Routine practice quotes a nominal EC₅₀ at one serum level |
| 2b | The same reporter at **two coactivator levels** | Emax reported **as a range**, never a point | Without it the assay systematically overstates tissue efficacy |
| 3 | Equilibrium dialysis in plasma **and retinal homogenate** | Both measured, same method | Kp,uu requires both; no measured retinal value exists for any fibrate |
| 4 | PAMPA/Caco-2 with a pH gradient, bidirectional, ± MRP/BCRP inhibitor | Efflux ratio < 2 | The pH-partition advantage of a shifted-pKa head is a measured property, not a predicted one |
| 5 | Transfected-cell uptake, **OATP1B1/1B3** | Not a substrate | The central design hypothesis — neutrality escapes OATP1B — must be tested. Digoxin and the taxanes are neutral OATP1B3 substrates |
| 6 | **Ocular distribution in a pigmented species**, free drug by microdialysis or homogenate-corrected | **Within [0.009–0.354], or the model is wrong** | §5's Kp,uu rests on a single measured ocular concentration. Pigmented, because melanin binding changes everything |
| 7 | PPARγ **and PPARδ** transactivation, full curves | ≥100× on both | δ is the one that matters and is routinely relegated to a secondary screen |
| 8 | FAAH/amidase stability in **retinal** homogenate; no absorbance >320 nm | — | The target organ is continuously illuminated and expresses FAAH |

### 12.8 Observation windows must be justified against clearance, not calendar

A **stock** readout (lesion burden) has time constant 1 ÷ clearance — the parameter this disease
suppresses. A **flux** readout (lesion turnover) responds directly. **A stock measure can read
flat at twelve months while the mechanism is working.** Flux primary; stock secondary, with a
window justified against the measured clearance rate.

### 12.9 Kill criteria

- Rodent study flat on both readouts **with confirmed ocular drug concentration** → no achievable
  local engagement by oral dosing; the local chemistry programme stops
- Matched non-PPAR lipid arm reproduces the effect → the receptor is not the agent of action
- Receptor knockout fails to abolish the effect → not receptor-mediated
- Benefit tracks lipid change tightly → a lipoprotein hypothesis; far more potent apoB-lowering
  agents exist than any fibrate
- EC₅₀ panel confirms the current values → elafibranor and seladelpar are dead for local
  engagement and only the systemic limb remains
- Validated immunostain shows PPARα protein absent from endothelium and microglia → the
  conditional-knockout phenotypes need a non-cell-autonomous explanation
- LXR candidate series fails cellular β-selectivity → the efflux arm is an acceptor problem, not
  an inducer problem, and the chemistry effort should stop

### 12.10 Combination work, and the route question that precedes it

The limb question determines which component a combination needs. **Two bench measurements
replace the modelling (~$100–150k):** the extracellular-removal term in a transporter-silenced
explant, and the clearance rate constant `E`.

The strongest concept is oral supply-lowering plus a **locally delivered ApoA1-mimetic
acceptor** at an injection visit these patients already attend. The acceptor adds a removal term
and the inducer multiplies one, so at low transporter activity they are complementary rather
than competing, and the acceptor alone guarantees a finite steady state where the inducer does
not.

> **Before any of this: the route assumption deserves attacking directly.** Candidates here have
> been ranked by oral-systemic feasibility for a disease whose standard of care is injection into
> the target compartment. Intravitreal delivery makes the entire exposure analysis of §5 moot for
> whatever is delivered that way. That is not a reason to prefer it uncritically — chronic
> intravitreal dosing carries its own burden and risk — but it is a reason to stop treating oral
> bioavailability as a precondition.

**Ruled out:** any supply agent plus scavenger-receptor blockade is **wrong-signed** — macrophage
uptake is the only catabolic route for retained lipoprotein in retina, so blocking it converts
dying foam cells into extracellular deposits nothing removes.

---

## 13. CONCLUSIONS

1. **Local PPARα in retinal endothelium and microglia is necessary, and no fibrate reaches it.**
   Two conditional knockouts establish necessity with the systemic confound structurally absent.
   A calibrated exposure model places every PPARα compound 37–1,340× short at the most
   favourable compartment, at peak plasma concentration. Both halves are solid and they point
   opposite ways; §7.2 lists the three live resolutions and the experiments that separate them.

2. **The shortfall is mechanistic, not a dosing problem.** These drugs need a 37–92× hepatic
   concentration step supplied by OATP1B, which retina does not express (502.3 nTPM liver vs 0.0
   retina). The property that makes a fibrate a drug denies it the eye. The model recovers the
   four compounds' known hepatoselectivity ordering with no hepatoselectivity parameter in it.

3. **The fibrate benefit in FIELD and ACCORD-Eye is real and is now unexplained by any of the
   four candidate limbs.** That is a sharper and more useful state than "unresolved".

4. **The FGF21 relay is closed and it failed.** A 25× concentration shortfall, a 10³–10⁴×
   native-hormone dose that did nothing, a missing co-receptor in human retina, and the wrong
   epidemiological sign in 9,697 patients. The surviving route runs through adipose and
   adiponectin, and its human fibrate leg has never been quantified.

5. **The restore-a-deficit framing is dead.** Retinal *PPARA* is not reduced in diabetes, with
   the null bounded by power.

6. **The one compound that reaches a retinal receptor reaches a pro-angiogenic one.** Seladelpar
   is 1.8× short at PPARδ at Cmax, and PPARδ dominates every vascular and immune compartment of
   human retina. This is a hazard finding for every PPARδ-active agent in DR before it is an
   opportunity, and elafibranor — the designated probe — is equipotent at both isoforms.

7. **Staging is unchanged and is the most robust conclusion here:** mild-to-moderate
   non-proliferative disease, reinforced by conditional knockouts that show no baseline
   phenotype and a diabetes-induced one.

8. **The non-acidic ligand is buildable and not worth building.** The pharmacophore is a
   2.222 ± 0.064 Å geminal pair, three neutral head groups clear it, going neutral raises
   neural-retina partition 19.7× — and the best neutral scaffold still needs 36 g/day while a
   lipophilicity-stripped acid needs 3.7 g/day. The low-logD strategy is inverted: the margin
   rises with logP. Probability of technical success 3–8%.

9. **The efflux arm is the one place the arithmetic favours a new agent**, because LXR ligands
   are 79% neutral and that relieves the selectivity requirement by 1.16 log. No public molecule
   demonstrates the needed selectivity in a cell, and whether an inducer or a direct acceptor is
   the right arm turns on one unmeasured number — retinal ABCA1/ABCG1 activity in diabetes.

10. **The critical path has moved.** The programme has been sequenced behind an ocular
    pharmacokinetic measurement that carries 19% of the variance in the compartments that
    matter. The EC₅₀ and its assay protein concentration carry 69%, and resolving them is cell
    culture rather than a clinical study.

11. **The route assumption is the largest unexamined premise.** This disease is treated by
    injection into the target compartment, and every candidate here has been judged on oral
    systemic exposure.

---

## APPENDIX — SUPPORTING MATERIAL

### Primary data and code

| Path | Contents |
|---|---|
| `src/analysis/ocular_exposure/` | 23-input exposure model; every input a tagged `Param` with a distribution. `report.py` regenerates every number in §5 |
| `src/analysis/retina_expression/` | Census, HPA, EyeGEx and GSE160306 arms |
| `src/analysis/fgf21_bridge/` | Plasma/active FGF21 comparison and the Monte-Carlo ratio |
| `src/analysis/efflux_axis/` | LXR axis pharmacology, physicochemical filter, steatosis selectivity grid, burden model |
| `src/analysis/ppara_ligand_design/` | AF-2 cage geometry from coordinates, head-group screen, H12 efficacy, scaffolds |
| `src/analysis/dr_matrix/` | Binding-evidence compound × gene matrix, pChEMBL-gated |
| `data/processed/ocular_exposure_margins.tsv` | 36 rows: compound × receptor × exposure × compartment, with bounds and P(margin ≥ 1) |
| `data/processed/retina_sc_celltype_summary.tsv` | Per-cell-type detection, 4.8M cells, 24 datasets |
| `data/processed/retina_sc_gene_presence.tsv` | Feature-presence matrix — absent vs below threshold |
| `data/processed/retina_hpa_celltype_ncpm.tsv`, `retina_hpa_bulk_ntpm.tsv` | Independent pipeline; KLB, ADIPOR1 and the barrier transporters |
| `data/processed/retina_bulk_dr_expression.tsv` | GSE160306 diabetic contrast with power bounds |
| `data/processed/chembl_panel_bioactivities.csv` | 62,219 measured activities; 16,407 on the PPAR receptors |
| `data/processed/efflux_axis_*.csv` | Axis targets, bioactivities, candidates, selectivity grid, burden model |
| `data/processed/ppara_af2_cage_*.tsv`, `ppara_headgroup_screen.tsv`, `ppara_h12_efficacy.tsv`, `ppara_nonacidic_scaffolds.tsv` | Structure geometry, the 25-head screen, Emax, five scaffolds |
| `data/processed/opentargets__DR_gene_disease.csv` | 2,652 DR gene-disease associations |

⚠ `opentargets__*` files carry `score_known_drug` and `score_clinical` columns encoding
approved-indication and trial evidence. **Drop both before any blinded re-run.**

### Detailed records

| Document | Contents |
|---|---|
| `docs/notes/retinal-exposure-model.md` | The exposure model in full: parameter table with provenance, calibration, sensitivity, per-compound verdicts |
| `docs/notes/ppara-retinal-expression.md` | Per-cell-type tables, atlas accessions, dropout analysis |
| `docs/notes/fgf21-concentration-bridge.md` | Both FGF21 datasets, the Monte-Carlo ratio, the co-receptor result |
| `docs/notes/dr-evidence-absence-audit.md` | The conditional knockouts, the ocular PK literature, full query logs |
| `docs/notes/retinal-lipid-efflux-candidates.md` | The LXR axis, the selectivity arithmetic, the candidate series and its defects, the burden model |
| `docs/notes/non-acidic-ppara-ligand-design.md` | AF-2 geometry, the head-group screen, the efficacy model, the five scaffolds, the assay cascade |
| `docs/notes/dr-data-gap-closure.md` | Affinity and gene-disease acquisition, and the panel |
| `docs/notes/dr-report-changelog.md` | Every claim in this report that changed, and what changed it |

### In this directory

| Document | Contents |
|---|---|
| `research-program.md` | The earlier experimental agenda, superseded by §12 where they differ |
| `BENCHMARK-RESULT.md` | Rediscovery scoring and methodological retrospective |
| `data-quality-findings.md` | 22 data defects |
| `disease-model.md` | DR pathobiology — stages, nine pathway modules, compartments |
| `consensus-report.md`, `round1-synthesis.md`, `round2-synthesis.md`, `debate-summary.md` | Earlier syntheses, retained as a dated record |
| `blinding-protocol.md`, `data-inventory.md`, `scoring/`, `agents/` | Method and provenance |

⚠ `agents/UNBLINDING-part-b.md` contains a held-out answer key. Do not read it, or expose it to
any agent, when re-running the benchmark.

**Research disclaimer.** This is a computational and literature-based analysis. Nothing here is
a clinical recommendation. All findings require experimental validation.
