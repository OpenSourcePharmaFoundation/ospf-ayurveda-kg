# P3 — Clinical Feasibility Assessment: Diabetic Retinopathy

**Agent:** Clinical Feasibility Assessor (reassigned; same agent as P1 Clinical Landscape)
**Run:** blinded benchmark, 2026-10-05
**Axis:** practical feasibility of reaching patients — NOT DR efficacy, NOT mechanism validity.

---

## 0. Scope, inputs, and the one methodological deviation

**Read:** `round1-synthesis.md`, `round2-score-matrix.txt`, `agents/debate-advocate.md` §1.1 and §9,
`agents/debate-integrator.md` §7–§10, `agents/p2-safety.md` §1.3, §4, §5,
`agents/p2-pathway.md` §2.3, §3.3, §4, `.claude/skills/clinical-feasibility-assessor/SKILL.md`,
plus my own `agents/p1-clinical.md`.

**Not read, deliberately:** `agents/UNBLINDING-part-b.md` (instructed), `BENCHMARK-RESULT.md`
(not instructed, but it is self-evidently a post-hoc scoring artefact and therefore an answer-key
file under brief §1.1 — I noticed it in the directory listing and did not open it),
`agents/p2-literature.md` (not on my read list; skipped entirely rather than risk its post-hoc
section), `data/processed/chembl_approved_drugs.csv` and everything under `data/holdout/`.

**Methodological deviation, declared.** `clinical-feasibility-assessor/SKILL.md` instructs the agent
to work from `data/processed/chembl_approved_drugs.csv` and `chembl_drug_indications.csv`. Both are
forbidden under the blinding protocol for this disease. The skill is also anchored to Oral Mucositis
throughout — an acute, 4–6 week, topically-treatable condition. **Almost every cost modifier in it
inverts for DR**, which is chronic, lifelong, posterior-segment and systemic. I have re-anchored the
framework and flag the three places the OM anchoring would have produced a wrong answer:
OM's "topical formulation → cheaper preclinical package" (DR: topical is a dead letter, model §6.3);
OM's "acute condition, short follow-up" (DR: 4–5 year endpoints); and OM's "placebo acceptable, no
standard of care" (DR: an effective procedural standard exists for late disease, so placebo is only
ethical in early disease or as add-on).

---

# PART I — AUDITING MY OWN FINDING

## 1. (a) The screening-embedded design: real, or too good to be true?

In P1 I claimed that embedding an early-DR trial in a national screening programme — which already
performs fundus photography on every diabetic as routine care — collapses marginal per-patient cost
from ~$15,000 to ~$2,000, turning a $60–100M programme into a $15–25M one.

**Verdict: the finding is real in direction and overstated by roughly 2× in magnitude. It survives
audit, with three corrections and one structural split.** Here is the audit.

### 1.1 Correction 1 — imaging grade. The biggest technical problem, and it is real.

| | National screening programme | Registrational DR trial |
|---|---|---|
| Capture | Non-mydriatic (or minimally mydriatic), **1–2 field, 45°** digital colour | **Stereoscopic 7-standard-field 30°**, mydriatic, certified photographers |
| Graded to | A **referral taxonomy** (R0–R3 / M0–M1, or ICDR levels) — typically 4–5 bins | **ETDRS DRSS, 11–13 steps**, certified masked reading centre |
| Purpose | "Does this person need to see an ophthalmologist?" | "Did this eye move 2 or 3 steps?" |

The gap is not resolution — it is **which lesions are gradeable**. Venous beading and IRMA, the
features that define the moderate→severe NPDR transition where most of the registrational signal
lives, are poorly detected on a single non-stereo 45° field. A screening-grade image stream can
support *progression to referable DR*; it **cannot** support a certified DRSS step change.

> **Consequence: the pure registry endpoint is an effectiveness endpoint, not a registrational one.**
> That is a genuine limitation and I did not state it in P1.

**Mitigation, and what it costs.** Add a protocol-grade capture — mydriatic 4-field, or better, a
single ultrawide-field image, which is *faster* than 7-field stereo and increasingly deployed — at
baseline and at 2–3 follow-up rounds, graded centrally. At 6,000 patients × 2 eyes × 4 timepoints =
48,000 grading sets at ~$40 each ≈ **$2M**, plus camera access. Real money; not programme-breaking.

### 1.2 Correction 2 — adherence dilution. The largest single correction, and it is arithmetic.

A pragmatic trial with annual contact has almost no adherence support. Real-world adherence to an
asymptomatic preventive oral over four years is plausibly **55–70%**. ITT effect scales roughly with
adherence, and sample size scales as 1/effect².

| | Conventional, supported trial | Registry-embedded, pragmatic |
|---|---|---|
| Assumed adherence | ~85% | ~60% |
| True per-protocol RRR | 30% | 30% |
| Observed ITT RRR | ~26% | ~18% |
| n per arm (15% control event rate, 90% power) | ~1,530 | ~3,390 |
| n total before dropout inflation | ~3,060 | ~6,780 |

**Adherence dilution inflates the required sample roughly 2.2×.** That eats more than half of the
per-patient cost saving, and I did not account for it in P1.

The registry design does, however, *win* on the other half of the problem. **Endpoint
ascertainment is better, not worse**: the endpoint is captured at a screening encounter the patient
attends anyway, and non-attendance is itself tracked by the programme — so loss to follow-up on the
*endpoint* approaches the programme's own non-attendance rate rather than a trial's dropout rate.
**The registry design trades adherence for ascertainment.** Both matter; the trade is survivable.

*Adherence mitigations that are nearly free in this setting:* measure adherence from **national
pharmacy dispensing records** (complete, passive, free in single-payer systems — a registry
advantage nobody has named); pre-specify a complier-average causal effect analysis using
randomisation as the instrument alongside the ITT; and consider a short run-in to shed early
discontinuers, at a stated cost in generalisability.

### 1.3 Correction 3 — consent and governance. The real binding risk, and it is institutional.

This is where the design most plausibly dies, and it is not a scientific problem.

- Randomising a drug is an **interventional trial**. No routine-care data waiver applies. You need
  ethics approval per jurisdiction, a lawful processing basis, controller/processor agreements
  between programme, sponsor and reading centre, and — unavoidably — **an individual research
  consent encounter**. Budget **$300–800 per consented patient** for research-nurse time and
  documentation. That is a real floor under the "the photo was free" argument.
- Harder than the paperwork: a national screening programme is a **public health service whose
  public trust depends on being seen as purely diagnostic.** Programme owners are frequently and
  reasonably reluctant to let a drug trial ride on it, and most have no GCP-trained staff and no
  research arm. **A failed negotiation here destroys the entire cost advantage, and it is the single
  largest programme risk in this assessment.**
- **The precedent that makes it credible anyway:** registry-randomised controlled trials embedded in
  national quality registries are an established methodology with a track record in cardiology,
  where randomisation was bolted onto an existing national registry and delivered large randomised
  evidence at a small fraction of conventional cost. The model is proven; it has simply never been
  applied to this screening infrastructure. Pick partners that already have a research arm.

### 1.4 The structural split this forces — and it is an improvement

The audit resolves into a **two-tier design that gets both products**, which is better than what I
proposed in P1:

| Tier | n | Imaging | Blinding | Endpoint | Delivers | Cost |
|---|---|---|---|---|---|---|
| **Pragmatic shell** | ~6,000–7,000 | Screening-grade + protocol captures | **PROBE** (open-label, blinded central endpoint) | Progression to referable DR | Effectiveness evidence, EML dossier, LMIC deployability, adherence realism | ~$3,000–4,500/pt → **$20–30M** |
| **Nested registrational cohort** | ~1,200 (inside the shell) | Upgraded mydriatic 4-field / UWF, certified reading centre | **Full double-blind**, firewalled labs | ≥3-step DRSS | Regulatory filing | ~$15,000/pt → **~$18M** |

### 1.5 Audited verdict on (a)

| | P1 claim | Audited |
|---|---|---|
| Marginal per-patient cost | ~$2,000 | **$3,000–4,500** (imaging upgrade + consent encounter) |
| Sample size | ~5,000 | **~6,000–7,000** (adherence dilution) |
| Total | $15–25M | **$25–40M** (both tiers: $38–48M) |
| vs conventional | 4× cheaper | **~2–2.5× cheaper** |
| Registrational on its own? | implied yes | **No** — needs the nested cohort |
| Biggest risk | not stated | **Programme-governance negotiation, not science** |

> **The finding survives.** A 2–2.5× cost reduction, better endpoint ascertainment, a realistic
> adherence readout, and an LMIC-relevant evidence base are worth having, and this is still the only
> route I can identify that makes a four-to-five-year early-DR trial affordable. But "$15–25M and
> registrational" was too good to be true, and I should not have said it without the imaging-grade
> and adherence corrections.

---

## 2. (b) The dilution argument — does renal dose-banding sink the trial?

The Devil's Advocate (§1.1, point 2): ~30–35% need a ~3-fold dose reduction, 5–10% are excluded,
and retinopathy and nephropathy track together — so the effect is carried by the healthiest third
while the high-event third is under-dosed.

**Verdict: it does not sink the trial under the mechanism the run has chosen to develop. It would
sink a retinal-limb trial. And the quantity that separates those two cases is measurable inside the
trial for free.**

### 2.1 The argument's force depends entirely on which limb is operating — and it inverts

The Safety agent (§4.1) established the pharmacology both sides are using:

- **Systemic/hepatic limb** — transporter-mediated, concentrative, **saturable**; dose–response for
  remnant lowering is flat-topped. A 3-fold dose cut costs it **~20–30%**, not 67%.
- **Retinal limb** — passive, **linear in free plasma concentration**. A 3-fold dose cut costs it
  the full **3-fold**.

### 2.2 The arithmetic, done properly — including the event-rate correlation

The Advocate's sharpest point is not dilution but **anticorrelation**: events concentrate where
the dose is lowest. Model it. Assume eGFR 30–59 carries ~2× the event rate of eGFR ≥60 (albuminuria
and eGFR decline are strong progression predictors), and that eGFR <30 is excluded at randomisation.

| Stratum | Population | Relative event rate | **Share of all events** | Effect retained (systemic limb) | Effect retained (retinal limb) |
|---|---|---|---|---|---|
| eGFR ≥60 | 60% | 1.0 | 48% | 1.00 | 1.00 |
| eGFR 30–59 | 32% | 2.0 | 52% | 0.75 | 0.33 |
| eGFR <30 | 8% | — | excluded | — | — |

**Event-weighted effect retained:**
- Systemic limb: 0.48×1.00 + 0.52×0.75 = **0.87** → a **13% loss of effect**, and sample size
  inflates by 1/0.87² = **1.32×**.
- Retinal limb: 0.48×1.00 + 0.52×0.33 = **0.65** → a **35% loss**, sample size **2.35×**.

> **The answer, stated plainly: under the systemic limb the renal dose-banding costs ~13% of effect
> and ~30% more patients. That is a budget line, not a trial-killer. Under the retinal limb it costs
> 35% of an effect that the run has already judged to be 1–3 logs short of threshold, which is
> fatal — but that limb is already dead on other grounds.**

**The Advocate is therefore right about the mechanism and wrong about the conclusion:** the finding
he identifies is real, he has correctly spotted that the Safety agent's framing understates it by
ignoring the event-rate correlation, and the corrected magnitude is still roughly a third of a
sample-size multiplier rather than a programme veto.

### 2.3 The reframing — the banding is a free within-trial mechanism discriminator

This is the constructive finding, and I believe it is new to the run.

The two limbs predict **quantitatively different eGFR-band × treatment interactions**: ~25% effect
attenuation in the reduced-dose stratum under the systemic limb, ~67% under the retinal limb.

> **So the renal dose-banding that the Advocate calls a fatal flaw is simultaneously a built-in,
> cost-free, within-trial natural experiment on the question the entire run has been unable to
> answer.** Pre-specify the eGFR-band × treatment interaction as a key secondary with a stated
> prediction, and the trial that was supposedly diluted by dose-banding instead *uses* the dose
> banding to discriminate the mechanism. No extra arm, no extra patient, no extra cost.

### 2.4 A bias nobody has stated — creatinine-based banding under-doses the active arm over time

The Safety agent (§4.3) showed the fibrate creatinine rise is predominantly analytical and
secretory, not filtration loss, and that CKD-EPI eGFR scales as creatinine^(−1.2), so a 15%
creatinine rise reads as a ~17% apparent eGFR fall.

Now apply that **inside the trial's own dose-banding rule**:

> A patient at true eGFR 64 on active drug reads as ~53 after starting. The protocol down-bands
> them. **This happens only in the active arm.** Over four years, creatinine-based banding
> therefore progressively and asymmetrically **under-doses the treated arm** — manufacturing
> precisely the dilution the Advocate fears, as an artefact of the measurement rather than the
> disease.

**This is a trial-integrity bias, not just a safety nuisance, and I have not seen it stated.**
Mitigation is the Safety agent's own: **cystatin-C-based eGFR as the sole banding and decision
variable**. One assay now solves four problems — the iatrogenic prescribing cascade, the renal
unblinding tell, the spurious down-banding bias, and the validity of the §2.3 interaction test.

### 2.5 The five design mitigations

1. **Stratified randomisation on eGFR band** (≥60 vs 30–59). Mandatory; guarantees balance and
   makes §2.3 estimable.
2. **Pre-specify the band × treatment interaction with a directional prediction** (§2.3).
3. **Cystatin-C eGFR as the sole banding variable** (§2.4). ~$25/assay × 36,000 assays ≈ **$0.9M**.
4. **Match the molecule to the problem.** Pemafibrate is hepatobiliary and needs no banding — the
   dilution objection is **fenofibrate-specific, not mechanism-level**. If dilution is the worry,
   the answer is the molecule. (Counterweight: pemafibrate is Japan-only, BID and branded, so it
   loses the deployment argument entirely — see §6.2 for why that bridge is more expensive than the
   Integrator costed.)
5. **Exclude eGFR <30 cleanly at screening**, never enrol-then-discontinue, which would break
   randomisation differentially.

### 2.6 The Advocate's *other* point is the more serious one, and it has a better fix

His point 1 — that statins have already removed 35–45% of apoB before the drug arrives, so the
mechanism operates on a shrunken residual — is a larger threat than the renal argument and nobody
has costed it either. **But it has a clean, cheap mitigation that the renal problem does not:
enrich on residual risk.** Enrol only patients with elevated remnant cholesterol / apoB particle
number **despite** statin therapy. That is ~25–35% of statin-treated diabetics, identifiable from a
routine lipid panel, and it is the population with the most headroom for the mechanism by
construction. See §3.

---

## 3. (c) The enrichment paradox — is there a valid strategy, or must this be all-comers?

The Pathway agent (§3.3, §4): hard exudate marks the **persistence** phase, where the rate-limiting
step is clearance via the self-renewing foam-cell futile cycle (§2.3), not influx. So the obvious
enrichment marker selects patients in whom a supply-lowering mechanism is weakest.

**Verdict: valid enrichment exists. The paradox is an artefact of enriching on the wrong variable —
a static deposit instead of a rate. Enrich on the SUPPLY term and the RATE; never on the DEPOSIT.**

### 3.1 Why the deposit is the wrong variable

The Pathway agent's own quotient makes it obvious:

```
deposit_burden ≈ influx_rate / clearance_rate
```

A supply agent acts on the **numerator**. Enriching on *burden* selects high numerator **or** low
denominator, and §3.3 says that by the time a deposit is visible the denominator is what is
binding. Enriching on burden is therefore enriching on the wrong half of the quotient. A
supply-side trial must enrich on **influx rate**, which has two measurable proxies — one in plasma,
one in time.

### 3.2 The three valid criteria

**(i) Plasma-side — enrich on the supply term itself.** Elevated **apoB particle number / remnant
cholesterol / small-dense LDL despite statin**, measured by NMR or ion-mobility (not LDL-C — the
Integrator §7 condition 1 is right about this). This directly measures the quantity the drug lowers
and the quantity that drives influx, and **it does not require the lesion to have formed**. It also
answers the Advocate's statin objection (§2.6) with the same criterion. Prevalence ~25–35% of
statin-treated diabetics.

**(ii) Time-side — enrich on RATE, not state.** Eligibility = **new or worsening retinal lesions
over the preceding screening interval**, rather than lesions present. A patient who went from no
exudate to some exudate in 12 months is in the accretion phase *by definition*. This is the exact
inverse of the paradoxical marker: it selects the transition, not the endpoint of the transition.

> **And here the two halves of this assessment solve each other.** A rate-based criterion normally
> costs a year of run-in observation before anyone can be randomised. **National screening
> programmes already hold serial images at 12-month intervals on the entire diabetic population.**
> The run-in has already happened, retrospectively, for free, for everyone. Grading one prior image
> per candidate (~$40) converts a prohibitively slow criterion into the cheapest one in the set.
> **The registry infrastructure and the enrichment paradox are each other's solution, and neither
> finding is usable without the other.**
>
> *Caveat:* selecting on a recent change invites regression to the mean. Handle it by requiring the
> trend across **two** prior intervals, or by accepting it and powering on the randomised contrast,
> where regression affects both arms equally.

**(iii) Exclusion, not inclusion — exclude where nothing works.** Per Pathway §3.3, organised
subfoveal plaque is fibrosis, and "transcriptional pharmacology does not remove a scar." Exclude it.
This is the one legitimate *use* of the exudate marker: as an exclusion, not an enrichment.

### 3.3 The composite criterion, with screening arithmetic

| Filter | Fraction surviving | Cumulative |
|---|---|---|
| Diabetic adults in a screening programme | — | 100% |
| S1–S2 DR present (not S0, not S4/S5) | ~0.30 | 30% |
| New or worsening lesions over prior interval | ~0.35 | ~11% |
| Elevated remnants/apoB despite statin | ~0.55 | ~6% |
| No organised subfoveal plaque; consent; other I/E | ~0.60 | **~3.5%** |

At ~3.5% net eligibility, enrolling 6,000 means screening ~170,000 people. **In a conventional
multicentre trial this is impossible.** In a national programme that images **millions per year**,
it is a database query against patients who are already attending. **Enrichment at this depth is
only affordable inside the registry design** — which is the third place these two findings prove
to be a single finding rather than two.

### 3.4 What enrichment costs, honestly

- **It is not free on the label.** A trial enrolling S1–S2 with residual lipid risk and progressing
  lesions yields a label for exactly that population, not for "diabetic retinopathy."
- **It forecloses the exudate-clearance claim.** By excluding established plaque you have selected
  away the population in whom exudate resolution could be demonstrated. This becomes a
  progression-prevention trial, not a lesion-clearance trial. Those are different products; say so.
- **Recommended structure:** full enrichment for the Gate-1 mechanistic trial (where the goal is a
  decision); for the pivotal trial, **enrich on (i) and (iii) and merely stratify on (ii)**, with
  pre-specified hierarchical gatekeeping — the rate criterion is the least regulatorily familiar and
  is better defended as a stratifier than as a gate.

---

## 4. (d) Trial-integrity mitigations — operationalised and costed

The Safety agent (§5) ranked ten mitigations. My job is to build them, cost them, and find what
breaks. Two things break.

### 4.1 The conflict nobody has noticed: the registry design and the blinding design are incompatible

> The Safety agent's single highest-value mitigation is **blinded lipid panels** — the lipid panel
> is a near-deterministic allocation tell affecting 7 of 16 candidates. **But in a
> registry-embedded trial the patient's routine lipid panel is ordered by their own primary-care
> physician and lands in the national record. There is no mechanism by which a sponsor can suppress
> it.** The mitigation that matters most and the design that makes the trial affordable are in
> direct conflict, and neither agent could see it because each held only one half.

Three resolutions, assessed:

| Option | Workable? |
|---|---|
| Suppress routine lipids for trial duration | **No.** Unenforceable across primary care, and arguably unsafe in a CV-risk population |
| Full double-blind in the pragmatic shell | **No.** Cannot be delivered; claiming it would be worse than not attempting it |
| **PROBE — open-label, blinded central endpoint** for the shell; **full double-blind with firewalled labs** for the nested registrational cohort | **Yes.** Two blinding levels, one trial |

**PROBE is defensible here precisely because of the Safety agent's §5.1 reassurance:** the primary
endpoint is centrally graded from images by readers masked to allocation, site and sequence, so the
endpoint itself is structurally protected. The damage runs through **rescue decisions and background
management**, and those are hardened directly (items 5 and 6 below) rather than through blinding.

### 4.2 The mitigation package, specified and costed

| # | Mitigation | Specification | Cost (5-yr, ~6,000 pts) |
|---|---|---|---|
| 1 | **Central masked reading of all imaging** | Readers masked to arm, site and visit sequence. Non-negotiable; it is what makes PROBE survivable | in imaging budget (~$2M) |
| 2 | **Firewalled unblinded safety team** | 1 physician + 1 pharmacist at coordinating centre; **no** site role, **no** endpoint role, **no** DSMB vote. Output restricted to a 5-item controlled vocabulary — CONTINUE / REDUCE TO LEVEL 2 / HOLD 4 WEEKS / PERMANENTLY DISCONTINUE / URGENT REVIEW — **with no values ever attached** | ~2 FTE → **$1.5–2.5M** |
| 3 | **Blinded lipid panels** | Nested double-blind cohort only (§4.1). Central lab → firewall only | ~$0.3M |
| 4 | **Cystatin-C eGFR as sole renal decision variable, all arms** | Creatinine reported only inside the firewall. Solves four problems at once (§2.4) | ~$0.9M |
| 5 | **Protocolised rescue with masked adjudication** | Referral for anti-VEGF/laser triggered **only** by objective pre-specified criteria (CST threshold, BCVA loss, DRSS step, NV present), adjudicated by a masked committee **reading the same central images that drive the primary endpoint**. Off-trigger referral requires committee review. Blocks the most damaging channel and bypasses investigator belief entirely | **$0.3–0.6M** |
| 6 | **Background-management protocolisation + drift monitoring** | Identical HbA1c/BP/LDL targets pre-specified across arms. **Between-arm drift in achieved HbA1c and SBP reported quarterly to the DSMB as a blind-integrity metric with a pre-specified threshold** (e.g. >0.2% HbA1c divergence triggers investigation). If the arms diverge on HbA1c the trial is functionally unblinded regardless of what anyone reports | ~$0 |
| 7 | **Ezetimibe arm as partial lipid-tell masker** | Degrades "the lipids moved" from a 1-of-2 to a 1-of-3 call. **Honest limit: it masks "is this active?" but not "which active?"** — a −40% TG with HDL rise still identifies the fibrate. Take it as a free rider on an arm justified by mechanism discrimination; do not justify the arm on it | in arm cost |
| 8 | **Blinding index at exit** | Patients and investigators asked which arm they believe they were in; formal index as a **pre-specified reported outcome**, not an afterthought | ~$0 |
| 9 | **Placebo selection reviewed for its own biology** | Specifically if any ω-3 arm is run — the placebo oil is itself a confounder with precedent | ~$0 |
| 10 | **Design-time exclusion of unmitigable tells** | Minocycline (permanent pigmentation **seen by the ophthalmologist performing the endpoint exam**), epalrestat (chromaturia from week one), linalool (the patient is detectably fragrant). These are not risks to manage — **they are structural objections to running the trial at all**, and they belong in a feasibility score, which is where I have put them | ~$0 |

**Total integrity package: ~$3–4.5M**, i.e. roughly 10% of the pragmatic shell, for the measures
that determine whether the result means anything. This is the cheapest high-value line in the budget.

---

## 5. (e) Durability — the question nobody asked, and why it is first-order

Nothing in Round 1, Round 2 or the debate addresses whether benefit **persists after stopping**.
That omission matters more than it looks.

### 5.1 Why it is not a secondary question

The Safety agent's entire §1 — the permissible-harm calculus for "asymptomatic lifelong prevention"
— is predicated on the word **lifelong**. The acyl-glucuronide covalent-burden argument, the
cumulative-exposure toxicology, the 40-year monitoring burden and the LMIC deployment economics all
scale with treatment duration.

> **If the correct product is a 5-year course in S1–S2 rather than a 40-year daily pill, the
> chronic-safety objections that dominate this entire run shrink by roughly an order of magnitude,
> and the LMIC cost and monitoring arguments change completely.** Durability is therefore not a
> nice-to-have secondary endpoint. It is the variable that determines whether the run's dominant
> objection applies at all. No agent has noticed this.

### 5.2 The mechanistic prior, stated so it can be falsified

A supply-lowering mechanism is, on its face, **rate-suppressive**: it lowers influx while present;
stop it and influx returns to baseline. But the **lesion is cumulative and partly irreversible** —
a closed capillary stays closed, a dead pericyte stays dead, an organised plaque stays organised.

> **Prediction: suppressive at the RATE level, disease-modifying at the BURDEN level.** Years of
> reduced influx buy permanently less accumulated damage, which is not given back on withdrawal —
> but no *further* benefit accrues after stopping. If true, the product is a defined course given
> during the accretion window, not a lifelong drug.

The alternative — a genuine **legacy effect**, where divergence persists or widens after treatment
stops, as described for metabolic memory in diabetic complications generally — would be the
strongest possible result. The null case — convergence back toward control — means a lifelong drug
with the full chronic-safety weight.

### 5.3 The trial element: a randomised withdrawal extension

At the end of the main treatment period (year 4), **re-randomise the active arm 1:1 to continue
versus withdraw to placebo**, carry a sample of the original placebo arm forward unchanged, and
follow all three for three further years on the same endpoint.

| Year-7 observation | Interpretation | Product consequence |
|---|---|---|
| Withdrawn arm's progression **rate** returns to control, but accumulated **burden** stays below control | Rate-suppressive, burden-modifying | **A time-limited course is a legitimate product.** Duration becomes a dose-finding question |
| Withdrawn arm's rate returns **and** burden converges toward control | Purely suppressive and reversible | Lifelong drug; full chronic-safety weight applies |
| Withdrawn arm keeps diverging from control | **True legacy effect / disease modification** | Strongest result available; short course, enormous value |
| Continue arm diverges further from withdrawn arm | Continued dosing adds benefit | Quantifies the increment of staying on |

**The safety mirror, which matters independently.** If the mechanism is suppressive, withdrawal
could produce **rebound** — remnant overshoot, or an abrupt fall in hepatic ANGPTL4. The withdrawal
arm is the only place this is observable.

> **A drug with a withdrawal rebound, deployed into a population with ~60% real-world adherence,
> is actively dangerous** — because unplanned withdrawal is not an edge case, it is the modal
> patient experience. The randomised withdrawal arm is therefore a safety requirement for
> population deployment, not merely a product-definition study.

### 5.4 What it costs

- Power on the **rate** comparison (a slope contrast), which is far more efficient than cumulative
  incidence. Re-randomise ~1,200 active (600 continue / 600 withdraw) + ~600 placebo = **~1,800**.
- Inside the registry shell the endpoint is again the routine screening encounter; drug is generic
  and half the extension is placebo.
- **Cost: $8–15M for three years.** In a conventional standalone design the same question costs
  **$35–55M**, which is why nobody asks it. **The registry shell is what makes the durability
  question affordable** — the fourth place where these findings prove to be one finding.
- **And the tail is nearly free.** The screening programme keeps imaging these patients annually
  forever, trial or no trial. **The marginal cost of a further 5–10 years of observational
  follow-up on the randomised cohorts is close to zero.** No conventional trial can say that.

### 5.5 The cheap partial answer that runs years earlier

A **washout substudy** inside the Gate-1 mechanistic trial: in ~150 patients at month 12, stop drug
for 8 weeks and measure reversion of plasma remnants/apoC-III/ANGPTL4 and of OCT hyperreflective-foci
burden. **~$300–600k.** It cannot answer structural durability, but it establishes whether the
*proximal* effect is exposure-dependent and whether a rebound signal exists — a necessary
precondition, available five years before the structural answer.

---

# PART II — PATHWAY, DEPLOYMENT, AND THE PLAN

## 6. (f) Regulatory strategy — extending P1 for a portfolio that is no longer all-generic

P1 §5 established the mechanics; I will not repeat them. Three things have changed since.

### 6.1 The portfolio now splits into two incompatible regulatory classes

| Class | Members | Exclusivity | Sponsor? | Deployable at scale? |
|---|---|---|---|---|
| **Generic orals** | Fenofibrate, fenofibric acid, ezetimibe, candesartan, icosapent ethyl | None that matters — US 3-yr indication exclusivity does not stop off-label generic substitution; the EU 8+2+1 window closed decades ago | **No** | **Yes** |
| **On-patent** | Pemafibrate, berotralstat, olezarsen, elafibranor, seladelpar | Real | **Yes** | **No** — branded/orphan pricing, and for olezarsen a cold-chain injectable |

**There is no molecule in either column that has both a sponsor and population-scale deployability.**
That is the structural fact the funding plan must answer, and it is not fixable by regulatory tactics.

### 6.2 The Integrator's pemafibrate → fenofibric acid bridge is regulatorily incoherent, and uncosted

The Integrator (§7) recommends pemafibrate as mechanism-validation agent with fenofibric acid as a
"second, bridging, public-health trial." As a scientific sequencing argument this is sound. As a
regulatory plan it does not work:

- Pemafibrate has **no US/EU reference listed drug** — there is no 505(b)(2) or Article 10(3) route
  for it, only a full NDA/MAA.
- **Efficacy data must reside in the molecule on the label.** You cannot validate with one molecule
  and file with another. A positive pemafibrate trial does not support a fenofibric acid label, and
  vice versa.
- **Consequence: the bridge is two full programmes, not one programme with two phases.** The
  Integrator's recommendation, costed honestly, is roughly **double** what it appears to be. Nobody
  in the run has said this.
- **Resolution:** use pemafibrate only where its properties are decisive and cheap — the Gate-1
  mechanistic trial, where no banding confound is wanted and no label is sought — and run the
  **pivotal trial in the molecule you intend to deploy**, which is fenofibrate or fenofibric acid.
  Accept the banding problem and manage it with §2.3–2.5, which the §2 analysis shows is a ~30%
  sample-size cost rather than a veto.

### 6.3 The one commercial structure where the product and the science coincide

P1 identified the fixed-dose combination as the most rational commercial structure. The enrichment
analysis in §3 now makes it specific and much stronger:

> The scientifically correct population is **"residual elevated remnants despite statin."** The
> commercially protectable product is a **statin + fibrate fixed-dose combination** — patentable,
> non-substitutable at the pharmacy counter, 3-year exclusivity, and with a genuine adherence
> rationale in a polypharmacy population. **The FDC is the only structure in which the
> commercially viable product and the scientifically indicated population are the same thing.**
> Everywhere else in this analysis the two pull apart.

Caveat, stated: an FDC requires demonstrating each component's contribution, adds bridging PK, and
raises the trial's complexity — and it does nothing for the LMIC case, where loose generics at
$0.03/day are the product.

### 6.4 If no structure justifies commercial investment — who funds it

| Funder | Realistic ceiling | Fit |
|---|---|---|
| **National health research agency** (registry-randomised trial) | $25–60M | **Best fit.** Exactly the question industry will not fund; the registry-RCT methodology is established; the screening programme is already public infrastructure |
| **International academic consortium** | $30–50M | Multiplies the screening programmes available; spreads governance risk |
| **Philanthropic blindness / diabetes funders** | $10–40M | The LMIC access gap is the argument they exist to answer |
| **Global-health funders + national programmes (India, China)** | variable | Where the burden is, where screening is scaling fastest, where per-patient cost is lowest, and — per §7.3 — where the mechanism has the **most** headroom |
| **Commercial sponsor** | — | **Only** via the §6.3 FDC, and only in high-income markets |
| **WHO EML listing** | the distribution endgame | Requires no patent. The property that destroys the commercial case is the property that makes this work |

---

## 7. (g) Global deployment

### 7.1 Cost of goods and supply chain

| Candidate | Finished-product cost | Supply chain | Chain verdict |
|---|---|---|---|
| **Fenofibrate** | **~$0.01–0.05/day → $4–18/patient-year** | Commodity API, many suppliers in India and China; small molecule, oral solid, room-temperature stable, long shelf life, no cold chain | **Best in set** |
| Fenofibric acid | ~$0.05–0.30/day | Same chemistry; fewer finished-product suppliers outside high-income markets | Very good |
| Ezetimibe | ~$0.03–0.10/day | Commodity generic, oral solid | Very good |
| Candesartan | ~$0.02–0.10/day | Commodity generic, universally listed | Very good |
| **Icosapent ethyl** | ~$0.50–2.00/day | **Soft-gel capsules; oxidation-sensitive; needs inert-gas packaging; shelf life degrades in hot, humid climates; 4 capsules/day bulk raises shipping and storage cost per patient-year** | **Poor for LMIC — nobody in this run has flagged this** |
| Pemafibrate | branded | Single-source, Japan | Not deployable |
| Berotralstat | orphan pricing | Specialty distribution | Not deployable |
| Olezarsen | very high | **Injectable ASO, cold chain** | Not deployable |

For calibration: **one anti-VEGF injection, even at a repackaged $50, is 3–12 years of fenofibrate.**
That single comparison is the whole global-deployment argument.

### 7.2 Is the monitoring burden a deal-breaker outside high-income settings?

The Safety agent's §1.3 principle — *safety that depends on monitoring does not survive translation
from a symptomatic to an asymptomatic indication* — is the sharpest deployment criterion in this
run, and it sorts the candidates better than anything else. Applied:

**Not a deal-breaker for a fibrate — but only because of a design choice that must be made now.**

What a fibrate would nominally require: baseline and periodic renal function for dose banding, LFTs,
CK if myalgic. Trivial in a trial, non-trivial in LMIC primary care. Three routes:

1. **Band on creatinine and accept misclassification.** Point-of-care creatinine is ~$5–10/test;
   point-of-care cystatin C is largely unavailable and more expensive. **So the measure you
   actually want (§2.4) is the one you cannot have at the point of deployment** — an uncomfortable
   and honest asymmetry between trial and field.
2. **Deploy a fixed low dose that is safe unbanded.** The Safety agent established that the systemic
   limb's dose–response is **flat-topped**. So a single dose acceptable at eGFR 30–59 for everyone
   sacrifices only the modest top-of-curve increment in the preserved-function majority, and
   **removes the monitoring requirement entirely.** A fixed low dose with no routine monitoring,
   dispensed through primary care, is a categorically different product from a banded dose with
   quarterly bloods.
   > **Recommendation: carry the fixed-low-dose unbanded regimen as a third arm in the pivotal
   > trial.** Without that arm you will finish a $30M trial with evidence for a regimen that cannot
   > be deployed where the patients are. This is the single most important deployment-design
   > decision in the programme and it costs one extra arm, not one extra trial.
3. **Entry stratification only, no longitudinal monitoring.** One baseline creatinine — which
   diabetics in any organised programme already receive — exclude eGFR <30, then nothing further;
   progression to eGFR <30 is caught at the annual diabetes review for free.

**By the same criterion, the monitoring burden IS a deal-breaker for dimethyl fumarate** —
lymphocyte monitoring is unconditional, there is no safe unmonitored dose, and the hazard it guards
against is PML. That is the cleanest application of the principle in the set.

### 7.3 The inversion: the mechanism has the most headroom where access is worst

The Advocate's strongest objection (§2.6) is that statins have already removed 35–45% of apoB
before the drug arrives, so the mechanism operates on a shrunken residual.

> **That is a high-income-country objection.** Statin coverage among diabetics runs ~60–75% in
> high-income settings and far lower — plausibly 10–30% — across much of the LMIC burden, while
> remnant and triglyceride levels in several of the largest affected populations are high. **The
> residual the mechanism acts on is therefore substantially larger in exactly the populations with
> the least access to any alternative therapy.**
>
> The dilution objection and the access argument point in opposite directions, and the place where
> the objection is weakest is also where screening programmes are scaling fastest, where
> per-patient trial costs are lowest, and where the unmet need is greatest. **This is a strong
> argument for siting the definitive trial in an LMIC or middle-income screening programme rather
> than treating LMIC deployment as a downstream afterthought.**

*(Stated as pharmaco-epidemiology — statin coverage and lipid distributions — not as any claim
about retinal outcomes.)*

---

## 8. (h) The staged, costed development plan

**Top recommendation:** the **systemic remnant-lowering limb in S1–S2 non-proliferative DR**,
enriched on residual lipid risk and lesion progression rate, deployed as a cheap oral generic —
with the receptor demoted from hypothesis to instrument, per the Integrator.

```
═══════════════════════════════════════════════════════════
CLINICAL FEASIBILITY ASSESSMENT: Systemic remnant-lowering, S1–S2 DR
  Lead deployment molecule: Fenofibrate / fenofibric acid
  Gate-1 mechanistic instrument: Pemafibrate (no label sought)
═══════════════════════════════════════════════════════════
OVERALL FEASIBILITY:        Moderate — high on access, low on funding
TIMELINE TO PATIENTS:       10–12 years
TOTAL DEVELOPMENT COST:     $40–70M  (midpoint ~$54M)
REGULATORY ROUTE:           505(b)(2) / EU Article 10(3) for the nested cohort;
                            WHO EML listing as the deployment endgame
PRINCIPAL RISK:             Not science. Screening-programme governance (§1.3)
                            and the absence of any commercial funder (§6.1)
═══════════════════════════════════════════════════════════
```

| Gate | What | Cost | Duration | Decision it gates | **Kill criteria** |
|---|---|---|---|---|---|
| **0** | **Preclinical discrimination + human exposure bound.** Integrator's 5-arm rodent study with **measured** retinal K<sub>p,uu</sub> by LC-MS/MS ($250–400k); aqueous-humour drug + ANGPTL4 tap in chronic-fibrate-exposed diabetics at routine cataract surgery ($50–100k); covariate analysis of whether retinal outcome tracks achieved lipid change in any existing dataset ($50–100k) | **$0.35–0.6M** | 9–12 mo | Whether a retinal-limb programme is ever started; whether the receptor framing survives | `Ppara-/-` arm **fails to abolish** the effect → receptor framing dead. Matched non-PPAR lipid-lowering arm **reproduces** it → abandon receptor, keep programme, reconsider molecule |
| **1** | **Human mechanistic / PD trial.** n ≈ 150, S1–S2 DR with elevated remnants despite statin. 1:1:1 pemafibrate (or fenofibric acid) / ezetimibe / placebo, 12 mo. Endpoints: apoB particle number + NMR subfractions, apoC-III, FGF21, **plasma ANGPTL4 (mandatory)**, MA turnover rate, OCT hyperreflective-foci burden. **Plus the 8-week washout substudy (§5.5).** Fully enriched | **$4–7M** | 24 mo | Does the drug move the proximal supply biomarkers *on top of statin*, and does any retinal imaging measure move at all in 12 months | **No change in MA turnover or HRF burden at 12 mo despite confirmed ≥30% remnant lowering** → the supply→lesion step is not operating at a detectable rate. Stop before the pivotal trial. Also kill on plasma ANGPTL4 rising with any signal of accelerated progression |
| **2** | **Registry-embedded pivotal trial.** Two tiers (§1.4). Pragmatic shell n ≈ 6,000–7,000, PROBE, primary = progression to referable DR. Nested double-blind registrational cohort n ≈ 1,200, upgraded imaging, primary = ≥3-step DRSS. **Three treatment arms: banded standard dose / fixed low unbanded dose (the deployment arm, §7.2) / placebo.** Stratified on eGFR band with the band × treatment interaction pre-specified (§2.3). Full integrity package (§4.2) | **$25–40M** (shell) **+ ~$18M** (nested) | 5–6 yr | Registration, and EML dossier | Interim futility: ITT RRR point estimate **<10%** with the upper CI excluding 25%. Blind-integrity kill: between-arm achieved-HbA1c drift **>0.2%** sustained → the trial is measuring its own co-intervention |
| **3** | **Randomised withdrawal extension.** Re-randomise 1,200 active to continue/withdraw + 600 placebo, 3 yr, same endpoint (§5.3). Near-free observational tail thereafter | **$8–15M** | 3 yr (+ ~free tail) | **Product shape** — 5-year course vs 40-year pill — and therefore the entire chronic-safety calculus. Also the only place withdrawal rebound is detectable | Withdrawn arm converges fully to control **and** a rebound signal appears → the product is a lifelong drug with a dangerous discontinuation profile in a 60%-adherence population. Reconsider deployment entirely |
| **4** | **Deployment.** EML dossier, national programme integration, FDC development if a commercial partner emerges (§6.3) | **$3–8M** | 2–3 yr | Patient access | — |

**Total: $40–70M over 10–12 years** for a deployable, EML-listable, evidence-based oral generic —
against $60–100M for a conventional trial that answers less, costs more, cannot ask the durability
question, and deploys nowhere.

### 8.0 Addendum — Gate 1 after the synthesis revision

`round1-synthesis.md` was revised during this assignment: the claim that **no fibrate can test the
retina-intrinsic limb** has been **retracted**, and **elafibranor** reinstated as a ~12-week
mechanistic probe on the strength of an endothelial margin of −0.7 to +0.4 log.

**Feasibility consequence, and it is favourable.** A 12-week probe is a different product-safety
question from a 40-year preventive: the Michael-acceptor enone liability and the two-year market
history are objections to *chronic dosing*, and they largely do not apply to a 12-week exposure in a
monitored trial. **So elafibranor is cheap to add and cheap to defend at Gate 1, and impossible to
defend at Gate 2.**

> **Recommendation: run elafibranor as a fourth, short-duration arm inside Gate 1** (12 weeks,
> n ≈ 40–60, mechanistic/PD endpoints only, no structural endpoint — nothing structural moves in 12
> weeks). Incremental cost **~$1.2–2.0M** on top of the $4–7M Gate 1. It answers "does endothelial
> PPAR engagement do anything at all in this disease" for the price of a rounding error on the
> pivotal trial, and a null there retires the retinal limb permanently rather than leaving it
> ambiguous forever.
>
> **It must not be carried past Gate 1.** Its feasibility score below is low because the axis is
> *reaching patients*, and a probe does not reach patients. That is not a contradiction — it is the
> axis doing its job. A molecule can be the right instrument and the wrong product.

Revised Gate 1 cost: **$5–9M**.

### 8.1 The three risks, with mitigations

1. **Screening-programme governance negotiation fails** (§1.3) — the cost model collapses and the
   programme reverts to $60–100M, i.e. unfundable. *Mitigation:* negotiate with two or three
   programmes in parallel before committing; prefer jurisdictions with an existing registry-RCT
   track record; make Gate 0 and Gate 1 conditional-free so a failure here costs only $5–7M.
2. **No funder exists for a generic** (§6.1, §6.4) — the structural risk, and it is not solvable by
   trial design. *Mitigation:* run Gate 0 and Gate 1 on academic/philanthropic money ($5–7M total,
   well within a single large grant), and use a positive Gate 1 to convert the pivotal trial from a
   speculative bet into a fundable proposition; develop the §6.3 FDC in parallel as the only
   commercial on-ramp.
3. **The effect is real but too small to detect** (the Advocate's central thesis) — *Mitigation:*
   this is precisely what the §3 enrichment answers, and the §2.3 interaction test means that even a
   null pivotal trial returns a mechanism answer rather than nothing.

### 8.2 Key de-risking step

> **Gate 1, and specifically its microaneurysm-turnover endpoint.** It is the first point at which a
> *retinal* consequence of the mechanism becomes visible in humans, it costs $4–7M against a
> $43–58M pivotal programme, and it is enriched so that if the effect exists anywhere it exists
> here. Everything downstream is a scaling decision; this is the only genuine go/no-go.

---

## 9. Cross-cutting: the four findings are one finding

Stated once, because it is the organising result of this assessment:

> The **registry/screening-embedded design** (§1) is not merely a cost measure. It is simultaneously
> (i) the only affordable route to a 4–5 year early-DR trial, (ii) the only infrastructure holding
> the **serial prior images** that make rate-based enrichment possible and so resolve the Pathway
> agent's enrichment paradox (§3.2), (iii) the only setting in which **3.5% net eligibility** is
> practical rather than absurd (§3.3), and (iv) the only structure under which the **durability
> question** (§5.4) and a decade-long observational tail are affordable to ask at all.
>
> Its single cost is that it **forecloses full double-blinding** (§4.1), which is survivable only
> because the DR endpoint is centrally graded and structurally protected.
>
> Four problems, one piece of infrastructure, one trade-off. That is the assessment.

---

## 10. Confidence and evidence basis

- **§1 audit arithmetic, §2 dilution arithmetic, §3 screening arithmetic, §5.4 costs:** HIGH
  confidence in the computations; **MODERATE** in the inputs (event rates, adherence, eligibility
  fractions, per-patient costs), all of which are consensus estimates requiring sourcing.
- **§2.4 (creatinine banding under-doses the active arm) and §4.1 (registry/blinding conflict):**
  MODERATE-HIGH. Both are deductions from other agents' established findings rather than new facts,
  which is the strongest kind of claim available in this run.
- **§5 durability:** the *framing* is HIGH confidence; the *mechanistic prediction* (rate-suppressive,
  burden-modifying) is explicitly a falsifiable prior, not a finding.
- **§7 costs of goods and supply chain:** MODERATE, order-of-magnitude.
- **Evidence basis: knowledge-based** throughout. No project data file informed this assessment.
- **Research disclaimer:** every figure here is an estimate for programme planning, not a protocol
  input.

---

## 11. Blinding compliance statement

**Files read:** listed in §0. **Files deliberately not opened:** `agents/UNBLINDING-part-b.md`
(instructed); **`BENCHMARK-RESULT.md`** — not mentioned in my instructions, but it appeared in the
directory listing and is self-evidently a post-hoc benchmark-scoring artefact, which makes it an
answer-key file under brief §1.1; I did not open it and I flag it so the orchestrator knows an
unguarded answer-key-class file is sitting in the report root; **`agents/p2-literature.md`** — not on
my read list, and since it is the report carrying the segregated post-hoc unblinding section, I
skipped it **entirely** rather than read part of it and risk the boundary. I did not grep its
headings. I did not use git history or any other route to recover redacted values.

**Disclosures.** I carry the same three exposures I declared in P1 — DR-specific trial knowledge for
**fenofibrate/fenofibric acid**, **candesartan** and **minocycline** — and I have again excluded all
three. Specifically for this assignment:

1. **Every durability argument in §5 is derived from mechanism** (a supply-lowering mechanism is
   rate-suppressive; the lesion is cumulative and partly irreversible) **and from the general
   metabolic-memory/legacy-effect concept in diabetic complications**, which is disease natural
   history, not any drug's DR record. I did not consult, and did not permit myself to recall,
   post-trial follow-up data for any candidate in a retinal setting.
2. **§2 and §3 are entirely arithmetic and pharmacology.** The dilution model uses the Safety
   agent's dose–response characterisation; the enrichment model uses the Pathway agent's quotient.
   No efficacy estimate anywhere in this document is taken from knowledge of any candidate's
   performance in DR — the 30% RRR used throughout is an **assumed** value for power calculation and
   is labelled as such at every use.
3. **§7.3** compares statin coverage and lipid distributions between high-income and LMIC diabetic
   populations. That is pharmaco-epidemiology. It contains no claim about retinal outcomes in any
   population.
4. **Negative decision disclosed.** I considered adding a section on "what prior trials of this class
   in this indication teach about feasibility" — which is, on the face of it, exactly my job. I did
   not write it, because it is the forbidden knowledge in its purest form. Its absence is deliberate.
5. **Skill-instructed deviation disclosed** (§0): `clinical-feasibility-assessor/SKILL.md` directs
   the agent to `chembl_approved_drugs.csv` and `chembl_drug_indications.csv`. Both are forbidden for
   this disease. **I followed the blinding protocol over the skill instruction** and record the
   conflict here so the orchestrator can fix the skill rather than assume the files were consulted.

**Self-assessment.** The highest-risk passage in this document is §5 (durability), because reasoning
about whether benefit persists after stopping is only one inferential step away from recalling
whether anyone has observed it. I have kept §5 strictly prospective — it designs an experiment and
pre-registers four interpretations — and it contains no statement that any candidate has ever been
withdrawn-and-followed in this indication. If a reviewer finds otherwise, §5 is contaminated and the
staged plan's Gate 3 should be re-derived.

**Scores below are practical feasibility of reaching patients. They encode nothing about efficacy.**

---

## SCOREBLOCK

*Axis: practical feasibility of reaching patients. Not efficacy, not mechanism validity.
Weighted on: cost of goods and supply chain · deployability without monitoring (Safety §1.3) ·
existence of a regulatory vehicle · whether a blinded trial can physically be run · whether any
funder exists. Candidates added after Round 1 are scored on the same axis and marked (new).*

SCORE|Fenofibrate|8|high|knowledge-based|Commodity API, pennies daily, no cold chain, deployable unbanded at fixed low dose
SCORE|Fenofibric acid|7|high|knowledge-based|Same chemistry and vehicle; fewer finished-product suppliers outside high-income markets
SCORE|Ezetimibe|7|high|knowledge-based|Generic, oral solid, excellent tolerability, no monitoring; wrong particle mechanistically
SCORE|Candesartan cilexetil|5|high|knowledge-based|Cheap and universal, but background-RAS use makes a clean trial nearly unrunnable
SCORE|Melatonin|5|moderate|knowledge-based|Trivially cheap and unmonitored; no US RLD, supplement-grade CMC, glucose-tolerance caveat
SCORE|Icosapent ethyl|5|high|knowledge-based|Generic but oxidation-sensitive softgels, hot-climate shelf life, four capsules daily
SCORE|Pemafibrate|4|moderate|knowledge-based|No renal banding needed, but Japan-only, BID, branded, single-source, no RLD
SCORE|Berotralstat|4|moderate|knowledge-based|Oral and on-patent, but orphan pricing, CYP polypharmacy DDIs, QT; rich markets only
SCORE|Dimethyl fumarate|3|high|knowledge-based|Cheap generic, but unconditional lymphocyte monitoring guarding PML kills population deployment
SCORE|Epalrestat|3|moderate|knowledge-based|Cheap in Japan and India, but TID, no US/EU RLD, chromaturia unblinds
SCORE|Elafibranor|2|moderate|knowledge-based|Valuable 12-week endothelial probe; orphan pricing and enone forbid chronic deployment
SCORE|Olezarsen|2|moderate|knowledge-based|Injectable ASO, cold chain, specialty pricing; reaches almost nobody at scale
SCORE|Minocycline|2|high|knowledge-based|Permanent pigmentation seen at the endpoint exam; stewardship veto at population scale
SCORE|Seladelpar|2|moderate|knowledge-based|Orphan pricing, minimal chronic database; a control, never a deployable product
SCORE|Quercetin|1|high|knowledge-based|No RLD, no CMC-grade product, bioavailability under two percent
SCORE|Linoleic acid|1|high|knowledge-based|Nutrient, no regulatory vehicle, no valid placebo, not dose-movable
SCORE|Alpha-linolenic acid|1|high|knowledge-based|Same as linoleic acid; no vehicle, no product, no trial
SCORE|Linalool|1|high|knowledge-based|Pharmacological oral dose makes the patient fragrant; no blinded administration possible
