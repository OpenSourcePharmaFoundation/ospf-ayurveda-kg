# PPARα as a Therapeutic Target in Diabetic Retinopathy
## A blinded computational analysis, its result, and the experiments that would settle it

**Analysis date** 2026-10-05 · **Method** 16-agent multi-agent pipeline, dataset-blinded
**Scope** Treatments for diabetic retinopathy, with specific focus on PPARα (gene *PPARA*)

---

## ABSTRACT

A sixteen-agent reasoning pipeline was run against a biomedical dataset from which every
diabetic retinopathy (DR) indication had been redacted, in order to (i) evaluate PPARα as a
therapeutic target for DR and (ii) measure whether mechanism-based reasoning alone recovers
known therapy.

The pipeline nominated the **fibrate / PPARα-agonist class**, ranking **fenofibric acid
first**, and independently derived that the treatable window is **mild-to-moderate
non-proliferative disease rather than the preclinical window** it had been instructed to
prioritise. Both conclusions are correct against the withheld evidence.

Its **mechanistic** conclusion was wrong in an instructive way. The pipeline converged on
systemic lipoprotein lowering; the clinical evidence most clearly excludes that limb. The
error is traceable to a structural bias in evidence grading rather than to faulty reasoning,
and that bias will recur for any target in a compartment that cannot be sampled.

**One measurement stands between this target and a decision and has never been made in any
species: free drug concentration in retinal tissue.** Every quantitative claim in this
analysis rests on estimated partition ratios. The experimental programme in §6 is organised
around obtaining that number and three others, for roughly $400–550k over 12–18 months.

---

## 1. THE SCIENTIFIC QUESTION

PPARα is a ligand-activated nuclear receptor governing fatty-acid catabolism. It is expressed
in retinal pigment epithelium, Müller glia and retinal vascular endothelium, and its retinal
expression is reported to *decrease* in diabetes — the classic configuration for an agonist to
restore a deficit rather than supraphysiologically stimulate a pathway.

The retina is the most metabolically active and most lipid-dense tissue per gram in the body.
Photoreceptor outer segments are shed and phagocytosed daily by the RPE, which oxidises those
lipids through fatty-acid β-oxidation as a genuine energy source. **The receptor is present
and the pathway it controls is one the tissue actually runs** — a better starting position
than most repurposing hypotheses.

### 1.1 Why the lipid axis is under-served

Hard exudates in DR are **not "fat."** They are retained, glycated-and-oxidised apoB
lipoproteins deposited in Henle's layer, and that modified species is directly cytotoxic to
pericytes, endothelium, Müller cells and RPE through endoplasmic-reticulum stress.

This resolves a standing paradox: plasma LDL cholesterol tracks DR poorly, while apoB particle
number and remnant particles track it well. **If the toxic agent is the modified particle
rather than cholesterol load, the relevant intervention lowers remnant supply, not LDL.**

No current therapy clears hard exudate, and subfoveal lipid causes permanent vision loss even
in anatomically dried eyes. The lipid axis is the mechanistically neglected module of this
disease.

### 1.2 The question is not whether, but which limb

PPARα agonism could act on DR through four mechanistically distinct routes. **They imply
different molecules, different disease stages and different experiments**, and the analysis
turns entirely on which is operative.

| | Limb | Drug acts at | Effect appears at | Engagement | Crosses the barrier? |
|---|---|---|---|---|---|
| **1** | Lipoprotein supply | Hepatocyte | Plasma composition → retina | **Certain** | No |
| **2** | Humoral relay | Hepatocyte | FGF21 → retinal endothelium, luminal side | Certain upstream | No |
| **3** | Local transrepression | Retinal endothelium / RPE | NF-κB → ICAM-1 → leukostasis | **Marginal** | One membrane, not the barrier |
| **4** | Local transactivation | Neural retina | PPRE-driven fatty-acid-oxidation genes | **Absent** | Yes — unreachable |

---

## 2. METHOD

### 2.1 The pipeline

Sixteen agents across five phases: disease modelling and candidate scouting; six parallel
domain analyses (chemistry, pharmacokinetics, target biology, disease staging, clinical
landscape, traditional medicine); five deep dives (pathway, safety, repurposing, structure-
activity, literature); an adversarial debate round; and final ranking, feasibility and
combination design. Roughly 17,000 lines of analysis.

Each agent received the same disease model and scored on an explicitly different axis. **Scores
were never averaged across axes** — a weighted mean over orthogonal dimensions was identified
by five separate agents as the pipeline's central methodological risk, and the final ranking
uses lexicographic gates with efficacy evidence as the dominant anchor.

### 2.2 The blind

Every DR indication was redacted from the working dataset: 154 cells across 79 drugs, verified
to zero residual matches. The source data was never modified — the pipeline read a parallel
redacted copy. Agents were additionally instructed to reason from mechanism and never cite
indication status as evidence.

**The blind was imperfect and degraded across phases**, which is reported in §7.4 rather than
minimised.

### 2.3 What the underlying data could not support

| Needed | Available |
|---|---|
| Drug–target binding affinity | **None.** Mechanism and target tables are near-empty test extracts with zero PPAR content |
| Measured pharmacokinetics | **None.** Distribution, permeability and bioavailability fields empty across all 3,276 drug records |
| Gene–disease associations for DR | **None.** Only a legacy oral-mucositis set |
| PPARα effector genes in the target panel | **None.** All three receptors present; not one downstream gene |

**The pathway under study was invisible to the data used to study it.** Every quantitative
claim below is reasoning from pharmacology, explicitly labelled as such throughout the
underlying reports.

---

## 3. RESULT — CANDIDATE RANKING

**Read as a ranking of experimental priority, not of assets.** Several entries are
deliberately *instruments* — probes that measure whether a mechanism operates, and control
arms that make a result interpretable. A poor chronic drug can be the best available probe.

| # | Compound | Score | Role | Basis |
|---|---|---|---|---|
| **1** | **Fenofibric acid** | 6.5 | **Lead** | Certain hepatic engagement; the only fibrate lowering apoB particle number; best drug-likeness in class |
| 2 | Pemafibrate | 6.0 | Lead alternate | Sub-nanomolar, >2000× isoform-selective, best renal safety — but its distinguishing remnant claim has an unfavourable hard-endpoint read |
| 3 | Fenofibrate | 5.5 | Prodrug of #1 | Adds an esterase step and a food effect without adding pharmacology |
| 4 | Elafibranor | 5.5 | **Probe (12 wk)** | The only compound plausibly reaching free EC₅₀ at retinal endothelium |
| 5 | Olezarsen | 5.0 | **Control** | Matched non-PPAR apoC-III suppression — the decisive discriminating arm |
| 6 | Inclisiran | 5.0 | **Falsification arm** | 3–5× the apoB effect of any fibrate; if apoB mass is the mechanism, it should work better |
| 7 | Candesartan | 5.0 | Comparator | Engagement certain at a luminal target; blocked by background therapy |
| 8 | Seladelpar | 4.5 | **Isoform control** | Exceeds free EC₅₀ in the target compartment; confounded as a falsifier |

**Bottom of the field:** quercetin (1.0), minocycline (1.5 — its papilloedema risk attacks the
very endpoint being measured), epalrestat (2.0 — excellent engagement of a *falsified* target),
and the dietary fatty acids (2.0–2.5, **not dose-movable**: plasma concentrations already sit
at their own EC₅₀).

### 3.1 The natural products collapsed, and that validated the controls

Quercetin finished last with the tightest agreement of any compound in the matrix. It had been
**first** in the raw target-coverage data, hitting 26 of 27 disease genes.

The traditional-medicine agent ran the null model nobody else had: **a random set of 20
compounds covers ≥26 of those 27 genes with probability 0.58.** Catalogue size correlates with
hit count at r = 0.911. Ascorbic acid alone covers 23. **The ranking measured how heavily a
compound had been studied, not what it does.** Its PPARα records also proved to be
"compound X blunts an insult-induced fall in expression" — not target engagement — and
quercetin actually *antagonises* a reference agonist, making its direction incoherent.

Sugars appeared as high-scoring "compounds" because they are experimental perturbagens. The
agent flagged that if one surfaced in the ranking, that was a bug.

---

## 4. RESULT — STAGING

**The analysis corrected its own instructions.** The brief named disease-modifying therapy for
*preclinical* disease as the top unmet need. The disease-biology agent rejected that half on
mechanistic grounds:

> The exposure-robust limb — lowering systemic lipoprotein supply — is **mechanically
> inoperative** before the barrier leaks. With an intact blood-retinal barrier there is no
> extravasation to prevent.

The right-stage limb (local fatty-acid-oxidation control in early disease) is precisely the
limb the exposure arithmetic most undermines. **The best-exposed mechanism acts at the wrong
stage; the right-stage mechanism has the worst exposure case.** The honest target is
mild-to-moderate non-proliferative disease.

### 4.1 Enrichment is harder than it looks

The obvious enrichment marker — existing hard exudate — **selects patients in whom a
supply-lowering mechanism is weakest**, because an established deposit is self-renewing and
clearance-limited. The marker that finds the lipid phenotype also finds patients past the
point where the mechanism acts.

Enrich on the **rate**, not the deposit: elevated remnants despite statin therapy, and new or
worsening lesions over a prior interval, excluding organised subfoveal plaque.

---

## 5. RESULT — MECHANISM

### 5.1 Local transactivation is excluded on arithmetic

The free-drug partition ratio cannot exceed 1. Even complete barrier failure leaves fenofibric
acid 10–100× below its free EC₅₀ in neural retina. **It does not arrive late; it never arrives.**

### 5.2 Compartment matters more than the barrier

The decisive correction of the run. PPARα in **retinal vascular endothelium sits on the blood
side** of the inner barrier, and PPARα in the **RPE faces fenestrated choriocapillaris.**
Neither requires crossing the barrier — only one plasma membrane. Estimated partition is
roughly tenfold better in those compartments than in neural retina, **and those are exactly
where the leukostasis and lipid-handling mechanisms live.**

### 5.3 Potency does not buy engagement

Pemafibrate is ~5 orders of magnitude more potent than fenofibric acid and circulates at ~4
orders lower free concentration. Its real margin is about **one** order better, not five.
Any ranking treating sub-nanomolar potency as decisive mis-ranks the set.

### 5.4 The wrong-sign risk is structurally bounded

ANGPTL4 — a direct PPARα target gene and a potent pro-permeability factor in ischaemic retina
— was initially treated as a fatal liability. Three agents independently dismantled it:

- **The two objections are mutually destructive.** ANGPTL4 induction requires the *same*
  gene-activation machinery the exposure objection says is unavailable. If local engagement is
  too weak to help, it is too weak to harm.
- **A ceiling from already-measured data.** ANGPTL4 inhibits lipoprotein lipase, so meaningful
  induction predicts triglycerides to *rise*. Observed triglycerides *fall*. Real-world
  induction is bounded above by a quantity already in hand.
- **The surviving path is systemic, not local** — hepatic engagement is certain, so hepatic
  ANGPTL4 induction raising the *circulating* pool, acting on endothelium from the luminal
  side, is the exposure-weighted risk. **Plasma ANGPTL4 is therefore a mandatory, cheap
  biomarker.**

### 5.5 What survives, and the limb the pipeline under-weighted

The debate round rejected the framing that had organised the whole analysis:

> **"Not either/or — the dichotomy is itself the error. It assumes a drug affects a tissue
> only by entering it."**

Limbs 1 and 2 are **systemic in pharmacokinetics and retinal in pharmacology.** The liver is a
legitimate site of action *on* the retina. The FGF21 relay in particular requires no barrier
crossing at any point, is human-proven upstream, and is animal-proven downstream by
laboratories independent of the lineage producing the retinal-PPARα claims.

### 5.6 The structural question, and a reversal

The analysis initially concluded that PPARα **requires** an acidic head group, that the acid is
what albumin and hepatic uptake transporters recognise, and therefore that potency and tissue
access are anti-correlated by construction — making the local hypothesis permanently untestable.

**The structure-activity agent refuted this, blind.** The receptor's anchoring residues are all
hydrogen-bond *donors*, so the ligand need only supply acceptors in the correct geometry — a
bidentate pair ~2.2–3.2 Å apart, **not a formal charge.** Charge is an acceptor-strength
multiplier worth a bounded 2.3–3.1 kcal/mol.

Measured in **ligand efficiency** rather than raw potency, the neutral endogenous ligand
oleoylethanolamide (0.41) is a *more* atom-efficient binder than fenofibric acid (0.29) or
pemafibrate (0.34). **The neutral head pays no efficiency penalty.**

The chemical space is empty because every PPARα indication has been hepatic, and for a hepatic
target high protein binding and transporter uptake are *features*. **Nobody ever needed a
PPARα ligand with a high free fraction.** Unexplored, not forbidden.

### 5.7 The uncovered module

**All 29 candidates reduce what *arrives* in the retina. Not one accelerates what *leaves*.**

The lesion is a self-renewing cycle: modified lipoprotein → scavenger uptake → transporter
downregulated → cholesterol cannot leave → inflammasome activation and foam-cell death →
lipid re-released → re-uptake. **The deposit regenerates from its own debris.**

Solving it as a two-compartment system gives burden = influx ÷ clearance **exactly** — the
recycling term cancels. **But as clearance approaches zero the system has no steady state; it
integrates.** A supply-lowering agent then buys *delay*, not a bounded burden.

The fibrates do not secretly cover this. Transporter induction is gene-activation driven — the
same limb shown absent locally — and it is a two-step relay, so *more* sensitive to that
shortfall, not less.

> **You cannot perform retinal reverse cholesterol transport from the liver.**

**One structural opening:** the PPARα pocket mandates a lipophilic acid; the LXR pocket does
not — its ligands are neutral. A retina-penetrant modulator aimed at the *efflux* arm is
chemically conceivable in a way a retina-penetrant PPARα agonist is not. The caveat is severe:
systemic agonism of that target has repeatedly failed on hepatic steatosis and
hypertriglyceridaemia.

---

## 6. EXPERIMENTAL PROGRAMME

The analysis is at the limit of what mechanism-based reasoning can deliver. **The next
increment comes from measurement.**

### 6.1 The critical-path unknown

> **Free drug concentration in retinal tissue, and the receptor occupancy it implies.**

Never measured in any species. Three mutually exclusive programmes hang on it. The practical
route is **human aqueous humour from patients on chronic therapy at routine cataract surgery**
— not retinal interstitium, but it bounds the problem at negligible added risk. **Pair it with
aqueous ANGPTL4 in the same tap: two of three central unknowns from one draw.**

### 6.2 The experiment that decides whether a local target exists

**Chronic oral fibrate in a diabetic rodent, reading transactivation against transrepression.**

| Readout class | Markers |
|---|---|
| Transactivation (gene-activation driven) | retinal CPT1A, ACOX1, HMGCS2, **ANGPTL4** |
| Transrepression (PPRE-independent) | retinal ICAM1, TNF, IL6; adherent-leukocyte count |

| Result | Conclusion |
|---|---|
| Transrepression ↓, transactivation flat | **Confirms a pharmacokinetically dissociated ligand** — anti-inflammatory action without gene induction, and therefore without the wrong-sign limb |
| Transactivation robustly ↑ | Low-occupancy model wrong; ANGPTL4 risk live |
| Both flat | **No local target.** Every retina-penetrant chemistry effort is unjustified |

**Two arms without which this is cheap and *indecisive*:** a receptor-knockout arm (fenofibrate
has documented receptor-*independent* effects, and much supporting in vitro work uses
concentrations above where those appear, without knockout or antagonist controls); and a
**matched non-PPAR lipid-lowering arm** (without it, a positive cannot be distinguished from
"any lipid lowering would have done this").

### 6.3 The discriminator that needs no new experiment

**Does benefit track the lipid change?** A covariate analysis, answerable from data routinely
collected. **If benefit does not track the lipid change, the supply limb is in trouble and the
receptor hypothesis strengthens.** Costs nothing; discriminates directly.

### 6.4 The gap beneath the best-evidenced limb

The FGF21 relay rests on two findings never placed on the same axis — fibrates raise plasma
FGF21 (human), and FGF21 protects retinal vasculature (animal). **Nobody checked whether those
are the same concentration.** The downstream work uses pharmacological recombinant protein; a
fibrate produces a modest physiological rise.

This is the **third** instance in this analysis of a real effect demonstrated at a dose the
intervention cannot deliver — after herbal fatty acids and after endogenous ligands already at
their own EC₅₀. **It is the characteristic failure of mechanism-first reasoning and should be
tested for explicitly rather than rediscovered.**

### 6.5 The necessity experiment the field has never run

**Cell-type-restricted conditional *Ppara* deletion in retina.** The global knockout cannot
substitute — it carries hypertriglyceridaemia, abolished ketogenesis and FGF21, and hepatic
steatosis, so "worse retinopathy" is fully explained by the competing systemic hypothesis.
**Citing it for the local limb is circular.** After roughly fifteen years of interest in this
target, the conditional deletion's continued absence is itself informative.

### 6.6 Sequenced

| # | Experiment | Cost | Time | Decides |
|---|---|---|---|---|
| 1 | Lipid-change covariate analysis | ~$0 | weeks | Supply limb vs local limbs. **Free — run first** |
| 2 | Human aqueous drug + ANGPTL4 | $50–100k | 6–12 mo | The critical-path unknown; the wrong-sign question |
| 3 | Rodent transactivation vs transrepression, **with knockout and non-PPAR arms** | $150–250k | 6–9 mo | Whether a local target exists |
| 4 | FGF21 concentration bridge | ~$50k | 6 mo | Whether the best-evidenced limb closes |
| 5 | ApoA1-mimetic explant, **transporter silenced** | ~$75k | 6 mo | Whether the uncovered module is addressable |
| 6 | Lipid clearance rate constant | ~$75k | 6 mo | Whether benefit is bounded or merely delayed |
| 7 | Conditional retinal receptor deletion | $300–500k | 18–24 mo | **Necessity** |

**Items 1–6: ~$400–550k over 12–18 months**, collectively deciding which of three mutually
exclusive programmes to run.

### 6.7 Observation windows must be justified against clearance, not calendar

A **stock** readout (lesion burden) has time constant 1 ÷ clearance — the parameter this
disease suppresses. A **flux** readout (lesion turnover) responds directly. **A stock measure
can read flat at twelve months while the mechanism is working.** Flux primary; stock secondary
with a window justified against the measured clearance rate. *An earlier draft of this
programme used them interchangeably in a stop/go criterion, which would have terminated a true
positive.*

### 6.8 Kill criteria

- Rodent study flat on both readouts with confirmed systemic exposure → no local target
- Matched non-PPAR lipid arm reproduces the effect → the receptor is not the agent of action
- Receptor knockout fails to abolish the effect → not receptor-mediated
- Benefit tracks lipid change tightly → a lipoprotein hypothesis; far more potent apoB-lowering
  agents exist than any fibrate
- Robust local transactivation with ANGPTL4 induction → wrong-sign limb live; re-derive
  risk-benefit by stage before any chronic exposure

### 6.9 Combination work is deferred, with reasons

The four-limb question determines which component a combination needs, so building one first
yields an uninterpretable result. **Two bench measurements replace it (~$100–150k):** the
extracellular-removal term in a transporter-silenced explant, and the clearance rate constant.

The strongest combination concept is oral supply-lowering plus a **locally delivered ApoA1-
mimetic acceptor** at an injection visit these patients already attend — for which the entire
barrier-penetration problem does not apply. Modelling shows a direct removal term keeps burden
finite **even at zero transporter activity**, whereas a transporter inducer multiplies a term
that may already be near zero. **The right partner is an acceptor, not a transporter inducer.**

**Ruled out:** any supply agent plus scavenger-receptor blockade is **wrong-signed** —
macrophage uptake is the only catabolic route for retained lipoprotein in retina, so blocking
it converts dying foam cells into extracellular deposits nothing removes.

---

## 7. BENCHMARK — DID BLIND REASONING RECOVER KNOWN THERAPY?

### 7.1 The withheld answer

Fenofibrate is an approved DR therapy in Australia (2013) — labelled for patients with
***existing*** retinopathy — and appears in current ADA guidance, qualified to **early**
retinopathy. Four randomised datasets support it; one follow-on shows the benefit **does not
persist after discontinuation.**

### 7.2 Scorecard

| Question | Verdict |
|---|---|
| Right compound? | **Yes.** Fenofibric acid / fenofibrate at the top of the blinded ranking |
| Right stage? | **Yes, emphatically.** Corrected its own brief on mechanistic grounds, matching the label wording and the pivotal subgroup |
| Right phenotype? | **Partially.** The exudative phenotype and incident-oedema endpoint corroborated; a lipid-level entry gate contradicted |
| **Right mechanism?** | **No.** Converged on systemic lipid lowering, which the evidence most clearly excludes |

**Round 1 metrics (the cleanly blinded phase): P@1 = 1.00, first correct hit at rank 1.**

### 7.3 The mechanism error, and why it generalises

Benefit does not track lipid change; it appears on top of a statin; and in one trial's
renal-impairment subgroup, dosing that produced **no lipid change at all** still produced
ocular benefit.

The diagnosis is structural, not a lapse:

> **Evidence-hierarchy grading systematically rewards the limb whose intermediate steps are
> easiest to measure.** Plasma markers are measurable, so that chain accumulates high-level
> citations. Retinal drug concentration and receptor occupancy are not, so that chain can only
> ever accumulate low-level citations **no matter how true it is.** The hierarchy measured
> *tractability of measurement* and reported it as *strength of evidence*.

**This will recur for any target behind a barrier** — brain, eye, testis, placenta. **The fix:**
normalise each limb against the best evidence level it could *possibly* attain given current
measurement technology, and report raw and normalised grades together.

**Precision about what this falsifies.** The analysis never concluded the drug would fail. It
concluded *local receptor engagement is not why*. That narrower claim remains partly live — the
literature itself reports effects on human retinal endothelial cells that are
receptor-*independent*. The true answer appears to be an intraocular effect that is neither
lipid-mediated nor cleanly receptor-mediated — **a third option no agent enumerated until the
debate round.**

### 7.4 Limits of this benchmark, stated plainly

**It did not measure naive rediscovery.** Dataset blinding removes a data signal; it cannot
remove pretrained knowledge. One agent disclosed it could not fully exclude that knowing an
outcome nudged a grade, and declined to artificially deflate it — correctly, since a deliberate
downward correction is equally contaminated.

**The blind degraded across phases, through three leaks of the same class, each created by the
fix for the last:** redaction markers that identified scrubbed rows without naming them; an
in-file section boundary defeated by a heading search; and finally an incident report that
described what the previous leak had exposed, in a file later agents were required to read.

**Phase 0 and Round 1 are the clean measurement. Phase 3 was not cleanly blinded.** Benchmark
claims are scoped to the phase that produced them.

**Five errors were the orchestrator's**, not the agents'. The most consequential reported a
pharmacokinetic *term* as if it were the full *product*, producing a confident headline
conclusion — that no drug in this class could probe the local mechanism — which the run's own
data contradicted, and which misdirected an entire downstream assignment. It is retracted in
the record.

> **The highest-yield attack surface in a multi-agent pipeline is not any agent's reasoning —
> it is the synthesis layer, where ranges collapse into point estimates.** Every agent reported
> ranges with uncertainty bounds and provenance tags; the synthesis stripped them.

---

## 8. CONCLUSIONS

1. **The fibrate class is the correct nomination**, recovered from receptor pharmacology with
   the answer removed from the data, and the staging restriction was derived rather than
   inherited.

2. **The mechanism is unresolved and the candidate limbs are distinguishable by cheap
   experiment.** The supply limb has certain engagement and disconfirming clinical evidence;
   the humoral relay has the best evidence and an unexamined concentration gap; the local limb
   is marginal and untested.

3. **Potency is nearly orthogonal to engagement in this chemical series**, so the apparent
   ordering of candidates by receptor affinity is misleading, and the most potent agent is not
   the best probe.

4. **The acid head is conventional, not mechanistic.** A neutral, retina-accessible ligand is
   designable. It should not be built until the rodent experiment reads positive.

5. **The efflux arm is the largest uncovered module**, it cannot be addressed from the liver,
   and the right partner is an extracellular acceptor rather than a transporter inducer.

6. **Confidence is low-to-moderate and lower than the volume of analysis suggests.** The
   project contributed no binding affinity, no measured pharmacokinetics, and no
   gene-disease data; the quantitative content is reasoning, not measurement.

> **One rodent study and one aqueous humour sample would contribute more than the sixteen
> agents that produced this report.**

---

## APPENDIX — SUPPORTING DOCUMENTS

All under `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/`.

| Document | Contents |
|---|---|
| `research-program.md` | The experimental agenda in full, with interpretation of every outcome |
| `BENCHMARK-RESULT.md` | Rediscovery scoring, mechanism post-mortem, phase-scoped validity |
| `data-quality-findings.md` | 22 defects, including the five orchestrator errors |
| `disease-model.md` | DR pathobiology — stages, nine pathway modules, compartments (1,555 lines) |
| `round1-synthesis.md`, `round2-synthesis.md`, `debate-summary.md` | Phase syntheses with retractions shown in place |
| `agents/` | 18 raw agent reports |
| `blinding-protocol.md` | Redaction method and verification |
| `scoring/` | Predictions and scores |

⚠ **`agents/UNBLINDING-part-b.md` contains the held-out answer.** Do not read it, or expose it
to any agent, when re-running this benchmark.

**Reproduce:**
```bash
python src/holdout/blind_dataset.py --disease diabetic-retinopathy
python src/holdout/score_run.py --disease diabetic-retinopathy \
    --predictions <run>/scoring/predictions-final.json
```

**Research disclaimer.** This is a computational multi-agent analysis. Nothing here is a
clinical recommendation. All findings require experimental validation.
