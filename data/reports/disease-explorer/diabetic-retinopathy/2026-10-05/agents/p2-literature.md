# Literature Review — Diabetic Retinopathy Candidate Set (BLINDED RUN, Phase 2)
Agent: Literature Reviewer · 2026-10-05
Role in this run: **the benchmark's unblinding checkpoint.**

> **STRUCTURAL NOTE — READ BEFORE USING THIS FILE.**
> This report has two parts that must never be merged.
> **Part A** is a fully blinded evidence appraisal. It uses no DR/DME clinical-trial or
> indication evidence. **Every score in the SCOREBLOCK is derived from Part A alone.**
> **Part B** is the post-hoc unblinding. It is the answer key as seen from the literature
> side. It is excluded from scoring and did not influence Part A.
> **Write-order attestation:** Part A was written to this file and committed to disk in a
> single operation *before* the agent issued any DR-specific literature search. Part B was
> appended afterwards. Part A was not edited after Part B was written.

---
---

# PART A — BLINDED EVIDENCE REVIEW

## A0. Scope, method, and what "evidence" means here

I applied the project's standard evidence hierarchy (SKILL.md), adapted to DR:

| Level | Type | Weight |
|---|---|---|
| 1a / 1b | Meta-analysis of RCTs / individual RCT | Highest |
| 2a / 2b | SR of cohorts / individual cohort, human PD study | High / Mod-High |
| 3 | Case-control, case series | Moderate |
| 4 | Preclinical animal model | Low-Moderate |
| 5 | In vitro / cell culture / receptor pharmacology | Low |
| 6 | Computational / in silico / structural inference | Lowest |
| 7 | Traditional use | Context-dependent |

**Two adaptations I made, and why.**

1. **I added a cross-cutting axis the standard hierarchy does not capture: *mechanism-class
   translational record*.** A Level-5 mechanistic claim whose entire drug class has failed
   repeatedly in humans is weaker than its level implies. A Level-4 claim in a mechanism class
   with human validation elsewhere is stronger than its level implies. This axis does most of
   the discriminating work in §A5 and it is the single most useful thing I can add to Round 1,
   because Round 1 reasoned almost entirely from *mechanism plausibility* and almost not at all
   from *mechanism track record*.

2. **I graded *reproducibility by independent laboratory* explicitly**, because the central
   pillar of the retina-intrinsic PPARα case turns out to be concentrated in a small number of
   groups (§A1.4). Round 1 did not weight this and it changes the grade.

**Blinding discipline applied in Part A.** Permitted and used: PPARα receptor pharmacology;
retinal lipid biology; preclinical PPARα-in-retina literature (knockouts, retina-targeted
expression, cell culture) as *mechanism*; human genetics; non-DR clinical evidence for every
candidate; comparator-mechanism evidence. Excluded and not used: any DR/DME trial, indication,
guideline, or regulatory fact for any candidate. Where the blinded brief itself already states
a DR fact (brief §4 names aldose-reductase and PKCβ inhibition as failed human DR mechanisms),
I used it **only at the level of abstraction the brief supplies** — "the mechanism class failed"
— and pushed all trial names, populations and effect sizes into Part B. Two borderline calls
are disclosed in §A8.

---

## A1. (a) THE MECHANISTIC EVIDENCE FOR PPARα IN RETINA — how strong is it really?

### A1.1 The claim being appraised

> Retinal PPARα is protective; its diabetes-associated downregulation is pathogenic; restoring
> or activating it in retina prevents DR lesions.

This is three claims, and they have different evidence grades. Round 1 and the Phase 0 scout
treated them as one.

### A1.2 Evidence table — retina-intrinsic PPARα

**SUPPORTING**

| Lvl | Type | Finding | Quality | Independent replication |
|---|---|---|---|---|
| 4 | Animal, global KO | `Ppara-/-` mice made diabetic develop worse retinal vascular lesions — more acellular capillaries, pericyte loss, leukostasis, permeability — than diabetic WT | **Moderate design, low inferential value** (see A1.3) | Reported by ≥2 groups; dominated by one |
| 4 | Animal, gain-of-function | Retina-targeted PPARα expression (AAV, intravitreal/subretinal) reduces vascular leakage, acellular capillaries, VEGF and ICAM-1 in diabetic and oxygen-induced-retinopathy models | **Moderate** | **Limited** — heavily concentrated in one laboratory lineage |
| 4 | Animal, pharmacological | Systemic or intravitreal PPARα agonist reduces retinal leukostasis, VEGF, permeability, pericyte loss in rodent diabetes | Moderate, but confounded (A1.5) | Multiple groups |
| 4/5 | Expression | PPARα mRNA/protein reported reduced in diabetic rodent retina and in human diabetic donor retina | **Low-moderate** — antibody-based, small donor n, post-mortem interval uncontrolled; conflicts with scRNA-seq showing low baseline retinal PPARA (Target Analyst §1.1) | Partial |
| 5 | Cell culture | PPARα agonists reduce VEGF, ICAM-1, NF-κB activity, apoptosis in human retinal endothelial cells, RPE and Müller cells | **Low, and frequently invalid as receptor evidence** (A1.5) | Many groups |
| 5/6 | Pathway | PPARα → AMPK/SIRT1/PGC-1α, Wnt/β-catenin inhibition, ceramide and sphingolipid control, FAO gene induction | Low — mostly correlative, few rescue/epistasis experiments | Mixed |
| 2b | Human genetics | *PPARA* polymorphism association with DR in candidate-gene studies | **Low.** Small, ethnically heterogeneous, inconsistent direction, no GWAS-scale support, no replication meeting modern genetic standards. **Does not constitute human genetic validation.** | Poor |

**CONTRADICTING / WEAKENING**

| Lvl | Type | Finding | Quality |
|---|---|---|---|
| 5 | Expression | Single-cell transcriptomic surveys place retinal *PPARA* at low abundance relative to *PPARD*, in most retinal cell types | Moderate — caps achievable signal amplitude regardless of occupancy |
| 5 | Pharmacology | Much in vitro "PPARα agonist" retinal work uses fenofibrate at 25–100 µM — **above the concentration at which fenofibrate exerts documented PPARα-independent effects** (direct NF-κB interference, AMPK activation, mitochondrial uncoupling, ER-stress induction). Without a `Ppara-/-` or GW6471 arm these experiments do not establish receptor mediation | **This invalidates a large fraction of the Level-5 supporting column** |
| 4 | Design | Global-KO phenotype is fully explicable by the knockout's systemic metabolic derangement (A1.3) | High-confidence methodological objection |
| — | Field-level | A target reported to improve essentially every measured retinal readout — vascular, neural, glial, inflammatory, metabolic — across model systems is a pattern more characteristic of publication bias and non-specific drug effects than of a single dominant node | Prior, not evidence, but a strong one |

### A1.3 The global-knockout arm contributes almost nothing — and this is the key appraisal

I agree with the Target Analyst and I will put it more strongly. **`Ppara-/-` + diabetes → worse
retinopathy is not evidence for a retina-intrinsic mechanism at all.** It is evidence that
PPARα is protective *somewhere in the organism*.

The confound is not hypothetical and not small. Global `Ppara-/-` mice carry:
hypertriglyceridemia, elevated circulating NEFA, abolished fasting ketogenesis, hepatic
steatosis, impaired fasting response, altered glucose/insulin handling, altered systemic
inflammatory tone, **and abolished FGF21 induction**. Every one of these is an independent
route to worse experimental retinopathy. Worse, several of them alter the response to
streptozotocin itself, so the knockout and WT arms are not receiving an equivalent diabetic
insult.

**This is exactly the mechanism Round 1 calls the *competing* hypothesis.** The knockout result
is therefore equally consistent with — arguably more consistent with — the systemic-lipid limb.
Citing it as support for the retinal limb is a circularity that has propagated through the
secondary literature and into this run's brief (§7 counter-consideration).

**Grade for the knockout arm as retina-intrinsic evidence: Level 4, quality LOW. It should carry
near-zero weight for the retinal limb and non-trivial weight for the systemic limb.**

### A1.4 The gain-of-function arm is the real pillar — and it is thinner than it looks

Retina-targeted PPARα expression being protective is the best retina-intrinsic evidence that
exists, and it is genuinely informative: it shows PPARα is **sufficient** in retinal tissue.

Four discounts:

1. **Sufficiency ≠ necessity.** Overexpression rescue on a WT background is a gain-of-function
   experiment. The necessity experiment — cell-type-restricted conditional *Ppara* deletion
   (floxed × Müller / endothelial / RPE Cre) — **has not been reported.** Its absence is
   conspicuous after ~15 years of interest in this target. Absence of evidence is not evidence
   of absence, but after this long it begins to be informative.
2. **Supraphysiological levels.** AAV overexpression routinely achieves receptor levels far
   above endogenous. A receptor present at low endogenous abundance (A1.2, contradicting row)
   that rescues when driven to high abundance tells you about the *pathway's* capacity, not
   about whether the endogenous receptor governs the phenotype. **And it is precisely the wrong
   model for a drug that will achieve, at best, partial occupancy of a low-abundance pool.**
3. **Laboratory concentration.** The retina-targeted-expression finding and the
   diabetes-downregulation finding derive substantially from one research lineage. This is not
   an accusation of error — it is a standard reproducibility discount, and it is the discount
   Round 1 omitted. Independent replication of the *conditional* result by an unaffiliated group
   would raise this grade materially.
4. **Delivery is not inert.** Intravitreal/subretinal AAV causes its own inflammatory and
   gliotic response; the comparison is to AAV-control, which controls for this only partially.

**Grade for the gain-of-function arm: Level 4, quality MODERATE.**

### A1.5 Overall grade for "PPARα in retina"

> **Level 4 (preclinical animal), quality MODERATE, with a documented reproducibility
> concentration and one decisive experiment missing. There is no human genetic validation and
> no Level 1–3 mechanistic evidence of any kind.**

Stated plainly: **the retina-intrinsic PPARα case is a normal, respectable preclinical
hypothesis. It is not an unusually strong one, and the brief's framing ("conditional genetic
evidence supports a retina-intrinsic component") overstates it by about one grade.** The
Target Analyst reached "moderate, not strong" and I concur, arriving independently and by a
different route — the receptor-mediation failure in the in vitro column (A1.2) is an additional
discount they did not apply.

**What would change this grade:** a cell-type-restricted conditional *Ppara* deletion from an
independent group, with a retinal phenotype, on a background with normal systemic lipids.
That single experiment is worth more than the entire existing preclinical corpus.

---

## A2. (b) THE THREE COMPETING LIMBS — which has the best evidence *as mechanism*?

### Limb (i) — hepatic/systemic apoB and remnant lowering, with humoral relay to retina

**This is the only limb with human-level mechanistic evidence, and it is not close.**

| Step in the causal chain | Best evidence | Level | Grade |
|---|---|---|---|
| Oral fibrate engages hepatic PPARα | OATP1B1/1B3-mediated hepatic uptake; hepatic transcriptional response measured in human liver and in human PD | 2b | **Certain** |
| → lowers apoC-III, raises LPL, lowers TG-rich remnants, lowers apoB particle number | Large human PD/lipid-endpoint literature, decades, many independent studies, dose-responsive | **1b–2a** | **Certain** |
| → raises FGF21 | *Fgf21* is a canonical direct PPARα target (PPRE-driven, abolished in `Ppara-/-`); **fibrate administration raises circulating FGF21 in humans** | 2b (human PD) + 4/5 (mechanism) | **Strong** |
| Circulating FGF21 acts on retinal vasculature via FGFR1c/β-Klotho from the luminal side | Recombinant FGF21 suppresses pathological retinal and choroidal neovascularization and protects retinal neurons/vasculature in rodent models, partly adiponectin-dependent — **from laboratories entirely independent of the PPARα-retina lineage** | 4 | **Moderate, and independently replicated** |
| Lower circulating modified-apoB supply → less intraretinal lipoprotein retention | Mechanistic: hard exudate composition is retained, modified apoB lipoprotein; glycated/oxidised LDL is cytotoxic to pericytes and retinal endothelium and to RPE in culture | 4/5 + human observational association of serum lipids with retinal hard exudate | **Moderate** |

**Why this limb wins the evidence contest.** Its weak link (apoB supply → retinal lesion) is
*shared* with every other lipid-lowering candidate and is the one genuinely uncertain step.
Every step before it is human-validated. The retinal limbs, by contrast, have an uncertain step
at *every* position in the chain: uncertain occupancy × uncertain receptor abundance × uncertain
transrepression threshold × uncertain downstream amplitude. Uncertainty multiplies.

**The FGF21 relay deserves more weight than Round 1's synthesis gave it, and I want to be
emphatic about why.** It is the only proposed mechanism in this entire run where:
- the upstream pharmacology is human-proven (fibrate → ↑plasma FGF21),
- the downstream retinal biology is animal-proven *by independent laboratories with no stake in
  the PPARα-retina hypothesis*,
- and **no barrier crossing by the drug is required at any point.**

A two-step chain with independent evidence at each end is epistemically stronger than a
one-step chain with weak evidence, even though it is longer. Round 1 noticed FGF21 (Target
Analyst §2) but filed it as a bonus row; on evidence grounds it is arguably the **primary**
retinal mechanism of systemic PPARα agonism, not an adjunct.

**Grade for limb (i): Level 2b human PD for the proximal chain, Level 4 independently
replicated for the retinal terminus. Overall MODERATE-HIGH — the strongest limb in the run.**

### Limb (ii) — endothelial/RPE PPARα transrepression of NF-κB at low occupancy

Graded in full in §A3. **Summary: Level 5/6, quality LOW.** It is a reasoned extrapolation, not
a measurement, and the mechanism class it extrapolates from has a bad translational record.

### Limb (iii) — retinal transactivation of fatty-acid-oxidation genes

| Lvl | Finding | Quality |
|---|---|---|
| 5 | PPARα-driven FAO programme (CPT1A, ACOX1, HMGCS2) is well characterised **in liver, heart, muscle** | High — but in the wrong tissue |
| 4 | Retinal energy metabolism uses FAO substantially; photoreceptors and RPE oxidise fatty acids; RPE β-oxidation supports photoreceptor ketone supply | **Moderate and genuinely interesting** — the tissue biology is real |
| — | **That oral fibrate dosing measurably induces retinal CPT1A/ACOX1/HMGCS2 in vivo** | **I could find no clean demonstration of this.** This is a measurement that should exist and apparently does not |
| 5 | Low retinal PPARA abundance caps amplitude independently of occupancy | Moderate |

**Grade: Level 4/5, quality LOW for the drug-driven version.** The underlying retinal FAO
biology is solid; the claim that a systemically dosed fibrate drives it is unsupported by
direct measurement and is the claim the exposure arithmetic attacks most effectively.

### A2.4 Verdict on (b)

> **Ranked by evidence quality as mechanism: (i) hepatic/systemic + FGF21 relay ≫ (iii) retinal
> FAO transactivation ≳ (ii) retinal transrepression.**

Note that this **inverts Round 1's ordering of the two retinal limbs.** Round 1 concluded
transrepression is "the surviving retinal limb" and transactivation "probably does not occur."
On *evidence* grounds the ordering is the other way round: the FAO limb at least rests on
well-characterised receptor biology in other tissues plus real retinal FAO physiology, whereas
transrepression at low occupancy rests on an unmeasured inter-receptor extrapolation (§A3).

This is not a contradiction of Round 1 — Round 1 ranked by *probability of occurring given the
exposure arithmetic*, which is a different question. But the pipeline should not conflate
"the limb most likely to survive the PK objection" with "the limb best supported by published
evidence." **They are different limbs, and the report should say so.**

---

## A3. (c) THE TRANSREPRESSION-AT-LOWER-OCCUPANCY CLAIM — graded

This is Round 1's most load-bearing novel claim, so it gets the most scrutiny.

### A3.1 What is actually published

**For glucocorticoid receptor — the source of the principle**

| Lvl | Finding | Quality |
|---|---|---|
| 5 | Dissociated GR ligands (RU-24858, ZK216348, Compound A and successors) separate transrepression from transactivation in reporter and cell systems; dose-response curves for NF-κB/AP-1 suppression lie left of those for GRE-driven transactivation, by roughly 10–100× in several systems | **Moderate in vitro; this is the real empirical basis of the claim** |
| 4 | `GRdim` mice (dimerisation-deficient) retain anti-inflammatory function with reduced transactivation | **Downgraded by later work:** GRdim was subsequently shown to retain substantial transactivation capacity and to be a leakier separation than originally believed. The canonical mouse genetic support for dissociation is **weaker now than when the field was founded.** |
| **1b** | **Translational record: after ~25–30 years and multiple clinical-stage compounds, no dissociated glucocorticoid has reached approval. In vivo, the therapeutic-index separation repeatedly proved far smaller than in vitro dose-response separation predicted.** | **HIGH-QUALITY NEGATIVE EVIDENCE, and the most important row in this table** |

**For PPARα specifically**

| Lvl | Finding | Quality |
|---|---|---|
| 5 | PPARα ligand-dependently antagonises NF-κB and AP-1 signalling; physical interaction with p65 and c-Jun; induction of IκBα; suppression of IL-6, COX-2, VCAM-1, CRP in vascular cells | Moderate — well replicated **qualitatively** |
| 5 | SUMOylation-dependent, NCoR-stabilising transrepression — the "non-consumed receptor / sub-stoichiometric" mechanism Round 1 leans on | **This mechanism was established principally for PPARγ (and LXR) in macrophages. Its extension to PPARα is by analogy, with thinner direct support.** Round 1 imported it without flagging the receptor substitution |
| 5 | Reported dose-response separation between NF-κB-target suppression and PPRE-target induction for PPARα | **Low — sparse, system-dependent, and critically: usually not corrected for the µM-range PPARα-independent effects of the test compounds** |
| **—** | **A quantified occupancy differential for PPARα — fractional occupancy required for half-maximal transrepression vs half-maximal transactivation, in any tissue** | **NOT PUBLISHED, as far as I can establish. The number Round 1 needs does not exist.** |
| — | The same number for retinal endothelium or RPE | Not published; not plausibly measurable with current reagents |

### A3.2 The three objections that most weaken the claim

**1. The confound that invalidates much of the supporting in vitro column.** Fenofibrate,
fenofibric acid, Wy-14643 and gemfibrozil all exert documented **PPARα-independent**
anti-inflammatory effects at the tens-of-µM concentrations used in most of these experiments.
An NF-κB-suppression dose-response curve generated at 10–100 µM fenofibrate without a
`Ppara-/-` cell or GW6471 reversal arm cannot distinguish receptor-mediated transrepression
from direct off-target NF-κB interference. **A large share of the "PPARα transrepresses at low
concentration" literature has this defect.** This is a methodological point Round 1 did not
make and it bites hard, because the *direction* of the bias is to make transrepression look
more potent and more left-shifted than it is.

**2. The receptor substitution.** The strongest mechanistic account of sub-stoichiometric,
non-consumed transrepression (SUMO → NCoR clearance block) is a PPARγ/LXR macrophage result.
Round 1's argument 2 ("catalytic character") therefore rests on a cross-isoform transfer — in a
run whose own brief (§4) explicitly mandates **isoform discipline** and forbids transferring
properties between PPAR isoforms. Round 1 applied that discipline to liabilities (PPARγ fluid
retention) and then, in the opposite direction, imported a PPARγ mechanism as a benefit.
**That asymmetry should be corrected.**

**3. The translational record is the decisive discount.** The dissociated-ligand principle has
been the explicit design hypothesis of a well-funded, 25-year, multi-company effort in the
glucocorticoid field, and it has produced **zero approved drugs**. The repeated finding was that
in vitro dose-response separation did not reproduce as in vivo therapeutic-index separation.
Round 1 cited the field's existence as *support* ("the entire basis of a drug-design field").
**The existence of a field is not evidence that its founding assumption translates; in this case
the field's outcome is evidence that it does not, at least not reliably.** This is the single
largest correction I am making to Round 1.

### A3.3 What survives

Round 1's argument 4 — the **nonlinear ICAM-1-density threshold for firm leukocyte adhesion
under shear** — is the one sub-argument I think is *strengthened* by closer reading. It does not
depend on the occupancy differential at all. It is a claim about downstream signal
amplification: a modest fractional reduction in endothelial ICAM-1 surface density can produce a
disproportionately larger reduction in firm adhesion, because adhesion under shear requires
multivalent bonding above a density threshold. That is supported by independent cell-adhesion
biophysics and leukocyte-rolling literature (Level 5, moderate quality) and it is mechanism-
agnostic — it applies to any intervention that lowers ICAM-1 a little.

So the salvageable version of Round 1 §6 is narrower and better:

> Not "transrepression needs 1–2 log less occupancy" (unmeasured, cross-receptor, with a bad
> class record), but **"the leukostasis endpoint amplifies small reductions in ICAM-1, so a weak
> retinal anti-inflammatory effect could still be phenotypically visible."** That is a defensible
> Level-5 claim. The occupancy-differential version is not.

### A3.4 Grade

> **The transrepression-at-lower-occupancy claim as stated: Level 5/6, quality LOW, with
> high-quality negative class-translational evidence against it. It should be reported as a
> hypothesis-generating consideration, not as the limb that rescues the retinal case.**
>
> **The ICAM-1 threshold-amplification sub-argument: Level 5, quality MODERATE. Keep it.**

Round 1 scored the transrepression limb as "marginal but NOT excludable." I would restate that
as **"not excludable, and also not supported — the correct status is unknown, and the prior from
the mechanism class is unfavourable."** The difference matters for how the pipeline's final
recommendation is worded.

---

## A4. (d) ANGPTL4 IN RETINA

### A4.1 Evidence that ANGPTL4 matters in retinal disease

| Lvl | Finding | Quality |
|---|---|---|
| 3 | ANGPTL4 is markedly elevated in aqueous humour and vitreous of patients with proliferative diabetic retinopathy and with diabetic macular edema, relative to non-diabetic controls | **MODERATE-HIGH. This is human tissue-level evidence, and it is the strongest human data point anywhere in this analysis.** Case-control design; confounded by disease severity and by vitrectomy indication |
| 5 | Recombinant ANGPTL4 increases retinal endothelial permeability and promotes angiogenesis in vitro; neutralising ANGPTL4 reduces permeability and neovascularization | Moderate; replicated |
| 4 | ANGPTL4 blockade reduces retinal neovascularization in animal models, **additively with VEGF blockade** — i.e. it is a genuinely VEGF-independent limb | Moderate; this is the finding that makes it interesting rather than redundant |
| 5 | In ischemic retina, ANGPTL4 induction is **HIF-1α-driven via hypoxia-response elements**; it behaves as a canonical hypoxia-inducible gene in this tissue | **MODERATE-HIGH, and this is the crux of the regulation question** |

### A4.2 HIF versus PPRE — the regulation question, answered as far as the literature allows

ANGPTL4 (originally FIAF/PGAR) carries **both** a functional PPRE — it is a canonical PPARα and
PPARγ target in liver and adipose, fasting-induced, abolished in `Ppara-/-` liver — **and**
functional hypoxia-response elements.

The evidence says these dominate in **different tissues and different conditions**:

- **Liver / adipose, nutritional and pharmacological PPAR activation:** PPRE-dominant. Not in
  dispute.
- **Ischemic retina, the disease-relevant condition:** **HIF-dominant.** The published retinal
  ANGPTL4 induction in PDR tracks hypoxia and HIF-1α stabilisation, not lipid or PPAR status.

**Implication, and it cuts in the wrong-sign hypothesis's favour.** The retinal ANGPTL4 that is
actually elevated in proliferative disease is being driven by a transcriptional input that a
PPARα agonist does not supply and, in a low-occupancy retina, could not meaningfully add to.
This is an *independent* reason to demote the wrong-sign risk — different from, and additional
to, the Target Analyst's "same-machinery" argument. Two independent arguments reaching the same
demotion is a stronger position than Round 1 recorded.

### A4.3 Does systemic PPARα agonism raise *intraocular* ANGPTL4?

> **No published measurement. This is a genuine void in the literature, not a gap in my search.**

What is published:
- Fibrate treatment raises **circulating/plasma** ANGPTL4 in humans — consistent with hepatic
  PPRE-driven induction, and directionally what the hepatic-engagement-is-certain model predicts.
  Level 2b, **moderate confidence; I flag this one as the claim in Part A I am least certain of
  at the level of specific numbers.**
- Aqueous/vitreous ANGPTL4 has been measured in diabetic patients (A4.1 row 1), but **not
  stratified by fibrate exposure.** The samples to do this almost certainly already exist in
  vitrectomy biobanks.

**Answering the Target Analyst's direct question to me:** no, there is no human measurement of
intraocular ANGPTL4 in fibrate-exposed versus unexposed diabetic patients. It is a cheap,
sample-available study and it would settle their §3 empirically. **I endorse it as the single
highest-value clinical-sample experiment the programme could commission.**

### A4.4 One more argument against the wrong-sign risk that nobody in Round 1 made

ANGPTL4 is a **physiological inhibitor of lipoprotein lipase.** If systemic PPARα agonism
induced ANGPTL4 to a functionally large degree, the predicted net effect on plasma triglycerides
would be **upward**. The observed human effect of fibrates is a large, reliable **downward**
movement in triglycerides. Therefore the ANGPTL4 induction achieved at human-tolerated fibrate
exposure must be **functionally subordinate** to the concurrent LPL induction and apoC-III
suppression — the lipolytic arm wins by a wide margin in the compartment where engagement is
certain.

This is a clean internal-consistency argument from well-established human pharmacology: **the
magnitude of real-world ANGPTL4 induction is bounded above by the observed TG-lowering.** It
does not eliminate a local vascular effect, but it caps the plausible size of the systemic one.

**Overall ANGPTL4 verdict (Part A): the human tissue evidence that ANGPTL4 matters in PDR is the
best human mechanistic evidence in this entire candidate set — but it is evidence about the
*disease*, not about the *drug*. The evidence that a PPARα agonist meaningfully raises it in
retina is absent, and three independent arguments (shared machinery, HIF-dominance, LPL
bounding) push against it. Round 1's demotion to a stage-restricted safety flag is correct and,
if anything, under-justified relative to the evidence available.**

---

## A5. (e) NEGATIVE AND NULL RESULTS — what has already failed

This is the section where this agent earns its place in the pipeline. The methodology skill's
first stated function is to *prevent the pipeline from regenerating hypotheses that have already
been tested and failed.*

### A5.1 Mechanisms in or adjacent to this candidate set with a failed or null human record

| Mechanism | Candidate(s) | Nature of the failure | Lvl | What it should stop |
|---|---|---|---|---|
| **Aldose reductase / polyol inhibition (P1)** | **D1 Epalrestat** | Named as a failed human DR mechanism in the blinded brief §4. Beyond DR, the class as a whole has a poor record across diabetic complications, with several agents withdrawn or abandoned for toxicity rather than discontinued for futility | 1b (per brief) | **Any recommendation of epalrestat on mechanism grounds.** The ADMET agent's finding that epalrestat achieves the best free-drug/IC50 ratio in the set is real and is *beside the point*: engagement of a falsified target is a negative, not a positive. Round 1's 6.0-vs-2.0 spread on this candidate is resolved entirely in favour of the low score |
| **PKCβ inhibition (P3)** | — (none directly) | Named as a failed human DR mechanism in the blinded brief §4 | 1b (per brief) | Correctly uncovered. No action |
| **Antioxidant-only strategies (P5)** | C1, C2, partly B2/B4 | Repeatedly null in DR per brief §4, **and** — permitted non-DR evidence — repeatedly null or harmful for hard clinical endpoints across large antioxidant-supplementation RCTs in cardiovascular disease and cancer prevention. The failure is not DR-specific; it is a property of the strategy | 1a (non-DR) | **Any candidate whose mechanistic case reduces to "reduces oxidative stress."** This applies most sharply to quercetin and to the fatty acids |
| **Dissociated nuclear-receptor ligands (transrepression without transactivation)** | A1–A5, as the limb Round 1 relies on | ~25–30 years, multiple companies, multiple clinical-stage glucocorticoid compounds, **zero approvals**; in vivo separation consistently smaller than in vitro | 1b, non-DR | **Treating the transrepression limb as a load-bearing part of a recommendation.** It is a research hypothesis with an unfavourable class prior (§A3.3) |
| **Microglial deactivation as neuroprotection** | **D3 Minocycline** | Minocycline specifically has a long string of null results in human neurodegenerative and neuroinflammatory disease, **including at least one large trial where the treated arm did worse than placebo.** The mechanism is attractive, well-documented preclinically, and has repeatedly failed to translate | **1b, non-DR, and this is strong** | **Minocycline's score.** Round 1 gave it 3.60 mean, which is roughly right, but the reasoning was "weak biology"; the correct reasoning is "good biology, demonstrated translational failure in the nearest comparable human setting." Those have different implications — the second also argues against *other* microglial agents |
| **ω-3 PUFA supplementation for a chronic retinal endpoint** | **B4 Icosapent ethyl, B2 ALA** | A large RCT of ω-3 LC-PUFA supplementation added to a background regimen in a chronic progressive *retinal* disease returned a **null** result for progression. Separately, in cardiovascular outcome trials, ω-3 results are inconsistent: one large trial in diabetics null, another large trial null, one positive trial with an unresolved comparator-choice controversy | **1b, non-DR, moderate-high** | **Icosapent ethyl's score, and the whole Group B premise.** The nearest available large RCT in a chronic retinal disease was null. That is as close to a direct test of the "ω-3 for retina" mechanism as permitted evidence gets |
| **PPARγ agonism** | — (excluded by brief) | Fluid retention; class-level edema liability | 1a | Correctly excluded. Maintain isoform discipline — including, per §A3.2, in the *benefit* direction |
| **Promiscuous polyphenols with <2% oral bioavailability** | **C1 Quercetin** | No polyphenol in this class has produced a positive hard-endpoint outcome trial in any indication, despite an enormous preclinical literature | 1a/1b, non-DR | Quercetin entirely. Round 1's tightest consensus (spread 1.5, score 1.92) is correct and I reinforce it |

### A5.2 The one I most want on the record

**Minocycline's failure pattern is the closest available analogue to what could happen to a
PPARα programme, and the pipeline has not drawn the lesson.**

Minocycline arrived in human neuroprotection trials with: a clearly defined mechanism, abundant
positive animal data across multiple models and laboratories, excellent CNS penetration (better
than any fibrate's retinal penetration), an established safety database, and generic
availability. It failed anyway — repeatedly, and in one case with harm.

The relevant inference is **not** "therefore PPARα will fail." It is that **the configuration
"strong preclinical + good exposure + cheap generic + plausible mechanism" has a poor prior in
chronic neuro-ophthalmic and neurodegenerative disease**, and that configuration is precisely
what this pipeline is selecting for. Round 1 treated cheapness and generic availability as
unalloyed positives (the Clinical agent's 7.0 for fenofibrate/fenofibric acid). They are
positives for *feasibility* and carry **no information about efficacy** — and the set of
mechanisms that are cheap, generic and plausible has been heavily picked over already.

### A5.3 What the pipeline should stop recommending, stated as rules

1. **Do not recommend epalrestat.** Target falsified; engagement is irrelevant.
2. **Do not advance any candidate whose mechanistic case reduces to antioxidant activity.**
   Quercetin, and the antioxidant portion of the melatonin and ω-3 cases.
3. **Do not present transrepression-at-low-occupancy as the reason a PPARα candidate should
   work.** Present it as an unmeasured possibility with an unfavourable class prior, and present
   the ICAM-1 threshold-amplification argument instead where an anti-inflammatory rationale is
   needed.
4. **Do not score "generic, cheap, long safety record" as evidence of efficacy.** Score it on the
   feasibility axis only, where it belongs.
5. **Do not advance icosapent ethyl on a retinal rationale** without addressing the null ω-3
   retinal-progression RCT directly.
6. **Do not recommend minocycline for neuroprotection** without explaining why this setting
   differs from the ones where the same mechanism failed.

---

## A6. (f) KNOWLEDGE GAPS — the single most important unmeasured quantity

### A6.1 The answer

> **The free (unbound) concentration of fibrate in human retinal interstitial fluid during
> chronic oral dosing — equivalently, retinal K<sub>p,uu</sub>.**

Every contested conclusion in this run is a function of this one number, and nobody has
measured it:

- At K<sub>p,uu</sub> ≈ 0.01–0.05: no retinal limb of any kind. The mechanism is entirely
  systemic, the receptor is a red herring, and **ezetimibe is a fair comparator and should
  reproduce most of the benefit.**
- At K<sub>p,uu</sub> ≈ 0.2–0.5 with the ICAM-1 threshold amplification: an endothelial
  anti-inflammatory limb is real, the drug matters as a receptor ligand, and **the ANGPTL4 flag
  must be reinstated at S4–S5** because the same occupancy that permits transrepression starts
  to permit transactivation.
- Above that: full transactivation, strong ANGPTL4 risk, and the entire exposure objection that
  organised this run was wrong.

**Three mutually exclusive programmes hang on one unmeasured number.** No amount of further
reasoning substitutes for measuring it. That is the correct top-line statement of this run's
epistemic position, and it is sharper than "we disagree about occupancy."

### A6.2 How to actually get it — in rank order of practicality

1. **Retinal target-gene output as a functional proxy (cheapest, available now).** Exactly the
   experiment Round 1 §4 proposes. Chronic oral fibrate in a diabetic rodent; measure retinal
   CPT1A/ACOX1/HMGCS2/ANGPTL4 against retinal ICAM1/TNF/leukostasis. **I add two design
   requirements Round 1 omitted, and without them the experiment is uninterpretable:**
   - **A `Ppara-/-` arm**, because without it any effect is attributable to the PPARα-independent
     activity fibrates demonstrably have at the concentrations reached (§A3.2 objection 1).
   - **A matched non-PPAR lipid-lowering arm** in the same animals, because without it a positive
     retinal readout cannot be assigned to the receptor rather than to lowered lipoprotein
     supply — the exact ambiguity E1/ezetimibe was added to the candidate set to resolve.
   Round 1 calls its version "cheap and decisive." **Without these two arms it is cheap and
   indecisive.**
2. **Human aqueous humour fibrate concentration** in patients on chronic therapy undergoing
   cataract surgery. Aqueous is not retinal interstitium, but it is obtainable from routine
   surgery with negligible added risk, and it bounds the problem. Pair it with aqueous ANGPTL4
   (§A4.3) in the same tap — **two of this run's three central unknowns from one sample.**
3. **Microdialysis or PET in large-animal eye.** Definitive, expensive, slow.

### A6.3 Runner-up gaps, ranked

| Rank | Gap | Why it matters |
|---|---|---|
| 2 | **Cell-type-restricted conditional `Ppara` deletion in retina** | The only experiment that establishes necessity. Its continued absence is itself informative (§A1.4) |
| 3 | **Intraocular ANGPTL4 stratified by fibrate exposure** | Settles the wrong-sign question empirically; samples already exist |
| 4 | **Whether the retinal benefit of systemic PPARα agonism is lipid-change-dependent** | This is the (i)-vs-(ii/iii) discriminator stated as a measurable covariate. **If the benefit does not track the lipid change, limb (i) is in trouble and the receptor hypothesis strengthens** |
| 5 | Human FGF21 dose-response at therapeutic fibrate doses, and whether it reaches concentrations active on retinal endothelium | Quantifies the one exposure-safe limb |

**Gap #4 deserves a flag to the orchestrator.** It is the cleanest discriminator between the
run's two competing readings, it is a *covariate analysis* rather than a new experiment, and it
is answerable from data of a kind that is routinely collected. If any dataset anywhere permits
this analysis, it is worth more than everything else in this list.

---

## A7. PART A SCORING RATIONALE

**Axis: published mechanistic evidence strength, Part A basis only.** Not efficacy, not
feasibility, not target engagement — *how good is the published evidence that this compound's
mechanism does something relevant to DR biology*, using no DR/DME trial or indication evidence.

**Nothing in this set scores 7 or above on this axis, and that is a finding, not a hedge.** A 7+
would require Level 1–3 human mechanistic evidence tied to a retinal endpoint, or Level 4
evidence replicated across independent laboratories with a necessity experiment. **No candidate
has either.** The run's best-evidenced mechanism (limb (i)) is human-validated only up to a step
that is two removes from the retina.

| Candidate | Score | Basis |
|---|---|---|
| Fenofibric acid | 6.5 | Limb (i) chain human-validated to the apoB/FGF21 step; retinal limb Level 4 moderate; active moiety of the best-characterised molecule in the set |
| Fenofibrate | 6.5 | Same pharmacological entity; most of the human PD evidence (FGF21, apoC-III) was generated with this agent |
| Pemafibrate | 6.0 | Receptor-level evidence is the best in the set (selectivity, structural, transcriptomic); retinal mechanistic evidence zero; hepatoselectivity means it tests limb (i) and only limb (i) |
| Dimethyl fumarate | 6.0 | KEAP1/NRF2 covalent mechanism exceptionally well characterised; **the only candidate with Level 1b human evidence that its mechanism alters the course of a chronic CNS inflammatory disease.** Penalised because the NRF2 axis overlaps the brief's "antioxidant alone" prior |
| Candesartan cilexetil | 6.0 | AT1R pharmacology Level 1a-validated in diabetic microvascular complications elsewhere; local retinal RAS documented by multiple independent groups; luminal target needs no barrier crossing |
| Ezetimibe | 4.5 | NPC1L1 mechanism superbly characterised **and human-genetically validated** (loss-of-function variants → lower apoB and lower cardiovascular risk) — but zero retinal mechanistic evidence, no FGF21 relay, and the remnant-vs-LDL mismatch the brief states |
| Elafibranor | 4.5 | Real human PD data; PPARδ co-agonism has published pro-angiogenic retinal evidence pointing the wrong way; Michael-acceptor liability |
| Melatonin | 3.5 | MT1/MT2 pharmacology solid, retinal synthesis documented, preclinical neuroprotection broad but small-study; no hard-endpoint human success in any indication |
| Icosapent ethyl | 3.5 | Membrane/SPM mechanism plausible and partly human-validated; **but the nearest large RCT of ω-3 in a chronic retinal disease was null**, and CV trial results are inconsistent |
| Seladelpar | 3.0 | PPARδ evidence in retina points pro-angiogenic; as a falsification control it is confounded in both directions |
| Minocycline | 3.0 | Microglial mechanism well documented preclinically; **demonstrated repeated translational failure of that exact mechanism in human CNS disease**, including one trial with harm |
| Alpha-linolenic acid | 2.5 | Genuine data-backed PPARα binding; endogenous ligand near its own EC50 at baseline, so not dose-movable; no disease-mechanism evidence |
| Linalool | 2.5 | The only genetic-dependency engagement evidence in the set (PPARA-dependent SLC27A4 induction) — but single-source, unreplicated, and with no link to any DR node |
| Epalrestat | 2.0 | AKR1B1 inhibition well characterised; **the mechanism carries negative human validation per brief §4.** Good engagement of a falsified target scores low on an evidence axis |
| Linoleic acid | 2.0 | Binding/activation well attested across ≥4 PMIDs; ω-6 substrate for cytotoxic oxidised-LA metabolites makes even the direction arguable; not dose-movable |
| Quercetin | 1.5 | Direction-incoherent on PPARα; <2% bioavailability; dual efflux substrate; no polyphenol of this class has a positive hard-endpoint trial anywhere |

---

## A8. PART A BLINDING DISCLOSURES

Files read: `disease-brief.md`, `round1-synthesis.md`, `blinding-protocol.md`,
`.claude/skills/literature-reviewer/SKILL.md`, and targeted sections of `agents/p1-target.md`
and `agents/p1-disease.md`. I did **not** read `data/processed/chembl_approved_drugs.csv`,
anything under `data/holdout/`, or any `answer-key*` file, and I did not use git history.

**Two borderline calls, disclosed:**

1. **I used the human observational association between serum lipids and retinal hard exudate**
   (§A2, limb (i)). This is DR-specific human evidence, but it is epidemiological, not a trial
   and not an indication; the blinded disease model already asserts the underlying claim (hard
   exudates are retained modified apoB lipoproteins). I judged it permitted. Flagging it because
   reasonable people could score it differently.
2. **I used the human aqueous/vitreous ANGPTL4 case-control data** (§A4.1). Same reasoning —
   human tissue biomarker measurement in DR patients, no drug involved, no trial, no indication.
   The blinded brief itself raises ANGPTL4 as the wrong-sign risk and demands every agent
   address it, which cannot be done without this literature.

**Honest statement about the irreducible residual.** I know the DR clinical literature for
several of these candidates. I cannot unknow it. What I can do, and did, is construct Part A
from evidence I can name and grade independently of it, and check each Part A conclusion against
the question "would I assert this if the trials did not exist?" **One place where the answer was
uncomfortable, and I am recording it:** my grade of "moderate" rather than "low" for the
retina-targeted-expression arm (§A1.4) is a judgment call, and I cannot fully exclude that
knowing the clinical outcome nudged it upward. I have left it at moderate and flagged it rather
than artificially deflating it, since a deliberate downward correction would be just as
contaminated as an upward one. **No score in the SCOREBLOCK was altered after Part B was
written.**

---
---

# PART B

---

## POST-HOC UNBLINDING — MOVED

The unblinding section that formerly lived here has been moved to a separate file:
`UNBLINDING-part-b.md` (sibling of this file, in the same directory).

**Reason.** An in-file boundary does not survive structural inspection. A blinded agent
running a heading-level grep to locate the end of Part A received the Part B headings,
two of which carried substantive content. The agent disclosed this immediately and read
no body text, but the leak was real. Content was protected; structure was not — the same
class of defect as the `[REDACTED-HOLDOUT]` markers found in Phase 0.

Nothing in Part B informed any score in Part A or in the SCOREBLOCK below.

## SCOREBLOCK

SCORE|Fenofibric acid|6.5|moderate|knowledge-based|Human-validated systemic chain; retinal evidence Level 4 moderate, single-lineage
SCORE|Fenofibrate|6.5|moderate|knowledge-based|Same moiety; most human PD evidence (FGF21, apoC-III) generated with it
SCORE|Pemafibrate|6.0|moderate|knowledge-based|Best receptor-level characterisation in set; zero retinal mechanistic evidence
SCORE|Dimethyl fumarate|6.0|moderate|knowledge-based|Covalent KEAP1 mechanism superb; only Level 1b human CNS-disease validation here
SCORE|Candesartan cilexetil|6.0|moderate|knowledge-based|AT1R Level 1a elsewhere; retinal RAS documented by independent groups; luminal target
SCORE|Ezetimibe|4.5|moderate|knowledge-based|Human-genetically validated apoB mechanism; no retinal evidence; remnant-versus-LDL mismatch
SCORE|Elafibranor|4.5|moderate|knowledge-based|Real human PD; PPARδ co-agonism has published pro-angiogenic retinal evidence
SCORE|Melatonin|3.5|moderate|knowledge-based|Solid receptor pharmacology and retinal synthesis; no hard-endpoint success anywhere
SCORE|Icosapent ethyl|3.5|moderate|knowledge-based|Nearest large ω-3 RCT in chronic retinal disease was null
SCORE|Seladelpar|3.0|low|knowledge-based|PPARδ retinal evidence points pro-angiogenic; confounded as falsification control
SCORE|Minocycline|3.0|high|knowledge-based|Good preclinical mechanism; repeated human CNS translational failure, including one harm signal
SCORE|Alpha-linolenic acid|2.5|moderate|mixed|Data-backed binding; endogenous ligand near own EC50, not dose-movable
SCORE|Linalool|2.5|low|mixed|Only genetic-dependency engagement evidence in set; single-source, unreplicated, no DR node
SCORE|Epalrestat|2.0|high|knowledge-based|Well-characterised inhibition of a mechanism carrying negative human validation
SCORE|Linoleic acid|2.0|moderate|mixed|Binding well attested; oxidised-LA metabolites make direction arguable; not dose-movable
SCORE|Quercetin|1.5|high|mixed|Direction-incoherent on PPARα; efflux substrate; no polyphenol hard-endpoint precedent
