# Round 2 Synthesis — Diabetic Retinopathy (BLINDED RUN)
Orchestrator synthesis of five Phase 2 deep-dive agents. 2026-10-05.

Agents: Pathway Analyst · Safety Pharmacologist · Drug Repurposing Strategist ·
SAR Analyst · Literature Reviewer (Part A only; its Part B is the benchmark's
unblinding checkpoint and is quarantined in `agents/UNBLINDING-part-b.md`).

Round 2 was tasked against the five questions Round 1 could not settle. Four returned
answers that changed the ranking; one returned a refutation of Round 1's organising premise.

---

## 1. WHAT ROUND 2 CHANGED

| Round 1 position | Round 2 verdict |
|---|---|
| The acid head is mandatory for PPARα, so potency and retinal access are anti-correlated by construction | **REFUTED.** The AF-2 cage is all-donor; the ligand supplies only acceptors. Geometry demands a bidentate acceptor pair ~2.2–3.2 Å apart, **not a formal charge** |
| No fibrate can test the retina-intrinsic hypothesis | **RETRACTED** (orchestrator error, findings §18) — elafibranor's endothelial margin is −0.7 to +0.4 log |
| Ezetimibe is the mechanism-discriminating control | **SUPERSEDED.** Wrong particle — it lowers LDL, the mechanism concerns remnants. An apoC-III-directed arm is the matched control |
| The efflux arm might be covered by PPARα→ABCA1 induction | **NO.** That induction is gene-activation driven — the same limb shown absent at achievable retinal occupancy — and it is a two-step relay, so *more* occupancy-sensitive |
| Dissociated-ligand design is the sharpest constructive idea | **DEMOTED** to a contingent follow-on. Bias is orthogonal to the occupancy bottleneck, and designing it in would delete the only certain engagement |
| Dimethyl fumarate is a serious contender (disease-biology 7.0) | **RED on safety (2.5).** Monitoring-dependent safety does not survive translation to asymptomatic population-scale use |

---

## 2. THE SAR REFUTATION — Round 2's most consequential finding

Round 1's structural centrepiece was that medicinal chemistry had optimised the fibrate
series' potency by 4–5 logs while degrading every term governing tissue access, because the
lipophilic bulk filling PPARα's arms II/III is the same element albumin site II and the
hepatic OATP1B transporters recognise. The conclusion drawn was that hepatoselectivity is
not optional within the chemotype, so the retinal limb is permanently untestable.

**The SAR Analyst dismantled the premise by changing the unit of measurement.**

- Measured in **ligand efficiency** (binding energy per heavy atom) rather than raw potency,
  the neutral endogenous ligand oleoylethanolamide sits at **LE 0.41** — *above* fenofibric
  acid (0.29) and pemafibrate (0.34). **The neutral head pays no efficiency penalty.**
- Charge is an acceptor-strength multiplier, not a structural requirement. Going neutral
  costs ~2.3–3.1 kcal/mol per contact — real, bounded, affordable.
- Three existence proofs: oleoylethanolamide (neutral, ~120 nM); the thiazolidinedione head
  (pKa ~6.5, inside the barrier-penetration window); linalool (LE 0.55).
- **Tetrazole is a false friend** — the reflexive carboxylate bioisostere raises pKa by only
  ~1.6, has a *larger* footprint, and remains a full OATP1B substrate, which is why the
  sartans are hepatically taken up.
- **PPARα's arm I is narrower than PPARγ's**, so head *footprint* is the first filter — which
  rules the thiazolidinedione out for α and rules **1,2,4-oxadiazol-5(4H)-one** in.

**The asymmetry that qualifies it:** Tyr464 sits on mobile helix 12 and pays for AF-2 closure,
so it is lost first. **A neutral head therefore produces a partial agonist by construction —
efficacy degrades before affinity.**

---

## 3. THE DISSOCIATED-LIGAND IDEA, DEMOTED

Round 1's surviving retinal limb was transrepression at low occupancy. The SAR Analyst found
it structurally designable by three routes and nonetheless **the wrong thing to design**, on
two arguments independent of the field's track record:

1. **Bias does not appear in `fu × C × Kp,uu / EC50`.** Occupancy is the limiting term; bias
   is orthogonal to the bottleneck.
2. **It would delete the only certain engagement in the run** — hepatic gene activation
   (LPL↑, APOA1↑, APOC3↓, FGF21↑) — in order to manage ANGPTL4, a risk already demoted and
   already carrying a cheap plasma biomarker. **Net-negative.**

The track record agrees: ~30 years across two receptor families, a dozen programmes, **zero
systemic approvals**; the only survivors reached patients topically or by inhalation, i.e. by
solving delivery the hard way.

The Literature Reviewer independently reached the same place from the evidence side, and
caught an isoform-discipline inconsistency the orchestrator had let through: **the
"non-consumed receptor" mechanism cited in support is a PPARγ/LXR result, imported into a run
whose brief mandates isoform separation. Round 1 applied that discipline to liabilities but
not to benefits.**

---

## 4. THE EFFLUX GAP — right gap, harder half

Four cell populations perform retinal reverse cholesterol transport: RPE (the only one with
direct acceptor access, across the fenestrated choriocapillaris), Müller glia (the retina's
ApoE source), microglia and macrophages (where the foam-cell lesion lives), and
photoreceptors (net producers).

**The lesion is a self-renewing cycle, not a deposit:** modified LDL → scavenger-receptor
uptake → ABCA1 down and acceptor scarce → cholesterol cannot leave → inflammasome activation
and foam-cell death → lipid re-released → re-uptake. **The deposit regenerates from its own
debris.**

**Supply + efflux is multiplicative, not merely additive.** Steady-state burden ≈ influx ÷
clearance rate constant, so the two agents act on numerator and denominator of the same
quotient. Two supply agents (a fibrate plus ezetimibe) are additive at best.

**One framing error corrected, with a wrong-sign risk attached.** Scavenger-receptor blockade
is not the complement to efflux — it is a second *uptake* intervention on the afferent side.
Macrophage uptake is the **only catabolic route** for retained apoB lipoprotein in retina, so
blocking it converts "foam cells that die and re-release" into "extracellular modified
lipoprotein that nothing removes." Its legitimate claim is inflammasome signalling, which
belongs to the inflammation module, not the lipid-efflux one.

**The structural statement worth carrying forward:** PPARα has an engagement-certain
compartment that is not the diseased one. The efflux arm's only useful compartment **is** the
diseased one. **You cannot perform retinal reverse cholesterol transport from the liver.**

**And the opening:** the PPARα pocket mandates a lipophilic acid; **the LXR pocket does not**.
An orally retina-penetrant LXRβ-biased modulator is chemically conceivable in a way a
retina-penetrant PPARα agonist is not — and it aims at the gap rather than the covered supply
side. Systemic LXR agonism has repeatedly failed on hepatic steatosis and
hypertriglyceridaemia, so isoform selectivity is the whole problem.

---

## 5. SAFETY — the bar, and what actually fails it

The Safety Pharmacologist set a quantitative bar: for a preventive with a number-needed-to-treat
near 33 over ten years, serious **irreversible** harm must stay below roughly
7.5 × 10⁻⁵ per patient-year. Statin primary prevention sits inside it; aspirin in diabetes
does not.

**The load-bearing distinction: "lifelong" does not multiply all toxicities equally.**
Reversible dose-dependent harm accumulates but recovers. **Idiosyncratic harm is
front-loaded** — thirty years is not thirty times one year. **Only genuinely cumulative
toxicity is what lifelong dosing punishes.** The reactive-metabolite question is therefore not
where this indication's risk lives.

**Acyl glucuronide reactivity, verified from SMILES and then reordered on molar burden:**
seladelpar's structural flag largely cancels once dose is accounted for; **epalrestat is the
real outlier at 17.5×**, being the only highly reactive scaffold at a high dose; ezetimibe
carries no acid at all.

**The finding that changes the leader's risk profile:** fenofibric acid's exoneration
**depends on rapid renal clearance of its conjugate.** In chronic kidney disease the conjugate
accumulates, transacylates more, and hydrolyses back to parent drug — raising free
concentration and feeding the myopathy risk. **The acyl-glucuronide problem and the renal
problem are one problem seen twice.**

**Myopathy, quantified:** all three gemfibrozil mechanisms are absent from fenofibrate; only
the pharmacodynamic limb transfers, so roughly 3× rather than 20×, which sits 7–15× inside
the bar. **An amplifier nobody had flagged: diabetic neuropathy degrades the myalgia
early-warning signal.**

**Creatinine:** production plus reduced tubular secretion, not nephrotoxicity — the
creatinine/cystatin-C discordance settles it. **But the decades-long harm is an iatrogenic
prescribing cascade**, because a 15% rise reads as a 17% fall in estimated kidney function and
crosses the thresholds that trigger stopping other drugs.

**Dimethyl fumarate, adjudicated RED (2.5).** Progressive multifocal leukoencephalopathy risk
extrapolates to roughly 2.3× over the bar across thirty years. The decisive argument is not
the number: **safety that depends on monitoring does not survive translation from symptomatic
specialist care to asymptomatic primary care at population scale.** A possible wrong-sign
mechanism was also raised — it succinates GAPDH Cys152, and GAPDH inhibition is the central
node of the disease model's unifying hypothesis.

---

## 6. REPURPOSING — the search that came back empty, and the one that did not

**No non-acidic PPARα ligand exists as a drug.** Every approved or late-stage pan- or
dual-PPAR agonist is a carboxylic acid, so none escapes the structural question. More
informative is *why the discontinued ones died*: heart failure, oedema, bone fracture,
cardiovascular events, and — for tesaglitazar — creatinine rise with falling kidney function.
**Every one is a liability this population tolerates worst.** The pan/dual lane carries a
class-level regulatory graveyard independent of any retinal argument, and every terminated
agent carried PPARγ.

**The N-acylethanolamines half-work and are the key handoff to SAR.** Oleoylethanolamide and
palmitoylethanolamide are neutral, non-ionisable PPARα agonists — direct existence proof that
the permanent anion is not required. They break every adverse coupling at once. **They fail on
pharmacokinetics:** FAAH and NAAA clear them in minutes, so oral dosing cannot move them above
their own active concentration. Repair is discovery, not repositioning.

**The uncomfortable prediction, stated rather than avoided:** PCSK9 inhibitors lower apoB by
45–55% against a fibrate's 5–15%. **If apoB supply is the mechanism, they should work better.**
The counter is that apoB *mass* is the wrong metric and remnant/apoC-III concentration is the
right one — which keeps the hypothesis alive **only as a remnant hypothesis.** Compounding it,
statins already remove 35–45% of apoB in both arms of any trial.

**And a correction to Round 1:** an apoC-III antisense agent suppresses precisely the node
through which PPARα lowers remnants, with no receptor involved — the same mechanism with the
receptor deleted. That, not ezetimibe, is the matched discriminating arm.

---

## 7. WHAT ROUND 2 LEFT FOR THE DEBATE

1. The run had now reversed itself twice on exposure. Was that convergence or drift?
2. Pemafibrate versus fenofibric acid remained tied across two rounds and six axes.
3. The mechanism consensus (systemic lipoprotein lowering) had never been attacked directly.
4. No agent had considered **durability** — whether benefit persists after stopping.
5. Every control in the design sat on the lipid side; **nothing tested "receptor without
   lipid" or "drug without lipid."**
