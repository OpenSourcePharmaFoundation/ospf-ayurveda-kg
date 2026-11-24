# Benchmark Result — Blinded Rediscovery Test, Diabetic Retinopathy
Run date 2026-10-05 · Unblinded by the Phase 2 Literature Reviewer's Part B

**This is the deliverable the holdout was built for.** The pipeline ran without access to
which drugs are already used for diabetic retinopathy. This document compares what it
concluded against what is actually true.

---

## 1. THE HELD-OUT ANSWER

**Fenofibrate is an approved, guideline-recognised therapy for diabetic retinopathy.**

| Study | Design | n | Key result |
|---|---|---|---|
| **FIELD** (2007) | RCT, fenofibrate vs placebo | 9,795 | First laser for DR 3.4% vs 4.9%; HR **0.69** (0.56-0.84), p=0.0002 |
| **FIELD ophthalmology substudy** | ETDRS-graded photography | 1,012 | 2-step progression overall **NS**. **With pre-existing retinopathy: 3.1% vs 14.6%, p=0.004.** Without: no effect |
| **ACCORD-Eye** (2010) | fenofibrate + simvastatin vs simvastatin | 1,593 | >=3-step progression/laser/vitrectomy at 4y: 6.5% vs 10.2%; OR **0.60** (0.42-0.87), p=0.006 |
| **LENS** (2024) | RCT, early disease (non-referable at baseline) | 1,151 | Progression to referable DR: 22.7% vs 29.2%, HR **0.73**. Incident macular edema 3.8% vs 7.5%, HR **0.50** |
| **ACCORDION Eye** (2016) | Observational follow-on | — | At 8y after stopping: 11.8% vs 10.2%, **NS — no legacy effect** |

**Regulatory:** Approved in Australia (TGA, Oct 2013) for *"reduction in the progression of
diabetic retinopathy in patients with Type 2 diabetes and **existing** diabetic
retinopathy."* Not approved for DR by FDA or EMA. **ADA Standards of Care 2026 §12:**
progression "may be slowed by the addition of fenofibrate, particularly with **early**
diabetic retinopathy at baseline."

**Still open:** DRCR Protocol AF (fenofibrate vs placebo, ~560 patients, mild-to-moderate
NPDR) is ongoing and is the definitive US trial.

---

## 2. SCORECARD

| Question | Verdict |
|---|---|
| **Right compound?** | **YES.** Fenofibrate/fenofibric acid at the top of the Round 1 consensus matrix |
| **Right stage-dependence?** | **YES, emphatically.** The pipeline independently corrected its own brief from preclinical (S0) to mild-moderate (S1-S2) on mechanistic grounds — matching the FIELD subgroup, the LENS enrolment criterion, the TGA label wording and the ADA qualifier |
| **Right phenotype enrichment?** | **PARTIALLY.** The exudative/lipid phenotype, the treatment window, prevention-over-clearance and the incident-edema endpoint are all corroborated. The proposed *lipid-level entry gate* is contradicted |
| **Right mechanism?** | **NO.** The pipeline converged on systemic lipoprotein lowering. The human evidence most clearly excludes exactly that |

> ### ⚠ VALIDITY WARNING — read before using the Phase 3 metrics
>
> **The final Phase 3 ranking is NOT a clean blinded result.** The agent that produced it had
> read `data-quality-findings.md` §17b, which — in the course of *documenting* a blinding
> breach — described what the leaked headings said: that some candidate in the set is an
> established approved therapy for this indication, and that the pipeline's mechanism
> conclusion was wrong. I wrote that description, and I instructed the ranker to read that
> file as binding. **The incident report became a wider leak than the incident.** See
> findings §19.
>
> **The clean measurement is the Round 1 consensus ranking**, produced and scored before that
> entry existed: **P@1 = 1.00, first tier-1 hit at rank 1.**
>
> The Phase 3 figures below are reported for completeness and because the ranker disclosed
> the contamination itself. Its two leader-affecting moves are independently checkable and do
> not depend on the leak — the pemafibrate demotion rests on that drug's own cardiovascular
> outcome record (non-DR, permitted), and the elafibranor reinstatement is re-derived
> arithmetic I verified separately against `p1-admet.md` §3.2. The ranker also states it knew
> only *that* an approved therapy existed in the set, not *which*.

### Formal rediscovery metrics — FINAL Phase 3 ranking vs the redacted key (SEE WARNING ABOVE)

```
P@1   1.00     first tier-1 hit at rank  1
P@3   1.00     all three top picks are in the answer key
P@5   0.60
P@10  0.30
strict (no active-moiety credit): 4 hits, 3 tier-1, first at rank 2
```

| Rank | Predicted | Matches key entry | Tier |
|---|---|---|---|
| **1** | **Fenofibric acid** | FENOFIBRATE (active moiety) | 1 |
| **2** | **Pemafibrate** | PEMAFIBRATE | 1 |
| **3** | **Fenofibrate** | FENOFIBRATE | 1 |
| 15 | Doxycycline | DOXYCYCLINE | 1 |
| 26 | Minocycline | MINOCYCLINE | 2 |

**The final ranking is better than Round 1's.** Round 1 tied pemafibrate and fenofibric acid
at the top; the Phase 3 ranker demoted pemafibrate on falsification grounds and promoted
fenofibric acid to sole first place — which is the correct answer. The demotion was argued
from pemafibrate's own hard-endpoint record in a near-identical population, **not** from any
retinopathy knowledge.

### Earlier metrics (Round 1 consensus ranking vs the redacted key)

```
P@1  1.00      first tier-1 hit at rank  1
P@3  0.667     tier-1 hit within top 1   YES
P@5  0.600     tier-1 hit within top 3   YES
P@10 0.400
```
Hits: Pemafibrate (#1), Fenofibric acid (#2, active-moiety equivalent to the key's
FENOFIBRATE), Fenofibrate (#4), Minocycline (#10, tier 2).

**Scoring caveat recorded:** the key is derived from ChEMBL indication tags, which marked
only CHEMBL672 FENOFIBRATE. Fenofibric acid (the circulating active moiety) and choline
fenofibrate (its salt) were untagged and would have scored as misses. The scorer now
applies an explicit active-moiety equivalence and reports strict and moiety-aware figures
separately. **Pemafibrate at #1 is not creditable as a hit on the clinical merits** — see §4.

---

## 3. WHAT THE PIPELINE GOT RIGHT, BLIND

1. **The compound class.** With DR indications stripped from the data, the Phase 0 scout
   derived the fibrates from PPARα ligand pharmacology and the blinded structural data alone.
2. **The stage restriction** — and this is the most impressive result. The brief handed it
   "disease-modifying therapy for early (S0-S2) DR" as unmet need #1. The Disease Biology
   agent *rejected* the S0 half on mechanistic grounds: with an intact barrier there is no
   extravasation to prevent, so the supply-lowering limb is mechanically inoperative. It
   concluded the honest target is **S1-S2**. The TGA label says "existing diabetic
   retinopathy"; the FIELD substudy found benefit **only** in patients with retinopathy at
   baseline and none in those without.
3. **The incident-edema endpoint.** The pipeline nominated prevention of macular edema over
   clearance of established edema. LENS's strongest single result is incident macular edema,
   HR 0.50.
4. **Epalrestat and the aldose-reductase class** — correctly scored near-bottom on a
   falsified target. Confirmed: the class failed in DR.
5. **The natural products.** Quercetin last at 1.92 with the tightest agreement in the
   matrix. There is no DR clinical evidence of any kind for quercetin, linalool, linoleic
   acid or alpha-linolenic acid. The rejection is correct and uncontroversial.
6. **FGF21 as a humoral relay** — proposed by the Target Analyst and independently graded
   strongest by the Literature Reviewer's blinded Part A. Published work the pipeline never
   saw shows pemafibrate prevents retinal pathological neovascularization **specifically by
   increasing FGF21**.
7. **ANGPTL4 demoted rather than treated as fatal.** Three agents argued it down. The
   literature goes further: fibrate exposure moves the ANGPTL axis in the *protective*
   direction, via ANGPTL3 inhibition. The pipeline was directionally right and still
   understated it.

---

## 4. WHAT IT GOT WRONG — and the diagnosis is the valuable part

### 4.1 The mechanism, which the run's best analysis actively drove it away from

The clinical evidence indicates the benefit is **not** lipid-mediated:
- FIELD: benefit not predicted by, nor proportional to, baseline or on-treatment lipids.
- ACCORD-Eye: the comparator arm was a statin; fenofibrate added a 40% relative reduction
  **on top of** LDL lowering.
- **LENS, decisively: in the renal-impairment subgroup on alternate-day dosing, fenofibrate
  changed no lipid parameter versus placebo — and ocular benefit still emerged.**

The pipeline concluded the opposite. Four agents converged on systemic lipoprotein lowering
as the exposure-defensible limb, and the Literature Reviewer's own blinded Part A ranked it
strongest by a wide margin.

**Precision about what this does and does not falsify.** The run never concluded fenofibrate
would fail. It concluded *retinal PPARα engagement is not why it works*. That narrower claim
is **still partly live** — the literature itself reports fenofibrate effects on human retinal
endothelial cells that are PPARα-**independent**. The true answer appears to be an
intraocular effect that is neither systemic-lipid-mediated nor cleanly PPARα-mediated.
**That third option was never enumerated by any agent.**

### 4.2 The root cause — a methodological bias, not an execution error

The Literature Reviewer's diagnosis, which generalises well beyond this run:

> **Evidence-hierarchy grading systematically rewards the limb whose intermediate steps are
> easiest to measure.** Hepatic engagement, plasma apoB and plasma FGF21 are all measurable
> in humans, so that chain accumulates high-level citations. Retinal drug concentration and
> retinal receptor occupancy are not measurable, so that chain can only ever accumulate
> low-level citations **no matter how true it is.** The hierarchy measured tractability of
> measurement and reported it as strength of evidence.

This will recur for **any** target in a hard-to-sample compartment — brain, eye, testis,
placenta.

**Recommended fix:** normalise each limb's evidence level against the best level that limb
could *possibly* attain given current measurement technology, and report raw and normalised
grades. A Level-4 claim in a compartment where Level-4 is the ceiling is not weaker than a
Level-2b claim where Level-1a is routine. This single change would have flipped the verdict.

### 4.3 The exposure objection organised the run and pointed the wrong way

The scout's ~2-log argument, the chemist's `occupancy ∝ fu × C × Kp,uu / EC50` analysis and
the conclusion that *"no molecule in the fibrate class can test the retina-intrinsic PPARα
hypothesis"* together predict an oral fibrate should produce no retinal pharmacological
effect. **An oral fibrate produces one, repeatedly, in three randomised trials.** The
arithmetic may still be right about PPARα occupancy specifically, but as a predictor of
clinical outcome it failed — and it consumed the run's best analytic effort.

### 4.4 My control design was under-specified — an orchestrator error

I added ezetimibe to discriminate receptor action from lipid lowering, and wrote only the
positive branch: *"if a matched apoB-lowering non-PPAR agent produces the same retinal
benefit, the receptor is not what is doing the work."* **I never wrote down what a null
means.** Given §4.1, ezetimibe would almost certainly return a null, and the natural unstated
reading — "lipid lowering is irrelevant, therefore it must be the receptor" — is wrong in its
final step, because the alternative to lipid lowering is not necessarily receptor engagement.

**Rule adopted:** every control must have *both* branches of its inference written down
before it is run.

### 4.5 Pemafibrate ranked #1 and is simply unknown

PROMINENT-Eye (DRCR Protocol AD) was **terminated for failure to recruit**; the parent
cardiovascular trial was null. There is no human DR result for pemafibrate. Ranking an
untested compound first is not a miss, but it is not a hit — **a rediscovery metric must not
credit it.** The pipeline's own clinical agent independently scored it down to 5 for
deployment reasons (Japan-only approval, branded pricing), which was the better instinct.

### 4.6 Durability was never considered by any agent

ACCORDION shows the benefit **does not persist after discontinuation**, unlike the glycemic
legacy effect. No agent asked whether the mechanism would be disease-modifying or merely
suppressive. For a lifelong oral therapy in asymptomatic people this is first-order: it
decides whether the product is a four-year course or a forty-year one, and it changes the
entire chronic-safety calculation.

### 4.7 Cheapness was scored as merit

The Clinical agent's high marks for fenofibric acid rested partly on cost and generic
availability. The Literature Reviewer's rebuke is correct: **that is a feasibility fact
carrying zero efficacy information**, and the configuration of "defined mechanism, abundant
animal data, good tissue penetration, cheap generic" describes **minocycline**, which failed
repeatedly in humans including one trial showing harm.

---

## 5. WHAT THIS BENCHMARK ACTUALLY MEASURED

**Not naive rediscovery, and by the end not fully blinded either.** Dataset blinding removed
the project's data signal; it cannot remove the model's pretrained knowledge. And in this run
the blind degraded over time through three successive leaks of the same class — redaction
markers, an in-file section boundary, and finally the incident report describing the breach
(findings §17b, §19). **Phase 0 and Round 1 were cleanly blinded. The debate round had one
partially-contaminated agent, which quarantined its own affected section. Phase 3 was not
cleanly blinded.** Benchmark claims must be scoped to the phase that produced them. The Literature Reviewer disclosed this directly,
noting it could not fully exclude that knowing the clinical outcome nudged one Part A grade
upward, and declining to artificially deflate it on the grounds that a deliberate downward
correction would be equally contaminated. That is the correct epistemic response and also
direct evidence of the contamination.

**What it did measure, and measured well:** whether a multi-agent pipeline reasoning from
mechanism, structure and pharmacology — with the answer removed from its data — reaches the
right compound, the right stage and the right endpoint. **It did, on all three.**

**The most valuable output is the contradiction, not the ranking.** A rigorous, well-executed
blinded analysis converged confidently on the wrong mechanism, and the reason is a structural
bias in evidence-hierarchy grading that will recur in every future run against a
hard-to-sample compartment. A benchmark that only reported "P@1 = 1.00" would have concealed
that entirely.

---

## 6. ADDENDUM — a late blinded finding that moved TOWARD the truth

Recorded after the Phase 2 SAR Analyst reported, and it changes the scorecard's texture.

Round 1's organising structural claim was that PPARα **requires** an acidic head, that the
acid is what both albumin and the hepatic uptake transporters recognise, and therefore that
potency and retinal access are anti-correlated by construction — making the retina-intrinsic
hypothesis permanently untestable with any fibrate.

**The SAR Analyst, still blind, refuted that premise.** Its argument:

- The AF-2 cage is **all-donor** — Ser280, Tyr314, His440 and Tyr464 each donate a hydrogen
  bond. The ligand supplies only **acceptors**. The geometry therefore demands a bidentate
  acceptor pair roughly 2.2-3.2 Å apart, **not a formal negative charge.**
- Charge is an acceptor-strength multiplier, not a requirement. Going neutral costs roughly
  2.3-3.1 kcal/mol per contact — real, bounded, and affordable.
- **Changing the unit of measurement inverts the Round 1 conclusion.** Measured in ligand
  efficiency rather than raw potency, the neutral endogenous ligand oleoylethanolamide
  (LE 0.41) is a *more* atom-efficient binder than fenofibric acid (0.29) or pemafibrate
  (0.34). The neutral head pays no efficiency penalty.
- Tetrazole, the reflexive carboxylate bioisostere, is a false friend — it remains a full
  OATP1B substrate, which is why the sartans are hepatically taken up.

**Why this matters for the benchmark.** The unblinded evidence says fenofibrate's benefit is
**intraocular and largely lipid-independent**. Round 1 argued its way to the opposite
conclusion partly on the strength of the "acid is mandatory, so retinal engagement is
impossible" claim. The SAR agent dismantled that claim without ever seeing the answer key.

> **The pipeline's last blinded analytical act moved it back toward the correct answer.**
> Had the SAR finding arrived in Round 1 rather than Round 2, the mechanism verdict might
> not have gone the way it did. This is evidence that the mechanism error was a
> *sequencing* artifact as much as a reasoning one — the structural claim that foreclosed
> the retinal limb went unchallenged for two rounds because no agent with the right
> expertise was asked about it until Phase 2.

**Process lesson:** the agent best placed to falsify a load-bearing claim should be
scheduled in the same round that the claim is made, not a round later. The pipeline
generated its own refutation one round too late to act on it.

---

## 7. ADDENDUM 2 — the debate round partially self-corrected the mechanism error

The Integration Specialist, **still blind**, rejected the framing that produced the error.

> **"Not either/or — the dichotomy is itself the error. It assumes a drug affects a tissue
> only by entering it."**

Round 1 posed the question as *hepatic/systemic lipoprotein lowering **versus** retinal
receptor engagement*, and the whole mechanism verdict followed from that binary. The
Integrator dissolved it, ranking four limbs by evidence × engagement certainty:

1. Hepatic PPARα → APOC3 down / LPL up → remnant and apoB particle number down.
   **Certain engagement, human pharmacodynamic evidence.**
2. Hepatic PPARα → **FGF21 up** → FGFR1c/β-Klotho receptors on retinal endothelium
   **from the luminal side**. Upstream human-proven, downstream animal-proven by
   laboratories with no stake in the PPARα-retina literature, and **no barrier crossing at
   any point.**
3. Endothelial transrepression → ICAM1 down. Low-level evidence with high-quality negative
   class precedent.
4. Retinal fatty-acid-oxidation transactivation. Absent at achievable occupancy.

**Its formulation of limbs 1-2: *systemic in pharmacokinetics, retinal in pharmacology.***
The liver is a legitimate site of action **on** the retina. This is not the lipid-lowering
hypothesis the unblinded evidence rejects, and it is not the retinal-occupancy hypothesis the
arithmetic rejects. **It is the third option §4.1 said no agent had enumerated — and the
debate round enumerated it, blind, one phase later.**

**The corroboration is direct and the pipeline never saw it.** Published work shows
pemafibrate prevents retinal pathological neovascularization **specifically by increasing
FGF21**. The Integrator ranked the FGF21 relay as the second-strongest limb, and the
Literature Reviewer's blinded Part A independently graded it strongest, on the reasoning that
its downstream evidence comes from laboratories independent of the lineage that produced the
PPARα-retina claims.

**Revised scorecard line for "Did it identify the mechanism?"**

> **Round 1: NO** — converged on systemic lipid lowering, which the human evidence most
> clearly excludes.
> **Debate round: PARTIALLY YES** — identified a humoral hepatic-to-retinal relay that is
> neither lipid-mediated nor dependent on retinal receptor occupancy, and which published
> work corroborates. **The pipeline reached the right neighbourhood on its last blinded
> move, two phases after it needed to.**

### Two further blind arguments that the answer key supports

- **The ANGPTL4 ceiling.** ANGPTL4 inhibits lipoprotein lipase, so a functionally meaningful
  induction predicts triglycerides to *rise*. Observed triglycerides *fall*. Real-world
  induction is therefore bounded above by an already-measured quantity. The Integrator and
  the Literature Reviewer produced this independently. The unblinded evidence goes further —
  fibrate exposure moves the ANGPTL axis in the *protective* direction via ANGPTL3.
- **The CKD amputation argument**, which no agent had made before and which the answer key
  makes newly important: the systemic limb is transporter-concentrative and saturable, the
  retinal limb is passive and linear in free plasma. **Renal dose-banding therefore
  selectively removes the retinal limb while sparing the systemic one — in precisely the
  patients with the most retinopathy**, since nephropathy and retinopathy track together.
  Note that LENS dosed alternate-day in renal impairment and **still saw ocular benefit with
  no lipid change at all** — which, read against this argument, is evidence *against* the
  retinal-occupancy limb and *for* a humoral relay that survives dose reduction.

**Design rule the Integrator derived, which survives unblinding intact:**
*build nothing that requires retinal partitioning above 0.2; build something that is
invariant to retinal partitioning of zero.*

---

## 8. ADDENDUM 3 — the final ranker caught an error of the same class it had caught in Phase 1

The Candidate Ranker role was reassigned to the Phase 1 Traditional Medicine agent after
agent spawning hit a system limit. It was chosen because it had the run's most disciplined
quantitative method — it ran null models rather than asserting, did dose arithmetic rather
than estimating — and because it had **no stake in the PPARα question**, having returned nine
not-assessable scores.

It then applied its own Phase 1 method to the run's best-evidenced mechanism and found the
same error there:

> The FGF21 relay is credited as the second-strongest limb on the strength of (a) human
> pharmacodynamic data showing fibrates raise plasma FGF21 and (b) rodent studies showing
> FGF21 protects retinal vasculature. **Nobody checked whether those two concentrations are
> the same concentration.** The rodent work uses pharmacological recombinant FGF21; a fibrate
> produces a modest physiological rise in the endogenous hormone.

Its own words: *"structurally identical to the error I caught in Phase 1 with herbal fatty
acids — a real effect demonstrated at a dose the intervention cannot deliver."*

**This matters for the benchmark because the FGF21 relay is the limb the unblinded literature
supports** (published work shows pemafibrate prevents retinal neovascularization specifically
by increasing FGF21). The pipeline identified the right limb and then, on its final move,
identified the quantitative gap that would have to be closed to believe it. **Neither the
blinded pipeline nor the unblinded literature review closed it** — the Literature Reviewer
confirmed no published measurement bridges the two concentrations.

**That is arguably the single most useful output of this run:** not the ranking, but a
specific, checkable, unanswered question sitting under the mechanism that the real-world
evidence favours.

### Final process observation

The same methodological failure mode — *a real effect demonstrated at a dose the intervention
cannot deliver* — was caught three times in this run, by three different agents, in three
different contexts: herbal fatty acids (Phase 1), endogenous PPARα ligands already at their
own active concentration (Phase 2), and the FGF21 relay (Phase 3). **It is the characteristic
error of mechanism-first reasoning**, and a pipeline of this kind should test for it
explicitly at every stage rather than rediscovering it.
