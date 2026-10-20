# P2 — Pathway Analyst — Diabetic Retinopathy (BLINDED RUN)
Axis: **pathway-network coverage and position**. 2026-10-05.
Inputs: disease-brief.md · round1-synthesis.md · disease-model.md (Axis B P1–P9, S0, S2, §4.4,
§5.2, §6.2–6.3) · `.claude/skills/pathway-analyst/SKILL.md` (methodology; cascade maps rebuilt
from the DR model, not transferred from the OM originals) · agents/p1-disease.md,
agents/p1-target.md (excerpts) · evidence/*.tsv.

---

## 0. HEADLINE — four findings, stated before the argument

1. **The efflux arm is the right gap and the harder half.** It is druggable as a *target class*
   and not deliverable as an *oral drug* with current chemotypes, because it is the exact
   mirror image of the PPARα problem: PPARα has an engagement-certain compartment that is not
   the diseased one; the efflux arm's only useful compartment **is** the diseased one — neural
   retina, the least accessible tissue in the eye. **You cannot perform retinal reverse
   cholesterol transport from the liver.**

2. **PPARα's ABCA1 induction does not rescue the arm, and Round 1's own logic settles it.**
   ABCA1 induction by PPARα is largely a two-step relay (PPARα → NR1H3/LXRα → ABCA1) and is
   **PPRE-driven transactivation — the identical limb the ANGPTL4 resolution declared absent at
   achievable retinal occupancy.** If retinal occupancy is too low to induce CPT1A, it is too low
   to induce ABCA1. Worse, the one efflux limb the fibrates *can* reach (hepatic APOA1 → raised
   circulating acceptor) is aimed at the **acceptor** half, while the diabetic lesion is on the
   **transporter** half. Supplying acceptor to a cell with downregulated ABCA1 is pushing on a
   closed door.

3. **Hard exudate is supply-limited while forming and clearance-limited while persisting**, and
   the hand-off is whether the lipid is still inside a macrophage. Because steady-state deposit
   ≈ influx ÷ clearance-rate-constant, a supply agent and an efflux agent act on **numerator and
   denominator of the same quotient — their effects multiply, they do not overlap.** The
   combination is additive-to-supra-additive, not redundant. They also have **opposite
   enrichment criteria**, which is independent evidence of non-redundancy.

4. **Two mechanism-level wrong-sign risks that Round 1 did not surface.** (i) MMF covalently
   succinates **GAPDH at Cys152** — in a disease whose central lesion *is* GAPDH inhibition, and
   whose photoreceptors are obligately glycolytic. (ii) **AKR1B1 is a 4-HNE reductase** (model
   P8.7), so an aldose-reductase inhibitor *impairs* retinal aldehyde detoxification. Both are
   specific, testable, and neither appears in Round 1.

---

## 1. THE DR NETWORK — rebuilt map

The skill file's cascades are Oral Mucositis. Below is the DR network as the disease model
describes it. **There are two hubs, not one, and they are topologically opposite.**

```
                              HYPERGLYCEMIA
                                    │
                                    ▼
    ┌──────────────── mitochondrial ETC superoxide ↑ ◄── NOX1/2/4 ◄── AT1R  [D4]
    │                               │                         ▲
    │                               │ PARP → PARylation       │  uncoupled NOS3
    │                               ▼                         │  (BH4 loss, ARG2)
    │                     ★ GAPDH INHIBITION ★                │
    │                   ═══ HUB 1: DIVERGENCE ═══             │
    │                               │                         │
    │   ┌───────────┬───────────────┼───────────────┐         │
    │   ▼           ▼               ▼               ▼         │
    │  P1 polyol   P2 AGE/RAGE    P3 PKCβ/δ      P4 hexosamine│
    │  AKR1B1[D1]  AGER,GLO1      DAG→PRKCB      GFPT1,OGT    │
    │   │           │               │               │         │
    │   │ NADPH     │ feed-fwd      │ occludin      │ SP1      │
    │   │ drain     │ loop          │ VEGFA,EDN1    │ TGFB1    │
    │   └───────────┴───────┬───────┴───────────────┘         │
    │                       │                                 │
    │   P5 oxidative ───────┤◄────────────────────────────────┘
    │   NFE2L2/KEAP1 [D2]   │
    │   SOD2 (silenced)     │
    │                       ▼
    │              ★ NF-κB / RELA ★
    │           ═══ HUB 2: CONVERGENCE ═══ ◄── transrepression [A1-A5], [D2 partial]
    │                       │
    │         ICAM1 VCAM1 TNF IL6 IL1B CCL2 NOS2 PTGS2 MMP9 VEGFA
    │                       │
    │                       ▼                        P8 LIPID AXIS
    │              P6 LEUKOSTASIS                  ╔═══════════════════╗
    │                       │                      ║ runs PARALLEL to  ║
    │                       ▼                      ║ the Brownlee      ║
    │              endothelial dropout             ║ quadrant, fed by  ║
    │                       │                      ║ SYSTEMIC supply   ║
    │                       ▼                      ║ [A1-A5,B4,E1]     ║
    └──────────► acellular capillaries ◄───────────╢ + local chemistry ║
                            │        ▲             ╚═══════════════════╝
                            │        │ pericyte loss (P3δ, ceramide,
                            │        │  gly-oxLDL — NOT leukostasis)
                            ▼
                   NONPERFUSION → HIF1A → P7 VEGFA/ANGPT2 → DME, PDR

    P9 NEUROVASCULAR UNIT  ── runs from S0, LARGELY OUTSIDE both hubs ──► BCVA
       Müller Kir4.1/AQP4 · GLUL loss · RGC apoptosis · microglia [D3] · [C2]
```

**Why the two-hub structure matters for scoring.** HUB 1 (ROS/GAPDH) is a *divergence* point:
block it and all four branches fall. HUB 2 (RELA) is a *convergence* point: block it and all four
branches' **inflammatory output** falls, but their non-inflammatory outputs — sorbitol osmotic
stress, basement-membrane crosslinking, occludin phosphorylation, TGFB1-driven fibrosis — do not.
A candidate's network position must be scored against *which* hub it touches and on which side.

---

## 2. (a) IS THE RETINAL EFFLUX ARM GENUINELY DRUGGABLE?

### 2.1 Who performs reverse cholesterol transport in the retina

The retina is a closed lipid compartment: **no lymphatics**, so every molecule of cholesterol that
enters or is synthesised must leave by transporter, by oxidation to a diffusible oxysterol, or not
at all. Four cell populations carry the load.

| Cell | Role in RCT | Acceptor it reaches | Status in diabetes |
|---|---|---|---|
| **RPE** | Principal drain. Basolateral **ABCA1/ABCG1** → plasma ApoA1/HDL across the **fenestrated** choriocapillaris. Also secretes ApoE. Handles the daily outer-segment phagocytic bolus (~10% of each photoreceptor OS per day — the heaviest per-mass lipid load in the body). | **Plasma acceptor, directly** — the only retinal cell with that privilege | ABCA1 down; cholesteryl-ester droplets accumulate; Bruch's accrues esterified cholesterol + apoB, plugging the outer drain from the far side |
| **Müller cell** | The retina's **ApoE source** (the astrocyte analogue). Secretes ApoE-containing HDL-like particles that are the *intraretinal* acceptor pool. ABCA1 lipidates them. | Makes its own acceptor locally | ABCA1 and LXR targets down; cholesterol and CE accumulate; gliosis |
| **Microglia / infiltrating macrophage** | The foam cell. Takes modified lipoprotein in via **CD36, OLR1 (LOX-1), MSR1**; must unload via ABCA1/ABCG1. | ApoE from Müller; ApoA1 only if barrier is leaking | **This is where the lesion lives** — see §2.3 |
| **Photoreceptor** | Net *producer* of cholesterol-rich shed membrane. Not an efflux cell. | — | VLC-PUFA/DHA content falls (P8.4) |

**Control layer:** NR1H3 (LXRα) and NR1H2 (LXRβ) transcribe *ABCA1, ABCG1, APOE*. Endogenous
ligands are oxysterols generated by **CYP46A1** (24S-OHC, the retina/brain-specific enzyme) and
**CYP27A1** (27-OHC). Side-chain oxidation is itself an export route — oxysterols cross membranes
unaided, which cholesterol does not. Per P8.3 the whole layer is **downregulated in diabetic
retina and in human diabetic donor eyes**, LXR agonism restores efflux and reduces retinal
inflammation and neovascularisation in models, and **ApoA1-mimetic peptides are protective in DR
models**. That is genuine mechanism-level validation of the arm, independent of any drug's
indication status.

### 2.2 The acceptor inventory — the half that is usually forgotten

**ABCA1 is a lipid translocase, not a pump to nowhere. Without an acceptor it does nothing.**
ABCA1 requires **lipid-poor pre-β ApoA1 or ApoE**; ABCG1 requires **mature HDL**. In the retinal
compartments:

- **Intraretinal (inner retina, OPL/Henle):** acceptor = Müller-derived ApoE, plus whatever ApoA1
  crosses a failed barrier. The physiological pool here is **small**. This is the compartment
  where hard exudate sits.
- **Subretinal / Bruch's:** acceptor = plasma ApoA1 and ApoE arriving across the fenestrated
  choriocapillaris. Larger pool — but Bruch's own lipid accumulation progressively obstructs it.

So the arm has **two serially required components** — transporter and acceptor — and a therapy
must supply whichever is limiting. **The diabetic lesion is reported on the transporter/LXR side.**
Hold that; it decides §2.4.

### 2.3 The foam-cell futile cycle — why the deposit is self-renewing

This is the mechanistic core of why hard exudate persists, and it is a *cycle*, not a deposit:

```
   extravasated apoB lipoprotein (LDL, VLDL remnant, small-dense LDL)
                          │
                          ▼  in-situ glycation + oxidation (P2 chemistry + P5 ROS)
                      gly-oxLDL ──────────────► direct toxicity to pericytes,
                          │                     endothelium, Müller, RPE (P8.2)
                          ▼  CD36 / OLR1 / MSR1
                  microglia / macrophage
                          │
                          ▼  ABCA1/ABCG1 ↓↓ (LXR axis suppressed), acceptor scarce
               ╔═══ CHOLESTEROL CANNOT LEAVE ═══╗
                          │
                          ▼  free-cholesterol / crystal / ER stress
                   NLRP3 → IL1B  +  foam-cell DEATH
                          │
                          ▼
                   lipid RE-RELEASED extracellularly
                          │
                          └──────────► back to CD36 uptake  ◄── SELF-RENEWING
```

**Consequence: the deposit regenerates itself from its own debris.** This is why anti-VEGF dries
the retina but does not clear exudate, and why exudate can *increase* as fluid resorbs. **Breaking
the cycle requires opening the exit, not closing the entrance** — see §3.3 for why blocking CD36
alone is the wrong move.

### 2.4 Is ABCA1's PPARα-inducibility enough to say the fibrates cover this? — **No.**

Three independent reasons, in descending order of force.

**(i) It is the transactivation limb, and Round 1 already declared that limb absent.**
PPARα raises ABCA1 **mostly indirectly**, via inducing *NR1H3* (LXRα) and the oxysterol ligand
pool, plus directly inducing *APOA1/APOA2*. Every step is **PPRE-driven transactivation** — the
same machinery as CPT1A, ACOX1, HMGCS2 and ANGPTL4. The synthesis's ANGPTL4 resolution is
symmetric and binding: *if retinal occupancy is too low to induce CPT1A and help, and too low to
induce ANGPTL4 and harm, it is too low to induce ABCA1 and clear.* An agent cannot claim the
efflux limb while disclaiming the ANGPTL4 limb — they are the same limb.

**(ii) A two-step relay is MORE occupancy-sensitive, not less.** PPARα → NR1H3 → ABCA1 multiplies
two fractional inductions. At ~0.3% fractional retinal occupancy (Target Analyst §4.2), a modest
fractional induction squared is negligible. And the **low-occupancy discount does not apply** —
the transrepression threshold advantage is specific to tethering at inflammatory promoters and
buys nothing for a PPRE.

**(iii) The one limb that *is* reachable points at the wrong half of the pathway.**
The disease agent's constructive idea — hepatic PPARα → APOA1 (engagement certain) → raised
circulating ApoA1 → a 28 kDa protein crosses a barrier already admitting a 500 kDa LDL particle →
**acceptor delivered to the site of retention** — is mechanistically coherent and is the only
efflux-side argument any candidate in the set possesses. Project data touches it: two CTD rows in
`evidence/ppara-interactions.tsv` encode *[pirinixic acid binds to and results in increased
activity of PPARA] promotes the reaction [APOA1 results in increased transport of cholesterol]*
(PMID:12595494) and a bezafibrate analogue — the **only efflux-adjacent rows in the entire
evidence pack**. But four things cut it down:

| Objection | Force |
|---|---|
| **Wrong half.** The diabetic lesion is reported on **ABCA1/LXR** (transporter). Adding acceptor to a cell whose pump is downregulated does not unload it. | **Decisive** |
| **Wrong HDL species.** ABCA1's substrate is **lipid-poor pre-β ApoA1**. Fibrates raise mature HDL-C; the pre-β pool moves far less. | Strong |
| **Magnitude.** Fibrate HDL-C raising is modest in absolute terms, and ApoA1 particle number rises less than HDL-C; interstitial concentration is plasma × permeability, so a ~10% plasma rise gives ~10% of a small base. | Strong |
| **Bootstrap.** It only operates in an eye leaking enough to admit lipoprotein — i.e. S2+, after deposition has begun. | Moderate (and the same stage logic as the supply limb, so not an extra penalty) |

> **Verdict on (a).** The retinal efflux arm is **biologically the correct gap and pharmacologically
> the harder half.** It is druggable at the *target-class* level — LXRα/β are nuclear receptors
> with crystallographically mapped pockets; CD36, OLR1 and MSR1 are cell-surface receptors;
> ApoA1/ApoE mimetic peptides are an established modality. It is **not currently deliverable**
> orally to Müller cells, microglia and RPE in the outer plexiform layer. **The fibrates do not
> cover it.** Their contribution is a modest acceptor-side nudge aimed at the non-limiting half of
> a two-component pathway — worth roughly half a scoring point, not coverage.
>
> **The structural statement:** PPARα's distinction is an engagement-certain compartment (liver)
> that is not the diseased compartment. The efflux arm has **no such escape** — its only useful
> compartment is the diseased one. That asymmetry, not target validity, is why the gap is open.

---

## 3. (b) WHAT WOULD AN EFFLUX-DIRECTED AGENT LOOK LIKE?

### 3.1 LXR agonists — the honest case against, in DR-specific form

The class liability is mechanistic, not idiosyncratic. Hepatic **LXRα → SREBF1 (SREBP-1c) →
FASN/SCD1/ACACA** → de novo lipogenesis → **hepatic steatosis and raised plasma VLDL-triglyceride**.
This has repeatedly stopped systemic LXR programmes.

**In this disease it is worse than a generic tox liability — it is self-cancelling:**

```
   LXR agonist ──┬──► retinal ABCA1/ABCG1 ↑  ──► efflux ↑        [WANTED]
                 │
                 └──► hepatic SREBP-1c ↑ ──► VLDL-TG ↑
                                           ──► TG-rich REMNANTS ↑ [THE TOXIC
                                                                   AFFERENT SPECIES, P8.2]
                                                        │
                                                        ▼
                                    MORE apoB particle supplied to a leaky barrier
```

A pan-LXR agonist would **improve the efferent limb while worsening the afferent limb of the same
axis**, in a population already defined by atherogenic dyslipidemia. It could plausibly net
negative. **This is a sharper objection than "LXR agonists cause steatosis" and it is specific to
DR.** Any efflux programme must clear this bar before anything else.

**Does isoform selectivity change it?**

| Design route | Assessment |
|---|---|
| **LXRβ-selective agonism** | **The rational route.** Hepatocyte lipogenesis is predominantly **LXRα**-driven; **LXRβ is ubiquitous** and carries much of the macrophage/glial efflux function — exactly the cells in §2.1. *Honest limits:* the two LBDs are ~78% identical, so real selectivity windows are hard-won and most "β-selective" compounds have modest ones; hepatocytes express some LXRβ, so β-bias reduces rather than abolishes the TG signal. Non-DR clinical experience with β-biased and partial agonists shows the TG signal attenuated, not removed. |
| **Partial agonism / tissue-selective modulator (an "SLXRM")** | Conceptually the right answer — exploit the same coactivator-recruitment dissociation that underwrites SPPARMα and dissociated glucocorticoids, to retain ABCA1 induction while leaving SREBF1 under-induced. Precedented as a design philosophy; **unproven for LXR**. |
| **Bypass LXR entirely — CYP46A1 induction** | Side-chain oxidation to 24S-hydroxycholesterol creates a species that **leaves by diffusion**, needing neither transporter nor acceptor. It is also an endogenous LXR ligand, so it recruits the pathway locally without systemic agonism. Retina/CNS-restricted enzyme → intrinsic tissue selectivity. `[EMERGING]`, no clinical chemical matter, but **the most elegant unexplored node in this arm.** |
| **ApoA1 / ApoE mimetic peptide** | Supplies the acceptor half directly. Protective in DR models per P8.3. **See §3.4 — this is the route with a realistic development path.** |

**The one encouraging asymmetry.** The PPARα pocket *mandates* a lipophilic carboxylic acid — the
chemotype §6.2 penalises hardest, which is the structural trap the Medicinal Chemist identified
(potency and access anti-correlated across the whole series). **The LXR pocket does not.** LXR
ligands are typically **neutral** lipophiles. Ionisation — the single worst BRB liability — is
therefore *not* locked in for this target class. The remaining obstacles (MW, cLogP > 5, PPB,
efflux-substrate risk) are ordinary medicinal-chemistry problems rather than a
structure-mandated contradiction. **An orally retina-penetrant LXRβ modulator is chemically
conceivable in a way an orally retina-penetrant PPARα agonist is not.** Target profile, to hand to
the SAR and Repurposing agents: neutral, **MW < 400, cLogP 2–4, TPSA < 70, HBD ≤ 2, not a
P-gp/BCRP substrate, PPB < 98%**, β-biased or partial, with **plasma TG as a mandatory
dose-limiting biomarker**.

### 3.2 Scavenger-receptor blockade — and a category error to correct

The brief frames CD36/LOX-1 blockade as "the complementary upstream option" to efflux. **At the
pathway level that is a category error, and the error matters.**

```
   AFFERENT SIDE                 CELLULAR COMPARTMENT              EFFERENT SIDE
   ─────────────                 ────────────────────              ─────────────
   plasma apoB ──► extravasation ──► CD36/OLR1/MSR1 ──► foam ──► ABCA1/ABCG1 ──► acceptor
   [A1-A5,B4,E1]                     ▲                   cell        ▲              ▲
                                     │                               │              │
                              "blockade" acts HERE          LXR agonist      ApoA1 mimetic
                              — INSIDE the afferent             │              │
                                 half, not the efferent         └──── THE REAL PAIR ────┘
```

Scavenger receptors are an **uptake** step. Blocking them does not accelerate egress — it is a
second supply-side intervention, positioned one compartment downstream of the first.
**The genuine complement to a transporter inducer is an acceptor donor, not an uptake blocker.**

**And blockade alone carries a wrong-sign risk.** Macrophage uptake is the **only catabolic route
for a retained apoB particle** in retina — there is no extracellular lipase that disassembles it.
Block CD36/OLR1/MSR1 and you convert "foam cells that die and re-release" into "**extracellular
gly-oxLDL that nothing removes**" — and extracellular gly-oxLDL is directly cytotoxic to pericytes
(the cell that dies first), endothelium, Müller cells and RPE (P8.2). You would be preserving the
toxin in order to protect the scavenger.

**What blockade legitimately buys is signalling, not clearance.** CD36 is a TLR4/TLR6 co-receptor
transducing oxLDL and cholesterol-crystal signals into **NLRP3 inflammasome** activation; LOX-1
drives endothelial NF-κB and NOX-derived ROS. Both are real P6 nodes. **That is an anti-
inflammatory claim and must be scored under P6, not under P8.3.** Calling it efflux coverage
double-counts.

### 3.3 Is hard exudate supply-limited or clearance-limited? — **Both, in sequence**

This is the determination that decides (c), so it is worth being exact.

| Phase | Rate-limiting step | Which agent acts | Enrichment biomarker |
|---|---|---|---|
| **Accretion (S1–S2, fresh exudate)** | **Influx** = barrier permeability × plasma apoB particle number. Lower particle number → proportionally lower deposition rate. | **Supply-side** (fibrate, ezetimibe, IPE) | high apoB / small-dense LDL, **no exudate yet** |
| **Persistence (weeks–months, established exudate)** | **Clearance** — and specifically the **macrophage futile cycle** of §2.3, not transporter capacity in the abstract. The deposit regenerates from its own debris. | **Efflux-side** (LXRβ, ApoA1 mimetic, CYP46A1) | **existing exudate**, extrafoveal |
| **Organised subfoveal plaque** | Neither — this is **fibrosis**, not a lipid problem | **Nothing.** Transcriptional pharmacology does not remove a scar. | — |

**What efflux does and does not address.** ABCA1/ABCG1 unload a *cell* of free cholesterol. They
do **not** disassemble an extracellular apoB particle and they do not dissolve an organised plaque.
So the efflux arm's genuine claim is precise: it **breaks the foam-cell futile cycle** and drains
the cholesterol fraction after macrophage catabolism, converting a self-renewing deposit into a
resorbing one. That is a real and sufficient claim — but it must not be overstated into "dissolves
hard exudate."

---

## 4. (c) WOULD AN EFFLUX AGENT COMBINE RATIONALLY WITH A SUPPLY-LOWERING AGENT?

**Yes, and the non-redundancy is structural rather than merely plausible.** Three arguments.

**(1) They act on the numerator and denominator of the same quotient.** For any compartment at
quasi-steady state:

```
                        influx_rate
   deposit_burden  ≈  ─────────────────
                      clearance_rate_k
```

A supply agent lowers the numerator; an efflux agent raises the denominator. Their effects are
**multiplicative**: halve influx *and* double clearance → one quarter of the steady-state burden,
where either alone gives one half. Two agents both lowering the numerator (e.g. fibrate +
ezetimibe) are **additive at best and sub-additive in practice**, since each successive apoB
reduction operates on an already-reduced base. **This is the cleanest available test of
redundancy and the two candidate classes fall cleanly on opposite sides of it.**

**(2) They cover different phases of the same lesion**, per §3.3 — and the supply agent's weakness
is precisely the efflux agent's indication. The disease agent flagged an uncomfortable trial-design
consequence for the fibrates: *the obvious enrichment biomarker (existing hard exudate) selects
patients in whom the supply mechanism is weakest.* The efflux agent inverts it exactly. **Opposite
enrichment criteria are independent evidence of mechanistic non-redundancy** — two agents selecting
the same patients are usually doing the same thing.

**(3) They engage different compartments.** The supply agent works from the liver (engagement
certain); the efflux agent must work in neural retina (engagement hard). This is a *development*
asymmetry, not a redundancy: there is no overlap to argue about because they are not in the same
tissue.

**Combination design implication.** Because the agents act in different phases, a trial enrolling
only fresh-exudate patients will under-read the efflux arm and one enrolling only established-plaque
patients will under-read the supply arm. **The combination should enrich for patients with both
fresh and persisting extrafoveal exudate — mid-trajectory S2–S3 — and should exclude organised
subfoveal plaque, where neither works.**

**Honest counter-arguments I considered and reject:**

- *"Both are 'lipid drugs' — this is one mechanism twice."* No. P8 is **eight sub-modules**, and
  the disease agent's matrix shows supply (P8.1) covered five-deep and efflux (P8.3) **empty**.
  Treating P8 as one axis is the error the sub-module decomposition exists to prevent.
- *"If supply falls far enough, clearance stops mattering."* Only for *new* deposition. It does
  nothing to an existing self-renewing deposit, which is the lesion that determines vision outcome.
- *"The toxic species is the particle, and efflux does not touch particles."* Correct and important
  — which is why the efflux agent's claim is scoped to the futile cycle (§3.3), and why it does
  **not** make the supply agent unnecessary. **That scoping is itself the argument for the
  combination:** neither mechanism covers the other's half of the lesion.

> **Verdict on (c): rationally additive and plausibly supra-additive, not redundant.** The
> combination is the correct therapeutic concept for the P8 axis. **The obstacle is that the
> efflux half does not exist as an approved oral drug** — and the honest consequence is that this
> finding is a *programme recommendation*, not a candidate ranking.

### 4.1 The route the run's framing is excluding

One non-obvious observation. The run's oral-only framing is correct for unmet need #1 (early,
systemic, population-scale). **It may be wrong for this specific arm.** The lesion the efflux agent
targets — persistent intraretinal exudate in exudative DME — occurs in patients who are **already
receiving intravitreal injections**. An intravitreal or suprachoroidal **ApoA1/ApoE-mimetic
peptide**, given as an adjunct at the same visit, adds **no new procedure** and bypasses the BRB
argument entirely — the whole of §2.1 and §3.1's delivery problem evaporates. Peptide mimetics are
protective in DR models (P8.3), and a peptide that must act in the interstitium (supplying an
acceptor) does **not** need to enter cells.

**This is the most developable version of the efflux concept and no agent in this run has named
it.** It serves unmet need #5 (hard exudate) and #2 (non-VEGF mechanism for incomplete responders)
without worsening #4 (treatment burden). Recommended to the Repurposing Strategist and the
Clinical agent as a distinct programme track.

---

## 5. (d) NETWORK POSITION OF EACH CANDIDATE RELATIVE TO THE BROWNLEE NODE

### 5.1 The position map

| Cand. | Position relative to HUB 1 (ROS/GAPDH divergence) | Position relative to HUB 2 (RELA convergence) | Verdict |
|---|---|---|---|
| **A1/A2 Fenofibric acid / fenofibrate** | **Outside the quadrant.** P8 is fed by systemic lipoprotein supply and by lipid-derived DAG/ceramide chemistry, not by glycolytic backup. Not a downstream branch at all. | **At the node**, by transrepression — marginal occupancy, threshold-advantaged | **Escapes the single-branch criticism on topology** |
| **A3 Pemafibrate** | Same | Same, and the only ligand potent enough to plausibly occupy it retinally | Same, with best node-occupancy case |
| **A4 Elafibranor** | Same | Same + PPARδ arm | δ adds P8.8 FAO **and** a pro-angiogenic/ANGPTL4 limb — **directionally dirtier** |
| **A5 Seladelpar** | Same | Shares the machinery | δ is the most abundant retinal PPAR and pro-angiogenic — **plausibly net wrong-signed in the compartment of interest** |
| **B1 Linoleic acid** | — | Weak, non-selective | **Net adverse:** supplies arachidonate for P8.6 (ALOX5/12/15, PTGS2) and 4-HNE for P8.7, in a retina whose n-6:n-3 shift is part of the lesion |
| **B2 α-linolenic acid** | — | Weak | Right direction; ALA→EPA conversion <5–10% in humans, so magnitude ≈ 0 |
| **B3 Linalool** | — | — | One genetic-dependency datum at SLC27A4 (P8.8 periphery). Access without position |
| **B4 Icosapent ethyl** | — | Indirect | **P8.6 RESOLUTION — the one territory nothing else in the set occupies.** Enables termination rather than blocking initiation. Underrated on this axis |
| **C1 Quercetin** | Nominal everywhere | Nominal | Direction-incoherent at PPARα; dual ABCB1/ABCG2 efflux substrate `[DATA]`; counts are a study-depth artifact per the matrix's own header. **Real coverage ≈ 0** |
| **C2 Melatonin** | Scavenging — the penalised prior | Weak | Best genuine claim is MT1/MT2 on Müller/microglia (P9), not antioxidant. Access without a node of consequence |
| **D1 Epalrestat** | **One branch (P1), downstream of divergence — the exact archetype §4.4 penalises** | — | Worst position in the set. **Plus an unflagged wrong-sign risk — see §5.3** |
| **D2 Dimethyl fumarate** | **On the disposal arm, one step lateral to the node** — see §5.2 | Partial, via NRF2 transrepression of IL6/IL1B | Broadest genuine coverage; the node claim is **half right** |
| **D3 Minocycline** | — | Microglial amplifier downstream of the node | Amplifier, not node; mechanism undefined. One upgrade: microglia **are** the foam cell of §2.3, so deactivation is an indirect, partial touch on exudate biology |
| **D4 Candesartan cilexetil** | **Upstream-lateral:** AT1R → NOX1/2/4 → ROS feeds HUB 1 from **outside** glycolysis | Damps it, from the **luminal** side — no BRB crossing needed | **Second-best position in the set**, and the only non-fibrate with an engagement-certain compartment |
| **E1 Ezetimibe** | Outside | None | Single node (P8.1 supply), certain, narrow — see §8 |

**Does PPARα escape the single-branch criticism by being a transcriptional hub?** The Target
Analyst's answer — escapes the *topological* version, not the *pharmacokinetic* version, and PKCβ
was also argued as a hub and still failed — is correct and I will not restate it. **The pathway-
level refinement I would add is that the hub frame is the wrong analytical tool here entirely.**

> PPARα is **not a node in the damage network**. It is a node in a *separate, protective regulatory
> network* that intersects the damage network at exactly two places: P8 (lipid supply/handling) and
> RELA (HUB 2). A hub's leverage is properly scored by **how much damage flux passes through it** —
> that is what makes AKR1B1 a bad target and RELA a good one. **No damage flux passes through
> PPARα at all.** Its leverage is set by how much protective programme it can *induce*, which is
> governed by occupancy and receptor abundance, not by network topology. **You cannot do flux
> accounting on PPARα, and arguments that try to are measuring the wrong quantity.** This is why
> the hub debate in Round 1 was unresolvable: both sides were using a frame the target does not fit.

### 5.2 Dimethyl fumarate's claim to act *at* the node — assessed rigorously

**The claim.** MMF alkylates KEAP1 (notably Cys151) → NRF2 stabilisation and nuclear translocation
→ ARE programme (HMOX1, NQO1, GCLC/GCLM, GSR, TXN, SRXN1, **GLO1**, GPX4) → restores the
antioxidant arm at HUB 1, hitting P1–P4 through their shared cause rather than branch by branch.

**Where the claim is strong — four points, and they are real:**

1. **The NRF2 output genuinely spans multiple Brownlee branches via their common cause, not via
   the branches.** GLO1 induction detoxifies methylglyoxal (**P2**, and GLO1 activity is
   specifically depressed in diabetes); GCLC/GSR restore the GSH pool that P1's NADPH drain
   depletes (**P1's consequence, addressed without touching AKR1B1**); GPX4/ALDH2/GSTs clear the
   P8.7 aldehyde load. **This is the only candidate in the set that covers P8.2 (modification
   capacity) and P8.7 (peroxidation) at all.**
2. **The diabetic retina is NRF2-*deficient*** — impaired nuclear translocation despite preserved
   total protein, increased KEAP1 binding (P5). Restoration, not supraphysiological stimulation —
   the same favourable setup the model grants PPARα.
3. **NRF2 directly represses *IL6*/*IL1B***, so it touches HUB 2 as well. Two hubs, one agent.
4. **The covalent/cumulative argument is the one thing exempt from the free-drug/EC50 arithmetic,
   and that exemption is genuine.** MMF is a Michael acceptor; KEAP1 modification is irreversible
   on the timescale of the protein's half-life, so occupancy integrates **exposure × time (AUC)**
   and resets only by resynthesis. A compound that never exceeds EC50 instantaneously can still
   modify a meaningful KEAP1 fraction under chronic daily dosing. **No other candidate in the set
   has this pharmacology.** The chemist and ADMET agents are right to weight it.

**Where the claim is weak or wrong — and this is the part Round 1 did not do:**

1. **It does not act at the node. It acts on the disposal arm, one step lateral.** The node is
   mitochondrial superoxide **production**. NRF2 increases superoxide **disposal**. These are
   different positions, and the gap between them is occupied by one specific enzyme:
   **SOD2 — the only antioxidant enzyme positioned exactly at the node — is epigenetically
   silenced (H3K9me, DNMT1-mediated) in diabetic retina as a core component of metabolic memory
   (P5). SOD2 is only weakly NRF2-dependent, and promoter methylation is not reversed by an NRF2
   dimer binding an ARE.** DMF's programme is overwhelmingly **cytosolic** — it cleans up
   superoxide-derived products after they leave the mitochondrion; it does not reduce production
   inside it. **The single enzyme that would make the "at the node" claim true is the one the
   mechanism cannot restore.** Demote the claim accordingly: *near* the node, on the disposal side,
   with real multi-branch output.
2. **It sits uncomfortably close to the brief's penalised prior** ("antioxidant as sole mechanism —
   repeatedly null in DR"). The legitimate defence is that DMF is a **transcriptional** antioxidant
   — it induces catalytic enzymes with turnover — rather than a **stoichiometric** scavenger
   consumed 1:1, which is what the failed vitamin trials deployed. That distinction is real and is
   DMF's strongest rebuttal. It is also a mechanistic argument, and the failed trials had
   mechanisms too. Net: the prior is weakened, not discharged.
3. **A wrong-sign risk at the node itself, which I believe is new to this run.** MMF has a
   well-characterised NRF2-**independent** mechanism: it **succinates GAPDH at Cys152**, inactivating
   it — this is how DMF suppresses aerobic glycolysis in activated immune cells and is thought to
   underlie part of its immunomodulation.

   > **In a disease whose central pathogenic lesion *is* GAPDH inhibition (the Brownlee node), and
   > whose photoreceptors are obligately glycolytic (Warburg-like, P8.8/P9), a drug that covalently
   > inhibits GAPDH is a wrong-sign risk at the exact node it claims to protect.**

   This does not kill the candidate: the immune-cell effect occurs in cells with extreme glycolytic
   flux and high local drug exposure, and retinal MMF concentration is likely far lower. But it
   converts "acts at the node" into "**acts near the node, possibly in both directions**," and it
   demands a specific preclinical readout — **retinal GAPDH activity and photoreceptor ERG
   (a-wave) under chronic MMF**, run alongside the NRF2 target panel. Cheap, and it is the
   experiment that decides whether the headline claim survives.
4. **The access argument rests on an uptake-transporter hypothesis.** MMF is a monocarboxylate
   anion at pH 7.4; the "best BRB physicochemistry in the set" claim depends on MCT1/MCT2 or
   NaDC-mediated uptake. The model states flatly that the retina has no OATP-analogous uptake
   system (§6) — though **MCTs genuinely are present and central to the photoreceptor–RPE lactate
   shuttle**, which makes the hypothesis materially more plausible here than for an aryl acid. It
   remains unverified and the disease agent already named it as the falsifier.

### 5.3 An unflagged wrong-sign risk for epalrestat

**AKR1B1 is listed in the disease model's own P8.7 table as a 4-HNE reductase** — aldose reductase
detoxifies the reactive aldehydes that the retina's extreme PUFA load generates. **An aldose-
reductase inhibitor therefore impairs retinal 4-HNE clearance** while blocking the polyol branch.
In a tissue the model calls maximally substrate-loaded for lipid peroxidation, that is a specific
adverse network consequence, not a theoretical one. It compounds an already-poor position (one
branch, downstream of divergence, with negative human clinical validation of the mechanism per
§4.4). I find no Round 1 agent raised it.

---

## 6. (e) THE LEUKOSTASIS CASCADE — HUB OR BRANCH?

### 6.1 The cascade, precisely

```
  AGE/RAGE (P2) ─┐
  PKC (P3)       ├─► NF-κB / RELA ──► ICAM1 ↑ (+ VCAM1, SELE, SELP)
  ROS (P5)       │   in retinal           │   on retinal capillary endothelium
  gly-oxLDL/CD36 │   capillary            │
  AT1R (D4)     ─┘   endothelium          │   circulating PMN/monocyte:
                                          │   CD11a/CD18 (ITGAL/ITGB2) ↑
                                          ▼
                              FIRM ADHESION UNDER SHEAR
                              (requires a ligand-DENSITY THRESHOLD ◄── nonlinearity)
                                          │
                                          ▼
                          CAPILLARY PLUGGING  (lumen ≈ leukocyte diameter)
                              ┌───────────┴───────────┐
                     transient│                       │sustained
                              ▼                       ▼
                    reperfusion ROS burst    FAS / FASLG-mediated
                              │              ENDOTHELIAL APOPTOSIS
                              └───────────┬───────────┘
                                          ▼
                                 ENDOTHELIAL DROPOUT
                                          ▼
                       ★ ACELLULAR CAPILLARIES ★  ◄──── pericyte-side route:
                     (the quantitative substrate         PKCδ/SHP-1→PDGFRβ,
                      of ischemia)                       ceramide, gly-oxLDL
                                          ▼              — NOT leukostasis
                               CAPILLARY NONPERFUSION
                                          ▼
                              retinal ischemia → HIF1A
                                          ▼
                         VEGFA, ANGPT2, EPO, plasma kallikrein
                              ┌───────────┴───────────┐
                              ▼                       ▼
                     DME (permeability)        PDR (neovascularisation)
                                                      ▼
                                              S5 fibrovascular traction
```

### 6.2 How much of DR's trajectory runs through it?

**For a hub:**
1. It is the **production mechanism for the ischemia that drives everything after S3.** Acellular
   capillaries → nonperfusion → HIF → VEGF is the main sequence to PDR. To the extent leukostasis
   dominates acellular-capillary formation, **the entire S3→S4→S5 arm is downstream of it** —
   which is most of the disease's severe morbidity.
2. **ICAM1 or CD18 blockade/knockout prevents both leukostasis and BRB breakdown** in models — the
   model calls this "one of the cleanest causal chains in the field." **Two outputs from one
   intervention** is the signature of a hub, not a branch.
3. **Genuine convergence:** RAGE (P2), PKC (P3), ROS (P5), oxLDL/CD36 (P8.2) and AT1R all feed
   RELA. Five modules, one node, and it sits **downstream of convergence** — the exact opposite
   topological position to AKR1B1.
4. **Modality-level corroboration from the disease model's own standard-of-care section:**
   intravitreal **corticosteroid** — a broad, non-VEGF-targeted NF-κB-suppressing modality — is
   effective in DME **including in some anti-VEGF non-responders** (P6, §4.1). That is the
   strongest available evidence that suppressing this node carries real therapeutic weight.
5. **A threshold nonlinearity amplifies weak signals here.** Firm adhesion under shear requires
   ICAM1 **surface density** above a threshold, so a 20–30% ICAM1 reduction can yield a
   disproportionately larger reduction in leukostasis. The inflammatory limb's phenotypic output
   amplifies a modest molecular effect; the metabolic limb's does not (a 20% CPT1A rise ≈ 20% FAO
   flux). **This is why a marginal-occupancy transrepression signal is worth more here than
   anywhere else in the network.**

**For a branch:**
1. **Pericyte loss is not downstream of it.** Pericyte dropout — the earliest, most characteristic
   DR lesion — is driven by polyol osmotic stress, PKCδ/SHP-1→PDGFRβ, ceramide (P8.5) and
   gly-oxLDL toxicity (P8.2). **Leukostasis kills endothelium, not pericytes.** An acellular
   capillary is a tube with *neither* cell, and a major parallel route reaches it from the
   pericyte side, bypassing this cascade entirely.
2. **S0 neurodegeneration is upstream and parallel.** RGC apoptosis, Müller gliosis, GLUL loss,
   Kir4.1/AQP4 uncoupling → cytotoxic edema — none requires leukostasis. Per P9, **visual function
   does not track vascular anatomy.**
3. **DME has five phenotypes**; leukostasis-driven inflammation is **one**. The Müller-cytotoxic
   and outer-BRB-pump-failure phenotypes lie wholly outside it.
4. **Adjacent negative precedent:** §4.4 lists intravitreal integrin antagonists as
   "mixed-to-disappointing" with the lesson that "adhesion-axis targeting has not yet delivered."
   *Fair scoping:* the agents tested were largely αvβ3/α5β1, angiogenesis-directed, **not**
   CD18/ICAM1 — so this is an adjacent caution, not an identical refutation. It should lower
   confidence, not close the question.

> **Verdict on (e): a hub for the vascular-ischemic trajectory (S2→S5), a branch for the
> neuro-glial trajectory (S0→visual function).** It is the dominant single contributor to
> acellular-capillary formation — but it supplies perhaps half the route to that lesion, with the
> pericyte axis supplying the other half, and a minority of the route to vision loss in any given
> patient, because so much vision loss is neural and edematous.

**The scoring consequence, stated operationally:**

> **The surviving retinal limb of the PPARα hypothesis — transrepression → ICAM1 ↓ → leukostasis ↓
> — predicts a DRSS (vascular) effect without a matched BCVA (neural) effect.** A programme powered
> on acuity will miss it; a programme powered on DRSS step-change and acellular-capillary/
> nonperfusion-area imaging will see it if it is there. This is a concrete, falsifiable,
> design-level prediction that follows from the hub/branch split and not from any drug's status.

---

## 7. (f) COMBINATION COVERAGE

### 7.1 Coverage matrix

`██` substantive and reachable · `▒▒` real but exposure-limited or indirect · `░░` none · `⚠` wrong-signed

| Candidate | P1 polyol | P2 AGE | P3 PKC | P5 ROS/NRF2 | **P6 RELA/leuko** | P7 VEGF | **P8.1 supply** | **P8.3 EFFLUX** | P8.4/.6 PUFA-resolution | P8.7 peroxidation | P9 NVU |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fenofibric acid | ░░ | ░░ | ▒▒ | ▒▒ | ▒▒ | ░░ | **██** | ▒▒ | ░░ | ░░ | ▒▒ |
| Fenofibrate | ░░ | ░░ | ▒▒ | ▒▒ | ▒▒ | ░░ | **██** | ▒▒ | ░░ | ░░ | ▒▒ |
| Pemafibrate | ░░ | ░░ | ▒▒ | ▒▒ | ▒▒ | ░░ | **██** | ▒▒ | ░░ | ░░ | ▒▒ |
| Elafibranor | ░░ | ░░ | ▒▒ | ▒▒ | ▒▒ | **⚠** | **██** | ▒▒ | ░░ | ░░ | ▒▒ |
| Seladelpar | ░░ | ░░ | ░░ | ▒▒ | ▒▒ | **⚠** | ▒▒ | ░░ | ░░ | ░░ | ░░ |
| Linoleic acid | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | **⚠** | **⚠** | ░░ |
| α-Linolenic acid | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ▒▒ | ░░ | ▒▒ | ░░ | ░░ |
| Linalool | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ▒▒ | ░░ | ░░ | ░░ | ░░ |
| Icosapent ethyl | ░░ | ░░ | ░░ | ░░ | ▒▒ | ░░ | ▒▒ | ░░ | **██** | ▒▒ | ░░ |
| Quercetin | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ |
| Melatonin | ░░ | ▒▒ | ░░ | ▒▒ | ▒▒ | ░░ | ░░ | ░░ | ░░ | ▒▒ | ▒▒ |
| Epalrestat | ▒▒ | ▒▒ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | **⚠** | ░░ |
| **Dimethyl fumarate** | ▒▒ | **██** | ░░ | **██** | ▒▒ | ░░ | ░░ | ░░ | ░░ | **██** | ▒▒ |
| Minocycline | ░░ | ░░ | ░░ | ░░ | ▒▒ | ░░ | ░░ | ▒▒ | ░░ | ░░ | ▒▒ |
| **Candesartan** | ░░ | ▒▒ | ▒▒ | **██** | **██** | ▒▒ | ░░ | ░░ | ░░ | ░░ | ▒▒ |
| Ezetimibe | ░░ | ░░ | ░░ | ░░ | ░░ | ░░ | **██** | ░░ | ░░ | ░░ | ░░ |
| — *(no candidate)* | | | | | | | | **✗ GAP** | | | **✗ GAP** |

**Gap summary.** Well-covered: **P8.1 supply** (six candidates — over-covered relative to need).
Thinly covered: P6 (two reachable). **Empty: P8.3 efflux** (§2–4) and **P9 Müller Kir4.1/AQP4**
(no chemical matter exists — which is why that gap persists despite its size).

### 7.2 Recommended pair — **Fenofibric acid (or pemafibrate) + Dimethyl fumarate**

Supply-side × node-lateral. The non-redundancy argument is the same multiplicative one as §4,
applied to a different pair of terms:

> **The toxicity of extravasated lipoprotein ≈ (particle number) × (in-situ modification
> capacity).** The fibrate lowers the first term, from the one compartment it certainly engages.
> DMF lowers the second, from inside the neural retina — the compartment the fibrate cannot reach.
> **Multiplicative, not overlapping.** Neither agent can substitute for the other, because neither
> can act in the other's compartment.

| | Contributes **uniquely** | Cannot do |
|---|---|---|
| **Fibrate** | Lowers **apoB/remnant particle flux** with certain hepatic engagement — the only mechanism in the set with certain target engagement **anywhere**. Raises ApoA1 (acceptor, partial). Transrepresses at HUB 2. | Nothing inside neural retina. Does not change modification capacity. |
| **DMF** | Blocks **gly-oxLDL formation** (P8.2) and detoxifies aldehyde products (P8.7, GPX4/ALDH2/GST) — **the only candidate covering either**. GLO1 (P2). GSH restoration (P1's consequence). Acts in the neural retina. | Cannot reduce what arrives. No systemic lipoprotein action at all. |

**Brownlee geography is complementary too:** the fibrate is *outside* the quadrant (P8) plus at
HUB 2; DMF is on the disposal arm *upstream* of the four branches plus partially at HUB 2. The
only overlap is anti-inflammatory action by two different routes (PPARα tethering vs NRF2
repression of *IL6*/*IL1B*) — and that overlap is **convergent reinforcement on a
threshold-nonlinear endpoint**, which is the good kind of redundancy (§6.2 point 5).

**Where this pair dies if it dies:** not on the network axis, but on **monitoring burden in an
asymptomatic population** — LFTs/creatinine for the fibrate, lymphocyte counts and PML vigilance
for DMF, stacked, for years, in people who can see fine. Round 1's clinical axis scored DMF 3.0
for exactly this. **My axis cannot rescue it and should not pretend to**; the lexicographic gate
must multiply, not average.

### 7.3 Lower-risk alternative — **Fenofibric acid + Candesartan cilexetil**

| | Contributes uniquely | Overlap |
|---|---|---|
| **Fibrate** | P8.1 supply (certain) | Both damp HUB 2 / ICAM1 |
| **Candesartan** | Removes an **upstream ROS source** feeding HUB 1 from outside glycolysis (AT1R → NOX1/2/4), plus EDN1↓/NOS3↑ vascular tone — and does it at the **luminal endothelial surface**, needing no BRB crossing. The only non-fibrate with an engagement-certain compartment. | as above |

Partially redundant at HUB 2 but by genuinely different upstream routes (ligand-activated nuclear
receptor tethering vs GPCR signal removal), and candesartan uniquely removes a ROS *source* rather
than its products. Lower network coverage than §7.2 — it leaves P8.2, P8.7 and P8.3 all uncovered
— but near-zero development risk in a population that is near-universally hypertensive and
CKD-burdened. **The pragmatic choice; the §7.2 pair is the mechanistically stronger one.**

### 7.4 Best available third — and the one that should be there instead

**Best third from the actual set: Icosapent ethyl.** It occupies **P8.6 resolution** — E-series
resolvins, arachidonate displacement from membrane phospholipid — which *nothing else in the set
touches*, and the model's own framing is that **failure of inflammation resolution, not just excess
initiation, is the under-exploited angle in DR**. On pure coverage grounds it is the correct third.
Its engagement axis is weak (Round 1 ADMET 3.0) and the Clinical agent must gate it.

**The third that should be there: an efflux agent.** I decline to pad the triple. The honest
statement is:

> **Fibrate (supply) + DMF (modification) + LXRβ-biased modulator or ApoA1-mimetic (efflux) is the
> combination that covers the P8 axis completely — afferent flux, in-situ modification, efferent
> clearance. Two of the three exist as approved oral drugs. The third does not, and finding or
> building it is the highest-value structural recommendation this analysis produces.**

**And the combination to avoid: fenofibrate + ezetimibe.** Both lower the same afferent term by
different routes — **maximally redundant on this axis** (§4, argument 1), sub-additive, and it
would consume a trial arm to answer a question the single-agent comparison already answers.
Ezetimibe belongs in the design as a **comparator arm**, never as a combination partner.

---

## 8. (g) EZETIMIBE'S PATHWAY POSITION — IS IT A GENUINE DISCRIMINATOR?

### 8.1 The two paths to the shared output

```
 EZETIMIBE ─┤ NPC1L1                      FIBRATE ─► PPARα (liver, OATP-concentrated)
   (enterocyte brush border,                   │
    hepatocyte canaliculus)        ┌───────────┼────────────┬──────────────┐
            │                      ▼           ▼            ▼              ▼
  ↓ dietary+biliary sterol      ↑ LPL      ↓ APOC3      ↑ APOA1     transrepression
     absorption                    │           │            │        (RELA/AP-1, FGF21)
            ▼                      └─────┬─────┘            │              │
  ↓ hepatic cholesterol pool             ▼                  ▼              ▼
            ▼                   ↓ TG-rich REMNANTS    ↑ ApoA1/HDL    ↓ ICAM1/TNF/IL6
  ↑ SREBP-2 → ↑ LDLR                     │             (ACCEPTOR,         (HUB 2)
            ▼                            │              §2.4)              │
  ↑ LDL particle clearance               │                  │              │
            │                            │                  │              │
            └──────────────┬─────────────┘                  │              │
                           ▼                                │              │
          ╔═══ CONVERGENCE: ↓ plasma apoB particle number ═══╣              │
                           ▼                                │              │
          ↓ apoB flux across a leaky BRB → ↓ intraretinal retention (P8.1)  │
                                                            │              │
                       NOT SHARED ────────────────────────► │ ◄────────────┘
```

**Shared:** exactly one output node — *plasma apoB particle number*.
**Not shared:** the entire path to it (gut transporter + SREBP-2/LDLR vs hepatic nuclear receptor +
LPL/APOC3), **plus two fibrate outputs ezetimibe does not possess at all** — ApoA1/acceptor raising
(§2.4) and transrepression/FGF21.

### 8.2 Assessment — three parts

**(1) At the pathway level it is a genuine discriminator, and better than the brief credits.** The
paths share **no node** upstream of the convergence — as far apart as two apoB-lowering mechanisms
can be. And critically, they converge on a **plasma concentration**, not on a signalling node.
That is an *observable you can measure and dose-match*, which makes this control experimentally
tractable in a way mechanistic-convergence controls usually are not. **Match on apoB, compare
retinal outcome** is a clean experiment in principle.

**(2) The species mismatch is real and is larger than "LDL vs remnants" conveys.** The model's
toxic species is the **small, dense, glycation- and oxidation-prone apoB particle**. Ezetimibe
lowers LDL-C chiefly by raising **LDLR**-mediated clearance — and **small dense LDL has reduced
LDLR affinity and is preferentially retained** relative to large buoyant LDL. Fibrates do the
opposite: by lowering triglyceride and reducing CETP-mediated remodelling, they **shift LDL from
small-dense toward large-buoyant**. So on the specific toxic subfraction, **the two agents may move
in opposite directions even while both "lower apoB."**

> **Operational fix, and it should be a design requirement, not a footnote: match on apoB particle
> number AND LDL particle size/subfraction distribution (NMR or ion-mobility), never on LDL-C.** If
> apoB matches but the size distributions diverge, the exposure that matters is **not** matched and
> a null result is uninterpretable.

**(3) Asymmetric informativeness — the point the orchestrator needs.**

| Result | Inference | Informativeness |
|---|---|---|
| **Ezetimibe matches the fibrate** | The receptor is not doing the work; this is a lipid-supply hypothesis wearing a receptor's name. And it is *good* news operationally — ezetimibe is cheaper, safer in CKD, and carries no statin-myopathy interaction in a universally statin-treated population. | **HIGH — near-decisive** |
| **Ezetimibe fails, fibrate works** | Ambiguous between **three** readings: (i) the receptor matters (transrepression/retinal limb), (ii) remnants matter and LDL does not, (iii) the particle-size mismatch of (2). **This pair cannot separate them.** | **LOW** |

> **E1 is a strong positive control and a weak negative one** — the inverse of seladelpar's failure
> mode (weak positive, ambiguous negative), and a real improvement on it. It is the right addition
> and should **not** be described as decisive. **The matched result is informative; the mismatched
> result is not.**

**Pathway-level verdict:** ezetimibe occupies exactly one node — P8.1 supply — with certainty, and
nothing else. On the therapeutic coverage axis that is narrow, and it is narrow in the module that
is *already* the best-covered in the set. On the **experimental-design** axis it is the single most
valuable addition made to this run.

---

## 9. SCORING RULE AND HONEST AXIS LIMITATION

My axis is **pathway-network coverage and position**: how much disease-relevant network a candidate
touches, whether its position is hub/branch/upstream/downstream, and whether its touches are
directionally correct. I apply a **modest** discount for compartment-reachability — a position you
cannot reach is not a position — but I do **not** re-score exposure, which is the ADMET axis.

**Declared bias:** this axis systematically **favours broad-coverage, upstream agents (DMF) and
disfavours narrow, certain ones (ezetimibe, candesartan)**. That is the correct behaviour for this
axis and the wrong behaviour for a composite. Per the Clinical agent's instruction in the Round 1
synthesis, **these scores must be MULTIPLIED with the engagement and viability axes, not averaged
with them.** DMF at 7.0 here alongside clinical 3.0 is not a 5.0 candidate; it is a candidate whose
biology is excellent and whose deployability is the open question.

**Data basis:** the project data contains **zero rows** for ABCA1, ABCG1, NR1H2, NR1H3, CD36, OLR1,
MSR1, APOA1, APOE, CYP46A1 or CYP27A1 in `compound-dr-target-matrix.tsv` and
`ppar-class-drug-properties.tsv`, and **two** in `ppara-interactions.tsv` (both PPARA→APOA1
cholesterol-transport CTD statements, §2.4). **The pathway arm this analysis is about is as
invisible to the run's data as the PPAR effector genes are.** Every efflux-arm conclusion here is
therefore `knowledge-based`, and I have marked it so.

---

## 10. FALSIFIERS FOR SCORES ≥ 7

| Candidate | What would falsify the score |
|---|---|
| **Fenofibric acid (7.0)** | A chronic diabetic-rodent fibrate study showing retinal ICAM1/TNF/leukostasis **unchanged** while plasma apoB falls — that would void the HUB 2 transrepression limb and leave only P8.1, dropping it to ~5. Equally: demonstration that intraretinal lipoprotein retention is governed by permeability alone and is insensitive to plasma particle number over the achievable range. |
| **Pemafibrate (7.0)** | Same, plus: measured retinal pemafibrate concentration showing hepatoselectivity is near-total (retinal Kp,uu < 0.05), which would remove the only reason to prefer it over A1 on this axis. |
| **Dimethyl fumarate (7.0)** | (i) Retinal **GAPDH activity falls** or photoreceptor ERG a-wave degrades under chronic MMF — the §5.2 wrong-sign risk realised, which would invert the headline claim; (ii) MMF shown to be an MCT/NaDC **non**-substrate with efflux ratio > 2, collapsing neural-retina access and removing the compartment advantage that is the entire basis of the score; (iii) NRF2 target induction (HMOX1/NQO1/GCLC) **absent** in diabetic retina at tolerated doses despite systemic induction. |

---

## 11. CROSS-CUTTING OBSERVATIONS

1. **The efflux gap is real, is correctly identified, and is not fillable from this candidate set.**
   The fibrates' ABCA1 claim fails on Round 1's own transactivation logic. The honest output is a
   **programme recommendation** (LXRβ-biased modulator, or ApoA1/ApoE mimetic — §3.1, §4.1), not a
   candidate score.
2. **The hub frame does not fit PPARα** (§5.1). No damage flux passes through it; it is a node in a
   protective network that *intersects* the damage network twice. Round 1's hub debate was
   unresolvable because both sides used a frame the target does not fit.
3. **Two unflagged wrong-sign risks:** MMF succinating GAPDH at the Brownlee node (§5.2), and
   AKR1B1 inhibition impairing 4-HNE detoxification (§5.3). Both are testable and both belong in
   the Safety Pharmacologist's scope.
4. **The DMF "acts at the node" claim is half right.** It acts on the **disposal** arm, one step
   lateral. **SOD2 — the only antioxidant enzyme at the node — is epigenetically silenced and is
   not NRF2-rescuable.** Demote the claim; keep the candidate.
5. **The leukostasis cascade is a hub for the vascular trajectory and a branch for the neural one**,
   which yields a concrete design prediction: **DRSS effect without matched BCVA effect** (§6.2).
6. **Icosapent ethyl is the most underrated candidate on this axis.** It occupies the resolution
   territory alone, and the model itself names resolution failure as the under-exploited framing.
   Round 1's mean of 4.92 understates its network position; its engagement axis is the real problem.
7. **Over-coverage is itself a finding.** Six of sixteen candidates act on P8.1 supply. The set was
   built around a hypothesis and has inherited that hypothesis's blind spot — it is dense where the
   thesis is and empty where the thesis's own disease model says the gap is.

**Question for other agents.** *To the Drug Repurposing Strategist:* is there an **approved,
neutral, MW < 400 LXRβ-biased or partial LXR agonist**, or any approved **CYP46A1 inducer**,
anywhere outside this set? The LXR pocket does not mandate an acid — so unlike the PPARα scaffold
problem (§3.1), this one is not structurally foreclosed, and a hit would fill the run's largest
declared gap. *To the Safety Pharmacologist:* MMF-mediated GAPDH succination in an obligately
glycolytic photoreceptor, and AKR1B1 inhibition versus 4-HNE clearance — both §5.2/§5.3.

---

## 12. BLINDING COMPLIANCE

**Files read:** `disease-brief.md`; `round1-synthesis.md`; `disease-model.md` (§2 Axis B P1–P9 in
full, S0, S2, §4.4, §5.2, §6.2–6.3); `.claude/skills/pathway-analyst/SKILL.md`;
`agents/p1-disease.md` and `agents/p1-target.md` (targeted excerpts); `evidence/ppara-interactions.tsv`,
`evidence/compound-dr-target-matrix.tsv`, `evidence/ppar-class-drug-properties.tsv`.

**Files NOT read, deliberately:** `data/holdout/` (any file), `data/processed/chembl_approved_drugs.csv`,
anything named `answer-key*`, any unblinded `data/processed/` table. I did not use git history, git
objects, or any other route to recover redacted values, and I made no attempt to infer which rows
were redacted.

**Rule 2 compliance.** I did not use, assert or cite the DR/DME indication, approval,
guideline status or trial history of any of the sixteen candidates. Every candidate's DR status was
treated as unknown throughout, including in the combination design (§7) and the control analysis
(§8).

**Disclosures — knowledge-adjacent judgments, including negative ones:**

1. **Intravitreal corticosteroid efficacy in DME** (§6.2, point 4) is cited as evidence that
   NF-κB-node suppression carries therapeutic weight. This is **standard-of-care content supplied
   by the disease model itself** (P6 and §4.1), concerning a modality that is not a candidate in
   this set. Not a candidate-status claim, but disclosed because it is DR-specific clinical fact.
2. **LXR agonist programme failures on hepatic steatosis and hypertriglyceridemia** (§3.1) is
   non-DR clinical knowledge about a target class that is not in the candidate set — allowed under
   Rule 3, and the compound class is not a candidate.
3. **ApoA1-mimetic peptides protective in DR models** (§2.1, §4.1) is taken from the disease
   model's own P8.3 and is model/mechanism evidence, not drug-indication status — the Rule 3
   "PPARα-knockout mice" category.
4. **DMF's PML and lymphopenia profile, and MMF's GAPDH Cys152 succination** (§5.2) are non-DR
   pharmacology and biochemistry — allowed under Rule 3.
5. **Aldose-reductase and PKCβ clinical disappointment** (§5.1, §5.3) are cited as *mechanism-level*
   failure priors, which §4.4 of the model supplies to all agents in exactly that form.
6. **Negative-decision disclosure.** I hold training knowledge of DR-adjacent clinical facts for
   several candidates in this set. I excluded that knowledge from every score and every argument,
   including where it would have *raised* a score. The clearest instance: my relative ordering of
   the fibrate series rests entirely on network position, exposure compartment and the Round 1
   structural finding — not on any outcome knowledge. I note the residual the synthesis already
   records: dataset blinding removes the project's data signal, not pretrained knowledge, and
   Group D's mechanism categories are themselves canonical DR development axes, so that subset is
   not independently blind.
7. **Data-basis honesty.** Per §9, the efflux arm has no representation in the project data. I have
   marked every efflux conclusion `knowledge-based` rather than `mixed`, and the only `mixed`
   ratings below are those where `evidence/` supplied physicochemical or interaction rows I
   actually used.

---

## SCOREBLOCK

SCORE|Fenofibric acid|7.0|moderate|mixed|Supply node certain plus convergence-node transrepression; outside Brownlee quadrant
SCORE|Fenofibrate|6.5|moderate|mixed|Identical network position to A1; adds nothing, depends on ester conversion
SCORE|Pemafibrate|7.0|moderate|mixed|Same two territories; only ligand potent enough to occupy convergence node retinally
SCORE|Elafibranor|5.0|moderate|mixed|Dual PPARa/d broadens coverage but delta limb is pro-angiogenic, wrong-signed S3-S4
SCORE|Seladelpar|3.0|moderate|knowledge-based|PPARd dominant retinal isoform, pro-angiogenic; plausibly net wrong-signed in target compartment
SCORE|Linoleic acid|1.5|moderate|mixed|Net adverse position: supplies arachidonate for P8.6 eicosanoids and P8.7 4-HNE
SCORE|Alpha-linolenic acid|2.5|moderate|mixed|Right direction into resolution arm; ALA-to-EPA conversion under 10%, magnitude negligible
SCORE|Linalool|2.5|low|mixed|One genetic-dependency datum at SLC27A4, P8.8 periphery; access without network position
SCORE|Icosapent ethyl|6.0|moderate|knowledge-based|Sole occupant of P8.6 resolution territory; model names resolution failure under-exploited
SCORE|Quercetin|1.5|high|mixed|Counts are study-depth artifact; direction-incoherent at PPARA; efflux substrate, unreachable
SCORE|Melatonin|4.0|moderate|mixed|Real access and MT1/MT2 glial actions, but no network node of consequence
SCORE|Epalrestat|2.0|high|knowledge-based|Single branch downstream of divergence node; plus AKR1B1 is a 4-HNE reductase
SCORE|Dimethyl fumarate|7.0|moderate|knowledge-based|Broadest genuine coverage, disposal arm near node; GAPDH succination wrong-sign risk
SCORE|Minocycline|4.0|low|knowledge-based|Microglial amplifier not node; indirect touch on foam-cell cycle; mechanism undefined
SCORE|Candesartan cilexetil|6.5|moderate|knowledge-based|Upstream-lateral ROS source plus convergence node, from engagement-certain luminal compartment
SCORE|Ezetimibe|4.0|high|knowledge-based|Single certain node in the already best-covered module; high value as discriminating control
