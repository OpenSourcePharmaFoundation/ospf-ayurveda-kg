# P1 — Clinical Landscape Assessment: Diabetic Retinopathy

**Agent:** Clinical Landscape Researcher
**Run:** blinded benchmark, 2026-10-05
**Scope:** treatment landscape at modality level · non-DR clinical track record of 15 candidates ·
trial design for two development paths · phenotype enrichment · regulatory pathway for oral generics ·
competitive landscape at mechanism class level · development economics

---

## 0. Blinding posture — read this before anything else

My normal job is to assess clinical precedent. For DR, clinical precedent **is** the held-out
information. I have therefore restricted myself as follows, and the reader should check my work
against these rules rather than trusting them:

**Used freely (allowed):**
- The DR/DME treatment landscape at **modality class** level — intravitreal anti-VEGF, intravitreal
  corticosteroid, panretinal and focal/grid laser, vitrectomy, systemic risk-factor control as a
  category. All of this is supplied by `disease-model.md` §4.1 and §6.3 and is not candidate-specific.
- Trial design, endpoints, regulatory mechanics and development economics for ophthalmic indications
  **generally**.
- Each candidate's **approved indications outside DR/DME**, the size and shape of its chronic-exposure
  safety database, its adverse-event profile from that experience, generic status and cost of goods.
- Drug-development arithmetic (power, enrolment rate, per-patient cost) which is indication-agnostic.

**Not used (forbidden, and actively suppressed):**
- Any statement, hint, or implicit weighting that a named candidate has been studied, trialed,
  approved, guideline-recommended, or shown any effect in DR or DME.

Three candidates in this set sit on exactly that line. See §9 for the full disclosure; in short, I
hold DR-specific trial knowledge for **fenofibrate/fenofibric acid**, **candesartan**, and
**minocycline**, and I have excluded it from every score. Where that knowledge would have *raised* a
score, the score is lower than it "should" be, and that is the correct behaviour for this run.

**Scoring axis.** Every score in §10 is **clinical and developmental viability, not DR efficacy.**
It is a composite of six things:

| Weight | Component |
|---|---|
| High | Size and quality of the chronic human safety database |
| High | Suitability of the AE profile for **lifelong dosing in asymptomatic or minimally symptomatic people** |
| High | Regulatory tractability — does a reference listed drug exist, is 505(b)(2)/Art.10(3) available |
| Medium | Trial-conduct feasibility — blinding hazards, background-use confound, dosing frequency, monitoring burden |
| Medium | Cost of goods, global availability, LMIC deployability |
| Medium | Whether **any** funding path exists at all |

A drug can score high here and still be pharmacologically hopeless for DR. That is intentional —
the ranker should multiply this score by the mechanism agents' scores, not average them.

---

## 1. (a) The DR treatment landscape at modality level

### 1.1 What exists, and who it actually serves

Five modalities, and a sixth that is not a treatment at all but determines who gets one.

| Modality | Serves | Typical regimen | Per-eye cost (US, order of magnitude) | Infrastructure required |
|---|---|---|---|---|
| **Intravitreal anti-VEGF** | Center-involving DME; PDR; severe NPDR progression risk | 4–6 loading doses then q4–q16wk indefinitely; 8–10 injections yr 1, 4–6/yr thereafter | Branded drug ~$1,800–2,000/dose → **$8,000–20,000/yr**; repackaged low-cost option ~$50–70/dose + ~$150–300 procedure | Retina specialist, sterile procedure room, OCT at nearly every visit |
| **Intravitreal corticosteroid** (implant / suspension) | Inflammatory-phenotype DME; pseudophakic eyes; incomplete anti-VEGF responders | Biodegradable implant q3–6mo, or non-biodegradable insert ~36 months | ~$1,300/implant; ~$8,800 for a 3-year insert | Same, plus IOP surveillance and near-certain cataract surgery in phakic eyes |
| **Focal / grid laser** | Non-center-involving DME; persistent extrafoveal leak | 1–3 sessions, sometimes repeated over years | ~$300–800/session | Laser, slit lamp, FA or OCT guidance |
| **Panretinal photocoagulation** | PDR; selected severe NPDR | 1,200–2,000 burns over 2–4 sessions | ~$500–1,500/course | Laser + trained operator; **cheapest durable option, which is why it persists** |
| **Pars plana vitrectomy** | Non-clearing vitreous haemorrhage, tractional detachment, VMT-associated DME | One-time surgery, sometimes staged | ~$4,000–10,000 facility + surgeon | Operating theatre, vitreoretinal surgeon, microincisional platform |
| **Systemic risk-factor control** *(not DR-specific)* | Everyone | Lifelong | Cents to dollars per day | Primary care |
| **Screening** *(gating infrastructure)* | Everyone with diabetes | Annual to biennial fundus imaging | $20–60/encounter; autonomous AI grading now cleared in US/EU and cheaper still | Camera + grading pathway; **the one piece of DR infrastructure that already scales** |

`[ESTABLISHED]` on the modality structure; `[CURRENT CONSENSUS]` on the cost figures, which vary
enormously by payer and country.

### 1.2 The access arithmetic — this is the number that defines the white space

- ~103 million adults have DR; ~28–30 million have vision-threatening DR (`disease-model.md` §1.2).
- Everything in the table above except screening and systemic risk-factor control requires a
  **vitreoretinal specialist**. Order-of-magnitude specialist density: roughly 1 per ~120,000 people in
  the US; roughly 1 per ~500,000–600,000 in India, which carries ~100M people with diabetes; in much
  of sub-Saharan Africa the ratio is one per several million, and several countries have none.
  `[CURRENT CONSENSUS]`, order-of-magnitude only.
- Therefore the binding constraint on DR treatment globally is **not drug cost** — a repackaged
  anti-VEGF dose can be had for tens of dollars — it is **procedural capacity**. Making the drug free
  would not fix it. This is the single most important structural fact in the landscape and it is why
  unmet need #8 ("deployable without specialist infrastructure") is not a footnote but a reframing of
  the whole problem.
- Even inside well-resourced systems, the modality fails on **adherence**: real-world visual outcomes
  are consistently worse than trial outcomes largely because patients receive fewer injections than
  protocol (`disease-model.md` §4.2.2). The modality is effective; its *delivery* is not.

### 1.3 Where the white space is

Mapping the model's ranked limitations onto the modality table above, four gaps are genuinely
unserved by *any* modality — not served badly, but not served at all:

| Gap | Population size | Served by any modality? | Why it is structurally hard |
|---|---|---|---|
| **1. Early / preclinical disease (S0–S2)** | The large majority of 103M | **No.** The pathway is "observe until sick enough to inject" | No procedure can be justified in an asymptomatic eye; only a systemic agent is deployable. Endpoint moves over years |
| **2. Incomplete responders in DME (30–50% of treated)** | ~30–50% of the ~5–7% of PWD with DME; several million | Partially — switching classes, adding steroid | Heterogeneous: at least five distinct mechanisms sit under one label (model §4.2.3). An all-comers trial dilutes any of them |
| **3. Neuroprotection / the function–anatomy gap** | All stages | **No** | No validated registrational functional endpoint independent of BCVA |
| **4. Treatment burden** | Everyone on injections | Being attacked from the *other* direction — see §7 | Longer-acting intravitreals are the incumbent's answer, and they are winning |

Plus two with no modality and no obvious path: **macular ischemia/reperfusion** and **hard exudate
clearance**. The second of these is notable because it is measurable on equipment that already exists
in every screening programme (colour fundus photography; OCT hyperreflective foci) — a rare case where
the unmet need and the cheap endpoint coincide.

**Landscape verdict.** The DR field has a well-capitalised, procedurally-delivered, specialist-gated
set of modalities that work well for late disease in rich countries, and nothing at all for the first
decade of the disease or for most of the world. An oral systemic agent does not compete with that
stack. It occupies the time before it and the geography outside it.

---

## 2. (b) Non-DR clinical track record of the 15 candidates

Everything below is drawn from each molecule's **non-DR** approved use and post-marketing experience.
Exposure figures are order-of-magnitude; treat them as `[CURRENT CONSENSUS]` unless marked.

### Group A — direct PPARα agonists

| | **A1 Fenofibric acid** | **A2 Fenofibrate** | **A3 Pemafibrate** |
|---|---|---|---|
| Approved for | Severe hypertriglyceridaemia; primary hyperlipidaemia; mixed dyslipidaemia | Same (the prodrug form) | Hyperlipidaemia / hypertriglyceridaemia — **Japan only** |
| First approval | 2008 (US, incl. choline salt, delayed-release) | 1993 US; fibrate class in Europe from the mid-1970s | 2017 |
| Chronic-exposure database | Shared with the fenofibrate family: **tens of millions of patient-years**, several decades, in exactly the comorbid diabetic/dyslipidaemic population of interest | As A1 — the most-used fibrate worldwide | Large Japanese post-marketing experience plus a **~10,000-patient cardiovascular outcomes trial in hypertriglyceridaemic T2D**, median ~3–3.5 yr follow-up (neutral on its CV primary endpoint) |
| AE profile from that experience | Reversible serum creatinine rise (~10–15%); myopathy, amplified with statins; rare rhabdomyolysis; transaminase elevation; cholelithiasis; homocysteine elevation; a venous-thromboembolism signal in large trials; pancreatitis | Identical (same active moiety) | Reported in the outcomes trial: more adverse renal events and more venous thromboembolism vs placebo; less hepatic steatosis. Little myopathy signal; minimal creatinine effect. `[EMERGING]` on the renal/VTE signals |
| Elimination | **Renal**, as the acyl glucuronide. Dose-reduce in moderate CKD, avoid in severe | Same | **Hepatic/biliary**; no dose adjustment in moderate CKD |
| Generic / COGS | Generic; **~$0.05–0.30/day** | Generic; **~$0.03–0.20/day**, available in essentially every national formulary | **Branded, Japan-only.** Order of magnitude more expensive; no US/EU RLD |

**A4 Elafibranor** — approved 2024 (US accelerated, EU conditional) for primary biliary cholangitis in
combination with UDCA. Chronic-exposure database is **small**: a few hundred patients in the pivotal
PBC programme plus ~2,000 patients from a failed Phase III steatohepatitis programme; ~2 years of
marketing. AEs: weight gain, abdominal pain/nausea, myalgia and a fracture signal, reversible
creatinine rise, hepatic-injury monitoring. Structural flag carried forward from the scout: the
**Michael-acceptor enone**, i.e. a covalent-reactivity motif, which is a different risk conversation at
10 years of dosing than at 2. Orphan-indication pricing.

**A5 Seladelpar** — approved 2024 for PBC. Same shape as A4: small database, ~2 years on market,
orphan pricing, no chronic-use experience worth the name. Additional class consideration: PPARδ
agonism carries a historical rodent carcinogenicity concern from the exercise-mimetic chemical
series, which matters specifically for a lifelong preventive indication. The brief designates this
molecule an **isoform falsification control**, and I score it as a development candidate only — see
the note in §10.

### Group B — natural products and endogenous ligands

**B1 Linoleic acid**, **B2 α-linolenic acid** — dietary nutrients. No approved indication, no RLD, no
NDA pathway, no CMC-compliant drug product. They cannot be dosed without displacing other dietary fat,
and they cannot be placebo-controlled without a lipid comparator that is itself biologically active.
Their "safety database" is human nutrition, which is reassuring and useless: it tells you nothing
about a defined pharmacologic dose. Development viability as **drugs** is near zero; as **dietary
interventions** they inherit the entire unhappy history of long, confounded, underpowered nutrition
trials.

**B3 Linalool** — a GRAS flavour/fragrance monoterpene. No clinical development, no meaningful human
PK, no chronic oral dosing data at pharmacologic doses. Known **contact sensitiser** in its oxidised
form, which is a dermatologic rather than oral concern but signals reactive-chemistry handling. Any
programme starts at a full IND with tox from scratch.

**B4 Icosapent ethyl** — approved 2012 (US) for severe hypertriglyceridaemia, label expanded 2019 for
cardiovascular risk reduction in statin-treated patients with elevated triglycerides. **This is the
only Group B molecule with a real clinical record.** Chronic-exposure database: a ~8,000-patient CV
outcomes trial with median ~5 years of follow-up, in a population that substantially overlaps the DR
population, plus a decade of commercial use. AEs: **increased atrial fibrillation/flutter**, increased
bleeding (notably with antithrombotics, which this population is often on), peripheral oedema,
musculoskeletal pain, GI effects. Now **generic** in the US following patent litigation. Practical
burden: 4 g/day as four large capsules — a non-trivial adherence problem layered onto existing
polypharmacy.

### Group C

**C1 Quercetin** — a dietary supplement. No approved indication anywhere, no RLD, therefore **no
505(b)(2) and no Art.10(3)**: a full IND and NDA from zero. Oral bioavailability <2% with extreme
inter-product variability; supplement-grade material would not survive CMC review. Chronic human
exposure is dietary, uncharacterised at pharmacologic dose. The brief independently designates it the
frequent-hitter control.

**C2 Melatonin** — regulatory status is more favourable than people assume and deserves to be stated
precisely. In the US it is a **dietary supplement** with no RLD. In the **EU/UK it is an approved
prescription medicine** (prolonged-release melatonin for insomnia in adults ≥55, and for insomnia in
children with autism spectrum disorder / Smith–Magenis syndrome) — so **an EU hybrid pathway exists**.
Safety is excellent: somnolence, headache, vivid dreams; paediatric safety data out to roughly two
years. Two specific concerns for *this* population: (i) pharmacologic melatonin taken near meals can
modestly impair glucose tolerance, which is a real issue in a diabetic trial and would need dosing
away from meals plus HbA1c monitoring as a safety endpoint; (ii) US supplement-grade product content
varies widely, so any trial must use pharmaceutical-grade material. Cost of goods is trivial.

### Group D — non-PPARα comparators

**D1 Epalrestat** — approved in **Japan (1992) and India** for diabetic peripheral neuropathy; **not
approved in the US or EU**, where the aldose-reductase class was abandoned. Chronic-exposure database:
decades of Japanese and Indian use, plausibly hundreds of thousands of patient-years, in diabetics.
Generally well tolerated; transaminase elevation, GI effects. Two concrete development liabilities:
**TID dosing** (50 mg three times daily), a poor fit for a lifelong preventive; and **chromaturia** —
it turns urine reddish-brown, which is an unmistakable, patient-visible effect and therefore a
**functional unblinding hazard** in any placebo-controlled trial. No US/EU RLD means a full NDA.
Independently, `disease-model.md` §4.4 carries a strong negative prior on the **mechanism** (P1), which
caps expected value regardless of viability.

**D2 Dimethyl fumarate** — approved 2013 (US/EU) for relapsing multiple sclerosis; fumaric acid esters
have been used for psoriasis in Germany since 1994. Chronic-exposure database is **large and
high-quality**: several hundred thousand MS patients with multi-year exposure, plus three decades of
dermatologic use. AEs: flushing (very common, ~35%, and another **unblinding hazard** — it is
unmistakable to the patient), GI upset, **lymphopenia** that can be prolonged and severe, **PML**
(rare, fatal), proteinuria and Fanconi-syndrome reports, hepatotoxicity. BID dosing. Generic available.

> **Landscape judgement on D2.** The database is excellent and the AE profile is acceptable *for
> active MS*. It is close to disqualifying for **asymptomatic prevention**. The risk–benefit bar for
> treating a person with no symptoms for ten years is far above the bar for treating active relapsing
> disease, and a programme that asks regulators to accept a non-zero PML risk in people who can
> currently see perfectly well will not get a receptive hearing. Plus mandatory lymphocyte monitoring
> destroys the LMIC deployability argument.

**D3 Minocycline** — approved 1971; acne and infections; chronic low-dose acne use often runs for
years. Chronic-exposure database is **very large** (tens of millions treated). AEs relevant to
lifelong dosing: vestibular toxicity (dizziness/vertigo, common and dose-limiting), **blue-grey
pigmentation of skin, sclera, mucosa and bone that increases with cumulative dose** (both a
disqualifier for decades of dosing and a visible unblinding hazard), drug-induced lupus, DRESS,
autoimmune hepatitis, photosensitivity, and **benign intracranial hypertension with papilloedema** —
an *ocular* adverse effect that would directly confound a retinal trial. 

> **Landscape judgement on D3.** Beyond the individual AE profile there is a population-level
> objection that is, in my view, decisive: you cannot put tens of millions of people on a
> **tetracycline antibiotic for a decade**. Antimicrobial stewardship and microbiome considerations
> make this a public-health non-starter at the scale the indication implies, independent of any
> efficacy question. Minocycline could only ever be a short-course or narrow-subpopulation agent.

**D4 Candesartan cilexetil** — approved 1998 (US) for hypertension, later heart failure.
Chronic-exposure database is enormous — the ARB class is among the most-prescribed in the world, and
candesartan specifically carries large multi-year outcome trial datasets in heart failure (~7,600
patients) and elderly hypertension (~4,900). Generic since ~2012; very cheap; globally available. AEs:
hypotension/dizziness, hyperkalaemia, acute kidney injury with volume depletion or NSAID co-use or dual
RAS blockade, and **teratogenicity — contraindicated in pregnancy**, which is awkward in a population
that includes a large number of women of childbearing age with long-duration type 1 diabetes.

> **Landscape judgement on D4 — the background-use problem.** This is the most severe
> trial-feasibility obstacle of any candidate in the set, and it has nothing to do with the drug's
> merits. RAS blockade is already standard of care for hypertension and diabetic kidney disease in
> this exact population. To run a clean placebo-controlled trial you must enrol **normotensive,
> non-albuminuric** diabetics — a minority of the population, systematically younger and healthier,
> with a *lower* event rate, which inflates sample size at the same time as it shrinks the eligible
> pool. And blood-pressure lowering itself is both a confounder and a plausible effect modifier, so a
> positive result would be hard to attribute to the proposed mechanism. An add-on-to-existing-ARB
> design avoids the enrolment problem but tests dose-intensification rather than the mechanism.

---

## 3. (c) Trial design — the two paths

This is the strategic core of the assessment. Call them **Path A** (early-DR disease modification) and
**Path B** (DME incomplete-responder adjunct).

### 3.1 Path A — disease modification in early DR

**The endpoint and how slowly it moves.** The accepted registrational currency is change on the
**ETDRS Diabetic Retinopathy Severity Scale (DRSS)**, graded from standardised fundus photographs by a
masked reading centre. Conventionally: **≥2-step improvement** for a benefit claim, **≥2-step or
≥3-step worsening** for a prevention-of-progression claim (the 3-step person-level definition is the
more conservative and the more defensible). Regulatory precedent for DRSS change as a basis for a
retinopathy indication exists at modality level (`disease-model.md` §4.1 — anti-VEGF is used in severe
NPDR precisely to reduce progression risk).

The problem is arithmetic, not acceptance. In **mild-to-moderate NPDR**, ≥2-step progression runs at
roughly **5–10% per year**, and ≥3-step progression over four years lands somewhere around
**10–20%** `[CURRENT CONSENSUS]`. In severe NPDR the rate is far higher — but severe NPDR is not the
population Path A is for, and treating it moves you into territory where effective therapy already
exists (a scoring prior the brief explicitly flags).

**Sample size.** Two-sided α=0.05, 90% power, two-proportion comparison of cumulative ≥3-step
progression at 4 years:

| Control 4-yr event rate | Relative risk reduction sought | n per arm | n total | +25% for dropout/loss |
|---|---|---|---|---|
| 15% | 30% (→10.5%) | ~1,150 | ~2,300 | **~2,900** |
| 15% | 25% (→11.3%) | ~1,700 | ~3,400 | **~4,300** |
| 20% | 30% (→14%) | ~830 | ~1,660 | **~2,100** |
| 10% | 30% (→7%) | ~1,800 | ~3,600 | **~4,500** |

A four-to-five-year trial in diabetics loses patients steadily, so the 25% inflation is optimistic;
30–35% is more honest. **Call it 3,000–4,500 randomised, 4–5 years on treatment.**

**A secular-trend risk that is easy to miss.** Background systemic metabolic care in this population is
improving rapidly and is now dominated by newer agent classes with substantial metabolic and
cardiovascular effects. A control arm recruited in 2027 will progress more slowly than the historical
cohorts the above rates come from. **Every percentage point the control event rate falls inflates
sample size roughly quadratically in the region of interest.** This is a genuine, under-discussed
threat to Path A power, and it argues for an event-driven rather than fixed-duration design.

**Cost.** Ophthalmic imaging trials are cheap per patient relative to oncology — the per-visit cost is
imaging plus a short exam, not infusion suites or biopsies. Roughly:

- Conventional multicentre design: **$12,000–20,000 per patient over 4–5 years** (6-monthly visits,
  stereoscopic 7-field or ultrawide-field photography, OCT, reading-centre grading, safety labs).
- 3,000 patients × $15,000 ≈ **$45M**, plus reading centre, DSMB, coordination, regulatory, statistics,
  drug supply and a long tail → **$60–100M all-in, 6–7 years from start to filing.**

**Could a surrogate shorten it?** Four candidates, none currently qualified:

| Candidate surrogate | Attraction | Why it is not yet usable |
|---|---|---|
| **Microaneurysm turnover rate** | Best-validated predictor of subsequent progression; computable from the same photographs; moves in months not years | Not a qualified regulatory endpoint; grading is automatable but not standardised across platforms |
| **Ultrawide-field peripheral lesion burden** | Captures peripheral disease that 7-field misses; plausibly raises measurable event rates substantially and therefore **shrinks sample size for free** | The UWF-to-DRSS mapping is not formally qualified; mixing UWF and ETDRS grading across sites invites heterogeneity |
| **OCT structural — GCL-IPL thinning rate, hyperreflective foci, hard exudate area** | Continuous rather than categorical → far more statistically efficient than a 2-step jump; equipment already everywhere | Only hard-exudate area has an intuitive link to a clinical outcome; thinning rate is confounded by age and glycaemia |
| **Functional — mfERG implicit time, flicker-induced vasodilation, microperimetry, contrast sensitivity** | Directly addresses the neuroprotection gap; moves early | No registrational precedent; high test–retest variability; equipment burden limits site count |

**My read:** continuous imaging endpoints are the right **Phase II** currency and should carry the
go/no-go decision. None of them will carry a Phase III. The honest position is that **Path A's
registrational endpoint is fixed, slow, and categorical, and there is no shortcut** — the lever is not
the endpoint, it is the *cost per patient* (see §8.2).

**Realistic Path A plan.**
- **Phase II:** n ≈ 200–300, 18–24 months, randomised, double-masked, placebo-controlled. Co-primary:
  MA turnover rate + change in a continuous OCT structural measure. Secondary: ≥2-step DRSS, mfERG,
  contrast sensitivity, hard exudate area. Purpose: dose selection and a signal, not proof.
- **Phase III:** n ≈ 3,000–4,500, 4–5 years, event-driven, ≥3-step DRSS progression primary, UWF
  imaging if a qualification path can be negotiated with the agency in advance.

### 3.2 Path B — adjunct in DME incomplete responders

**Population.** Centre-involving DME with persistent central subfield thickness elevation and/or
residual BCVA deficit after a protocol-defined anti-VEGF loading course (≥3–6 monthly injections).
This is 30–50% of treated DME (`disease-model.md` §4.2.3) — a large, already-identified, already-in-clinic
population.

**Design.** Randomised, double-masked, placebo-controlled **add-on** to continued protocol-driven
anti-VEGF (treat-and-extend or PRN with pre-specified retreatment criteria), 52 weeks. The background
therapy is held at protocol, so the oral agent is tested as an increment, not a replacement — which is
both the honest scientific framing and the one that avoids an ethics problem.

**Endpoints, and the power arithmetic that makes this path attractive.** Assuming α=0.05 two-sided and
90% power:

| Endpoint | Assumed SD of 52-wk change | Difference sought | n per arm | n total |
|---|---|---|---|---|
| BCVA (ETDRS letters) | 11 letters | **3 letters** | ~285 | ~570 |
| BCVA | 11 letters | **5 letters** | ~105 | ~210 |
| Central subfield thickness (µm) | 100 µm | **40 µm** | ~135 | ~270 |
| **Injection count over 52 wks** | 3.0 injections | **1.5 fewer injections** | **~85** | **~170** |
| Injection count | 3.0 | 1.0 fewer | ~190 | ~380 |

> **This is the single most actionable finding in the trial-design section.** The
> **injection-count endpoint is by far the cheapest to power** — roughly a third of the sample size of
> a 3-letter BCVA difference — because the measure is a count with modest variance rather than a noisy
> psychophysical test. It also maps directly onto unmet need #4, which is a need patients and payers
> both feel. A **co-primary of (injection count, BCVA non-inferiority)** is the design that extracts
> the most regulatory value per dollar. The risk is that a burden-reduction claim is only persuasive
> if the field has not already solved burden by other means — see §7.

**Duration and cost.** Each trial is **one year of patient time**, which is the decisive difference
from Path A. Per-patient cost is *higher* than Path A — monthly or near-monthly visits, OCT at every
visit, injections, more intensive safety capture — call it **$35,000–60,000 per patient**.

- **Phase II:** n ≈ 200, ~2.5 years calendar → **~$8–12M**
- **Phase III:** two trials × ~600 = 1,200 patients, ~4 years calendar → **~$55–70M**
- **Total ≈ $65–85M over ~6–7 years**, but with a **decision-grade readout at ~2.5 years** instead of
  ~6.

### 3.3 Path comparison

| | **Path A — early DR disease modification** | **Path B — DME incomplete-responder adjunct** |
|---|---|---|
| Population | S0–S2 NPDR; the large majority of 103M | CI-DME with incomplete anti-VEGF response; low single-digit millions |
| Primary endpoint | ≥3-step (or ≥2-step) DRSS progression | Injection count + BCVA non-inferiority; or BCVA + CST |
| Endpoint status | Accepted but categorical and slow | Accepted, continuous/countable, fast |
| Phase II size / duration | 200–300 / 18–24 mo | ~200 / 12 mo treatment |
| Phase III size | 3,000–4,500 | ~1,200 across two trials |
| Treatment duration per patient | **4–5 years** | **1 year** |
| Time to first decision-grade signal | ~4 years from start | **~2.5 years from start** |
| Total programme cost | $60–100M | $65–85M |
| Total programme duration | 8–10 years | 6–7 years |
| Dropout exposure | **High** — 4–5 yr follow-up in diabetics | Low — 1 yr, and patients are already attending monthly |
| Control-arm drift risk | **High** — improving background metabolic care erodes event rate | Low — background anti-VEGF is protocolised inside the trial |
| Probability of success (programme, from Phase II start) | **~10–15%** — ophthalmology base rate ~18% Ph1→approval, adjusted *down* for a long categorical endpoint, dropout, adherence, and the model's §4.4 record of systemic mechanisms failing to move DRSS | **~20–30%** — adjusted *up* for a short accepted endpoint and a defined population, *down* for the thin margin available on top of effective background therapy |
| Label value if won | Enormous population; first-in-class; transformative | Narrow; adjunct; second-line |
| Commercial viability for a **generic oral** | **Nil** — no pricing power over a $0.10/day pill | **Nil without reformulation** — same problem, smaller population |
| Who would fund it | Public / academic networks, philanthropy, global health | A sponsor **only** if a formulation or FDC creates IP |
| Strategic verdict | The prize. Unfundable commercially. **Fundable publicly only if per-patient cost collapses** (§8.2) | The de-risking step. Run it first — it generates the human proof-of-mechanism that makes anyone willing to fund Path A |

**Recommended sequencing.** Path B first, as a Phase II of ~200 patients with injection count and CST
as co-primaries, enriched or at least stratified by phenotype (§4). That is **$8–12M and ~2.5 years**
— an order of magnitude cheaper than the Path A Phase III and within reach of a single large public or
philanthropic grant. A positive readout converts Path A from a speculative mechanistic bet into a
fundable programme with human precedent. A negative readout kills both paths for a tenth of the money.
Running Path A first is the error to avoid: it bets $60–100M and six years on a mechanism with no human
ocular signal.

---

## 4. (d) Phenotype-enriched trial design

Take the lipid/exudative DME phenotype as the worked example, since the brief's focus mechanism (P8)
maps onto it.

**Enrichment criterion.** Two-part, both measurable with equipment already in every retina clinic:
1. **Ocular:** hard exudate present within 1,500 µm of the foveal centre on colour fundus photography,
   or OCT hyperreflective-foci burden above a pre-specified reading-centre threshold. Graded centrally,
   not at site, to avoid the enrolment inflation that site-read eligibility criteria always produce.
2. **Systemic (optional, strengthens the mechanistic argument):** fasting triglycerides above ~150–200
   mg/dL, or non-HDL-C or apoB above a threshold.

**The enrolment arithmetic.** Rough prevalences, all `[CURRENT CONSENSUS]` and order-of-magnitude:

| Filter | Fraction surviving | Cumulative |
|---|---|---|
| Centre-involving DME under active anti-VEGF treatment | — | 100% of the screened pool |
| Incomplete responder after loading | ~0.40 | 40% |
| Hard exudate within 1,500 µm of fovea | ~0.35 | ~14% |
| Systemic lipid criterion (if applied) | ~0.60 | ~8% |
| Consent + all other I/E criteria (media clarity, prior treatment windows, comorbidity exclusions) | ~0.55 | **~5% (with lipid criterion) / ~8% (ocular only)** |

To enrol **300 patients** at ~8% net eligibility you must **screen ~3,750 actively-treated DME
patients**. A busy retina practice carries perhaps 150–400 such patients at any time, and you can
realistically screen a fraction of them per month. That implies roughly **30–45 sites and 15–20 months
of enrolment** — feasible, but not fast.

**Does enrichment make the trial smaller, or merely slower? Both — and the ratio decides it.**

The two scalings pull in opposite directions:
- Sample size scales as **1/Δ²** in the effect size.
- Enrolment *duration* scales as **n / (eligibility × sites × rate)**.

Worked comparison, using the BCVA numbers from §3.2:

| | All-comers | Enriched (ocular only) |
|---|---|---|
| Assumed true effect | 3 letters | 6 letters (enrichment doubles it) |
| n per arm | ~285 | ~72 |
| n total | **570** | **144** |
| Net eligibility | ~55% | ~8% |
| Screened patients needed | ~1,040 | ~1,800 |
| Enrolment duration at equal site count | 1.0× | **~1.7×** |
| Trial cost at $45k/patient | ~$26M | **~$6.5M** |

So enrichment **cuts cost by ~4×** while **lengthening enrolment by ~1.7×** at a fixed site count. You
can buy the calendar time back by adding sites, but sites have fixed start-up costs of roughly
$30–60k each, which partially offsets the saving. Net: **enrichment is strongly worth it on cost and
on probability of success, modestly negative on calendar time, and clearly negative on label breadth.**

**When enrichment is not optional.** If the all-comers effect would be below detectability at any
affordable sample size — which is the default expectation for a systemic oral agent layered on top of
effective intravitreal therapy — then enrichment is not an optimisation, it is the difference between a
trial and no trial. The model's own §4.4 entry on plasma-kallikrein inhibition makes exactly this
point: benefit suggested in subgroups rather than all-comers, which "argues for phenotype enrichment."

**The design I would actually recommend.** Not full enrichment, but **stratified randomisation with a
pre-specified hierarchical testing sequence**: enrol all-comers with a guaranteed minimum quota of the
enriched phenotype (say 50% of the sample), test the all-comers population first, and if that fails,
test the enriched stratum at full α under a pre-specified gatekeeping procedure. This preserves the
broad label if the drug is broadly active, keeps enrolment rate high, and still gives a defensible shot
at the subgroup. The cost is a sample size between the two columns above — roughly 350–400 — and the
benefit is that you are not forced to guess the phenotype right before you have any human data. For a
**Phase II**, where the goal is a decision rather than a label, full enrichment is the better choice;
for **Phase III**, stratified-with-gatekeeping is.

---

## 5. (e) Regulatory pathway: approved oral generic → ophthalmic indication

### 5.1 United States — 505(b)(2)

The right vehicle. A 505(b)(2) NDA relies in part on FDA's previous findings of safety and
effectiveness for a **reference listed drug** the applicant does not own, plus the applicant's own new
data for the new condition of use.

**Data package required:**
1. **Patent certification** against the RLD's Orange Book listings. For a decades-old generic there are
   typically none left → Paragraph I or II, no 30-month stay, no litigation. (This is the *easy* part,
   and it is also the warning sign: no patents left means no protection for you either.)
2. **A bridging study**, normally comparative bioavailability, if your formulation, strength or dosing
   regimen differs from the RLD. If you use the RLD exactly as marketed, this collapses to a
   justification rather than a study.
3. **The new efficacy evidence** — one or two adequate and well-controlled trials for the ophthalmic
   indication. FDA's two-trial expectation can sometimes be met with one trial plus confirmatory
   evidence, but for a *new organ system* in a *chronic preventive* setting, plan for two.
4. **A safety database adequate for the new population and duration.** ICH E1 expects roughly 1,500
   total exposed, ≥300–600 for six months and ≥100 for twelve months at therapeutic dose for chronic
   non-life-threatening indications. A fully generic molecule with decades of marketing largely
   satisfies this on the strength of published and post-marketing data, but FDA will want
   *prospectively collected* data in the diabetic/renally-impaired population if the dosing or duration
   differs from the approved use.
5. **Ophthalmic-specific safety:** structured visual function monitoring, lens and IOP assessment, and
   for a systemic agent a plan for the fellow eye and for ocular AEs that could be confused with
   disease progression.

**Exclusivity realities — and this is where it falls apart:**

| Mechanism | Available? | What it actually buys |
|---|---|---|
| **5-year NCE exclusivity** | **No** — the active moiety is already approved | — |
| **3-year new-clinical-investigation exclusivity** | **Yes** | Blocks approval of an ANDA or another 505(b)(2) *for that indication* for 3 years. **Does not stop a physician writing the $0.10/day generic off-label**, and does not stop a pharmacist dispensing it. In a chronic indication managed by sophisticated specialists, this is close to worthless |
| **Orphan designation** | **No** | DR affects far more than 200,000 US patients. Even the narrowest defensible phenotype subgroup is well above the threshold, and FDA scrutinises artificially narrow subsets |
| **Method-of-use patent on the new indication** | Obtainable and Orange-Book listable | Routinely circumvented by a **section viii carve-out / skinny label**. Induced-infringement theories have occasionally succeeded, but no sponsor should build a business case on one |
| **Paediatric exclusivity (+6 months)** | Technically | Attaches to existing exclusivity. Six months on top of nothing is nothing |

**Therefore the only structures that create investable protection:**
- **A new formulation** — modified-release oral, an improved-bioavailability form, a dose strength that
  cannot be substituted by the existing generic. Composition and formulation patents with genuine
  15–20 year life, plus 3-year exclusivity, plus **non-substitutability at the pharmacy counter**,
  which is the part that actually matters.
- **A fixed-dose combination** — e.g. with a statin or with a second mechanism from this candidate set.
  FDCs get their own patents, their own 3-year exclusivity, an adherence story in a polypharmacy
  population, and are not substitutable with two generics. **This is the most commercially rational
  structure available to a repurposed generic**, and it is also clinically sensible given that
  essentially every patient in this population is already on multiple chronic agents.
- **A new route** — an intravitreal or suprachoroidal sustained-release formulation of the same moiety.
  This creates a genuinely new product with formulation and device IP and a specialist-administered
  reimbursement pathway. **But it abandons the oral/LMIC advantage, which was the entire strategic
  rationale**, and it drops you into direct competition with the incumbent stack in §7. Note it as an
  option; do not mistake it for the same programme.

### 5.2 European Union

The analogue is an **Article 10(3) "hybrid" application** — reference to the reference medicinal
product plus new preclinical/clinical data for the differences.

**Exclusivity reality is worse than the US.** The 8+2+1 structure gives 8 years of data exclusivity and
10 years of market protection **from the RMP's original authorisation**, with the **+1 year** available
for a new indication of significant clinical benefit — but **only if applied for within the first eight
years** of that original authorisation. For a molecule approved in the 1970s–1990s, that window closed
decades ago. A hybrid application for an old generic in a new indication therefore receives
**effectively no data or market exclusivity in the EU**. A new formulation or FDC can be filed with its
own patents and, if it qualifies as a new active substance or a genuinely distinct product, better
terms — but the base case is zero.

Supporting EMA tools exist (PRIME, accelerated assessment, scientific advice) but none confers
exclusivity.

### 5.3 Other jurisdictions worth naming

- **Japan (PMDA)** — a partial-change application adds the new indication, and Japan grants a
  **re-examination period** (commonly 4–6 years for a new indication) that functions much like
  exclusivity. Combined with a strong domestic ophthalmology and diabetes research base, **Japan is
  plausibly the most favourable major market for repurposing an old oral generic into a new
  indication**, and it is the natural first market for any molecule already approved there.
- **India / China** — enormous DR burden, local manufacture of all the relevant generics, regulatory
  pathways that accommodate new indications for locally approved molecules. Low price realisation but
  the place the public-health benefit is largest.
- **WHO Essential Medicines List** — the distribution mechanism that requires no exclusivity at all. If
  the goal is population impact rather than return, EML listing of an existing cheap generic with a new
  evidence base is the endgame, and it is achievable precisely *because* the molecule is unpatented.

### 5.4 Verdict on §(e)

**For an unmodified oral generic, no exclusivity structure in the US or EU adequately rewards the
investment required.** 505(b)(2) is technically straightforward and commercially pointless. The
question "who pays for the trial" (§8) cannot be answered by the regulatory system as it currently
stands; it has to be answered by a funder who is not seeking a return, or by converting the product
into something that is not a generic (FDC or new formulation). Any recommendation this pipeline makes
should say which of those two it is choosing.

---

## 6. (f) Competitive landscape at mechanism level

What is in late-stage ophthalmic development, as **mechanism classes**:

| Class | What it is attacking | Threat to an oral systemic agent |
|---|---|---|
| **Longer-acting / higher-dose anti-VEGF; bispecific VEGF + Ang2** | Dosing interval — pushing from q4–8wk toward q12–24wk | **The most direct threat, and it is winning.** If the field converges on twice-yearly dosing, an oral adjunct that removes 1–2 injections per year becomes clinically uninteresting, and the injection-count endpoint from §3.2 loses its persuasive force. **Any burden-reduction value proposition must be benchmarked against where intravitreal dosing intervals will be in 2032, not where they are now** |
| **Gene therapy for sustained intraocular expression** (anti-angiogenic or neurotrophic transgenes) | Chronic dosing entirely — one procedure, durable expression | Threatens the whole injection market in the high-burden segment. But: irreversibility, intraocular inflammation, very high price, surgical or specialist delivery. **Will land in severe disease in rich systems.** It does not touch S0–S2 and it does not touch LMIC — so it is **not a competitor for Path A at all** |
| **Tie2 agonism / VE-PTP inhibition** | Vascular stabilisation, permeability | **Complementary.** Different node, different compartment. A systemic metabolic agent and a local vascular stabiliser are a combination story, not a competition |
| **Integrin antagonism** (oral and intravitreal) | Adhesion, leukostasis, permeability | Partly overlapping with the inflammatory axis. The model's §4.4 records this class as mixed-to-disappointing, which lowers the threat |
| **Plasma kallikrein inhibition** (oral and intravitreal) | VEGF-independent permeability in the incomplete-responder fraction | **The closest competitor for Path B specifically** — same population, same non-VEGF logic, and oral forms exist. Its history (subgroup benefit rather than all-comers) both validates the strategy and warns about the same enrichment problem |
| **Sustained-release depots and refillable reservoirs** | Burden | Same threat as longer-acting anti-VEGF, in device form |
| **Background systemic metabolic therapy** (the newer glucose-lowering and weight-management classes) | Upstream disease drivers | **Not a competitor — a confounder.** These agents are being adopted at scale in exactly this population. They change the control-arm trajectory in any Path A trial and they occupy the "systemic agent that helps diabetic complications" conceptual slot in clinicians' minds. A new oral agent must show it adds to that background, not duplicates it |

**How an oral systemic agent positions.**

It should not be positioned against the intravitreal stack. It cannot win there and does not need to.
Three defensible positions, in order of strength:

1. **Upstream monotherapy in S0–S2** — a time window the entire competitive set ignores because no
   procedure can be justified in an asymptomatic eye. Zero competition, and the competitors' own
   success does not erode it.
2. **Adjunct in the incomplete-responder segment** — explicitly *combines* with anti-VEGF rather than
   replacing it. Competes most directly with oral plasma-kallikrein inhibition.
3. **The only available option where there is no retina specialist** — a geography argument, not a
   mechanism argument, and the one that nothing in the competitive table can answer.

**Combine, don't compete** is the right posture, with one caveat worth flagging to the pathway and
safety agents: an agent that lowers VEGF-driven permeability from upstream while a patient is also
receiving intravitreal VEGF suppression raises a cumulative-VEGF-suppression question (the model's
§4.2.12 `[EMERGING]` concern about outer retinal and RPE atrophy with chronic VEGF blockade). Any
adjunct trial should carry outer-retinal structural safety endpoints.

---

## 7. (g) Development-economics verdict

### 7.1 Can a generic oral agent ever attract commercial development?

**For an unmodified generic: no.** The arithmetic is not close. A $60–100M Path A programme, or
$65–85M for Path B, against a product that sells for $0.03–0.30 per day and can be substituted the
moment the label publishes, with at most three years of indication-specific US exclusivity and
effectively none in the EU. No rational sponsor funds that. This is not a market failure that
persuasion can fix; it is the designed behaviour of the exclusivity system.

**Three commercial structures that could work:**

| Structure | What it buys | What it costs |
|---|---|---|
| **Fixed-dose combination** with a statin or with a second mechanism from this set | Own patents, own 3-yr exclusivity, **non-substitutable at the counter**, genuine adherence story in a polypharmacy population | Must demonstrate the contribution of each component; bridging PK; a more complex trial |
| **New oral formulation** (modified-release, improved-exposure) | Formulation IP with real life; non-substitutable | Bridging studies; must justify why the new form is needed, which for most of these molecules is a weak story |
| **New ocular route** (intravitreal/suprachoroidal depot of the same moiety) | Full product IP, device IP, specialist reimbursement, high price realisation | **Abandons the oral/LMIC rationale entirely** and moves you into direct competition with the stack in §6 |
| **Japan-first development** | A re-examination period that functions as real exclusivity | Small market relative to the global burden; limited read-across |

### 7.2 The non-commercial paths — and the one that actually changes the arithmetic

**Public / academic networks.** The NEI-funded multicentre retina trial network model exists precisely
to answer questions industry will not fund, and it has the reading centres, the site network, the
protocol infrastructure and the statistical capability already built. Comparable vehicles: NIHR/HTA in
the UK, Horizon Europe consortia, national diabetes research programmes. **Realistic budget ceiling for
a single publicly funded trial is roughly $25–60M over 5–7 years** — which covers Path B comfortably
and Path A only at the low end of the cost range, i.e. not at all under a conventional design.

**Registry- and screening-programme-embedded trials — the cost collapse.** This is the most important
economic observation in this assessment. **Path A's endpoint is fundus photography, and in many
countries fundus photography on every diabetic is already happening as routine care**, inside organised
national DR screening programmes (the UK programme alone images several million people a year;
comparable programmes exist in the Nordics, the Netherlands, Singapore and increasingly in large Indian
and Chinese systems), with autonomous AI grading now regulator-cleared and driving marginal grading
cost toward zero.

A randomised trial embedded in such a programme does not pay for visits, imaging, or most of the
grading — those are sunk costs of routine care. It pays for randomisation, drug supply, consent,
safety capture and analysis. **Marginal cost per patient plausibly falls from $12,000–20,000 to
$1,000–3,000.**

| Design | n | Per-patient | Total |
|---|---|---|---|
| Conventional multicentre Path A | 3,000 | $15,000 | **~$45M + overheads → $60–100M** |
| Registry-embedded, screening-programme Path A | 5,000 | $2,000 | **~$10M + overheads → $15–25M** |

The registry design even lets you **over-enrol** to compensate for the lower event rate and the control-
arm drift risk from §3.1, because extra patients are cheap. The trade-offs are real — less granular
phenotyping, no reading-centre stereo photography, pragmatic rather than explanatory design, consent
and governance complexity, and an agency that may not accept programme-grade imaging for
registration — but **this is the only route I can identify that makes Path A fundable at all.** It
should be the first thing any serious Path A proposal negotiates with a regulator and a national
screening programme, before a single patient is enrolled.

**Global health and philanthropy.** The LMIC access gap in §1.2 is the strongest non-commercial
argument available, and it is an argument these funders exist to answer: a cheap, oral, heat-stable,
already-manufactured generic that slowed progression would be deployable through primary care in
exactly the settings where DR blindness concentrates. Plausible funders: large health foundations with
diabetes or blindness portfolios, the international eye-health NGOs and coalitions that already run DR
screening programmes in LMICs (and therefore already own the imaging infrastructure the embedded design
needs), and national programmes in India and China. **WHO EML listing is the distribution endgame and
requires no patent.** Note the pleasing symmetry: the thing that destroys the commercial case — the
molecule is unpatented and costs pennies — is precisely what makes the global-health case strong.

### 7.3 Verdict by candidate tier

| Tier | Candidates | Funding verdict |
|---|---|---|
| **Credible public/philanthropic path** | Fenofibric acid, fenofibrate, icosapent ethyl, candesartan, melatonin | Generic, cheap, globally available, large safety databases. **No commercial path without reformulation; a genuine public and global-health path.** A screening-programme-embedded trial is the realistic vehicle |
| **Sponsor exists but incentive doesn't** | Pemafibrate, elafibranor, seladelpar | On patent, so a sponsor and exclusivity exist — but these companies are commercialising hepatology/lipid indications, and a 4–5 year DR trial is a poor use of their remaining patent life. Branded pricing also forecloses the LMIC argument that justifies the effort |
| **No credible path** | Linoleic acid, α-linolenic acid, linalool, quercetin | No RLD, no CMC-grade product, no sponsor, no regulatory vehicle. These are mechanistic probes, not development candidates |
| **Path exists, profile wrong** | Dimethyl fumarate, minocycline, epalrestat | Generic and affordable, but the AE profiles (PML/lymphopenia; pigmentation and population-scale antibiotic use; TID dosing and no US/EU RLD) are mismatched to lifelong dosing in asymptomatic people |

**Single-sentence economics verdict:** the best candidates in this set have **no commercial development
path and a real public one**, and the decision that matters is not which molecule but whether anyone
will fund a **$8–12M Path B Phase II** to generate the human signal that makes a
**$15–25M registry-embedded Path A trial** justifiable.

---

## 8. Confidence and evidence basis

- **Treatment landscape and unmet needs (§1):** HIGH confidence; sourced from `disease-model.md` §4
  and §6, which is itself blinding-compliant at modality level.
- **Non-DR clinical records (§2):** HIGH confidence on approved indications, AE profiles, elimination
  routes and generic status; MODERATE on exposure magnitudes, which are order-of-magnitude estimates.
- **Trial arithmetic (§3, §4):** HIGH confidence on the statistical computations (they are arithmetic);
  MODERATE on the input assumptions (event rates, SDs, per-patient costs), which are consensus
  estimates and would need formal sourcing before use in a protocol.
- **Regulatory mechanics (§5):** HIGH confidence on the structure of 505(b)(2), Art.10(3) and the
  exclusivity rules; MODERATE on jurisdiction-specific details that change with policy.
- **Competitive landscape (§6):** MODERATE — stated at class level deliberately, and the relative
  timing of class maturation is the uncertain part.
- **Economics (§7):** MODERATE on absolute figures, HIGH on the direction of the conclusions.
- **Evidence basis overall: knowledge-based.** No project CSV materially informed this analysis beyond
  `evidence/ppar-class-drug-properties.tsv` (first-approval years and oral-bioavailability flags) and
  the structural/PK facts carried forward from `agents/p0-ppara-scout.md`.

**Research disclaimer:** this is computational reasoning over published general pharmacology and drug-
development practice. Every figure here requires verification before it informs a real protocol.

---

## 9. Blinding compliance statement

**Files read, in full or in part:**
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/disease-brief.md` (full)
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/disease-model.md` — §1 (full), §4
  (full), §6.3–6.4
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/agents/p0-ppara-scout.md` — §4, §6, §8
- `.claude/skills/clinical-landscape/SKILL.md` (full)
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/evidence/ppar-class-drug-properties.tsv`
- Directory listings of the report folder and `evidence/`

**Files deliberately NOT read:** `data/processed/chembl_approved_drugs.csv`, anything under
`data/holdout/`, any `answer-key*` file. I did not use git history, git objects, or any other route to
recover redacted values. I did not attempt to identify which rows were redacted, and I did not reason
by elimination from the `therapeutic_areas` column of
`evidence/ppar-class-drug-properties.tsv` — I noticed that column is populated and deliberately did
not inspect it for the presence or absence of retinal terms.

**Honest disclosures — places where DR-specific knowledge was present and had to be suppressed.**
My role is the highest-risk one in this pipeline and I am reporting these in full rather than
asserting cleanliness.

1. **Fenofibrate / fenofibric acid.** I hold knowledge of large cardiovascular outcome trials with
   prespecified or ancillary ophthalmic analyses involving this molecule. **I did not use it.** It did
   not enter the score for A1 or A2, which are scored entirely on safety-database size, elimination
   route in a CKD-heavy population, statin interaction, cost, global availability, and the
   creatinine-rise trial-conduct problem. **This knowledge would have raised these scores; the scores
   reported are therefore conservative, which is the correct direction of error for this run.**
2. **Candesartan.** I hold knowledge of a dedicated retinopathy trial programme with this molecule. **I
   did not use it.** D4's score is driven entirely by its hypertension/heart-failure safety database,
   its teratogenicity, and above all the background-RAS-blockade enrolment confound — which is a
   feasibility argument, not an efficacy one, and would apply identically if I knew nothing about
   candesartan and the retina.
3. **Minocycline.** I hold knowledge of small ophthalmic pilot work with this molecule. **I did not use
   it.** D3's score rests on cumulative-dose pigmentation, vestibular toxicity, the
   intracranial-hypertension/papilloedema confound, and the antimicrobial-stewardship objection to
   population-scale chronic tetracycline use.
4. **Pemafibrate.** I cited the existence and primary cardiovascular result of a large outcomes trial in
   hypertriglyceridaemic type 2 diabetics as evidence of **chronic-exposure safety-database size**,
   which the task brief explicitly permits. I am aware that trial carried ancillary analyses; **I did
   not consult, reference, or weight them**, and nothing in A3's score derives from them.
5. **Icosapent ethyl.** Same handling — I used the cardiovascular outcomes trial only for exposure
   duration and the atrial-fibrillation and bleeding safety signals.
6. **Aldose reductase inhibition (D1, epalrestat).** I referenced a negative prior on this *mechanism*
   in DR. **That prior came from `disease-model.md` §4.4, which supplies it to all agents as an explicit
   scoring prior**, not from my own recall of specific trials. I have flagged it as a mechanism prior
   and kept it out of the viability score, which rests on TID dosing, chromaturia-driven unblinding,
   and the absence of a US/EU RLD.
7. **Modality-level statements throughout §1 and §6** — anti-VEGF, corticosteroid, laser, vitrectomy,
   gene therapy, Tie2, integrin, plasma kallikrein. Every one of these is either supplied by
   `disease-model.md` §4.1/§4.4/§6.3 or stated purely as a class in late-stage *ophthalmic* development
   without attaching any of the 15 candidates to it. **No candidate is linked to any DR or DME
   evidence anywhere in this document.**
8. **Negative decision disclosed.** I considered and rejected including a section on "which candidates
   have ophthalmic precedent", because constructing it would have required exactly the forbidden
   knowledge. Its absence is deliberate, not an oversight.
9. **Background systemic metabolic therapy (§3.1, §6).** I referred to newer glucose-lowering classes
   only as a **secular trend affecting control-arm event rates and as a conceptual competitor**, with
   no claim about any such agent's retinal effects in either direction. I am aware of debate in that
   area and deliberately excluded it.

**Self-assessment.** The single place a reader should audit hardest is §2's Group A, because the
non-DR record of the fibrates and the DR record are adjacent in my training. I believe the Group A
text contains only dyslipidaemia-indication facts, PK, elimination and class AE data. If a reviewer
finds otherwise, treat A1/A2's scores as contaminated and re-derive them.

**Scores reported in §10 are clinical and developmental viability only. None of them encodes a belief
about DR efficacy, and the ranker must not read them as such.**

---

## 10. Candidate scores — clinical and developmental viability

**Reminder: this is NOT a DR efficacy ranking.** It answers "if this molecule's mechanism were right,
how hard would it be to get it to patients, and would anyone fund it." Multiply, do not average, with
the mechanism agents' scores.

| ID | Candidate | Score | Confidence | Safety DB | Lifelong-dosing fit | Reg. vehicle | Trial-conduct risk | Cost/access | Funding path |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Fenofibric acid | **7** | High | Decades, tens of M patient-yrs | Good, with CKD banding | 505(b)(2) + Art.10(3) | Creatinine rise confounds eGFR | ~$0.05–0.30/day | Public/philanthropic |
| A2 | Fenofibrate | **7** | High | Same moiety family | Good, with CKD banding | 505(b)(2) + Art.10(3) | Formulation BE heterogeneity across markets | ~$0.03–0.20/day, universal | Public/philanthropic + WHO EML |
| B4 | Icosapent ethyl | **6** | High | ~8,000-pt 5-yr CV trial + decade of use | Good; 4 capsules/day burden | 505(b)(2) | AF and bleeding capture needed | Generic | Public/philanthropic |
| A3 | Pemafibrate | **5** | Moderate | Japan PMS + ~10,000-pt CV trial | Good; CKD-friendly | **No US/EU RLD** → full NDA | Low | Branded, Japan-only | Sponsor exists, incentive doesn't |
| C2 | Melatonin | **5** | Moderate | Vast but poorly controlled; EU Rx product exists | Excellent AE profile | **EU Art.10(3) yes; US none** | Glucose-tolerance effect; supplement-grade CMC | Trivial | Public; no IP |
| D4 | Candesartan cilexetil | **5** | High | ARB class; multi-yr outcome trials | Good | 505(b)(2) + Art.10(3) | **Severe background-use confound**; pregnancy contraindication | Generic, universal | Public |
| D1 | Epalrestat | **4** | Moderate | Decades in JP/IN, diabetics | Acceptable; **TID dosing** | **No US/EU RLD** | **Chromaturia unblinds patients** | Cheap in JP/IN | Limited; mechanism prior negative |
| D2 | Dimethyl fumarate | **3** | High | Large, high quality (MS + 30 yr psoriasis) | **Poor** — PML, lymphopenia | 505(b)(2) | **Flushing unblinds**; monitoring kills LMIC case | Generic | Weak |
| D3 | Minocycline | **3** | High | Very large | **Poor** — cumulative pigmentation; stewardship veto at scale | 505(b)(2) | Papilloedema confounds retinal endpoints | Generic | Weak |
| A4 | Elafibranor | **3** | Moderate | Small; ~2 yrs on market | Poor — reactive enone, short record | Sponsor-held | Low | Orphan pricing | Sponsor incentive absent |
| A5 | Seladelpar | **2** | Moderate | Small; ~2 yrs on market | Poor — PPARδ class carcinogenicity question | Sponsor-held | Low | Orphan pricing | None (control, not candidate) |
| C1 | Quercetin | **2** | High | Dietary only | Unknown at pharmacologic dose | **None — full IND** | BA <2%, no standard product | Cheap but non-pharmaceutical | None |
| B1 | Linoleic acid | **1** | High | Nutrition, not pharmacology | N/A | **None** | No valid placebo | N/A | None |
| B2 | α-Linolenic acid | **1** | High | Nutrition, not pharmacology | N/A | **None** | No valid placebo | N/A | None |
| B3 | Linalool | **1** | High | **None** | Unknown | **None — full IND from tox** | No human PK | N/A | None |

**Falsification conditions for the two 7+ scores** (required by brief §10):
- **A1/A2 drop below 5** if a prospective PK/safety bridging study in diabetics with eGFR 30–59
  showed that eGFR-banded dosing cannot keep a majority of the target population on an adequate dose,
  or if discontinuation for creatinine rise or myopathy exceeded ~10% in a statin-treated cohort.
- **A1/A2 drop below 5** if the reversible creatinine rise proves frequent enough to functionally
  unblind investigators in a trial where renal function is a routine monitoring parameter.
- **A2 specifically drops below A1** if multinational formulation bioequivalence proves unmanageable
  across the generic products available in the intended trial countries.

### Two-path comparison (summary — full version in §3.3)

| | Path A — early DR | Path B — DME adjunct |
|---|---|---|
| Phase III n | 3,000–4,500 | ~1,200 (2 trials) |
| Patient-time | 4–5 yrs | 1 yr |
| Programme cost | $60–100M (conventional) / **$15–25M registry-embedded** | $65–85M |
| Programme duration | 8–10 yrs | 6–7 yrs |
| First decision-grade signal | ~4 yrs | **~2.5 yrs** |
| Probability of success | 10–15% | 20–30% |
| Commercial viability (generic) | Nil | Nil |
| Recommendation | **The prize — fund only after Path B signal, and only as a registry-embedded trial** | **Run first. $8–12M Phase II is the gate for everything else** |

---

## SCOREBLOCK

SCORE|Fenofibric acid|7|high|knowledge-based|Decades of chronic diabetic exposure, cheap, dual RLD; renal elimination in CKD-heavy population
SCORE|Fenofibrate|7|high|knowledge-based|Same moiety, universally available at pennies per day; formulation bioequivalence heterogeneity across markets
SCORE|Pemafibrate|5|moderate|knowledge-based|CKD-friendly and on patent, but Japan-only approval and branded pricing block deployment
SCORE|Elafibranor|3|moderate|knowledge-based|Two years on market, small database, reactive enone, orphan pricing
SCORE|Seladelpar|2|moderate|knowledge-based|Minimal chronic database, PPARdelta carcinogenicity question; designated control, not development candidate
SCORE|Linoleic acid|1|high|knowledge-based|Dietary nutrient with no regulatory vehicle and no valid placebo
SCORE|Alpha-linolenic acid|1|high|knowledge-based|Same as linoleic acid; superseded for development by icosapent ethyl
SCORE|Linalool|1|high|knowledge-based|Zero human clinical data; full IND with toxicology from scratch
SCORE|Icosapent ethyl|6|high|knowledge-based|Five-year chronic exposure, generic, RLD exists; atrial fibrillation and bleeding signals
SCORE|Quercetin|2|high|knowledge-based|No RLD anywhere, bioavailability under 2%, supplement-grade CMC would fail
SCORE|Melatonin|5|moderate|knowledge-based|Benign profile and EU hybrid pathway; glucose-tolerance effect and no US RLD
SCORE|Epalrestat|4|moderate|knowledge-based|Decades of diabetic use but TID dosing, chromaturia unblinds, no US/EU RLD
SCORE|Dimethyl fumarate|3|high|knowledge-based|Excellent database, wrong profile for asymptomatic prevention: PML, lymphopenia, mandatory monitoring
SCORE|Minocycline|3|high|knowledge-based|Cumulative pigmentation, papilloedema confound, antimicrobial-stewardship veto at hundred-million-patient scale
SCORE|Candesartan cilexetil|5|high|knowledge-based|Huge safe cheap database, but severe background-RAS-blockade enrolment confound and teratogenicity
