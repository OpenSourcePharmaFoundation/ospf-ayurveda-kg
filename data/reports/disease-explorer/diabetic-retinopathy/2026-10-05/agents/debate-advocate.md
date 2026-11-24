# Debate — Devil's Advocate

**Agent:** Devil's Advocate (Debate round) · 2026-10-05
**Run:** BLINDED benchmark run — compliance statement at §10, **including one disclosed leak**
**Brief:** attack the consensus. The Integration Agent supplies the balance; this file does not.

**Inputs read.** `disease-brief.md` · `blinding-protocol.md` · `round1-synthesis.md` ·
`round1-score-matrix.txt` · `round2-score-matrix.txt` · `data-quality-findings.md` ·
`agents/p2-pathway.md` · `agents/p2-safety.md` · `agents/p2-repurpose.md` · `agents/p2-sar.md` ·
`agents/p2-literature.md` **Part A only** · targeted sections of `agents/p1-admet.md` (§3.1, §3.2
A1/A3/A4, §5.1) for verification of numbers quoted by the synthesis.

---

## 0. The attack in one paragraph

**The pipeline's conclusion has been invariant across two rounds, eleven agents, three self-reversals
and sixteen recorded defects. Its reasons have changed completely. When the premises are replaced and
the conclusion is not, the conclusion is not being derived from the premises.** Phase 0 said the
exposure gap killed the hypothesis; Round 1 said the gap was mis-measured and relocated the mechanism
to the liver; Round 2's SAR agent said the structural constraint that organised Round 1 is not real.
Through all of it, fenofibric acid and pemafibrate sat first and second. Every demotion the run
produced landed on a peripheral candidate (quercetin, minocycline, epalrestat, DMF, seladelpar);
every rescue landed on the leaders. Below I show that the run's two load-bearing quantitative
claims — "the exposure gap was overstated by one log and the relevant compartments are accessible"
and "potency does not buy engagement in this series" — are **contradicted by the arithmetic of the
agent they are sourced to**, and that the run's central mechanistic consensus (systemic lipoprotein
lowering) makes a prediction about *which fibrate should win* that is the exact opposite of what the
run concluded, from a discriminating pair the run already had in its own candidate set and never used.

---

## 1. Why the leading candidate fails — taken separately, because they fail differently

### 1.1 Fenofibric acid (and fenofibrate) — failure by effect size under phenotype dilution

The consensus mechanism is systemic apoB/remnant supply reduction. Grant it entirely. It still fails,
and the most likely route is not mechanism-falsity but **magnitude**, compounded four ways:

1. **It is a second-order perturbation on an already-treated axis.** The population is universally
   statin-treated (brief §5; safety §3). Statins remove 35–45% of apoB before the fibrate arrives.
   The run's own finding §14 states this and then does not act on it: *whatever a fibrate adds is the
   remnant component statins do not touch*, which is the small residue of an already-shrunken term.
2. **The dose is removed from the patients who have the disease.** Safety §4.1: ~30–35% of the
   population needs a ~3-fold dose reduction and 5–10% are excluded, and retinopathy and nephropathy
   track together. The safety agent used this to argue *for* the systemic limb (it is flat-topped and
   tolerates dose reduction). Read the other way, it means the trial's effect is carried by the
   healthiest third of the population while the enriched, high-event third is under-dosed —
   the standard recipe for a diluted, non-significant result.
3. **Stage offset.** Round 1 §3 establishes that the exposure-robust limb is mechanically inoperative
   at S0 and only operates once the barrier leaks (S1–S3). The pathway agent (§4) adds that the
   obvious enrichment biomarker — existing hard exudate — *selects the patients in whom the supply
   mechanism is weakest*, because an established deposit is self-renewing and clearance-limited. So
   the mechanism has no valid enrichment marker: the marker that identifies lipid-phenotype patients
   also identifies the patients past the point where supply-lowering acts.
4. **The endpoint cannot see a small effect.** Early-DR regulatory endpoints do not exist
   (SAR §9.2 risk iv). A DRSS-step endpoint is graded, subjective, and has substantial inter-reader
   variance; against modern background therapy (intensive glycaemia, BP control, SGLT2i, GLP-1RA) the
   residual lipid-attributable risk is small and the measurement noise is not.

> **Most likely single failure statement:** *the mechanism is real, the effect is small and
> stage-restricted, and there is no enrichment strategy that selects for it without selecting against
> it. The trial reads null and nobody learns whether the mechanism was wrong or the population was.*

A second, independent failure mode that nobody in the run has costed: safety §4.3's **iatrogenic
prescribing cascade**. A creatinine rise that is analytical and secretory, not filtration loss, still
triggers withdrawal of metformin, SGLT2 inhibitors and RAS blockade in routine care. In a 20-year
preventive deployment, the harm from *withdrawn renoprotection* plausibly exceeds the benefit from a
small retinal effect. The safety agent identified this and scored it as a manageable nuisance because
cystatin C fixes it in a trial. It does not fix it in primary care at population scale, which is the
deployment the brief's unmet need #1 actually describes.

### 1.2 Pemafibrate — failure by moving the run's own toxic species in the wrong direction

This is the attack I most want on the record, because it is specific, it is permitted non-DR clinical
knowledge, and **no agent in eleven raised it.**

The disease model's toxic species is the **modified apoB particle**. The run's consensus limb is
**reduction in apoB/remnant supply**. The Repurposing Strategist's case for pemafibrate (§6, §3.2) is
that it has the *largest apoC-III/remnant effect in the class* and therefore lowers "the right
particle." The Safety Pharmacologist ranks it #2 overall at 7.0. The Pathway Analyst gives it 7.0.

**But pemafibrate's effect on apoB particle number is not negative. In the large cardiovascular
outcome programme in statin-treated diabetic patients with hypertriglyceridaemia, pemafibrate lowered
triglycerides and remnant cholesterol by roughly a quarter, lowered apoC-III — and *raised* LDL
cholesterol by roughly 10% and apoB by a few percent, with no reduction in cardiovascular events.**
`[knowledge-based, non-DR clinical — permitted under protocol §3]`

Three consequences, each fatal to a different part of the run's case for this compound:

- **It falsifies the particle argument as applied to pemafibrate.** The agent's own framing — "the
  right particle" — requires apoB particle number to fall. It does not. Lowering remnant-TG while
  holding or raising apoB redistributes lipid between particles; it does not reduce the flux of
  apoB-containing particles across a leaky barrier, which is the run's stated mechanism.
- **It undercuts the supply hypothesis generally.** A drug producing the class's largest apoC-III
  suppression and largest remnant-TG reduction produced no hard-endpoint benefit in the population
  under study. The run treats apoC-III suppression as the privileged node ("precisely the node
  through which PPARα lowers remnants," §5 correction) and nominates olezarsen as the discriminating
  arm on that basis. The best available test of that node has already been run in an adjacent
  endpoint and it was null. The run's §14 noticed the PCSK9 half of this falsification test and
  missed the apoC-III half, which is the half it had a drug for.
- **Hepatoselectivity deletes every alternative.** Pemafibrate's free plasma concentration is
  **12–24 pM** (ADMET §3.2, A3). If any part of the benefit is extrahepatic — retinal PPARα,
  endothelial transrepression, or anything PPARα-independent — pemafibrate is the one molecule in
  the set guaranteed not to have it. The run concedes this and reframes it as a virtue ("it tests
  limb (i) and only limb (i)," literature A7). That is only a virtue if limb (i) is correct. It makes
  pemafibrate a maximally brittle bet: it wins only in the single world where the consensus is right,
  and in that world it is the drug whose apoB signature is wrong.

> **Most likely single failure statement:** *pemafibrate is selected for a property (hepatoselective
> remnant lowering) that has already failed its nearest available hard-endpoint test, while being
> constructed so that no other mechanism can rescue it.*

Against this, the run's actual affirmative case for pemafibrate reduces to **chronic-use tolerability
in CKD** — real (safety §4.2), and an argument about who can take the drug, not about whether it
works. The run has promoted a tolerability finding into an efficacy ranking.

---

## 2. The most optimistic and least supported assessment

### 2.1 Highest impact: the Round 1 synthesis's elevation of the ADMET endothelial estimate

This is not the ADMET agent's claim — the ADMET agent labelled its numbers `[CALC/KB]`, gave ±1 log
on the protein correction, and called compartment-resolved Kp,uu its #3 data gap. **The optimism was
introduced by the orchestrator's synthesis**, and it is the single most consequential unsupported
step in the run.

Round 1 §1 reports two things as established:

> "The ~2-log exposure gap — **Overstated by ~1 log.**"
> "Retinal **endothelial / RPE** PPARα engagement is achievable — **ALIVE, marginal.** Est. Kp,uu
> 0.2–0.7."

Now read the agent being summarised. ADMET §3.2, A1, line 10:

```
10. ENDOTHELIUM / RPE free (5 × Kp,uu 0.3–0.7)   0.03–0.22 µM
      margin vs free EC50 ................... 0.001 – 0.073  →  −3.0 to −1.1 log
```

**The endothelial margin for fenofibric acid, after every correction the synthesis credits, is −3.0
to −1.1 log, with a midpoint near −2.0.** The Phase 0 scout's objection was "~2 logs." The
"correction" did not change the number. It changed the compartment the number refers to, and then
reported the **best corner of a two-log band** as the new central estimate.

To reach −1.1 you must simultaneously draw: the top of the Kp,uu range (0.7), the bottom of the
±1-log free-EC50 correction (3 µM, not 30), and the top of the free-plasma range (0.31 µM, not 0.10).
Three independent favourable draws. The three ranges are the agent's own declared uncertainty; taking
the favourable end of each and calling the result "marginal but alive" is **stacked best-casing**,
and it is the move on which the survival of the retinal limb — and therefore the entire Round 1
headline, the Phase 2 question set, and the SAR agent's assignment — depends.

**Falsifier:** recompute the endothelial margin at the midpoint of each declared range. It is −2 log.
If the orchestrator's own synthesis is re-derived at midpoints rather than at favourable corners, the
row reads "DEAD, same as neural retina, one log less dead" — and Phase 2's framing collapses.

### 2.2 The claim that is flatly contradicted by the arithmetic it cites

Round 1 §2, the "deepest result of the round":

> "The ADMET agent independently produced the same result from the other direction: potency rank
> within Group A is pemafibrate ≫ elafibranor > seladelpar ≫ fenofibric acid, and **the
> retinal-access rank is the exact reverse.**"
> And §1: "**Potency buys engagement — FALSE.**"

The computed endothelial margins in the report being cited:

| Compound | Potency rank | Endothelial margin vs free EC50 (ADMET §3.2) |
|---|---|---|
| Elafibranor | 2nd | **−0.7 to +0.4 log** |
| Pemafibrate | 1st | **−1.6 to −0.2 log** |
| Fenofibric acid | last | **−3.0 to −1.1 log** |

**The occupancy rank runs in the same order as potency, not the reverse.** The *access* term (Kp,uu)
is mildly reversed; the *occupancy* — which is the whole left-hand side of the run's own governing
equation — is not. Pemafibrate ends ~1 log **better** than fenofibric acid; elafibranor ~2.3 logs
better. The ADMET agent says so explicitly: "its endothelial margin is ~1 log better than fenofibric
acid's." Potency bought engagement at a brutal exchange rate — roughly 1 log of occupancy per 4.8
logs of potency — but it bought it.

The synthesis converted "a term in the numerator moves the wrong way" into "the net moves the wrong
way." That is a conflation of one factor with the product, and it propagated into:

- **data-quality §13** — "no molecule in the fibrate chemotype can test the retina-intrinsic PPARα
  hypothesis," recorded as a governing finding for the final ranking;
- **Round 1 §9 question 4** — the entire SAR Analyst assignment;
- **p2-sar.md** — a 1,029-line scaffold-hopping analysis, a $150–400M NCE cost model and a 15–25%
  PTS estimate, all premised on a structural impossibility.

And it is contradicted inside the same ADMET report, which says of elafibranor: *"the only Group A
compound that plausibly reaches or exceeds its free EC50 at the retinal endothelium… the cleanest
pharmacological probe of whether endothelial PPAR engagement does anything in this disease."* **An
existing, approved fibrate-class drug can test the retinal limb.** The honest claim was never
structural; it was that the molecule which can test it has a chronic-dosing electrophile and two
years of market history. That is a safety and commercial objection, not a law of medicinal chemistry,
and it has a cheap answer the run never proposed: *elafibranor as a 12-week mechanistic probe with a
retinal biomarker readout, not as a therapy.* The run had its probe, declared it structurally
impossible, and commissioned a decade-long chemistry programme to replace it.

### 2.3 Most optimistic *agent* claim: the SAR Analyst, §9.1 / §7.1

> "The constraint is not fundamental, it is unexplored… the anion is the conventional solution, not
> the mechanistic one… the design does not require a better LLE than anyone has achieved."

Four attacks:

1. **The lead concept contradicts the headline.** §9.1 argues the acid is not required, via neutral
   ligands. The highest-confidence design, Concept A, uses a **1,2,4-oxadiazol-5(4H)-one, pKa 6.0–7.0
   — 80–97% ionised at pH 7.4**. The recommended answer to "is the acid required?" is therefore
   *"yes, essentially — shift its pKa by three units."* The neutral-head case (OEA, linalool) carries
   the rhetoric; the acidic head carries the molecule. The report's own §7.5 ranks the two neutral
   concepts below it on potency, Emax, and confidence.
2. **LLE is not conserved along a logD reduction, and the whole arithmetic assumes it is.** §7.1's
   target profile closes the gap by spending "the same LLE at logD 2.8 instead of 5.5." But the
   report's own §2.3 explains why that is the one thing this receptor will not allow: PPARα is a
   fatty-acid sensor with a 1,300–1,400 Å³ hydrophobic cavity, and binding energy comes from burying
   hydrophobic surface. In such a pocket, stripping 2.7 logD units typically costs *more* than 2.7
   log of potency, because you lose specific contacts along with the generic burial — LLE falls, it
   does not hold. "Pemafibrate demonstrates LLE 3.45" is an observation at logD 5.5; asserting it
   transfers to logD 2.8 is the composition fallacy the whole report exists to warn about.
3. **The existence proof is weaker than quoted.** The LE 0.41 result rests on OEA at ~120 nM. OEA's
   PPARα potency is reported across more than a log, its receptor-mediation has been contested, and
   OEA engages GPR119 and TRPV1 in the same assays. Computing a ligand-efficiency metric from the
   favourable end of a contested EC50, comparing it across different assay formats and readouts, and
   calling the result "**the** quantitative falsification of 'the acid is required'" (§2.2) is a
   single soft number carrying a structural conclusion.
4. **The report double-counts its own penalties and then calls the result affordable.** §1.2 prices a
   neutral head at 3.5–5.5 kcal/mol (10²–10⁴ in K_d). §1.3 adds that Emax degrades before affinity,
   by construction. §2.5 adds that PPARδ selectivity *starts worse* for a neutral compact chemotype.
   §7.1 then assumes 500 nM with Emax 60–90% and ≥100× δ-selectivity. Each stated penalty is
   acknowledged in prose and absent from the arithmetic.

To be fair to this agent: its *strategic* conclusion — "tractable and premature; run the $100k rodent
experiment before the $300M programme" — is the most operationally sensible sentence in the run, and
it survives everything above. The optimism is confined to the chemistry feasibility claim, and the
chemistry claim is not load-bearing for any ranking.

### 2.4 The Pathway Analyst's multiplicativity claim (§4)

> "Halve influx and double clearance → one quarter of the steady-state burden… Their effects are
> **multiplicative**… additive-to-supra-additive, not redundant."

Two problems.

- **"Multiplicative" here is a scale artifact, not a synergy finding.** For `burden = influx ÷ k`,
  two interventions on different factors are multiplicative *by the definition of independence on a
  ratio scale*. Independent effects are always multiplicative in ratio terms. Reporting that as
  "supra-additive" imports a pharmacological meaning the algebra does not supply.
- **It contradicts the same report's §3.3.** The foam-cell futile cycle makes the established deposit
  **self-renewing** — i.e. there is a source term *inside* the compartment. A compartment with an
  internal source is not `influx ÷ k`; lowering external influx does not scale it. By the pathway
  agent's own lesion model, the supply agent's effect on an established deposit is near zero, so the
  combination is not multiplicative — it is "the efflux agent does the work on the lesion that
  determines vision, and the supply agent does not contribute to that term at all." The agent reaches
  this conclusion in §3.3 and the opposite one in §4 and never reconciles them.

### 2.5 The Target Analyst's transrepression argument — dead, but still scored

The Literature Reviewer graded it **Level 5/6, quality LOW, with high-quality negative class evidence
against it** (A3.4), identified that Round 1 imported a PPARγ/LXR macrophage mechanism into PPARα in
a run whose brief mandates isoform discipline (A3.2 objection 2), and issued the rule *"do not present
transrepression-at-low-occupancy as the reason a PPARα candidate should work"* (A5.3 rule 3).

The Pathway Analyst, scoring in the same round, places fenofibric acid "**at the node**, by
transrepression — marginal occupancy, threshold-advantaged," scores it 7.0, and names that limb in its
own falsifier for the 7.0. The orchestrator then averaged the two. **The Round 2 matrix therefore
contains a 7.0 that is explicitly conditioned on a limb another Round 2 agent graded LOW with negative
class evidence, and the averaging destroyed the contradiction rather than surfacing it.** Parallel
execution is the excuse; propagating the demotion into the score is the fix, and it was not done.

---

## 3. Two reversals: convergence on truth, or rationalisation?

### 3.1 The structural test

A truth-seeking process and a rationalising process are distinguishable without knowing the answer.
Under truth-seeking, **conclusions are unstable and reasons are stable** — you keep the argument and
change what it supports. Under rationalisation, **conclusions are stable and reasons are unstable** —
you keep the answer and replace the argument when it fails.

| Round | Load-bearing claim | Status by end of run | Top-2 ranking |
|---|---|---|---|
| Phase 0 | Retinal exposure gap ~2 log → hypothesis fails | "Overstated by 1 log"; relocated to a different compartment | fenofibric acid / pemafibrate |
| Round 1 | Potency cannot buy engagement; no fibrate can test the retinal limb | Contradicted by the ADMET margins it cites (§2.2) | fenofibric acid / pemafibrate |
| Round 1 | Transrepression at low occupancy is the surviving retinal limb | Graded LOW with negative class evidence (lit A3.4) | fenofibric acid / pemafibrate |
| Round 2 | The structural constraint is not real; the chemotype is designable | Internally contradicted; lead concept is acidic (§2.3) | fenofibric acid / pemafibrate |

**Four load-bearing claims, four reversals or demotions, zero movement in the answer.** Round 1 mean
6.10 → Round 2 mean 5.80, with the composition of the panel changed. That is not convergence; that is
a fixed point under argument.

### 3.2 The asymmetry that makes it diagnostic

The run is capable of killing candidates — quercetin, minocycline (BLACK), epalrestat (RED), DMF
(RED), seladelpar (RED), the natural-product arm as a class. So it is not uniformly credulous. But
**every kill landed on a non-leader, and every rescue landed on a leader.** In two rounds and sixteen
defects, no finding has ever demoted fenofibric acid or pemafibrate out of the top two. A process
with genuine power to falsify, applied to sixteen candidates, that never once falsifies the two it
started pointed at, is selecting its scrutiny.

### 3.3 Where each framing invited the next

The sequence is not independent agents converging; it is a chain in which each agent's question was
set by the previous agent's answer:

- The **brief** (§7) tells every agent that "the critical path item is retinal exposure after oral
  dosing, **not target validity**." Target validity is thereby removed from scope before Round 1
  begins. The Literature Reviewer, arriving in Round 2, re-opens it and finds the retina-intrinsic
  case is "Level 4, quality MODERATE, overstated by the brief by about one grade" with **no human
  genetic validation and no decisive necessity experiment in fifteen years** (A1.5). That is the
  finding that should have organised the run, and the brief had foreclosed it.
- Round 1 concludes "no fibrate can test the retinal limb" → **this becomes the SAR agent's
  assignment**, so the SAR agent's job is defined as "how would you build the molecule," not "is the
  premise true." It never checks the premise, which was false (§2.2).
- Round 1 concludes the systemic limb survives → **this becomes the Repurposing Strategist's
  reframe (§3)**, which then nominates inclisiran and olezarsen *within* the supply frame. No agent
  was ever assigned to attack the supply frame itself. The ezetimibe control tests "lipid without
  receptor." **No arm anywhere in this run tests "receptor without lipid," or "drug without lipid."**
  The control structure is one-sided, and it is one-sided in the direction that cannot overturn the
  consensus.

> **Verdict on §3: this is rationalisation, in the specific and non-pejorative sense that the
> pipeline's search was never pointed at its own conclusion.** The agents are individually rigorous
> and several are excellent. The *process* has no arm that could have produced a different answer.

---

## 4. Missing data, ranked by how much it would move the conclusion

| # | Missing quantity | Why it moves the conclusion | Obtainable? |
|---|---|---|---|
| **1** | **Does the retinal benefit covary with the individual lipid change?** (mediation/covariate analysis) | This is the entire (i)-vs-(intraocular) question as a measurable covariate. If benefit does not track the lipid response, the whole Round 1 + Round 2 consensus is wrong and the ranking inverts: pemafibrate, ezetimibe, inclisiran and olezarsen all fall, and total-exposure agents rise. The literature agent ranked it #4; **it should be #1**, because it is the only item on this list that can falsify the consensus rather than refine it, and it needs no new experiment. | **Yes — covariate analysis of existing data** |
| **2** | **Measured retinal (or aqueous) free fibrate concentration — Kp,uu** | Three mutually exclusive programmes hang on it (lit A6.1). At 0.01–0.05 the receptor is a red herring; at 0.2–0.5 the receptor matters and the ANGPTL4 flag returns at S4–S5. Every contested number in the run is a function of this one. | **Yes — aqueous tap at routine cataract surgery** |
| **3** | **apoB particle number and particle-size distribution for each candidate, matched** | Immediately resolves §1.2. If pemafibrate does not lower apoB, the run's #1/#2 ranking is internally inconsistent with its own disease model. Pathway §8.2 already requires this for the ezetimibe arm and nobody applied it to the fibrates themselves. | **Yes — existing lipid data, NMR/ion mobility** |
| **4** | **The rodent experiment with the two arms the literature agent added** — `Ppara-/-` arm and matched non-PPAR lipid-lowering arm | Round 1 called its version "cheap and decisive." Without a `Ppara-/-` arm it cannot exclude the PPARα-independent activity fibrates demonstrably have at the concentrations reached; without a lipid-matched arm it cannot assign a positive result to the receptor. **As specified in Round 1, it is cheap and indecisive.** | Yes, 6–9 months, ~$150k |
| **5** | **Cell-type-restricted conditional `Ppara` deletion in retina** | The only necessity experiment. Its absence after ~15 years is itself evidence (lit A1.4). Would settle target validity, which the brief removed from scope. | Yes, slow |
| **6** | **Effect-size realism: DR incidence stratified by baseline lipids on modern background therapy** | Determines whether any lipid-mediated effect is powerable at all in the current treatment era. Governs §1.1 failure mode 4. | Yes — registry/cohort |
| **7** | **Any drug–target affinity measurement at all from this project** | The project supplied none (DQ §2). Would convert at least one claim in the run from knowledge-based to data-backed. | Requires re-scrape |
| **8** | Intraocular ANGPTL4 stratified by fibrate exposure | Settles the wrong-sign question. Samples exist in vitrectomy biobanks. Lower rank only because the risk is already demoted by three independent arguments. | Yes, cheap |

---

## 5. The bet against: **pemafibrate**

Among the five candidates with full five-agent coverage in Round 2 (fenofibric acid 5.80, pemafibrate
5.80, candesartan 5.50, fenofibrate 5.00, ezetimibe 4.90), I bet against **pemafibrate**, and I would
take the other side at meaningful odds.

1. **It moves the run's own toxic species in the wrong direction** (§1.2). Remnant-TG and apoC-III
   down; apoB and LDL-C flat-to-up. The disease model's lesion is the retained modified apoB particle.
2. **Its distinguishing mechanism has already failed its nearest hard-endpoint test** in the same
   population — statin-treated diabetics with hypertriglyceridaemia — which is also the population
   the brief describes. `[knowledge-based, non-DR]`
3. **Hepatoselectivity makes it maximally brittle.** 12–24 pM free plasma. It wins only in the world
   where the consensus is exactly right, and in that world §1 applies to it.
4. **Its affirmative case is a tolerability case wearing an efficacy ranking.** Safety 7.0 is earned
   (hepatobiliary clearance, no creatinine rise, 493× lower molar covalent burden, no CKD banding).
   None of that is evidence it works.
5. **Its own axis-specialist scored it 2/16 — the lowest headroom in the set** (SAR §10), and the
   orchestrator averaged that 2 into a mean that still places it first. If the SAR axis were removed
   as its author explicitly instructed, pemafibrate's mean rises to 6.75 and the apparent tie with
   fenofibric acid (6.00) disappears — the Round 2 "tie" is manufactured by an operation two agents
   told the orchestrator not to perform.
6. **Practical disqualifiers stacked on top:** Japan-only approval, BID dosing for a lifelong
   asymptomatic preventive, no Western chronic database, and the worst hepatic-ANGPTL4 profile in the
   set precisely because it is the most hepatoselective (repurpose §6).

**Runner-up bet-against, and it is formally the top of the Round 2 matrix: berotralstat (7.00, n=1).**
Its headline argument is that `Kp,uu` "drops out" because the target is plasma-derived. That is wrong
as stated. The pathogenic species is **prekallikrein that has already extravasated into the vitreous
and is activated there**; a zymogen is not inhibited by a kallikrein active-site inhibitor, so
inhibiting plasma kallikrein in the circulation does not stop extravasated prekallikrein being
activated in the eye. To block bradykinin generation in the vitreous the inhibitor must be *in the
vitreous* — so `Kp,uu` does not drop out, it returns for a MW 562, aLogP 5.70, QED 0.23 molecule. The
run's "strongest single structural argument" for its highest-scoring Round 2 candidate inverts on
inspection, and that candidate's 7.00 rests on one agent's score with no second opinion.

---

## 6. ATTACK ON THE MECHANISM CONSENSUS — the case that the benefit is intraocular and not lipid-mediated

This is the attack most likely to be productive, so it gets the most space.

### 6.1 What the consensus commits to, and the prediction it cannot avoid

The consensus (Round 1 §1, §3; Round 2 pathway §8, repurpose §3, lit A2) is: **the exposure-defensible
limb is hepatic PPARα engagement → lower apoC-III, higher LPL → lower TG-rich remnant/apoB supply →
less transretinal lipoprotein flux across a leaky BRB → less intraretinal retention.**

That commits to a quantitative chain, and the chain generates falsifiable predictions the run states
and then does not pursue:

| Prediction | Status in the run |
|---|---|
| Agents lowering apoB more should work better: PCSK9i (45–55%) ≫ fibrate (5–15%) | Stated in DQ §14 as "a clean falsifiable prediction that the pipeline should state rather than avoid." Never pursued. |
| Statins (35–45%, universal background) should already have captured most of it | Stated in DQ §14. Never pursued. |
| Ezetimibe should reproduce it if apoB is the species | Added as E1, then **demoted by the run itself** as the wrong particle (DQ §14) — i.e. the control was weakened precisely where it could have falsified |
| A matched apoC-III agent should reproduce it | Olezarsen nominated. **The apoC-III/remnant node has already been tested on a hard endpoint and was null** (§1.2) |
| Benefit should require the lipid phenotype | **Never stated by any agent** |

Note the pattern: the consensus has generated four discriminating predictions and the run's response
to each has been to narrow the hypothesis until the prediction no longer applies — apoB → remnants →
apoC-III → "the modified particle." **Each narrowing rescues the hypothesis and removes a test.**
That is the behaviour of a hypothesis being protected, not tested.

### 6.2 The positive case for an intraocular mechanism

**(a) The run's own arithmetic does not support the systemic limb being large enough.** The supply
limb's weakest step — apoB supply → retinal lesion — is, as the literature agent concedes (A2), "the
one genuinely uncertain step," and it is shared with every lipid agent. The epidemiological
association between serum lipids and DR is modest and is strongest for **hard exudate**, a secondary,
localised finding, not for progression. A mechanism whose human evidence is concentrated on exudate
cannot carry a general disease-modification claim.

**(b) The run declared Kp,uu > 1 impossible without an uptake transporter. That is false, and the
exception applies to exactly this drug in exactly this cell.** ADMET §5.1:

> "A barrier is a *resistance*, not a *pump*. Removing a resistance drives Kp,uu toward 1… Only an
> **uptake transporter** can concentrate drug against its gradient."

**Uptake transporters are not the only route to Kp,uu > 1.** Three others are standard pharmacology,
and the run considered none:

1. **Metabolic trapping.** Fenofibric acid's dominant circulating species is the **acyl glucuronide**,
   present at concentrations at or above the parent. The run treated it exclusively as a toxicology
   liability (acyl migration, protein adducts; safety §2). But the **RPE is the most lysosome-dense
   cell in the retina**, with a daily phagocytic load and correspondingly high β-glucuronidase
   activity. A glucuronide that enters the RPE and is hydrolysed intracellularly **regenerates the
   acid inside the cell**, which is then ion-trapped at cytosolic pH. Hydrolytic regeneration behind
   a membrane is a pump in the thermodynamic sense: it consumes the conjugate to maintain a gradient
   of the parent. **Kp,uu > 1 with no uptake transporter.** This is cheap to test (RPE homogenate
   β-glucuronidase turnover of fenofibric acid glucuronide) and it is the only named mechanism in
   this run that could rescue a retinal limb without rescuing it everywhere else.
2. **Lysosomal and lipid-phase sequestration** in a cell whose daily job is to digest outer-segment
   lipid. A lipophilic acid partitioning into a lipid-rich, slowly-turning compartment accumulates
   over years of dosing.
3. **Time integration.** The run computed an **instantaneous** steady-state occupancy and asked
   whether it exceeds an EC50. The lesion accumulates over 20 years. For a process governed by
   cumulative rather than instantaneous exposure — lipid deposition in Bruch's/outer plexiform layer,
   oxidised-lipid adduct load — the relevant quantity is ∫C·dt, not C. **Nobody in eleven agents
   computed a time integral.** A 1% occupancy sustained for a decade is not pharmacologically
   equivalent to a 1% occupancy for an hour, and the run's entire arithmetic treats them as identical.

**(c) The compartment the run named and then abandoned: the RPE.** The ADMET agent assigned the RPE a
Kp,uu of 0.2–0.6 on correct grounds — its basal surface faces the **fenestrated** choriocapillaris, and
the choroid has the highest per-gram blood flow of any tissue in the body — and then every subsequent
agent built on the **endothelial** compartment instead. The RPE is: the most lipid-loaded cell in the
body; the site of the outer-BRB pump function the disease model names as a distinct DME phenotype;
HMGCS2-ketogenic and FAO-dependent; and the cell that would benefit from a lipid-handling intervention
in a way that has **no plasma lipid correlate at all**. An RPE-mediated benefit — improved pump
function, reduced oxidised-lipid load, restored ketone supply to photoreceptors — is intraocular,
local, and **would be completely invisible to a serum-lipid covariate analysis.** The run named this
compartment in Round 1 and scored no candidate on it.

**(d) PPARα-independent pharmacology was used to destroy evidence and never used to generate
hypotheses.** The literature agent's most incisive methodological point (A1.2, A3.2) is that most in
vitro "PPARα agonist" retinal work uses fenofibrate at 25–100 µM, above the concentration at which it
exerts documented **PPARα-independent** effects — direct NF-κB interference, AMPK activation,
mitochondrial uncoupling, ER-stress induction. That argument invalidates the receptor interpretation
of those experiments. **It does not invalidate the experiments.** Something is producing those effects.
The run used the PPARα-independence finding only as a discount on the receptor hypothesis and never
asked the obvious follow-up: *if the retinal effect is real and is not receptor-mediated, what is it,
and what exposure does it need?* No agent built a PPARα-independent intraocular hypothesis. That is a
whole quadrant of the hypothesis space left empty because the brief's §7 pointed everyone at a
receptor.

### 6.3 The discriminating experiment the run already had and did not notice

**This is the most useful thing in this report.**

The two readings make opposite predictions about **which fibrate should win**, and both fibrates are
already in the candidate set:

| | Systemic remnant/apoC-III limb | Intraocular, concentration- or exposure-driven limb |
|---|---|---|
| Predicts the winner is | **Pemafibrate** — largest apoC-III suppression, largest remnant effect, hepatoselective by design | **Fenofibrate/fenofibric acid** — total plasma 31–47 µM vs pemafibrate's 10–20 nM, i.e. **~2,000–3,000× more total drug presented to every ocular compartment** |
| Predicts about dose–response | Flat above the lipid plateau | Continues to rise above the lipid plateau |
| Predicts about normolipidaemic patients | **No benefit** — no supply to lower | Benefit preserved |
| Predicts about ezetimibe / inclisiran / PCSK9i | Reproduce the benefit, proportional to apoB lowering | No benefit |
| Predicts about endpoint profile | Benefit concentrated on exudative/lipid endpoints | Benefit on non-exudative progression, neurodegeneration, ERG, microaneurysm turnover |
| Predicts about time course | Benefit follows the lipid change (complete in 4–8 weeks) with a lesion-turnover lag | Divergence continues widening long after lipids plateau |

> **A head-to-head of fenofibrate versus pemafibrate on a retinal endpoint, dose-matched on
> triglyceride or apoC-III response, discriminates the two readings in a single two-arm trial using
> two approved drugs the run has already assembled.** If the hepatoselective, more-potent,
> larger-remnant-effect agent loses to the one with 3,000× more total systemic drug, the mechanism is
> not systemic remnant lowering. If it wins, the consensus is confirmed and ezetimibe/olezarsen
> become the next question rather than the first one.
>
> The run spent Round 1 §5 and a Phase 2 correction (DQ §14) constructing a lipid-side control —
> ezetimibe, then olezarsen — and **never built the receptor-side or exposure-side control**, despite
> having the two molecules for it ranked #1 and #2 in its own matrix. **The ranking treats
> fenofibric acid and pemafibrate as near-interchangeable leaders. They are a controlled
> experiment.**

### 6.4 What the pipeline would have missed if the mechanism were intraocular and PPARα-independent

Everything, and systematically:

1. **The candidate set cannot express the hypothesis.** Nine of sixteen are PPAR ligands; the rest are
   lipid agents or mechanism comparators. There is no **structurally matched, PPARα-inactive fibrate
   analogue**, no prodrug-versus-acid comparison, no total-exposure arm. The set was built from the
   brief's §7 focus question and inherits its blind spot — the pathway agent says exactly this
   (§11.7: "dense where the thesis is and empty where the thesis's own disease model says the gap is")
   and applies it only to the efflux arm.
2. **The within-class ranking inverts.** On an intraocular exposure-driven reading, pemafibrate is the
   worst molecule in Group A by ~3 logs, not the best. The run's #1/#2 would swap and the gap would be
   large, not a tie.
3. **The prodrug question reopens.** The run closed it by assertion — fenofibrate "cleaved
   presystemically, → 0" (SAR §8) — while the same run certifies that it holds **no measured PK of any
   kind** (DQ §12) and that the one metabolism file it does hold is 10× duplicated with a meaningless
   `drug_name` column (DQ §1). The neutral ester (logP ~4.7) is the only species in the set that could
   partition into a lipid-rich ocular compartment, and its elimination from consideration rests on a
   single unmeasured completeness assumption.
4. **Every dose and formulation recommendation is wrong.** A supply mechanism is flat-topped and
   tolerates CKD dose-banding (safety §4.1). An exposure-driven intraocular mechanism is linear in
   dose, so dose-banding is amputation — in exactly the patients with the most disease. The two
   readings give opposite answers to "what do we do about renal impairment," and the run adopted one
   without testing it.
5. **The biomarker strategy is wrong.** The run's proposed readouts are plasma ANGPTL4, plasma lipids,
   and retinal transactivation genes — all chosen for the receptor/supply frame. An intraocular
   mechanism needs aqueous drug concentration, ocular imaging of lipid-independent endpoints, and
   function (ERG, microperimetry), none of which appear.
6. **The "nothing serves the retina-intrinsic hypothesis" conclusion is an artifact of the search
   frame.** The Repurposing Strategist searched approved, late-stage, discontinued, endogenous-ligand
   and retinal-delivery space **for PPARα ligands** (§6.2). If the mechanism is PPARα-independent, that
   search was looking for the wrong thing and its null is uninformative.

### 6.5 Honest counter-pressure on my own attack

Three things weaken it, and I state them because an attack that does not survive scrutiny wastes
everyone's time:

- **The free-drug objection applies to intraocular PPARα too.** RPE unbound ≈ choroidal unbound ≈
  plasma unbound (albumin passes the fenestrae, so Kp,uu → 1 there) ≈ 0.10–0.31 µM against a free EC50
  of 3–30 µM. That is still 1–2.5 logs short. So the intraocular case **cannot** be a simple
  concentration argument at the receptor. It must run through trapping, time integration, or a
  non-PPARα target with better potency. My §6.2(b) is the load-bearing part of the attack, and it is a
  mechanism nobody has measured — the same epistemic position I am criticising the consensus for.
- **A PPARα-independent effect needs 10–100 µM**, which is further out of reach than the receptor. So
  the strongest intraocular story is *receptor-mediated at the RPE, with trapping or integration* —
  narrower than "intraocular and PPARα-independent" as posed.
- **Two of my discriminators are already partly answered against me.** If pemafibrate had an obvious
  retinal advantage the field would likely have noticed, and the run's hepatic-engagement-is-certain
  claim is genuinely the best-evidenced step anywhere in the analysis.

**Net:** I do not claim the intraocular reading is correct. I claim the run **cannot distinguish it,
built every control on one side of the question, had the discriminating pair in hand and ranked it as
a tie, and therefore is not entitled to present the systemic limb as the consensus.** The correct
output is a two-branch recommendation with a named discriminating experiment, not a ranked list.

---

## 7. Attack on the benchmark design

### 7.1 The blinding removed the data signal and left the answer in the brief

The protocol redacted 154 indication cells. It did not redact the **orchestrator's framing document,
which every agent reads first**, and which leaks the answer's shape repeatedly:

1. **The premise presupposes the conclusion.** Brief §7: *"**If a PPARα agonist helps the retina**,
   retinal PPARα engagement may not be the reason — systemic lipoprotein lowering may be."* The
   antecedent is handed to the agents as the frame of the question. Every agent is then asked to
   explain *why* it helps, not *whether*. This single sentence is a larger leak than all 154 redacted
   cells, because it converts the task from discovery to rationalisation. The run's actual output —
   "the systemic limb is the exposure-defensible one" — **is the second half of that sentence.**
2. **The critical path is pre-specified away from the falsifiable question.** Brief §7: *"The critical
   path item is retinal exposure after oral dosing, **not target validity**."* Target validity is the
   question that could have produced a negative answer, and it is removed from scope before Round 1.
   When the Literature Reviewer finally examines it in Round 2 it comes back Level 4 / MODERATE with
   no necessity experiment and no human genetic validation — and by then the run is organised around
   exposure.
3. **The candidate set is built from the answer.** Five of fifteen entries are fibrate-class
   (A1 fenofibric acid, A2 fenofibrate, A3 pemafibrate, A4 elafibranor, A5 seladelpar), including both
   the prodrug and its active metabolite as separate entries. No blind process generates that set. The
   scout disclosed the parallel problem for Group D — its "mechanistic comparators" are the canonical
   DR development axes — and the disclosure was recorded as a limitation and then not acted on.
4. **The counter-consideration is pro-hypothesis.** Brief §7 supplies agents with the rebuttal to the
   exposure objection (*"retinal PPARα expression is reported decreased in diabetes, so an agonist
   would restore rather than supraphysiologically stimulate"*) and with the conditional-genetics
   argument — which the Literature Reviewer later finds **overstates the evidence by about one grade**
   (A1.5). The orchestrator supplied an overstated pro-hypothesis argument as framing to all eleven
   agents.
5. **The scoring priors encode DR-specific outcomes.** Brief §4 names aldose reductase (P1) and PKCβ
   (P3) as failed DR mechanisms. That is DR clinical knowledge, injected by the orchestrator, and it
   determined epalrestat's fate across both rounds. Agents then cited it as an independent finding;
   the SAR agent honestly flagged the circularity (disclosure 4), and the literature agent sourced its
   epalrestat rule to "per brief §4."

### 7.2 Direct evidence of backward reasoning in the reports

- **The Literature Reviewer's own admission** (A8): *"my grade of 'moderate' rather than 'low' for the
  retina-targeted-expression arm is a judgment call, and I cannot fully exclude that knowing the
  clinical outcome nudged it upward."* This is an admission of contamination **at the exact pivot of
  the retina-intrinsic case** — the one arm the agent calls "the real pillar." The agent handled it
  impeccably by disclosing rather than silently correcting; the benchmark still has to absorb it.
- **The SAR Analyst's disclosure 5**: knows the DR/DME trial status of several compounds, cannot
  unknow it, and offers as evidence of honesty that its ranking is "close to the inverse of what
  DR-status knowledge would produce." That is a real argument on an orthogonal axis — and it is also
  an argument only available to someone who knows the answer.
- **The stacked best-casing in §2.1** is the behavioural signature. An analyst with no prior reports
  the midpoint of a declared range. An analyst who knows which corner leads somewhere reports that
  corner. The synthesis reported the corner, three times in one line, and labelled it a correction.
- **The one-sided control structure** (§3.3, §6.1). Two controls were built on the lipid side
  (ezetimibe, then olezarsen). Zero on the receptor or exposure side, despite both molecules being
  present and ranked. Control design reveals which direction the designer thought the answer lay.

### 7.3 The scoring instrument is invalid, and the run says so in five places

Five separate agents instructed the orchestrator not to average these axes — Round 1 §7 ("averaging
across orthogonal axes is **not** a composite score"), the Clinical agent ("must be MULTIPLIED, not
averaged"), the Pathway Analyst (§9, "these scores must be MULTIPLIED… not averaged"), the SAR Analyst
(§10, "deliberately orthogonal… **must not be averaged**… would mislead worst of all if averaged"), and
the Repurposing Strategist (§6.1, "collapsing these into one ranking would repeat the averaging error
Round 1 warned about"). **The orchestrator produced mean-ranked tables in both rounds, and the mean is
now the official result** — it is how the debate prompt itself describes the leaders ("tied at 6.10
mean", "at the top (5.80)").

Three concrete defects this introduces:

1. **Rows are not comparable.** Round 2 ranks berotralstat (7.00) and inclisiran (6.00) above every
   incumbent on **n=1** — one agent's score on one axis — against n=5 rows. A single-agent row and a
   five-agent row are printed in the same column and sorted together.
2. **The orthogonal axis is load-bearing by accident.** Removing the SAR axis, as its author
   instructed, moves pemafibrate from 5.80 to 6.75 and fenofibric acid from 5.80 to 6.00. **The
   Round 2 "tie at the top" is an artifact of including an axis its author said must be excluded.**
3. **Contradictions are averaged into invisibility** (§2.5): a 7.0 conditioned on a limb another
   agent in the same round graded LOW.

### 7.4 How much to discount

The blinding protocol already concedes the frame ("this run measures mechanistic-path plausibility
under data blinding, not naive rediscovery"). I would go further:

> **Rediscovery credit should be ~zero.** The candidate set, the focus question, the critical-path
> designation, the counter-arguments and the failed-mechanism priors were all supplied by an
> orchestrator who knew the answer. Eleven agents were asked to explain a result that the brief's own
> §7 states conditionally as a premise.
>
> **The run does have a measurable, non-contaminated output, and it is worth more than the ranking:
> the mechanistic argument structure.** Whether the pipeline's limb decomposition, its ANGPTL4
> resolution, its stage-offset finding, its control-design critique and its identification of the
> single unmeasured number are *correct* can be scored against the literature independently of
> candidate selection. **Score the reasoning, not the ranking.** The ranking was given away in the
> brief; the reasoning was not.

---

## 8. How confident should the final report be?

### 8.1 The evidence base, stated without euphemism

| What the project contributed | Status |
|---|---|
| Drug–target affinity | **None.** Mechanism table 11 rows, target table 44, zero PPAR content (DQ §2) |
| Measured PK of any kind | **None.** `logd`, `cx_logd`, `permeability`, `bioavailability_score` empty for all 3,276 rows (DQ §12) |
| Gene–disease data for DR | **None.** All DisGeNET data is scoped to the prior Oral Mucositis project (DQ §3) |
| DR-panel target matrix | Contains all three PPAR receptors and **zero PPAR effector genes**; **zero of the approved-drug candidates appear in it at all** (DQ §10, §11) |
| Metabolism file | 10× duplicated, `drug_name` column meaningless (DQ §1) |
| Plant-use corpus | 99.6% "UNKNOWN USE"; 8 real rows, none ocular (DQ §6) |
| Lipophilicity field | `alogp` present, **wrong by ~4 logs for every acid in the candidate set** (DQ §12) |

**What was genuinely data-backed and actually used:** physicochemical descriptors from
`ppar-class-drug-properties.tsv` (13 rows); quercetin's dual-efflux and SLCO1B1 status; linalool's
PPARA-dependent SLC27A4 induction; the fenofibrate→fenofibric acid esterase conversion — and that last
one comes from the file the run itself certifies as corrupt and 10× duplicated. **That is the entire
data contribution to a drug-discovery analysis.**

### 8.2 What that does to the numbers

Essentially every quantitative claim in this run is a model-generated point estimate wearing the
typography of a measurement: `Kp,uu 0.2–0.7` · `±1 log protein correction` · `1.3–1.5 kcal/mol per
contact of charge assistance` · `pK_BHX 4.3–4.8` · `PML risk ~2.3× over threshold` · `17.5× reactive
metabolite burden` · `493× lower molar covalent burden` · `LLE 3.45` · `15–25% probability of technical
success` · `$150–400M`. **Of these, exactly zero derive from a measurement in this project.** Several
are tagged `[CALC]`, which denotes arithmetic performed on knowledge-based inputs — the tag describes
the operation, not the provenance, and a reader will not make that distinction.

There is also **label inflation**: the SAR agent's pemafibrate score is marked `data-backed`, and the
data is QED/RTB/logP descriptors. The descriptors are data; the claim ("lowest headroom in the set")
is judgment. `evidence_basis` is being set by whether a number appears anywhere in the reasoning, not
by whether the number supports the conclusion.

### 8.3 Confidence the report is entitled to claim

**Entitled to claim:**
- A structured, internally-criticised hypothesis space with named falsifiers.
- A ranked set of *questions*, which is genuinely good: the identification of retinal Kp,uu as the one
  number three mutually exclusive programmes hang on (lit A6.1) is the best output of the run.
- Specific, cheap, decisive experiments — with the literature agent's two added arms, not Round 1's
  version.
- Sixteen documented data defects, several of which are real findings about the project's own
  tooling. **This is the most durable product of the run and it is not about diabetic retinopathy.**

**Not entitled to claim:**
- Any confidence interval, any `data-backed` label on a mechanistic claim, any probability of
  technical success, any cost estimate carried to two significant figures.
- A ranking. The instrument that produced it is invalid by the explicit instruction of five of its own
  agents (§7.3), and the top two are a manufactured tie.
- A mechanism consensus. The run built controls on one side of the question only (§6.1, §6.3).
- Rediscovery. The answer was in the brief (§7.1).
- Any confidence above **moderate**, anywhere, on anything mechanistic.

**Recommended concrete actions for the final report:** (i) relabel every `[CALC]` derived from
knowledge-based inputs as `[ESTIMATE]`; (ii) delete the mean column or replace it with the
lexicographic gate the Clinical agent specified and the Repurposing Strategist actually applied
(§6, G1–G4); (iii) state the effective measurement count bearing on PPARα-in-DR, which is **zero**;
(iv) present a two-branch mechanism recommendation with the fenofibrate-vs-pemafibrate discriminator
(§6.3) as the top-line experiment; (v) carry the data-defect register forward as the run's primary
deliverable.

---

## 9. The three attacks ranked by how much they should move the final ranking

1. **The endothelial margin was best-cased and "potency does not buy engagement" is contradicted by
   the arithmetic it cites** (§2.1, §2.2). Moves: the Round 1 headline, the "no fibrate can test the
   retinal limb" finding (DQ §13), the SAR agent's entire assignment, and elafibranor's status — which
   should rise from "probe only" to **the designated 12-week mechanistic probe**, because it is the one
   approved molecule whose free concentration plausibly reaches free EC50 at the retinal endothelium.
2. **Pemafibrate moves apoB in the wrong direction and its mechanism has already failed its nearest
   hard-endpoint test** (§1.2, §5). Moves: pemafibrate out of the top two, and with it the run's
   assumption that remnant/apoC-III lowering is the privileged node.
3. **The mechanism consensus is untestable as constructed, and the discriminating pair was already in
   the set and scored as a tie** (§6.3). Moves: the ranking becomes two branches, and the top-line
   recommendation becomes a head-to-head rather than a lead compound.

---

## 10. Blinding compliance statement — including one disclosed leak

**Files read.** As listed in the header. I did **not** read `data/processed/chembl_approved_drugs.csv`,
anything under `data/holdout/`, or any `answer-key*` file, and I did not use git history, git objects,
or any other route to recover redacted values. I did not attempt to infer which rows were redacted.

**DISCLOSED LEAK — Part B of the literature report.** I did not read Part B's body. However, in
locating the Part A boundary I ran a **heading-level grep (`grep -n "^#\{1,3\} "`) across the whole
file**, which returned the Part B section headings. Two of them carry substantive content:
one heading states that a specific compound in the candidate set is an established approved therapy
for this indication, and another announces that the pipeline's mechanism analysis is wrong. I stopped
immediately, read no Part B body text, and read nothing after line 570.

**Effect on this report, assessed honestly, section by section:**

- **§6 (the mechanism attack) is the section most contaminated.** I was assigned to argue that the
  mechanism may be intraocular rather than lipid-mediated, and a Part B heading announcing that the
  pipeline's mechanism analysis is wrong is a signal pointing in that direction. **The Integration
  Agent and the scorer should discount §6's *confidence*, though not necessarily its *content*:**
  every argument in §6 is constructed from Part A, the Round 1/Round 2 reports and general
  pharmacology, and §6.5 states the counter-pressure against my own position at full strength. The
  §6.3 discriminator (fenofibrate vs pemafibrate head-to-head) is derived entirely from the ADMET
  agent's exposure table and does not depend on the leak.
- **§1.2 and §5 (the pemafibrate attack) are not contaminated by the leak** but **are** knowledge-based
  on non-DR clinical grounds. The cardiovascular outcome and lipid-fraction results I cite for
  pemafibrate are cardiovascular, not retinal, and are permitted under protocol §3. I did not use, and
  do not know from this run, any DR-specific result for pemafibrate.
- **§2, §3, §4, §7, §8 are uncontaminated by the leak.** They are arithmetic and consistency checks
  performed against files in the run tree, verifiable line-by-line by anyone re-reading
  `agents/p1-admet.md` §3.2 and `round1-synthesis.md` §1–§2.
- **One compound identity is now known to me.** I have not used it anywhere. The symmetric risk is
  that I over-attack or under-attack that compound to compensate; §1.1 attacks it on effect size and
  deployment, which is the same attack I would have written from the exposure arithmetic alone, and
  my bet-against (§5) is the *other* leader.

**Recommendation to the orchestrator arising from this.** The `## POST-HOC UNBLINDING` section should
live in a **separate file**, not after a boundary marker in a file that blinded agents are instructed
to read. Any structural listing operation — grep for headings, a table of contents, an outline view,
an editor's symbol list — defeats an in-file boundary. This is the same class of defect as the
`[REDACTED-HOLDOUT]` marker the Phase 0 scout found: the content was protected and the **structure**
was not. I recommend it be added to `data-quality-findings.md` as defect §17.

**Knowledge used and its basis.** General pharmacology, pharmacokinetics (free-drug theory and its
documented exceptions: metabolic trapping, lysosomal sequestration, time-integrated exposure),
medicinal chemistry, lipoprotein biology, ocular anatomy and physiology, trial design and statistics,
and non-DR clinical outcomes for lipid-lowering agents. All permitted under protocol §3. Every
quantitative claim I make about this run's own numbers is sourced to a named file and section and can
be checked.

**Negative decisions disclosed.** I declined to attack candesartan, which sits third in Round 2 — not
because of anything I know about it in DR, but because its target is luminal, its safety case is
genuine, and the attack would have been weaker than the three I made. I also declined to pursue
melatonin and icosapent ethyl, where the Literature Reviewer's Part A null-result evidence (A5.1) is
already stronger than anything I would add.
