# Phase 2 — Drug Repurposing Strategist
## Diabetic Retinopathy (BLINDED RUN) · 2026-10-05

**Axis scored:** repositioning attractiveness = mechanism fit × achievable exposure at the
relevant compartment × development feasibility in a chronic, CKD-dominant, polypharmacy
population.

**Evidence tagging:** `[DATA]` = read from `data/processed-blinded-diabetic-retinopathy/` or the
Round 1 evidence pack. `[KB]` = my pharmacological knowledge, non-DR. `[CALC]` = my arithmetic.
Everything of consequence in this report is `[KB]`; §7 says why, and what would change it.

---

## 0. EXECUTIVE SUMMARY

I was asked to search drug space for an escape from the trap Round 1 identified. I found three
things, one negative and two positive.

**The negative, and it is firm.** There is **no approved non-acidic PPARα agonist anywhere**, and
there is **no approved molecule with meaningful PPARα activity that reaches retinal tissue**. I
searched the approved pan/dual-PPAR space, the non-fibrate PPARα-active space, the endogenous
ligand classes, and — approaching from the opposite direction — the drug classes that are *known*
to achieve retinal concentrations, asking whether any of them touch PPARα. The two sets do not
intersect. **Round 1's conclusion that the retina-intrinsic PPARα hypothesis is untestable by
repositioning is correct, and I am confirming it from the drug-space side rather than the
chemistry side.** Testing that hypothesis requires a molecule that does not exist.

**Positive finding 1 — the structural escape nobody has used.** Every candidate in this run fights
the term `Kp,uu` in `occupancy ∝ fu × C_plasma × Kp,uu / EC50`. The **plasma kallikrein–kinin axis
eliminates that term instead of fighting it**: intravitreal kallikrein is plasma-derived
prekallikrein that extravasated, so a systemically dosed inhibitor acts on its target in the
compartment where the target already is. No barrier crossing is required for the mechanism to
work. **Berotralstat** (CHEMBL5189739, `[DATA]`) is an approved, once-daily **oral** plasma
kallikrein inhibitor whose licensed use is *chronic outpatient prophylaxis in asymptomatic people*
— the exact deployment model DR needs — and it is not primarily renally cleared. This is my top
new nomination (score 7) and it is orthogonal to the entire PPARα question.

**Positive finding 2 — Round 1 §5 contains a factual error I can correct.** The synthesis states:
*"No non-PPAR remnant-lowering generic exists to do better [than ezetimibe]."* A non-PPAR
remnant-lowering agent now exists: **olezarsen**, an apoC-III antisense oligonucleotide approved
in Dec 2024. This matters disproportionately, because **apoC-III suppression is the precise
downstream node through which PPARα agonism lowers remnants** (PPARα transrepresses *APOC3*).
Olezarsen is therefore not a loosely-matched control like ezetimibe — it is the *same mechanism
with the receptor deleted*. It is expensive and indication-restricted, so it is a probe and not a
therapy, but as the discriminating arm it is far cleaner than E1.

---

## 1. (a) IS THERE AN APPROVED OR LATE-STAGE NON-ACIDIC PPARα LIGAND ANYWHERE?

### 1.1 The search frame

The Medicinal Chemist's result defines what I am looking for. Potency in this class is bought with
lipophilic bulk filling PPARα's arms II/III, and that same bulk is what albumin site II and the
hepatic OATP1B transporters recognise — so `fu`, `C_plasma` and `Kp,uu` all degrade together as
`EC50` improves. The acidic head group is the other half of the problem: a permanent anion at
pH 7.4 is both the AF-2 anchor *and* the OATP1B recognition element *and* the albumin site II
anchor. **A molecule that escapes needs AF-2 engagement without a permanent anion.** That is the
single specification. Everything below is scored against it.

### 1.2 Pan-PPAR and dual agonists of other chemotypes

| Agent | Status | Chemotype / ionisation | Why it does or does not escape |
|---|---|---|---|
| **Saroglitazar** | Approved (India, 2013) — diabetic dyslipidaemia, NAFLD/NASH | Phenoxyalkyl-pyrrole **α-alkoxy-propanoic acid** | **No escape.** Same anionic head as the fibrates, same albumin/OATP1B recognition. Adds PPARγ agonism → the brief's fluid-retention prior (§4). |
| **Lanifibranor** | Phase 3 (MASH) | Indole/benzothiophene-sulfonyl; reported **non-fibrate, non-TZD** chemotype — I believe it carries **no free carboxylic acid**, but the structure should be confirmed before relying on this | **The closest thing to a chemotype escape that exists.** Disqualified on pharmacology, not chemistry: it is a **pan-PPAR agonist including γ**, and its Phase 2b showed weight gain and peripheral oedema — a direct hit on the scoring prior the brief singles out as associated with worsening macular oedema. |
| **Chiglitazar** | Approved (China, 2021) — T2D | Non-TZD pan-agonist, **carboxylic acid** | No chemotype escape; γ-dominant; oedema/weight gain reported. |
| **Aleglitazar** | **Discontinued 2013** (AleCardio) | Oxazole-**propanoic acid** | Terminated for **heart failure, bone fracture, GI haemorrhage, renal dysfunction**. |
| **Muraglitazar** | **Discontinued 2006** | Glycine/oxazole **acid** | Terminated for **excess death/MI/stroke/TIA, oedema, heart failure**. |
| **Tesaglitazar** | **Discontinued 2006** | **Propanoic acid** | Terminated for **serum creatinine rise and falling GFR** — the precise liability the brief flags as critical in a population where renal impairment is the norm. |
| **Ragaglitazar / farglitazar** | Discontinued | Acids | Rodent urinary bladder tumours (ragaglitazar); efficacy (farglitazar). |

**The pattern is itself the most important finding in this section, and it is independent of any
retinal consideration.** Every dual or pan PPAR agonist that reached late-stage Western development
was terminated, and the terminating toxicities form a coherent set: **oedema, heart failure,
creatinine rise and GFR decline, bone fracture, cardiovascular events.** Each of those is a
liability the diabetic retinopathy population — CKD-dominant, cardiovascular, and at risk of
macular oedema — can least afford. **The dual/pan-PPAR lane is not merely unattractive here; it
carries a class-level regulatory graveyard, and a sponsor proposing it would be asked to explain
AleCardio before anything else.** I score the whole lane low regardless of chemotype.

### 1.3 Non-fibrate molecules with PPARα activity

- **Statins** — weak, indirect, not credible as direct agonism. Also the confound (§3.4).
- **Telmisartan** — a genuine nuclear-receptor-active ARB, but **PPARγ** partial agonist, not α.
  Carries the oedema flag; wrong isoform under the brief's isoform discipline.
- **Phthalates (DEHP, dibutyl phthalate)** — the parent diesters are neutral, but the actual PPARα
  ligands are the **mono-ester acids** formed in vivo. So even the best-controlled activation
  evidence in the project file `[DATA: ppara-interactions.tsv]` is evidence for an *acid*. Also
  reproductive toxicants. Mechanistic controls only, as the brief already designates.
- **WY-14643 (pirinixic acid), GW7647, GW590735** — tool compounds, all acids, never approved.
- **Perfluoroalkyl acids** — acids and toxicants.
- **Bezafibrate** — weak pan-PPAR, acid. Not in the dataset `[DATA: 0 hits]`.

**Nothing here escapes.** The acid is not a convention in this class; it is load-bearing in every
approved and tool molecule.

### 1.4 N-acylethanolamines — the direct answer, assessed seriously

The brief asked me to take these seriously. I have, and they are the most interesting molecules in
this report — they are simultaneously the **right answer to the chemotype question and the wrong
answer to the exposure question**, and the reason is specific and worth stating precisely.

**Why they are the right chemotype.** Oleoylethanolamide (OEA) and palmitoylethanolamide (PEA) are
**neutral, non-ionisable** PPARα agonists — OEA with reported EC50 ~120 nM, PEA considerably
weaker (~low µM, and an appreciable share of PEA's pharmacology is argued to run through
GPR55/"entourage" potentiation of endocannabinoid tone rather than PPARα proper). The ethanolamide
head — an amide carbonyl plus a primary hydroxyl — apparently substitutes for the carboxylate at
the AF-2 anchor (Ser280 / Tyr314 / His440 / Tyr464). **This is a direct existence proof that the
permanently anionic head is not required for PPARα AF-2 engagement**, which is the single most
useful thing I can hand the SAR Analyst for question 4 of the Phase 2 routing.

Consequences for every numerator term, which is exactly what Round 1 said no fibrate can deliver:

| Term | Fibrate | N-acylethanolamide |
|---|---|---|
| `fu` | ~0.01 (albumin **site II anion** pocket) | Bound, but by lipid partitioning — not the site-II anion pocket; not the same hard floor |
| `Kp,uu` | 0.01–0.15 neural / 0.2–0.7 endothelial, and **capped below 1** | Neutral lipophilic amide: good passive transcellular permeability, no anion exclusion |
| Hepatoselectivity | **Obligate** — OATP1B1/1B3 substrate | **None.** Not an organic anion; no OATP1B recognition element |

**Why they nonetheless fail.** PEA and OEA are substrates for **FAAH** and **NAAA**, with
half-lives of minutes. Oral PEA — micronised/ultramicronised, 600–1200 mg/day, widely available in
Europe as a food for special medical purposes with a genuinely benign chronic record and
essentially no DDIs — produces transient, modest plasma excursions. It is **almost certainly not
dose-movable to a sustained free concentration above its PPARα EC50.** This is the same
"not dose-movable" objection the Ethnobotany agent raised against α-linolenic acid, but arising
from a different cause: enzymatic destruction rather than homeostatic buffering.

**The repair, stated honestly as discovery and not repositioning.** Two routes:
1. **FAAH inhibition**, which raises endogenous OEA/PEA several-fold and is CNS-penetrant by
   design. But there is **no approved FAAH inhibitor**; the field carries the BIA 10-2474
   catastrophe (Rennes 2016 — one death, four with neurological injury, attributed to that
   compound's off-target activity rather than to FAAH inhibition per se), and PF-04457845 was
   clean in humans but failed on efficacy.
2. **A FAAH/NAAA-resistant OEA analogue** — α-methylation or oxazoline/retro-amide replacement of
   the hydrolysable bond. This is tractable medicinal chemistry and it is the concrete molecule
   this programme would have to make.

A third, more conservative variant deserves recording: a **deliberately slowly-hydrolysed ester or
amide prodrug of fenofibric acid**. Fenofibrate does not do this — it is hydrolysed essentially
completely pre-systemically, so it never delivers neutral drug to the retina; it is a solubility
prodrug, not a distribution prodrug. An esterase-resistant ester designed to **circulate as the
neutral species** and unmask intracellularly would carry the anion across as cargo. Again:
discovery, not repositioning.

### 1.5 Answer to (a)

> **No.** No approved non-acidic PPARα ligand exists. The two near-misses fail for opposite and
> instructive reasons: **lanifibranor** may have the right chemotype but has disqualifying
> pan-PPAR/γ pharmacology (oedema, weight gain) in precisely the indication where that matters
> most; **PEA/OEA** have exactly the right chemotype, real PPARα agonism, and excellent chronic
> safety, but are destroyed by FAAH/NAAA faster than they can accumulate. **The retina-intrinsic
> PPARα hypothesis cannot be tested by repositioning. It requires a new chemical entity**, and
> §1.4 specifies what it should look like.

---

## 2. (b) IS THERE ANY PPARα-ACTIVE MOLECULE THAT REACHES RETINAL TISSUE?

I approached this from the delivery side as instructed — enumerate what *does* get into retina
after systemic dosing, then ask whether any of it touches PPARα.

### 2.1 What actually achieves retinal concentrations, and by what route

| Class / exemplar | Retinal access mechanism | PPARα activity |
|---|---|---|
| **Tetracyclines** — minocycline, doxycycline | Amphoteric, tissue-accumulating; minocycline is the most lipophilic and most CNS/retina-penetrant of the class | **None** |
| **Melanin-binding basic amines** — hydroxychloroquine, chloroquine, thioridazine, phenothiazines | **Bind melanin in RPE/choroid** and accumulate to the point of causing retinal *toxicity* | **None** |
| **MFSD2A / LPC lipid route** — DHA, lysophosphatidylcholine conjugates | **A genuine concentrative uptake transporter at the inner BRB**, carrying LPC-esterified fatty acids into retina | Weak/non-selective (the ω-3 pool) |
| **Carotenoid route** — lutein, zeaxanthin (StARD3/GSTP1); retinol (RBP4/STRA6) | Actively concentrated into macula/RPE | **None** |
| **Fluoroquinolones** | Reach vitreous at therapeutic levels | None |
| **PDE5 inhibitors** — sildenafil | Reach retina (PDE6 cross-reactivity causes the visual symptoms) | None |
| **Carbonic anhydrase inhibitors** — acetazolamide | Reach RPE; act on the outer-BRB pump | None |
| **Vigabatrin, deferoxamine** | Reach retina (vigabatrin demonstrably — it causes retinal toxicity) | None |

### 2.2 The two design insights this table yields

These are worth more to the programme than any candidate.

**(i) Melanin binding is the retinal analogue of OATP1B.** The brief's §6 says "the retina has no
analogous uptake transporter to the liver's OATP system." That is true for *transporters*, but
**RPE and choroidal melanin are a real retinal concentrating sink**, and the molecules that exploit
it are **basic lipophilic amines**. Hydroxychloroquine retinopathy is the proof — the sink is so
effective it is a toxicity mechanism. **Fibrates are anions; they do the exact opposite.** A basic
amine centre is therefore a concrete, actionable design element for a retina-directed PPARα ligand,
and no PPARα-active molecule has one.

**(ii) MFSD2A *is* the missing uptake transporter — it just does not take anions.** MFSD2A carries
lysophosphatidylcholine-esterified fatty acids across the inner BRB, and LPC conjugation is an
established delivery strategy (LPC-DHA dramatically improves brain delivery versus free DHA).
**An LPC conjugate of a PPARα ligand is the single most specific available answer to the brief's
core objection**, because it supplies precisely the concentrative mechanism the brief says does not
exist. This is a discovery proposal, but it is a well-specified one.

### 2.3 The one half-exception, and one disqualified curiosity

**Icosapent ethyl / EPA** is the only candidate that rides a real retinal lipid route. It is a
genuine oral drug with a chronic cardiovascular safety database `[DATA: CHEMBL2095209, approved
2012]`. Its failure is not access — it is that its PPARα agonism is weak, non-selective, and
**not dose-movable above endogenous free-fatty-acid tone**, the same objection that sinks B1/B2.
It also carries an atrial fibrillation and bleeding signal on chronic dosing. This partially
rehabilitates its *rationale* while leaving its *score* where Round 1 put it.

**Bexarotene** deserves recording because it is the one non-obvious way to activate the PPARα
transcriptional unit without a PPARα ligand at all: PPARα:RXR is a **permissive heterodimer**, so
an RXR agonist activates it from the other subunit. Bexarotene is approved (CTCL), lipophilic and
CNS-penetrant. It is nonetheless **unusable here**: it causes severe hypertriglyceridaemia in the
large majority of patients and central hypothyroidism. The lipid effect runs *directly against* the
systemic limb of the hypothesis — the two mechanisms would fight each other inside the same
patient. Mechanistically elegant, clinically disqualified. Score 1.

### 2.4 Answer to (b)

> **Essentially no.** The classes that reach retina — tetracyclines, melanin-binding basic amines,
> the MFSD2A/LPC lipid route, the carotenoid route — contain **nothing with meaningful PPARα
> activity**. The classes with PPARα activity are organic anions that none of those routes carry.
> The sets are disjoint, and the reason is the same anionic head group that §1 identified.

---

## 3. (c) REFRAME — IF THE MECHANISM IS SYSTEMIC apoB/REMNANT LOWERING

This is the most important section, because it is the strongest version of the Round 1 concern and
it deserves to be taken at full force before being answered.

### 3.1 The challenge at full strength

If the operative mechanism is reduction of the supply of atherogenic apoB particles to a leaking
retinal vasculature, then PPARα is a **bystander** — an upstream lever that happens to move apoB
a little — and the correct question is simply *which drug moves the toxic particle most, safely,
in this population*. On that question the fibrates are near the bottom of the table.

| Agent | apoB ↓ | TG / remnant ↓ | LDL-C ↓ | Administration | Chronic safety in CKD + polypharmacy |
|---|---|---|---|---|---|
| **PCSK9 mAb** (evolocumab, alirocumab) | **~45–55%** | ~15–20% | 55–60% | SC q2w/q4w | Excellent; no renal adjustment; no myopathy; no meaningful DDI |
| **Inclisiran** (PCSK9 siRNA) | ~40–45% | modest | ~50% | **SC twice yearly** | Excellent; injection-site reactions only |
| **Evinacumab** (anti-ANGPTL3) | ~40–50% | ~50% | ~50% | IV q4w | HoFH-restricted; extreme cost |
| **High-intensity statin** | ~35–45% | ~15–25% | 45–55% | Oral generic | **Background therapy → confound (§3.4)** |
| **Olezarsen** (apoC-III ASO) | modest | **~50–70%** | — | SC monthly | Approved Dec 2024, FCS-restricted |
| **Ezetimibe (E1)** | ~15–20% | ~5–10% | ~18–20% | Oral generic | Very good |
| **Bempedoic acid** | ~15–20% | ~0 | ~18% | Oral | **Raises uric acid → gout; tendon rupture** — both common in this population |
| **Fibrate** | **~5–15%** | **~35–50%** | variable, can ↑ | Oral generic | Creatinine rise; statin-myopathy interaction |

> **Read plainly: a PCSK9 inhibitor lowers apoB three to five times more than any fibrate.** If
> apoB supply is the mechanism, a PCSK9 inhibitor must produce a *larger* retinal effect than a
> fibrate. That is a clean, falsifiable, and uncomfortable prediction, and the honest position is
> that the PPARα framing is in real jeopardy from it.

### 3.2 The counter that rescues the framing — and it is a particle argument, not a receptor argument

The counter is not "but the receptor matters." It is that **apoB mass is the wrong metric.**

- PCSK9 inhibition clears **LDL**, by upregulating hepatic LDL receptor.
- Fibrates clear **triglyceride-rich remnants**, by LPL activation via *APOC3* repression and
  *APOA5* induction.
- The disease model identifies the retinal toxic species as the **extravasated, glycated-and-
  oxidised apoB particle retained in the outer plexiform layer** — hard exudate is retained modified
  lipoprotein, not "fat."
- **Diabetic dyslipidaemia is a remnant and small-dense-LDL disorder in which LDL-C is often
  near-normal.** The particles that extravasate and are retained are the small, modified ones.

**Therefore apoB mass reduction is the wrong endpoint and remnant-particle / apoC-III reduction is
the right one** — and on *that* metric fibrates are competitive with or superior to PCSK9
inhibitors despite far smaller apoB numbers. The hypothesis survives, but only in a specific form:
*it is a remnant hypothesis, not an apoB-mass hypothesis.*

### 3.3 The consequence — Round 1 §5 can be corrected, and the control upgraded

Round 1 §5 states: *"No non-PPAR remnant-lowering generic exists to do better."* **The generic
qualifier is right; the existence claim is now wrong.**

> **Olezarsen** — apoC-III antisense oligonucleotide, approved December 2024 for familial
> chylomicronaemia syndrome. Lowers apoC-III ~70–85% and triglycerides ~50–70%. **Zero PPAR
> activity.** **Plozasiran** (apoC-III siRNA) is in Phase 3 behind it.

This is not a loosely-matched control like ezetimibe. **ApoC-III suppression is the exact
downstream node through which PPARα agonism lowers remnants.** Olezarsen is the same mechanism with
the receptor surgically removed — which is the definition of the discriminating arm this run has
been looking for:

- Olezarsen reproduces the retinal benefit → **the receptor is not doing the work**; the programme
  is a remnant-lowering programme and should be run as one, with a far better drug than a fibrate.
- Olezarsen does *not* reproduce it while a fibrate does → **a retinal or transrepression
  contribution survives**, and it survives a much harder test than ezetimibe could ever impose.

It is expensive, SC monthly, and indication-restricted, so it is a **mechanistic probe, not a
therapy for this population.** But for a 60–100 patient mechanism-discrimination study with a
surrogate endpoint, that is acceptable — and it is a far better use of money than a large ezetimibe
arm whose null result would be uninterpretable.

**On E1/ezetimibe specifically:** retain it, but downgrade expectations. It lowers *cholesterol
absorption* and predominantly *LDL-C* — the wrong particle. A null ezetimibe result cannot
distinguish "the receptor matters" from "LDL is not the toxic species," so **E1 cannot do the job
it was added to do.** It remains worth including because it is cheap, safe, oral and generic, but
the orchestrator should add an apoC-III-directed arm as the properly matched comparator.

### 3.4 A confound the brief flags that deserves restating

**Statins are background therapy in essentially this entire population**, and a high-intensity
statin lowers apoB 35–45% — more than any fibrate. If apoB supply were straightforwardly
protective, much of that effect is already being delivered to every patient in both arms of any
trial. Any incremental lipid-limb effect is therefore being measured *on top of near-maximal
background apoB lowering*, which (i) compresses the achievable effect size and (ii) argues that
whatever a fibrate adds is more likely to be the **remnant/apoC-III** component that statins do
*not* address. This strengthens §3.2 and is an argument for powering on remnant metrics.

### 3.5 Answer to (c)

> **Yes, the PPARα framing may well be wrong — but ezetimibe is not the test that would show it.**
> The properly matched test is an **apoC-III-directed agent (olezarsen)**, which did not exist when
> Round 1 was written and does now. Separately: **if the apoB limb is the real one, the best drug
> for it is not a fibrate.** Among all agents it is **inclisiran** — ~40–45% apoB reduction,
> outstanding chronic safety, no renal adjustment, no DDI, and uniquely **twice-yearly** dosing,
> which is the only administration schedule genuinely compatible with lifelong prophylaxis in
> asymptomatic people (unmet need #4). Among oral generics it is **pemafibrate**, on remnant and
> apoC-III lowering plus CKD safety, not on apoB mass.

---

## 4. (d) THE ANGPTL4 INVERSION

**Direct answer: this yields no repositioning candidate, and I want to be unambiguous about that
rather than manufacture one.**

**ANGPTL4 itself is not druggable systemically.** Systemic ANGPTL4 blockade in non-human primates
produced **lethal chylous ascites and severe intestinal lymphadenopathy** — a finding that closed
systemic anti-ANGPTL4 as a therapeutic route across the industry. Intravitreal anti-ANGPTL4 is
conceivable, but it would then compete on the same route, with the same burden, against established
intravitreal therapy — serving neither unmet need #1 nor #4. There is nothing approved.

**ANGPTL3 is the druggable, safe member of the family** — evinacumab (approved, HoFH), zodasiran
and solbinsiran (siRNA, development). Humans with ANGPTL3 loss of function are healthy (familial
combined hypolipidaemia), which is why it lacks the ANGPTL4 toxicology. **But I want to prevent a
category error that is easy to make here:** ANGPTL3 inhibition is a **lipid mechanism**, not a
retinal-permeability mechanism. It lowers LDL and remnants. It belongs in §3's table — and it
belongs there near the bottom on feasibility (evinacumab is IV q4w, HoFH-restricted, extraordinarily
expensive). **It does nothing whatsoever about the ANGPTL4 sign problem.** ANGPTL3 and ANGPTL4 are
family members, not substitutes.

**Does the inversion reframe the target?** Only in the way Round 1 already concluded, and I confirm
it rather than extend it: it argues for **stage-gating the PPARα programme to S1–S3 and excluding
S4/PDR**, and for **plasma ANGPTL4 as a mandatory monitored biomarker**. I would add one
repositioning-specific observation: the hepatic ANGPTL4 induction route the ADMET agent identified
— hepatic PPARα *is* fully engaged, raising **circulating** ANGPTL4 which reaches retinal
endothelium from the luminal side needing no barrier crossing — is **worst for the most
hepatoselective agent**. That is a real, quantifiable demerit specific to pemafibrate, and it
partially offsets pemafibrate's advantages in §6. It should be measured, not argued about.

> **ANGPTL4 is a safety flag and a biomarker. It is not a target, and it generates no candidate.**

---

## 5. (e) KALLIKREIN–KININ AND VEGF-INDEPENDENT PERMEABILITY

This is where the search paid off, and the reason is structural rather than pharmacological.

### 5.1 Why this axis is categorically different from everything else in this run

Every other candidate in this run — all sixteen — is fighting `Kp,uu`. The kallikrein axis
**deletes the term**:

- `[DATA: disease-model.md §355-360]` Plasma prekallikrein (**KLKB1**) and Factor XII (**F12**)
  **extravasate into the vitreous from plasma**, are activated there, and generate bradykinin acting
  on **BDKRB1/BDKRB2** → vasodilation, permeability, haemorrhage. The model grades this
  `[EMERGING → CURRENT CONSENSUS]` and calls it a leading explanation for the anti-VEGF
  non-responder fraction — **unmet need #2**, the second-ranked need in the brief.
- **The pathogenic protein is plasma-derived.** A systemically dosed inhibitor engages prekallikrein
  and kallikrein **in the compartment they already occupy**, before and during extravasation. The
  blood-retinal barrier is not an obstacle to the mechanism; it is upstream of it.
- `occupancy ∝ fu × C_plasma × Kp,uu / EC50` **→ `Kp,uu` drops out.** The entire arithmetic that
  dominates this run does not apply.

That is a genuinely different kind of candidate, and it is the strongest single structural argument
I can make for anything in this report.

### 5.2 The armamentarium, assessed for route and feasibility

| Agent | Route / schedule | Status | Repositioning assessment |
|---|---|---|---|
| **Berotralstat** (Orladeyo) | **Oral, 150 mg once daily** | Approved 2020, HAE **prophylaxis** | **Best fit by a clear margin.** Its licensed use *is* chronic daily prophylaxis in outpatients who feel well — the exact behavioural model DR needs. `[DATA: CHEMBL5189739, MW 562.57, aLogP 5.70, PSA 108.76, RTB 9, QED 0.23, first approval 2020]`. Not primarily renally cleared → **no dose adjustment in mild/moderate renal impairment**, which in a CKD-dominant population is close to decisive. |
| **Lanadelumab** | SC q2w–q4w | Approved, HAE prophylaxis | Excellent chronic safety, no DDI, no hepatic/renal issues. Biologic cost and injection burden; monoclonal size means negligible vitreous entry — but per §5.1 it does not need any. A credible second choice, better tolerated than berotralstat, far more expensive. |
| **Garadacimab** | SC monthly | Approved 2025, anti-FXIIa | Upstream of kallikrein; monthly dosing. Same logic, less precedent. |
| **Sebetralstat** | Oral, **on-demand** | Approved 2025 | Designed for acute attacks, not prophylaxis. Wrong use-model. |
| **Ecallantide** | SC, acute | Approved | **Anaphylaxis risk**; acute use only. Unsuitable. |
| **Icatibant** | SC, on-demand, B2R antagonist | Approved | Receptor-level, on-demand only; B1R escape is a mechanistic concern in chronic inflammation. |
| **Aprotinin** | IV | **Withdrawn** (mortality) | Dead. |

### 5.3 A non-obvious safety advantage

Plasma kallikrein sits in the **contact activation pathway**, and contact-pathway inhibition is
notably **not** associated with bleeding — humans deficient in FXII or prekallikrein do not bleed.
This is the entire thesis of the FXI/FXII anticoagulant field. **That matters specifically here**,
because the population at S4 is already at risk of vitreous haemorrhage, and a permeability drug
that increased bleeding risk would be unusable. Berotralstat does not carry that liability.

### 5.4 Honest liabilities

- **CYP2D6 and CYP3A4 inhibition** — a real DDI concern in a polypharmacy population. Requires a
  systematic interaction review against the concomitant classes the brief lists.
- **QT prolongation at supratherapeutic doses**; **GI intolerance**; **transaminase elevation**;
  not studied in severe hepatic impairment.
- **Orphan-drug pricing** — a serious obstacle to unmet need #8 (LMIC deployability). This argues
  for targeting unmet need #2 (incomplete-responder DME, a specialist population already receiving
  expensive therapy) rather than unmet need #1.
- **It addresses permeability, not early disease modification.** It serves need #2, not #1.
- `[DATA]` The project dataset contains **two** KLKB1 rows in the whole PubChem interaction file,
  both CTD mRNA-expression associations from toxicants (dibutyl phthalate, methyleugenol). **This
  nomination has zero data backing in this project. It is entirely knowledge-based.**

### 5.5 Trial-design note

The disease model `[DATA: §1081]` records that intravitreal plasma-kallikrein inhibition produced
mixed results, with benefit suggested in subgroups rather than all-comers, and concludes this
**argues for phenotype enrichment.** I take that seriously and build it in: any study should enrich
for the incomplete-anti-VEGF-responder phenotype, and ideally for a measurable contact-pathway
biomarker, rather than testing all-comers. I am not over-reading that line as support — it is a
caution, and I am treating it as one.

---

## 6. (f) FASTEST PATH TO PATIENTS

I apply the Clinical agent's lexicographic gate rather than an average: **(1)** can it engage its
target in the relevant compartment? **(2)** is the mechanism directionally right for a real unmet
need? **(3)** is chronic safety acceptable in a CKD-dominant polypharmacy population? **(4)** is
there a credible development path?

| Candidate | G1 engagement | G2 mechanism | G3 chronic safety | G4 path | Verdict |
|---|---|---|---|---|---|
| **Berotralstat** *(new)* | **PASS, cleanly** — plasma-compartment target, no barrier crossing | Right for need #2 | Acceptable; DDI + QT need work; **renally forgiving** | Approved oral; Phase 2 in enriched DME directly | **Best new candidate** |
| **Pemafibrate** | Partial — best Group A endothelial margin `[DATA: −1.6 to −0.2 log]`; hepatic limb certain | Largest apoC-III/remnant effect in the class = the *right particle* (§3.2) | **Best in class: no creatinine rise, biliary clearance, minimal statin-myopathy interaction** | Japan-only; global development needed | **Best incumbent on mechanism+safety** |
| **Fenofibric acid** | Hepatic PASS, retinal FAIL | Systemic limb, right stage S1–S3 | Creatinine rise (**and a functional unblinding hazard**), myopathy with statins | **Trivial** — generic, global, decades of diabetic exposure | **Best incumbent on feasibility** |
| **Inclisiran** *(new)* | PASS trivially (hepatic) | apoB limb at 3–5× fibrate magnitude | **Outstanding**; no renal adjustment, no DDI | Approved; **twice-yearly SC** | **Best drug if the apoB limb is real** |
| **Olezarsen** *(new)* | PASS trivially | The matched apoC-III probe (§3.3) | Good | Approved but FCS-restricted, costly | **Best mechanism-discriminating arm** |
| **Candesartan cilexetil** | PASS (systemic RAS; local retinal RAS plausible) | Modest but directionally right; **zero PPAR confound** | **Excellent**; already indicated for this population's comorbidities | **Trivial** — generic | Underrated on feasibility; BP-lowering confound |
| **Elafibranor** | Best Group A margin `[DATA: −0.7 to +0.4 log]` | Confounded by δ co-agonism | **Michael-acceptor enone at 120 mg/day for life**; 2 years of market history | Approved 2024 | Probe only, not a therapy |

### 6.1 Recommendation, split by which limb is being developed

Collapsing these into one ranking would repeat the averaging error Round 1 warned about. The honest
answer is three answers:

1. **For unmet need #2 (non-VEGF permeability in incomplete-responder DME): BEROTRALSTAT.** Oral,
   approved, licensed for chronic prophylaxis, plasma-compartment target that makes the exposure
   problem disappear, renally forgiving, and **completely orthogonal to the PPARα question** — so
   it de-risks the portfolio rather than doubling down on it. This is my single strongest new
   nomination.
2. **For unmet need #1/#5 (oral, deployable, S1–S3 systemic lipid limb): PEMAFIBRATE on mechanism
   and safety; FENOFIBRIC ACID if cost and global access dominate.** I am **not displacing the
   Round 1 leaders** — I am sharpening why they lead. Pemafibrate's much-criticised hepatoselectivity
   is **not a discriminating demerit**, because §1 establishes that no fibrate can test the retinal
   limb anyway; meanwhile its creatinine-neutral, biliary-cleared profile is a genuine advantage in
   a population where renal impairment is the norm and where a creatinine rise is additionally a
   *functional unblinding hazard*. Against it: §4's hepatic-ANGPTL4 concern is **worst** for the
   most hepatoselective agent.
3. **For resolving whether the mechanism is apoB at all: INCLISIRAN (therapeutic) + OLEZARSEN
   (control).** This is how the programme stops arguing and finds out.

### 6.2 What I could not deliver

**Nothing I found serves the retina-intrinsic PPARα hypothesis.** I searched approved space,
late-stage space, discontinued space, endogenous ligand space, and retinal-delivery space. The
molecule does not exist. Round 1's structural conclusion stands, and I am reinforcing it from an
independent direction.

---

## 7. (g) WHAT THE PROJECT DATA CAN AND CANNOT SUPPORT

**This search is knowledge-based. I want that stated without hedging.**

### 7.1 Verified data limits

| Check | Result |
|---|---|
| `chembl_drug_mechanisms.csv` | **11 rows total**; `grep -ic PPAR` → **0** |
| `chembl_drug_targets.csv` | **44 rows**; PPAR content → **0** |
| `chembl_drug_indications.csv` | **80 rows**; PPAR content → **0** |
| `chembl_bioactivities.csv` | PPAR content → **0** |
| `chembl_approved_drugs.csv` | 3,276 rows. `logd`, `cx_logd`, `permeability`, `molecular_species`, `bioavailability_score` → **0/3,276 filled, every one** |
| `molecule_type` distribution | **3,276/3,276 "Small molecule"** |
| 16 canonical candidates in `compound-dr-target-matrix.tsv` | **5 of 16**, all natural products (quercetin, melatonin, linoleic acid, linalool, α-linolenic acid) |
| KLKB1 in all project interaction data | **2 rows**, both CTD mRNA-expression from toxicants |
| ANGPTL4 / APOC3 rows | 9 / 7, **all CTD expression-level**, and contaminated by the known curation defects (sucrose, D-fructose) |

### 7.2 The consequence that matters most for *this* report

**The dataset contains no biologics at all** — 3,276 of 3,276 rows are small molecules. Every
large-molecule and oligonucleotide agent I assess in §3 and §5 (PCSK9 mAbs, inclisiran, olezarsen,
evinacumab, lanadelumab, garadacimab) is **structurally absent from the dataset**. I want to be
precise about what that means: **this is a scope limitation of the ChEMBL extract, not a blinding
artifact, and I am not treating their absence as information of any kind.** I did not infer anything
from any absence, and I did not attempt to determine what was redacted.

**Net: zero of my substantive conclusions are data-backed.** The data supported exactly three
things — that berotralstat, bempedoic acid and ezetimibe exist as approved small molecules with the
physicochemical profiles I quote; that the fibrate-series descriptor progression the Medicinal
Chemist described is real `[DATA: ppar-class-drug-properties.tsv]`; and that the KLKB1/ANGPTL4/APOC3
axes have no usable coverage in this project.

### 7.3 What data would make this data-backed

1. **A full ChEMBL bioactivity pull on PPARA (CHEMBL239), PPARD (CHEMBL3979), PPARG (CHEMBL235)**
   with pChEMBL values. This would convert §1's central claim from assertion to measurement: I could
   enumerate every annotated PPARα ligand, compute the fraction carrying an ionisable acid, and
   state the non-acidic set exhaustively rather than from recall. **This is the single highest-value
   data acquisition for this run** and it is a straightforward scraper target given the project's
   existing ChEMBL module.
2. **Populate `cx_logd` (pH 7.4) and `molecular_species`.** Both columns already exist in the schema
   and are 100% empty. ChEMBL serves them directly. They would immediately partition the entire
   3,276-drug table into ACID / BASE / NEUTRAL / ZWITTERION — which is precisely the axis this whole
   analysis turns on, and would let a *query* rather than my memory identify neutral PPAR-adjacent
   chemotypes.
3. **A ChEMBL target pull on KLKB1 (CHEMBL3286), F12, BDKRB1, BDKRB2** to give the kallikrein
   nomination any data footing at all.
4. **Expand the 27-gene DR panel.** It currently contains all three PPAR receptors and **zero PPAR
   effector genes**, so the pathway this run is about is invisible to the run's own data. It needs
   ANGPTL4, CPT1A, ACOX1, HMGCS2, APOC3, APOA5, LPL, FGF21 — and, for §5, KLKB1, F12, BDKRB1/2.
5. **A retinal-penetration reference set** — drugs with measured vitreous:plasma or retina:plasma
   ratios — to fit a local permeability model. Nothing of the kind exists in this project, and
   §2 was conducted entirely from recall as a result. This is the gap that most limits the whole run.

---

## 8. CROSS-CUTTING OBSERVATIONS

1. **The search instruction contained its own answer.** Being told to search drug space for a
   non-acidic PPARα ligand and finding none, across approved, late-stage and discontinued space, is
   a *result*, not a failure. It converts Round 1's structural argument from a chemistry prediction
   into an empirical observation about the entire developed pharmacopoeia.
2. **The productive move was changing which term to attack.** Six Round 1 agents attacked `Kp,uu`
   from six directions and all reached the same wall. §5 wins by choosing a mechanism whose target
   is already in plasma, so the term never enters. **Future candidate generation in this programme
   should screen on "where does the pathogenic protein live?" before screening on potency.**
3. **The PPAR class carries a regulatory graveyard that is rarely stated plainly** (§1.2), and every
   terminating toxicity in it — oedema, heart failure, creatinine rise, fracture — is one this
   particular population tolerates worst.
4. **Round 1's biggest remaining vulnerability is now fixable.** §5 of the synthesis said no matched
   non-PPAR remnant-lowering agent existed. One does. The run should take the correction.
5. **A particle-level, not mass-level, framing of the lipid hypothesis is what keeps it alive.**
   State it that way or a reviewer will reach for PCSK9 and win the argument in one sentence.

**Biggest concern:** that the programme proceeds with fenofibrate because it is cheap, generates an
ambiguous result, and burns the hypothesis. §1 shows a negative fibrate result is irreducibly
ambiguous; §3.3 shows how to design a study that is not.

**Question for other agents** — *to the Safety Pharmacologist and SAR Analyst:* berotralstat
inhibits CYP2D6 and CYP3A4 and prolongs QT at supratherapeutic exposure. Against the concomitant
classes in brief §5 — metformin, sulfonylureas, insulin, statins, RAS blockers, antiplatelets,
diuretics — is that DDI profile manageable with ordinary labelling, or is it a programme-level
obstacle? And to the SAR Analyst specifically: §1.4 establishes that PPARα AF-2 engagement does not
require a permanent anion (the N-acylethanolamides prove it). Does the ethanolamide head generalise
to a synthetic, FAAH-resistant scaffold?

---

## 9. BLINDING COMPLIANCE

**Files read.** `disease-brief.md`; `round1-synthesis.md`; `.claude/skills/drug-repurposing-
strategist/SKILL.md`; `evidence/ppar-class-drug-properties.tsv`; `evidence/compound-dr-target-
matrix.tsv` (header and first column only); targeted greps of `disease-model.md` (kallikrein,
ANGPTL, lines 355–382, 1081) and `agents/p1-admet.md` (exposure blocks); and, under
`data/processed-blinded-diabetic-retinopathy/` only: `chembl_approved_drugs.csv`,
`chembl_drug_mechanisms.csv`, `chembl_drug_targets.csv`, `chembl_drug_indications.csv`,
`chembl_bioactivities.csv`, `pubchem_phytochem_target_interactions.csv`.

**I did not read** `data/processed/chembl_approved_drugs.csv`, anything under `data/holdout/`, any
`answer-key*` file, or git history/objects. I saw no `[REDACTED-HOLDOUT]` markers. I made no attempt
to determine which rows or fields were redacted, and I did not reason by elimination from any
absence — including the dataset's complete absence of biologics, which I explicitly attribute to
extract scope (3,276/3,276 small molecules) rather than to blinding (§7.2).

**Disclosures — made honestly, including negative decisions.**

1. **Kallikrein (§5) — my most significant disclosure.** The brief itself named the HAE
   armamentarium and directed me to assess it, and `disease-model.md` §1081 records that
   *intravitreal* plasma kallikrein inhibition has been attempted with mixed, subgroup-dependent
   results. So the axis was handed to me, not recalled by me. I am nonetheless aware in general terms
   that ocular kallikrein programmes have existed. **My case for berotralstat rests on four things
   and none of them is DR evidence:** that the pathogenic protein is plasma-resident so `Kp,uu`
   drops out of the exposure equation; that its licensed use is chronic oral outpatient prophylaxis;
   that it is not primarily renally cleared; and that contact-pathway inhibition does not cause
   bleeding. That argument stands with the DR literature entirely removed. I have also used §1081
   only as a *caution* (arguing for phenotype enrichment), never as support.
2. **Candidates I did NOT propose, and why — stated because negative decisions can leak information
   as easily as positive ones.** I considered and rejected on blinding-clean grounds: **topical/
   ocular reformulation** of any systemic agent (brief §4 states a strong prior against topical
   delivery to a posterior-segment target); **intravitreal reformulation** generally (it fails
   unmet needs #1, #4 and #8 by construction); **bexarotene** (hypertriglyceridaemia and central
   hypothyroidism, §2.3); **aprotinin** (withdrawn for mortality); **aleglitazar, muraglitazar,
   tesaglitazar** (discontinued for the toxicities named in §1.2). Each rejection is on general
   pharmacology, formulation science, or publicly-known non-DR discontinuation reasons.
3. **No candidate in this report occurred to me because of DR evidence.** The two new nominations
   arose from explicit structural reasoning — berotralstat from the `Kp,uu`-elimination argument in
   §5.1, olezarsen from asking "what is the downstream node through which PPARα lowers remnants, and
   is there a drug that hits it directly?" in §3.3. Neither required, used, or was influenced by any
   DR or DME clinical fact.
4. **I used only non-DR indication knowledge throughout**, as permitted: HAE prophylaxis, FCS,
   dyslipidaemia, MASH, T2D, CTCL, HoFH, and the publicly documented reasons for the PPAR-class
   discontinuations.
5. **Residual limitation, same as Round 1 §10:** dataset blinding removes the project's data signal,
   not my pretrained pharmacology. A search over approved drug space is *intrinsically* a search
   over knowledge rather than over this dataset — §7 quantifies exactly how little of this report the
   project data could support. The scoring step should read my scores as mechanistic-path
   plausibility under data blinding, not as naive rediscovery.

---

## SCOREBLOCK
SCORE|Fenofibric acid|6|moderate|knowledge-based|Trivial feasibility, defensible systemic limb; retinal engagement fails; creatinine, myopathy
SCORE|Fenofibrate|5|moderate|mixed|Dominated by its own active metabolite; adds food-effect variability, no offsetting benefit
SCORE|Pemafibrate|7|moderate|knowledge-based|Best remnant/apoC-III effect and CKD safety; hepatoselectivity non-discriminating since no fibrate tests retina
SCORE|Elafibranor|4|moderate|mixed|Best exposure margin but Michael-acceptor enone lifelong, delta confound, minimal market history
SCORE|Seladelpar|2|moderate|knowledge-based|Confounded control, PPARdelta carcinogenicity question, minimal chronic database, no therapeutic rationale
SCORE|Linoleic acid|1|high|data-backed|Dietary nutrient, not dose-movable, no regulatory vehicle, no repositioning path exists
SCORE|Alpha-linolenic acid|2|high|data-backed|Same; plasma already at own EC50, so not dose-movable as intervention
SCORE|Linalool|1|moderate|data-backed|Fragrance compound; no chronic dosing precedent, no formulation, no meaningful potency
SCORE|Icosapent ethyl|5|moderate|mixed|Real oral drug riding retinal lipid route; weak non-selective PPARalpha; AF and bleeding signal
SCORE|Quercetin|1|high|data-backed|Sub-2% bioavailability, dual efflux substrate, SLCO1B1 inhibitor DDI with background statins
SCORE|Melatonin|4|moderate|mixed|OTC, safe, crosses BRB freely; negligible PPARalpha potency; adjunct not receptor test
SCORE|Epalrestat|2|moderate|knowledge-based|Good engagement, wrong target; mechanism carries negative human clinical validation
SCORE|Dimethyl fumarate|4|moderate|knowledge-based|Covalent mechanism escapes free-drug arithmetic; PML, lymphopenia, mandatory monitoring disqualify asymptomatic prophylaxis
SCORE|Minocycline|4|moderate|knowledge-based|Genuinely reaches retina, oral generic; chronic tetracycline toxicity and resistance hard to justify lifelong
SCORE|Candesartan cilexetil|6|moderate|knowledge-based|Oral generic already indicated in this population; zero PPAR confound; modest mechanism, BP confound
SCORE|Ezetimibe|5|moderate|knowledge-based|Cheap safe oral control but wrong particle; null result cannot discriminate receptor from lipid
SCORE|Berotralstat|7|moderate|knowledge-based|Oral approved chronic prophylaxis; plasma-resident target eliminates Kp,uu; renally forgiving; DDI and cost
SCORE|Olezarsen|5|moderate|knowledge-based|Matched non-PPAR apoC-III remnant control Round 1 said did not exist; probe not therapy
SCORE|Inclisiran|6|moderate|knowledge-based|Twice-yearly apoB lowering far exceeding fibrates, superb safety; wrong particle, cost
SCORE|Lanadelumab|5|moderate|knowledge-based|Same plasma-kallikrein logic, superb chronic safety, no DDI; biologic cost and injection burden
SCORE|Evolocumab|5|moderate|knowledge-based|Largest apoB reduction available; q2w injection burden poor for asymptomatic prophylaxis; wrong particle
SCORE|Bempedoic acid|4|moderate|mixed|Oral apoB lowering, zero PPAR; wrong particle, raises urate causing gout, tendon rupture
SCORE|Palmitoylethanolamide|4|low|knowledge-based|Only non-acidic PPARalpha agonist humans can actually take; FAAH clearance likely prevents sustained engagement
SCORE|Oleoylethanolamide|3|low|knowledge-based|More potent than PEA at PPARalpha but faster clearance, worse supply and formulation
SCORE|Doxycycline|4|low|knowledge-based|Reaches retina, chronic sub-antimicrobial dosing approved, MMP9 inhibition; no PPARalpha activity
SCORE|Lanifibranor|3|low|knowledge-based|Possibly non-acidic chemotype but pan-PPAR gamma oedema and weight gain disqualifying here
SCORE|Saroglitazar|3|low|knowledge-based|Approved India but acidic chemotype gives no escape; PPARgamma oedema risk
SCORE|Evinacumab|2|moderate|knowledge-based|IV monthly, HoFH-restricted, extreme cost; ANGPTL3 better served by siRNA
SCORE|Bexarotene|1|moderate|knowledge-based|Elegant RXR route to PPARalpha heterodimer; severe hypertriglyceridaemia opposes the systemic limb
