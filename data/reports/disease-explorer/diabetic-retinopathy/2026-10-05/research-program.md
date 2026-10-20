# Preclinical Research Programme — PPARα and the Retinal Lipid Axis in Diabetic Retinopathy
Derived from an 16-agent blinded analysis, 2026-10-05. Experimental agenda, 2026-10-19.

**What this document is.** The pipeline's forward-looking output, stated as a research
programme rather than a development plan. Every experiment below was specified by a named
agent during the run; this document collects, sequences and costs them, and says what each
one decides.

**The organising fact.** This target has **one measurement standing between it and a
decision**, and that measurement has never been made. Everything else in the programme is
sequenced behind it.

---

## 0. THE SCIENTIFIC QUESTION, STATED PRECISELY

PPARα agonism is associated with benefit in diabetic retinopathy. **The mechanism is
unresolved, and the four candidate mechanisms imply different experiments, different
molecules and different disease stages.**

| Limb | Site of drug action | Site of biological effect | Engagement | Requires barrier crossing? |
|---|---|---|---|---|
| **1** | Hepatocyte | Plasma lipoprotein composition → retina | **Certain** (OATP1B concentrates fibrates 10–100× in liver) | No |
| **2** | Hepatocyte | FGF21 → FGFR1c/β-Klotho on retinal endothelium, luminal side | **Certain upstream**; downstream unquantified | No |
| **3** | Retinal endothelium / RPE | NF-κB transrepression → ICAM1↓ → leukostasis↓ | **Marginal** (−3.0 to −1.1 log vs free EC50) | One membrane, not the barrier |
| **4** | Neural retina | PPRE-driven fatty-acid-oxidation genes | **Absent** at achievable occupancy | Yes — and unreachable |

**Limb 4 is excluded on arithmetic**: the free-drug partition ratio cannot exceed 1, so even
complete barrier failure leaves fenofibric acid 10–100× below its free EC50 in neural retina.
It does not arrive late; it never arrives.

**Limbs 1–3 are live and mutually distinguishable by experiment.** The programme below
distinguishes them.

---

## 1. THE CRITICAL-PATH MEASUREMENT

> **Free fibrate concentration in retinal tissue, and the receptor occupancy it implies.**

Three mutually exclusive programmes hang on this single number, and **no measurement of it
exists in any species.** Every quantitative claim in this entire analysis — the exposure
objection, the compartment correction, the potency-versus-access argument, the ANGPTL4
demotion — is a calculation built on estimated partition ratios, not a measurement.

**Three routes, in order of practicality:**

| Route | What it gives | Feasibility |
|---|---|---|
| **Human aqueous humour at routine cataract surgery**, patients on chronic fibrate | Bounds the problem. Aqueous is not retinal interstitium, but it is obtainable from routine surgery at negligible added risk | **Highest. Do this first.** |
| Chronic-dosed rodent, retinal free-drug by microdialysis or tissue-binding-corrected homogenate | Direct partition ratio in a diseased eye | Moderate; requires method development |
| Large-animal microdialysis or PET | Definitive | Expensive, slow |

**Pair the aqueous tap with aqueous ANGPTL4 in the same sample — two of the run's three
central unknowns from one draw.** No published study has stratified intraocular ANGPTL4 by
fibrate exposure, despite banked samples of exactly this kind existing.

---

## 2. GATE 0 — THE EXPERIMENT THAT DECIDES WHETHER THERE IS A RETINAL TARGET

**Chronic oral fibrate in a diabetic rodent, reading transactivation against transrepression.**

| | |
|---|---|
| **Cost** | ~$50–150k |
| **Duration** | 6–9 months |
| **Decides** | Whether limb 3 exists at all, and whether limb 4 is as dead as the arithmetic says |

**Readouts, paired by mechanism:**
- **Transactivation (PPRE-driven):** retinal CPT1A, ACOX1, HMGCS2, **ANGPTL4**
- **Transrepression (PPRE-independent):** retinal ICAM1, TNF, IL6, and leukostasis by
  adherent-leukocyte count

**Interpretation, stated in advance:**

| Result | Conclusion |
|---|---|
| Transrepression **down**, transactivation **flat** | **Confirms the pharmacokinetically dissociated-ligand model.** At achievable retinal occupancy the retina sees anti-inflammatory transrepression without metabolic transactivation — and therefore without ANGPTL4 induction. Limb 3 is real and the wrong-sign risk is structurally absent |
| Transactivation **robustly up** | The low-occupancy model is wrong, the ANGPTL4 risk is live, and the dissociated-ligand synthesis collapses |
| **Both flat** | No retinal target. The programme is limb 1/2 only, and every retina-penetrant chemistry effort is unjustified |

**Two arms the original specification omitted, without which this is cheap and *indecisive*:**

1. **A `Ppara-/-` arm.** Without it, a positive result cannot be attributed to the receptor —
   fenofibrate has documented PPARα-*independent* effects, and much of the supporting in vitro
   literature uses 25–100 µM without knockout or antagonist controls, above the threshold where
   those off-target effects appear.
2. **A matched non-PPAR lipid-lowering arm.** Without it, a positive result cannot be
   distinguished from "any lipid lowering would have done this."

**This is the single highest-value experiment in the programme. It costs roughly 0.05% of the
medicinal-chemistry programme that is contingent on it.**

---

## 3. THE NECESSITY EXPERIMENT THAT HAS NEVER BEEN RUN

> **Cell-type-restricted conditional `Ppara` deletion in retina.**

**The gain-of-function arm is the only real pillar of the retina-intrinsic case**, and it is
thinner than it reads: sufficiency is not necessity; supraphysiological overexpression is the
wrong model for a partial-occupancy drug; the finding is concentrated in one laboratory
lineage; and the delivery vector is not inert.

The global knockout contributes almost nothing, because it carries hypertriglyceridaemia,
abolished ketogenesis and FGF21, hepatic steatosis and an altered diabetes response — so
"worse retinopathy" is fully explained by the *competing* systemic hypothesis. **Citing it for
the retinal limb is circular.**

**The conditional deletion — Müller-restricted, endothelium-restricted, RPE-restricted — is
the only experiment that establishes necessity. After roughly fifteen years of interest in
this target, its continued absence is itself informative.**

---

## 4. THE DISCRIMINATOR THAT NEEDS NO NEW EXPERIMENT

> **Does the retinal benefit track the lipid change?**

This is the cleanest available separator between limb 1 and limbs 2–3, it is a **covariate
analysis rather than a new study**, and it is answerable from data of a kind that is routinely
collected in any trial of a lipid-modifying agent with an ocular endpoint.

**If benefit does not track the lipid change, limb 1 is in trouble and the receptor hypothesis
strengthens.** If it tracks tightly, the receptor framing is largely decorative and the right
comparator set is the broader lipid-modifying armamentarium.

**If any existing dataset permits this analysis, it is worth more than everything else on this
list**, because it costs nothing and discriminates the run's two competing readings directly.

---

## 5. THE FGF21 CONCENTRATION BRIDGE — an unexamined gap under the best-evidenced limb

Limb 2 is credited on two findings that have never been placed on the same axis:

- **Upstream, human:** fibrates raise plasma FGF21.
- **Downstream, animal:** FGF21 protects retinal vasculature.

**Nobody has checked whether those are the same concentration.** The downstream work uses
pharmacological recombinant FGF21; a fibrate produces a modest physiological rise in the
endogenous hormone.

This is structurally identical to an error the pipeline caught twice elsewhere — a real effect
demonstrated at a dose the intervention cannot deliver. It was first identified in herbal
fatty acids, then in endogenous PPARα ligands already sitting at their own EC50, and finally
here, in the limb the evidence most favours.

**Experiment:** dose-response of plasma FGF21 at therapeutic fibrate doses in humans, read
against the concentration-response for FGF21 on retinal endothelial readouts. **This is the
one gap sitting directly under the mechanism the external evidence supports, and it is
checkable from existing samples and published concentration-response data.**

---

## 6. THE LIPID-CLEARANCE RATE CONSTANT — and why it changes how to read a null

The retinal lipid lesion is a **self-renewing cycle**, not a static deposit: modified
lipoprotein → scavenger-receptor uptake → transporter downregulated and acceptor scarce →
cholesterol cannot leave → inflammasome activation and foam-cell death → lipid re-released →
re-uptake.

Solving it as a two-compartment system gives foam-cell burden = influx ÷ clearance **exactly**
— the recycling rate cancels. **But as clearance approaches zero, the system has no steady
state; it integrates.** A supply-lowering agent then buys *delay*, not a bounded burden.

**Two consequences for experimental design:**

1. **Measure the clearance rate constant.** It determines whether the integrating regime
   applies, and therefore whether any supply-side monotherapy benefit is time-limited by
   construction.
2. **A stock measure and a flux measure are not interchangeable readouts.** Microaneurysm
   turnover is a flux measure. Hyperreflective-foci burden is a **stock** measure whose time
   constant is 1 ÷ clearance — the parameter this disease suppresses. **A stock readout can
   read flat at twelve months while the mechanism is working**, because the lesion is still
   draining on a longer clock. Any study powering on a stock measure must justify its
   observation window against the measured clearance rate, not calendar convenience.

---

## 7. THE CHEMISTRY QUESTION — tractable, and correctly deferred

**The structural finding:** PPARα's AF-2 cage is **all-donor** — Ser280, Tyr314, His440 and
Tyr464 each donate a hydrogen bond, so the ligand supplies only acceptors. The geometry
demands a **bidentate acceptor pair ~2.2–3.2 Å apart, not a formal negative charge.** Charge
is an acceptor-strength multiplier worth roughly 2.3–3.1 kcal/mol per contact — real, bounded,
affordable.

**The existence proof:** the neutral endogenous ligand oleoylethanolamide binds at ~120 nM
with **ligand efficiency 0.41 — higher than fenofibric acid (0.29) or pemafibrate (0.34).**
The neutral head pays no efficiency penalty.

**Why the chemical space is empty:** every PPARα indication has been hepatic, and for a
hepatic target high protein binding and transporter-mediated uptake are *features*. **Nobody
ever needed a PPARα ligand with a high free fraction.** The space is unexplored because it was
never commercially interesting, not because it is forbidden.

**Two bench experiments, cheap and parallel to Gate 0 (<$100k, 2–4 months):**
- Confirm the one genetic-dependency hit in the dataset by surface plasmon resonance or
  isothermal titration calorimetry, with antagonist reversal
- Measure transporter-mediated uptake of a model conjugate, and turnover of a lysolipid
  conjugate — the two routes that would deliver a neutral ligand

**The honest assessment of the full programme:** a real, ordinary, buildable medicinal
chemistry effort. The required moves — shrink the head group, shift or neutralise the pKa,
branch rather than extend, park polarity on the distal vector — are all standard. **What makes
it hard is that no assay cascade exists for the thing being optimised.** Nobody has ever run a
PPARα programme against *free-drug retinal exposure*, so the metrics, the models and the
translation are unbuilt. The cascade would need free-drug-corrected EC50, measured free
fraction, and measured partition ratio in a species with a comparable barrier — none of which
is standard practice.

**Probability of technical success to a retinal biomarker readout: 15–25%, conditional on Gate
0 reading positive.** Dominant risks in order: Gate 0 reads negative and there is no target;
maximal efficacy collapses with the neutral head; isoform selectivity cannot be achieved from
a neutral compact scaffold.

> **Verdict: tractable, and premature.** A ~$100k rodent experiment determines whether there
> is a retinal target at all. Committing to a multi-year chemistry programme before running it
> would be indefensible. **The chemistry's contribution is that it does not argue against
> running the experiment, and it establishes that if the experiment reads positive, the
> molecule is designable.**

---

## 8. THE UNCOVERED BIOLOGY — and the one bench experiment that opens it

**Every compound considered in this analysis — all 29 — reduces what *arrives* in the retina.
Not one accelerates what *leaves*.** The reverse-cholesterol-transport arm is the single
largest uncovered module, and it sits inside the run's own declared thesis.

**The fibrates do not secretly cover it.** Transporter induction is PPRE-driven — the same
limb shown absent at achievable retinal occupancy — and it is a two-step relay, so it is
*more* sensitive to that shortfall, not less. The one reachable limb raises circulating
acceptor, which addresses the **acceptor** half while the diabetic lesion sits on the
**transporter** half, and it raises mature HDL when the transporter's actual substrate is
lipid-poor pre-β ApoA1.

**The modelling result that reorders the options.** Adding a direct extracellular-removal term
keeps burden finite **even at zero transporter activity**; a transporter inducer multiplies a
term that may already be near zero. **So the right intervention is an extracellular acceptor
or scavenger, not primarily a transporter inducer** — which reverses the preference ordering
the analysis had been carrying.

**The deciding bench experiment, cheap and never specified by anyone:**

> In a diabetic retinal explant or foam-cell model **with the efflux transporter silenced**,
> does an ApoA1-mimetic peptide still reduce extracellular modified-lipoprotein mass?
>
> **If yes**, direct extracellular removal is real, the acceptor route stands, and it is the
> best complement to supply-lowering available. **If no**, the peptide acts only as a
> transporter substrate, and supplying acceptor to a cell whose pump is downregulated does not
> unload it.

**One structural advantage worth noting:** the PPARα pocket mandates a lipophilic acid, which
is what couples potency to hepatoselectivity. **The LXR pocket does not — its ligands are
neutral.** Ionisation is not structurally locked in for that target, so a retina-penetrant
modulator aimed at the efflux arm is chemically conceivable in a way a retina-penetrant PPARα
agonist is not. The caveat is severe: systemic agonism of that target has repeatedly failed on
hepatic steatosis and hypertriglyceridaemia, so isoform selectivity or tissue restriction is
the entire problem.

---

## 9. SEQUENCED PROGRAMME

| # | Experiment | Cost | Time | What it decides |
|---|---|---|---|---|
| **1** | **Covariate analysis: does benefit track lipid change?** | ~$0 | weeks | Limb 1 versus limbs 2–3. **Run first — it is free** |
| **2** | **Human aqueous fibrate concentration + aqueous ANGPTL4**, same tap, at routine cataract surgery | ~$50–100k | 6–12 mo | Bounds the critical-path unknown; settles the wrong-sign question empirically |
| **3** | **Gate 0 rodent study**, with `Ppara-/-` and matched non-PPAR lipid arms | ~$150–250k | 6–9 mo | Whether a retinal target exists at all |
| **4** | **FGF21 concentration bridge** | ~$50k | 6 mo | Whether the best-evidenced limb closes quantitatively |
| **5** | **ApoA1-mimetic explant study**, transporter silenced | ~$75k | 6 mo | Whether the uncovered module is addressable |
| **6** | **Clearance rate constant** in a diabetic model | ~$75k | 6 mo | Whether benefit is bounded or merely delayed; sets every observation window downstream |
| 7 | Bench chemistry: binding confirmation, conjugate uptake | <$100k | 2–4 mo | Whether a neutral chemotype has a delivery route |
| 8 | **Conditional retinal `Ppara` deletion** | $300–500k | 18–24 mo | **Necessity.** The experiment the field has never run |

**Total for items 1–7: roughly $500–650k over 12–18 months**, and they collectively decide
which of three mutually exclusive programmes to run. Item 8 is the definitive necessity
experiment and is worth commissioning in parallel if the target is being taken seriously.

---

## 10. WHAT WOULD END THE PROGRAMME

- **Gate 0 flat on both readouts** with confirmed systemic exposure → no retinal target;
  continue only as a systemic lipid programme, and the receptor framing is decorative.
- **A matched non-PPAR lipid-lowering arm reproduces the effect** → the receptor is not the
  agent of action. Keep the programme, abandon the target.
- **`Ppara-/-` fails to abolish the effect** → the receptor is not mediating it.
- **Benefit tracks lipid change tightly** → this is a lipoprotein hypothesis, and far more
  potent apoB-lowering agents exist than any fibrate.
- **Robust retinal transactivation with ANGPTL4 induction** → the wrong-sign limb is live, and
  the risk–benefit must be re-derived stage by stage before any chronic exposure.

---

## 11. CONFIDENCE

**Every quantitative claim in this programme is knowledge-based.** The source project contains
no drug–target affinity data, no measured pharmacokinetics (distribution, permeability and
bioavailability columns are empty across all 3,276 drug records), no gene–disease associations
for this indication, and a target panel containing all three PPAR receptors and **not one PPAR
effector gene** — so the pathway under study is invisible to the data that was used to study
it.

**That is the strongest argument for this programme's shape.** The analysis is at the limit of
what reasoning from mechanism can deliver, and the next increment comes from measurement, not
from further analysis. **One rodent study and one aqueous tap would contribute more than the
16 agents that produced this document.**
