# Debate Round Summary — Diabetic Retinopathy (BLINDED RUN)
Devil's Advocate versus Integration Specialist. 2026-10-05.

Both agents received the full two-round record and were blinded. Neither saw the other's
output. The Advocate disclosed a partial blinding breach (findings §17b) and quarantined the
section it affected.

**This round produced the run's most important findings — including the discovery that two of
the pipeline's load-bearing claims were orchestrator transcription errors rather than agent
conclusions.**

---

## 1. THE ADVOCATE'S CENTRAL CHARGE

> **"The pipeline's conclusion has been invariant across two rounds, eleven agents, three
> self-reversals and sixteen recorded defects. Its reasons have changed completely. When the
> premises are replaced and the conclusion is not, the conclusion is not being derived from
> the premises."**

Phase 0 said the exposure gap killed the hypothesis. Round 1 said the gap was mismeasured and
relocated the mechanism to the liver. Round 2 said the structural constraint organising
Round 1 was never real. Through all of it, the same two compounds sat first and second.
**Every demotion landed on a peripheral candidate; every rescue landed on a leader.**

**Status: partially upheld.** The final ranker accepted the charge as "substantially
rationalised," and responded correctly — by demoting a leader on falsification grounds rather
than by reweighting. The charge should permanently temper confidence in the ordering.

---

## 2. THE TWO ORCHESTRATOR ERRORS THE ADVOCATE FOUND

Both were verified independently by the orchestrator against `agents/p1-admet.md` §3.2 and
corrected in place. Full record in findings §18.

### 2.1 A term reported as a product

Round 1 claimed potency rank and retinal-access rank are "the exact reverse" of each other,
and built on it the conclusion that potency and engagement are anti-correlated.

The **Kp,uu term alone** is reversed — that is the ADMET agent's Table 1, explicitly headed
"rank by retinal access." The **occupancy product** is not. Endothelial margins versus free
EC50, from the same report:

| Compound | Margin | At geometric midpoint |
|---|---|---|
| **Elafibranor** | **−0.7 to +0.4 log** | **−0.14** |
| Pemafibrate | −1.6 to −0.2 log | −0.92 |
| Fenofibric acid | −3.0 to −1.1 log | −2.07 |

**Same order as potency.** The ADMET agent's own wording was that potency is "nearly
*orthogonal* to engagement," which the synthesis rendered as inversely correlated.

### 2.2 The retracted structural conclusion

Round 1's most emphatic claim — *"no molecule in the fibrate class can test the
retina-intrinsic PPARα hypothesis"* — is contradicted by the run's own arithmetic. The ADMET
agent names elafibranor **"the only Group A compound that plausibly reaches or exceeds its
free EC50 at the retinal endothelium… the cleanest pharmacological probe."**

**The run had its probe and declared the question structurally impossible.** That retracted
finding had framed the entire SAR assignment and fed a cost model for a new chemical entity.

**The retraction is partial:** elafibranor carries PPARδ co-agonism that confounds the isoform
question, a Michael-acceptor enone at 120 mg/day that is a genuine chronic liability, and a
Cmax the ADMET agent flags as its lowest-confidence number. **But "confounded and uncertain"
is a different claim from "structurally impossible."**

**Resolution: elafibranor reinstated as a ~12-week mechanistic probe**, not as a chronic
therapeutic.

---

## 3. THE ADVOCATE'S OTHER ATTACKS

**Pemafibrate moves the run's own toxic species the wrong way.** The disease model's lesion is
the retained modified apoB particle. In its cardiovascular outcome programme in statin-treated
diabetics, pemafibrate lowered triglycerides, remnant cholesterol and apoC-III — while
**raising LDL-C ~10% with apoB flat, and producing no event benefit** (non-retinopathy
evidence, permitted). So the "right particle" argument fails for the very drug it was used to
promote, and the privileged node the run nominated has had its best hard-endpoint test with an
unfavourable read. **No agent in eleven had raised this.** *Status: upheld; it drove the
pemafibrate demotion.*

**The mechanism consensus is untestable as built.** Every control sits on the lipid side.
**No arm anywhere tests "receptor without lipid" or "drug without lipid."** Meanwhile the two
readings make opposite predictions about *which fibrate should win* — systemic remnant-lowering
favours pemafibrate, an intraocular mechanism favours fenofibrate, which delivers roughly
3,000× more total drug to every ocular compartment. **A dose-matched head-to-head discriminates
in one two-arm trial using two approved drugs the run already had and scored as
interchangeable.** *Status: upheld.*

**The "only an uptake transporter gives Kp,uu > 1" axiom is false.** Metabolic trapping offers
a route: the acyl glucuronide hydrolysed by β-glucuronidase in the lysosome-dense RPE would
regenerate ion-trapped acid intracellularly. *Status: plausible, unmeasured, and it makes the
Gate 0 measurement more valuable.*

---

## 4. THE INTEGRATOR'S RESOLUTION

### 4.1 The dichotomy was the error

> **"Not either/or — the dichotomy is itself the error. It assumes a drug affects a tissue
> only by entering it."**

Four limbs, ranked by evidence × engagement certainty:

1. Hepatic PPARα → APOC3↓/LPL↑ → remnant and apoB particle number ↓. **Certain engagement.**
2. Hepatic PPARα → **FGF21↑** → retinal endothelium **from the luminal side.** Upstream
   human-proven, downstream animal-proven by independent laboratories, **no barrier crossing
   at any point.**
3. Endothelial transrepression → ICAM1↓. Low evidence, negative class precedent.
4. Retinal fatty-acid-oxidation transactivation. Absent at achievable occupancy.

**Limbs 1–2 are *systemic in pharmacokinetics and retinal in pharmacology*. The liver is a
legitimate site of action *on* the retina.** This is the third option neither the
lipid-lowering nor the retinal-occupancy framing had enumerated.

### 4.2 Four compartments, not two

Neural retina **dead** (1–3 logs short, never arrives at any stage). Endothelium and RPE
**marginal and unmeasured.** Hepatocyte **certain.** And **plasma — the compartment nobody
counted, where the Kp,uu term does not appear at all.**

**Design rule:** *build nothing requiring retinal partitioning above 0.2; build something
invariant to retinal partitioning of zero.*

### 4.3 A population-level argument that settles the exposure question without chemistry

The systemic limb is transporter-concentrative and saturable; the retinal limb is passive and
linear in free plasma. **Renal dose-banding therefore selectively amputates the retinal limb
while sparing the systemic one — in exactly the patients with the most retinopathy**, since
nephropathy and retinopathy track together. Not fixable by molecule choice.

*The feasibility agent later turned this into an asset: the two limbs predict quantitatively
different kidney-function × treatment interactions (~25% versus ~67% attenuation), so
pre-specifying it makes dose-banding a **free within-trial mechanism discriminator** — and
even a null pivotal trial returns a mechanistic answer.*

### 4.4 The ANGPTL4 ceiling

ANGPTL4 inhibits lipoprotein lipase, so a functionally meaningful induction predicts
triglycerides to **rise**. Observed triglycerides **fall**. Real-world induction is therefore
bounded above by an already-measured quantity. *The Literature Reviewer produced this
independently.*

### 4.5 On abandoning the PPARα framing

**Partially abandon it — and the programme gets stronger.** Conceded as a stated kill
criterion, not a hedge: if the mechanism is apoB *mass*, the framing is wrong and the right
drug is inclisiran. But apoB mass is not the model's mechanism; the toxic species is the
modified remnant particle, and diabetic dyslipidaemia is a remnant disorder.

---

## 5. WHAT THE DEBATE LEFT UNRESOLVED

- **Whether limb 1 is strong at all.** The final ranker extended the Advocate's pemafibrate
  argument against limb 1 itself: pemafibrate is the natural experiment for maximal hepatic
  engagement and maximal apoC-III suppression, and it is not the best drug in the class.
- **Whether the FGF21 relay closes quantitatively.** The ranker found nobody had checked
  whether the physiological rise a fibrate produces reaches the pharmacological concentration
  at which retinal protection was demonstrated. **The Literature Reviewer confirmed no
  published measurement bridges them.**
- **The rationalisation charge itself.** Mitigated by the ranker's falsification-driven
  demotion, not dissolved.
