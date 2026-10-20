# P3 — Combination Design: Diabetic Retinopathy (BLINDED RUN)
## Combination Designer · 2026-10-19 · the agent the run skipped

**Standing.** This agent's slot was lost to a fork limit and the run shipped with the
combination question formally unanswered (`consensus-report.md`, PIPELINE CONFIGURATION).
This report closes that gap. It builds on the completed record rather than re-deriving it:
the Pathway Analyst's efflux analysis (`p2-pathway.md` §2–4, §7), the Integrator's four-limb
model and four-compartment map (`debate-summary.md` §4), the final 29-candidate ranking
(`p3-ranker.md` §7) and the staged plan (`p3-feasibility.md` §8).

**Skill-file adaptation, as directed.** `.claude/skills/combination-designer/SKILL.md` is
written for Oral Mucositis and treats Ayurvedic multi-plant formulations as a first-class
case. Both are inapplicable. The Traditional Medicine agent returned a documented null for
this disease, and the project's phytochemical corpus does not contain the traditional
retinopathy pharmacopoeia at all. **The traditional-formulation branch is dropped entirely.**
The skill's synergy-assessment methodology (target overlap → pathway coverage → DDI →
formulation feasibility) is retained, with OM phases replaced by the S0–S5 / P1–P9 axes and
"cancer treatment compatibility" replaced by polypharmacy-and-comorbidity compatibility.

---

## 0. HEADLINE — five findings, stated before the argument

1. **The quotient model is correct, and the Pathway Analyst under-sold it.** Solving the
   futile cycle as a two-compartment system gives foam-cell burden `F* = J/c` **exactly** —
   the recycling rate cancels. More importantly, as efflux `c → 0` the system has **no steady
   state**: it integrates. A supply agent then buys *delay*, not a bounded burden. That is a
   change of dynamical regime, which is stronger than multiplicativity.

2. **But his "multiplicative vs additive" contrast is mis-stated.** Two supply agents are
   *also* multiplicative on burden. The real distinction is **parameter independence and
   headroom**, not algebraic form. The correction strengthens the conclusion and weakens the
   stated reason.

3. **The second component does not exist as an approved oral drug — with one near-exception
   nobody in the run named.** Low-dose efavirenz is an allosteric CYP46A1 activator, and
   CYP46A1 oxidation creates a species that leaves by diffusion, needing neither transporter
   nor acceptor. It is approved, oral, CNS-penetrant — and undeployable here for reasons
   given in §3. Everything else fails, each for a different and instructive reason.

4. **The model says the right second component is an extracellular acceptor/scavenger, not
   primarily a transporter inducer.** Adding a direct extracellular-removal term `e` keeps
   burden **finite even at `c = 0`**; a transporter inducer does not, because it multiplies a
   term that may be near zero. This reverses the implicit preference ordering (LXR first,
   peptide second) that the run carried forward, and it points at the one delivery route that
   dissolves the BRB problem entirely.

5. **No combination earns a Gate 1 arm. Two combination *measurements* do, for ~$100–130k.**
   Deferral is the recommendation, argued, not hedged.

---

# PART I — PRESSURE-TESTING THE ARITHMETIC

## 1. (a) Is the quotient model right?

### 1.1 The base case — exactly right

For a compartment at quasi-steady state with influx `J` and first-order clearance `c`:

```
   dM/dt = J − c·M        ⇒        M* = J / c
```

A supply agent scales `J` by `α < 1`; an efflux agent scales `c` by `β > 1`; burden scales by
`α/β`. Halve influx and double clearance → one quarter. The Pathway Analyst's arithmetic is
sound.

### 1.2 The first correction — two supply agents are *also* multiplicative

`p2-pathway.md` §4 argument (1) says two supply-side agents are "additive at best and
sub-additive in practice." **That is the wrong contrast.** If a fibrate scales apoB flux by
0.85 and a second supply agent by 0.60, the combined numerator is 0.51 — a product, not a sum.
Both pairings multiply.

What actually distinguishes them is two things the quotient notation hides:

| | Supply × supply | Supply × efflux |
|---|---|---|
| **Algebraic form** | multiplicative on `J` | multiplicative on `J/c` |
| **Parameter independence** | **No** — both act through one intermediate (plasma apoB particle number) under shared homeostatic feedback: NPC1L1 blockade raises hepatic synthesis; hepatic output reduction raises LDLR. Each agent shrinks the other's substrate. | **Yes** — `J` and `c` are set by different tissues, different cells, different transcriptional programmes |
| **Headroom** | Bounded by the residual apoB left after statin (35–45% already removed — Advocate §2.6) | `c` is *suppressed* in diabetes (ABCA1/LXR axis down, P8.3), so the denominator has the most headroom of any term in the model |
| **Honest verdict** | real but concave | real and approximately independent |

> **Correction to carry forward:** the combination case does not rest on multiplicative-vs-
> additive. It rests on **independence and headroom.** State it that way and it survives
> scrutiny; state it the other way and a reviewer breaks it in one line.

### 1.3 The second test — does it hold for a self-renewing cycle?

`p2-pathway.md` §2.3 establishes the lesion as a cycle, not a deposit: uptake → foam-cell
death → re-release → re-uptake. Model it with two compartments — extracellular modified
lipoprotein `E`, intracellular foam lipid `F`:

```
   dE/dt = J + r·F − u·E          u = scavenger uptake (CD36/OLR1/MSR1)
   dF/dt = u·E − r·F − c·F        r = re-release on foam-cell death
                                  c = true efflux (ABCA1/ABCG1 → acceptor)
```

Solving at steady state:

```
   F* = J / c                                  ← recycling term r CANCELS
   E* = J·(r + c) / (u·c)   =   (J/u)·(1 + r/c)
   M*total = (J/c)·[1 + (r + c)/u]
```

**Three results, and all three favour the combination more than the prose version did.**

- **`F* = J/c` exactly.** The quotient model survives the cycle untouched for the compartment
  where the lesion lives. The futile cycle does not break the arithmetic.
- **The cycle acts as a *multiplier* on the quotient**, not a competing mechanism: the bracket
  `[1 + (r+c)/u]` amplifies `J/c`. More recycling → more total burden for the same `J` and `c`.
  The efflux term is therefore **more** leveraged in a recycling lesion, not less.
- **At `c → 0` there is no steady state.** `d(E+F)/dt = J`, and total lipid grows linearly
  forever. In the suppressed-efflux diabetic retina the system is an **integrator**. A supply
  agent halving `J` halves the accumulation rate and doubles time-to-threshold — valuable, and
  precisely what a prophylactic should claim — but it **cannot set a finite burden.** Only
  `c > 0` converts accumulation into a bounded steady state.

> That last point is the strongest available form of the Pathway Analyst's argument and he did
> not make it. The supply/efflux pair is not merely multiplicative; **it is the difference
> between slowing an integrator and closing it.**

### 1.4 Where multiplicativity breaks down — five conditions

**(i) Serial dependence — transporter without acceptor.** `p2-pathway.md` §2.2: ABCA1 needs
lipid-poor pre-β ApoA1; ABCG1 needs mature HDL. If the limiting half is *acceptor*, inducing
the transporter multiplies by zero. The structure becomes **conditional (gating), not
multiplicative** — the efflux agent reads null alone and only works atop an acceptor source.
This is an argument *for* pairing and *against* efflux monotherapy, but it means an efflux
monotherapy failure would not falsify the arm.

**(ii) The self-cancelling loop — `β` and `α` move together.** `p2-pathway.md` §3.1: hepatic
LXRα → SREBP-1c → VLDL-TG → **more remnants**. An LXR agent raises `β` *and* raises `J`. The
quotient becomes `(α_fibrate · α_LXR)/β` with `α_LXR > 1`. Net sign is not guaranteed.
**This is the one condition under which the combination is not merely non-synergistic but net
harmful** — and see §4.2, because it is simultaneously the best argument for the pairing.

**(iii) Compartment-locality.** `M* = J/c` assumes one well-mixed compartment. The retina has
at least three lipid compartments (intraretinal OPL/Henle where hard exudate sits;
subretinal/Bruch's; intracellular foam) and burden is `Σ Jᵢ/cᵢ`. A supply agent lowers every
`Jᵢ`; an efflux agent raises only the `cᵢ` it reaches. **Multiplicativity is compartment-local
and applies only where both act.** Since the OPL is the hardest compartment to reach orally,
this is the main practical threat to Combination 3 and the main argument for Combination 2.

**(iv) Irreversible sinks.** Organised subfoveal plaque is fibrosis: `c = 0` by construction
and no transcriptional pharmacology changes it (`p2-pathway.md` §3.3). That fraction of burden
is invariant to both agents and dilutes the measured effect in proportion to how late the
enrolled population is. **Every combination here must exclude organised subfoveal plaque.**

**(v) Time scale — and this one has a trial-design consequence the plan has not absorbed.**
`M*` is an asymptote; approach time is `τ = 1/c`. In the diabetic retina `c` is small, so `τ`
is long — plausibly many months to years. **A 12-month imaging endpoint can therefore read null
for a true-positive supply mechanism**, because the system has not had time to relax toward its
new, lower asymptote. Gate 1's kill criterion ("no change in MA turnover or HRF burden at 12
months despite confirmed ≥30% remnant lowering → stop") is written as if the lesion equilibrates
fast. Under the quotient model it may not. Raising `c` *also shortens `τ`*, which is the efflux
agent's second and entirely unremarked benefit: **it makes the trial readable sooner.**

> **Recommendation to the feasibility plan:** Gate 1 should pre-specify **microaneurysm turnover
> rate** (a flux measure, which responds on the timescale of `J`) as the primary and
> **hyperreflective-foci burden** (a stock measure, which responds on the timescale of `1/c`) as
> a secondary with an explicitly weaker prior. The current kill criterion treats them as
> interchangeable. They are not — one reads the numerator, the other the quotient.

### 1.5 Verdict on (a)

> **The quotient model is right, survives the futile cycle exactly, and is under-stated rather
> than over-stated.** Its stated justification ("multiplicative vs additive") is wrong and
> should be replaced by **independence and headroom**. It breaks down under acceptor-limited
> serial dependence, under a partner that raises influx while raising clearance, across
> compartments the partner does not reach, in fibrotic sinks, and — most consequentially for
> this programme — **on the timescale of a 12-month trial.**

---

# PART II — THE COMBINATIONS

## 2. Component eligibility — which Tier 1/2 entries are therapies

The brief warns that a combination built from two control arms is a category error. Adjudicated
against `p3-ranker.md` §7:

| Candidate | Comp. | Eligible as a therapeutic component? |
|---|---|---|
| **Fenofibric acid** | 6.5 | **Yes — the anchor.** Only Group A molecule producing the apoB-particle output the mechanism specifies |
| **Pemafibrate** | 6.0 | **Yes, as an alternative anchor** — relevant mainly for §7 (no renal banding), demoted on efficacy |
| **Fenofibrate** | 5.5 | Yes, but dominated by its own metabolite. Not a distinct component — any "fenofibrate + fenofibric acid" pairing is one drug |
| **Elafibranor** | 5.5 | **NO — 12-week probe.** Michael-acceptor enone at 120 mg/day; chronic liability. Cannot be half of a chronic regimen |
| **Olezarsen** | 5.0 | **NO — control.** Its entire value is deleting the receptor from the mechanism; putting it *with* a fibrate destroys that |
| **Inclisiran** | 5.0 | **YES — and this is the discriminating call.** The ranker says explicitly it is "a genuine therapeutic candidate if that reading is right," not only a falsification arm. It is the one Tier-2 entry with a therapeutic reading |
| **Candesartan** | 5.0 | **NO — already background.** Not a combination; see §6.3 |
| **Seladelpar** | 4.5 | **NO — control**, and its PPARδ carcinogenicity is Type C duration-dependent, i.e. disqualifying for anything chronic |
| **Ezetimibe** | 4.0 | **NO — comparator.** The ranker states it outright: "Never a combination partner" |
| **Dimethyl fumarate** | 2.5 | **NO — RED.** See §6.4 |

**Eligible therapeutic components from the ranked set: fenofibric acid, pemafibrate,
fenofibrate, inclisiran. That is all of them.** Everything else in the top tiers is an
instrument. The efflux half must therefore come from outside the 29.

---

## 3. (c) THE EFFLUX PROBLEM — is there any second component today?

Asked plainly and answered plainly. **Essentially no — and the near-misses are instructive
because each fails differently.**

| Agent / class | Status | Does it move retinal efflux? | Why it fails here |
|---|---|---|---|
| **LXR pan-agonists** (T0901317, GW3965 class) | No approvals; systemic programmes repeatedly stopped | Yes, in principle — ABCA1/ABCG1/APOE are direct targets | Hepatic LXRα → SREBP-1c → VLDL-TG → **more remnants.** In this disease the liability is not generic tox, it is **self-cancelling** (§1.4-ii) |
| **LXRβ-selective / SLXRM** | **Does not exist as a clinical molecule** | Conceptually yes | §5 in full. 78% LBD identity; no asset to combine with |
| **ApoA1 mimetic peptides** (4F / D-4F class) | Preclinical and early clinical; protective in DR models (P8.3) | Supplies the acceptor half, and plausibly removes extracellular modified lipoprotein directly | Oral D-4F bioavailability is poor; no chronic oral product. **But see §4.2 — the delivery objection dissolves if you stop insisting on oral** |
| **CSL112-class apoA-I infusions** | Not available; the class's large outcome programme did not deliver | Raises **lipid-poor pre-β ApoA1** specifically — the right species, which almost nothing else does | Weekly IV over a short course, cardiology-shaped, manufacturing cost prohibitive for lifelong use. Would reach Bruch's/subretinal across the fenestrated choriocapillaris but **not the intraretinal OPL**, which is where hard exudate sits |
| **Niacin** | Approved, oral, chronic, cheap — the most tempting | **No, and the project's own data says so** — see below | Four distinct kills, below |
| **CETP inhibitors** (obicetrapib, late-stage) | Late-stage | Raises HDL-C substantially | **Mature HDL, not pre-β ApoA1** — ABCA1's substrate is the lipid-poor species (§2.2). An afferent agent with an HDL side-effect, not an efflux agent. Class history is poor |
| **CYP46A1 activation — low-dose efavirenz** | **Approved drug, oral, CNS-penetrant; sub-antiretroviral dose (order 10–50 mg/day) is an allosteric CYP46A1 activator** | **Partially — and it is the only entry in this table that can say yes today.** Side-chain oxidation to 24S-hydroxycholesterol produces a species that **leaves by diffusion**, needing neither transporter nor acceptor, and which is itself an endogenous LXR ligand, recruiting the pathway locally without systemic agonism | CYP2B6/3A4 induction in a near-universally polypharmacy population; neuropsychiatric effects persisting at low dose; teratogenicity signal in a population including women of childbearing age; and **the retinal CYP46A1 pool sits predominantly in neurons, not in the microglia/RPE where the foam cell lives.** Undeployable — but it is a real, nameable, approved exception and **no agent in this run named it** |

### 3.1 Niacin, killed four ways — all from pharmacology and the project's own data

This matters because niacin is the one cheap, oral, chronic, generic agent anyone proposing an
efflux arm will reach for first.

1. **The project's own data is direction-incoherent, exactly as it was for quercetin at PPARα.**
   `data/processed-blinded-diabetic-retinopathy/pubchem_phytochem_target_interactions.csv`
   (CTD rows, CID 938) carries four rows asserting *increased* ABCA1 expression or
   ABCA1/ABCG1-mediated export (PMID:15037193, 18602814, 20303128, 20448206, 21317532) and
   three asserting *decreased* ABCA1/ABCG1 protein (PMID:19878707, 18602814 co-treatment).
2. **The decisive row is the receptor-mediated one.** PMID:20655299 encodes
   *[niacin binds to and results in increased activity of HCAR2 protein] which results in
   decreased expression of ABCA1 protein → decreased export of cholesterol.* **HCAR2 agonism is
   niacin's high-affinity pharmacology and the arm you cannot dose around.** The project's own
   evidence therefore places niacin's *receptor* arm on the wrong side of the efflux question.
   *(Caveat per the brief: CTD rows are expression-level associations, not engagement. Row count
   is not evidence weight. This is offered as direction-incoherence, not as proof.)*
3. **Wrong HDL species.** Niacin raises HDL-C largely by reducing hepatic holo-ApoA1 catabolism
   — it preserves **mature** HDL. ABCA1's substrate is lipid-poor pre-β ApoA1. Same failure as
   the CETP class.
4. **Wrong-signed on the disease's dominant driver.** Niacin worsens glycaemic control and
   raises HbA1c in diabetics. HbA1c is the single strongest progression determinant in the
   disease model. An agent that worsens it to improve a second-order lipid term is net-negative
   before any efficacy argument starts — and it unblinds by flushing in an asymptomatic
   population that has no symptom to trade against.

> **Niacin is also the class's cautionary tale, and the lesson generalises:** it raised HDL-C
> reliably and delivered nothing. **Raising HDL-C is not raising efflux capacity.** Any efflux
> programme must be measured with a *functional* cholesterol-efflux-capacity assay, never an
> HDL-C number. That single methodological point is why §8 asks for CEC at Gate 1.

### 3.2 Verdict on (c)

> **Stated plainly, as instructed: there is no approved or late-stage agent that can serve as
> the efflux component of a rational DR combination today.** The one approved molecule that
> moves the arm at all (low-dose efavirenz via CYP46A1) is undeployable in this population for
> reasons unrelated to its mechanism. **This is a finding, not a failure** — it means the
> highest-value combination this disease supports cannot be built, and the correct response is
> to generate the evidence that would justify building its missing half (§8), not to substitute
> a second supply agent and call it a combination.

---

## 4. (b) THE COMBINATIONS

Three designed. One is buildable today and modest; one is the real multiplicative pair and
needs a component that is preclinical; one is the oral version of the same idea and needs a
component that does not exist.

---

### 4.1 COMBINATION 1 — "Remodel then clear"

```
═══════════════════════════════════════════════════════════════════
COMBINATION DESIGN 1: Remodel-then-clear (afferent × afferent, coupled)
═══════════════════════════════════════════════════════════════════

COMPONENTS
  1. Fenofibric acid   135 mg PO once daily   (45 mg if eGFR 30–59)
     — hepatic PPARα: APOC3↓ / LPL↑ → TG-rich remnant particles↓;
       and CETP-remodelling↓ → LDL shifts small-dense → large-buoyant
  2. Inclisiran        284 mg SC day 0, month 3, then q6 months
     — hepatic PCSK9 siRNA → LDLR surface density↑ → apoB particle
       clearance capacity↑ (~40–45%)

COMBINATION TYPE: Sequential pathway coupling (skill §Synergy-2),
                  NOT phase-complementary and NOT numerator/denominator
═══════════════════════════════════════════════════════════════════
```

**The synergy mechanism, stated precisely.** This is a supply × supply pairing, which the
Pathway Analyst rejected — and it survives rejection only because of a specific coupling the
run identified without connecting. `p2-pathway.md` §8.2(2) established that **LDLR-mediated
clearance preferentially spares small-dense LDL**, which is the retention-prone, glycation-prone
species the disease model names as the toxic one. That is the objection that makes the ezetimibe
null uninterpretable, and it applies to inclisiran in full. Separately, fibrates **shift LDL
from small-dense toward large-buoyant** by lowering TG and reducing CETP-mediated remodelling.

> **So the fibrate converts the toxic subfraction into the species that LDLR can clear, and
> inclisiran supplies the clearance capacity.** Upstream remodelling plus downstream capacity.
> Neither is redundant with the other: the fibrate alone remodels into a pathway whose capacity
> is statin-saturated; inclisiran alone adds capacity selective for the particles that were
> never the problem.

This is also the only construction in which the run's own unresolved tension resolves rather
than persists. Round 2 §6 posed it: *"PCSK9 inhibitors lower apoB by 45–55% against a fibrate's
5–15%. If apoB supply is the mechanism, they should work better."* The remodelling argument is
the first answer to that which is not simply "apoB mass is the wrong metric."

**Limb coverage.** Fibrate covers Limb 1 (certain) and Limb 2 (FGF21, certain upstream), and
Limb 3 marginally. **Inclisiran covers none of the four** — the four-limb taxonomy is
PPARα-centric and a non-PPAR partner falls outside it. Name the extra limb explicitly:
**Limb 0 — non-receptor apoB clearance capacity (LDLR density).** Combination = 1 + 2 + (3) + 0.

**Stage and module coverage that neither component achieves alone — honestly, none.**

| | S0 | S1 | S2 | S3 | S4 | S5 |
|---|---|---|---|---|---|---|
| Fenofibric acid | ░░ | ██ | ██ | ▒▒ | ░░ | ░░ |
| Inclisiran | ░░ | ██ | ██ | ▒▒ | ░░ | ░░ |
| **Combination** | ░░ | ██ | ██ | ▒▒ | ░░ | ░░ |

| Module | Fibrate | Inclisiran | Combination |
|---|---|---|---|
| **P8.1 supply** | ██ | ██ | ██ (deeper, and on the *right subfraction*) |
| **P8.3 efflux** | ▒▒ | ░░ | ▒▒ — **STILL THE GAP** |
| P6 RELA/leukostasis | ▒▒ | ░░ | ▒▒ |
| P8.2 / P8.7 modification | ░░ | ░░ | ░░ |
| P1–P5, P7, P9 | ░░ | ░░ | ░░ |

> **The honest statement, and it is why this scores 5.0 rather than 7:** the combination adds
> **no stage and no pathway module.** It deepens one module on the correct subfraction. That is
> a real pharmacological argument and a thin combination argument.

**DDI and practical assessment.** Excellent, and unusually so. Inclisiran is a GalNAc-conjugated
siRNA: no CYP metabolism, no transporter competition, no plasma-protein-binding displacement, no
renal dose adjustment in mild-to-moderate CKD. Fenofibric acid is ~99% albumin-bound and renally
eliminated as the acyl glucuronide — the two elimination routes do not intersect at any point.
Neither component adds to the other's myopathy liability (the fibrate–statin pharmacodynamic
limb is ~3×, Safety §; inclisiran contributes nothing to it). **Overall DDI risk: minimal — the
lowest of any pairing considered here.**

**Expected failure mode, named in advance.** Not safety and not pharmacology. **Economics and
interpretability.** (i) Inclisiran is branded and expensive; `p3-feasibility.md` §6–7 makes the
*entire* programme rationale a cheap oral generic routed to WHO EML listing, and this
combination destroys that endgame. (ii) It is wholly afferent: under §1.3 it slows an integrator
and does nothing to an established self-renewing lesion, so it will under-perform exactly in the
patients enrichment would otherwise select. (iii) Its mechanistic premise — the subfraction
coupling — **rests entirely on the ranker's F2/K11, which has not been measured.** If F2 reads
negative (fibrates do not reduce the retention-prone subfraction), this combination's whole
rationale evaporates along with the class.

**Verdict: Promising but subordinate.** Buildable today, mechanistically coupled, operationally
clean — and it buys depth where the run already has depth, at the cost of the deployment model.
**Its correct form is not a combination arm but a 2×2 factorial at Gate 2**, where it would
simultaneously test the combination and settle the remnant-vs-apoB-mass question the run could
not close.

---

### 4.2 COMBINATION 2 — "Numerator and denominator, delivered locally" — **TOP PICK**

```
═══════════════════════════════════════════════════════════════════
COMBINATION DESIGN 2: Oral supply × locally delivered acceptor
═══════════════════════════════════════════════════════════════════

COMPONENTS
  1. Fenofibric acid   135 mg PO once daily   (45 mg if eGFR 30–59)
     — lowers J (afferent apoB/remnant flux), hepatic engagement certain
  2. ApoA1-mimetic peptide (4F class), intravitreal or suprachoroidal,
     co-administered at an EXISTING anti-VEGF injection visit (q8–12 wk)
     — supplies lipid-poor acceptor and sequesters oxidised phospholipid
       directly in the interstitium
     — NO established clinical dose. Design target below, not a number
       invented for this report.

POPULATION: S3–S4 with exudative/lipid-phenotype DME, already receiving
            intravitreal therapy. EXCLUDE organised subfoveal plaque (§1.4-iv).

COMBINATION TYPE: True numerator × denominator — plus phase-complementary
                  (skill §Synergy-4) — plus toxicity-free by route separation
═══════════════════════════════════════════════════════════════════
```

**Why this is the top pick, and the analytic result that drives it.** Return to §1.3 and add a
direct extracellular-removal term `e` (an acceptor/scavenger that binds modified lipoprotein and
oxidised phospholipid in the interstitium, rather than inducing a cellular transporter):

```
   dE/dt = J + r·F − u·E − e·E
   dF/dt = u·E − (r + c)·F

   ⇒  E* = J / [ u·c/(r+c) + e ]        F* = u·J / [ u·c + e·(r+c) ]

   At c = 0 (the suppressed-efflux diabetic retina):
      transporter inducer alone  →  E*, F*  →  ∞        (no steady state)
      extracellular remover      →  E* = J/e,  F* = uJ/(e·r)   ← FINITE
```

> **An extracellular removal route restores a bounded steady state even when transporter
> function is zero. A transporter inducer cannot, because it multiplies a term that may be near
> zero.** This reverses the preference ordering the run carried forward, which put LXR
> modulation first and peptides second. **On the dynamics, the acceptor/scavenger is the better
> complement, not the fallback.**

**And it is the more developable one.** `p2-pathway.md` §4.1 named the delivery insight and
observed that no agent in the run had picked it up: the lesion an efflux agent targets —
persistent intraretinal exudate in exudative DME — occurs in patients **already receiving
intravitreal injections**. Co-administration at the same visit adds **no new procedure**, and
**the entire BRB argument — §2.1, §3.1, the Kp,uu term, the four-compartment map, the
"you cannot perform retinal reverse cholesterol transport from the liver" statement — simply
does not apply.** A peptide acting in the interstitium does not need to enter cells either.

**This is the only construction in this report where the efflux component is both mechanistically
right and physically deliverable.**

**Limb coverage.** Fibrate: Limb 1 + Limb 2 + (3). Peptide: **a limb the four-limb taxonomy does
not contain** — the efferent limb, call it **L-E**. That is precisely the point: the taxonomy was
built around PPARα and inherits its afferent-only blind spot.

**Stage and module coverage that neither component achieves alone — substantial, unlike Combo 1.**

| | S0 | S1 | S2 | S3 | S4 | S5 |
|---|---|---|---|---|---|---|
| Fenofibric acid | ░░ | ██ | ██ | ▒▒ | ░░ | ░░ |
| ApoA1 peptide (local) | ░░ | ░░ | ▒▒ | ██ | ██ | ░░ |
| **Combination** | ░░ | ██ | ██ | **██** | **██** | ░░ |

| Module | Fibrate | Peptide | Combination |
|---|---|---|---|
| **P8.1 supply (accretion)** | ██ | ░░ | ██ |
| **P8.3 efflux (persistence)** | ▒▒ | **██** | **██ ← the run's only empty, chemically addressable module, filled** |
| P8.2 / P8.7 oxidised-lipid load | ░░ | ▒▒ (oxPL sequestration) | ▒▒ |
| P6 NLRP3 / inflammation | ▒▒ | ▒▒ (less foam-cell death → less IL1B) | ▒▒ |

**The patient neither component covers alone.** `p2-pathway.md` §3.3 and §4 establish that hard
exudate is supply-limited during accretion and clearance-limited during persistence. The
mid-trajectory patient — **fresh and persisting extrafoveal exudate simultaneously** — is served
by neither agent alone and by the pair completely. And the Pathway Analyst's own independent
check applies: **the two agents have opposite enrichment criteria** (the fibrate wants elevated
remnants and *no* exudate yet; the peptide wants existing exudate). Two agents selecting opposite
patients are not doing the same thing.

**Unmet-need coverage.** #5 (hard exudate / intraretinal lipid — the P8 axis) directly; #2
(non-VEGF mechanism for the 30–50% incomplete-responder DME fraction) directly; and #4 is not
worsened, because the injection already exists.

**Dose, stated honestly.** There is no established clinical dose for an intravitreal
ApoA1-mimetic peptide and I will not invent one. The design target is: an intravitreal
concentration exceeding the peptide's oxidised-phospholipid binding Kd, sustained across the
injection interval. **The binding PK requirement is a vitreous half-life ≥ the q8–12-week dosing
interval**, which for a small unmodified peptide it will not have — so this requires a depot,
PEGylation, or an Fc/albumin conjugate, and that formulation problem is the programme's first
real cost, ahead of any efficacy question.

**DDI and practical assessment.** Systemic × intravitreal: no pharmacokinetic interaction is
possible. **Do not co-formulate with the anti-VEGF agent** — compatibility is unknown and a
precipitation or aggregation failure would be attributed to the wrong component; give as a
separate injection or sequentially at the same visit. Procedural risk is not additive if truly
co-administered at an existing visit, but a second needle pass is not nothing and
endophthalmitis risk must be measured, not assumed unchanged.

**Expected failure mode, named in advance.** **The term `e` is the load-bearing assumption and it
is unmeasured.** The whole argument above depends on the peptide removing extracellular modified
lipoprotein, not merely accepting cholesterol from cells. If 4F-class peptides act *only* as
ABCA1 acceptors, then §2.2's objection returns in full — the diabetic lesion is reported on the
**transporter** side, and supplying acceptor to a cell whose pump is downregulated does not
unload it, and the combination degrades to the gating structure of §1.4(i). **The experiment that
decides it:** in a diabetic retinal explant or foam-cell model with ABCA1 silenced, does the
peptide still reduce extracellular modified-lipoprotein mass? If yes, `e > 0` and this design
stands. If no, it does not. That experiment is cheap and nobody has specified it.

Secondary failure modes: a peptide is immunogenic on repeat intravitreal dosing; and the
population is S3–S4, which is **not** the programme's chosen S1–S2 window, so this is a second
programme rather than an extension of the first.

**Verdict: Recommended as a distinct parallel programme track. The strongest combination concept
this disease supports.** It is also the one with the shortest route from concept to a decisive
experiment.

---

### 4.3 COMBINATION 3 — "The oral multiplicative pair"

```
═══════════════════════════════════════════════════════════════════
COMBINATION DESIGN 3: Oral supply × oral efflux (CONCEPT ONLY)
═══════════════════════════════════════════════════════════════════

COMPONENTS
  1. Fenofibric acid 135 mg PO daily — lowers J
  2. An orally retina-penetrant LXRβ-biased partial modulator
     — DOES NOT EXIST. Target profile at §5.
       Neutral; MW < 400; cLogP 2–4; TPSA < 70; HBD ≤ 2; PPB < 98%;
       not a P-gp/BCRP substrate; plasma TG as mandatory dose-limiting
       biomarker.

COMBINATION TYPE: Numerator × denominator, PLUS toxicity mitigation
                  (skill §Synergy-5) — and the second is why the pair
                  is better than either component's solo case
═══════════════════════════════════════════════════════════════════
```

**The synergy mechanism has two independent legs, and the run only noticed one.**

*Leg 1 — the quotient.* As §1. The fibrate lowers `J` from the liver with certain engagement;
the modulator raises `c` in the retina. Independent parameters, independent tissues, maximum
headroom in the denominator.

*Leg 2 — and this is the part nobody stated.* §1.4(ii) identified the self-cancelling loop as
the condition under which the pairing fails: residual LXRα agonism raises hepatic SREBP-1c →
VLDL-TG → remnants → raises `J`. **A fibrate is the specific antidote to exactly that liability.**
PPARα agonism raises LPL and lowers APOC3, which is the direct pharmacological reversal of a
VLDL-TG rise. So the co-administered fibrate does not merely add a second mechanism — **it
neutralises the class liability that has repeatedly stopped systemic LXR programmes.**

> **This inverts the development logic.** The standard objection to systemic LXR agonism is
> hypertriglyceridaemia and steatosis. In this specific combination, the partner is a drug whose
> principal established pharmacodynamic effect is lowering triglycerides. **An LXR modulator may
> be more developable in combination with a fibrate than alone** — which, if true, is the single
> most useful thing this report says to anyone considering the LXR route, and it is a claim that
> can be tested in a rodent study for the cost of a dose-ranging arm.

**Limb coverage:** 1 + 2 + (3) + L-E, with an extra: **LXR has its own well-described NF-κB
transrepression arm**, so the modulator contributes to P6 independently of the fibrate's marginal
transrepression — convergent reinforcement on a threshold-nonlinear endpoint, which §6.2 of the
Pathway report classifies as the good kind of redundancy.

**Module coverage:** P8.1 ██ + P8.3 ██ + P6 ▒▒. The complete P8 lipid axis minus the modification
sub-modules (P8.2/P8.7), which no safe candidate covers (§6.4).

**Expected failure mode:** §5, in full. The short version is that this is a 12–15-year NCE
programme costing an order of magnitude more than the entire $40–70M plan it would attach to.

**Verdict: Not recommended as a programme to start. Recommended as the thing Gate 0 and Gate 1
should be instrumented to justify or refute for someone else.** See §8.

---

## 5. (d) THE LXR OPENING — assessed as a combination-partner concept

Round 2's structural finding is real and it is the run's best constructive output: the PPARα
pocket mandates a lipophilic acid, which couples potency to hepatoselectivity and ionisation —
the single worst BRB liability. **The LXR pocket does not. LXR ligands are neutral.** So the
contradiction that makes a retina-penetrant PPARα agonist structurally impossible is simply
absent for LXR, and what remains are ordinary medicinal-chemistry problems. And it aims at the
**gap** rather than the module that is already covered six-deep.

### 5.1 What it would need to be

| Requirement | Target | Source |
|---|---|---|
| Ionisation | **Neutral** — the whole opening | Pathway §3.1 |
| Physicochemistry | MW < 400, cLogP 2–4, TPSA < 70, HBD ≤ 2, PPB < 98% | Pathway §3.1 / model §6.2 |
| Efflux | Not a P-gp or BCRP substrate (the quercetin failure mode) | Ranker #29 |
| Isoform | **LXRβ-biased** — hepatocyte lipogenesis is predominantly LXRα-driven; LXRβ is ubiquitous and carries the macrophage/glial efflux function | Pathway §3.1 |
| Efficacy profile | **Gene-selective partial agonist**: retain ABCA1/ABCG1 induction, leave SREBF1 under-induced | Pathway §3.1 |
| Safety biomarker | **Plasma TG, mandatory and dose-limiting** | Pathway §3.1 |

### 5.2 What kills it — six, ranked

**1. The gene-selectivity demand is stronger than tissue-selectivity and probably unmet.**
This is the sharpest objection and it comes from the run's own SAR work. Round 2 §2 established
that for PPARα a neutral head produces a **partial agonist by construction**, because Tyr464 sits
on mobile helix 12 and pays for AF-2 closure, so efficacy degrades before affinity. The same
physics applies to LXR's AF-2. For an SLXRM that is what you want — but the design asks the
partial agonist to induce *ABCA1* fully while leaving *SREBF1* under-induced. **That requires the
two promoters to have materially different coactivator-recruitment thresholds, and whether they do
is unknown.** It is a single, cheap, decisive reporter experiment, and it should be done before
any chemistry: **if ABCA1 and SREBF1 share a recruitment threshold, the entire SLXRM concept is
dead and no amount of medicinal chemistry rescues it.**

**2. The 78% LBD identity.** Real β-selectivity windows are hard-won and most "β-selective"
compounds have modest ones. Hepatocytes express LXRβ, so β-bias **reduces rather than abolishes**
the TG signal. Non-clinical and non-DR clinical experience with β-biased and partial agonists
shows the signal attenuated, not removed.

**3. Isoform promiscuity across the nuclear-receptor superfamily — the ranker's K3 argument,
transplanted.** A neutral, MW<400, cLogP 2–4 lipophile is the preferred chemotype of several
nuclear receptors, **PXR above all**. PXR activation induces CYP3A4, which in a near-universally
polypharmacy, statin-treated, RAS-blocked population is a programme-level liability, not a
footnote. Selectivity over PXR is an underrated kill risk and should be a counter-screen from
compound #1.

**4. The precedent.** Round 2 §3: ~30 years, two receptor families, a dozen programmes of
tissue-selective and dissociated nuclear-receptor ligands, **zero systemic approvals**. The only
survivors reached patients topically or by inhalation — i.e. by solving delivery the hard way.
**Applied here, the precedent argues for local delivery — which is Combination 2.**

**5. It must be developed as a monotherapy first.** No regulator approves an NCE only in
combination with a generic. So the "combination partner" framing is misleading: the LXRβ
programme has to clear its own efficacy bar, in a disease where the efflux arm has **never been
clinically validated in any indication**, before it can be a partner at all.

**6. Therefore the arithmetic.** An NCE programme of that shape is 12–15 years and plausibly
$500M+. `p3-feasibility.md` costs the *entire* recommended programme at $40–70M over 10–12 years,
and names its principal risk as **"no funder exists for a generic."** The LXR route sits an order
of magnitude outside that envelope. **It is not that the idea is wrong — it is the best idea in
the run — it is that it belongs to a different programme with a different balance sheet.**

### 5.3 Verdict on (d)

> **The LXR opening is real, correctly identified, and outside this programme's envelope by a
> factor of ten.** The right action is not to start it and not to drop it: it is to make Gate 0
> and Gate 1 generate, almost for free, the two measurements that would tell an LXR programme
> whether to exist — **is `c` genuinely the limiting term in diabetic retina, and do ABCA1 and
> SREBF1 separate on coactivator-recruitment threshold.** §8 costs this at ~$100–130k.

---

## 6. (e) COMBINATIONS THAT WOULD BE MISTAKES

### 6.1 Fibrate + ezetimibe — **NO (five reasons, and the fifth is the one that matters)**

1. **Same afferent term, with shared homeostatic feedback.** NPC1L1 blockade raises hepatic
   cholesterol synthesis; hepatic output reduction raises LDLR. Each agent shrinks the other's
   substrate. Sub-additive on the shared intermediate.
2. **The subfraction directions may oppose.** `p2-pathway.md` §8.2(2): ezetimibe works through
   LDLR, which **spares small-dense LDL**; fibrates shift LDL *toward* large-buoyant. On the
   specific toxic subfraction, the two may move in opposite directions even while both "lower
   apoB." **The combination's effect on the retention-prone particle could be smaller than the
   fibrate's alone.**
3. **Additive cholelithiasis risk** — both increase biliary cholesterol saturation, in a
   population with elevated gallstone prevalence.
4. **It consumes a trial arm to answer nothing**, in a trial whose binding constraint is 3.5%
   net eligibility and whose principal risk is that no funder exists.
5. **It destroys the run's single most valuable design contribution.** Ezetimibe's role
   (disease-brief §8 Group E, ranker #9) is the **mechanism-discriminating comparator**. You
   cannot use the same agent as comparator and combination partner without destroying the
   comparison. And since the ezetimibe *null* is uninterpretable (§8.2 asymmetric
   informativeness: the mismatched result carries no information), a combination containing it
   **inherits the uninterpretability** — a null combination arm would tell you nothing at all.

> The ranker already wrote "Never a combination partner." This report upholds that and adds that
> the reason is experimental-design integrity, not only pharmacological redundancy.

### 6.2 Fibrate + statin — **NOT A COMBINATION; it is the control arm**

Statins are background therapy in essentially the whole population and the trial design assumes
it. "Adding a statin" adds nothing. The only genuinely new question is **intensifying** it, and
that is actively harmful to the programme in three ways:

- It removes more apoB from **both** arms, shrinking the fibrate's measurable increment — which
  is the Advocate's §2.6 point and the most likely way the programme dies (ranker F1: *the
  power calculation, free, do it first*).
- It adds the class's one real DDI. The Safety agent quantified it: all three gemfibrozil
  mechanisms are absent from fenofibrate, only the pharmacodynamic limb transfers, so roughly
  **3× rather than 20×** — inside the bar, but non-zero. And the amplifier the Safety agent
  flagged applies here specifically: **diabetic neuropathy degrades the myalgia early-warning
  signal**, so the one toxicity you would be stacking is the one this population cannot report.
- **The trap to name explicitly:** do **not** run a "fibrate + high-intensity statin" arm against
  a low-intensity-statin control. That design measures the statin and attributes it to the
  fibrate. Fix the statin regimen across arms and enrich on **residual** risk instead — elevated
  remnants despite statin, per `p3-feasibility.md` §2.6/§3.

### 6.3 Fibrate + candesartan — **NOT A COMBINATION; already background, and blocked where it is not**

`p2-pathway.md` §7.3 offered this as the pragmatic alternative pair, and the later rounds closed
it. The ranker blocked candesartan at G3 for a deployment reason that is fatal to it as a
combination component: **the population is already largely on renin-angiotensin blockade**, and
where it is not, adding it creates contraindicated dual RAS blockade. So the "combination" is
either already present in both arms or unsafe. There is no third case.

*One genuinely useful residue, worth keeping as investigator training rather than as a
combination:* candesartan also raises creatinine, by efferent-arteriolar haemodynamics — **the
same lab signal as the fibrate, opposite meaning, opposite management.** In a trial using
creatinine-adjacent decisions this contrast will come up and the sites should be taught it.

### 6.4 Fibrate + dimethyl fumarate — **NO as a chronic therapy, despite being the best network pair**

This was `p2-pathway.md` §7.2's recommended pair and I am **overruling it**, consistent with
Round 2 §5 and ranker #17. The network argument is genuinely strong — toxicity of extravasated
lipoprotein ≈ (particle number) × (in-situ modification capacity), the fibrate lowers the first
term from the liver, DMF lowers the second from inside the neural retina, and DMF is the only
candidate in the set covering P8.2 or P8.7 at all. **The structure is right. The molecule is
not.**

- **RED on safety (2.5).** PML risk extrapolates ~2.3× over the Safety agent's bar across thirty
  years; mandatory lymphocyte monitoring.
- **The decisive argument is not the number:** safety that depends on monitoring does not survive
  translation from symptomatic specialist care to asymptomatic primary care at population scale.
  **In a combination this is worse, not better** — you stack LFTs and creatinine for the fibrate
  on lymphocyte counts and PML vigilance for DMF, for decades, in people who can see perfectly
  well. The monitoring burden is the product of two monitoring programmes, not the maximum of
  them.
- **An unquantified wrong-sign risk that bears specifically on combination use:** DMF succinates
  GAPDH Cys152, and GAPDH inhibition is the central divergence node of the disease model's
  unifying hypothesis.

> **Disposition: rule out as a chronic combination; retain the *structure*.** If a safer NRF2
> activator with retinal access emerges, supply × modification is the second multiplicative pair
> this disease supports and the argument above transfers intact.

### 6.5 Anything + scavenger-receptor blockade (CD36 / OLR1 / MSR1) — **NO, and the model makes the wrong-sign risk sharper than the prose did**

`p2-pathway.md` §3.2 called this a category error — blockade is a second *uptake* intervention on
the afferent side, not the complement to efflux — and attached a wrong-sign risk. The
two-compartment model of §1.3 states it exactly. Scavenger blockade lowers `u`:

```
   F* = J / c                    ← INDEPENDENT OF u. Blockade does not reduce
                                   steady-state foam-cell lipid AT ALL.
   E* = J·(r + c) / (u·c)        ← RISES as u falls. The extracellular pool grows.
```

> **Lowering `u` leaves the foam-cell burden exactly where it was and inflates the extracellular
> modified-lipoprotein pool — and extracellular gly-oxLDL is the directly cytotoxic species
> (P8.2), lethal to pericytes, endothelium, Müller cells and RPE.** Blockade trades the less
> toxic compartment for the more toxic one.

And it is **maximally dangerous in exactly the diabetic state**: as `c → 0` with no extracellular
removal route, macrophage uptake is the only remaining sink, and closing it sends `E*` to
infinity. The model and the Pathway Analyst's prose agree precisely, including on the legitimate
residue: blockade *does* reduce the **rate** of foam-cell formation and death, hence NLRP3
signalling. **That is an anti-inflammatory claim scored under P6, never efflux coverage under
P8.3.** Calling it efflux coverage double-counts.

*(Model caveats, stated: single-compartment, first-order kinetics, quasi-steady state, no
saturation of `u` — CD36-mediated uptake does saturate. The structure is reliable; the magnitudes
are not.)*

### 6.6 Fibrate + icosapent ethyl — **defer; not a mistake, but it does not earn a slot**

Tempting, because IPE is the sole occupant of P8.6 resolution, which the disease model names as
under-exploited, and it is the only dosable form of the Group B fatty-acid finding. Against it:
bleeding risk on antiplatelets **in a trial where vitreous haemorrhage is a measured outcome** —
structurally the same flaw as minocycline's papilloedema, an adverse effect that attacks the
endpoint from inside; an AF signal; and the ranker's gate, a null large ω-3 RCT in a chronic
progressive retinal disease.

**And one new objection from the project's own data.** `pubchem_phytochem_target_interactions.csv`
records, for linoleic acid (CID 5280450, CTD): *linoleic acid results in increased degradation of
ABCA1 protein* and *linoleic acid inhibits the reaction [ABCA1 protein results in increased export
of cholesterol]* (PMID:16118212), plus decreased ABCG1 mRNA and protein (PMID:16730733). **A free
fatty acid is not efflux-neutral by default — in this corpus one of them is a data-backed efflux
antagonist.** EPA is not linoleic acid and the finding does not transfer directly, but it means
any PUFA arm must **measure** ABCA1/efflux capacity rather than assume it. This also sharpens the
ranker's "direction-arguable" verdict on linoleic acid (#22) into something more specific:
**linoleic acid has data-backed wrong-sign activity on the exact arm this report identifies as
the gap.**

### 6.7 Two instruments together — **category error, named as instructed**

Olezarsen + seladelpar, ezetimibe + inclisiran, elafibranor + anything chronic. Each component's
value lies in what its *isolated* result licenses you to infer. Combining two of them produces a
result that licenses nothing. Listed because the brief asked for it to be listed.

### 6.8 Any intra-class pairing — **one drug wearing two names**

Fenofibrate + fenofibric acid is a single pharmacological entity plus a hydrolysis step and a
food effect (ranker #3). Fenofibrate + pemafibrate is one receptor hit twice by two molecules
with different liabilities and no complementary coverage. There is no intra-class combination.

---

## 7. (g) THE DOSE-BANDING INTERACTION — mitigate or compound?

### 7.1 The answer is neither by default: a combination **averages**, weighted by effect share

This needs stating carefully because the intuitive answer is wrong. Multiplicative effects on
burden are **additive on log-burden**. So if component A retains fraction `ρ_A` of its log-effect
in the dose-banded stratum and component B retains `ρ_B`, the combination retains the
**effect-share-weighted mean**, not the product. A combination does not automatically compound
renal fragility — but neither does it automatically dilute it.

Using `p3-feasibility.md` §2.2's own strata (eGFR ≥60: 60% of population, 48% of events; eGFR
30–59: 32% of population, 52% of events, 3× dose reduction; eGFR <30 excluded) and its own
retention figures (systemic limb 0.75, retinal limb 0.33), with a 50/50 effect split:

| Regimen | Banded-stratum retention | Event-weighted retention | Sample-size inflation | vs fibrate mono |
|---|---|---|---|---|
| **Fenofibric acid alone** (systemic limb) | 0.75 | **0.870** | **1.32×** | — |
| **+ renally invariant partner** (inclisiran; or any local agent) | 0.875 | **0.935** | **1.14×** | **13% fewer patients** |
| **+ partner also renally banded** (another renally-cleared systemic agent) | 0.750 | 0.870 | 1.32× | no change |
| **+ partner dependent on passive retinal exposure** | 0.540 | 0.761 | 1.73× | **31% more patients** |
| *(retinal-limb monotherapy, for reference)* | 0.33 | 0.652 | 2.36× | — |

*(These reproduce the feasibility agent's 0.87 and 1.32× exactly, which is the check that the
model is the same one.)*

### 7.2 The three consequences

**1. A renally invariant partner is worth ~13% of sample size — and that is the strongest
*practical* argument for Combination 1.** Inclisiran is GalNAc-targeted with no renal dose
adjustment and a fixed twice-yearly dose, so the banded stratum keeps 100% of its contribution.
*Honest counterweight:* `p3-feasibility.md` §2.5 mitigation 4 already achieves most of this with
a **molecule choice** — pemafibrate is hepatobiliary and needs no banding at all. So the real
comparison is combination-with-inclisiran versus just-use-pemafibrate, and pemafibrate is cheaper
and simpler but Japan-only, BID, branded, and was demoted on efficacy. That is the actual
trade-off and it should be stated as such rather than as an argument for the combination.

**2. Combination 2's local component is invariant *by construction*, and lands where the disease
is worst.** An intravitreal agent has no systemic dose–response, so renal function cannot band it
at all. And because nephropathy and retinopathy track together, **the banded stratum is also the
higher-event, more-exudative stratum** — so the local component delivers its full effect precisely
where the oral component is weakest and the disease is most advanced. That is a structural
argument for local delivery that the run has not made, and it is independent of the efflux
argument.

**3. The rule that follows, and it is the general answer to (g):**

> **Choose combination partners on elimination route, not only on mechanism.** A partner that is
> renally invariant strictly improves the trial; a partner that is renally banded is neutral; a
> partner whose action depends on passive retinal exposure **imports the exact fragility the run
> spent two rounds establishing is fatal**, and costs ~31% more patients. The last case is the
> one to watch, because a "retina-penetrant" partner sounds like the solution to the run's
> central problem and is, in a banded population, a way of making the problem bigger.

### 7.3 One new trial-integrity point, extending feasibility §2.4

The feasibility agent showed that creatinine-based banding progressively **under-doses the active
arm only**, because the fibrate's benign creatinine rise reads as a ~17% apparent eGFR fall, and
fixed it with cystatin-C-based eGFR. In a **combination** trial the problem changes character: the
artefact fires on the fibrate component only, so a combination arm and a monotherapy arm are
down-banded at **different rates**, and the arms' achieved exposures drift apart over time in a
way that is not randomised. **In a combination trial, cystatin-C banding is not a de-biasing
nicety — it is a precondition for the arms remaining comparable at all.**

---

## 8. (f) DOES A COMBINATION EARN A GATE 1 SLOT?

### 8.1 The recommendation — **No. Defer. And the deferral is argued, not hedged.**

Gate 1 as costed: n≈150, three arms (fibrate / ezetimibe / placebo), 12 months, $4–7M, plus a
12-week elafibranor probe arm n≈40–60 at +$1.2–2.0M, total **$5–9M**. Five reasons no combination
belongs in it:

**1. A combination arm would obscure Gate 1's own kill criterion.** That criterion is "no change
in MA turnover or HRF burden at 12 months despite confirmed ≥30% remnant lowering → stop." If a
combination arm moves the endpoint and the monotherapy arm does not, you cannot tell which
component carried it, and you have spent the power that was supposed to produce a clean go/no-go.
**Gate 1 exists to answer one question and a combination arm makes that question unanswerable.**

**2. It is not powerable.** n≈150 across three arms is ~50/arm, already enriched to 3.5% net
eligibility. A combination arm is only interpretable inside a **2×2 factorial** — four cells, ~38
per cell — which cannot support a PD endpoint at this enrichment. Adding cells instead of
splitting them raises cost by a third or more on a programme whose principal stated risk is that
no funder exists.

**3. The only combination with genuine multiplicative structure has no second component.** §3.
You cannot run it. Substituting a second supply agent to have *a* combination arm would be exactly
the error §6.1 describes.

**4. The one buildable combination answers a question better asked another way.** If inclisiran
belongs at Gate 1, it belongs as a **fourth monotherapy arm** — the apoB-mass falsification arm
the ranker already specified — not as a combination partner. Its combination value (§4.1) is a
Gate 2 factorial question.

**5. Sequencing.** Every combination in this report depends on a quantity **nobody has measured**:
the retinal clearance rate constant `c`, and whether the lesion is at steady state or in the
accumulating regime of §1.3. Until that is known, combination design is speculation with a
decimal point. **And measuring it is a Gate 0/1 job.**

### 8.2 What *does* earn a place — two measurements, no arms, ~$100–130k

These are the combination programme's correct footprint today. Neither adds a patient, an arm, or
a unit of statistical power.

| Where | What to add | Cost | What it decides |
|---|---|---|---|
| **Gate 0** (the existing 5-arm rodent study, $350–600k) | The transactivation panel already includes *ABCA1* mRNA. Add: **ABCA1/ABCG1 protein** (not transcript alone), **retinal free- and esterified-cholesterol mass**, and a **macrophage cholesterol-efflux-capacity assay on terminal plasma.** Plus the §5.2(1) reporter: do **ABCA1 and SREBF1 separate on coactivator-recruitment threshold** under a partial LXR ligand? | **~$30–60k** | Whether `c` is genuinely the limiting term — the premise of every combination here. And whether the SLXRM concept is chemically askable at all, which is the single cheapest way to kill or license the LXR route |
| **Gate 1** (the existing plasma biomarker panel) | **Cholesterol efflux capacity (CEC)** on stored plasma — a *functional* assay, never HDL-C | **~$150 × ~450 samples ≈ $70k** | Whether the fibrate's ApoA1/acceptor nudge (§2.4) does anything measurable. This is the measurement that would have killed niacin and the CETP class decades early, and it is the one that tells you whether Combination 3's premise is already half-satisfied |

> **Total incremental ask: ~$100–130k, roughly 1.5% of Gate 1's budget, zero new arms, zero
> patients, zero power cost.** Against that, it is the only route by which the run's identified
> gap becomes a decidable question rather than a standing observation.

### 8.3 Where combinations re-enter the plan

- **Gate 2** — if and only if Gate 1 is positive: a **2×2 factorial of fibrate × inclisiran**
  nested in the registrational cohort. It tests Combination 1 and simultaneously settles the
  remnant-vs-apoB-mass question that two rounds and a debate could not close. Only affordable
  because the registry shell already exists.
- **A parallel track, not a gate** — Combination 2 as its own programme in exudative DME (S3–S4,
  already-injected patients). Different population, different endpoint, different regulatory
  route, different unmet needs (#5 and #2). **It should not be bolted onto the S1–S2 prophylaxis
  programme**; it should start with the §4.2 explant experiment that measures `e`, which is a
  bench study, not a trial.
- **Never** — Combination 3 as a programme this plan funds. §5.3.

---

## 9. SUMMARY TABLE

| Combination | Type | Limbs | Stages | Modules added vs best single agent | Synergy real? | Achievable? |
|---|---|---|---|---|---|---|
| **1. Fenofibric acid + inclisiran** | Sequential coupling (remodel → clear) | 1, 2, (3), **0** | S1–S2 | **None.** Depth in P8.1 only | Yes, modest; rests on unmeasured F2 | **Yes, today** — but breaks the generic/EML deployment model |
| **2. Fenofibric acid + local ApoA1-mimetic** | **Numerator × denominator**, phase-complementary | 1, 2, (3), **L-E** | S1–S2 **+ S3–S4** | **P8.3 (the empty module)**, plus P8.2/P8.7 and P6 partially | **Yes, the real one** — and dynamically stronger than a transporter inducer (§4.2) | Component 2 preclinical; **delivery problem already solved** |
| **3. Fenofibric acid + LXRβ-biased SLXRM** | Numerator × denominator **+ toxicity mitigation** | 1, 2, (3), **L-E** | S1–S4 | P8.3 + P6 | **Yes**, with two independent legs | **No** — NCE, 12–15 yr, ~10× the programme budget |
| *Fibrate + ezetimibe* | — | — | — | — | No | Destroys the comparator. **Ruled out** |
| *Fibrate + statin intensification* | — | — | — | — | Not a combination | **Ruled out** — it is the control arm |
| *Fibrate + DMF* | Supply × modification | — | — | P8.2/P8.7 | Structure yes, molecule no | **Ruled out** — RED, stacked monitoring, GAPDH wrong-sign |
| *Fibrate + candesartan* | — | — | — | — | Already background | **Ruled out** |
| *Anything + SR blockade* | — | — | — | — | **Wrong-signed** (`F*` unchanged, `E*` rises) | **Ruled out** |

---

## 10. CONFIDENCE AND EVIDENCE BASIS

- **§1 ODE derivations:** HIGH confidence in the algebra (`F* = J/c`, `E* = J(r+c)/uc`, the `c→0`
  divergence, the `e`-term result, the `u`-independence of `F*`); **LOW** confidence in every
  magnitude, because no parameter in the model has ever been measured in human diabetic retina.
  The model is a structure generator, not a calculator. **Every quantitative statement in §1 is
  conditional on parameters §8 asks someone to measure.**
- **§7 dose-banding arithmetic:** HIGH in the computation — it reproduces `p3-feasibility.md`
  §2.2 exactly; MODERATE in the inputs, inherited from that report.
- **§3.1 niacin and §6.6 linoleic acid:** **data-backed**, from
  `data/processed-blinded-diabetic-retinopathy/pubchem_phytochem_target_interactions.csv`. But
  these are CTD **expression-level** rows, not binding or engagement, and the disease brief's
  warning applies: row count is not evidence weight. Treated as direction-incoherence and
  wrong-sign *flags*, not as proof.
- **Everything else: knowledge-based.** Consistent with the consensus report's finding that the
  project contains no drug-target affinity data and no measured pharmacokinetics. I confirmed
  this independently: `chembl_drug_mechanisms.csv` (11 lines), `chembl_drug_targets.csv` (44),
  `chembl_bioactivities.csv` (24), `drugbank_drug_targets.csv` (19), `ttd_drug_target_genes.csv`
  (4) in the blinded tree are near-empty test extracts with no LXR, ABCA1, APOA1 or CYP46A1
  content. **No combination claim in this report is or could be supported by a drug→target edge
  in this project's data.**
- **Nothing scores 7+**, consistent with the ranker's discipline: a 7 requires a falsifier I can
  state and expect to survive, and the top combination's second component is preclinical.
- **Research disclaimer.** Computational multi-agent analysis. Nothing here is a clinical
  recommendation. Every combination requires experimental validation in combination assays, not
  inference from single-agent data.

---

## 11. BLINDING COMPLIANCE STATEMENT

**Files read, in full or in part:**
- `disease-brief.md` (full), `consensus-report.md` (full), `round2-synthesis.md` (full),
  `debate-summary.md` (full)
- `agents/p3-ranker.md` §6–8, `agents/p3-feasibility.md` §2, §8
- `agents/p2-pathway.md` §2–4, §7
- `.claude/skills/combination-designer/SKILL.md` (full), root and project `CLAUDE.md`
- Project data: **only** from `data/processed-blinded-diabetic-retinopathy/` —
  `pubchem_phytochem_target_interactions.csv` (queried for ABCA1/ABCG1/NR1H2/NR1H3/APOA1/CYP46A1
  rows) and line counts / header greps on the ChEMBL, DrugBank and TTD extracts.
- `evidence/` pack: grep counts only.

**Files deliberately NOT read:**
- `agents/UNBLINDING-part-b.md` — not opened.
- `data/processed/chembl_approved_drugs.csv`, anything under `data/holdout/`, any `answer-key*`
  file — not opened.
- **`data-quality-findings.md` — not opened at all.** The team lead's instruction identified §17b
  and §19 as the record of a blinding breach. I judged that reading the record of a leak is a
  route to the leak, and chose not to open the file rather than read around it. I therefore
  cannot cite its defect numbering directly and have relied on the summaries in
  `consensus-report.md` and `round2-synthesis.md`, which characterise the defects without
  restating any indication status.
- I did not use git history, git objects, or any other route to recover redacted values, and did
  not attempt to identify which rows were redacted.

**Residual-contamination disclosure, honestly:**
1. I read `agents/p3-ranker.md` and `agents/p3-feasibility.md`, which `consensus-report.md`
   states were **"not cleanly blinded."** I found no statement in the sections I read asserting
   any candidate's DR or DME indication, approval, guideline or trial status. The non-DR clinical
   facts I relied on from them (pemafibrate's cardiovascular outcome programme in statin-treated
   diabetics; elafibranor's weight-gain signal in its named non-DR indication; the DMF PML and
   lymphopenia profile; the fibrate–statin myopathy ratio) are explicitly permitted under brief
   §1.3 and are each labelled as non-DR in the source.
2. The ranker gates icosapent ethyl on *"a null large ω-3 RCT in a chronic progressive retinal
   disease."* That is a retinal-disease trial fact. I cited it as the ranker's gate (§6.6), did
   **not** attempt to identify which disease or trial it refers to, and **it is not load-bearing**
   — my IPE deferral rests independently on the bleeding/vitreous-haemorrhage endpoint conflict,
   the AF signal, and the linoleic-acid ABCA1 data.
3. **My anchor component is a fibrate, and I am aware from training that this class has
   DR-specific clinical evidence.** I did not use it. The anchor choice is inherited from
   `p3-ranker.md`'s ordering, which the team lead instructed me to build on rather than
   re-derive, and **every combination argument in this report is indifferent to which supply
   agent occupies the anchor slot** — §1, §4.2, §4.3, §6 and §7 are arguments about `J`, `c`,
   `u`, `e`, elimination route and compartment, and would read identically with any
   remnant-lowering agent in that position. §4.1 is the one exception and it turns on the
   fibrate's *subfraction remodelling* pharmacology, which is general lipidology.

**Negative decisions disclosed, as brief §1.5 requires.** I excluded **niacin** (§3.1) on four
grounds: direction-incoherent ABCA1 rows in the project's own CTD data including a wrong-signed
HCAR2-mediated row; the mature-HDL-versus-pre-β-ApoA1 species mismatch; HbA1c worsening in
diabetics; and flushing-driven unblinding. I excluded **CETP inhibitors** on the same species
mismatch. I excluded **low-dose efavirenz** (§3, row 7) on CYP induction, neuropsychiatric
effects, teratogenicity and cell-type distribution. I excluded **icosapent ethyl** per (2) above.
**None of these exclusions used, or required, any candidate's DR or DME indication status.** Each
rests on general pharmacology, on the disease model's own physiology, or on the project's blinded
data.

**Statement:** I did not use, assert, or rely on the DR/DME indication, approval,
guideline-recommendation or trial status of any compound at any point in this analysis. The
combination logic stands on pharmacology, compartment physiology and kinetics alone, as
instructed.

---

## SCOREBLOCK

SCORE|Fenofibric acid + local ApoA1-mimetic peptide (oral supply x intravitreal acceptor)|6.0|low|knowledge-based|True numerator-denominator pair; delivery solved; partner preclinical, extracellular-removal term unmeasured
SCORE|Fenofibric acid + inclisiran (remodel-then-clear)|5.0|moderate|knowledge-based|Buildable today, subfraction-coupled; adds no module or stage; breaks generic deployment economics
SCORE|Fenofibric acid + LXR-beta-biased partial modulator|3.5|low|knowledge-based|Right mechanism, two synergy legs; component nonexistent, NCE cost ten times programme budget
SCORE|Fenofibric acid + dimethyl fumarate (supply x modification)|2.5|moderate|knowledge-based|Network structure correct; DMF RED, stacked lifelong monitoring, GAPDH wrong-sign risk
SCORE|Fenofibric acid + candesartan|2.5|moderate|knowledge-based|Not a combination; already background therapy, or contraindicated dual RAS blockade
SCORE|Fenofibric acid + ezetimibe|1.5|high|mixed|Redundant afferent term, opposing subfraction effects, destroys the mechanism-discriminating comparator
SCORE|Fibrate + statin intensification|1.5|high|knowledge-based|Not a combination; shrinks measurable increment in both arms, stacks myopathy under neuropathic masking
SCORE|Any supply agent + scavenger-receptor blockade|1.0|moderate|knowledge-based|Wrong-signed: foam-cell burden unchanged, cytotoxic extracellular pool rises, worst where efflux suppressed
