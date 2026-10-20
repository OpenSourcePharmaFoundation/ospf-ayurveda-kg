# Debate Integrator — Diabetic Retinopathy (BLINDED RUN)
Agent: Integration Specialist · Phase 3 (Debate) · 2026-10-05
Axis: **synthesis** — conflict resolution, evidence weighting, and the strongest defensible
position. Not a scoring agent; I file no SCOREBLOCK.

**Inputs read:** `disease-brief.md` · `round1-synthesis.md` · `round1-score-matrix.txt` ·
`round2-score-matrix.txt` · `data-quality-findings.md` (§1–17) · `agents/p2-pathway.md` ·
`agents/p2-safety.md` · `agents/p2-repurpose.md` · `agents/p2-sar.md` ·
`agents/p2-literature.md` **Part A only** (compliance statement at §9).

---

## 0. THE ONE-PARAGRAPH POSITION

The run has been asking the wrong question for two rounds, and the Phase 2 agents have between
them supplied the right one without quite assembling it. The question is not *"can a PPARα
agonist engage the retina?"* — three independent lines of work (chemistry, drug-space search,
pharmacokinetics) now agree it cannot, with any molecule that currently exists. The question is
**which compartment the therapeutic claim lives in**, and the answer is that there are *four*
compartments, not two: neural retina (dead), retinal endothelium/RPE (marginal and unmeasured),
hepatocyte (certain), and — the one nobody counted — **plasma**, where two humoral relays
(FGF21, protective; ANGPTL4, potentially harmful) act on retinal endothelium from the luminal
side and for which the exposure term does not appear in the equation at all. The defensible
programme is built entirely on the compartments where engagement is certain, is stated as a
**remnant/apoC-III hypothesis rather than a receptor hypothesis**, is stage-restricted to
S1–S3, is powered on a vascular rather than a neural endpoint, and is **invariant to the value
of retinal K<sub>p,uu</sub>** — the single unmeasured number on which three mutually exclusive
readings of this run depend. The retinal limb is carried as a free option that a $250–400k
five-arm rodent experiment either converts into a programme or kills. That is a smaller claim
than the run opened with and it is the only one that survives the attacks assembled below.

---

# PART I — RESOLVING THE CONFLICTS

## 1. THE EXPOSURE QUESTION, WHICH REVERSED TWICE

### 1.1 Why it reversed twice: the three positions are not about the same thing

The apparent double-reversal dissolves once you notice the three claims answer three different
questions. Laying them side by side is most of the resolution:

| Position | Actual claim | Scope | Status |
|---|---|---|---|
| **Phase 0 scout** | free fenofibric acid sits ~2 log₁₀ below PPARα EC50; retina has no uptake transporter | one molecule, whole retina, aggregate | **Arithmetically wrong by ~1 log, directionally right** |
| **Round 1 ADMET** | the gap is ~1 log, and the retina is not one compartment: endothelial/RPE K<sub>p,uu</sub> 0.2–0.7 vs 0.01–0.15 neural | one molecule, **compartment-resolved** | **Holds. The load-bearing correction of the run.** |
| **Phase 2 SAR** | the acid is not mechanistically mandatory; the AF-2 cage is all-donor and wants a bidentate *acceptor pair*, not a charge; OEA achieves LE 0.41 vs fenofibric acid 0.29 | **the chemotype, not any existing molecule** | **Holds — and does not touch the exposure of any available drug** |

The scout's error is conceded by everyone and is specific: it compared *free* plasma against a
*nominal* EC50 measured in serum-containing medium where the ligand is itself protein-bound.
Correcting both sides to free drug recovers 0.5–1.5 log. **Direction unchanged, magnitude wrong.**

The SAR finding is the one being misread as a third reversal, and it is not one. Its own §2.3
says so explicitly: going neutral recovers the **ionisation** term (~4 logs of permeant
fraction), the **anion-efflux** term (MRP/BCRP) and the **OATP1B hepatic-sink** term — but it
does **not** recover `fu`, because PPARα is a fatty-acid sensor with a 1,300–1,400 Å³ hydrophobic
cavity, potency there is bought by burying hydrophobic surface, and OEA is neutral and still
~99% bound. Three of four terms, not four. The fourth has to be designed against separately, by
holding logD ≤ 3.3 through the potency climb — which the SAR agent itself names as "the
programme's central difficulty."

> **So the SAR agent did not reverse the exposure conclusion. It severed a different link.**
> Round 1 argued: potency and access are anti-correlated → therefore no molecule can test the
> retinal limb → therefore the retinal hypothesis is untestable and the target is a dead end.
> The SAR agent shows the anti-correlation is a property of the **series that was built**, not
> of the **receptor** — PPARα's indications were all hepatic, and for a hepatic target high PPB
> and OATP1B uptake are *features*, so nobody ever needed a high-free-fraction PPARα ligand.
> The chemical space is empty for commercial reasons, not physical ones.

### 1.2 Resolution by compartment — the defensible position

**Retinal exposure is not one number and treating it as one is the error that generated the
whole dispute.** Stated as four claims with four different confidence levels:

| Compartment | Est. K<sub>p,uu</sub> | Fenofibric acid free conc. vs free-corrected EC50 | Verdict |
|---|---|---|---|
| **Neural retina** | 0.01–0.15 | 1–3 logs short | **DEAD.** Not a late-arrival problem — it never arrives. No correction rescues it. |
| **Inner-BRB endothelium / choriocapillaris-facing RPE** | 0.2–0.7 | ~0.5–1.5 logs short | **MARGINAL, UNMEASURED, NOT EXCLUDED.** These pools sit on the blood side of the tight junction — one membrane, not a barrier. |
| **Hepatocyte** | concentrative, 10–100× | far above | **CERTAIN.** Not in dispute by any agent in either round. |
| **Plasma** | **term does not apply** | n/a | **CERTAIN, and this is the compartment the run did not count — see §2.** |

**And the position has to be stated with its honest epistemic status, because the Devil's
Advocate is entitled to it:** the Literature agent is right that retinal K<sub>p,uu</sub> is
*the* unmeasured quantity, that three mutually exclusive programmes hang on it, and that no
amount of further reasoning substitutes for measuring it. At 0.01–0.05 there is no retinal limb
of any kind and the receptor is a red herring. At 0.2–0.5 with ICAM-1 threshold amplification
an endothelial anti-inflammatory limb is real — **and the ANGPTL4 flag must be reinstated at
S4–S5**, because the same occupancy that permits transrepression begins to permit
transactivation. Above that, the entire exposure objection that organised this run was wrong.

> **The defensible position is therefore not a point estimate of K<sub>p,uu</sub>. It is a
> design rule: build nothing that requires K<sub>p,uu</sub> > 0.2, and build something whose
> value is unchanged if K<sub>p,uu</sub> = 0.** That is achievable, and §7 is what it looks like.

### 1.3 The argument that settles it at the population level, which is not a chemistry argument

The Safety agent supplied an independent line that I think is underweighted and that I elevate
here, because it converts the exposure question from a chemistry dispute into an epidemiological
one that no medicinal chemistry can fix:

- The **hepatic/systemic limb** is transporter-mediated, concentrative and **saturable** — its
  dose–response for remnant lowering is relatively flat at the top of the curve, so a 3-fold
  dose reduction costs it proportionally little.
- The **retinal limb** is passive and **linear in free plasma concentration** — a 3-fold dose
  reduction costs it the full 3-fold.
- In a CKD-dominant population, ~1/3 of patients are dose-banded ~3-fold and 5–10% excluded
  outright. Retinopathy and nephropathy are the same microvascular disease in two organs and
  **they track together.**
- Nephrotic-range proteinuria, common here, *raises* free fraction in those same patients
  (99.0% → 98.0% bound doubles free drug) — a second, opposing amplifier in the same people.

> **CKD dose-banding selectively amputates the retinal limb while largely sparing the systemic
> one, in exactly the patients with the most disease.** If the mechanism is systemic, banding is
> a nuisance. If it is retina-intrinsic, banding is close to fatal — and it is not fixable by
> picking a better molecule within the approved set. Pemafibrate escapes it (hepatobiliary), but
> pemafibrate is the molecule that *least* tests the retinal limb. The trap closes from both sides.

### 1.4 What I am therefore willing to assert, and what I am not

**Assert:** oral fibrate dosing achieves certain hepatic engagement, certain plasma-compartment
presence, a marginal and unmeasured endothelial/RPE occupancy that is plausibly in the
threshold-amplification range for ICAM-1 but is not demonstrated, and no neural-retinal
engagement at all. **The acid is not mechanistically mandatory for PPARα, but no non-acidic
PPARα ligand exists as a drug** — a claim now established twice independently, from chemistry
(SAR §1–2) and from an exhaustive drug-space search (Repurposing §1, approved + late-stage +
discontinued + endogenous + retinal-delivery space; "the two sets do not intersect").

**Decline to assert:** any number for retinal K<sub>p,uu</sub>; that transrepression occurs in
human retina at achievable exposure; that the retina-intrinsic hypothesis is *false* (it is
**untested**, which is a different and more honest word than Round 1's framing).

---

## 2. THE MECHANISM SPLIT — NOT EITHER/OR, AND THE DICHOTOMY IS ITSELF THE ERROR

### 2.1 The framing error

The conflict is posed as *hepatic/systemic lipoprotein lowering* **versus** *retinal
endothelial/RPE engagement*, with the Pathway agent's sharp formulation that "PPARα has an
engagement-certain compartment that is not the diseased one."

That formulation is correct and **incomplete**, and the completion changes the answer. It
assumes a drug affects a tissue only by *entering* it. Two of the four limbs below violate that
assumption, and one of them is the best-evidenced thing in the entire run.

### 2.2 The four limbs, ranked by (evidence grade × engagement certainty)

| # | Limb | Compartment | Engagement | Evidence grade (Part A) | Barrier crossing needed? |
|---|---|---|---|---|---|
| **1** | Hepatic PPARα → APOC3↓ / LPL↑ / APOA5↑ → TG-rich remnant & apoB particle number ↓ → less apoB flux across a leaky barrier | liver → plasma | **CERTAIN** | **1b–2a human PD for the proximal chain**; weak link is supply→lesion | **No** |
| **2** | Hepatic PPARα → **FGF21↑** (canonical PPRE target, abolished in `Ppara-/-`, fibrate raises circulating FGF21 in humans) → FGFR1c/β-Klotho on retinal endothelium **from the luminal side** | liver → plasma → luminal endothelium | **CERTAIN upstream** | 2b human PD + Level 4 retinal terminus **independently replicated by labs with no stake in the PPARα-retina lineage** | **No** |
| **3** | Retinal endothelial/RPE transrepression of NF-κB → ICAM1↓ → leukostasis ↓ | endothelium/RPE | **MARGINAL, unmeasured** | **Level 5/6, LOW**, with high-quality negative class-translational evidence against (§5) | Yes, partially |
| **4** | Retinal FAO transactivation (CPT1A/ACOX1/HMGCS2) | neural retina / RPE | **ABSENT at achievable occupancy** | Level 4/5 LOW for the drug-driven version; **no clean demonstration that oral fibrate induces retinal FAO genes exists** | Yes, fully |

**Limb 2 is the finding that dissolves the dichotomy, and I am endorsing the Literature agent's
emphasis on it in full.** It is the only proposed mechanism in this run where the upstream
pharmacology is human-proven, the downstream retinal biology is animal-proven by *independent*
laboratories, **and no barrier crossing by the drug is required at any point**. A two-step chain
with independent evidence at each end is epistemically stronger than a one-step chain with weak
evidence, even though it is longer. Round 1 noticed FGF21 and filed it as a bonus row. On
evidence grounds it is arguably the **primary** retinal mechanism of systemic PPARα agonism.

> **The reframe:** the hepatic compartment is not merely where the drug *goes*. It is a
> legitimate **site of action on the retina**, via humoral relays that use the bloodstream as
> the delivery vehicle. "Wrong compartment" becomes "right compartment, indirect route." The
> either/or collapses because limbs 1 and 2 are *systemic in pharmacokinetics and retinal in
> pharmacology*.

### 2.3 The symmetry I am obliged to accept with it

The same logic that makes FGF21 the strongest limb makes **circulating hepatic ANGPTL4** the
surviving wrong-sign risk — induced in the compartment where engagement is certain, acting on
retinal endothelium from the luminal side, needing no barrier crossing. **You cannot accept one
and dismiss the other.** I accept both.

Three independent arguments bound the ANGPTL4 risk, and two of them are new since Round 1:
1. **Shared machinery** (Round 1/Target Analyst): retinal PPRE-driven induction requires the same
   occupancy the exposure objection says is unavailable. Self-cancelling for the *retinal* route.
2. **HIF dominance** (Literature A4.2): in ischemic retina — the disease-relevant condition —
   ANGPTL4 induction tracks hypoxia and HIF-1α, not PPAR or lipid status. A PPARα agonist does
   not supply that transcriptional input.
3. **LPL bounding** (Literature A4.4, and this is the cleanest): ANGPTL4 is a physiological LPL
   inhibitor. If fibrates induced it to a functionally large degree, the predicted net plasma TG
   movement would be **upward**. The observed human effect is a large, reliable **downward**
   movement. Therefore ANGPTL4 induction at human-tolerated exposure is functionally subordinate
   to the concurrent LPL induction and apoC-III suppression. **The magnitude of real-world
   ANGPTL4 induction is bounded above by the observed TG lowering.**

And the operational consequence is a gift rather than a burden: **the programme's two most
important mechanistic quantities — FGF21 and ANGPTL4 — are both plasma biomarkers, measurable
in any trial for near-zero marginal cost.** Both become mandatory pre-specified readouts.
Note the Repurposing agent's demerit, which I accept: the hepatic-ANGPTL4 route is **worst for
the most hepatoselective agent**, i.e. pemafibrate. That is measurable, not arguable, and §7
builds the measurement in.

### 2.4 Is the conflict a feature?

**In one specific sense, yes, and in another, no.**

Yes: a fibrate is a single molecule that delivers a **certain** systemic mechanism and a **free
option** on a marginal retinal one. You pay for the first and the second arrives at zero
marginal cost.

No: the error — and it is the error that produced two rounds of unresolvable argument — is to
**price the lottery ticket into the decision**. The programme must be justified entirely by
limbs 1 + 2. Limb 3 is upside that the trial is designed to *detect* but is not powered to
*require*, and limb 4 is the one whose positive result would be bad news (it reinstates ANGPTL4
and means the exposure model is wrong).

---

## 3. PEMAFIBRATE vs FENOFIBRIC ACID — THE TIE IS AN ARTIFACT, AND THE CHOICE IS A SEQUENCING DECISION

### 3.1 First, kill the tie

They tie at 6.10 (Round 1) and 5.80 (Round 2) from opposite directions, and both ties are
artifacts of averaging orthogonal axes — the error the Round 1 synthesis, the Pathway agent
(§9), the SAR agent (§10) and the Clinical agent all explicitly warned against. The round-2
spread tells the story the mean conceals: pemafibrate spread **5.0** (pathway 7.0 vs SAR 2.0),
fenofibric acid spread **3.0**. These are not interchangeable molecules and no composite exists.

### 3.2 Is the choice between molecules or between mechanisms? — **Between mechanisms, and that
makes the molecule choice a consequence rather than a decision.**

| If the mechanism is... | Then... |
|---|---|
| **Systemic remnant lowering (limbs 1+2)** | Hepatoselectivity is a **feature**, not a bug. CKD-robustness is decisive in a CKD-dominant population. Remnant/apoC-III lowering is the right particle metric, and pemafibrate's is the largest in the class. **Pemafibrate wins on every axis that matters**, and its retinal-exposure weakness is simply irrelevant because the mechanism does not use that compartment. |
| **Retinal engagement (limb 3)** | Pemafibrate is *uninterpretable* (Safety §7.5: "the right drug if the mechanism is systemic, and an uninterpretable one if it is retinal"). **But fenofibric acid is 1–3 logs short and is equally uninterpretable.** Neither tests it. |

> **Therefore the molecule choice carries no information about the mechanism question, and the
> mechanism question does not select between the molecules.** The run has been treating this
> pair as a referendum on the central hypothesis. It is not one. What actually separates them is
> **deployability versus CKD safety**, which is a programme-design question.

### 3.3 Does the acyl-glucuronide/CKD convergence settle it? — **It settles the science, not the programme**

The Safety agent's §2.3 is, I think, the single best new finding in Phase 2, and it should be
stated in its strongest form: **fenofibric acid's acyl-glucuronide exoneration and its renal
problem are the same problem viewed twice.** The structural exoneration (Tier III, quaternary
α-carbon, zero α-hydrogens) was earned under *normal* renal clearance; the AG is not a terminal
metabolite but a reactive circulating species whose residence time, not just its intrinsic
reactivity, sets the integral of covalent adduct formation. In CKD it accumulates, migrates and
transacylates for longer, *and* hydrolyses back to parent creating a reservoir that raises
steady-state free drug — feeding the myopathy risk. Three liabilities, one population.

And they do not arrive alone. In the same patients: 3-fold dose-banding, hypoalbuminaemia
doubling free fraction, the creatinine rise driving an **iatrogenic prescribing cascade**
(metformin reduction/withdrawal, SGLT2i hesitancy, RAS-blocker down-titration — the last being
the most harmful, since it is the evidence-based renoprotective therapy) in patients who did not
actually lose filtration. The Safety agent is right that over decades this cascade is plausibly
the fibrate's *principal* renal harm, and right that it is **completely and cheaply preventable**
by making cystatin-C-based eGFR the sole renal decision variable.

Pemafibrate is immune to all of it: hepatobiliary elimination, 493× lower molar covalent burden,
minimal creatinine signal (so eGFR monitoring stays interpretable), PPARγ excluded with ~5–6 logs
of margin — uniquely valuable in a macular-edema-sensitive indication — and, at 0.4 mg/day,
plasma concentrations 2–3 logs below any DDI-perpetrator threshold, so it **cannot** drive a
statin interaction in a universally statin-treated population.

**But it does not settle the programme question,** because unmet need #8 is LMIC deployability
and pemafibrate is Japan-only, BID, not generic, with a limited Western chronic database. A drug
that is better for the 35% of patients with CKD and unavailable to 90% of the world's patients
is not self-evidently the better *programme*.

### 3.4 Resolution — the choice is false because they belong in different slots

> **Pemafibrate is the mechanism-validation molecule. Fenofibric acid is the deployment molecule.
> Run them in that order, in two separate trials.**

Trial 1 (registration/mechanism) uses **pemafibrate**: no dose-banding attenuation, no
population amputation, no creatinine confound and therefore no prescribing cascade and no renal
unblinding tell, cleanest PPARγ exclusion, no statin-myopathy perpetration, largest apoC-III
effect. You get an **unconfounded answer about the systemic limb**.

Trial 2 (public-health bridging), only if Trial 1 reads positive, asks the genuinely different
question: *does a cheap global generic reproduce the effect at an attenuated dose in a
CKD-banded population?* That is a far better question to ask **second** than first.

**Running fenofibric acid first conflates three questions** — does the mechanism work, does it
survive 3-fold dose-banding, and does the creatinine cascade harm patients — and a null result
cannot be assigned to any of them. The Repurposing agent's stated biggest concern is exactly
this: *"that the programme proceeds with fenofibrate because it is cheap, generates an ambiguous
result, and burns the hypothesis."* I endorse it without qualification. **Cheapness is a
feasibility property and carries no information about efficacy** (Literature A5.3 rule 4), and
the configuration "strong preclinical + good exposure + cheap generic + plausible mechanism" has
a demonstrably poor prior in chronic neuro-ophthalmic disease — which is the minocycline lesson
and the pipeline has not drawn it.

**Accepted cost of choosing pemafibrate:** its hepatoselectivity maximises the hepatic-ANGPTL4
limb, the one surviving wrong-sign route. Mitigation is already in the design — plasma ANGPTL4
as a mandatory pre-specified biomarker, S4/PDR excluded, and a prespecified safety stop on
excess progression to proliferative disease or centre-involving edema.

---

## 4. DIMETHYL FUMARATE — ADJUDICATED: the Safety agent is right, and for one of its three reasons

### 4.1 The 7.0 and the 2.5 are both correct and they describe two different products

The Disease agent's 7.0 is a *pathway × stage × compartment fit* score and it is well argued: DMF
reaches the NRF2 node, spans S0–S2, has the best BRB physicochemistry in the set, covers P8.2
(modification capacity) and P8.7 (peroxidation) — **the only candidate covering either** — and
its covalent cumulative KEAP1 alkylation is the one mechanism in the entire set that the
free-drug/EC50 arithmetic does not govern, because occupancy integrates exposure × time and
resets only by protein resynthesis. That exemption is genuine and no other candidate has it.

The Safety agent's 2.5 is a *chronic safety for asymptomatic lifelong prevention* score. The
round-2 mean of 4.5 is meaningless: **DMF is not a 4.5 candidate; it is a 7-biology /
2.5-deployability candidate, and those two numbers point at two different products.**

### 4.2 Which safety argument carries the weight — and which I would not rest on

I separate these deliberately, because a Devil's Advocate will attack the weakest and claim the
verdict with it.

- **The PML arithmetic (1.7×10⁻⁴/PY vs a 7.5×10⁻⁵/PY bar, ~2.3× over) — I would not rest here.**
  It is a `[CALC]` on a `[CALC]`: the §1.1 bar itself assumes an efficacy magnitude for which
  there is no evidence, and a 30-year extrapolation from 3–4 year MS data is uncertain in both
  directions. The Safety agent is admirably explicit that this is the case and even notes a
  utilitarian might accept the trade. It is supporting evidence, not the verdict.
- **The monitoring-translation argument (§1.3) — this is the decisive one and it is close to
  unattackable.** DMF's acceptable safety in MS is *manufactured* by three things: a specialist
  neurology service, quarterly CBCs, and a symptomatic patient who complies because they feel
  ill. Asymptomatic preventive care delivered through primary care at population scale has
  **none of them**. The real-world harm rate therefore exceeds the trial harm rate by a large,
  unmeasured factor, and trial safety data for such a drug systematically understates its
  population safety. This generalises beyond DMF: it is a statement about *what kind of drug can
  be a population preventive at all.* On this argument alone, DMF is out.
- **Serious infection, not PML, is the bigger quantitative harm** — chronic moderate lymphopenia
  in a diabetic population with elevated baseline infection risk (foot infections, UTIs,
  pneumonia, TB in endemic regions), biting hardest exactly where unmet need #8 points.
- **And a recalibration that cuts against the run's own instincts:** DMF delivers **10.7× the
  molar electrophile load of elafibranor** and is 2–3 further orders of magnitude more
  intrinsically reactive (a *trans*-bis-ester-activated alkene with no aryl delocalisation and no
  steric shielding, versus a doubly aryl-conjugated, *ortho,ortho*-dimethyl-shielded chalcone).
  **This run flagged the Michael acceptor on the wrong molecule.**

### 4.3 The GAPDH wrong-sign mechanism — real, unquantified, and its correct status is a required experiment

Two agents reached it independently (Pathway §5.2.3, Safety §7.1), which raises my confidence
that it is a genuine hypothesis rather than one agent's artifact.

**Why it must be taken seriously:** MMF succinates GAPDH at Cys152, inactivating it — this is
how DMF suppresses aerobic glycolysis in activated immune cells. The disease model's unifying
Brownlee hypothesis places **GAPDH inhibition at the centre**, backing up glycolytic
intermediates into the polyol, hexosamine, PKC and AGE branches. The retina is among the most
glycolytic tissues in the body, photoreceptors are obligately glycolytic, and the diabetic retina
is in a **pre-existing NADPH/GSH deficit** because the P1 polyol pathway consumes the NADPH
needed to regenerate GSH. So a fast, promiscuous thiol electrophile is dosed into a tissue with
compromised capacity to buffer it. **The hormetic window is plausibly narrower in diabetic retina
than anywhere this drug has ever been used.**

**Why I do not treat it as proven:** the immune-cell GAPDH effect occurs in cells with extreme
glycolytic flux and high local exposure; retinal MMF concentration is likely far lower; the
window may still be open.

**Verdict:** it converts "acts at the node" into "acts **near** the node, possibly in both
directions," and it demands a specific, cheap readout — **retinal GAPDH activity and
photoreceptor ERG a-wave under chronic MMF**, run alongside the NRF2 target panel.

Note that the headline claim was already half-demoted before safety arrived: the Pathway agent
shows DMF acts on the **disposal** arm, one step lateral to the node, and **SOD2 — the only
antioxidant enzyme positioned exactly at the node — is epigenetically silenced (H3K9me,
DNMT1-mediated) and is not NRF2-rescuable.** The single enzyme that would make "at the node"
true is the one the mechanism cannot restore.

### 4.4 Adjudication

> **The lexicographic gate multiplies; it does not average. 7.0 × 2.5 is low. Dimethyl fumarate
> is RED as a lifelong population preventive and is not in the portfolio.**
>
> **It is not worthless.** It is the best available **short-course mechanistic probe of the NRF2
> limb** — 12–24 weeks, monitored, specialist setting, with retinal biomarker readouts and with
> retinal GAPDH activity plus ERG a-wave as mandatory safety endpoints. That preserves the
> information content of the 7.0 without buying the 2.5. Its legitimate defence against the
> brief's "antioxidant alone" prior — that it is a *transcriptional* antioxidant inducing
> catalytic enzymes with turnover, not a *stoichiometric* scavenger consumed 1:1, which is what
> the failed vitamin trials deployed — is real and weakens that prior without discharging it.

---

## 5. THE DISSOCIATED-LIGAND DEMOTION — CORRECT, AND FOR A STRONGER REASON THAN THE SAR AGENT GAVE

The SAR agent demoted the chemist's "sharpest idea in the run" to a contingent follow-on. **Yes,
that is right.** Four independent arguments converge, and the SAR agent made two of them.

**1. Orthogonality (SAR §3.3, reason 1).** `occupancy ∝ fu × C_plasma × K_p,uu / EC50`. Bias
changes what the receptor does *once occupied*; it appears nowhere in that expression. The
retinal limb's problem is that occupancy is ~0.3%. **Designing bias does not move that number at
all.** Decisive on its own.

**2. Deletion (SAR §3.3, reason 2) — and it is worse than the SAR agent stated.** A
transrepression-biased ligand ablates the hepatic PPRE-driven limb in the one compartment where
engagement is certain. The SAR agent lists what is deleted: LPL↑, APOA1/APOA5↑, APOC3↓,
CPT1A/ACOX1/HMGCS2↑, **FGF21↑**. It does not notice that the last item is, per Literature Part A,
**the strongest-evidenced single limb in the entire run** (§2.2 above) — and FGF21 induction is
PPRE-driven, so bias engineering deletes it too. **The trade is not "delete the lipid limb to
purify a retinal one." It is "delete the lipid limb *and* the best-evidenced retinal-effect limb,
in order to manage a risk Round 1 already demoted and that a plasma assay already monitors."**
I add this as a reinforcement the SAR agent missed.

**3. The class translational record (Literature A3.2 obj. 3, SAR §3.2, reached independently).**
~25–30 years, two receptors, a dozen serious programmes, **zero systemic approvals**; the in vivo
therapeutic-index separation repeatedly proved far smaller than in vitro dose–response separation
predicted; the only dissociated molecules that reached patients did so **topically or inhaled** —
i.e. by solving delivery the hard way rather than by the dissociation. Round 1 cited the field's
*existence* as support. **The existence of a field is not evidence that its founding assumption
translates; here the field's outcome is evidence that it does not.** And `GRdim`, the canonical
mouse genetic support, was subsequently shown to retain substantial transactivation — the genetic
pillar is weaker now than when the field was founded.

**4. Two methodological defects Round 1 did not apply, and both bias in the same direction.**
   - **Contaminated in vitro base.** Most of the supporting "PPARα transrepresses at low
     concentration" literature uses fenofibrate/Wy-14643/gemfibrozil at 10–100 µM, above the
     concentrations at which these compounds exert documented **PPARα-independent** effects
     (direct NF-κB interference, AMPK activation, mitochondrial uncoupling, ER stress). Without a
     `Ppara-/-` cell or GW6471 reversal arm these experiments do not establish receptor mediation
     — and the bias direction makes transrepression look **more potent and more left-shifted than
     it is.**
   - **An isoform-discipline violation, and it is the sharpest correction in Phase 2.** Round 1's
     "catalytic / non-consumed receptor" argument (SUMO → NCoR clearance block) is a **PPARγ/LXR
     macrophage result** imported into a PPARα argument, in a run whose brief explicitly forbids
     transferring properties between PPAR isoforms. **Round 1 applied isoform discipline to
     liabilities (γ fluid retention) and then violated it in the benefit direction.** That
     asymmetry must be corrected on the record and I am correcting it here.

### 5.1 What survives, and must be carried forward

- **The ICAM-1 density-threshold amplification argument.** Two agents reached it independently
  (Literature A3.3; Pathway §6.2 point 5) and it does **not** depend on the occupancy differential
  at all. Firm leukocyte adhesion under shear requires multivalent bonding above a ligand-density
  threshold, so a modest fractional reduction in endothelial ICAM-1 can produce a
  disproportionately larger reduction in firm adhesion. Level 5, quality MODERATE. **This is the
  defensible version of the anti-inflammatory rationale and it should replace the occupancy
  version everywhere in the final report.**
- **The SAR agent's corollary, which I think is the most elegant line in Phase 2:** you get
  partial agonism *for free* anyway. Any neutral-head design is a partial agonist by construction
  (the Tyr464/H12 contact is the first casualty, and it is the contact that pays for AF-2 closure,
  so **efficacy degrades before affinity does**); any low-occupancy fibrate is already a
  *pharmacokinetically* dissociated ligand. **The retina sees a dissociated profile whether or not
  anyone designs one. Designing it costs an NCE and deletes the working limb; not designing it
  costs nothing.**

**Status: contingent follow-on.** Revisit only on one specific experimental result — Gate 0
showing robust retinal **transactivation**, which would simultaneously mean the exposure
objection collapsed and the ANGPTL4 risk went live. At that point bias engineering becomes
rational. Not before.

---

## 6. IS THE PPARα FRAMING CORRECT AT ALL? — PARTIALLY ABANDON IT, AND THE PROGRAMME GETS STRONGER

This is the most serious challenge in the debate and the one where conceding correctly is worth
more than defending.

### 6.1 Concede the strong form first

> **If the operative mechanism is apoB *mass* reduction, the PPARα framing is wrong, should be
> abandoned, and the right drug is not a fibrate.** A PCSK9 inhibitor lowers apoB 45–55% against a
> fibrate's 5–15% — three to five times more. That is a clean, falsifiable, uncomfortable
> prediction and the honest position is to state it rather than avoid it. On that reading the
> best agent is **inclisiran**: ~40–45% apoB reduction, outstanding chronic safety, no renal
> adjustment, no meaningful DDI, and **twice-yearly** dosing — the only administration schedule
> genuinely compatible with lifelong prophylaxis in asymptomatic people (unmet need #4).

A position that cannot name the conditions under which it is wrong is not defensible. Those
conditions are named in §8 as kill criteria K4–K6.

### 6.2 But apoB mass is not the mechanism the disease model specifies

The model's toxic species is the **small, dense, glycated-and-oxidised apoB particle retained in
the outer plexiform layer** — hard exudate is retained modified lipoprotein, not "fat." Three
facts make particle-vs-mass load-bearing rather than special pleading, and the third is a
mechanistic prediction with a measurement attached:

1. **Diabetic dyslipidaemia is a remnant and small-dense-LDL disorder in which LDL-C is frequently
   near-normal.** Lowering a normal number is not an intervention.
2. **Statins are near-universal background therapy at 35–45% apoB lowering.** Any trial measures
   the *increment over near-maximal apoB lowering already delivered to both arms*. Whatever a
   fibrate adds is, by construction, the **remnant/apoC-III component statins do not touch.**
   This is an argument about trial arithmetic rather than about biology, and it is the strongest
   of the three.
3. **The two agents may move the toxic subfraction in opposite directions while both "lowering
   apoB."** Ezetimibe lowers LDL-C chiefly by raising LDLR-mediated clearance — and **small dense
   LDL has reduced LDLR affinity and is preferentially retained.** Fibrates do the opposite: by
   lowering TG and reducing CETP-mediated remodelling they shift LDL from small-dense toward
   large-buoyant. (Pathway §8.2.)

### 6.3 Therefore: keep the receptor, demote the claim about it

> **The defensible framing is not "PPARα is the target." It is: the target is the
> remnant/apoC-III axis, and PPARα is currently the only approved, oral, generic,
> globally-deployable way to move it. The receptor is the *instrument*, not the *hypothesis*.**

That reframing survives every element of the attack:

| Attack | Response under the reframing |
|---|---|
| "PCSK9 lowers apoB 3–5× more" | Yes — and it lowers the wrong particle, additively to the particle statins already address. Power on remnant/apoC-III, not apoB mass. |
| "No non-acidic PPARα ligand exists as a drug" | True, confirmed twice independently — and **irrelevant** once the receptor is an instrument. We are not trying to build a better receptor ligand. |
| "Every pan/dual-PPAR agonist is an acid" | Same answer. |
| "The discontinued ones failed for liabilities this population tolerates worst" | **The strongest part of the attack, and it is a γ graveyard.** AleCardio (aleglitazar: heart failure, fracture, GI haemorrhage, renal dysfunction), muraglitazar (death/MI/stroke, oedema, heart failure), tesaglitazar (**creatinine rise and falling GFR** — the precise liability flagged as critical here), ragaglitazar (bladder tumours). **Every terminated agent carried γ.** The brief's mandated isoform discipline cuts *in favour of* keeping α-selective agents and killing the dual/pan lane entirely. I kill the lane: saroglitazar, chiglitazar, lanifibranor (pan-PPAR including γ, with weight gain and peripheral oedema in Ph2b — a direct hit on the macular-edema prior), elafibranor as a therapy. |
| "If the mechanism is apoB supply, the receptor is the wrong search" | Conceded for apoB *mass*. Rejected for *remnant particle*. And K4/K5 are the experiments that decide. |

### 6.4 What this concession costs, stated plainly

It concedes that the run's titular question — *"is PPARα a good DR target?"* — was the wrong
question, and that Phase 0 and Round 1 were spent answering it. The brief's §7 instruction
("score systemic lipid-lowering plausibility and anti-inflammatory transrepression as separate
axes from retinal PPARα occupancy") anticipated this correctly; the pipeline then spent most of
its effort on the third axis, which is the one with no achievable engagement and no human
evidence. **That is the single most useful correction this debate round can return.**

---

# PART II — THE CONSTRUCTIVE POSITION

## 7. (a) THE SINGLE MOST DEFENSIBLE RECOMMENDATION

> **Run a remnant / apoC-III-lowering programme in S1–S3 non-proliferative diabetic retinopathy,
> using pemafibrate as the mechanism-validation agent, powered on DRSS step-change and
> nonperfusion area rather than BCVA, with plasma FGF21 and plasma ANGPTL4 as mandatory
> pre-specified mechanistic biomarkers, and with the receptor explicitly demoted from hypothesis
> to instrument. Run Gate 0 (§9) in parallel for ~$250–400k to decide whether a retinal
> programme is ever started.**

**Ten conditions, each of which is a real constraint and not decoration:**

1. **The claim is about the remnant particle, not apoB mass.** Match and power on **apoB particle
   number AND NMR / ion-mobility subfraction distribution** — never on LDL-C. If apoB matches but
   the size distributions diverge, the exposure that matters is not matched and a null is
   uninterpretable.
2. **Stage-restrict to S1–S3. Exclude S4/PDR** (ANGPTL4 stage-restriction; and vitreous
   haemorrhage if any ω-3 arm is included).
3. **Not S0, and the brief must be corrected.** Unmet need #1 names the S0 preclinical window. A
   supply-lowering mechanism is **mechanically inoperative with an intact barrier** — there is no
   extravasation to prevent. The honest development target is **S1–S2**. Correspondingly, the
   "bootstrapping paradox" dissolves rather than bites: a leaky barrier is the *indication* for a
   supply-lowering mechanism, not an obstacle to it.
4. **Pre-specify the endpoint prediction, because it is falsifiable and because getting it wrong
   throws away a true positive.** The surviving retinal limb predicts a **DRSS / vascular effect
   without a matched BCVA / neural effect** (Pathway §6.2: leukostasis is a hub for the
   vascular-ischemic trajectory S2→S5 and a *branch* for the neuro-glial one). A trial powered on
   acuity will miss a real effect; a trial powered on acuity and finding nothing has **not**
   falsified the hypothesis. Fix this before enrolment.
5. **Three arms minimum. Two cannot answer the question.** A two-arm fibrate-vs-comparator null is
   irreducibly ambiguous between "neither works" and "both work equally" — which is precisely the
   question the comparator was added to settle. Active / matched non-PPAR remnant-lowering
   comparator / placebo.
6. **Firewalled unblinded safety team + blinded lipid panels.** The **lipid panel, not
   creatinine**, is the near-deterministic unblinding tell and it affects seven of sixteen
   candidates: a 40% TG fall with an HDL rise is effectively diagnostic of allocation at the
   individual-patient level. One firewalled physician/pharmacist with no role in endpoint
   assessment, rescue decisions or clinical management receives all lipid, renal and haematology
   values and issues only categorical instructions with no values attached.
7. **Cystatin-C-based eGFR as the sole renal decision variable, in every arm.** One measure, two
   problems: it removes the iatrogenic prescribing cascade (§3.3) *and* the renal unblinding tell.
   Report creatinine only inside the firewall. **And train investigators on the candesartan
   contrast** — candesartan also raises creatinine, but by pure efferent-arteriolar haemodynamics,
   which is genuine, intended and renoprotective. *Same lab signal, opposite interpretation,
   opposite management.* An investigator who conflates them will mismanage both arms.
8. **Protocolise rescue therapy** with objective pre-specified triggers adjudicated by a masked
   committee — this is the most damaging unblinding channel and it bypasses the masked reading
   centre entirely.
9. **Background control.** Stratify on dihydropyridine CCB use (peripheral oedema, increased
   macular thickness), **exclude TZD**, record insulin-intensification episodes as a time-varying
   covariate, pre-specify identical HbA1c/BP/LDL targets across arms, and **report between-arm
   drift in achieved HbA1c and BP as a blind-integrity metric**. Without this, a trial measuring
   macular thickness is measuring its own concomitant-medication profile.
10. **Measure the blind at exit** (patients and investigators asked which arm they believe they
    were in; formal blinding index as a pre-specified reported outcome). Cheap, standard, almost
    never done.

**Why pemafibrate, compactly:** the only Group A member giving full dose to the patients with the
most disease; no creatinine confound; PPARγ excluded with 5–6 logs of margin (uniquely valuable
in a macular-edema-sensitive indication); cannot perpetrate a statin interaction at 0.4 mg/day;
493× lower molar covalent burden; largest apoC-III / remnant effect in the class. Its real
weaknesses — Japan-only, BID, not generic, worst hepatic-ANGPTL4 exposure — are addressed by
making fenofibric acid the **second, bridging, public-health trial** and by making plasma ANGPTL4
mandatory.

**What this recommendation deliberately does NOT claim:** that retinal PPARα is engaged; that
transrepression occurs in human retina; that the effect will be large; or that a cheap generic
will reproduce it. Every one of those is a separate, later, falsifiable question.

---

## 8. (b) THE PORTFOLIO — THREE PROGRAMMES THAT FAIL ON INDEPENDENT AXES

The test of a real portfolio is that its members do not share a failure mode. Stating the failure
axes explicitly is the work:

| # | Programme | Unmet need | **Fails if...** | **Independent because the failure is about...** |
|---|---|---|---|---|
| **1** | **Remnant / apoC-III lowering, S1–S3, pemafibrate → fenofibric acid bridge** | #1, #5 | the supply→retinal-lesion step is false; or the achievable increment over background high-intensity statin is below detectable | **lipoprotein biology and trial arithmetic** |
| **2** | **Plasma kallikrein inhibition (berotralstat), enriched incomplete-anti-VEGF-responder DME** | #2, #4 | the contact pathway is not a dominant driver in the enriched phenotype; or CYP2D6/3A4 DDI and QT prove unmanageable in polypharmacy | **a different pathway, a different stage, and an exposure argument that does not exist** — intravitreal kallikrein is extravasated plasma prekallikrein, so a systemic inhibitor meets its target where the target already is. **K<sub>p,uu</sub> drops out of the equation entirely.** |
| **3** | **Efflux arm — intravitreal/suprachoroidal ApoA1/ApoE-mimetic peptide (lead), or an oral LXRβ-biased modulator (harder)** | #5, #2 | the LXR TG/steatosis liability cannot be engineered away; or the peptide fails to break the foam-cell futile cycle | **chemistry/modality and the efferent limb** — the only programme aimed at the declared empty module (P8.3) |

**Why this is a portfolio and not a list:**

- **Programmes 1 and 3 are multiplicative, not redundant.** At quasi-steady state,
  `deposit ≈ influx ÷ clearance_rate_k`. One lowers the numerator; the other raises the
  denominator. Halve influx *and* double clearance → one quarter of the burden, where either
  alone gives one half. They also have **opposite enrichment criteria** (1 enriches for high apoB
  with *no exudate yet*; 3 enriches for *existing* extrafoveal exudate) — and two agents selecting
  the same patients are usually doing the same thing, so opposite criteria are independent
  evidence of non-redundancy.
- **Programme 2 is deliberately orthogonal to the entire PPARα question**, which de-risks the
  portfolio rather than doubling down on it. Berotralstat's licensed use *is* chronic daily oral
  outpatient prophylaxis in people who feel well — the exact behavioural model DR needs — and it
  is not primarily renally cleared, which in a CKD-dominant population is close to decisive. Its
  contact-pathway mechanism is notably **not** associated with bleeding (FXII/prekallikrein-
  deficient humans do not bleed), which matters specifically because vitreous haemorrhage is
  itself a measured disease outcome. Honest limits: orphan pricing argues for targeting unmet
  need #2 (a specialist population already on expensive therapy) rather than #1; and the model's
  own record of mixed intravitreal kallikrein results argues for **phenotype enrichment**, which
  the design builds in.
- **Elevating the Pathway agent's §4.1 observation, which no earlier agent made:** the efflux
  agent's patients are *already receiving intravitreal injections*. An ApoA1/ApoE-mimetic peptide
  given as an adjunct at the same visit adds **no new procedure** and deletes the entire BRB
  delivery argument — and a peptide supplying an acceptor in the interstitium does not need to
  enter cells. **The run's oral-only framing is right for programme 1 and wrong for programme 3.**
- **The combination to avoid: fibrate + ezetimibe.** Maximally redundant on the same afferent
  term, sub-additive, with additive cholelithiasis risk (both raise biliary cholesterol
  saturation). Ezetimibe belongs in the design as a **comparator arm, never as a combination
  partner.**

**Explicitly not in the portfolio, with reasons:**

| Excluded | Reason |
|---|---|
| **Dimethyl fumarate** | §4. Short-course mechanistic probe only, never a lifelong preventive. |
| **Elafibranor** | Database immaturity (2024 approval, 3–4 orders of magnitude smaller than fenofibrate's) + **unexcluded PPARγ with a γ-like weight-gain signal, in the one indication where that liability is named** + an uncharacterised NRF2 limb that contaminates the D2 arm. 6–12 month monitored probe only. |
| **Seladelpar** | PPARδ carcinogenicity is a **Type C duration-dependent** hazard — precisely what lifelong dosing in healthy-feeling people cannot absorb. Retain as a short-duration isoform control; it is not a candidate. |
| **Candesartan** | Excellent drug, **and its only available deployment route in this population creates contraindicated dual RAS blockade.** The scientific question it would answer is already being answered by standard care. |
| **Minocycline** | BLACK. It can cause **papilloedema and visual-field loss in a trial measuring retinal endpoints** — an adverse effect that attacks the primary endpoint from inside — plus irreversible ocular pigmentation visible to the examining ophthalmologist at every slit-lamp exam, plus a demonstrated repeated translational failure of that exact mechanism in human CNS disease. |
| **Epalrestat** | Target carries negative human validation; good engagement of a falsified target is a negative. Plus the highest reactive-metabolite burden in the set (~17.5× reference), no FDA/EMA safety review ever conducted, and an **unflagged wrong-sign risk: AKR1B1 is a 4-HNE reductase**, so inhibiting it impairs retinal aldehyde detoxification in a maximally PUFA-loaded tissue. |
| **Quercetin** | A `[DATA]`-backed SLCO1B1 statin-uptake interaction — *gemfibrozil's own mechanism*, from the supplement aisle — in a universally statin-treated population, with **zero achievable exposure and therefore a risk–benefit ratio whose denominator is zero.** |
| **Icosapent ethyl** | Best third on pathway coverage (sole occupant of P8.6 resolution territory, and the model names resolution failure as the under-exploited angle). Gated by the null large ω-3 RCT in a chronic progressive retinal disease, plus bleeding in an antiplatelet-treated population and an AF signal. Not killed — deferred. |
| **The dual/pan-PPAR lane** | §6.3. A γ graveyard whose every terminating toxicity is one this population tolerates worst. |
| **Linalool, linoleic acid, α-linolenic acid, melatonin** | Not dose-movable (B1/B2), no safety database at any relevant dose (B3, and organoleptically unblinding), or glycaemic confounding of the dominant disease driver (C2). Linalool retains value only as an **SAR fragment**, gated on an orthogonal binding confirmation. |

---

## 9. (c) THE DECISIVE EXPERIMENT, SPECIFIED PROPERLY

Round 1 proposed: chronic oral fibrate in a diabetic rodent; retinal CPT1A/ACOX1/ANGPTL4
(transactivation) vs retinal ICAM1/TNF/leukostasis (transrepression); called it "cheap and
decisive." The Literature agent is right that **without a `Ppara-/-` arm and a matched non-PPAR
lipid-lowering arm it is cheap and *indecisive*.** Here is the full specification.

### 9.1 Design — five arms

| Arm | Content | What it rules out |
|---|---|---|
| 1 | Diabetic WT + vehicle | baseline |
| 2 | Diabetic WT + chronic oral fibrate, **exposure-matched** | the effect itself |
| **3** | **Diabetic `Ppara-/-` + the same fibrate** | **PPARα-independent drug action.** Without it, any effect is attributable to the direct NF-κB interference, AMPK activation, mitochondrial uncoupling and ER-stress induction fibrates demonstrably exert at the concentrations reached. This is the arm that redeems the contaminated in vitro literature. |
| **4** | **Diabetic WT + a matched non-PPAR remnant-lowering intervention**, titrated to the **same plasma remnant / apoC-III reduction** | **the lipid-supply confound.** Without it a positive retinal readout cannot be assigned to the receptor rather than to lowered lipoprotein supply — the exact ambiguity E1 was added to the candidate set to resolve. |
| 5 | Non-diabetic WT + vehicle | model validity |

Arm 3 inherits the global-knockout confound (hypertriglyceridaemia, elevated NEFA, abolished
ketogenesis, hepatic steatosis, **abolished FGF21 induction**, altered STZ response). That is
tolerable **here** and not elsewhere, because arm 3 is being used as a *pharmacological
specificity control within genotype* (does the drug effect disappear?), not as evidence that
PPARα is protective. Where the knockout *was* misused — as evidence for a retina-intrinsic
mechanism — the Literature agent's demolition stands: that result is equally, arguably more,
consistent with the systemic limb, and citing it for the retinal limb is a circularity that has
propagated into this run's own brief.

### 9.2 Three requirements no prior agent assembled in one place

**(i) Measure the independent variable; do not infer it.** Terminal **retinal free drug
concentration** and matched plasma free concentration by LC-MS/MS, with plasma protein binding
measured in the same species, yielding a **measured K<sub>p,uu</sub>**. The Literature agent
names this as the single most important unmeasured quantity in the run, on which three mutually
exclusive programmes hang. **A transcriptional study that does not measure the exposure it is
probing re-creates the ambiguity it exists to remove.** This is the most important single
addition to Round 1's design.

**(ii) Matched readouts on both limbs, plus the two humoral relays.**
- *Transactivation panel:* CPT1A, ACOX1, HMGCS2, ANGPTL4, **and ABCA1** — the Pathway agent's
  efflux question rides on the identical limb, so it is answered for free here.
- *Transrepression panel:* ICAM1, TNF, IL6, VCAM1 **plus functional leukostasis** (adherent-
  leukocyte count). The ICAM-1 threshold argument is about a **nonlinear functional endpoint**,
  not a transcript, so a transcript-only readout cannot test it.
- *Plasma:* **FGF21 and ANGPTL4**, to size the two luminal relays — the limbs needing no barrier
  crossing, and nearly free to measure.
- *Structural:* acellular capillaries, pericyte loss, permeability.
- *If a DMF arm is ever run:* **retinal GAPDH activity and photoreceptor ERG a-wave** (§4.3).

**(iii) Exposure-matching rather than dose-matching across arms 2–4, with pre-registered
inferences.** Four outcomes, each with its consequence fixed in advance:

| Readout | Inference | Consequence |
|---|---|---|
| Transrepression ↓ **without** transactivation ↑; **arm 3 abolishes it**; **arm 4 does not reproduce it** | a genuine, receptor-mediated, retina-intrinsic anti-inflammatory limb exists at achievable exposure | the retinal programme is real; bias engineering becomes a sensible 2nd-generation objective |
| **Arm 4 reproduces arm 2's retinal benefit** | the receptor is not doing the work | **abandon the receptor framing, keep the programme** — and ask whether a better remnant-lowering agent should run it |
| Robust retinal **transactivation** (CPT1A/ACOX1 up) | the low-occupancy model is wrong and the exposure objection that organised this run collapses | **reinstate the ANGPTL4 flag at S4–S5**; bias engineering becomes rational |
| **Arm 3 fails to abolish arm 2's effect** | the effect is PPARα-independent off-target pharmacology | the receptor framing is dead **regardless of the direction of the effect** |

### 9.3 Honest cost, and the human experiment that runs alongside

The SAR agent's Gate 0 estimate (~$50–150k, 6–9 months) is for the **two-arm** version. The
five-arm version with LC-MS/MS exposure determination is realistically **$250–400k and 9–12
months** — still trivial against a $150–400M NCE programme, and the honest number to quote rather
than inheriting "cheap." **It must be stated that Round 1's version would have produced a
positive, uninterpretable result, and that result would have been used to justify a $300M
programme.**

**Running in parallel, because the samples already exist:** **aqueous humour drug concentration
plus aqueous ANGPTL4 in chronic-fibrate-exposed versus unexposed diabetic patients undergoing
routine cataract surgery.** Aqueous is not retinal interstitium, but it bounds the problem, it is
obtainable from routine surgery at negligible added risk, and it delivers **two of the run's three
central unknowns from one tap.**

**And one covariate analysis that is not an experiment at all and may be worth more than either:**
in any dataset where a lipid-lowering exposure and a retinal outcome co-exist, test **whether the
retinal benefit tracks the achieved lipid/remnant change.** If benefit does not track the lipid
change, limb 1 is in trouble and the receptor hypothesis strengthens. It is the cleanest
discriminator between the run's two readings, it requires no new tissue, and it is answerable
from data of a kind that is routinely collected.

---

## 10. (d) KILL CRITERIA — STATED IN ADVANCE

Grouped by what each kills, so that a failure retires the right amount of the programme.

### Kill the retinal receptor limb if:

- **K1.** Gate-0 **arm 3 (`Ppara-/-`) fails to abolish** arm 2's retinal readout → the effect is
  off-target pharmacology, not the receptor. *Kills the limb regardless of effect direction.*
- **K2.** **Measured** terminal retinal K<sub>p,uu</sub> < 0.05 **and** no transrepression signal
  → occupancy is too low and nothing is happening.
- **K3.** No neutral, non-basic, retina-competent PPARα chemotype reaches **≥100× selectivity over
  both γ and δ** within the first lead-optimisation cycle. This is the SAR agent's own
  highest-ranked chemistry risk and it is structural: compact neutral lipophiles are **PPARδ's**
  preferred chemotype, δ is the most abundant retinal PPAR, is pro-angiogenic, and induces
  ANGPTL4 at least as strongly — **the carboxylate was itself part of PPARα's selectivity, so the
  hop worsens the isoform margin.**

### Kill the receptor *framing* (but not the programme) if:

- **K4.** Gate-0 **arm 4 reproduces** the fibrate's retinal benefit at matched remnant lowering →
  it is a remnant-supply programme; transfer it to the best remnant-lowering agent and close the
  receptor file.
- **K5.** In human data, the retinal benefit **does not track the achieved remnant/apoC-III
  change** → limb 1 is wrong and the framing must be rebuilt from scratch.

### Kill the systemic programme if:

- **K6.** The achievable increment over **background high-intensity statin** on remnant particle
  number is below the smallest effect the trial can detect. **This is a power calculation to be
  run before enrolment, not a result** — and it is the most likely way this programme dies
  quietly. If the arithmetic does not close on paper, do not run the trial.
- **K7.** Prespecified safety stop: **excess progression to proliferative disease**, or **excess
  centre-involving macular edema**, in the treated arm.
- **K8.** No regulatory endpoint for early (S1–S2) DR becomes established. The programme then has
  no registration path regardless of mechanism. The SAR agent ranks this above every chemistry
  risk and I agree. **Address it with regulators before the Phase 2a, not after.**

### Kill the whole PPARα enterprise if:

- **K9.** **K1/K2 and K4 both hold** — no receptor limb, and no receptor-specific contribution to
  the systemic limb. At that point PPARα is a historical label on a lipid programme; the honest
  action is to transfer and close.
- **K10.** A **cell-type-restricted conditional retinal `Ppara` deletion from an independent
  group**, on a background with normal systemic lipids, shows **no retinal phenotype**. The
  Literature agent is right that this one experiment is worth more than the entire existing
  preclinical corpus — and that its continued absence after ~15 years of interest in this target
  is itself mildly informative.

---

## 11. WHAT I AM CONCEDING, STATED BEFORE ANYONE ELSE SAYS IT

A synthesis that only defends is not a synthesis. Seven concessions:

1. **The run's titular question was the wrong question** and two phases were spent on it (§6.4).
2. **My recommendation is smaller than the run opened with.** It is a lipid programme with a
   receptor as its instrument, a stage restriction, a vascular endpoint, and an explicitly
   optional retinal limb.
3. **The whole position rests on one unmeasured number**, and I have not measured it. The
   mitigation is that the recommendation is deliberately constructed to be *invariant* to it —
   but that is a design choice, not a measurement, and it should be read as such.
4. **FGF21's retinal terminus is Level 4 animal evidence.** I weight it heavily because it is
   independently replicated by laboratories with no stake in the PPARα-retina hypothesis and
   because the upstream step is human-proven — but it is not human retinal evidence and there is
   none.
5. **Pemafibrate is not globally available** and I am recommending it first anyway, on the
   argument that an interpretable answer from an unavailable drug beats an uninterpretable one
   from an available drug. That is a defensible trade and it is a trade.
6. **Two of my three portfolio programmes have nothing to do with PPARα.** That is deliberate —
   a portfolio whose members share a failure mode is not a portfolio — but it does amount to a
   partial concession of the run's premise.
7. **No conclusion anywhere in this debate is data-backed by this project.** No drug→target
   affinity exists anywhere in the repository; the ChEMBL mechanism (11 rows), target (44) and
   indication (80) tables are near-empty test extracts with **zero PPAR content**; `logd`,
   `cx_logd`, `permeability`, `molecular_species` and `bioavailability_score` are empty for all
   3,276 drug rows; the 27-gene DR panel contains all three PPAR receptors and **zero PPAR
   effector genes**, so the pathway this run is about is invisible to the run's own data; the
   efflux arm has two rows; KLKB1 has two rows, both CTD expression from toxicants; and the
   dataset contains **no biologics at all** (3,276/3,276 small molecules), so every
   oligonucleotide and antibody discussed is structurally absent rather than informatively absent.
   **This run measured mechanistic-path plausibility under data blinding. It did not measure
   data-driven rediscovery, and the scoring step must read it that way.**

---

## 12. SUMMARY OF CORRECTIONS THIS DEBATE ROUND MAKES TO THE RECORD

| # | Correction | Source |
|---|---|---|
| 1 | The exposure question is **compartment-stratified, not aggregate**; and there is a **fourth compartment (plasma)** for which the term does not apply | this agent, from ADMET + Literature + Repurposing |
| 2 | The SAR finding is about **designability, not exposure**; it severs Round 1's inference without reversing its arithmetic. Going neutral fixes 3 of 4 terms, **not `fu`** | SAR §2.3, clarified here |
| 3 | Round 1 **violated its own isoform discipline in the benefit direction** — importing a PPARγ/LXR macrophage SUMO mechanism into a PPARα argument | Literature A3.2 |
| 4 | The occupancy-differential version of transrepression must be **replaced** by the ICAM-1 density-threshold version everywhere | Literature A3.3 + Pathway §6.2 |
| 5 | Bias engineering would delete **FGF21** — the best-evidenced limb — not merely the lipid limb | this agent, extending SAR §3.3 |
| 6 | The dual/pan-PPAR graveyard is a **γ graveyard**; isoform discipline cuts in favour of α | Repurposing §1.2, reframed here |
| 7 | **Cheapness carries no information about efficacy** and must be scored on feasibility only; the "cheap generic + strong preclinical" configuration has a poor prior (minocycline) | Literature A5.2–A5.3 |
| 8 | The **lipid panel, not creatinine**, is the dominant unblinding tell | Safety §5.2 |
| 9 | The fibrate's principal renal harm over decades is plausibly an **iatrogenic prescribing cascade**, not nephron loss — and cystatin C fixes it and the unblinding tell together | Safety §4.3 |
| 10 | The honest development target is **S1–S2, not S0**; unmet need #1 as written is mechanically unreachable by a supply-lowering agent | Round 1 §3, reaffirmed |
| 11 | The decisive experiment must **measure retinal free drug**, not infer it from transcripts | this agent |
| 12 | Gate 0 costs **~$250–400k**, not "cheap"; Round 1's version would have produced a positive, uninterpretable result | this agent |

---

## 13. BLINDING COMPLIANCE

**Files read, completely unless noted:** `disease-brief.md`; `round1-synthesis.md`;
`round1-score-matrix.txt`; `round2-score-matrix.txt`; `data-quality-findings.md` (§1–17, full);
`agents/p2-pathway.md` (full); `agents/p2-safety.md` (full); `agents/p2-sar.md` (full);
`agents/p2-repurpose.md` (§0–§9 opening); **`agents/p2-literature.md` — lines 1–571 only.**

**Part B attestation.** `agents/p2-literature.md` contains the header
`## POST-HOC UNBLINDING (EXCLUDED FROM SCORING)` at **line 572**. I located that line number
with `grep -n` *before* reading any content, and then read the file with an explicit
`sed -n '1,571p'` range cap. The last content I read is the bare `# PART B` title line at 570 and
the blank line at 571. **I did not read line 572 or anything after it. No post-hoc unblinding
content entered this synthesis, and nothing in this document derives from DR/DME trial,
indication, guideline or regulatory evidence for any candidate.**

**Files NOT read, deliberately:** `data/holdout/` (any file); `data/processed/chembl_approved_drugs.csv`;
anything matching `answer-key*`; any unblinded `data/processed/` table. I did not use git history,
git objects, or any other route to recover redacted values, and I made no attempt to infer which
rows were redacted.

**Rule 2 compliance.** I did not use, assert or cite the DR/DME indication, approval, guideline
status or trial history of any candidate. Every candidate's DR status was treated as unknown
throughout, including in the portfolio construction (§8), the kill criteria (§10) and the
experimental design (§9).

**Disclosures of knowledge-adjacent judgment, including negative decisions, per brief §1.5:**

1. **Two inherited borderline calls.** My §2 weighting of limb 1 relies in part on the Literature
   agent's use of the human observational association between serum lipids and retinal hard
   exudate, and my §2.3 ANGPTL4 bounding relies on its use of human aqueous/vitreous ANGPTL4
   case-control data. Both were disclosed by that agent as borderline-permitted (epidemiological
   and biomarker data, no drug, no trial, no indication) and I adopt both judgments and the
   disclosure with them.
2. **Class liabilities treated as given framing.** PPARγ fluid retention and macular-edema
   association (brief §4 supplies this to all agents as a scoring prior); aldose-reductase and
   PKCβ as failed human DR mechanisms (brief §4, used only at the brief's own level of
   abstraction — "the mechanism class failed," with no trial names, populations or effect sizes);
   intravitreal corticosteroid efficacy in DME (disease-model §4.1, a modality not in the
   candidate set); mixed intravitreal kallikrein results (disease-model §1081). None is a
   candidate-status claim.
3. **Non-DR clinical facts used freely and permissibly:** the glitazar discontinuation record
   (AleCardio, muraglitazar, tesaglitazar, ragaglitazar); the dissociated-glucocorticoid field's
   30-year record; DMF's PML/lymphopenia profile and GAPDH Cys152 succination; minocycline's
   benign intracranial hypertension and its CNS-trial failure record; the null ω-3 RCT in a
   chronic retinal disease; PCSK9/inclisiran/olezarsen lipid pharmacology; LXR agonist steatosis
   failures. All non-DR, all permitted under brief §1.3.
4. **Negative-decision disclosure.** I hold pretrained knowledge of the DR clinical literature for
   several candidates in this set. I excluded it from every argument in this document, **including
   where it would have raised a recommendation's confidence**. The two places where I am least
   able to certify that exclusion, and am recording rather than silently correcting:
   (a) my confidence that the **systemic lipid limb is the one worth developing** is higher than
   the Level 4 retinal evidence alone would warrant, and although I can derive it from the
   evidence-grade argument in §2.2 and the CKD-banding argument in §1.3, I cannot fully exclude
   that knowing the shape of the field nudged it upward; (b) my **stage restriction to S1–S3**
   is derivable entirely from the ANGPTL4/HIF argument and the barrier-integrity argument, but it
   is also a conventional DR development choice. I have left both as reasoned and flagged rather
   than artificially deflating them, since a deliberate downward correction would be just as
   contaminated as an upward one.
5. **The irreducible residual the synthesis already names applies to me.** Dataset blinding
   removes the project's data signal, not pretrained pharmacology. This document reports
   mechanistic-path plausibility under data blinding, not naive rediscovery.
