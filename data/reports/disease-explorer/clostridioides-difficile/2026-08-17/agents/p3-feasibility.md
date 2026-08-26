# Phase 3 — Clinical Feasibility Assessment

**Disease:** *Clostridioides difficile* infection (CDI)
**Agent:** Clinical Feasibility Assessor (`.claude/skills/clinical-feasibility-assessor/SKILL.md`, adapted for CDI)
**Date:** 2026-08-17
**Inputs:** `disease-model.md` §1.3, §1.5, §3.3–3.4, §4.1–4.6, §6.3–6.4, Appendix A.2/A.3 · `debate-summary.md` · `agents/p2-repurposing.md` · `agents/p1-clinical-landscape.md` §2.4, §3, §4 · `agents/debate-integrator.md` §3–§6

---

## 0. Executive summary

**The capital structure question has an answer, and it is not one of the four options as posed.**

The four funding models in my tasking are not alternatives competing to fund one programme. They are the correct instruments for **three structurally different products**, and the pipeline contains one of each. Choosing between them is a category error; the decision to make is *portfolio composition*, and the composition is forced by a fact nobody in Rounds 1–2 stated:

> **In CDI, probability of technical success and probability of post-approval commercial survival are anti-correlated.** The assets with the best technical odds are cheap generics that cannot survive commercially. The asset with the best commercial defensibility is an NCE with the worst technical odds. Ranking candidates on a single axis cannot express this, which is why the pipeline's ranking and the feasibility ranking disagree.

Five findings drive everything below.

1. **Ribaxamase is the only candidate in the set whose reimbursement channel is not broken.** Hospital-onset CDI is a CMS-penalised, publicly-reported healthcare-associated infection. A prophylactic administered *during* the admission that reduces hospital-onset CDI puts the cost and the benefit in the same institution's hands. Every other candidate is a retail/pharmacy-benefit product entering the market that withdrew bezlotoxumab and divested VOWST at a loss. This is the strongest commercial argument available to any candidate here and **the pipeline has not made it**.

2. **Ribaxamase's Phase 3 is roughly twice the size the pipeline assumes, and its price is capped by NNT.** At a 3.5% control incidence and 50% RRR the trial needs ~2,600 patients (my computation, §3.2), not the $80–150M programme the integrator estimated — I get **$150–280M excluding acquisition**. Worse, NNT ≈ 58 at that incidence caps a cost-neutral price at **$350–525/course**. The programme is only viable on a **high-risk-enriched label** (incidence 8–10%, NNT 20–25, price ceiling $800–1,500), which also shrinks the trial to ~900–1,100 patients. *The label enrichment is not a marketing refinement; it is the difference between a viable and a non-viable asset.*

3. **Every design choice that raises PTS shrinks the recruitable pool, and PROCLAIM is what happens when you stack them all.** Toxin-EIA confirmation (×0.55), multiply-recurrent enrichment (×0.10), and standard CDI exclusions (×0.25) compound to a **0.5–1.4% screen-to-enrol rate**. At PROCLAIM's observed rate, an n=160 trial needs **150–200 sites over 3–4 years**. Relaxing enrichment from "≥2 prior recurrences" to MODIFY's "≥1 recurrence *or* ≥1 risk factor" gives a **5× improvement to 13–39 sites** while holding the placebo event rate at 35–40%. **Keep toxin-EIA; relax the recurrence count.** That single substitution is the highest-value trial-design decision in this report.

4. **Berberine has the only anti-conservative endpoint confound in the set, and it is a safety hazard rather than a statistical nuisance.** Five candidates have GI pharmacology that touches the diarrhoea endpoint. In four of them (UDCA, chenodiol, niclosamide, CamSA) the drug's own effect is *diarrhoea* — biasing **against** the drug, so a positive result is trustworthy. Berberine's is **constipation**, which biases **for** the drug on a diarrhoea endpoint *while masking the ileus/toxic-megacolon signal that §4.1 says to avoid*. A blinded endpoint committee is sufficient for the other four. Berberine additionally needs a prospective ileus/megacolon DSMB stop rule. **This has not been flagged anywhere in the pipeline and it is the most serious unaddressed trial-design defect in it.**

5. **The tasking's QIDP premise does not hold for the two assets it was applied to.** My brief states ribaxamase is "QIDP-eligible." It very likely is not: GAIN requires an *antibacterial or antifungal drug*, and an orally-delivered β-lactamase that degrades antibiotic is neither. It does not matter — as a BLA it carries **12 years of BPCIA exclusivity regardless**, which is better than QIDP's 8. Niclosamide is likewise not QIDP-eligible (its CDI mechanism is anti-toxin, not antibacterial). The Clinical Landscape agent's §4.1 correction was right and I extend it: **QIDP is materially valuable to exactly one candidate in this set — CamSA** (NCE 5 + QIDP 5 = 10 years, arguably stackable with orphan for rCDI).

**The single most realistic development programme:** acquire ribaxamase; develop it on a **high-risk-enriched primary-prevention label**; fund it with **BARDA/ASPR non-dilutive capital plus a strategic partner holding hospital-channel commercial infrastructure**; gate the whole thing on a **$300–500K diligence pass** covering both the unverified Phase 2b package **and** the CMC/tech-transfer questions that a clinical-data diligence would miss (§5.1.1). In parallel, spend **$1.8–4.5M** on a shared experimental package that prices the entire bile-acid germination axis at once. Details in §8.

**The uncomfortable corollary:** on cost per unit probability of durable patient access, the ranking *inverts* the pipeline's ranking. Berberine's $11M investigator-initiated trial is **13× more capital-efficient** than ribaxamase and **65× more** than ibezapolstat (§7.2). That is not an argument for funding berberine over ribaxamase — the addressable populations and evidence tiers differ by more than the ratio — but any funder with a small budget and no acquisition capacity should read §7.2 before reading §8.

---

## 1. Method — how the skill file was adapted, and what that changed

### 1.1 The skill file's rubric does not transfer

`clinical-feasibility-assessor/SKILL.md` is written for Oral Mucositis. Six of its structural assumptions are wrong for CDI, and three of them are wrong in ways that reverse a conclusion:

| Skill file assumption | CDI reality | Consequence |
|---|---|---|
| "Topical formulation → cheaper preclinical package" | The colonic lumen is reached by **oral** dosing; there is no topical route (except rectal, in ileus) | The cost saving is real but arrives through non-absorption, not topicality |
| "Patient recruitment: OM is common → easy" | CDI is common; **trial-eligible CDI is rare.** Toxin-EIA + recurrence enrichment compounds to <1.5% of screened | **Reversed.** Recruitment is the dominant feasibility risk, not a favourable factor |
| "Endpoint clarity: WHO OM grading well-established" | CDI's endpoint is *diarrhoea recurrence*, and **5 of 10 candidates have GI pharmacology that moves it** | Endpoint integrity requires design machinery, not just a scale |
| "Market size >500K patients → favourable" | ~365–500K US cases/yr, but the market **withdrew an approved product** (bezlotoxumab, Jan 2025) and divested another cheap (VOWST) | **Reversed.** Market size is not the constraint; commercial survival is |
| "IP matters for investment" | Correct, and it is *load-bearing* here: 6 of 12 programme deaths were financial | Elevated from a caveat to a primary scoring dimension |
| "Comparator: placebo acceptable for most OM" | Placebo is acceptable **only** in add-on designs; replacement designs face vancomycin/fidaxomicin | Determines a 5–10× cost difference (§2.1) |

### 1.2 What I added that the skill file does not contain

Four dimensions, each forced by CDI's specific failure record:

1. **Probability of commercial survival post-approval** — a separate probability from PTS, applied *after* approval. CDI is one of very few indications where this is not ~1.0. Bezlotoxumab (approved 2016, discontinued Jan 2025) and VOWST (approved, divested) are the empirical basis.
2. **Recruitment feasibility, quantified as a funnel** — not "Easy/Moderate/Challenging" but enrolled-per-site-year and required site count (§3.1).
3. **Direction of endpoint bias** — not merely whether a confound exists, but whether it biases conservatively or anti-conservatively (§3.3).
4. **Capital efficiency per unit probability of patient access** — the metric that lets a $11M IIT and a $230M acquisition be compared on the same axis (§7.2).

### 1.3 What this report does and does not measure

It measures **development-path tractability and financial survivability**. It does **not** measure probability of clinical benefit — that is what the PTS column imports from other agents, and PTS here is my own compounding of their gates, not an independent biological judgement. Where I disagree with an upstream agent on biology I say so and defer; where I disagree on *cost, timeline, trial size, or survivability* I overrule, because that is this seat's remit.

---

## 2. The five structural facts that determine CDI feasibility

These apply to every candidate and are not repeated in the individual assessments.

### 2.1 Add-on positioning is worth 5–10× on cost and is 3-for-3 versus 0-for-3

The Clinical Landscape agent's §3 finding is the single most important input to this report:

| Design | Trials | n per pivotal | Record |
|---|---|---|---|
| **Replacement** (instead of SOC), active comparator, sustained response d30 | Surotomycin, cadazolid, ridinilazole | ~530–630 × 2 | **0 for 3** |
| **Add-on** (with SOC), placebo-controlled, recurrence through wk 8–12 | Bezlotoxumab, REBYOTA, VOWST | ~182–1,300 | **3 for 3** |

**Every candidate in this report is assessed in add-on positioning unless it structurally cannot be** — which applies to exactly two: ibezapolstat (a replacement antibacterial by design) and ribaxamase (a prevention agent, which is neither).

### 2.2 The primary endpoint is recurrence through week 8, not sustained clinical response at day 30

My tasking specifies "SUSTAINED CLINICAL RESPONSE at 30–90 days (not initial cure)." I accept the *intent* — durability over initial cure — but the operative wording matters, and the Clinical Landscape agent's §4.2 is more precise than my brief:

- **Sustained clinical response at d30** is the *Ri-CoDIFy* primary — the endpoint on which ridinilazole failed, and (per the Devil's Advocate, surviving debate at 65% kill probability) the endpoint with the **strongest negative correlation to preclinical→clinical translation** in the literature.
- **CDI recurrence through week 8** is the *ECOSPOR III / PUNCH CD3 / MODIFY* primary — the endpoint of all three approvals.

These are not the same endpoint. Sustained response is a composite (initial cure **and** no recurrence), so a candidate that does not improve initial cure is *penalised* by the composite even when its recurrence effect is large — precisely what happened to ridinilazole (recurrence 8.1% vs 17.3%, p=.0002; failed on initial response 86.5% vs 92.3%). **Recurrence-through-week-8, conditional on initial cure at end of therapy, is the correct primary for every add-on candidate here.** I am adjusting my brief on this point and flagging it to the final synthesis.

### 2.3 Toxin-EIA enrolment is non-negotiable, and it costs recruitment

NAAT/PCR detects the *organism*; toxin EIA detects *active toxin production*. PCR-positive/toxin-negative patients include colonised patients whose diarrhoea has another cause — they resolve without the study drug, inflating apparent placebo response and diluting measurable effect. SER-109 failed its PCR-enrolled Phase 2 and succeeded in its toxin-EIA-enrolled Phase 3 (ECOSPOR III) with essentially the same product.

**Consequence:** toxin-EIA confirmation is the highest-value single protocol element available and must not be traded away. Its cost is roughly **45% of otherwise-eligible patients** (§3.1). Trade away the recurrence-count enrichment instead.

### 2.4 Six of twelve programme deaths were financial — and two of those were *after approval*

| Failure mode | Assets | Stage at death |
|---|---|---|
| Failed on trial design (replacement) | Surotomycin, cadazolid, ridinilazole | Phase 3 |
| Failed on biology | Tolevamer, actoxumab, 2 toxoid vaccines | Phase 3 |
| **Failed on money** | CP101, Acurx/ibezapolstat, NTCD-M3, ribaxamase | Phase 2→3 transition |
| **Failed on money *post-approval*** | **Bezlotoxumab** (approved 2016 → discontinued Jan 2025), **VOWST** (approved → divested cheap) | **Market** |

The last row is the one my tasking flags as CRITICAL and it deserves its own treatment (§4). It means the standard feasibility question — "can this reach patients?" — is insufficient in CDI. The question is **"can this reach patients and still be there in five years?"**

### 2.5 There is no accepted microbiome surrogate, and there never has been

FDA has never accepted microbiome diversity or secondary bile acid restoration as an approvable endpoint. Ridinilazole had excellent microbiome-preservation data and it bought nothing. **Any candidate whose differentiation rests on mechanistic microbiome data must convert that data into a clinical recurrence difference or it is worth zero at the review division.** This is a hard ceiling and it bears directly on ibezapolstat, berberine, and UDCA.

---

## 3. Trial design — the CDI-specific machinery

### 3.1 Recruitment feasibility, quantified

My tasking's PROCLAIM datum — **1,572 screened → 7 enrolled over 3 years** ⚠verify — is a 0.45% screen-to-enrol rate. I built a funnel model and checked it against that anchor:

```
  screened / high-volume site-year                      60
  × 0.55   toxin-EIA positive                        →  33.0
  × 0.10   ≥2 prior recurrences (strict enrichment)  →   3.3
  × 0.50   other I/E met (no ileus, no IBD flare,
           consentable, no excluded meds)            →   1.65
  × 0.50   consents                                  →   0.83  enrolled/site-yr

  model screen-to-enrol      1.38%
  PROCLAIM observed          0.45%   ← the empirical anchor; my model is 3× optimistic
```

Required sites, using PROCLAIM's observed rate as the realistic case:

| Trial | Model rate | **PROCLAIM rate** |
|---|---|---|
| n=160 (50% RRR, 40% placebo) | 65 sites @ 3 yr / 48 @ 4 yr | **200 sites @ 3 yr / 150 @ 4 yr** |
| n=480 (12-pt effect) | 194 sites @ 3 yr / 145 @ 4 yr | **599 sites @ 3 yr / 449 @ 4 yr** |

**A 480-patient strictly-enriched trial is not feasible at any realistic site count.** A 160-patient one is feasible only with a 150–200-site network — which is what ECOSPOR III in fact built.

**The mitigation, and it is decisive.** Substitute MODIFY's enrichment (≥1 prior recurrence **or** ≥1 risk factor: age ≥65, immunocompromise, severe disease, RT027) for the strict ≥2-recurrence criterion. This raises the eligible fraction from ~10% to ~50% of toxin-positive patients — a **5× improvement to 4.1 enrolled/site-year** — while holding the placebo event rate at 35–40% (§1.3: recurrence is 35–45% after a first recurrence):

| Trial | Sites @ 3 yr, relaxed enrichment |
|---|---|
| n=160 | **13 sites** |
| n=480 | **39 sites** |

> **Recommendation, applying to every add-on candidate: toxin-EIA confirmed + MODIFY-style risk-factor enrichment + add-on to fidaxomicin + recurrence through week 8.** This is simultaneously the highest-PTS and the most recruitable configuration available, and it is the one configuration with three approvals behind it.

### 3.2 Sample size — computed, and validated against real trials

80% power, α=0.05 two-sided, recurrence through week 8:

| Placebo recurrence | Active | RRR | n/arm | **Total** |
|---|---|---|---|---|
| 40% | 20% | 50% | 79 | **158** |
| 40% | 24% | 40% | 130 | **260** |
| 40% | 28% | 30% | 241 | **482** |
| 35% | 20% | 43% | 136 | **272** |
| 25% | 18% | 28% | 537 | **1,074** |

**Validation:** the 40%→20% row gives n=158; ECOSPOR III (VOWST, enriched, large effect) enrolled ~182. The 25%→18% row gives n=1,074; MODIFY I/II (bezlotoxumab, unenriched, ~10-point effect) enrolled ~1,300 per trial. The model reproduces both actual trials to within ~15–20%, which is why I trust the recruitment and pricing figures derived the same way.

**The lesson for candidate selection:** required n is dominated by effect size, and effect size is dominated by *mechanism strength*, not enrichment. A microbiome-restoring product with a 50% RRR needs 158 patients. An adjunct with a 30% RRR needs 482 — a trial that, strictly enriched, cannot be recruited at all. **Any candidate whose plausible RRR is below ~35% is not developable in CDI as a standalone add-on**, regardless of its biology. That disqualifies more of this set than any safety or chemistry objection.

Primary prevention (ribaxamase), event-driven on new-onset CDI incidence:

| Control incidence | Active | RRR | n/arm | **Total** | NNT |
|---|---|---|---|---|---|
| 2.0% | 1.00% | 50% | 2,316 | **4,632** | 100 |
| 3.5% | 1.75% | 50% | 1,307 | **2,614** | 58 |
| 5.0% | 2.50% | 50% | 903 | **1,806** | 40 |
| **8.0%** | **4.00%** | **50%** | **550** | **1,100** | **25** |
| **10.0%** | **5.00%** | **50%** | **432** | **864** | **20** |

### 3.3 Endpoint integrity — and the direction of bias

My tasking notes "5/10 candidates have GI pharmacology corrupting the primary diarrhea endpoint" and prescribes a blinded endpoint committee. That is necessary but insufficient, because **the confounds do not all point the same way**:

| Candidate | Own GI effect | Direction of bias on a diarrhoea endpoint | Adequate mitigation |
|---|---|---|---|
| UDCA | Diarrhoea (most common AE) | **Against** the drug — conservative | Blinded committee + toxin-confirmed recurrence + stool frequency as a *safety* variable |
| Chenodiol | Diarrhoea (dose-limiting) | **Against** — conservative | Same |
| Niclosamide | GI upset / loose stool | **Against** — conservative | Same |
| CamSA | Bile-acid class; diarrhoea plausible at high dose | **Against** — conservative | Same |
| Ibezapolstat | GI AEs reported in Phase 2 | **Against** — conservative | Same |
| **Berberine** | **Constipation / antimotility** | **FOR the drug — anti-conservative** | **Insufficient.** See below |

A conservative confound is a *power* problem: it makes a true effect harder to detect, so a positive result is trustworthy. An anti-conservative confound is a *validity* problem: it manufactures apparent efficacy.

**Berberine's constipation does three bad things at once.** It (i) reduces stool frequency independently of any effect on *C. difficile*, directly inflating the primary endpoint; (ii) prolongs toxin contact time with the epithelium, which §4.1 identifies as the mechanism by which antimotility agents cause **toxic megacolon**; and (iii) masks the earliest clinical sign of ileus, which is a *reduction* in stool output. A blinded endpoint committee does not fix any of these — the committee sees the same corrupted stool data.

> **Required for any berberine trial, and absent from every prior report in this pipeline:**
> 1. Toxin-EIA confirmed recurrence as the *sole* primary component — never symptom-defined recurrence alone.
> 2. A **prospective ileus/toxic-megacolon DSMB stop rule** with protocol-mandated abdominal assessment and imaging triggers.
> 3. Pre-specified **co-primary or key-secondary requirement that the recurrence benefit persists after the drug is stopped** — a motility artefact disappears on washout; a microbiome/host effect does not. This is the only design element that can distinguish the two.
> 4. Exclusion of concomitant antimotility agents (already standard of care, but it must be an explicit exclusion here).

### 3.4 Blinded endpoint committee — scope

For all add-on candidates: independent, blinded adjudication committee with a charter requiring (a) toxin-EIA confirmation of every recurrence event, (b) explicit differential adjudication against post-infectious IBS, drug-induced diarrhoea, and enteral-feeding diarrhoea, (c) blinded review of *all* stool-frequency data, not only events called by the site. In an elderly polypharmacy population where metformin, GLP-1 agonists, and enteral feeds all move stool frequency (§3.3 of the disease model), site-adjudicated recurrence is not a reliable endpoint.

---

## 4. Probability of commercial survival post-approval — the CRITICAL analysis

My tasking states: *"CDI's commercial environment kills APPROVED products. Any business case must model post-approval commercial survival."* Here is that model.

### 4.1 The evidence that approval is not the finish line

| Product | Approved | Fate | Root cause |
|---|---|---|---|
| **Bezlotoxumab** (Zinplava) | 2016 | **Discontinued Jan 2025** | IV administration in an outpatient-managed disease; ~10-point absolute benefit; CHF warning; buy-and-bill economics against a $100 generic backbone |
| **VOWST** (SER-109) | 2023 | **Divested cheap** | Cost of goods for a donor-derived spore product; bowel prep adherence barrier; payer resistance |
| **REBYOTA** | 2022 | Marketed, rectal route | Route is a structural commercial handicap (§6.3) |
| **Fidaxomicin** | 2011 | Marketed; **genericising** | Preferred in guidelines and *still* routinely denied by payers on cost |

And from the adjacent antibacterial market, which is the relevant comparator set for any NCE here: **Achaogen** (plazomicin approved 2018 → bankrupt 2019), **Melinta**, **Tetraphase**, **Paratek** — approval followed by insolvency is the *modal* outcome for a small-company antibacterial in the United States.

### 4.2 The four reimbursement channels, and which one works

This is where the analysis pays off, because CDI has exactly one aligned channel and only one candidate can use it.

| Channel | Who pays | Who benefits | Aligned? | Candidates |
|---|---|---|---|---|
| **Retail pharmacy benefit** (outpatient oral) | PBM / plan | Patient; downstream medical benefit | **No** — the pharmacy silo pays, the medical silo saves. This is why fidaxomicin is denied | UDCA, niclosamide, CamSA, berberine, ibezapolstat |
| **Buy-and-bill / infusion** | Provider, reimbursed | Patient | **No** — killed bezlotoxumab | (none remaining) |
| **Inpatient DRG bundle** | Hospital, from a fixed payment | Hospital, *if* it avoids a penalised event | **YES — if and only if the avoided event is penalised** | **Ribaxamase** |
| **Public health / stockpile pull** | Government | Population | Would work; **PASTEUR Act not enacted** — do not model it | (hypothetical) |

**The ribaxamase channel, stated precisely.** Hospital-onset *C. difficile* LabID event is a CMS-reported healthcare-associated infection measure feeding the Hospital-Acquired Condition Reduction Program and Hospital Value-Based Purchasing. A hospital therefore faces **direct financial penalty** for its hospital-onset CDI rate, on top of the ~$20–30K incremental cost per case it absorbs inside the DRG. A capsule given during the admission that reduces that rate has the payer, the beneficiary, and the penalised party as **the same institution**. That is a genuinely aligned incentive and it exists nowhere else in this candidate set. ⚠verify current programme inclusion and penalty magnitude before external use.

**But NNT caps the price.** Cost-neutrality requires `price ≤ avoided_cost / NNT`:

| Control incidence | NNT (50% RRR) | Max price/course @$20K | @$30K |
|---|---|---|---|
| 2.0% | 100 | $200 | $300 |
| 3.5% | 57 | $350 | $525 |
| 5.0% | 40 | $500 | $750 |
| **8.0%** | **25** | **$800** | **$1,200** |
| **10.0%** | **20** | **$1,000** | **$1,500** |

An unenriched all-comers label prices a recombinant enzyme biologic at **$200–525/course**. That is below plausible COGS-plus-margin for a delayed-release enzyme product and it is why an all-comers ribaxamase is not a business. A **high-risk-enriched label** (age ≥65 + prolonged IV β-lactam + prior CDI or ICU stay) reaching 8–10% background incidence supports **$800–1,500/course**, halves the Phase 3 to ~900–1,100 patients, and adds avoided HAC penalty on top of avoided treatment cost.

> **This is the central strategic recommendation of this report: ribaxamase must be developed on an enriched label from the Phase 3 protocol forward. Enrichment is simultaneously the trial-feasibility fix, the pricing fix, and the payer fix. Developing it all-comers optimises the label and destroys the asset.**

### 4.3 Commercial survival probabilities

| Candidate | Exclusivity | Generic-substitution exposure | Channel | **P(commercial survival \| approval)** |
|---|---|---|---|---|
| **Ribaxamase** | 12 yr BPCIA (BLA); QIDP irrelevant | None — no generic β-lactamase | Inpatient DRG, **aligned** | **0.55–0.65** |
| **CamSA** | 5 NCE + 5 QIDP = 10 yr; orphan possibly stacks | None — NCE, composition of matter | Retail, misaligned | **0.60–0.70** |
| **Niclosamide** | 3 yr (new dosage form) + formulation patents | **High** — API is pennies; compounding pharmacies | Retail | **0.30–0.40** |
| **Ibezapolstat** | 5 NCE + 5 QIDP = 10 yr | None, but **competes with generic fidaxomicin** | Retail antibacterial — the Achaogen channel | **0.20–0.30** |
| **UDCA** | 3 yr new indication | **Total** — off-label generic ursodiol on day 1 | Retail | **0.10–0.15** as a *product* |
| **Berberine** | None (dietary supplement) | Total | None — no product | **N/A** |

### 4.4 The reframe that resolves the paradox

For UDCA and berberine, "probability of commercial survival" is the wrong question, and asking it produces a misleading answer. Neither is intended to become a *product*; the deliverable is **a guideline recommendation on an already-marketed molecule**. Measured correctly:

| Candidate | P(commercial survival as a product) | **P(durable patient access \| positive trial)** |
|---|---|---|
| UDCA | 0.10–0.15 | **~0.75** — generic ursodiol cannot be withdrawn for commercial reasons; supply is secure; guideline uptake is the only gate |
| Berberine | N/A | **~0.50** — supplement supply is permanent, but **product standardisation is not**: a positive trial on one characterised extract does not transfer to what patients actually buy. This is berberine's real access risk and it is under-appreciated in the pipeline |

> **The deepest finding in this section: in a market that withdraws approved products, un-ownable products are the ones that survive.** Bezlotoxumab had 12 years of exclusivity, an aligned mechanism, and a Level 1 evidence base — and it is gone. Generic ursodiol, if a trial ever supports it, cannot be taken away. A funder optimising for patients-treated-in-2040 should weight this heavily; a funder optimising for return cannot touch it. **That is the fork, and it is not resolvable by analysis — it is a mandate question for whoever commissions the work.**

---

## 5. Candidate assessments

Format follows the skill file's output template, adapted: "Formulation" retains OM's structure but scored against §6.2's inverted ADMET logic; "Commercial Viability" is split into IP/channel and an explicit post-approval survival probability; "Recruitment Feasibility" is quantified per §3.1.

### 5.1 Ribaxamase — **rank 1**

```
═══════════════════════════════════════════════════════════
CLINICAL FEASIBILITY ASSESSMENT: Ribaxamase (SYN-004)
Pipeline score 7.5 · in-license, not repurpose
═══════════════════════════════════════════════════════════
OVERALL FEASIBILITY: MODERATE-HIGH (highest in set)
ESTIMATED TIMELINE TO PATIENTS: 6-8 years from acquisition close
ESTIMATED DEVELOPMENT COST: $150-280M excluding acquisition
                            (I overrule the integrator's $80-150M — see below)
PTS: 0.30-0.40   ·   P(commercial survival | approval): 0.55-0.65
P(durable patient access): 0.21   ← highest in the set

RECOMMENDED PATHWAY:
  Route: BLA 351(a) — recombinant enzyme biologic, orally delivered,
         delayed-release, acting in the intestinal lumen
  Designations: Fast Track (serious condition + no approved primary-
         prevention option) — YES, on its own merits.
         Breakthrough — ARGUABLE on a strong Phase 2b.
         QIDP — NO. ⚑ CORRECTION TO MY TASKING: GAIN requires an
         antibacterial or antifungal DRUG. An enzyme that degrades
         antibiotic is neither. Immaterial: BPCIA gives 12 years
         regardless, which exceeds QIDP's 8.
  Rationale: no RLD exists; it is a biologic; there is no alternative route

FORMULATION:
  Form: enteric/delayed-release oral capsule — ALREADY DEVELOPED and
        clinically demonstrated to deliver active enzyme to the lumen
  Feasibility: HIGH on delivery, MODERATE on CMC
  Key challenge: enzyme biologic CMC is harder than any small molecule
        here — potency assay, aggregation, cold chain, comparability
        after any process change. Budget $25-50M and 24-36 months.
        ⚠ The delayed-release coating is pH-triggered; PPI use is near-
        universal in this population (§3.3) and raises gastric pH.
        Whether the existing coating is PPI-robust is a first-order
        diligence question that nobody in this pipeline has asked.

CLINICAL DEVELOPMENT:
  Phase 1 needed?: NO — human exposure exists
  Phase 2 needed?: NO — Phase 2b positive (⚠UNVERIFIED, see risk 1)
  Phase 3 design: ENRICHED primary prevention. Hospitalised patients
        receiving IV beta-lactams WITH >=2 risk factors (age >=65,
        anticipated >=5d IV beta-lactam, prior CDI, ICU). Randomised,
        double-blind, placebo-controlled, drug given for the duration
        of IV therapy + 72h.
  Primary endpoint: new-onset CDI (toxin-EIA confirmed) through day 30
        post-antibiotic. NOTE: this is the ONE candidate for which my
        tasking's "sustained clinical response" endpoint does not
        apply — it has no treatment episode to sustain. Incidence is
        the correct and cleaner endpoint, and escaping the sustained-
        response endpoint is one of its three main structural
        advantages (§4.5 failure modes).
  Size: all-comers @3.5% incidence -> ~2,600 patients (NOT VIABLE)
        enriched @8-10% incidence  -> ~900-1,100 patients (VIABLE)
  Trials: one large adequate-and-well-controlled trial is plausible
        for an unmet-need prevention indication, but FDA will want
        strong statistical persuasiveness plus confirmatory evidence.
        Budget for a second smaller trial or a large safety cohort.
  Recruitment feasibility: EASY — the only candidate with a favourable
        answer. Eligible patients are ALREADY INPATIENTS, identifiable
        from the pharmacy order for IV beta-lactam, with no toxin-EIA
        gate and no recurrence-history gate. Screen-to-enrol will be
        30-60%, not 0.5%. THIS IS A LARGE AND UNDER-VALUED ADVANTAGE:
        it is the only candidate that escapes the PROCLAIM problem
        entirely.
  Blinded endpoint committee: still required (adjudicate CDI vs
        antibiotic-associated diarrhoea) but the drug has NO GI
        pharmacology of its own — zero endpoint-corruption risk (§3.3)

COMMERCIAL VIABILITY:
  Addressable: ~500K-1M US high-risk IV beta-lactam recipients/yr
        (order-of-magnitude); ~7,500-15,000 CDI cases prevented/yr
  Channel: INPATIENT DRG with a CMS-penalised target event —
        the only aligned reimbursement channel in this disease (§4.2)
  Pricing: NNT-capped. $350-525 all-comers (non-viable);
        $800-1,500 enriched (viable). ⚠verify HAC programme details
  IP: 12-yr BPCIA; no generic enzyme pathway in practice
  Competition: DAV132 (Phase 3, adsorbent, same space, further along
        and NOT financing-constrained — this is the real competitive
        threat and the pipeline has not weighted it)
  Ceiling: prevents only beta-lactam-driven CDI. Fluoroquinolone- and
        clindamycin-driven CDI untouched. NOBODY IN THIS PIPELINE
        QUANTIFIED THIS and it directly sizes the market — a first-
        order diligence item.

MANUFACTURING:
  Supply chain: microbial fermentation — well-understood, scalable
  Scale-up: MODERATE. Enzyme + delayed-release coating; the coating
        process is the harder half
  QC: potency bioassay + coating dissolution. Non-trivial but routine

RISK SUMMARY:
  1. THE PHASE 2b PACKAGE IS UNVERIFIED BY ANYONE IN THIS PIPELINE.
     The entire recommendation rests on it. — Mitigation: the
     $300-500K diligence pass (§5.1.1 expands this from $150-300K to
     add a CMC/tech-transfer workstream), before any other
     commitment. This is not a risk to manage, it is a gate to pass.
  2. All-comers label is commercially non-viable (NNT-capped price
     below COGS). — Mitigation: enriched label from the protocol
     forward; this is a design decision, not a marketing one.
  3. Acquisition cost is unknown and DAV132 is ahead in the same
     space. — Mitigation: price the option against DAV132's timeline;
     walk away above a threshold set before negotiating.

GO/NO-GO: CONDITIONAL ADVANCE — fund the diligence, not the programme
  Rationale: it is the only candidate that escapes all four field-wide
  failure modes (initial-cure NI bar, sustained-response endpoint,
  diarrhoea-endpoint confound, rodent-only evidence), the only one
  with an aligned payer, and the only one with easy recruitment. Its
  defect is capital, which is correctable; the alternatives' defects
  are pharmacodynamic, which are not.
  Key de-risking step: $300-500K diligence on (a) the Phase 2b data
  package, (b) beta-lactam-attributable fraction of CDI, (c) PPI
  robustness of the delayed-release coating, (d) acquisition price,
  and (e) CMC/tech-transfer — cell-bank transferability, process
  tech-transferability, right of reference, batch comparability
  (§5.1.1). The CMC half is the more likely deal-breaker.

CONFIDENCE: MODERATE on specifics (rests on unverified data);
            HIGH on the strategic logic
═══════════════════════════════════════════════════════════
```

**Where I overrule upstream.** The integrator's $80–150M is too low. A prevention Phase 3 is event-driven, and even enriched to 8–10% incidence it needs ~900–1,100 patients; unenriched it needs ~2,600. Adding enzyme-biologic CMC ($25–50M) and a confirmatory package, **$150–280M excluding acquisition** is the honest range. The integrator flagged its own estimate as "probably optimistic" — this quantifies by how much.

#### 5.1.1 The diligence scope is incomplete in the place biologic acquisitions usually fail

The integrator's de-risking item #1 — "Ribaxamase Phase 2b diligence: full data package, endpoint definitions, acquisition cost, $150–300K" — and my own Stage 1 above both scope the **clinical, commercial and regulatory** questions. Both omit the **CMC/tech-transfer** question, and for an enzyme biologic being acquired from a sponsor that ran out of money, that is the more likely failure point. Financially distressed biologics programmes do not merely stop spending; they let cell-bank storage contracts, CRO agreements and supplier qualifications lapse, and the asset quietly degrades from "Phase 3-ready" to "Phase 3-ready if you re-develop the process."

Five questions, none of which a clinical-data diligence would ask:

| # | Question | Why it can end the deal |
|---|---|---|
| 1 | Is the **master and working cell bank** in hand, fully characterised to current expectations, and **legally transferable** — or held at a CRO under a lapsed or unassignable agreement? | Without a transferable, characterised MCB there is no product. Re-deriving and re-characterising a bank is 12–18 months on its own |
| 2 | Is the **manufacturing process tech-transferable** — complete batch records, validated analytical methods, a qualified potency bioassay — or does it require re-development? | A process that exists only as institutional knowledge in a dispersed team is not an asset you can buy |
| 3 | Is there a **right of reference** to the Phase 2b IND/data, or only the data itself? | These are different assets and the second is far less useful. Data without a right of reference may not support a BLA without repeating work |
| 4 | Does the **delayed-release enteric coat** have a qualified supplier, and does the release specification still meet current expectations? | Compounds risk 1 in §5.1's formulation block: the PPI-robustness question is unanswerable without a qualified coating process to test |
| 5 | Are the **Phase 2b clinical batches comparable** to whatever Phase 3 material would be made from — and if not, how large is the comparability exercise? | A comparability failure converts inherited clinical data into supportive-only evidence, which is the whole reason for buying the asset |

**The cost of getting this wrong:** if the process is not transferable, add **18–24 months and $15–30M** for process re-development plus comparability — on top of the $25–50M CMC line already budgeted in Stage 3. That is a material fraction of the programme, it is invisible to a clinical-data diligence, and it is discoverable for a few hundred thousand dollars **before** the acquisition rather than after.

> **Recommendation, and it amends both the integrator's item #1 and my own Stage 1: expand the diligence from $150–300K to $300–500K and add a CMC/tech-transfer workstream** staffed by a biologics CMC assessor rather than a clinical-data reviewer. The incremental $150–200K is 0.1% of programme cost and it prices the risk that most plausibly destroys the thesis after close. Two of the five questions above (1 and 3) are **binary deal-breakers** and should be added to the Stage 1 kill criteria, not merely to the valuation model.

This is my most concrete addition to the integrator's plan, and it is the one place where I think the pipeline's top recommendation is under-diligenced rather than merely unverified.

### 5.2 Niclosamide — **rank 2 by pipeline score; rank 5 by feasibility**

```
═══════════════════════════════════════════════════════════
CLINICAL FEASIBILITY ASSESSMENT: Niclosamide
Pipeline score 6.5
═══════════════════════════════════════════════════════════
OVERALL FEASIBILITY: LOW (unconditional) / MODERATE (post-package)
ESTIMATED TIMELINE TO PATIENTS: 8-11 years
ESTIMATED DEVELOPMENT COST: $75-140M, after a $200-400K kill-or-cure
                            package that will probably end it
PTS: 0.01-0.03 unconditional  ·  0.20-0.25 conditional on a clean package
P(commercial survival | approval): 0.30-0.40
P(durable patient access): 0.077 post-package

RECOMMENDED PATHWAY:
  Route: 505(b)(2) CONTINGENT on a formal listed-drug determination.
         US marketing (Niclocide) was discontinued; a discontinued
         listing can serve as RLD ONLY if withdrawal was not for
         safety or effectiveness reasons. NOBODY HAS ASKED FDA. If the
         answer is no, the path is 505(b)(1) — full NDA, +2-3 years
         and +$50M.
  Designations: QIDP — NO. ⚑ CORRECTION: the CDI mechanism is anti-
         toxin (TcdB entry blockade), not antibacterial. GAIN does not
         reach it. My tasking's "505(b)(2) contingent on RLD status"
         is right; the implied QIDP benefit is not available.
         Orphan for rCDI — plausible, worth 7 years ⚠verify
  Exclusivity if approved: 3 years (new dosage form) + formulation
         patents. NOT 8 — there is no QIDP to add.

FORMULATION:  ← THE BINDING CONSTRAINT
  Form: an enabling formulation is MANDATORY — amorphous solid
        dispersion, nanocrystal, salt/co-crystal, or soluble prodrug
  Feasibility: LOW
  Key challenge: intrinsic aqueous solubility ~1.6 uM (~0.5 ug/mL) at
        neutral pH — AT OR BELOW the reported TcdB-entry-blockade
        range. Yomesan's poor dissolution is a FEATURE for killing a
        tapeworm scolex by contact and a DEFECT for reaching an
        intracellular target. Multiple COVID-era solubility programmes
        attempted this and struggled. This is a NEW DOSAGE FORM
        505(b)(2): full CMC + bridging study, 24-36 months and
        $10-20M BEFORE Phase 2 opens.

CLINICAL DEVELOPMENT:
  Phase 1 needed?: YES for the new formulation (repeat-dose exposure
        at levels the single-dose anthelmintic label does not cover)
  Phase 2: add-on to fidaxomicin, n~150, recurrence through wk 8
  Phase 3: 2 trials, n~250-300 each
  Primary endpoint: recurrence through wk 8, toxin-EIA confirmed
  Endpoint confound: GI upset — biases AGAINST the drug (conservative).
        Blinded committee sufficient (§3.3)
  Recruitment: MODERATE — standard add-on rCDI funnel, 13-39 sites
        under relaxed enrichment
  Effect size required: this is the quiet killer. Per §3.2, an add-on
        needs ~>=35% RRR to be developable. A protonophore acting on
        an intracellular target through three serial low-efficiency
        steps is not a >=35%-RRR proposition on any current evidence.

COMMERCIAL VIABILITY:
  Channel: retail pharmacy — misaligned
  IP: formulation patents are real but the API is pennies and
        compounding is a live substitution threat
  Competition: the C4 anti-toxin axis is genuinely empty after
        bezlotoxumab's withdrawal — this is niclosamide's single
        best feature and it is a positioning advantage, not a
        technical one

RISK SUMMARY:
  1. Four serial gates, any one fatal: RLD status, nitro reduction at
     Eh ~-200 mV, free-drug concentration in faecal water above the
     entry-blockade IC50, and uncoupling selectivity. — Mitigation:
     three are benchtop experiments and one is a letter to FDA, total
     $200-400K. Answer all four before spending anything else.
  2. Mechanism-intrinsic efficacy/safety coupling (Devil's Advocate,
     70% kill probability, survived debate). The protonophore that
     deacidifies the endosome uncouples mitochondria and commensals.
     Per the integrator, this is NOT fixable by des-nitro or by
     formulation, and the therapeutic index NARROWS as colonic barrier
     damage increases — i.e. it is worst in the sickest patients.
     — Mitigation: the selectivity-ratio experiment ($60-120K) is a
     gate, not a de-risking step. There is no formulation answer.
  3. Effect size probably below the developability floor. —
     Mitigation: none available pre-clinically. This is why the
     conditional PTS is 0.20-0.25 rather than higher even after a
     clean package.

GO/NO-GO: CONDITIONAL — fund the $200-400K package, expect a negative
  Rationale: the pipeline's #2 ranking reflects preclinical package
  quality and white-space position. Neither survives contact with the
  development path: the formulation gap alone is $10-20M and 2-3 years
  before Phase 2, on a molecule whose mechanism-intrinsic toxicity
  coupling is unfixable and whose plausible effect size is below the
  developability floor.
  Key de-risking step: FDA listed-drug determination letter — it is
  nearly free, it is a hard gate, and nobody has sent it.

CONFIDENCE: HIGH that the package is the right next spend;
            HIGH that it will be negative
═══════════════════════════════════════════════════════════
```

### 5.3 CamSA — **rank 3**

```
═══════════════════════════════════════════════════════════
CLINICAL FEASIBILITY ASSESSMENT: CamSA
(cholic acid m-aminobenzenesulfonamide) — NCE
Pipeline score 6.3
═══════════════════════════════════════════════════════════
OVERALL FEASIBILITY: MODERATE on path, LOW on timeline
ESTIMATED TIMELINE TO PATIENTS: 9-13 years
ESTIMATED DEVELOPMENT COST: $80-140M
PTS: 0.10-0.15   ·   P(commercial survival | approval): 0.60-0.70
P(durable patient access): 0.078

RECOMMENDED PATHWAY:
  Route: 505(b)(1) full NDA. No RLD; novel moiety.
  Designations: QIDP — ARGUABLE AND WORTH PURSUING. ⚑ This is the ONE
         candidate for which my tasking's QIDP premise straightforwardly
         pays. An anti-germinant prevents the organism becoming
         metabolically active and replicating; that is a far better
         "antibacterial" claim than a microbiome-restorative bile acid
         can make. If granted: 5 NCE + 5 QIDP = 10 years, plus Fast
         Track. Orphan for rCDI plausibly stacks (+7) ⚠verify.
  Rationale: no alternative exists for an NCE, and the exclusivity
         arithmetic is the best in the set — which is precisely why it
         is the only candidate that could attract equity capital.

FORMULATION:
  Form: immediate-release oral capsule. NO colon-targeting needed —
        the sulfonate guarantees non-absorption by construction
  Feasibility: HIGH — one amide coupling from cholic acid, a commodity
        API. Anionic, MW 564, TPSA ~153, zero reducible groups
  Key challenge: taste (bile acid + sulfonate) and capsule size at
        whatever dose the germination IC50 dictates — and that IC50
        does not yet exist for this compound in a form usable for
        dose projection. Cost of goods should be low.
  ⚑ THE STRUCTURAL ADVANTAGE, and it is real: applying the Safety
        Pharmacologist's coupled-filter, CamSA is the only candidate
        where efficacy and safety levers point the SAME way — the
        sulfonate that drives potency is the group that guarantees
        non-absorption. Every other candidate either has no coupling
        (UDCA, berberine) or has adverse coupling (ebselen fatal,
        niclosamide serious). This inversion is why an unadvanced NCE
        ranks third, and I concur with the integrator on it.

CLINICAL DEVELOPMENT:
  Preclinical/IND-enabling: $8-15M, 24-30 months. Lighter systemic tox
        package justified by non-absorption, but a bile-acid derivative
        still needs 2-species repeat-dose with hepatic and colonic
        histopathology, genotox, and — specifically — a commensal-
        spectrum and microbiome-impact package, which for this class
        FDA will read as core toxicology, not as a nice-to-have.
  Phase 1: healthy volunteers, $4-8M. Unusual design: the readout is
        FAECAL concentration and microbiome impact, not plasma PK.
        Plasma should be undetectable, and demonstrating that IS the
        Phase 1 result.
  Phase 2: add-on to fidaxomicin, n~150, recurrence wk 8, $12-20M
  Phase 3: 2 trials, n~250-300 each, $50-90M
  Recruitment: MODERATE (13-39 sites, relaxed enrichment)
  Endpoint confound: bile-acid-class diarrhoea plausible; conservative
        direction; blinded committee sufficient

COMMERCIAL VIABILITY:
  Channel: retail — misaligned, BUT 10 years of exclusivity and no
        generic substitute means it can at least charge a price
  Addressable: rCDI, and uniquely the immunocompromised subset that
        live biotherapeutics cannot serve (§3.4, unmet need #1)
  IP: composition of matter on an NCE — the strongest position in the
        set. NOTE: CamSA is described in the literature, so the
        composition claim may be unavailable and the estate may rest
        on method-of-use plus formulation plus the U-2 analog series.
        ⚠ FREEDOM-TO-OPERATE AND PATENTABILITY DILIGENCE IS A GATE,
        not a task — a $50-100K item that could void the entire
        commercial rationale, and no prior report raises it.
  Competition: none clinically on the germination axis

RISK SUMMARY:
  1. THE CLASS QUESTION, which is bigger than the molecule: can ANY
     anti-germinant hold against a continuously replenished spore
     load, and does blocking germination without killing spores merely
     DELAY disease? The disease model raises this at §2.3 and the
     integrator notes nothing in the analysis addresses it. CamSA,
     UDCA, chenodiol and urso-CamSA all die together if the answer is
     no. — Mitigation: this needs a purpose-designed experiment
     (relapse-after-withdrawal in a spore-challenge model) that
     nobody has proposed. It should precede the IND, not the NDA.
  2. Prior-art/patentability may void the commercial case. —
     Mitigation: FTO opinion, $50-100K, before any chemistry spend.
  3. The ~1000x-CDCA potency figure is knowledge-based, from a
     germination assay, single-lab, mouse-validated only. — Mitigation:
     independent germination dose-response ($50-100K, shared with the
     UDCA/TUDCA/CDCA panel) plus an independent in vivo replication.
  4. 9-13 years means the market it launches into is not the market
     analysed here. — Mitigation: none. Price this into the discount
     rate honestly.

GO/NO-GO: CONDITIONAL ADVANCE as a research programme, NOT a
  development programme. Fund the FTO opinion, the germination dose-
  response, and the class-level spore-replenishment experiment
  (~$150-250K total). Only then consider IND-enabling work.
  Rationale: the best-designed molecule in the set and the only one
  with a defensible commercial position, sitting on the emptiest
  high-value axis — but it is 9-13 years and ~$100M+ away from a
  patient, and an unanswered CLASS-level question could void the whole
  bile-acid axis including the fast-path UDCA probe.
  Key de-risking step: the class question. It is cheap relative to the
  programme, it has never been asked, and it prices four candidates.

CONFIDENCE: HIGH on pathway and cost; LOW-MODERATE on biology
═══════════════════════════════════════════════════════════
```

### 5.4 UDCA — **fastest path; buy the option, not the programme**

```
═══════════════════════════════════════════════════════════
CLINICAL FEASIBILITY ASSESSMENT: UDCA (ursodiol)
Pipeline score 5.5
═══════════════════════════════════════════════════════════
OVERALL FEASIBILITY: HIGH on path, LOW on biology, ZERO on commerce
ESTIMATED TIMELINE TO PATIENTS: 5-6 years
ESTIMATED DEVELOPMENT COST: $45-85M + $1-3M Stage 0
PTS: 0.12-0.16 unconditional · 0.30-0.35 conditional on Stage 0 pass
P(commercial survival as a product): 0.10-0.15
P(DURABLE PATIENT ACCESS | positive trial): ~0.75  ← the metric that matters
P(durable patient access) overall: 0.105

RECOMMENDED PATHWAY:
  Route: 505(b)(2), RLD = Actigall / Urso 250 / Urso Forte. Dose within
         the approved range -> maximal reliance. Cleanest regulatory
         position of any candidate here.
  Designations: QIDP — ARGUABLE at best. A bile acid positioned as
         microbiome-restorative will struggle to read as an
         antibacterial to FDA. DO NOT BUILD THE BASE CASE ON IT.
         Orphan for rCDI — plausible ⚠verify.
  Exclusivity: 3 years, realistically. 8 only if QIDP is granted.

FORMULATION:
  Form: existing marketed IR capsules/tablets. Feasibility 10/10.
  Key challenge: none for Fork A. Fork B (proprietary colon-targeted
        formulation) carries a specific and under-rated technical risk:
        pH-triggered coatings in a population with near-universal PPI
        use (§3.3) may release in the wrong compartment.

CLINICAL DEVELOPMENT:
  Phase 1: NO — 40 years of chronic human dosing
  STAGE 0 (the gate, and it is non-optional): faecal bile acid PK,
        n=20-30 CDI patients on SOC +/- ursodiol 15 mg/kg/d. Measure
        FREE UDCA, LCA, TCA in FAECAL WATER — not total faecal, not
        plasma — against the anti-germination IC50. 9-12 months,
        $1-3M. Include chenodiol and taurocholate arms.
  ⚑ SEQUENCING CORRECTION, and it is important: Stage 0 as specified
        compares a concentration to a threshold THAT DOES NOT EXIST.
        No UDCA anti-germination IC50 has been published (Literature
        Gap #4). The $50-100K bile-acid germination dose-response
        experiment MUST PRECEDE Stage 0, or Stage 0 returns a number
        with nothing to compare it to. The integrator caught this; it
        is a hard sequencing dependency and it changes the critical
        path.
  Phase 2: n~120-150, add-on, placebo-controlled, recurrence wk 8,
        18-24 months, $8-15M
  Phase 3: 1-2 trials, n~250-300 each, 30-36 months, $30-60M
  Recruitment: MODERATE (13-39 sites under relaxed enrichment)
  Endpoint confound: UDCA's most common AE is DIARRHOEA and the
        primary endpoint is diarrhoea recurrence. Direction is
        CONSERVATIVE (biases against the drug), so blinded committee +
        toxin-confirmed adjudication + stool frequency analysed as a
        SAFETY variable is adequate. Must be designed in from the
        protocol synopsis.
  Dose ceiling: high-dose UDCA (28-30 mg/kg/d) in PSC produced HARM.
        Practical ceiling ~20 mg/kg/d. YOU CANNOT ANSWER A SUB-
        THERAPEUTIC COLONIC CONCENTRATION BY ESCALATING THE DOSE —
        this is what makes Stage 0 a genuine go/no-go rather than a
        dose-finding exercise. ⚠verify

COMMERCIAL VIABILITY:
  Pennies per dose. 3-year exclusivity on a molecule any physician can
  prescribe off-label the day the Phase 3 publishes. NEGATIVE NPV for
  a commercial sponsor — unambiguously. Fork A (public funding) or
  Fork B (proprietary formulation, +2-3 yrs, +$15-25M) are the only
  options, and Fork B carries the PPI-coating risk.
  BUT: see §4.4. As a generic it cannot be WITHDRAWN. Its access
  durability is the highest in the set. The right way to state this:
  UDCA is commercially worthless and clinically durable, which is the
  exact inverse of bezlotoxumab.

RISK SUMMARY:
  1. Colonic free concentration may be an order of magnitude below
     IC50, and the dose ceiling blocks the fix. — Mitigation: Stage 0,
     preceded by the germination dose-response. $1-3M answers a
     $45-85M question.
  2. The effector may be LCA (produced by bai-guild 7alpha-
     dehydroxylation) rather than UDCA itself — in which case UDCA
     depends on the exact enzymology CDI destroys, and the rational
     move is to deliver LCA directly. — Mitigation: Stage 0 measures
     LCA; this is why the LCA arm is not optional.
  3. The negative hamster study (n=8) is underpowered and used the
     wrong model for the proposed use. — Mitigation: apply the
     symmetric discount the debate established. A 3.5-grade instrument
     is 3.5-grade in both directions; it neither kills nor clears.

GO/NO-GO: BUY THE OPTION, NOT THE PROGRAMME
  Rationale: fastest path, cleanest regulatory position, best safety
  transfer, and the weakest biology in the top tier. The correct
  instrument for that profile is a $1-3M staged option, not a $45-85M
  commitment. Exercise on a positive Stage 0.
  Key de-risking step: germination dose-response FIRST ($50-100K),
  then Stage 0 faecal PK ($1-3M).

CONFIDENCE: HIGH on pathway/cost; LOW-MODERATE on biology
═══════════════════════════════════════════════════════════
```

### 5.5 Ibezapolstat — **the financing question is the wrong question**

```
═══════════════════════════════════════════════════════════
CLINICAL FEASIBILITY ASSESSMENT: Ibezapolstat
Pipeline score 6.2
═══════════════════════════════════════════════════════════
OVERALL FEASIBILITY: MODERATE on path, LOW on both PTS and survival
ESTIMATED TIMELINE TO PATIENTS: 6-8 years
ESTIMATED DEVELOPMENT COST: $120-200M (one Phase 3) / $300M+ (two)
PTS: 0.10-0.15   ·   P(commercial survival | approval): 0.20-0.30
P(durable patient access): 0.030  ← LOWEST in the set

RECOMMENDED PATHWAY:
  Route: 505(b)(1) NDA. QIDP + Fast Track granted ⚠verify — the ONLY
         candidate for which my tasking's QIDP premise holds without
         qualification. NCE 5 + QIDP 5 = 10 years.
  ⚑ ON "FDA IS OPEN TO A SINGLE PHASE 3": accurate but dangerously
         incomplete. FDA accepts a single adequate and well-controlled
         trial when there is (a) STATISTICAL PERSUASIVENESS — in
         practice a very low p-value, not p=0.04 — plus (b)
         confirmatory evidence. A single Phase 3 landing at p=0.03 is
         likely NOT sufficient, and a single-trial structure has no
         second trial to average against. "One Phase 3" halves the
         cost and MORE than doubles the variance. For a financing-
         constrained sponsor that is not de-risking; it is leverage.

CLINICAL DEVELOPMENT (as designed — replacement):
  Phase 3: head-to-head vs vancomycin, n~550-650, non-inferiority on
        initial cure THEN superiority on sustained response
  ⚑ THE BAR, stated exactly: per the integrator's corrected reading of
        Ri-CoDIFy, ridinilazole DID deliver the recurrence advantage
        (8.1% vs 17.3%, p=.0002) and failed on INITIAL CLINICAL
        RESPONSE (86.5% vs 92.3%). So a narrow-spectrum agent must
        FIRST clear an NI margin on initial cure against an 85-92%-
        effective comparator — the exact bar that killed the last
        entrant — before its recurrence advantage is even evaluable.
        Total ibezapolstat human exposure is ~50-60 subjects. Nothing
        in that data set demonstrates it clears the initial-cure bar.
  Recruitment: EASIER than the add-on candidates (no recurrence
        enrichment; first-episode or first-recurrence CDI) but a
        replacement design means withholding a proven generic, which
        is harder on IRBs and on consent in an acutely ill elderly
        population
  Endpoint confound: GI AEs reported in Phase 2; conservative direction

  THE ALTERNATIVE POSITIONING, which the Clinical Landscape agent
  recommends and I endorse: reposition as SEQUENTIAL or ADD-ON
  (fidaxomicin -> ibezapolstat consolidation) scored on recurrence.
  That moves it from the 0-for-3 column to the 3-for-3 column, cuts
  Phase 3 from ~600 to ~250-300 per trial, and drops cost from $300M+
  to $60-100M. It also abandons the standalone-antibacterial commercial
  story, which is the story that cannot be financed anyway. This
  repositioning is worth more to the asset than the financing is.

COMMERCIAL VIABILITY:
  ⚑ THE FINDING: even if approved, it launches against GENERIC
  FIDAXOMICIN. An approved small-company antibacterial competing with
  a generic incumbent is the Achaogen scenario — plazomicin approved
  2018, bankruptcy 2019 — repeated at Melinta, Tetraphase, Paratek.
  The relevant question is not "can Acurx fund Phase 3" but "does an
  approved narrow-spectrum CDI antibacterial have a business at all in
  2032 against generic fidaxomicin." My assessment: probably not, at
  the price a payer will accept, without a pull incentive.
  PASTEUR Act would change this specifically and materially. It has
  been repeatedly introduced and not enacted. DO NOT MODEL IT.
  IP: 10 years exclusivity — strong on paper, worth little if the
  product cannot be priced.

RISK SUMMARY:
  1. Seventh entrant on an eight-programme graveyard axis, facing the
     exact bar that killed the last one, with ~50-60 subjects of
     exposure. — Mitigation: reposition to add-on/sequential. This is
     free and it is the single highest-value action available to the
     asset.
  2. Post-approval commercial survival ~0.20-0.30 against generic
     fidaxomicin. — Mitigation: none within the sponsor's control.
     Requires a pull incentive that does not exist.
  3. Single-Phase-3 structure concentrates rather than reduces risk.
     — Mitigation: pre-specify a design that can achieve high
     statistical persuasiveness, and secure agreement on what
     confirmatory evidence FDA will accept, at the End-of-Phase-2
     meeting rather than after the readout.
  4. Its differentiation leans on microbiome/secondary-bile-acid data,
     and FDA has never accepted a microbiome surrogate (§2.5). —
     Mitigation: none. The data must convert to clinical recurrence.

GO/NO-GO: HOLD. Do not fund as designed.
  Rationale: the most clinically advanced novel asset in the set and
  the worst capital efficiency in it — $5.3B per unit probability of
  durable access, 65x worse than the cheapest option (§7.2). Its
  problem was never financing; financing is what a bad expected value
  looks like from the inside. Reposition it and it becomes fundable;
  fund it as designed and it repeats Ri-CoDIFy with less exposure data.
  Key de-risking step: an End-of-Phase-2 meeting seeking agreement on
  an ADD-ON/SEQUENTIAL design with recurrence as primary. Costs
  ~$200K. Changes the asset's category.

CONFIDENCE: HIGH on the commercial analysis; MODERATE on PTS
═══════════════════════════════════════════════════════════
```

### 5.6 Berberine — **the cheapest real experiment in the pipeline, with the worst endpoint hazard**

```
═══════════════════════════════════════════════════════════
CLINICAL FEASIBILITY ASSESSMENT: Berberine
Pipeline score 5.5
═══════════════════════════════════════════════════════════
OVERALL FEASIBILITY: HIGH as an IIT, IMPRACTICAL as a product
ESTIMATED TIMELINE TO EVIDENCE: 4-5 years
ESTIMATED COST: $6-14M (IIT) — NOT a $45-85M programme
PTS (scientific question): 0.25-0.30
P(commercial survival): N/A — there is no product
P(durable patient access | positive trial): ~0.50, limited by
                                            PRODUCT STANDARDISATION
P(durable patient access): 0.135
CAPITAL EFFICIENCY: $81M per unit probability — BEST IN THE SET (§7.2)

RECOMMENDED PATHWAY:
  Route: NOT a 505(b)(2) — there is no US RLD for berberine as a drug.
         Three real options:
         (a) INVESTIGATOR-INITIATED TRIAL under an investigator IND,
             NIAID-funded. Output: evidence and a guideline
             recommendation. No NDA, no product. ← RECOMMENDED
         (b) 505(b)(1) full NDA on a standardised berberine drug
             product. 8-10 years, $80-150M, negative NPV. Not viable.
         (c) DSHEA structure/function claims. CANNOT claim CDI
             recurrence prevention. Useless for this purpose, and
             actively harmful if a positive trial gets marketed
             through this channel with unstandardised product.
  Designations: QIDP arguable as an antibacterial, but irrelevant on
         path (a) — there is no exclusivity to extend.
  ⚠ Data flag: ChemBL CHEMBL295124 records max_phase 4.0 with NO
         first_approval and withdrawn_flag TRUE with no reason, year,
         or country. Read as a data-quality artefact of legacy/non-US
         records — but it must not be quoted as evidence of approval
         OR of withdrawal without verification.

FUNDING VEHICLE (named, because "IIT" is not a funder):
  NIAID DMID, and specifically the ANTIBACTERIAL RESISTANCE LEADERSHIP
  GROUP (ARLG) — a NIAID-funded network whose explicit purpose is
  running trials of existing and non-commercial agents in difficult
  bacterial infections. CDI is squarely in scope; berberine is exactly
  the kind of asset no company will fund. Alternatives: PCORI
  (pragmatic comparative effectiveness), VA/DoD health system trials,
  academic-foundation consortia. ⚠verify current ARLG scope and
  funding cycles.

CLINICAL DEVELOPMENT:
  Phase 1: NO — Level 1 human safety at chronic oral doses including a
        large GI-indication RCT ⚠verify. Among these candidates only
        vancomycin, fidaxomicin, UDCA and niclosamide have comparable
        human safety, and none of those has rodent CDI efficacy data.
  Phase 2 (the whole programme): add-on to FIDAXOMICIN — NOT
        vancomycin — n~150, randomised placebo-controlled, recurrence
        through wk 8, toxin-EIA confirmed. 4-5 years, $6-14M.
  ⚑ PAIR WITH FIDAXOMICIN, NOT VANCOMYCIN, and note the cost: the
        rodent data supporting berberine was generated in the
        berberine+VANCOMYCIN configuration, and vancomycin is exactly
        the pair carrying the biofilm signal (1/2 MIC, p=0.02). So the
        safe combination is the one WITHOUT supporting animal data,
        and the supported combination is the one with a flagged risk.
        This is a genuine and unresolved design conflict; the honest
        resolution is to run the fidaxomicin pair and accept that the
        animal data does not transfer.
  Recruitment: MODERATE (13-39 sites, relaxed enrichment)

  ⚑ ENDPOINT INTEGRITY — THE MOST SERIOUS UNADDRESSED DESIGN DEFECT
    IN THIS PIPELINE (see §3.3 for the full argument):
    Berberine causes CONSTIPATION. On a diarrhoea-recurrence endpoint
    that biases FOR the drug — anti-conservative — while
    simultaneously (i) prolonging toxin contact time, the mechanism by
    which §4.1 says antimotility agents cause TOXIC MEGACOLON, and
    (ii) masking reduced stool output, the earliest sign of ileus.
    A blinded endpoint committee DOES NOT FIX THIS; it sees the same
    corrupted stool data. Required instead:
      1. Toxin-EIA confirmed recurrence as the sole primary component
      2. Prospective ileus/megacolon DSMB stop rule with mandated
         abdominal assessment and imaging triggers
      3. Pre-specified requirement that the benefit PERSISTS AFTER
         DRUG WITHDRAWAL — a motility artefact vanishes on washout,
         a microbiome/host effect does not. This is the only element
         that can distinguish them.
      4. Explicit exclusion of concomitant antimotility agents

COMMERCIAL VIABILITY:
  None, and that is the point of path (a). No IP, no owner, no
  product. ⚠ THE ACCESS RISK NOBODY HAS NAMED: a positive trial on
  one characterised, standardised extract DOES NOT TRANSFER to what
  patients buy at retail. Supplement berberine varies enormously in
  content and purity. A positive IIT could produce a guideline
  recommendation that patients cannot reliably act on. Mitigation:
  publish full characterisation of the trial material and pursue a
  USP monograph — cheap, and it is the difference between evidence and
  access.

RISK SUMMARY:
  1. Anti-conservative endpoint confound + toxic megacolon hazard.
     — Mitigation: the four-element design above. Non-optional.
  2. spo0A upregulation (a sporulation master regulator) — berberine
     may INCREASE sporulation, which would be directly counter-
     therapeutic on the axis that drives recurrence. — Mitigation:
     the $150-300K in vivo spo0A experiment, which the integrator
     ranks as the highest-value DISCONFIRMING experiment in the
     pipeline. RUN IT BEFORE THE TRIAL, not during.
  3. DDI in the highest-risk population: P-gp substrate/inhibitor,
     CYP3A4/2D6 inhibitor. The small absorbed fraction still matters
     against tacrolimus, cyclosporine, digoxin, DOACs (§3.3).
     — Mitigation: exclude narrow-TI CYP3A4/P-gp substrates, or
     protocol-mandate therapeutic drug monitoring. This materially
     narrows the enrollable population in a transplant/IBD-heavy
     disease — a recruitment cost not yet counted.
  4. Category credibility after PLACIDE and the probiotic collapse.
     — Mitigation: present as mechanistically-grounded pharmacology
     with a stated mechanism, explicitly distinguished from the failed
     probiotic class. §4.5 says a candidate must state which it is.

GO/NO-GO: CONDITIONAL ADVANCE as an IIT — run the spo0A experiment
  first ($150-300K), then a $6-14M ARLG/NIAID Phase 2.
  Rationale: the best capital efficiency in the set by a factor of 8,
  Level 1 human safety, rodent data already in the winning add-on
  configuration, and the only candidate hitting the host-directed
  white space and the microbiome space simultaneously. Gated on one
  disconfirming experiment and one non-negotiable design package.
  Key de-risking step: spo0A in vivo. If berberine increases
  sporulation, the programme is over for less than $300K.

CONFIDENCE: HIGH on path and cost; MODERATE on the science;
            HIGH on the endpoint hazard
═══════════════════════════════════════════════════════════
```

---

## 6. Summary — all six candidates

| Candidate | Route | Timeline | Cost | PTS | P(surv\|appr) | **P(access)** | Recruit | Endpoint bias | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Ribaxamase** | BLA 351(a) | 6–8 yr | **$150–280M** + acq | **0.35** | **0.60** | **0.210** | **EASY** | None | **Conditional advance — fund diligence** |
| **CamSA** | 505(b)(1) NDA | 9–13 yr | $80–140M | 0.12 | **0.65** | 0.078 | Moderate | Conservative | Research programme, not development |
| **UDCA** | 505(b)(2) | 5–6 yr | $45–85M + $1–3M | 0.14 | 0.12 / **0.75 access** | 0.105 | Moderate | Conservative | **Buy the $1–3M option** |
| **Berberine** | IIT / inv. IND | 4–5 yr | **$6–14M** | 0.27 | N/A / 0.50 access | 0.135 | Moderate | **ANTI-CONSERVATIVE ⚠** | Conditional IIT, spo0A gate first |
| **Niclosamide** | 505(b)(2) contingent | 8–11 yr | $75–140M | 0.02 → 0.22 | 0.35 | 0.077 | Moderate | Conservative | Fund $200–400K package, expect negative |
| **Ibezapolstat** | 505(b)(1) NDA | 6–8 yr | $120–200M | 0.12 | **0.25** | **0.030** | Easier | Conservative | **Hold — reposition before funding** |

**Regulatory designations, corrected:**

| Candidate | QIDP | Total exclusivity | Note |
|---|---|---|---|
| Ribaxamase | **NO** — not an antibacterial drug | **12 yr (BPCIA)** | Better than QIDP would give |
| CamSA | **YES, arguable — pursue** | **10 yr** (5 NCE + 5), +7 orphan possible | The one candidate QIDP genuinely helps |
| Ibezapolstat | **YES — granted** ⚠verify | 10 yr | Exclusivity is not the constraint |
| UDCA | Arguable at best | 3 yr (8 if granted) | Do not build the base case on it |
| Niclosamide | **NO** — anti-toxin, not antibacterial | 3 yr + formulation patents | My tasking's implied benefit is unavailable |
| Berberine | Arguable, irrelevant on IIT path | None | No exclusivity to extend |

---

## 7. The capital structure question

### 7.1 The four models map to three products, not one

| Model | Correct for | Why | Deliverable |
|---|---|---|---|
| **In-licensing orphaned de-risked assets** (BARDA/ASPR + AMR Action Fund + strategic partner) | **Ribaxamase**, NTCD-M3 | Positive human Phase 2 data available below replacement cost because the sponsor ran out of money. A capital defect is correctable; a pharmacodynamic defect is not. Ribaxamase additionally has the only aligned payer channel in the disease | An owned, surviving product |
| **NIAID/BARDA/PCORI grants for generic repurposing** | **UDCA**, niclosamide | Negative NPV for any commercial sponsor, by construction. But they need no post-approval survival — the product already exists and cannot be withdrawn | A guideline recommendation |
| **Foundation / academic IIT (ARLG, PCORI, VA/DoD)** | **Berberine**, and UDCA as an alternative | 1/5 the cost. Output is evidence, not a product. The only realistic vehicle for an unpatentable supplement | Published evidence |
| **Industry / equity** | **CamSA** only, and only after FTO | Requires composition-of-matter IP and 10 years of exclusivity to clear a venture return. CamSA is the only candidate that could plausibly meet that test — *if* the prior art permits a claim | A venture-backed NCE |
| ~~Industry (ibezapolstat)~~ | **Nothing** | Financing is not its problem; a bad expected value is. It launches against generic fidaxomicin into the channel that bankrupted Achaogen, Melinta, Tetraphase and Paratek. **Reposition it as an add-on before financing it** | — |

### 7.2 Capital efficiency — the metric that inverts the ranking

`$ per unit probability of durable patient access = cost / (PTS × P(access))`

| Asset | Cost ($M) | PTS | P(access) | P(durable access) | **$M per unit** | Rank |
|---|---|---|---|---|---|---|
| **Berberine (ARLG IIT)** | 11 | 0.27 | 0.50 | 0.135 | **81** | **1** |
| **UDCA (Fork A 505(b)(2))** | 68 | 0.14 | 0.75 | 0.105 | **648** | **2** |
| **Ribaxamase (acq + BLA)** | 230 | 0.35 | 0.60 | 0.210 | **1,095** | **3** |
| Niclosamide (post-package) | 108 | 0.22 | 0.35 | 0.077 | 1,403 | 4 |
| CamSA (NCE NDA) | 115 | 0.12 | 0.65 | 0.078 | 1,474 | 5 |
| **Ibezapolstat (1× Ph3)** | 160 | 0.12 | 0.25 | 0.030 | **5,333** | **6** |

**Read this table carefully, because it is easy to misuse.**

What it legitimately shows: **ibezapolstat is 65× less capital-efficient than berberine and 5× less than ribaxamase.** That gap is far too large to be an artefact of my probability estimates — it would survive halving berberine's PTS and doubling ibezapolstat's. Ibezapolstat's poor efficiency is *structural*: a replacement-positioned antibacterial pays the most for the least defensible commercial position.

What it does **not** show — the two corrections that keep it honest:

1. **Addressable population is not in the denominator.** Order-of-magnitude: enriched primary prevention could avert **~7,500–15,000 CDI cases/yr** (500K–1M high-risk IV β-lactam recipients × ~3% × 50% RRR); an rCDI add-on could avert **~12,000 recurrences/yr** (~30K multiply-recurrent patients × 40% RRR). These are the same order of magnitude, which is a genuinely non-obvious result — it means ribaxamase's larger population does *not* rescue it past berberine on efficiency, and equally that berberine's efficiency advantage does *not* come from serving a bigger population. Both estimates are ±3× at best.
2. **Evidence tier is not in the numerator.** Ribaxamase's 0.35 PTS rests on positive **human Phase 2b**; berberine's 0.27 rests on **rodent** data plus a live spo0A concern. Per §A.3, preclinical CDI evidence predicts Phase 3 poorly — so the honest reading is that berberine's PTS carries much wider error bars than ribaxamase's, in a direction that is more likely down than up.

> **Net: the table does not tell you to fund berberine instead of ribaxamase. It tells you that ibezapolstat should not be funded as designed, that UDCA and berberine are extraordinarily cheap ways to buy real probability, and that a funder without acquisition capacity is not thereby locked out of CDI.**

### 7.3 The mandate question that analysis cannot settle

Two funders should read this report and reach opposite conclusions, correctly:

- **A commercial funder** should conclude that only ribaxamase and CamSA are investable, that ribaxamase's aligned payer channel makes it the only near-term option, and that everything else is philanthropy.
- **A public-health funder (NIAID/BARDA/PCORI)** should conclude the opposite: that UDCA and berberine deliver 6–13× more probability-of-access per dollar, that their commercial worthlessness *is their durability* (§4.4), and that the assets a market withdraws are exactly the ones public money should not buy.

**Neither is wrong.** State the mandate before choosing the portfolio, or the portfolio will be chosen by whoever happens to answer the phone. That is, in one sentence, how six of twelve CDI programmes died.

---

## 8. The single most realistic development programme

### 8.1 Primary recommendation: enriched-label ribaxamase, gated on diligence

```
STAGE 1 — DILIGENCE GATE                        $300-500K      3-4 months
  CLINICAL / COMMERCIAL / REGULATORY WORKSTREAM   ($150-300K)
  a. Phase 2b data package: design, n, event counts, whether the CDI
     endpoint was primary or exploratory, and whether the effect
     survives a per-protocol/ITT split
  b. beta-lactam-attributable fraction of CDI — sizes the market
     ceiling and NOBODY IN THIS PIPELINE HAS QUANTIFIED IT
  c. PPI robustness of the delayed-release coating (§3.3: PPI use is
     near-universal in this population)
  d. Acquisition price, and the DAV132 competitive timeline
  e. CMS HAC/VBP inclusion and penalty magnitude for hospital-onset CDI
  CMC / TECH-TRANSFER WORKSTREAM (§5.1.1)         (+$150-200K)
  f. Master/working cell bank: in hand, characterised, TRANSFERABLE?
  g. Process tech-transferability: batch records, validated methods,
     qualified potency bioassay — or re-development required?
  h. RIGHT OF REFERENCE to the Phase 2b IND/data, or data only?
  i. Enteric-coat supplier qualification and release specification
  j. Phase 2b-to-Phase 3 batch comparability: required, and how large?
  KILL CRITERIA, set before negotiating: Phase 2b CDI endpoint was
  exploratory-only; OR beta-lactam-attributable fraction <40%; OR
  acquisition price above a pre-set threshold; OR DAV132 is >2 years
  ahead with equivalent effect; OR (f) the cell bank is not legally
  transferable; OR (h) there is no right of reference.
  DOWNSIDE IF (g) FAILS: +18-24 months and +$15-30M for process
  re-development and comparability, on top of Stage 3.

STAGE 2 — ACQUISITION + REGULATORY ALIGNMENT    $2-5M + acq    6-9 months
  Type B meeting: agree the ENRICHED population, incidence-based
  primary endpoint, single-trial acceptability and what confirmatory
  evidence FDA requires. Fast Track request. Do NOT request QIDP.

STAGE 3 — CMC                                   $25-50M        24-36 months
  Enzyme biologic process, potency assay, coating robustness across
  the gastric pH range. Runs parallel to Stage 4 start-up.

STAGE 4 — PHASE 3, ENRICHED                     $110-200M      36-42 months
  Hospitalised patients on IV beta-lactams with >=2 risk factors
  (age >=65, anticipated >=5d IV therapy, prior CDI, ICU stay).
  Target background incidence 8-10%. n ~900-1,100 for 50% RRR at 80%
  power. Primary: toxin-EIA-confirmed new-onset CDI through day 30
  post-antibiotic. Blinded adjudication committee.
  Recruitment: inpatients identified from the IV beta-lactam pharmacy
  order — 30-60% screen-to-enrol, not 0.5%.

STAGE 5 — BLA                                   $8-15M         12-15 months

TOTAL: $150-280M excluding acquisition · 6-8 years from close
FUNDING: BARDA/ASPR non-dilutive push funding for Stages 3-4 +
  AMR Action Fund for the acquisition + a strategic partner holding
  HOSPITAL-CHANNEL commercial infrastructure (not retail — the
  channel is the whole thesis).
COMMERCIAL: $800-1,500/course on the enriched label; the buyer is the
  hospital, which pays the CDI cost inside its DRG and the HAI
  penalty on top.
```

**Why this and not the others, in one line each:** it is the only candidate that escapes all four field-wide failure modes; the only one with an aligned payer; the only one with easy recruitment; the only one whose best evidence is human rather than rodent; and its defect is capital, which money fixes.

**If Stage 1 fails**, the fallback is not a consolation prize but a genuinely different bet: the **C1 germination programme** — CamSA as the molecule, UDCA as the fast clinical probe, positioned for the immunocompromised population where no live biotherapeutic can compete. Note that this fallback *shares the entire Stage 2 experimental package below*, so the package is worth funding either way.

### 8.2 Run this in parallel regardless — $1.8–4.5M, ~12 months

These are not alternatives to §8.1; they are cheap options on four candidates at once, and the sequencing dependency in item 1 is a hard one.

| # | Experiment | Cost | Decides |
|---|---|---|---|
| **1** | **Bile-acid germination dose-response** — UDCA, TUDCA, CDCA, CamSA, urso-CamSA vs taurocholate, full curves | $50–100K | **MUST PRECEDE Stage 0.** Generates the first UDCA IC₅₀; resolves the TUDCA conflict; prices the whole C1 axis. Without it Stage 0 compares a concentration to a threshold that does not exist |
| **2** | **Class-level spore-replenishment test** — does blocking germination *prevent* or merely *delay*, against a replenished spore load, with relapse-after-withdrawal readout | $150–300K | **The largest unasked question in the pipeline.** UDCA, CDCA, CamSA and urso-CamSA all die together if the answer is "delay." Nobody has proposed this design |
| **3** | Anaerobic faecal-slurry stability panel — niclosamide, berberine, CamSA, UDCA, at Eh ≈ −200 mV | $80–150K | Four agents independently nominated it; never done for any candidate |
| **4** | Commensal-spectrum MIC panel — *Lachnospiraceae*, *Ruminococcaceae*, *C. scindens/hiranonis*, *Bacteroides* | $100–200K | The central §6.4 question, and per Safety §8.6 the primary *toxicology* experiment for every antibacterial here. Only ibezapolstat has any of this data |
| **5** | Berberine spo0A in vivo | $150–300K | Highest-value disconfirming experiment. Kills or clears berberine for <$300K |
| **6** | Niclosamide kill-or-cure package + **FDA listed-drug determination letter** | $200–400K | Four gates at once. The FDA letter is nearly free and nobody has sent it |
| **7** | CamSA freedom-to-operate / patentability opinion | $50–100K | Could void CamSA's entire commercial rationale. **Not raised by any prior report** |
| **8** | Stage 0 faecal bile-acid PK (UDCA + chenodiol + taurocholate arms) — **after item 1** | $1–3M | Go/no-go on the fastest-path candidate |

**Total $1.8–4.5M and ~12 months resolves the go/no-go on five of six candidates** — roughly 2% of the cheapest development programme in this report.

### 8.3 Recommended portfolio

| Instrument | Asset | Spend | Funder | Decision point |
|---|---|---|---|---|
| **Programme** | Ribaxamase, enriched label | $300–500K → $150–280M | BARDA/ASPR + AMR Action Fund + hospital-channel strategic | Diligence gate, 3–4 mo |
| **Shared option** | Bile-acid axis (UDCA/CDCA/CamSA) | $1.8–4.5M | NIAID DMID / ARLG | 12 mo |
| **Cheap option** | Berberine spo0A → ARLG Phase 2 | $300K → $6–14M | NIAID / ARLG / PCORI | spo0A readout, 6–9 mo |
| **Kill package** | Niclosamide | $200–400K | Any | 4–6 mo, expect negative |
| **Free repositioning** | Ibezapolstat | $200K meeting | Current sponsor | EOP2 meeting on add-on design |
| **Do not fund** | Ibezapolstat as designed | — | — | — |


### 8.4 Total de-risking investment recommended — the consolidated number

The tasking asks for a single figure. There are properly **two**, because one item in the package is an order of magnitude larger than the rest and is **conditional on another item passing first**.

| Tranche | Items | Cost | Timing |
|---|---|---|---|
| **A — the diligence gate** | §8.1 Stage 1: clinical/commercial/regulatory **+ CMC/tech-transfer** (§5.1.1) | **$300–500K** | 3–4 mo |
| **B — the shared experimental package, unconditional** | §8.2 items 1–7: germination dose-response · class-level spore-replenishment test · anaerobic stability panel · commensal-spectrum MIC panel · berberine *spo0A* in vivo · niclosamide kill-or-cure + FDA listed-drug letter · CamSA FTO opinion | **$0.8–1.6M** | 2–9 mo, parallel |
| **Subtotal — everything that is unconditionally worth funding today** | | **$1.1–2.1M** | **≤12 mo** |
| **C — conditional, gated on B item 1** | §8.2 item 8: UDCA Stage 0 faecal bile-acid PK (± chenodiol, ± taurocholate arms) | **$1–3M** | 9–12 mo, **only after** an IC₅₀ exists |
| **TOTAL if C is triggered** | | **$2.1–5.1M** | 18–24 mo |

> **The number to quote is $1.1–2.1M.** That is the unconditional spend, it resolves the go/no-go on **all six** candidates in this report, and it is **under 1% of the cheapest development programme assessed here** ($150–280M for ribaxamase; $110–180M for ibezapolstat's single Phase 3; $45–85M for UDCA's full programme). The $1–3M Stage 0 tranche should not be committed until item 1 has produced the IC₅₀ it is meant to be compared against — commissioning it earlier spends $1–3M generating a concentration with no threshold, which is the single clearest sequencing error available in this pipeline.

**What the $1.1–2.1M buys, stated as decisions rather than data:** whether to acquire ribaxamase (A); whether the entire bile-acid germination axis is a real therapeutic strategy or a delaying one (B2 — the largest unasked question in the analysis, and the one that kills UDCA, chenodiol, CamSA and urso-CamSA together if it goes the wrong way); whether niclosamide's scaffold is salvageable (B6, expect a negative); whether berberine's mechanism contradicts its own endpoint (B5); and whether CamSA is even ownable (B7). **Five of the six candidates are resolved for less than the cost of a single Phase 2 site-year.**

**What it does not buy, and this is the honest limit of the recommendation:** none of these experiments addresses **C6 — epithelial barrier repair — which has zero coverage in the candidate set** (ranker §6.2), and none of them makes the C2 axis worth re-entering. A funder who spends $2.1M here has priced the assets in front of them very well and has not addressed the pipeline's structural gap. That gap is a discovery problem, not a de-risking problem, and it needs a different instrument.

---

## 9. Cross-cutting findings

1. **PTS and commercial survival are anti-correlated in CDI.** A single ranked list cannot express this, which is why the feasibility ranking (ribaxamase, UDCA, berberine, CamSA, niclosamide, ibezapolstat) differs from the pipeline's score ranking. Any final synthesis should present a 2×2, not a list.

2. **The trial-design decision that matters most is not add-on-versus-replacement (already settled) but *which* enrichment to keep.** Toxin-EIA confirmation is the PTS driver and must be kept; the ≥2-recurrence criterion is the recruitment killer and should be relaxed to MODIFY's risk-factor definition. This is a 5× recruitment improvement at no cost to the placebo event rate, and it converts a 150–200-site trial into a 13–39-site trial.

3. **Direction of endpoint bias is a distinct dimension from presence of endpoint confound**, and only berberine is anti-conservative. Its constipation inflates a diarrhoea endpoint *while masking the ileus signal* — a validity and safety problem that a blinded endpoint committee does not solve.

4. **Ribaxamase's payer alignment (CMS HAI penalty + inpatient DRG) is the strongest commercial argument available to any candidate in this analysis, and no prior report made it.** Equally, its NNT-capped pricing means an all-comers label destroys the asset. Both facts point to the same design change.

5. **QIDP is materially valuable to exactly one candidate (CamSA).** It is unavailable to ribaxamase and niclosamide (neither is an antibacterial drug), redundant for ribaxamase (BPCIA gives more), arguable-at-best for UDCA, and irrelevant to berberine and to an already-designated ibezapolstat whose constraint is commercial rather than exclusivity.

6. **"FDA is open to a single Phase 3" is not a de-risking fact.** A single trial halves cost and more than doubles variance, and single-trial acceptance requires statistical persuasiveness well beyond p<0.05 plus confirmatory evidence. For a financing-constrained sponsor it is leverage, not efficiency.

7. **My tasking's primary endpoint should be recurrence through week 8, not sustained clinical response at day 30.** They are different endpoints: sustained response is a composite that penalises a candidate for not improving initial cure, which is exactly how ridinilazole failed despite delivering its recurrence effect. All three CDI approvals used recurrence through week 8–12.

8. **In a market that withdraws approved products, un-ownable products are the ones that survive.** Bezlotoxumab had 12 years of exclusivity and is gone; generic ursodiol, if a trial ever supports it, cannot be withdrawn. This inverts the skill file's "no IP = no investment" guardrail for publicly-funded repurposing — the guardrail is about *investment*, and investment is not the only route to patients.

---

## 10. Items requiring verification before external use

| # | Claim | Why it matters |
|---|---|---|
| 1 | **Ribaxamase Phase 2b design and results** (primary vs exploratory CDI endpoint, n, event counts) | The §8.1 recommendation rests entirely on it. Flagged ⚠verify by the Repurposing Strategist and never resolved |
| 2 | **β-lactam-attributable fraction of CDI** | Sizes ribaxamase's market ceiling; unquantified by anyone in this pipeline |
| 3 | **CMS HAC Reduction Program / VBP inclusion of hospital-onset CDI and penalty magnitude** | The entire §4.2 payer-alignment argument |
| 4 | **PROCLAIM enrolment figures** (1,572 screened / 7 enrolled / 3 yrs) | Supplied in my tasking; it is the empirical anchor for every recruitment number in §3.1 |
| 5 | **DAV132 current phase and timeline** | The real competitor to ribaxamase; determines whether the acquisition window is open |
| 6 | **Ibezapolstat QIDP/Fast Track status; Acurx financing position** | Affects §5.5, though not its conclusion |
| 7 | **Generic fidaxomicin US availability and timing** | Load-bearing for ibezapolstat's commercial survival estimate |
| 8 | **Niclosamide US listed-drug/RLD status** | Determines whether niclosamide has a 505(b)(2) path at all |
| 9 | **High-dose UDCA PSC harm signal** (28–30 mg/kg/d) | The dose ceiling on the fastest-path candidate |
| 10 | **UDCA/CDCA/CamSA anti-germination IC₅₀ values** | Stage 0's entire go/no-go criterion; the UDCA value appears not to exist |
| 11 | **CamSA prior art and patentability** | Could void CamSA's commercial rationale entirely |
| 12 | **Berberine Level 1 human RCT data** (the ~1,100-patient GI trial) | The basis for skipping Phase 1 |
| 13 | **ARLG current scope and funding mechanisms for CDI** | The named funding vehicle for berberine and UDCA Fork A |
| 14 | **Orphan designation precedent for recurrent CDI** | Worth 7 years; stacks with QIDP |
| 15 | **Bezlotoxumab discontinuation date and stated reason** | The load-bearing example in §4.1 |
| 16 | **Ribaxamase asset condition** — master/working cell bank existence, characterisation and legal transferability; right of reference to the Phase 2b IND; enteric-coat supplier qualification | §5.1.1. Items 1 and 3 of that list are **binary deal-breakers** and are the most likely way the top recommendation dies *after* close rather than before it. Nothing in this pipeline addressed asset condition as distinct from asset data |

---

## 11. Research disclaimer

All cost, timeline, sample-size, PTS, commercial-survival, and capital-efficiency figures in this report are **estimates derived from published base rates, the disease model, and upstream agent reports** — no primary data was generated and no live literature or trial-registry retrieval was performed. Sample sizes are computed analytically (normal approximation, 80% power, α=0.05 two-sided) and validated against two actual CDI trials to within ~15–20%; they are adequate for programme sizing and are **not** a substitute for a statistician's protocol-specific calculation. PTS and commercial-survival probabilities are **structured judgements** built by compounding named gates, not empirical frequencies; the capital-efficiency table in §7.2 is a sensitivity tool whose *ordinal* conclusions (particularly ibezapolstat's position) are robust and whose *cardinal* values are not. Population estimates in §7.2 are order-of-magnitude and should be treated as ±3×. The §5.1.1 process-re-development downside (+18–24 months, +$15–30M) is a typical-case estimate for a biologics tech transfer that has to be re-derived, not a figure specific to this asset — its purpose is to size a diligence question, not to price a known defect. Every item in §10 must be cleared before any external-facing use, and item 1 gates the report's primary recommendation.

---

*End of Phase 3 Clinical Feasibility Assessment.*
