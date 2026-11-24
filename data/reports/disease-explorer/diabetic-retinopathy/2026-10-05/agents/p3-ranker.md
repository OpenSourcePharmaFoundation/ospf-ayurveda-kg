# P3 — Final Candidate Ranking
## Diabetic Retinopathy (BLINDED RUN) · Candidate Ranker · 2026-10-05

**Reassignment note.** I wrote `p1-ethno.md` (Phase 1, Traditional Medicine). I returned 9 NAs
and scored my 6 assessable candidates 2–5. I have no position to defend in the PPARα question
and no candidate in the top tier that I previously advocated.

**Method.** Lexicographic gates, not a weighted mean. The MCDA skeleton of
`.claude/skills/candidate-ranker/SKILL.md` is retained; every dimension is re-anchored to DR and
the weighted-aggregation step (Step 4) is **replaced**, because averaging orthogonal axes is the
defect five agents in this run warned against and the orchestrator performed twice.

---

## 0. HEADLINE

**Three leader-affecting changes, each produced by a falsification rather than a reweighting:**

1. **Pemafibrate is demoted out of first place.** Its distinguishing claim — the largest
   apoC-III/remnant effect in the class, therefore "the right particle" — has had its nearest
   available hard-endpoint test in nearly this brief's population, and it **did not lower apoB
   particle number and produced no event benefit**. The run promoted a tolerability finding
   (Safety 7.0) into an efficacy ranking. §3 adjudicates and commits.

2. **Elafibranor is reinstated** as the designated mechanistic probe, and **seladelpar is
   upgraded** to a usable isoform falsification control. Both were scored down on reasoning that
   the run's own arithmetic contradicts. At the geometric midpoint of every declared range,
   endothelial occupancy is **elafibranor −0.14 log · pemafibrate −0.92 · fenofibric acid −2.07**
   — the same order as potency. Seladelpar sits at **+0.6 to +1.3** and candesartan at
   **+0.0 to +1.0**: the only two compounds in the set that *exceed* their free EC50 in the
   target compartment. I re-derived all of these from `p1-admet.md` §3.2 and §6.1 (§2.1).

3. **A new argument against the run's own #1-ranked mechanism.** Pemafibrate is the natural
   experiment for limb 1: maximal hepatic PPARα engagement, maximal apoC-III suppression,
   maximal remnant-TG lowering. If limb 1's causal chain were strong it should be the best drug
   in the class. It is not. The Devil's Advocate used this against pemafibrate; **it also bears
   against limb 1 itself**, which no agent in twelve has said (§5.1).

**And one new gap, found by applying my Phase 1 method to the run's best-evidenced limb.** The
FGF21 relay is credited as limb 2 on the strength of (a) human PD showing fibrates raise plasma
FGF21 and (b) rodent studies showing FGF21 protects retinal vasculature. **Nobody checked whether
those two concentrations are the same concentration.** The rodent work uses pharmacological
recombinant FGF21; a fibrate produces a modest physiological rise in the endogenous hormone.
This is structurally identical to the error I caught in Phase 1 with herbal fatty acids — a real
effect demonstrated at a dose the intervention cannot deliver. It is checkable from existing
published data with no new experiment, and the final report should not lean on limb 2 until it
is (§4.2, F5).

**Top pick: fenofibric acid, 6.5/10, moderate confidence, and it is a weak first.** Nothing in
this set reaches 7. §8 states what the report is entitled to claim, and it is less than a ranking.

---

## 1. SCORING ARCHITECTURE

### 1.1 Why not a weighted mean

Five agents instructed the orchestrator not to average (Round 1 §7; Clinical; Pathway §9;
SAR §10; Repurposing §6.1). The orchestrator averaged, twice, and the mean became the official
result. Three concrete defects follow, all verified:

- **n=1 rows sorted against n=5 rows.** Berotralstat (7.00) and inclisiran (6.00) top the Round 2
  table on one agent's score on one axis.
- **An axis its author excluded is load-bearing.** Remove the SAR column as SAR §10 instructs and
  pemafibrate goes 5.80 → 6.75, fenofibric acid 5.80 → 6.00. **The Round 2 "tie at the top" is
  manufactured by the averaging operation itself.**
- **Contradictions average into invisibility.** Pathway's 7.0 for fenofibric acid is explicitly
  conditioned on transrepression, which the Literature agent graded Level 5/6 LOW *in the same
  round*. The mean destroyed the conflict instead of surfacing it.

### 1.2 The gates

Applied in strict order. **Gates 1 and 2 set the tier. Gates 3 and 4 reorder within a tier and
can never move a candidate across a tier boundary.**

| Gate | Question | Effect |
|---|---|---|
| **G1 — EFFICACY EVIDENCE ANCHOR** | For the best limb this molecule can *actually engage*: what is the evidence grade × engagement certainty? Evidence grade per the Literature agent's hierarchy; engagement per the ADMET occupancy arithmetic. | **Sets the tier.** |
| **G2 — HARD VETO** | Is there a liability that is disqualifying for *this* deployment — lifelong, asymptomatic, CKD-dominant, universally statin-treated, in a trial measuring retinal endpoints? | **Floors the tier**, or restricts to "probe only." |
| **G3 — INTERPRETABILITY & DEPLOYABILITY** | Would a result with this molecule be assignable? Can it reach the population? | **Reorders within tier only.** |
| **G4 — HEADROOM** | Chemistry/formulation optionality. | **Reorders within tier only, smallest weight.** |

### 1.3 Binding constraints applied

- **No target-count scoring** (DQ §11). Only 5 of 16 candidates appear in the matrix, all natural
  products. I found the defect in Phase 1 and I do not use the metric here. Absence from the
  matrix is not evidence of inactivity.
- **No `alogp` as a permeability proxy** (DQ §12). Fenofibric acid reads 3.81; its logD at pH 7.4
  is ≈ −0.5. `logd` is empty for all 3,276 rows. I use explicit ionisation state and the ADMET
  agent's labelled estimates, and I label them knowledge-based.
- **Cheapness carries zero efficacy information** (Lit A5.3 rule 4). Generic status, once-daily
  dosing and a 30-year chronic database enter at **G3 only**. They break a within-tier tie. They
  never promote a candidate into a tier. This specifically constrains my fenofibric acid call and
  I say below exactly where it is and is not doing work.
- **Minocycline is the governing prior.** "Defined mechanism, abundant animal data, good
  penetration, cheap generic" is not a profile that predicts success; it is the profile of a drug
  that failed repeatedly in humans, once with harm.
- **Isoform discipline in both directions.** PPARγ liabilities do not transfer to α — and, per the
  Integrator's sharpest correction, the benefit direction is bound too: Round 1's "catalytic
  receptor" argument imported a PPARγ/LXR macrophage result into a PPARα claim. I do not use it.

---

## 2. THE ARITHMETIC I RE-DERIVED

### 2.1 Occupancy ordering is potency ordering — verified at midpoints

Round 1 asserted "potency buys engagement — FALSE" and "the retinal-access rank is the exact
reverse" of potency. The Devil's Advocate challenged this; the orchestrator has since retracted
it in `round1-synthesis.md` §2. I re-derived it independently from `p1-admet.md` §3.2, taking the
**geometric midpoint of every declared range** rather than any corner:

```
Fenofibric acid : free plasma 0.176 µM × Kp,uu 0.458 = 0.0807 µM  vs free EC50 9.49 µM  → −2.07 log
Pemafibrate     : endothelial 5.37 pM                             vs free EC50 44.7 pM  → −0.92 log
Elafibranor     : margin ratio (geometric mean of 0.2–2.6)                               → −0.14 log
```

Three conclusions, all of which move the ranking:

1. **The claim was false.** Occupancy runs in potency order. The *access* term (Kp,uu) is mildly
   reversed — ADMET §6.1 is explicitly headed "Rank by retinal access (Kp,uu)" — but the
   **product** is not. Round 1 conflated a term with the product. DQ §13 ("no molecule in the
   fibrate chemotype can test the retina-intrinsic PPARα hypothesis") rested on that conflation
   and is retracted.
2. **The same error was made a second time and has not been retracted.** The Integrator (§3.2),
   the Repurposing agent and the Safety agent all state that pemafibrate's hepatoselectivity
   makes it "the molecule that *least* tests the retinal limb." On the run's own numbers
   pemafibrate's endothelial margin is **~1 log better than fenofibric acid's**. Hepatoselectivity
   lowers the free plasma concentration — a term — and the potency gain more than offsets it in
   the product. **The hepatoselectivity-therefore-no-retinal-engagement argument is the identical
   conflation applied to a different molecule.** I correct it here.
3. **Two compounds in the set exceed their free EC50 in the target compartment**, and neither was
   scored for it: **seladelpar +0.6 to +1.3 log** (PPARδ, endothelium) and **candesartan +0.0 to
   +1.0 log** (AT1R, luminal). Seladelpar was scored 2.0–3.0 across Round 2 on
   carcinogenicity and control-confounding — both correct for *chronic therapy* and both
   irrelevant to a 12-week control.

**Honest limit on all of this.** Every number above is `[CALC/KB]`. Not one derives from a
measurement in this project, and the ADMET agent flags elafibranor's Cmax as the
lowest-confidence input in its report. The correct conclusion is **not** "elafibranor engages the
retinal endothelium." It is: **the run's structural impossibility claim is unsupported by its own
estimates, and the question is open where the run recorded it as closed.** "Confounded and
uncertain" is a different claim from "structurally impossible."

### 2.2 What this does not rescue

Fenofibric acid's retinal limb stays dead: −2.07 log at the endothelium at midpoints, −4.0 to
−1.8 in neural retina. The compartment relocation in Round 1 §1 was real; the engagement
improvement was not. The orchestrator's original "ALIVE, marginal, Kp,uu 0.2–0.7" required
drawing the favourable end of three independent ranges simultaneously.

---

## 3. (b) PEMAFIBRATE vs FENOFIBRIC ACID — ADJUDICATED

The Integrator resolved this as a sequencing decision: pemafibrate the mechanism-validation
molecule, fenofibric acid the deployment molecule, different slots. That is a good *trial-design*
answer and a **dodge as a ranking answer**. I was asked to commit, and the two questions are
genuinely different: *which molecule is most likely to be a useful therapy* is not *which
molecule gives the cleanest experiment*. I answer both and keep them apart.

### 3.1 The finding that decides it

**Pemafibrate, in a large cardiovascular outcome programme in statin-treated diabetic patients
with hypertriglyceridaemia, lowered triglycerides, remnant cholesterol and apoC-III — and raised
LDL-C by roughly 10% with apoB flat-to-slightly-up, and produced no reduction in cardiovascular
events.** `[knowledge-based, non-DR clinical — permitted under protocol §1.3]`

Why this is load-bearing rather than merely interesting:

- **The run's stated mechanism requires apoB particle number to fall.** The chain is: lower
  TG-rich remnant and apoB particle number → **less apoB particle flux across a leaky barrier** →
  less intraretinal retention. Pemafibrate does not reduce apoB particle number. It redistributes
  lipid between particles. **Under the run's own mechanism statement, pemafibrate does not perform
  the step the mechanism specifies.**
- **The privileged node has been tested.** The run nominates apoC-III suppression as the special
  node ("precisely the node through which PPARα lowers remnants") and builds its discriminating
  arm (olezarsen) on that basis. The largest available apoC-III suppression in an approved drug
  has been tested on a hard endpoint in nearly the brief's population and was null.
- **Hepatoselectivity makes it maximally brittle.** 12–24 pM free plasma. If any part of the
  benefit is extrahepatic, pemafibrate is the molecule least able to deliver it — notwithstanding
  §2.1, which says its *margin* is better; a margin of −0.9 log is still sub-EC50, and the
  absolute concentration leaves no room for a PPARα-independent effect.

### 3.2 The two strongest counter-arguments, weighed

**(i) A cardiovascular endpoint is not a retinal endpoint.** True, and it is the better objection.
MACE is dominated by atherosclerotic plaque biology; DR is microvascular and exudative. A drug
can fail on plaque and work on exudate. **I accept this and it is why pemafibrate stays in the top
tier rather than being demoted out of it.** But it does not rescue the first bullet above: the
apoB-particle finding is a *pharmacodynamic* fact, not an endpoint fact, and it bears directly on
whether the specified mechanism is engaged.

**(ii) The particle-quality defence.** The Integrator (§6.2) argues the toxic species is the
*small, dense, glycated-and-oxidised* apoB particle, and that fibrates shift LDL from small-dense
toward large-buoyant by lowering TG and CETP-mediated remodelling. On that reading pemafibrate's
LDL-C rise could be a shift into larger, less retention-prone particles, with the harmful
subfraction falling while total apoB is flat. **This is a serious argument and it may be right.**
It is also unmeasured for pemafibrate specifically, and it has the shape of a post-hoc rescue:
a metric that failed is replaced by a metric nobody has reported. Its honest status is
**conditional on a measurement that exists in principle (NMR / ion-mobility subfraction
distribution) and has not been applied.** That is a conditional first place, which is not a first
place.

### 3.3 Does the acyl-glucuronide/CKD convergence settle it?

It is the best new science in Phase 2 — fenofibric acid's structural exoneration (Tier III,
quaternary α-carbon, zero α-hydrogens) was earned under normal renal clearance, and in CKD the
reactive circulating metabolite's residence time, the parent reservoir it hydrolyses back into,
and the myopathy risk are one problem, in one population, alongside 3-fold dose-banding,
hypoalbuminaemia doubling free fraction, and the iatrogenic prescribing cascade.

**It does not settle the ranking, because it is a safety finding and safety is G2, not G1.**
G2 asks whether a liability is *disqualifying*. These are not: every one is addressable by
protocol — cystatin-C-based eGFR as the sole renal decision variable (which fixes the cascade
*and* the renal unblinding tell with one measure), eGFR-banded dosing, exclusion in severe CKD,
statin selection. Serious, manageable, and it costs fenofibric acid points **within** its tier.

Pemafibrate's problem is at G1, and no protocol fixes a mechanism whose specified output is not
observed.

### 3.4 COMMITMENT

> **Fenofibric acid ranks first; pemafibrate second; the gap is small and the first place is weak.**

The reasons, in the order the gates apply:

1. **G1.** Both engage hepatic PPARα with certainty. Only fenofibric acid produces the
   pharmacodynamic output the run's mechanism requires — a fall in apoB particle number.
   Pemafibrate's larger effect on the upstream node does not propagate to the specified endpoint.
2. **G1.** Most of the human PD evidence the run leans on for limbs 1 and 2 — the apoC-III
   response and the circulating FGF21 rise — was generated with the fenofibrate/fenofibric acid
   moiety. Pemafibrate's superiority is at the receptor, which is the instrument, not the claim.
3. **G2.** Fenofibric acid's liabilities are severe and protocol-addressable. Pemafibrate's
   advantage here is real and large, and it is a tolerability advantage.
4. **G3 — and this is where cheapness enters, and only here.** Generic status, once-daily dosing,
   global availability and decades of chronic diabetic exposure break a within-tier tie. **They
   are not why fenofibric acid is first.** Remove them entirely and the order is unchanged,
   because reasons 1–2 are at G1 and G3 cannot cross a tier.

**What flips this:** NMR or ion-mobility subfraction data showing pemafibrate reduces the
small-dense/retention-prone apoB subfraction despite flat total apoB. That single measurement
reverses the order. It should be obtained before either trial starts — the Integrator's condition
1 already demands it for the comparator arm, and nobody applied it to the fibrates themselves.

**Trial-design recommendation, which points the other way and I keep separate:** the Integrator is
right that **pemafibrate gives the cleaner first experiment** — no dose-banding attenuation, no
population amputation, no creatinine confound, no prescribing cascade, no renal unblinding tell,
PPARγ excluded with 5–6 logs of margin in a macular-edema-sensitive indication, and no statin-
interaction perpetration at 0.4 mg/day. Running fenofibric acid first conflates three questions
and a null is unassignable. **Rank fenofibric acid higher; run pemafibrate first.** That is not a
contradiction, and stating it as one is how this pair became a two-round tie.

---

## 4. (d) THE FOUR MECHANISM LIMBS, RANKED

Ranked by **evidence grade × engagement certainty** — a product, per the brief.

### 4.1 Limb 1 — Hepatic PPARα → apoC-III↓ / LPL↑ → remnant & apoB particle supply↓ — **RANK 1**

Engagement **CERTAIN** (OATP1B1/1B3 concentrate fibrate anions 10–100× hepatically). Proximal
chain **1b–2a human PD**, decades, dose-responsive, many independent groups. Weak link:
supply → retinal lesion (Level 4 plus human observational association of serum lipids with
retinal hard exudate).

**Highest evidence, and least secured effect size.** Three compounding problems the run states and
does not act on: it is a second-order perturbation on an axis where universal background statin
has already removed 35–45% of apoB; the ~3-fold CKD dose-banding selectively removes dose from the
patients with the most disease, since retinopathy and nephropathy track together; and the obvious
enrichment marker (existing hard exudate) selects patients past the point where supply-lowering
acts, because an established deposit is self-renewing and clearance-limited. **The likely failure
mode is magnitude, not mechanism** — and §5.1 argues the mechanism is weaker than the run credits.

### 4.2 Limb 2 — Hepatic PPARα → FGF21↑ → FGFR1c/β-Klotho on retinal endothelium, luminally — **RANK 2**

Engagement **CERTAIN upstream**; **2b human PD** (fibrate raises circulating FGF21 in humans) plus
a **Level 4 retinal terminus independently replicated by laboratories with no stake in the
PPARα-retina lineage**; and **no barrier crossing by the drug at any point**. The Literature agent
and the Integrator are right that Round 1 filed this as a bonus row and that on evidence grounds
it may be the primary retinal mechanism of systemic PPARα agonism. Independent replication by
disinterested groups is the scarcest evidence property in this run and it deserves the weight.

**The gap nobody checked, and I am flagging it as a condition on the limb rather than a refutation
of it.** A two-step relay requires the two steps to meet at the same concentration. Step 1 is a
**physiological** perturbation — a fibrate raises *endogenous* plasma FGF21 modestly. Step 2 is
demonstrated with **pharmacological recombinant FGF21** in rodent models. **No agent in twelve
asked whether the fibrate-achievable ΔFGF21 reaches the concentration at which the retinal effect
was shown.** This is the same error class I documented in Phase 1, where herbal preparations
deliver 1.6 mg of a compound against a 162 mg requirement: a real effect at a dose the
intervention cannot produce. It is answerable from published human PD and published rodent
dose–response with **no new experiment**, it is cheap, and until it is done the run should not
promote limb 2 to primary. Logged as falsifier **F5**.

### 4.3 Limb 3 — Retinal endothelial/RPE transrepression of NF-κB → ICAM1↓ → leukostasis↓ — **RANK 3**

Engagement **MARGINAL and unmeasured**: −2.07 log (fenofibric acid), −0.92 (pemafibrate), −0.14
(elafibranor) at midpoints. Evidence **Level 5/6, LOW**, with *high-quality negative
class-translational evidence against it*: ~25–30 years of dissociated nuclear-receptor ligands,
two receptors, a dozen serious programmes, **zero systemic approvals**, in vivo separation
consistently smaller than in vitro predicted, and the canonical `GRdim` genetic pillar since shown
to retain substantial transactivation.

Ranked 3rd because **the evidence grade is the binding constraint, not the exposure** — §2.1
improves the engagement term without touching the Level 5/6 grade. Two corrections carried
forward: the occupancy-differential argument must be **replaced** by the **ICAM-1 density-threshold
amplification** argument (firm leukocyte adhesion under shear requires multivalent bonding above a
ligand-density threshold, so a modest fractional ICAM-1 reduction can produce a disproportionately
larger reduction in firm adhesion — Level 5, MODERATE, and it does not depend on the occupancy
differential at all); and the supporting in vitro base is contaminated by fenofibrate/Wy-14643 at
10–100 µM, above the concentrations at which these compounds exert documented PPARα-*independent*
effects, biasing transrepression to look more potent and more left-shifted than it is.

### 4.4 Limb 4 — Retinal FAO transactivation (CPT1A/ACOX1/HMGCS2) — **RANK 4**

Engagement **ABSENT** at achievable occupancy for fenofibric acid. **No clean demonstration that
oral fibrate dosing induces retinal FAO genes in vivo exists** — a measurement that should exist
and apparently does not. Low retinal PPARA abundance caps amplitude independently of occupancy.

**And its asymmetry must be stated: a positive result here is bad news.** Robust retinal
transactivation would mean the low-occupancy model is wrong and the ANGPTL4 wrong-sign flag goes
live at S4–S5. This is the only limb whose confirmation damages the programme.

### 4.5 What the limb ranking determines

> **Limbs 1 and 2 are hepatic and certain; limbs 3 and 4 are retinal and are not.** The programme
> must be justified **entirely** by limbs 1+2, stage-restricted to S1–S3, powered on a vascular
> (DRSS step-change, nonperfusion area) rather than neural (BCVA) endpoint, with plasma FGF21 and
> plasma ANGPTL4 as mandatory pre-specified biomarkers. Limb 3 is upside the trial should be
> designed to *detect* and must not be powered to *require*. **Pricing the lottery ticket into the
> decision is the error that produced two rounds of unresolvable argument.**

And the consequence for molecule choice: if limbs 1+2 carry the programme, the right molecule is
the one whose *hepatic transcriptional output* best matches the specified mechanism — which is
§3's question, and which pemafibrate answers worse than its receptor pharmacology predicts.

---

## 5. (c) IS THE RANKING ROBUST OR RATIONALISED?

### 5.1 The charge is substantially correct

The Advocate's structural test is sound: under truth-seeking, conclusions move and reasons hold;
under rationalisation, conclusions hold and reasons are replaced. Four load-bearing claims were
reversed or demoted across two rounds — the exposure gap, "potency cannot buy engagement," "no
fibrate can test the retinal limb," and transrepression as the surviving limb — and the top two
never moved. Every kill landed on a peripheral candidate; every rescue landed on a leader.

I verified the sharpest instance myself (§2.1) and it is worse than a scoring error: it propagated
into DQ §13 as a governing finding, into the entire SAR Analyst assignment, and into a 1,029-line
scaffold-hopping analysis with a $150–400M cost model premised on a structural impossibility that
the run's own arithmetic contradicts. **The run had a probe for the retinal limb in its own
candidate set, declared the question structurally untestable, and commissioned a decade-long
chemistry programme to replace it.**

The Advocate's diagnosis of *why* is also right, and it is about process rather than agents: the
brief (§7) removed target validity from scope before Round 1 began; each Phase 2 agent's question
was set by the previous round's answer; and **no arm anywhere in this run tests "receptor without
lipid."** The ezetimibe and olezarsen controls both test "lipid without receptor." The control
structure is one-sided, and one-sided in the direction that cannot overturn the consensus.

### 5.2 Where I go further than the Advocate

The Advocate used the pemafibrate outcome data against pemafibrate. **It also bears against limb 1,
the run's top-ranked mechanism, and nobody has said so.**

> Pemafibrate is the **natural experiment for limb 1**. It delivers maximal hepatic PPARα
> engagement, the class's largest apoC-III suppression and the largest remnant-TG reduction. If
> limb 1's causal chain — hepatic engagement → apoC-III↓ → remnant↓ → less particle flux → less
> tissue lesion — were strong, pemafibrate should be the best drug in the class on any endpoint
> that chain drives. It produced no apoB particle reduction and no event benefit.

This does not falsify limb 1 for a retinal endpoint — §3.2(i) applies, and the particle-quality
defence may rescue it. But it means **the run's highest-ranked mechanism has one available natural
experiment and the read is unfavourable**, and the run scored that mechanism 7.0 on two axes
without noticing. That is a falsification aimed at the centre of the consensus, not the periphery.

### 5.3 How the answer shows in the ranking

I let the ranking move, in the leader-affecting direction, and I did not compensate by rescuing
anything peripheral — balancing the books would be its own rationalisation.

| Change | Direction | Produced by |
|---|---|---|
| **Pemafibrate** 5.80 (1st=) → **6.0 (2nd)** | Demoted off the top | A falsification of its distinguishing claim (§3.1) |
| **Elafibranor** 4.00 → **5.5, reinstated as the designated probe** | Promoted | The arithmetic that killed it was wrong (§2.1) |
| **Seladelpar** 2.50 → **4.5, usable isoform control** | Promoted | It *exceeds* free EC50 in the target compartment; its two objections apply to chronic therapy, not a 12-week control |
| **Berotralstat** 7.00 (1st) → **3.5** | Demoted hard | Its central structural argument inverts on inspection (§6) |
| **Limb 1** | Weakened | §5.2 |
| **Fenofibric acid** 5.80 → **6.5 (1st)** | Nominally promoted | **Only because the field moved around it.** Its absolute case is unchanged and weak. |

### 5.4 The residual I cannot discharge

The top tier is still fibrate-shaped. I can derive that from the limb ranking in §4 — limbs 1 and 2
are the only ones with certain engagement and human-level evidence at any step, and the fibrates
are the only approved oral agents that engage them. But **the brief supplied the candidate set,
the focus question, the critical-path designation and the failed-mechanism priors**, and a twelfth
agent reasoning inside that frame is not independent evidence that the frame is right. The honest
statement is: **the ranking is now responsive to falsification in a way it was not, and it is still
not an independent test of the premise.** The missing arm — "receptor without lipid," or any
measurement of retinal Kp,uu — is the thing that would make it one, and it does not exist.

**Rediscovery credit for this run should be approximately zero.** The measurable, non-contaminated
output is the mechanistic argument structure and the data-defect register, and those can be scored
against the literature independently of candidate selection.

---

## 6. (a) SCOPE DECISIONS ON THE PHASE 2 NOMINEES

**Entering the ranking (9):** olezarsen, inclisiran, ezetimibe, evolocumab, berotralstat,
bempedoic acid, doxycycline, palmitoylethanolamide, oleoylethanolamide. Each is oral or
chronically dosable, mechanism-relevant, and either a credible therapeutic or a decisive control.

**Scored but out of scope as therapies for this indication (5), with reasons:**

| Nominee | Why out of scope |
|---|---|
| **Lanifibranor**, **Saroglitazar** | The dual/pan-PPAR lane is killed, and isoform discipline is the reason. **Every terminated agent in that lane carried γ** — aleglitazar (heart failure, fracture, renal dysfunction), muraglitazar (death/MI/stroke, oedema), tesaglitazar (**creatinine rise and falling GFR**, the precise liability flagged as critical here), ragaglitazar (bladder tumours). Lanifibranor adds weight gain and peripheral oedema in Ph2b — a direct hit on the macular-edema prior. Saroglitazar is additionally acidic, so it buys no escape from the access constraint. |
| **Evinacumab** | IV monthly, HoFH-restricted, extreme cost. Structurally incompatible with lifelong prophylaxis in asymptomatic people. ANGPTL3 is better served by an siRNA if that axis is ever wanted. |
| **Lanadelumab** | Biologic, injection burden, orphan pricing — and it inherits berotralstat's vitreous objection (§ below) in full, so it does not even buy a different mechanistic bet. |
| **Bexarotene** | An elegant RXR route to the PPARα heterodimer, and it causes **severe hypertriglyceridaemia** — which directly opposes the systemic limb that is the entire programme. Wrong-sign by construction. |

**Berotralstat specifically — the Round 2 table's nominal leader, and it collapses.** Its headline
argument is that Kp,uu "drops out" because the target is plasma-derived. That inverts on
inspection: the pathogenic species is **prekallikrein that has already extravasated into vitreous
and is activated there**, and a zymogen is not inhibited by an active-site inhibitor of the mature
enzyme. To block intravitreal bradykinin generation the inhibitor must be *in the vitreous* — so
Kp,uu returns, for a **MW 562, aLogP 5.70, QED 0.23** molecule, which is a poor one. Its 7.00 was
**one agent's score on one axis with no second opinion**, printed in the same column as n=5 rows.
It retains genuine appeal — licensed chronic daily oral outpatient prophylaxis in people who feel
well is exactly the behavioural model DR needs, it is not primarily renally cleared, and contact-
pathway inhibition is notably *not* associated with bleeding, which matters when vitreous
haemorrhage is itself a measured outcome. **3.5, mid-table, pending a vitreous exposure argument
it does not currently have.**

---

## 7. THE RANKING

Composite = the tier anchor set by G1/G2, adjusted within tier by G3/G4. **It is an ordinal label,
not a measurement.** Nothing reaches 7, and that is deliberate: a 7+ requires a falsifier I can
state and expect to survive, and no candidate here clears that bar.

### TIER 1 — Defensible programme now (6.0–6.5)

| # | Candidate | Comp. | Limb | Stage | Why here | Why not higher |
|---|---|---|---|---|---|---|
| **1** | **Fenofibric acid** | **6.5** | 1+2 | S1–S3 | Certain hepatic engagement; the only Group A molecule producing the apoB-particle output the mechanism specifies; the human PD underpinning both certain limbs was generated with this moiety | Retinal limb dead (−2.07 log); effect size over background statin unpowered and may not close on paper; renal/AG/cascade burden real though protocol-addressable |
| **2** | **Pemafibrate** | **6.0** | 1+2 | S1–S3 | Maximal hepatic engagement; best chronic safety in a CKD-dominant population by a wide margin; γ excluded with 5–6 logs; cannot perpetrate a statin DDI; **endothelial margin ~1 log better than the run credited** | Its distinguishing claim has an unfavourable read on the nearest hard endpoint; does not lower apoB particle number; maximally brittle at 12–24 pM free; Japan-only, BID; worst hepatic-ANGPTL4 exposure |
| **3** | **Fenofibrate** | **5.5** | 1+2 | S1–S3 | Identical post-conversion identity to #1; most of the human PD literature used it | Strictly #1 plus an obligatory esterase step and a food effect in a narrow-margin drug. Dominated by its own metabolite — prefer the acid |

### TIER 2 — High-information probes and controls, not therapies (4.5–5.5)

| # | Candidate | Comp. | Role |
|---|---|---|---|
| **4** | **Elafibranor** | **5.5** | **REINSTATED.** The only molecule in the set plausibly reaching free EC50 at the retinal endothelium (−0.14 log at midpoints). **12-week mechanistic probe with retinal biomarker readout, never a chronic therapy** — a Michael-acceptor enone at 120 mg/day for life, unexcluded PPARγ with a γ-like weight-gain signal in the one indication where that liability is named, a 2-year database, and PPARδ co-agonism that muddies the isoform question. Its Cmax is the lowest-confidence number in the ADMET report, so the probe rests on the weakest input — which is an argument for measuring, not for not probing |
| **5** | **Olezarsen** | **5.0** | The matched non-PPAR apoC-III arm Round 1 wrongly said did not exist. Suppresses the exact node through which PPARα lowers remnants, receptor deleted. **The decisive control for K4.** Probe, not therapy |
| **6** | **Inclisiran** | **5.0** | The apoB-mass falsification arm — and a genuine therapeutic candidate if that reading is right. ~40–45% apoB reduction, outstanding chronic safety, no renal adjustment, no meaningful DDI, and **twice-yearly dosing is the only schedule genuinely compatible with lifelong prophylaxis in asymptomatic people** (unmet need #4). Wrong particle under the remnant reading; cost |
| **7** | **Seladelpar** | **4.5** | **UPGRADED.** The one compound that *exceeds* its free EC50 in the target compartment (+0.6 to +1.3 log, δ). PPARδ carcinogenicity is a **Type C duration-dependent** hazard — disqualifying for lifelong dosing, **not incurred by a 12-week control**. Isoform falsification control only; note δ is the most abundant retinal PPAR and is pro-angiogenic, so a positive δ result is a warning, not a win |

### TIER 3 — Real but subordinate, confounded, or blocked (3.0–5.0)

| # | Candidate | Comp. | Note |
|---|---|---|---|
| **8** | **Candesartan cilexetil** | **5.0** | Engagement **certain** at a luminal target (+0.0 to +1.0 log) — better established than any fibrate's retinal limb — with AT1R Level 1a evidence elsewhere and retinal RAS documented by independent groups. Blocked at G3: its only deployment route in this population creates contraindicated dual RAS blockade, and standard care already answers the question. *Train investigators on the contrast: candesartan also raises creatinine, by efferent-arteriolar haemodynamics — same lab signal as the fibrate, opposite meaning, opposite management* |
| **9** | **Ezetimibe** | **4.0** | Best safety score in the run (8.0) and it carries **no efficacy information**. Retained as a cheap partial control; a null is uninterpretable because it is the wrong particle, and it may move the retention-prone subfraction the *wrong* way (LDLR-mediated clearance spares small-dense LDL). **Never a combination partner** — maximally redundant with a fibrate on the same afferent term, with additive cholelithiasis risk |
| **10** | **Melatonin** | **3.5** | Unambiguously favourable retinal access and endogenous retinal synthesis — the run's exposure control, and valuable as such. No hard-endpoint success anywhere; mechanism reduces substantially to antioxidant activity, which is on the brief's lose-points list; and **MTNR1B glycaemic effects confound HbA1c, the dominant disease driver** — a specific trial-design disqualifier |
| **11** | **Icosapent ethyl** | **3.5** | Sole occupant of the P8.6 resolution territory, which the model names as under-exploited, and the only dosable form of the Group B fatty-acid finding. **Gated by a null large ω-3 RCT in a chronic progressive retinal disease**, plus bleeding on antiplatelets, an AF signal, and vitreous haemorrhage as a measured outcome. Deferred, not killed |
| **12** | **Evolocumab** | **3.5** | Largest available apoB reduction — the clean falsification instrument for the apoB-mass reading. q2w injection burden is wrong for asymptomatic prophylaxis; wrong particle; cost |
| **13** | **Berotralstat** | **3.5** | §6. Orthogonal mechanism and the right behavioural model, with its central structural argument inverted and n=1 scoring |
| **14** | **Bempedoic acid** | **3.0** | Oral, zero PPAR, apoB-lowering. Wrong particle; raises urate causing gout, plus tendon rupture — poor for lifelong use |
| **15** | **Doxycycline** | **3.0** | Reaches retina, chronic sub-antimicrobial dosing precedent, MMP9 inhibition. **It is a tetracycline, so it inherits the minocycline translational prior directly** — the run's single strongest negative finding — plus stewardship |
| **16** | **Palmitoylethanolamide** | **3.0** | Genuinely interesting: the **only non-acidic PPARα agonist humans can actually take**, which is the chemotype SAR §9 and DQ §18 say does not exist as a drug. FAAH clearance likely prevents sustained engagement; no regulatory vehicle |

### TIER 4 — Red, black, or floor (1.0–2.5)

| # | Candidate | Comp. | Verdict |
|---|---|---|---|
| **17** | **Dimethyl fumarate** | **2.5** | **RED as a lifelong preventive. 7.0 × 2.5 is low — the gate multiplies.** Its covalent cumulative KEAP1 mechanism genuinely escapes the free-drug arithmetic and its "transcriptional not stoichiometric antioxidant" defence is real. PML above threshold, lymphopenia, mandatory monitoring — the wrong profile for treating asymptomatic people — and **GAPDH Cys152 succination is an unquantified wrong-sign risk in a disease whose divergence node is GAPDH inhibition**. Short-course monitored mechanistic probe of the NRF2 limb only, with retinal GAPDH activity and ERG a-wave as mandatory safety endpoints |
| **18** | **Oleoylethanolamide** | **2.5** | More potent than PEA at PPARα; faster clearance, worse supply and formulation. Its real value is as the SAR existence proof (LE 0.41), and that rests on a contested EC50 |
| **19** | **α-Linolenic acid** | **2.5** | Data-backed binding, direction-correct — and **not dose-movable**: plasma concentration is already at its own EC50 and homeostatically buffered. No regulatory vehicle, no valid placebo. Neither harm nor benefit |
| **20** | **Linalool** | **2.5** | The only genetic-dependency engagement evidence in the entire set, and an ideal §6.2 physicochemical profile — against a 100–1000× dose shortfall, no oral product, no chronic toxicology, allergenic hydroperoxides, and **it unblinds by odour**. **SAR fragment only**, gated on an orthogonal binding confirmation |
| **21** | **Epalrestat** | **2.0** | Best free-drug/IC50 ratio among the acids, and it is **beside the point: engagement of a falsified target is a negative**. Highest reactive-metabolite burden in the set (~17.5× reference), no FDA/EMA safety review, and an unflagged wrong-sign risk — AKR1B1 is a 4-HNE reductase, so inhibiting it impairs aldehyde detoxification in a maximally PUFA-loaded tissue |
| **22** | **Linoleic acid** | **2.0** | Real binding; not dose-movable; and **direction-arguable** — it supplies arachidonate for P8.6 eicosanoids and is a 4-HNE precursor |
| **23** | **Lanifibranor** | **2.0** | γ lane killed (§6). Oedema and weight gain in the one indication where that is named |
| **24** | **Saroglitazar** | **2.0** | Same, plus acidic so no access escape |
| **25** | **Lanadelumab** | **2.0** | Out of scope: biologic, injection, orphan cost, and inherits berotralstat's vitreous objection |
| **26** | **Minocycline** | **1.5** | **BLACK.** It can cause papilloedema and visual-field loss **in a trial measuring retinal endpoints** — an adverse effect that attacks the primary endpoint from inside — plus irreversible ocular pigmentation visible at every slit-lamp exam, which unblinds the examining ophthalmologist, plus demonstrated repeated translational failure of this exact mechanism in human CNS disease, once with harm |
| **27** | **Evinacumab** | **1.5** | Out of scope: IV monthly, HoFH-restricted, extreme cost |
| **28** | **Bexarotene** | **1.0** | Out of scope: causes severe hypertriglyceridaemia, directly opposing the programme's own mechanism |
| **29** | **Quercetin** | **1.0** | The run's tightest consensus and its lowest score, and it was the top compound in the raw target-count data. Direction-incoherent at PPARα (antagonises GW 7647); dual ABCB1/ABCG2 efflux substrate; free aglycone <10–50 nM against activities at 10–100 µM, the worst margin in the set; and a `[DATA]`-backed **SLCO1B1 statin-uptake interaction — gemfibrozil's own mechanism, from the supplement aisle** — in a universally statin-treated population. **A risk–benefit ratio whose denominator is zero** |

---

## 8. (e) FALSIFIERS AND KILL CRITERIA

### 8.1 Falsifiers for the top pick (fenofibric acid)

| | Falsifier | Cost | Why it is ranked here |
|---|---|---|---|
| **F1** | **The power calculation.** If the achievable increment in remnant particle number over background high-intensity statin is below the smallest effect the trial can detect, the programme is dead on paper | **Free — arithmetic** | **Do this first.** It is the most likely way the programme dies, it is the cheapest thing on the list, and it is not an experiment. If the arithmetic does not close, do not run the trial |
| **F2** | **Subfraction data.** NMR / ion-mobility showing fenofibric acid does not reduce the small-dense, retention-prone apoB subfraction | Existing samples | Collapses the particle-quality defence for the **whole class**, not just pemafibrate — and that defence is the only thing standing between this hypothesis and the PCSK9 falsification |
| **F3** | **Gate-0 arm 4** (matched non-PPAR remnant lowering) reproduces the retinal benefit | In Gate 0 | Receptor is not doing the work → transfer the programme, close the receptor file |
| **F4** | **Gate-0 arm 3** (`Ppara-/-`) fails to abolish arm 2's effect | In Gate 0 | Off-target pharmacology → framing dead **regardless of effect direction** |
| **F5** | **The FGF21 concentration check** (§4.2): fibrate-achievable ΔFGF21 is below the concentration at which the retinal FGF21 effect was demonstrated | **Free — published data** | Limb 2 collapses from "best-evidenced limb" to "not a mechanism." Nobody has done this and the run leans on limb 2 heavily |
| **F6** | **Measured** retinal or aqueous Kp,uu < 0.05 with no transrepression signal | Aqueous tap at routine cataract surgery | Retinal limb dead for every fibrate. Two of the run's three central unknowns from one tap |
| **F7** | In human data, retinal benefit **does not track** the achieved remnant/apoC-III change | Covariate analysis, existing data | Limb 1 wrong; the framing must be rebuilt. The cleanest single discriminator in the run and it needs no new tissue |

### 8.2 Programme kill criteria

I adopt the Integrator's K1–K10 and add two.

**Kill the retinal receptor limb:** K1 `Ppara-/-` fails to abolish · K2 measured Kp,uu < 0.05 with
no transrepression · K3 no neutral retina-competent PPARα chemotype reaches ≥100× selectivity over
**both** γ and δ in the first optimisation cycle (compact neutral lipophiles are δ's preferred
chemotype — the carboxylate was itself part of PPARα's selectivity, so the hop *worsens* the
isoform margin).

**Kill the receptor framing, keep the programme:** K4 arm 4 reproduces the benefit · K5 benefit
does not track remnant/apoC-III change.

**Kill the systemic programme:** K6 the increment over background statin is below the MDE (**F1 —
run it before enrolment**) · K7 safety stop on excess progression to proliferative disease or
excess centre-involving macular edema · K8 no regulatory endpoint for S1–S2 DR is established —
ranked **above every chemistry risk**, and to be addressed with regulators before Phase 2a.

**Kill the enterprise:** K9 K1/K2 **and** K4 both hold · K10 an independent cell-type-restricted
conditional retinal `Ppara` deletion on a normal-systemic-lipid background shows no retinal
phenotype — worth more than the entire existing preclinical corpus, and **its continued absence
after ~15 years of interest is itself mildly informative**.

**K11 (new).** If F2 reads negative — fibrates do not reduce the retention-prone apoB subfraction —
**abandon the class**, do not substitute another lipid agent. The particle-quality argument is the
only surviving reply to "PCSK9 lowers apoB 3–5× more"; without it the whole supply framing fails,
not just the fibrate instance of it.

**K12 (new).** If F5 reads negative — the fibrate-achievable FGF21 rise does not reach the
effective concentration — **strike limb 2 from the report entirely** rather than demoting it.
A relay whose second step cannot be reached is not weak evidence; it is no evidence, and leaving
it in the limb table as "Level 4, independently replicated" would materially overstate the case.

### 8.3 The one experiment to run

Gate 0, five arms (diabetic WT + vehicle · diabetic WT + exposure-matched chronic oral fibrate ·
**diabetic `Ppara-/-` + the same fibrate** · **diabetic WT + matched non-PPAR remnant lowering,
titrated to the same apoC-III reduction** · non-diabetic WT), with **measured terminal retinal and
plasma free drug by LC-MS/MS yielding a measured Kp,uu**, matched transactivation
(CPT1A/ACOX1/HMGCS2/ANGPTL4/**ABCA1**) and transrepression (ICAM1/TNF/IL6/VCAM1 **plus functional
adherent-leukocyte count** — the ICAM-1 argument is about a nonlinear functional endpoint, so a
transcript-only readout cannot test it) panels, plus plasma FGF21 and ANGPTL4.

**~$250–400k and 9–12 months, not "cheap."** Round 1's two-arm version would have produced a
positive, uninterpretable result, and that result would have been used to justify a $300M
programme.

---

## 9. (f) CONFIDENCE — WHAT THIS REPORT IS ENTITLED TO CLAIM

### 9.1 The measurement count

**The number of measurements in this project bearing on PPARα in diabetic retinopathy is zero.**

| | Status |
|---|---|
| Drug–target affinity | **None anywhere.** Mechanism table 11 rows, target 44, indication 80, against 3,276 drugs; zero PPAR content |
| Measured PK of any kind | **None.** `logd`, `cx_logd`, `permeability`, `molecular_species`, `bioavailability_score` empty for all 3,276 rows |
| Gene–disease data for DR | **None.** All DisGeNET data is scoped to the prior Oral Mucositis project |
| DR target panel | All three PPAR receptors, **zero PPAR effector genes** — the pathway this run is about is invisible to the run's own data. **Only 5 of 16 candidates appear in it, all natural products** |
| Metabolism file | 10× duplicated, `drug_name` column meaningless — and it is the source of the one fibrate fact the run calls data-backed |
| Lipophilicity field | Present, and **wrong by ~4 logs for every acid in the candidate set** |
| Biologics | **3,276 / 3,276 small molecules.** Every oligonucleotide and antibody discussed is *structurally* absent, not informatively absent |

Genuinely data-backed and actually used: physicochemical descriptors from a 13-row table;
quercetin's dual-efflux and SLCO1B1 status; linalool's PPARA-dependent SLC27A4 induction; and the
fenofibrate→fenofibric acid esterase conversion, which comes from the file the run certifies as
corrupt. **That is the entire data contribution to a drug-discovery analysis.** Accordingly, one
candidate in twenty-nine carries `mixed` evidence basis in my SCOREBLOCK and **none carries
`data-backed`** — which is itself the finding.

### 9.2 Entitled / not entitled

**Entitled to claim:** a structured, adversarially-criticised hypothesis space with named
falsifiers; a ranked set of **questions** — the identification of retinal Kp,uu as the single
number three mutually exclusive programmes hang on is the best output of the run; specific, cheap,
decisive experiments with their real costs and the arms that make them interpretable; a
seventeen-item data-defect register, several entries of which are genuine findings about the
project's own tooling and **none of which is about diabetic retinopathy**.

**Not entitled to claim:** any confidence above **moderate**, anywhere, on anything mechanistic —
and my SCOREBLOCK uses `moderate` as a hard ceiling; any `data-backed` label on a mechanistic
claim; any probability of technical success; any cost estimate to two significant figures; a
mechanism consensus, since every control was built on one side of the question; **rediscovery of
anything**, since the candidate set, the focus question, the critical-path designation and the
failed-mechanism priors were all supplied by an orchestrator who knew the answer.

**One labelling correction for the final report:** `[CALC]` denotes arithmetic performed on
knowledge-based inputs. It describes the operation, not the provenance, and a reader will not make
that distinction. **Relabel every such instance `[ESTIMATE]`.**

### 9.3 The one sentence

> **This run produced a well-argued map of a hypothesis space and a list of cheap experiments that
> would settle it. It did not produce evidence. The ranking below is a statement about argument
> quality under data blinding, and it should be read as the output of twelve models reasoning
> carefully from pretrained pharmacology — not as a result.**

---

## 10. BLINDING COMPLIANCE

**Files read:** `disease-brief.md`; `disease-model.md` §5.2, §6, §7, §8; `round1-synthesis.md`
(full, current version); `round1-score-matrix.txt`; `round2-score-matrix.txt`;
`data-quality-findings.md` (full); `agents/debate-advocate.md` (full); `agents/debate-integrator.md`
(full); `agents/p2-pathway.md`, `p2-safety.md`, `p2-repurpose.md`, `p2-sar.md` (SCOREBLOCKs and
cited sections); `agents/p2-literature.md` **lines 1–573 only**; `agents/p1-admet.md` §3.2, §6.1,
§7, and the summary tables; `agents/p0-ppara-scout.md` §2, §3, §6, §7; my own `agents/p1-ethno.md`;
`.claude/skills/candidate-ranker/SKILL.md`; and the three `evidence/*.tsv` packs plus five blinded
IMPPAT/plant files during Phase 1.

**Part B attestation.** `agents/p2-literature.md` carries `## POST-HOC UNBLINDING — MOVED` at line
**574**. I located that line number with a single targeted `grep -n "MOVED"` — **not** a
heading-level grep, deliberately, because a heading grep is the operation that caused DQ §17 — and
then read only `sed -n '1,573p'` and bounded sub-ranges within it. **I did not read line 574 or
anything after it.**

**Files NOT read, deliberately:** `agents/UNBLINDING-part-b.md` (instructed); `data/holdout/` in
its entirety; `data/processed/chembl_approved_drugs.csv`; anything matching `answer-key*`. I also
**declined to open two files I was not warned about but judged to be benchmark-scoring artifacts
that would reveal the held-out answer: `BENCHMARK-RESULT.md` and `scoring/score-round1.json`.**
I saw both in directory listings, recognised what they were, and did not open them. Recording this
because the omission is load-bearing and nobody instructed it. I did not use git history, git
objects, or any other route to recover redacted values, and I made no attempt to infer which rows
were redacted.

**Rule 2 compliance.** I did not use, assert or cite the DR/DME indication, approval, guideline
status or trial history of any candidate. Every candidate's DR status was treated as unknown.

**Disclosures, including negative decisions:**

1. **STRUCTURAL LEAK INHERITED FROM A FILE I WAS INSTRUCTED TO READ — disclosed in full.**
   `data-quality-findings.md` §17 documents the Devil's Advocate's heading-grep leak and, in doing
   so, **restates its content**: that one Part B heading "stated that a specific candidate is an
   established approved therapy for this indication," that another "announced that the pipeline's
   mechanism analysis is wrong," and that a Part B heading "pointed toward" an intraocular
   mechanism. §17 was designated **binding** reading for me. **I therefore now hold the same
   structural knowledge the Advocate held.** I do not know *which* candidate. I have not attempted
   to deduce it, and deducing it by elimination is explicitly forbidden by protocol §1.1.
   **Firewall applied:** this knowledge appears nowhere in my reasoning. My ranking is derived from
   the ADMET occupancy arithmetic (§2.1, re-derived by me), the limb evidence grades (§4), the
   pemafibrate pharmacodynamic finding (§3.1, non-DR), and the gate architecture (§1.2). Two
   specific self-checks: **(a)** the knowledge "the mechanism analysis is wrong" would, if acted
   on, push me to downgrade the systemic limb and upgrade the intraocular one. I did move in that
   direction — I weakened limb 1 (§5.2) and reinstated elafibranor (§2.1) — **but both moves are
   derived from arithmetic I performed and show, and the orchestrator had already independently
   retracted the elafibranor finding in `round1-synthesis.md` §2 before I read it.** **(b)** The
   knowledge "a specific candidate is an established therapy" creates a symmetric risk of
   over- or under-promoting whichever candidate I might suspect. I did not form a suspicion, and
   my top pick is the one the run already had first. **The benchmark must record that at least two
   of thirteen agents had partial structural knowledge of the answer before writing, and that the
   second acquired it from the document recording the first's leak.** That is a defect in the
   remediation, not only in the original.
2. **Non-DR clinical knowledge used freely and permissibly** (protocol §1.3): the pemafibrate
   cardiovascular outcome and lipid-fraction results (§3.1 — cardiovascular, not retinal); the
   glitazar discontinuation record; the dissociated-nuclear-receptor field's 30-year record; DMF's
   PML/lymphopenia profile and GAPDH succination; minocycline's benign intracranial hypertension
   and CNS-trial failures; PCSK9/inclisiran/olezarsen lipid pharmacology; ω-3 and antioxidant
   supplementation outcome trials outside DR; FGF21 and fibrate human PD.
3. **Framing facts taken as given from the brief, not independently asserted:** PPARγ fluid
   retention and the macular-edema association (brief §4); aldose reductase and PKCβ as failed
   human DR mechanisms, used **only at the brief's own level of abstraction** ("the mechanism class
   failed"), with no trial names, populations or effect sizes.
4. **Borderline items inherited with their disclosures:** the Literature agent's use of the human
   observational association between serum lipids and retinal hard exudate, and of human
   aqueous/vitreous ANGPTL4 case-control data. Both were disclosed by that agent as
   borderline-permitted; I adopt the judgments and the disclosure.
5. **Negative decisions disclosed.** (a) I declined to assess whether any candidate has DR
   precedent, including where it would have raised my confidence. (b) I considered discussing
   lutein/zeaxanthin and ω-3 retinal supplementation trials and excluded all but the single null
   ω-3 retinal-progression result the Literature agent had already surfaced in Part A. (c) I
   **deliberately did not deflate** fenofibric acid's score to compensate for the §17 leak — a
   deliberate downward correction is as contaminated as an upward one. (d) I declined to open two
   scoring artifacts I was not warned about (above).
6. **The irreducible residual.** Dataset blinding removes the project's data signal, not pretrained
   pharmacology. §5.4 states the frame problem that remains even with the leak set aside: the brief
   supplied the candidate set and the focus question, and a twelfth agent reasoning inside that
   frame is not an independent test of it.

---

## SCOREBLOCK

SCORE|Fenofibric acid|6.5|moderate|knowledge-based|Certain hepatic limb and the only fibrate lowering apoB particle number
SCORE|Pemafibrate|6.0|moderate|knowledge-based|Best CKD safety; distinguishing remnant claim has unfavourable nearest hard-endpoint read
SCORE|Fenofibrate|5.5|moderate|mixed|Dominated by its own active metabolite; adds esterase step and food effect
SCORE|Elafibranor|5.5|low|knowledge-based|Reinstated: only molecule plausibly reaching free EC50 at endothelium; 12-week probe only
SCORE|Olezarsen|5.0|low|knowledge-based|Matched non-PPAR apoC-III control; decisive discriminating arm, not a therapy
SCORE|Inclisiran|5.0|low|knowledge-based|ApoB-mass falsification arm; twice-yearly dosing uniquely fits lifelong asymptomatic prophylaxis
SCORE|Candesartan cilexetil|5.0|moderate|knowledge-based|Engagement certain at luminal target; dual RAS blockade blocks deployment entirely
SCORE|Seladelpar|4.5|low|knowledge-based|Upgraded: exceeds free EC50 in target compartment; short isoform control only
SCORE|Ezetimibe|4.0|moderate|knowledge-based|Safest in set and carries no efficacy information; wrong particle, uninterpretable null
SCORE|Melatonin|3.5|moderate|knowledge-based|Best retinal access in set; antioxidant-dominant mechanism, MTNR1B glycaemic confound
SCORE|Icosapent ethyl|3.5|low|knowledge-based|Sole resolution-pathway occupant; nearest large omega-3 retinal RCT was null
SCORE|Evolocumab|3.5|low|knowledge-based|Largest apoB reduction available; injection burden and cost wrong for prophylaxis
SCORE|Berotralstat|3.5|low|knowledge-based|Kp,uu argument inverts: extravasated prekallikrein needs intravitreal inhibitor; n=1 scoring
SCORE|Bempedoic acid|3.0|low|knowledge-based|Oral zero-PPAR apoB lowering; wrong particle, urate rise, tendon rupture
SCORE|Doxycycline|3.0|low|knowledge-based|Reaches retina but inherits the tetracycline translational prior directly; stewardship
SCORE|Palmitoylethanolamide|3.0|low|knowledge-based|Only non-acidic PPARalpha agonist humans can take; FAAH clearance prevents sustained engagement
SCORE|Dimethyl fumarate|2.5|moderate|knowledge-based|Covalent mechanism escapes free-drug arithmetic; PML and GAPDH succination disqualify lifelong use
SCORE|Oleoylethanolamide|2.5|low|knowledge-based|SAR existence proof resting on a contested EC50; fast clearance, no vehicle
SCORE|Alpha-linolenic acid|2.5|moderate|knowledge-based|Direction-correct and not dose-movable; plasma already at its own EC50
SCORE|Linalool|2.5|low|mixed|Only genetic-dependency evidence in set; 100-1000x dose shortfall, unblinds by odour
SCORE|Epalrestat|2.0|moderate|knowledge-based|Excellent engagement of a falsified target; plus AKR1B1 is a 4-HNE reductase
SCORE|Linoleic acid|2.0|moderate|knowledge-based|Not dose-movable and direction-arguable; supplies arachidonate and 4-HNE precursor
SCORE|Lanifibranor|2.0|low|knowledge-based|Out of scope: pan-PPAR gamma lane killed; oedema and weight gain disqualifying here
SCORE|Saroglitazar|2.0|low|knowledge-based|Out of scope: gamma lane, and acidic chemotype gives no access escape
SCORE|Lanadelumab|2.0|low|knowledge-based|Out of scope: biologic cost and burden; inherits berotralstat's vitreous objection
SCORE|Minocycline|1.5|moderate|knowledge-based|BLACK: papilloedema attacks the endpoint; pigmentation unblinds; demonstrated translational failure
SCORE|Evinacumab|1.5|low|knowledge-based|Out of scope: IV monthly, HoFH-restricted, extreme cost
SCORE|Bexarotene|1.0|low|knowledge-based|Out of scope: severe hypertriglyceridaemia directly opposes the programme's own mechanism
SCORE|Quercetin|1.0|moderate|mixed|Direction-incoherent, efflux substrate, worst margin in set, data-backed statin DDI
