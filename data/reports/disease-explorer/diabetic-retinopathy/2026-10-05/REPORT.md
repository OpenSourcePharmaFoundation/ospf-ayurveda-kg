# PPARα as a Therapeutic Target in Diabetic Retinopathy
## What is measured, what is modelled, and the one measurement that still decides it

**Report revised** 2026-11-03 · **Original analysis** 2026-10-05
**Scope** Treatments for diabetic retinopathy (DR), with specific focus on PPARα (gene *PPARA*)

---

## PROVENANCE TAGS

Every quantitative claim in this report carries one of four tags. Conflating them —
presenting reasoning with the confidence of measurement — is the failure this report is
written to avoid.

| Tag | Meaning |
|---|---|
| **[M]** | **Measured.** Read from a primary experimental result, with the source named |
| **[C]** | **Computed.** Derived from measured values by arithmetic stated at the point of use. No new assumption |
| **[Mod]** | **Modelled.** Output of a model over distributions chosen to span a published spread. The assumptions are stated |
| **[R]** | **Reasoned.** A pharmacological argument with no measurement behind it |

An untagged number in this report is an error.

---

## ABSTRACT

**Compound.** Fenofibric acid remains the lead for DR, on certainty of hepatic engagement
rather than potency. Its affinity for its own receptor is now measured and is weaker than
the lead position implies: **pChEMBL 5.58 (≈2.6 µM) at human PPARα [M]**, below the
conventional ≤1 µM activity threshold that fenofibrate (6.00), elafibranor (8.00) and
pemafibrate (9.00) clear.

**Stage.** Mild-to-moderate non-proliferative disease. Unchanged, and the strongest surviving
conclusion in this report.

**Mechanism.** Of four candidate routes, **the live one is local, cell-autonomous PPARα in
retinal vascular endothelium and microglia.** Cell-type-restricted conditional *Ppara*
deletion in mouse endothelium (PMID 41485550) and microglia (PMID 36497130) each reproduce a
worsened diabetic retinal phenotype — declining ERG, retinal thinning, vascular leakage,
pericyte loss — **with hepatic PPARα, plasma triglycerides, ketogenesis and FGF21 all intact
[M]**. The competing systemic explanation is structurally absent in those animals, not merely
adjusted for. Local PPARα is necessary in those two compartments.

**Two mechanisms are now closed.** The hepatic-to-retinal **FGF21 relay fails**: achievable
plasma FGF21 on a fibrate sits **25× below the lowest concentration at which retinal
protection has been demonstrated (95% CI 6–99×) [Mod]**, and the human retina does not express
the obligate co-receptor β-Klotho (**KLB 0.0 nTPM, 9th percentile of the retinal
transcriptome, against 16.6 nTPM in liver [M]**). And the **restore-a-deficit framing is
unsupported**: retinal *PPARA* is not reduced in diabetes (macula +3%, periphery −6%, both
null; a ≥1.40× / ≥1.26× change would have been detected at 80% power [M]).

**Retinal exposure — the actual number.** Retinal fibrate concentration has been measured, by
LC-MS, in rodents. In mouse retina + vitreous after intraperitoneal fenofibrate 2 mg/kg/day ×
7 days: **fenofibric acid 0.140 ± 0.044 ng/mg tissue [M]** (PMID 34943243) = **439 nM, range
301–577 nM [C]**. Against the measured PPARα EC₅₀ of 2,630 nM, that is **≈6× below, range
4.6–8.7× [C]** — with both sides uncorrected for protein binding, and with retina and vitreous
pooled. That is within one order of magnitude, far narrower than any purely pharmacological
estimate of neural-retina partition gives. **It is not the human oral number:** no fibrate
concentration has ever been quantified in any ocular compartment after **oral** dosing in any
species, and the one reported attempt was below the assay's detection limit.

**A targeting constraint that only expression data reveals.** The isoform split in human retina
follows the neural/vascular boundary. PPARα dominates rods (68.0% of cells), RPE (64.8%) and
cones (54.5%); **PPARδ dominates every vascular and immune compartment** — microglia 2.8×,
smooth muscle 1.18×, ganglion cells 1.77×, endothelium 1.15×, pericytes 1.10× [M]. The
compartments where local PPARα has just been shown to be *necessary* are the compartments
where it is *least abundant* and where its pro-angiogenic sibling is more abundant.

**The single measurement that still decides the rest:**

> **Free fenofibric acid concentration in human aqueous humour under chronic oral dosing,
> drawn at routine cataract surgery, paired with aqueous ANGPTL4 in the same tap.**

The assay is mature — three independent groups have validated ocular LC-MS for this analyte
since 2019 [M]. The human oral measurement has never been made, and intraocular ANGPTL4
stratified by fibrate exposure has never been measured in any species. One draw settles both.

---

## 1. STATE OF KNOWLEDGE

| Question | Answer | Basis |
|---|---|---|
| Is PPARα expressed in human retina? | **Yes, decisively.** 7.9–68.0% of cells in every major class, against a 0.00–0.1% ambient floor; 92nd percentile of the expressed transcriptome in 523 retinas | **[M]** |
| In which cells? | Rods 68.0%, RPE 64.8%, cones 54.5% — the compartments behind the barrier. Endothelium 15.4%, microglia 15.5%, Müller 18.2% — the compartments the mechanisms need | **[M]** |
| Is it reduced in diabetes? | **No.** Null at both retinal sites, no severity gradient, power-bounded | **[M]** |
| Does PPARδ exceed PPARα in retina? | **Globally no; in every vascular and immune compartment, yes** | **[M]** |
| Is local PPARα necessary for retinal protection? | **Yes, in endothelium and microglia**, confound-free by design. Unknown for rods, cones, RPE, Müller glia | **[M]** |
| Does the FGF21 relay close? | **No. It fails** on concentration (25×, CI 6–99×), on a failed 10⁴× native-hormone dose, on a missing co-receptor, and on epidemiological sign | **[Mod] + [M]** |
| What is the fibrate's measured affinity for PPARα? | Fenofibric acid 2.6 µM; pemafibrate 1.0 nM; elafibranor 10 nM; seladelpar 1.5 µM (and 1.9 nM at PPARδ) | **[M]** |
| What is retinal drug exposure? | One measurement exists: 439 nM total fenofibric acid in mouse retina+vitreous after IP dosing, ≈6× below the measured EC₅₀ | **[M] → [C]** |
| What is retinal exposure after **oral** dosing? | **Unmeasured in every species.** One attempt, below detection | — |
| Can the efflux arm be drugged? | **Unexamined.** No candidate set has been assembled | — |
| Can a non-acidic PPARα ligand be built? | **Unexamined.** The structural argument that it is possible stands; no molecule has been designed | — |

---

## 2. THE SCIENTIFIC QUESTION

PPARα is a ligand-activated nuclear receptor governing fatty-acid catabolism. The retina is
the most metabolically active and most lipid-dense tissue per gram in the body. Photoreceptor
outer segments are shed and phagocytosed daily by the retinal pigment epithelium, which
oxidises those lipids through fatty-acid β-oxidation as a genuine energy source. **The
receptor is present and the pathway it controls is one the tissue actually runs** — a better
starting position than most repurposing hypotheses.

Two framings commonly used to support this hypothesis do not survive the data.

**Retinal PPARα is not deficient in diabetes [M].** In the only public human neural-retina
series with a graded diabetic axis (GEO **GSE160306**, 79 samples from 43 donors, macular and
peripheral punches analysed separately), *PPARA* moves +0.046 log₂ in macula (p = 0.836) and
−0.096 log₂ in periphery (p = 0.367), with no correlation to retinopathy severity
(ρ = +0.057 and −0.102). The minimum effect detectable at 80% power is **1.40× in macula and
1.26× in periphery**, so this is a bounded null rather than an underpowered silence. Any
agonist effect in DR must therefore be **supraphysiological activation of a normally expressed
receptor**, which carries a different dose-response and a different safety argument than
correcting a deficit.

**The receptor is most abundant where a drug can least reach, and least abundant where the
mechanisms live [M].** See §3.

### 2.1 Why the lipid axis is under-served

Hard exudates in DR are **not "fat."** They are retained, glycated-and-oxidised apoB
lipoproteins deposited in Henle's layer, and that modified species is directly cytotoxic to
pericytes, endothelium, Müller cells and RPE through endoplasmic-reticulum stress **[R —
mechanistic reading of the pathology literature]**.

This resolves a standing paradox: plasma LDL cholesterol tracks DR poorly, while apoB particle
number and remnant particles track it well. **If the toxic agent is the modified particle
rather than cholesterol load, the relevant intervention lowers remnant supply, not LDL.**

No current therapy clears hard exudate, and subfoveal lipid causes permanent vision loss even
in anatomically dried eyes. The lipid axis is the mechanistically neglected module of this
disease.

### 2.2 Four limbs, four different experiments

PPARα agonism could act on DR through four mechanistically distinct routes. **They imply
different molecules, different disease stages and different experiments.**

| | Limb | Drug acts at | Effect appears at | Status after measurement |
|---|---|---|---|---|
| **1** | Lipoprotein supply | Hepatocyte | Plasma composition → retina | **Live.** Engagement certain; clinical evidence disfavours it as the agent of benefit |
| **2** | Humoral relay (FGF21) | Hepatocyte | FGF21 → retinal endothelium, luminal side | **Closed. Fails** — §5 |
| **3** | Local transrepression | Retinal endothelium / microglia / RPE | NF-κB → ICAM-1 → leukostasis | **Live, and now genetically necessary** — §6 |
| **4** | Local transactivation | Neural retina | PPRE-driven fatty-acid-oxidation genes | **Live but marginal.** Narrowed, not excluded — §7 |

---

## 3. THE RECEPTOR IN HUMAN RETINA

### 3.1 Expression, measured

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
**7.9–68.0%**. There is no retinal cell type in which PPARA sits at the floor. In rods, cones
and RPE it exceeds the low-abundance housekeeping genes *TBP* and *POLR2A*.

Four independent cohorts agree on abundance **[M]**:

| Source | PPARA | PPARD | PPARG |
|---|---|---|---|
| **EyeGEx bulk, GEO GSE115828, n = 523 retinas** | 143.5 CPM, **92.4th percentile** of expressed genes, detected in **99.8%** of retinas | 31.7 CPM, 62.6th | 1.55 CPM, 6.4th |
| **GSE160306**, macula / periphery, control means | 129.6 / 227.5 CPM, 91.8th / 95.7th percentile | 43.3 / 47.4 CPM | 4.08 / 1.63 CPM |
| **Human Protein Atlas bulk retina** | 16.6 nTPM, 79.8th percentile (liver: 30.8) | 10.1 nTPM | 0.6 nTPM |
| **Census single-cell, rods** | 68.0% of 1.21M cells | 13.3% | 0.29% |

PPARA in human retina sits at **54% of its own level in liver [C]** — the canonical PPARα
tissue. An unsupervised whole-body single-cell clustering assigns *PPARA* to a
photoreceptor/phototransduction cluster alongside *RHO* and *NR2E3*, flagging it "cell type
enhanced" in rods at 680 nCPM, **above hepatocytes (327) [M]**.

PPARA, PPARD and PPARG are present in the feature space of **24 of 24 retina datasets [M]**,
so no zero reported here is a missing-feature artifact. Every zero is a measured
non-detection.

### 3.2 The apparent antibody-versus-transcriptomics conflict is a detection artifact

Three measured mechanisms account for the impression that retinal atlases do not show *PPARA*.

**(a) Detection rate of a transcription factor is largely a measure of the assay.** Binning
whole-cell retinal cells by sequencing depth, PPARA detection swings **4.07% → 40.58%** from
the first to the tenth decile with no biology changing **[M]**. Across atlases the dependence
is near-deterministic for low-abundance genes (Spearman *TBP* detection vs median genes/cell
= **0.934, p = 1.8 × 10⁻⁹**, n = 20). The negative controls are what make this interpretable:
*PRM1* and *INS* stay at 0.00% across all ten deciles while PPARA climbs tenfold. **Depth
recovers real signal; it does not manufacture it.**

**(b) The transcript is nuclear-enriched, so whole-cell protocols under-report it.**
Restricted to rod photoreceptors, composition controlled, ten atlases from seven publications:
whole-cell rods **11.7–29.1%**; single-nucleus rods **53.0–82.0% [M]**. The two distributions
do not overlap, their depth ranges do, and *GAPDH* moves in the opposite direction (95–100% →
18–70%). The signature is shared across all three PPAR isoforms, so it is a family property,
not a *PPARA* quirk.

**(c) The comparison gene determines the conclusion.** In rods, *ACTB* is detected in only
16.8% of cells — rods are so dominated by phototransduction transcripts that ordinary
housekeeping genes are squeezed out in CPM terms **[M]**. Benchmarking PPARA against *ACTB* in
rods makes it look abundant; benchmarking against *GAPDH* in Müller glia (80.8%) makes it look
absent. Both are artifacts of the denominator.

The atlases that shaped the field's impression are shallow (493–1,890 genes/cell) **whole-cell**
datasets, in which PPARA in rods reads 11.7–29.1% beside *GAPDH* at 95–100%. On a dot plot
that looks like background.

**What survives is a real discordance about *which cells*, not *whether*.** The antibody
literature leads with Müller glia, endothelium, ganglion cells and microglia; those are the
compartments with the **lowest** PPARA transcript in the retina. Three explanations are live
and cannot be separated from these data: genuine protein/mRNA divergence for a long-lived
nuclear receptor; antibody specificity; or sampling bias, since immunohistochemistry resolves
glia and vessels better than densely packed outer-nuclear-layer nuclei. Decisively, **the
reference antibody resource has never stained retina for PPARα** — its retina IHC panel covers
113 proteins and includes none of PPARA, PPARD, PPARG, RXRA/B/G, KDR or FLT1, and it grades
PPARα immunofluorescence "Uncertain" on two antibodies (HPA066941, CAB075701) **[M]**.

### 3.3 The isoform split follows the neural/vascular boundary

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

All **[M]**. In bulk, PPARA leads comfortably (4.5× in EyeGEx, 3–5× in GSE160306, 1.6× in
HPA) — but that ratio is dominated by rods, which are ~70% of retinal cells, and **it conceals
a complete reversal in the vasculature.**

**This converts isoform selectivity from a safety preference into a targeting constraint.**
PPARδ is pro-angiogenic and shares the transrepression machinery. Every local-engagement
mechanism proposed for DR is sited in endothelium, pericytes, Müller glia or microglia — and
each of those is PPARδ-dominant or PPARα/PPARδ-balanced. Three consequences, all inferences
from measured affinity (§8) crossed with measured expression **[C]**:

1. **Elafibranor engages PPARα and PPARδ equally** (both pChEMBL 8.00 [M]), so in the retinal
   vasculature it is a **pro-angiogenic risk**, not a neutral dual agonist.
2. **Pemafibrate's 3.2-log PPARα/PPARδ margin** (9.00 vs 5.80 [M]) is exactly what avoids
   PPARδ — and therefore delivers almost no engagement in the PPARδ-dominant compartments
   where DR pathology lives.
3. **Seladelpar is functionally a PPARδ agonist** (PPARδ 8.72 vs PPARα 5.82 [M]). It would
   engage the dominant vascular isoform — which makes it a sharper probe of that compartment
   and a sharper angiogenic hazard at the same time.

Separately, **PPARG is the retinal ganglion cell isoform** (46.3%, vs PPARA 13.0%) and a
vascular-mural isoform (VSMC 23.9%) **[M]** — and among 2,652 DR gene-disease associations it
ranks **9th with a genetic association score of 0.750, while PPARA ranks 66th with none at all
[M]**. That signal most plausibly propagates from type 2 diabetes susceptibility rather than
from retinopathy specifically, since evidence propagates across the disease ontology.
Resolving whether it is DR-specific is a single query and has not been run.

### 3.4 A stoichiometric limit, offered as a hypothesis

PPARα cannot transactivate except as a PPARα::RXR heterodimer. The partner is scarcer than
the receptor in exactly the cells where the receptor is most abundant **[C, from [M] detection
rates]**:

| | Rod | Cone | RPE | Müller | Endothelium |
|---|---:|---:|---:|---:|---:|
| PPARA | 67.97 | 54.51 | 64.77 | 18.17 | 15.39 |
| ΣRXR (sum of marginals — an **upper bound**) | 10.60 | 73.95 | 19.79 | 26.82 | 25.21 |
| **PPARA : ΣRXR** | **6.4 : 1** | 0.74 : 1 | 3.3 : 1 | 0.68 : 1 | 0.61 : 1 |

In rods, PPARα outnumbers its obligate partner at least 6.4 to 1 — the cell type with the most
PPARα has the least capacity to use it for transactivation. This would be the first constraint
on limb 4 independent of drug concentration.

**It is a hypothesis, not a finding.** Transcript stoichiometry is not protein stoichiometry,
and RXR protein is long-lived. It has a clean test: co-immunoprecipitation or proximity
ligation in donor retina. One nominal observation points the other way and should not be
buried — *RXRA* **rises** with DR severity at both retinal sites (periphery log₂FC +0.185,
p = 0.037; ρ = +0.462 vs severity, p = 0.003) **[M, nominal; does not survive FDR]**.

---

## 4. RETINAL DRUG EXPOSURE — WHAT HAS ACTUALLY BEEN MEASURED

### 4.1 The measurements exist, for the wrong route

Fibrate concentration in ocular tissue has been measured by LC-MS more than once, in more than
one species, by independent groups. All **[M]**.

| Study | Species | Route | Ocular result |
|---|---|---|---|
| Huang 2021, *Biology (Basel)* 10(12):1328, **PMID 34943243** | Mouse | **Intraperitoneal, 2 mg/kg/day × 7 d** | Retina + vitreous: fenofibric acid **0.140 ± 0.044 ng/mg**, fenofibrate 0.033 ± 0.014 ng/mg |
| Huang 2021 (same study, comparator arm) | Mouse | Topical 0.1% drop | Retina + vitreous: fenofibric acid 0.472 ± 0.064, fenofibrate 1.402 ± 0.341 ng/mg |
| Kaffash 2026, *J Control Release* 391:114656, **PMID 41580131** | Rat | Topical microemulsion | Aqueous humour: fenofibric acid **131.0 ± 28.2 ng/g** at 1 h → 27.5 ± 11.2 at 4 h |
| Poudel 2026, *Int J Pharm* 689:126503, **PMID 41407273** | Rat, rabbit | Intravitreal depot | Sustained retinal levels ≥ 6 months |
| Qiu 2019, *Mol Pharm* 16(5):1958, **PMID 30912953** | Rat | Intravitreal | Quantified by LC-MS; free drug below quantification within days |

**The route comparison is itself a result.** Systemic (IP) versus topical dosing of the same
drug in the same study gives a **42× penalty for the prodrug fenofibrate but only a 3.4×
penalty for the active metabolite fenofibric acid [C]**. The active species distributes into
the eye from the systemic circulation far better than the prodrug does — a measured argument
for dosing the acid rather than the ester.

### 4.2 Placing the measured concentration against the measured affinity

Neither of these numbers is new; putting them on one axis is.

Converting the IP arm at tissue density 1.0 g/mL and fenofibric acid MW 318.75 **[C]**:

```
0.140 ± 0.044 ng/mg  =  140 ng/g  =  439 nM total fenofibric acid   (range 301 – 577 nM)
measured human PPARα EC50, pChEMBL 5.58                =  2,630 nM
                                        ratio  =  6.0× below   (range 4.6 – 8.7×)
```

**This is within one order of magnitude — substantially narrower than any estimate of
neural-retina partition derived from physicochemistry alone.** Five caveats bound it, and
none of them is small:

1. **Retina and vitreous were pooled.** Vitreous dilutes; retinal tissue alone could be
   higher. The direction of this error favours the mechanism.
2. **Intraperitoneal, not oral.** The clinically relevant route has never produced a bounded
   ocular value in any species. One reported oral attempt in rat found fenofibrate and
   fenofibric acid **below detection** in the eye — a negative measurement, not silence, but
   traced only to a secondhand citation and not independently verified.
3. **Total tissue concentration, not free.** Retinal tissue binding is unmeasured. Fenofibric
   acid is ~99% protein-bound in plasma; if intracellular binding is comparable, the free
   concentration is one to two logs lower.
4. **The EC₅₀ is also a nominal, protein-containing-medium number.** Comparing total tissue
   against nominal EC₅₀ is at least internally consistent, which comparing *free* drug against
   a *nominal* EC₅₀ is not — that inconsistency double-counts binding and is worth about a
   log. It is the error this comparison avoids rather than commits.
5. **Mouse at 2 mg/kg/day IP versus human at 145–200 mg/day oral (~2–3 mg/kg)** is similar on
   a mg/kg basis but not on exposure, since clearance scales allometrically and first-pass
   differs by route.

**The honest statement:** the single measured retinal concentration available puts fenofibric
acid within an order of magnitude of its measured receptor EC₅₀ on a consistently uncorrected
basis, by a route that is not the clinical one, in a compartment that was pooled with
vitreous. That is enough to stop treating local engagement as arithmetically excluded. It is
not enough to treat it as achieved.

### 4.3 Compartment matters more than the barrier

The barrier is not a single hurdle, and treating it as one conflates three very different
access problems **[R]**:

- **Retinal vascular endothelium sits on the blood side** of the inner blood-retinal barrier.
  A drug reaching it crosses no barrier at all — it binds a receptor in a cell facing the
  lumen.
- **RPE faces the fenestrated choriocapillaris.** Choroidal endothelium is fenestrated, so
  plasma reaches the RPE basolateral surface; engaging RPE PPARα requires crossing **one
  plasma membrane**, not the tight-junction barrier.
- **Neural retina sits behind the tight junction** and requires crossing it.

**The first two are exactly where the leukostasis, lipid-handling and ketogenic mechanisms
live** — and where the conditional-knockout evidence of §6 sites necessity. The partition
ratios attached to this argument remain **[R]**: no measured distribution, permeability or
protein-binding value exists for any fibrate in any ocular compartment, and the 439 nM figure
of §4.2 pools retina with vitreous and cannot be resolved to a compartment.

### 4.4 What has not been measured

- **No fibrate concentration in any ocular compartment after oral dosing, in any species.**
- **No human ocular fibrate measurement of any kind.**
- **No measured free fraction in retinal tissue**, for any fibrate.
- **No measured partition ratio.** Systematic search found none.
- **No parameterised ocular exposure model** has been constructed for this chemotype, so the
  question of which input dominates output variance — and therefore where measurement effort
  should go — is unanswered. Candidate inputs are dose, steady-state plasma concentration,
  measured fraction unbound, ionisation at pH 7.4 (these are acids with pKa ≈ 3, so logD at
  pH 7.4 is roughly −0.5 against a nominal logP near 3.8 **[R]**, and the measured logD column
  is empty for all 3,276 drug records in the working dataset), passive permeability, and
  efflux at the barrier.

An independent 2026 review of fenofibrate's ophthalmic repurposing (**PMID 42713229**)
reaches the same conclusion from outside this work, still asking for the pharmacokinetic
dataset **[M]** — corroboration that the gap is real rather than an artifact of search
coverage.

---

## 5. LIMB 2 — THE FGF21 RELAY FAILS

The best-evidenced-looking mechanism was a hepatic-to-retinal humoral relay: a fibrate raises
plasma FGF21, and FGF21 protects retinal vasculature. Both halves are published. They are not
the same concentration, and the retina cannot receive the hormone.

### 5.1 A unit correction that runs against the conclusion

Every retinal in-vitro result in this literature is reported as "ng/mL FGF21." It is not
FGF21. It is **PF-05231023**, a CovX-body: two modified FGF21 molecules conjugated to a
humanised IgG1κ scaffold, **2:1 stoichiometry, ~190 kDa total [M]**, against mature human
FGF21 at **19.5 kDa [M]**. The conjugate is ~90% scaffold by mass.

Converting through moles **[C]**:

```
100 ng/mL PF-05231023 ÷ 190,000 g/mol × 2 arms × 19,500 g/mol = 20,526 pg/mL FGF21-equivalent
 50 ng/mL PF-05231023                                          = 10,263 pg/mL FGF21-equivalent
```

Reading the clinical and retinal literatures as the same analyte overstates the retinal dose
~5×. **Correcting it halves the apparent gap** — the correction runs against the verdict
below, which is why the verdict is trustworthy.

### 5.2 Both datasets on one axis

**Achievable, human plasma [M].** Baseline in non-diabetic adults 85–235 pg/mL by study
median (with a **250-fold range across 76 healthy individuals**, so any single "normal value"
is a point on a very wide distribution); baseline in type 2 diabetes with retinopathy
450–670 pg/mL; fibrate fold-change **1.28–1.61** across four human studies (fenofibrate +28%,
GW590735 +39%, pemafibrate 0.4 mg/d +61% in n = 244 over 12 weeks). **Maximum absolute
concentration achieved on any fibrate: ~1,000 pg/mL.**

Assay platforms disagree: healthy-control medians span **85–235 pg/mL, a 2.8× spread**, across
seven kits **[M]**. That spread is carried into the model rather than argued away. A sharper
assay problem bites harder: fibroblast activation protein cleaves circulating FGF21 after
Pro-171, the β-Klotho-binding determinant; **10–34% of circulating FGF21 is C-terminally
cleaved [M]**, and deleting the C-terminal 10 residues costs **~50× in EC₅₀ [M]**. Essentially
all published assays are *total* assays, so the measured numerator **overstates** active
hormone.

**Active, retinal [M].** Protection of primary human retinal microvascular endothelial cells
against VEGF-induced permeability was demonstrated at **50 and 100 ng/mL PF-05231023 only**.
**No concentration below 50 ng/mL has ever been tested on any retinal preparation.** That is
the single most load-bearing uncertainty in this analysis, and it is handled by extending the
lower tail of the active-concentration distribution to 5,000 pg/mL — well below anything ever
tested.

**Two independent anchors on the denominator**, agreeing within 2.2× from entirely separate
experiments **[M]**: the retinal anchor (lowest protective concentration, 10,263 pg/mL
FGF21-equivalent) and a receptor anchor (FGF21 EC₅₀ for glucose uptake in human adipocytes,
1.16 nM = 22,620 pg/mL).

**The ratio [Mod]** — 200,000 Monte-Carlo draws over the published spread of every input:

```
baseline                    550 pg/mL   [249 – 1,213]
achievable, total FGF21     770 pg/mL   [341 – 1,741]
achievable, intact FGF21    598 pg/mL   [260 – 1,378]
active concentration     15,049 pg/mL   [5,012 – 44,809]

SHORTFALL, total      19.5×   [5.0× – 75.9×]
SHORTFALL, intact     25.0×   [6.3× – 98.7×]
log10 shortfall        1.40   [0.80 – 1.99]

P(achievable >= active)        = 0.0000
P(achievable >= 10% of active) = 0.095
```

Three calibration checks **[C]**: the modelled active concentration sits 1.2× below the bottom
of the band achieved in clinical FGF21-analog trials (17,500–150,000 pg/mL), exactly where an
EC should sit relative to developer-chosen exposures; reaching the active concentration from a
550 pg/mL baseline needs a **27× rise** against a delivered **1.28–1.61×**; and endogenous
FGF21 in type 2 diabetes already sits 41× below the adipocyte EC₅₀, which is why the retinal
anchor carries the argument and the receptor anchor is corroboration only.

### 5.3 Three constraints that are harder than the arithmetic

**1. Native hormone at ~10⁴× endogenous did not work [M].** In the one experiment that tested
it, native FGF21 at 5 mg/kg twice daily had **no effect** on retinal neovascularisation in
mouse oxygen-induced retinopathy, while the 28-hour-half-life conjugate at 1 mg/kg daily
suppressed it (**PMID 28199833**). A fibrate's +40% cannot do what 10³–10⁴× of the native
hormone failed to do.

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
vascular endothelium (116.7, KLB 1.1), against 54.1 nCPM KLB in hepatocytes **[M]**. **No
plasma concentration repairs a missing co-receptor.** Caveats: this is mRNA, not protein; a
small KLB⁺ subpopulation would be invisible in pooled bulk; whole mouse retina has reported
detectable *Klb* by RT-PCR, a lower bar in a different species. A single-cell confirmation
across the 24 retina datasets has been specified but not completed, so this rests on one
consortium's two arms (bulk and single-cell), not two consortia.

**3. The epidemiological sign is wrong [M].** In the largest human dataset linking plasma
FGF21 to retinopathy, higher FGF21 predicted *more* microvascular disease (n = 9,697,
**PMID 26055067**), and a larger **fenofibrate-induced** FGF21 rise predicted *faster*
glycaemic progression (HR 1.18 top tertile, n = 9,697, **PMID 28606915**). FGF21
> 554.7 pg/mL carried **> 8× the risk** of sight-threatening DR in n = 654.

Most of this is plausibly reverse causation — FGF21 is a stress hormone that rises with
metabolic disease severity, and DR severity tracks diabetes severity. **The second finding is
not.** It is the within-patient, treatment-induced change, which is the exact quantity the
relay proposes is therapeutic, and in 9,697 patients it predicted a worse outcome.

### 5.4 The strongest counter-argument, and why it does not close the gap

Duration, not amplitude, separated success from failure in the decisive in-vivo experiment:
half-life 0.4 h failed, half-life 28 h succeeded. A fibrate gives the *right kinetics* and the
*wrong amplitude*.

| | Amplitude | Duration | Retinal effect |
|---|---|---|---|
| Native FGF21, 5 mg/kg BID | ~10³–10⁴× active | t½ 0.4 h | **none [M]** |
| PF-05231023, 0.5–10 mg/kg | ~1–10× active | t½ 28 h | **protective [M]** |
| **Fibrate in humans** | **0.04× active** | **sustained for months** | **never tested** |

**The cell that matters is empty.** That is the honest residual uncertainty. Three things stop
it rescuing the mechanism: occupancy is set by concentration, so sustained sub-threshold
exposure gives sustained sub-threshold occupancy unless the readout integrates over time,
which has not been shown for any of these endpoints; the fibrate elevation has been observed
for 12 weeks at +61% for a decade with no retinal readout ever attached; and *Fgf21*−/− mice
do show increased neovascularisation **[M]**, which establishes that the hormone matters but
cannot establish that a 40% increment moves a retinal endpoint — dose-response is not
recoverable from a null allele.

### 5.5 What survives: a different relay

The retinal biology is real and is **adiponectin-mediated** — deleting adiponectin
**completely abolished** FGF21's retinal protection in two separate models (**PMID 28199833**,
**PMID 36943533**) **[M]** — and the retina is built to receive adiponectin (ADIPOR1 at the
98th percentile) and not built to receive FGF21 (KLB at the 9th).

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

## 6. LIMB 3 — LOCAL PPARα IS NECESSARY IN ENDOTHELIUM AND MICROGLIA

This is the live mechanism, and it rests on the strongest evidence in this report.

**Two cell-type-restricted conditional *Ppara* deletions in mouse retina have been published
[M]**, from the same group, with two different inducible Cre drivers:

| Model | Driver | Finding | Source |
|---|---|---|---|
| **Endothelial-specific** cKO, with a conditional transgenic gain-of-function arm | *Vecad-CreERT2* | Decreased postnatal retinal vascular density; enlarged avascular area and fewer endothelial progenitors in oxygen-induced retinopathy; in 6-month streptozotocin diabetes, **declined ERG amplitude, decreased retinal thickness on OCT, increased vascular leakage** vs floxed-uninduced littermates. Mechanism: endothelial mitochondrial dysfunction and senescence | *Am J Pathol* 2026;196(4):960-975, **PMID 41485550** |
| **Microglia-specific** cKO, with a conditional transgenic arm | *Cx3Cr1-CreERT2* | No baseline phenotype without diabetes; under diabetes, **decreased ERG response, exacerbated pericyte loss**, increased subretinal microglial migration, glycolytic shift, increased STING/TNFα. The gain-of-function arm **alleviated** the diabetic phenotype | *Cells* 2022;11(23):3869, **PMID 36497130** |

Both use tamoxifen-inducible Cre to avoid developmental confounds, and both include Cre-only
toxicity controls.

**Why this is decisive about circularity.** The global *Ppara* knockout carries
hypertriglyceridaemia, abolished ketogenesis and FGF21, hepatic steatosis and an altered
diabetes response, so "worse retinopathy" in that animal is fully explained by the competing
systemic hypothesis. **In both conditional models, hepatic PPARα is intact — and therefore so
are plasma triglycerides, ketogenesis and FGF21 production — and the worsened diabetic retinal
phenotype still appears [M].** The systemic confound is structurally absent rather than
statistically adjusted. Both papers state this exclusion as their explicit purpose.

Nobody has gone back and statistically corrected the original global-knockout retinopathy
papers for triglycerides, FGF21 or steatosis as covariates. That re-analysis is now largely
redundant for these two compartments, and a matched non-PPAR lipid-lowering comparator arm
remains the only place that idea appears.

### 6.1 What remains open, and the inversion that makes it matter

**No conditional deletion exists for RPE, Müller glia or photoreceptors [M].** So necessity is
established for the **two lowest-PPARA compartments** (endothelium 15.4%, microglia 15.5%) and
unaddressed for the **three highest** (rods 68.0%, RPE 64.8%, cones 54.5%). Findings
attributed to global-knockout photoreceptor or RPE phenotypes — including the
neuroprotection and mitochondrial-efficiency results in *PLoS One* 2019;14(2):e0208399
(**PMID 30716067**) — remain exactly as confounded as before.

**Neither conditional-knockout paper measures ANGPTL4** (checked by full-text search; zero
hits in either) **[M]**.

The resulting picture is the crux of this report: **local PPARα is necessary in precisely the
compartments where it is least abundant, where its pro-angiogenic sibling is more abundant,
and where no drug has been shown to arrive at a free concentration near its EC₅₀.**

---

## 7. LIMB 4 — LOCAL TRANSACTIVATION, NARROWED RATHER THAN EXCLUDED

Three separate arguments bear on whether an orally dosed fibrate can drive PPRE-dependent
gene expression in neural retina. Two have weakened and one has strengthened.

**Weakened — the exposure arithmetic.** The previous exclusion rested on a reasoned 10–100×
deficit against free EC₅₀, with no measured distribution value behind it. The one measured
value now available puts total fenofibric acid ~6× below the measured EC₅₀ in mouse retina +
vitreous after IP dosing (§4.2). That does not establish engagement — the route is wrong, the
compartment was pooled, and the free correction is missing on both sides — but it removes the
claim that the drug "never arrives."

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
reflected what has been *studied*, not the biology: six of the sixteen effectors have no
ChEMBL target at all, and the fatty-acid-oxidation genes are absent from the DR association
set entirely **[M]** — but a pathway nobody has investigated in a disease is indistinguishable,
in those datasets, from a pathway that is genuinely uninvolved. **No one has looked.**

Two of those rows are assay specifications in their own right. **HMGCS2 is RPE-specific**
(23.0% of cells, ≤0.1% everywhere else) and a direct PPARα target, which makes it the one
tractable local-transactivation readout in human eye. **FGF21 is flat zero in every retinal
cell type** (0.00–0.01% of 4.8M cells; 0.00 CPM across 523 retinas), so the humoral relay of
§5 is necessarily hepatic-to-retinal with no local-production escape hatch.

One nominal hint points the right way and does not survive multiple-testing correction:
*PDK4* falls in diabetic peripheral retina (log₂FC −0.62, p = 0.015) **[M, nominal]**,
consistent with reduced fatty-acid-oxidation signalling.

**Strengthened — the stoichiometric ceiling.** §3.4. In rods, PPARα exceeds its obligate RXR
partner by at least 6.4 to 1, which would cap transactivation independently of drug
concentration. Hypothesis, with a clean test.

**Net.** Limb 4 is marginal, not arithmetically excluded. It fails or succeeds on a free-drug
measurement that has never been made, and the measurement is the same one that decides
everything else.

---

## 8. CANDIDATE RANKING

**Read as a ranking of experimental priority, not of assets.** Several entries are deliberately
*instruments* — probes that measure whether a mechanism operates, and control arms that make a
result interpretable. A poor chronic drug can be the best available probe.

| # | Compound | Role | Measured PPARα / PPARδ / PPARγ (pChEMBL) | Basis |
|---|---|---|---|---|
| **1** | **Fenofibric acid** | **Lead** | **5.58** / — / 4.00 | Certain hepatic engagement; the only fibrate lowering apoB particle number; best drug-likeness in class; **and the only fibrate with a measured ocular tissue concentration** |
| 2 | Pemafibrate | Lead alternate | **9.00** / 5.80 / 5.96 | Sub-nanomolar, best renal safety — but its selectivity excludes the PPARδ-dominant compartments where DR pathology lives (§3.3), and its remnant claim has an unfavourable hard-endpoint read |
| 3 | Fenofibrate | Prodrug of #1 | 6.00 / — / 6.24 | Adds an esterase step and a food effect without adding pharmacology; **42× worse ocular distribution than the acid by the systemic route [C]** |
| 4 | Elafibranor | **Probe (12 wk)** | 8.00 / **8.00** / 6.76 | Highest plausible free concentration at retinal endothelium — but equal PPARδ potency makes it a **pro-angiogenic risk** in retinal vasculature, not a neutral dual agonist |
| 5 | Olezarsen | **Control** | — | Matched non-PPAR apoC-III suppression — the decisive discriminating arm |
| 6 | Inclisiran | **Falsification arm** | — | 3–5× the apoB effect of any fibrate; if apoB mass is the mechanism, it should work better |
| 7 | Candesartan | Comparator | — | Engagement certain at a luminal target; blocked by background therapy |
| 8 | Seladelpar | **PPARδ probe** | 5.82 / **8.72** / — | Reclassified. Functionally a PPARδ agonist, so it probes the dominant vascular isoform directly — and carries the matching angiogenic hazard |

All affinities **[M]**, from 5,271 / 3,223 / 7,913 validity-filtered activities on human PPARA
(CHEMBL239), PPARD (CHEMBL3979) and PPARG (CHEMBL235) — 62,219 measured activities in total
across the panel, 16,407 on the PPAR receptors.

**Bottom of the field:** quercetin, minocycline (its papilloedema risk attacks the very
endpoint being measured), epalrestat (excellent engagement of a *falsified* target), and the
dietary fatty acids (**not dose-movable**: plasma concentrations already sit at their own
EC₅₀).

### 8.1 Two measured corrections to the ranking's own logic

**The lead fails a conventional activity threshold at its own target [M].** Fenofibric acid's
best measured PPARα affinity is **pChEMBL 5.58 (≈2.6 µM)**, below the standard ≤1 µM cut that
fenofibrate (6.00), pemafibrate (9.00) and elafibranor (8.00) clear. This does not overturn
the ranking — it ranks on certainty of hepatic engagement, and hepatic portal concentrations
engage a micromolar EC₅₀ — but the margin is thinner than a first-place position implies.

**Potency does not buy engagement, measured.** Pemafibrate exceeds fenofibric acid by
**3.4 log units best-vs-best (≈2,600×) and 4.5 log units median-vs-median (≈30,000×) [M]**.
*Pemafibrate has only n = 3 measurements in ChEMBL, all EC₅₀; this is thin and should not be
over-read.* Against that, pemafibrate circulates at
roughly four orders lower free concentration, so its real margin is about **one** order better
**[C]**. Any ranking treating sub-nanomolar potency as decisive mis-ranks the set.

### 8.2 Target-coverage counts measure study volume, not pharmacology

A compound's count of hits against a disease gene panel, as reported by curated interaction
databases, is close to unrelated to measured binding. Quercetin illustrates it **[M]**:

| Quercetin | Value |
|---|---|
| Curated interaction count, 27-gene panel | **26 of 27** |
| ChEMBL genes bound at ≤1 µM, 43-gene panel | **3** (AKR1B1 7.83, MMP9 6.76, KDR 6.55) |
| PPARα effector genes bound at ≤1 µM | **0** |
| PPARG | 4.58 — ≈26 µM, not meaningful |

The pattern is general: of 153 compounds in the original coverage set, **15 bind any panel
gene at ≤1 µM and 3 bind any PPARα effector gene at ≤1 µM**; mean effector genes bound across
the 152 matched compounds is **0.046 [M]**. Catalogue size correlates with hit count at
**r = 0.911**, and a random set of 20 compounds covers ≥26 of those 27 genes with probability
**0.58**. Coverage counts measured how heavily a compound had been studied.

**One caution that must not be dropped:** a blank is not a zero. Absence of a ChEMBL activity
means *not measured in ChEMBL*, not *no interaction*.

---

## 9. STAGING

**Mild-to-moderate non-proliferative disease.** The exposure-robust limb — lowering systemic
lipoprotein supply — is mechanically inoperative before the barrier leaks, because with an
intact blood-retinal barrier there is no extravasation to prevent **[R]**. The right-stage
limb (local control in early disease) is the one the exposure arithmetic most constrains.
**The best-exposed mechanism acts at the wrong stage; the right-stage mechanism has the worst
exposure case.**

The conditional-knockout evidence of §6 sharpens this rather than softening it: both models
show **no baseline phenotype without diabetic stress** and a phenotype that emerges under it,
which is the signature of a mechanism operating during early injury rather than at steady
state **[M]**.

### 9.1 Enrichment is harder than it looks

The obvious enrichment marker — existing hard exudate — **selects patients in whom a
supply-lowering mechanism is weakest**, because an established deposit is self-renewing and
clearance-limited. The marker that finds the lipid phenotype also finds patients past the
point where the mechanism acts.

Enrich on the **rate**, not the deposit: elevated remnants despite statin therapy, and new or
worsening lesions over a prior interval, excluding organised subfoveal plaque.

---

## 10. THE WRONG-SIGN RISK

ANGPTL4 — a direct PPARα target gene and a potent pro-permeability factor in ischaemic retina
— is a bounded liability, and the measurements now locate it.

- **It is sited in the right compartment, which strengthens the concern.** ANGPTL4 in retina
  is a mural and endothelial transcript: pericytes 23.1%, smooth muscle 22.9%, endothelium
  12.0%, versus ~1% in photoreceptors **[M]**. That is exactly where a permeability risk would
  act.
- **And that compartment is PPARδ-dominant [M]**, so induction there would be driven by PPARδ
  engagement at least as much as by PPARα — which makes equal-potency dual agonists the
  specific hazard, not PPARα selectivity.
- **The two objections remain mutually destructive.** ANGPTL4 induction requires the same
  gene-activation machinery that the exposure argument constrains. If local engagement is too
  weak to help, it is too weak to harm — and §4.2 narrows both sides of that trade together.
- **A ceiling from already-measured data.** ANGPTL4 inhibits lipoprotein lipase, so meaningful
  induction predicts triglycerides to *rise*. Observed triglycerides *fall*. Real-world
  induction is bounded above by a quantity already in hand **[M]**.
- **The surviving path is systemic.** Hepatic engagement is certain, and fenofibrate and
  pemafibrate reliably raise circulating ANGPTL4 2–4× **[M]**, acting on endothelium from the
  luminal side. **Plasma ANGPTL4 is therefore a mandatory, cheap biomarker.**
- ANGPTL4 has **no ChEMBL target [M]** — it cannot be engaged directly by a small molecule, so
  biomarker is the only available role.

Among 2,652 DR gene-disease associations ANGPTL4 ranks 273rd with a **literature score of
0.776 — higher than PPARA's own [M]**. This is a genuinely active area, not a theoretical
worry.

**Intraocular ANGPTL4 stratified by fibrate exposure has never been measured, in any
species** — verified by systematic search across ten distinct query strings **[M]**. The
nearest adjacent result is an in-vitro study in which pemafibrate raised ANGPTL4 mRNA in a
human RPE cell line, but **less** than a non-selective PPARα agonist did (**PMID 39768065**);
that is evidence about the mechanism, not the measurement.

---

## 11. TWO OPEN MODULES

Both are tractable and neither has been attempted. They are stated here as specifications
rather than results.

### 11.1 Nothing in the candidate set accelerates lipid clearance

Every compound considered reduces what *arrives* in the retina. **Not one accelerates what
leaves.**

The lesion is a self-renewing cycle: modified lipoprotein → scavenger uptake → transporter
downregulated → cholesterol cannot leave → inflammasome activation and foam-cell death →
lipid re-released → re-uptake. **The deposit regenerates from its own debris.** Solving it as
a two-compartment system gives burden = influx ÷ clearance exactly — the recycling term
cancels. **But as clearance approaches zero the system has no steady state; it integrates.** A
supply-lowering agent then buys *delay*, not a bounded burden **[R, with one measured
anchor: ABCA1 is expressed in 53.4% of retinal microglia and 44.2% of RPE [M], so the efflux
machinery is present in the cells that would need it]**.

The fibrates do not cover this. Transporter induction is gene-activation driven — the limb
most constrained by local exposure — and it is a two-step relay, so *more* sensitive to that
shortfall, not less. **Retinal reverse cholesterol transport cannot be performed from the
liver.**

**One structural opening:** the PPARα pocket mandates a lipophilic acid; the LXR pocket does
not — its ligands are neutral. Ionisation is not structurally locked in for that target, so a
retina-penetrant modulator of the *efflux* arm is chemically conceivable in a way a
retina-penetrant PPARα agonist is not. The caveat is severe: systemic agonism of that target
has repeatedly failed on hepatic steatosis and hypertriglyceridaemia, so isoform selectivity
or tissue restriction is the entire problem, not a detail.

**What has not been done.** No candidate set has been assembled against the efflux axis
(NR1H2, NR1H3, ABCA1, ABCG1, APOA1, APOE, and the scavenger-uptake side CD36, OLR1, MSR1),
filtered on retinal-access physicochemistry, and assessed for the steatosis liability. **Until
that is done, the claim that the efflux arm is undruggable is an assumption, not a finding.**

**And the preference ordering may be backwards.** Adding a direct extracellular acceptor keeps
burden finite even at zero transporter activity, whereas a transporter inducer multiplies a
term that may already be near zero **[R]**. If that holds, an acceptor beats an inducer. It is
a two-parameter question — the extracellular-removal term and the clearance rate constant —
and both are measurable in a transporter-silenced explant.

### 11.2 The non-acidic PPARα ligand has not been built

The structural argument that it is possible is strong and stands.

The AF-2 cage is all-donor: Ser280, Tyr314, His440 and Tyr464 each donate a hydrogen bond, so
the ligand supplies only acceptors. The geometry demands a **bidentate acceptor pair roughly
2.2–3.2 Å apart — not a formal charge.** Charge is an acceptor-strength multiplier worth a
bounded **2.3–3.1 kcal/mol per contact [R, from the structural literature]**.

The existence proof is in hand: oleoylethanolamide is neutral, binds near 120 nM, and has
**ligand efficiency 0.41 — higher than fenofibric acid (0.29) or pemafibrate (0.34) [C]**. The
neutral head pays no efficiency penalty. The chemical space is empty because every PPARα
indication has been hepatic, where high protein binding and transporter uptake are *features*.
**Nobody ever needed a high-free-fraction PPARα ligand.** Unexplored, not forbidden.

**What has not been done.** No pharmacophore has been built from the donor-cage geometry; no
screen of the neutral and weakly acidic head-group window has been run
(1,2,4-oxadiazol-5(4H)-one, acylsulfonamide, hydroxyisoxazole, phosphine oxide,
phosphonamide — with tetrazole to be ruled out explicitly, since it raises pKa by only ~1.6,
has a larger footprint, and remains a full hepatic uptake transporter substrate); no scaffold
has been proposed with a predicted potency, logD, free fraction, retinal partition and
isoform-selectivity strategy against **both** PPARγ and PPARδ; and the efficacy asymmetry has
not been modelled. That last point is the one that could kill the idea cheaply: Tyr464 sits on
mobile helix 12 and pays for AF-2 closure, so it is lost first, and a neutral head should
produce a **partial agonist by construction, with efficacy degrading before affinity [R]**. A
partial agonist that cannot drive the transcriptional programme is not useful.

**The assay problem is the real blocker.** No cascade exists for optimising against free-drug
retinal exposure: free-drug-corrected EC₅₀, measured free fraction, and measured partition in a
species with a comparable barrier. Building that cascade is a prerequisite for the chemistry,
not a consequence of it. **Nothing should be built until the exposure measurement of §4 reads
positive.**

---

## 12. EXPERIMENTAL PROGRAMME

### 12.1 The critical-path unknown

> **Free fibrate concentration in human ocular tissue under oral dosing, and the receptor
> occupancy it implies.**

The practical route is **human aqueous humour from patients on chronic therapy at routine
cataract surgery** — not retinal interstitium, but it bounds the problem at negligible added
risk. **Pair it with aqueous ANGPTL4 in the same tap: two unknowns from one draw**, and the
ANGPTL4 half has been verified as unmeasured in any species.

The assay is not a barrier. Ocular LC-MS for fenofibrate and fenofibric acid has been built
and validated by three independent groups since 2019 **[M]**, with published detection limits
in the ng/g range in aqueous humour. What is missing is the human oral cohort, not the
capability.

### 12.2 The experiment that decides whether local engagement is achievable

**Chronic oral fibrate in a diabetic rodent, reading transactivation against transrepression**
— with paired ocular LC-MS on the same animals, so the pharmacodynamic readout is anchored to
a measured concentration rather than an assumed one.

| Readout class | Markers |
|---|---|
| Transactivation (gene-activation driven) | retinal CPT1A, ACOX1, **HMGCS2 in RPE specifically**, **ANGPTL4** |
| Transrepression (PPRE-independent) | retinal ICAM1, TNF, IL6; adherent-leukocyte count |

| Result | Conclusion |
|---|---|
| Transrepression ↓, transactivation flat | **Confirms a pharmacokinetically dissociated ligand** — anti-inflammatory action without gene induction, and therefore without the wrong-sign limb |
| Transactivation robustly ↑ | Low-occupancy model wrong; ANGPTL4 risk live |
| Both flat **with confirmed ocular drug concentration** | No achievable local engagement by this route |

Two arms are essential, and one of them is now cheaper than it was. A **receptor-knockout
arm** is available off the shelf for endothelium and microglia (the *Vecad-CreERT2* and
*Cx3Cr1-CreERT2* lines of §6), since fenofibrate has documented receptor-*independent* effects
and much supporting in-vitro work uses concentrations above where those appear. A **matched
non-PPAR lipid-lowering arm** remains to be run, and without it a positive cannot be
distinguished from "any lipid lowering would have done this." **Measure PPARδ alongside PPARα
throughout** — in microglia and the vasculature PPARδ is the more abundant receptor, so an
effect attributed to PPARα there is not safely attributable without the control.

### 12.3 The discriminator that needs no new experiment

**Does benefit track the lipid change?** A covariate analysis, answerable from data routinely
collected. **If benefit does not track the lipid change, the supply limb is in trouble and the
receptor hypothesis strengthens.** Costs nothing; discriminates directly.

### 12.4 The necessity question, rescoped

Conditional deletion is **complete for endothelium and microglia** and both read positive.
What remains is **RPE-, photoreceptor- and Müller-glia-specific deletion** — the three
compartments with the highest PPARα expression, where every existing retinal phenotype still
comes from the confounded global knockout. This is a rescoped item, not a from-scratch one.

### 12.5 Sequenced

| # | Experiment | Cost | Time | Decides |
|---|---|---|---|---|
| 1 | Lipid-change covariate analysis | ~$0 | weeks | Supply limb vs local limbs. **Free — run first** |
| 2 | **Validated PPARα immunostain on human donor retina**, per cell type, with knockout or peptide-competition controls | ~$15–30k | 2–3 mo | The only surviving part of the antibody/transcript conflict. **No such stain exists; cheapest decisive item in this programme** |
| 3 | Human aqueous drug + ANGPTL4 at cataract surgery | $50–100k | 6–12 mo | **The critical-path unknown**, and the wrong-sign question |
| 4 | Rodent transactivation vs transrepression, with paired ocular LC-MS, the off-the-shelf knockout arms, a non-PPAR lipid arm, and PPARδ controls | $150–250k | 6–9 mo | Whether local engagement is achievable |
| 5 | ApoA1-mimetic explant, transporter silenced | ~$75k | 6 mo | Whether the clearance module is addressable; acceptor vs inducer |
| 6 | Lipid clearance rate constant | ~$75k | 6 mo | Whether benefit is bounded or merely delayed |
| 7 | RPE / photoreceptor-specific conditional deletion | $150–300k | 18–24 mo | Necessity in the high-expression compartments |

**Items 1–6: roughly $370–530k over 12–18 months.**

### 12.6 Cheap data acquisitions that would move several answers at once

- **A second diabetic human retina cohort.** GSE160306 is the only public human neural-retina
  series with a diabetic axis, and nothing in a 95-gene panel survives FDR in it. A ≤26%
  reduction in *PPARA* remains possible.
- **A single-cell atlas of diabetic human neural retina.** None exists — 13,075,889 human eye
  cells are available and zero are diabetic; every public diabetic eye single-cell dataset
  profiles fibrovascular membranes or blood **[M]**.
- **Single-cell confirmation of retinal KLB** across the 24 retina datasets. The co-receptor
  finding of §5.3 currently rests on one consortium's bulk and single-cell arms.
- **An FGF21 concentration-response on retinal endothelial cells below 50 ng/mL**, which has
  never been run. If protection persists at ~205 pg/mL FGF21-equivalent, the §5 verdict is
  wrong and should be withdrawn.
- **Whether PPARG's DR genetic association is DR-specific or propagated from parent diabetes
  terms.** One query; it bears on whether the wrong isoform has been the target all along.
- **Protein-level PPARα:RXR stoichiometry in donor retina** (co-IP or proximity ligation),
  before §3.4's transcript-ratio hypothesis propagates as a finding.

### 12.7 Observation windows must be justified against clearance, not calendar

A **stock** readout (lesion burden) has time constant 1 ÷ clearance — the parameter this
disease suppresses. A **flux** readout (lesion turnover) responds directly. **A stock measure
can read flat at twelve months while the mechanism is working.** Flux primary; stock secondary,
with a window justified against the measured clearance rate.

### 12.8 Kill criteria

- Rodent study flat on both readouts **with confirmed ocular drug concentration** → no
  achievable local engagement by oral dosing
- Matched non-PPAR lipid arm reproduces the effect → the receptor is not the agent of action
- Receptor knockout fails to abolish the effect → not receptor-mediated
- Benefit tracks lipid change tightly → a lipoprotein hypothesis; far more potent apoB-lowering
  agents exist than any fibrate
- Robust local transactivation with ANGPTL4 induction → wrong-sign limb live; re-derive
  risk-benefit by stage before any chronic exposure
- Validated immunostain shows PPARα protein absent from endothelium and microglia → the
  conditional-knockout phenotypes require a non-cell-autonomous explanation and the local
  hypothesis needs rebuilding

### 12.9 Combination work stays deferred

The limb question determines which component a combination needs, so building one first yields
an uninterpretable result. **Two bench measurements replace it (~$100–150k):** the
extracellular-removal term in a transporter-silenced explant, and the clearance rate constant.

The strongest combination concept is oral supply-lowering plus a **locally delivered
ApoA1-mimetic acceptor** at an injection visit these patients already attend — for which the
barrier-penetration problem does not apply at all.

**Ruled out:** any supply agent plus scavenger-receptor blockade is **wrong-signed** —
macrophage uptake is the only catabolic route for retained lipoprotein in retina, so blocking
it converts dying foam cells into extracellular deposits nothing removes.

---

## 13. CONCLUSIONS

1. **The fibrate class is the correct nomination for mild-to-moderate non-proliferative
   disease.** The staging conclusion is the most robust claim in this report and nothing
   measured since has disturbed it.

2. **The live mechanism is local, cell-autonomous PPARα in retinal endothelium and
   microglia.** Two conditional knockouts establish necessity with the systemic confound
   structurally absent. This is the strongest evidence in the file and it did not come from
   reasoning about the target.

3. **The FGF21 relay is closed, and it failed.** A 25× concentration shortfall (CI 6–99×), a
   10³–10⁴× native-hormone dose that did nothing, a missing co-receptor in human retina, and
   the wrong epidemiological sign in 9,697 patients. The route that survives runs through
   adipose and adiponectin, and its human fibrate leg has never been quantified.

4. **The restore-a-deficit framing is dead.** Retinal *PPARA* is not reduced in diabetes, with
   the null bounded by power. Any effect must be supraphysiological activation of a normally
   expressed receptor.

5. **Isoform selectivity is a targeting constraint, not a safety preference.** PPARδ dominates
   every vascular and immune compartment of human retina. The receptor is necessary where it
   is least abundant.

6. **Retinal exposure is no longer unmeasured, but the measurement that matters is still
   missing.** One rodent value by the wrong route puts total fenofibric acid ~6× below its
   measured EC₅₀. No oral, free, or human number exists anywhere.

7. **Potency is nearly orthogonal to engagement in this series, measured.** The most potent
   agent is not the best probe, and the lead compound sits below a conventional activity
   threshold at its own target.

8. **Two modules remain genuinely unexamined** — a drugged lipid-efflux arm, and a non-acidic
   high-free-fraction PPARα ligand. Both are tractable. Neither should be pursued before
   item 3 of §12.5 reads out.

9. **What still separates this target from a decision is one draw of aqueous humour.** The
   difference from a year ago is that the surrounding questions have been answered, so that
   draw now decides a specific, narrow thing rather than everything at once.

---

## APPENDIX — SUPPORTING MATERIAL

### Primary data generated for this report

| Path | Contents |
|---|---|
| `data/processed/retina_sc_celltype_summary.tsv` | Per-cell-type detection, 4.8M cells, 24 datasets |
| `data/processed/retina_sc_gene_presence.tsv` | Feature-presence matrix — absent vs below threshold |
| `data/processed/retina_sc_depth_dropout.tsv` | Sequencing-depth dropout deciles |
| `data/processed/retina_bulk_dr_expression.tsv` | GSE160306 diabetic contrast with power bounds |
| `data/processed/retina_eyegex_abundance.tsv` | GSE115828, 523-retina abundance reference |
| `data/processed/retina_hpa_bulk_ntpm.tsv`, `retina_hpa_celltype_ncpm.tsv` | Independent pipeline, plus KLB / FGFR1 / ADIPOR1 |
| `data/processed/chembl_panel_bioactivities.csv` | 62,219 measured activities; 16,407 on the PPAR receptors |
| `data/processed/dr_compound_target_matrix.tsv` | 38,818 compounds × 43 genes, pChEMBL-gated |
| `data/processed/dr_gene_panel.csv` | 43 genes, each annotated with the limb it discriminates |
| `data/processed/opentargets__DR_gene_disease.csv` | 2,652 DR gene-disease associations |

Analysis code: `src/analysis/retina_expression/`, `src/analysis/fgf21_bridge/`,
`src/analysis/dr_matrix/`. Collection code: `src/scrapers/chembl/chembl_target_axis.py`,
`src/scrapers/opentargets/`.

⚠ `opentargets__*` files carry `score_known_drug` and `score_clinical` columns that encode
approved-indication and trial evidence. **Drop both before any blinded re-run.**

### Detailed records

| Document | Contents |
|---|---|
| `docs/notes/ppara-retinal-expression.md` | Full per-cell-type tables, atlas accessions, dropout analysis |
| `docs/notes/fgf21-concentration-bridge.md` | Both FGF21 datasets, the Monte-Carlo model, the co-receptor result |
| `docs/notes/dr-evidence-absence-audit.md` | The conditional knockouts, the ocular PK literature, full query logs |
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

⚠ `agents/UNBLINDING-part-b.md` contains a held-out answer key. Do not read it, or expose it
to any agent, when re-running the benchmark.

**Research disclaimer.** This is a computational and literature-based analysis. Nothing here
is a clinical recommendation. All findings require experimental validation.
