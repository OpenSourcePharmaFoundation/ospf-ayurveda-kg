# P1 — Molecular Target Analyst
## Target profile: PPARA for diabetic retinopathy, and comparative target validation across the 15-candidate set

**Agent:** Molecular Target Analyst (`target-profiler`, re-anchored from Oral Mucositis to DR)
**Run:** blinded benchmark, 2026-10-05
**Scope:** target-level analysis. Scores below are **target-axis expected value**, not full
candidate scores — ADMET, formulation, trial design and cost belong to other agents.

---

## 0. Headline findings

Five claims, in order of how much they should move the pipeline:

1. **PPARα is the only target in the entire candidate set whose mechanism has a
   high-confidence-engagement compartment that is *not* the diseased compartment.** The liver
   concentrates fibrate anions via OATP1B1/1B3 to intracellular levels far above plasma, so hepatic
   PPARα engagement is not in doubt. Hepatic engagement produces *humoral* outputs — reduced
   TG-rich remnant particles and apoB number, raised ApoA1/HDL, and raised **FGF21** — that reach
   the retina without any drug crossing the blood–retinal barrier. This architecture makes the
   hypothesis survivable even if the scout's retinal-exposure objection is entirely correct. It
   should be the headline reading of the target, and it reframes pemafibrate's hepatoselectivity
   from a bug into a feature.

2. **The ANGPTL4 objection and the retinal-exposure objection are logically mutually destructive.**
   ANGPTL4 induction is PPRE-driven *transactivation*. If retinal free drug sits ~2 log₁₀ below the
   PPARα EC₅₀ — the scout's central claim — then retinal transactivation does not occur, and
   therefore neither does retinal ANGPTL4 induction. One cannot simultaneously hold that retinal
   PPARα transactivation is too weak to help and strong enough to harm. **Verdict: ANGPTL4 is a
   stage-restricted, monitorable safety flag, not a fatal wrong-sign limb.** Full argument in §3.

3. **Transrepression plausibly operates at 1–2 log₁₀ lower fractional occupancy than
   transactivation** — the principle the entire dissociated-ligand / SEGRM / SPPARM field is built
   on. That is exactly the size of the gap the scout identified. It materially weakens the exposure
   objection **for the inflammatory limb specifically**, and for nothing else. The consequence is
   elegant and testable: *at low retinal occupancy the retina sees a pharmacokinetically dissociated
   PPARα ligand — anti-inflammatory transrepression without metabolic transactivation and without
   ANGPTL4 induction.* §4.

4. **Seladelpar is a confounded falsification control, not a clean one**, and should not be relied
   on to falsify the PPARα hypothesis. PPARδ is the most abundantly expressed PPAR in retina, is
   pro-angiogenic, is at least as strong an ANGPTL4 inducer as PPARα, and shares the identical
   transrepression machinery. Both a positive and a negative seladelpar result are ambiguous. The
   decisive control is a **matched-lipid-lowering non-PPAR comparator**, which tests a different and
   more important null hypothesis. §5.

5. **The project data cannot address the question I was principally asked.** The 27-gene DR panel in
   `compound-dr-target-matrix.tsv` contains PPARA, PPARD and PPARG but **contains no ANGPTL4, CPT1A,
   ACOX1, HMGCS2, FABP4, LPL, APOA1, ABCA1 or FGF21** — i.e. not one PPARα lipid target gene. Ten of
   the fifteen candidates appear nowhere in the matrix, and seladelpar is absent from the PPAR
   properties file entirely. Every directional claim in §2 and §3 is knowledge-based. §8.

---

## 1. TARGET PROFILE — PPARA

```
═══════════════════════════════════════════════════════════
TARGET PROFILE: PPARA — Peroxisome proliferator-activated receptor alpha
═══════════════════════════════════════════════════════════

IDENTIFIERS
  Gene: PPARA | UniProt: Q07869 | Locus: 22q13.31
  Family: Nuclear hormone receptor, NR1C1. Obligate heterodimer with RXR (NR2B1),
          binds DR-1 PPREs. Modular: DBD (two zinc fingers) + hinge + LBD with
          AF-2 helix 12.
  Endogenous ligands: long-chain unsaturated fatty acids, fatty-acyl-CoAs,
          oxidised phospholipids, leukotriene B4, 16:0/18:1-GPC.

DRUGGABILITY: HIGH / KD — highest-confidence call in this report.
  - Large (~1,300 Å³) Y-shaped hydrophobic LBD pocket, extensively co-crystallised.
  - Accepts carboxylic-acid-bearing lipophilic ligands; acidic head group anchors
    to the S280/Y314/H440/Y464 polar cluster that stabilises helix 12.
  - Multiple validated chemotypes (fibric acids, SPPARMα, dual/pan agonists);
    selective-modulator design is a mature discipline; a validated antagonist
    (GW 6471) exists for mechanistic controls.
  - Natural-product chemical space is intrinsically privileged — the physiological
    ligands ARE dietary fatty acids. This is why the project's natural-product file
    produces genuine binders (§8).
  Caveat that is a druggability issue, not a target issue: the pocket's preference
  for lipophilic ACIDS is in direct tension with blood–retinal-barrier penetration
  (permanent anion at pH 7.4, high albumin binding, efflux-direction OATs at the
  inner BRB and RPE). The pocket that makes PPARα easy to drug makes it hard to
  drug *in the retina*.

VALIDATION LEVEL (re-anchored to DR)
  Level 1 (clinical):     NOT ESTABLISHED in this analysis — and not assessable
                          under the blinding protocol.
  Level 2 (genetic):      MODERATE. Global Ppara-/- → worse experimental
                          retinopathy; retina-targeted PPARα expression protective.
                          Confounded — see §1.3.
  Level 3 (pharmacol.):   MODERATE-STRONG preclinical breadth, UNCERTAIN effect size.
  Level 4 (expression):   CONTESTED. The weakest link. See §1.1.
  Level 5 (pathway):      STRONG. Hits P8 (lipid), P6 (NF-κB/leukostasis),
                          P5 (CAT/AMPK/SIRT1), plausibly P9.
  Level 6 (computational):WEAK-NEGATIVE in this project. 143 rows, zero drug edges.

  Composite honest grade: **Level 2–3, moderate.** Not Level 1. Not weak.

DIRECTION NEEDED: ACTIVATION (agonism).
COMPARTMENT PRIORITY: liver/plasma (high confidence) > retinal vascular endothelium
                      (marginal) > Müller/RPE (lowest confidence).
STAGE FIT: S0–S3. Mechanistically weakest at S4–S5, where the ANGPTL4 flag also bites.
═══════════════════════════════════════════════════════════
```

### 1.1 Retinal expression — weighing the scRNA-seq / antibody conflict

The disease model flags this honestly (§5.2a) and I want to go further, because the conflict is
**resolvable and the two methods do not err symmetrically.**

**Why single-cell atlases under-report PPARA.**
- Nuclear receptors are, as a class, low-abundance transcripts outside their dominant tissue. PPARA
  in liver/heart/kidney cortex is high; elsewhere it typically runs an order of magnitude or more
  lower while remaining functionally competent.
- Droplet-based 3′ scRNA-seq has severe dropout for transcripts in the 1–5 TPM band. A gene at that
  level is detected in a minority of cells per cluster and never appears on a marker-gene or
  "prominent transcript" list. **Absence from a marker list is not absence of expression** — it is
  the expected behaviour of a moderately expressed transcription factor in a method tuned to
  high-abundance cell-identity genes.
- PPARA has a long 3′UTR and multiple isoforms, and regulatory-protein mRNAs are enriched in the
  nuclear fraction — all of which further depress capture in single-cell and especially single-nucleus
  protocols relative to cytoplasmic transcripts.

**Why antibody studies over-report it.**
- The nuclear receptor DBD and LBD folds are highly conserved across NR1C1/C2/C3 and more broadly.
  Commercial anti-PPARα antibodies have a documented history of detecting bands in PPARA-null
  tissue. Any immunolocalisation not validated on a KO or knockdown control should be heavily
  discounted. A substantial fraction of the "PPARα is present in ganglion cells / photoreceptor
  inner segments" literature rests on exactly such unvalidated reagents.

**Weighted conclusion.** The truth is almost certainly between the two, and closer to the
transcriptomic end than the IHC end. The defensible statement is:

> PPARA is **detectably but modestly expressed** in RPE, Müller glia, retinal vascular endothelium
> and microglia, and is **not a prominent retinal transcript**. Claims of abundant neuronal PPARα
> should be treated as unsupported. `[EMERGING / partly UNCERTAIN]`

**The analytically important consequence — and it is routinely conflated.** Low receptor abundance
and low ligand exposure are *different objections with different consequences*:

| | Governed by | Consequence |
|---|---|---|
| **Fractional occupancy** | [L]free / ([L]free + K_d) — **independent of receptor number** | Determines *whether* signalling starts |
| **Signal amplitude** | receptor number × occupancy × coactivator supply × PPRE accessibility | Determines *how big* the output is |

So low retinal abundance does **not** make occupancy harder — it caps the *amplitude* of whatever
occupancy achieves. The exposure objection is an occupancy argument; the expression objection is an
amplitude argument. They compound multiplicatively (a small fraction of a small number), which is
why the retinal limb is weak — but agents should stop treating them as one argument, because they
have different remedies: occupancy is fixable with potency (pemafibrate), amplitude is not.

### 1.2 "Restore a deficiency" vs supraphysiological stimulation — the framing is weaker than it reads

The model and brief both lean on the observation that retinal PPARα is *decreased* in diabetes, so
an agonist restores rather than over-drives. This framing is rhetorically attractive and
**partially a category error.** An agonist raises the *fractional occupancy of the receptor that
remains*; it does not raise receptor *number*. Three cases:

1. **If the deficiency is at the receptor-protein level** (less PPARα protein in diabetic retina),
   an agonist's ceiling is **lowered, not restored**. Fewer receptors means less transactivation
   capacity *and* less transrepression capacity — a double hit on exactly the two limbs being
   scored. On this reading the decreased-expression finding is **evidence against** the retinal
   limb, not for it. The only escape is PPARα autoinduction, which is modest and tissue-dependent.

2. **If the deficiency is functional — reduced endogenous ligand supply, increased corepressor
   occupancy, inhibitory phosphorylation/SUMOylation, or NCoR retention** — then exogenous ligand is
   exactly the right intervention, and "restoration" is mechanistically coherent. This version is
   defensible and is the one proponents should argue. It also predicts that a *ligand*
   (fatty-acid-class, Group B) and a *drug* should act similarly, which is a testable discriminator.

3. **Dose.** "Restorative vs supraphysiological" is a dose question, not a target property. Fibrates
   at clinical doses produce hepatic occupancy far above any physiological set point. In retina,
   by the scout's arithmetic, they produce ~0.3% occupancy — which is not restoration either.

**You cannot hold both "we only need a gentle restorative nudge" and "we are two logs below EC₅₀."**
The restore-deficiency framing and the exposure objection are in tension, and the honest position is
that the restore framing is only load-bearing under case (2). I recommend downstream agents stop
citing decreased retinal PPARA as support unless they also specify that the deficiency is functional
rather than at the protein level.

### 1.3 Conditional genetic evidence — how strong, and what confounds it

| Experiment | What it shows | Strength | Confounds |
|---|---|---|---|
| Global `Ppara-/-` + diabetes → worse retinopathy | Ppara is protective *somewhere* | **Weak for retina-intrinsic** | Global KO has hypertriglyceridemia, impaired fasting ketogenesis, hepatic steatosis, altered FA handling and altered systemic inflammatory tone. It also alters glucose/insulin handling and the response to STZ itself. Worse retinopathy is fully explicable by systemic metabolic derangement — i.e. by the *indirect* mechanism. This design **cannot** separate retina-intrinsic from systemic. |
| Retina-targeted PPARα expression (AAV / tissue-restricted) → protective | PPARα is **sufficient** in retina | **Moderate** | (i) Overexpression paradigms routinely reach supraphysiological levels, and supraphysiological gain-of-function can rescue phenotypes the endogenous gene does not govern. (ii) Rescue on a WT background is gain-of-function, not conditional rescue; only rescue on the KO background is informative about necessity. (iii) AAV delivery is itself not inert in retina. |
| **Retina-cell-type-specific conditional deletion** (floxed *Ppara* × Müller / endothelial / RPE Cre) | PPARα is **necessary** in a defined retinal cell type | **Would be decisive** | **This experiment is the missing one.** |

**Grade: moderate, not strong.** Sufficiency in an overexpression paradigm is demonstrated;
necessity *within the retina* is not, and the global knockout cannot establish it. The brief's
counter-consideration ("knockout worse, retina-targeted expression protective supports a
retina-intrinsic component") is directionally right but overstated — it supports *a retinal
capability*, not a retinal requirement, and the knockout arm contributes almost nothing once its
systemic lipid phenotype is accounted for. The single highest-value preclinical experiment this
whole programme could commission is a cell-type-restricted conditional *Ppara* deletion.

---

## 2. PPARα's direct transcriptional programme mapped onto DR pathway modules

Direction convention: all rows assume **induction** by an agonist. "Sign" is the expected effect on
DR pathobiology. Compartment matters enormously and is stated separately.

| Gene | Module | What induction does | Sign in diabetic retina |
|---|---|---|---|
| **CPT1A** | P8.8 | Mitochondrial long-chain FA import → β-oxidation | **Mixed.** Genuinely helpful in **RPE**, which physiologically oxidises phagocytosed outer-segment lipid and whose lipid-droplet/ceramide load drives ER stress. **Uncertain-to-harmful in inner retina and endothelium**: photoreceptors run near-Warburg aerobic glycolysis, and endothelial FAO serves dNTP synthesis rather than ATP, so forcing FAO there is not obviously beneficial and raises electron flux into an already ROS-stressed chain. |
| **ACOX1** | P8.8 | Peroxisomal β-oxidation of VLCFA, first and rate-limiting step | **Conditionally harmful.** ACOX1 generates **H₂O₂ stoichiometrically** with each desaturation cycle. Inducing it in a tissue under sustained oxidative load is a direct ROS-generating intervention. It is tolerable *only because PPARα co-induces catalase in the same peroxisome*. If CAT induction is blunted — and NRF2 is functionally deficient in diabetic retina (model row 22) — ACOX1 induction is net pro-oxidant. **This is an under-discussed wrong-sign risk and it is coupled to the CAT row below.** |
| **HMGCS2** | P8.8 | RPE ketogenesis; β-hydroxybutyrate exported to photoreceptors | **Clearly helpful — the cleanest right-sign limb in the programme.** Restores RPE metabolic support of the outer retina. BHB is additionally an HDAC inhibitor, an NLRP3 inflammasome inhibitor and an HCAR2 ligand — three independent anti-inflammatory actions on top of the fuel role. |
| **FABP1** | P8.8 | Liver FABP; hepatic FA trafficking | Neutral for retina; supports the hepatic limb. |
| **FABP4** | P8.8 | Adipocyte/macrophage FABP | **Potential wrong sign.** FABP4 is raised in DR serum and vitreous and is pro-angiogenic and pro-inflammatory (model row 46). PPARγ is the dominant inducer, but PPARα contributes in some contexts. Partly offset because systemic PPARα agonism tends to *lower* circulating FABP4 via improved insulin sensitivity and adipose lipolysis. **Direction genuinely uncertain — a second, smaller ANGPTL4-shaped concern.** |
| **FABP5** | P8.8 | Lipid chaperone; shuttles ligands preferentially to **PPARδ** | Neutral-to-unhelpful. Note the pharmacological consequence: FABP5 induction biases downstream ligand delivery toward the δ isoform, i.e. toward the arm §5 identifies as pro-angiogenic. |
| **LPL** | P8.1/P8.2 | Lipoprotein lipase; TG hydrolysis at endothelium | **Systemically helpful, locally ambiguous.** Systemically it is a principal mechanism of TG lowering → fewer remnant particles available to extravasate. *Locally in retina*, LPL induction would hydrolyse extravasated TG-rich lipoprotein at the vessel wall, liberating free fatty acids and lysophospholipids — locally lipotoxic species. The classic vessel-wall-LPL paradox applies here, and hard exudate is precisely extravasated lipid. |
| **APOA1 / APOA2 / APOA5** | P8.2/P8.3 | ApoA1 ↑ (HDL acceptor), ApoA5 ↑ (TG lowering) | **Helpful.** Model row 47 notes ApoA1 mimetics are protective in retinal models. Raises the acceptor arm of retinal cholesterol efflux. |
| **ABCA1** | P8.3 | Cholesterol efflux from Müller, RPE, pericytes | **Helpful.** ABCA1 is specifically *downregulated* in diabetic retina (model row 48), so this is a genuine restoration — and unlike PPARA itself, the deficiency here is in the effector, which an agonist can actually raise. |
| **FGF21** | P8/endocrine | Hepatokine; metabolic and anti-inflammatory | **Helpful, and strategically the most important row in this table.** FGF21 is *secreted from liver into plasma* and acts on target tissue via FGFR1c/β-Klotho. Retinal vascular endothelium is reachable from the luminal side. FGF21 has independent reports of retinal protection and reduced pathological neovascularization. **This is a humoral relay from the compartment where engagement is certain to the compartment where it is not — it bypasses the blood–retinal-barrier objection entirely.** It deserves far more weight than §5.2 of the disease model gives it. |
| **CAT** | P5 | Peroxisomal catalase | **Helpful — and obligatory.** It is the designated counterweight to ACOX1. The PPARα programme is internally coherent *only if the ACOX1:CAT induction ratio stays favourable*. Worth measuring directly in any model study. |
| **ANGPTL4** | P7/P8 | LPL inhibitor systemically; cANGPTL4 is a pro-permeability, pro-angiogenic retinal factor | **The crux — see §3.** |

**Net read of the programme.** The lipid-handling limb is *not* uniformly right-signed. HMGCS2,
APOA1/A5, ABCA1, FGF21 and CAT are clean positives. CPT1A is compartment-split. ACOX1 and local LPL
are conditionally negative. FABP4/FABP5 lean mildly wrong. ANGPTL4 is the acute question. A fair
summary is that **the programme's systemic/hepatic output is robustly right-signed, while its
retina-local output is a mixed bag that depends on compartment and on the ACOX1:CAT ratio.** That
asymmetry is, again, the same conclusion as §0.1: the systemic limb is the defensible one.

---

## 3. ANGPTL4 — the crux. Verdict and justification

### 3.1 The case for calling it fatal

- ANGPTL4 is a textbook direct PPAR target with well-mapped PPREs, induced by α, δ and γ ligands.
  Fibrate dosing demonstrably raises ANGPTL4 in liver, adipose and plasma in humans and rodents.
  **PPARα agonism therefore predicts ANGPTL4 induction. That premise is solid and not disputable.**
- The C-terminal fibrinogen-like fragment (cANGPTL4) is a potent vascular-permeability and
  angiogenic effector in retina, acting on endothelial junctions partly through integrin and
  neuropilin engagement, **partly independently of VEGF** — which makes it a mechanism anti-VEGF
  therapy would not mask.
- It is hypoxia-inducible through HIF-1α, is produced by Müller glia, and is elevated in the
  intraocular fluid of ischemic retinal disease.
- So in principle the drug's own mechanism predicts induction of a factor that drives exactly the
  endpoints (permeability, neovascularization) one is trying to prevent. This is a legitimate
  wrong-sign concern and the scout was right to weight it.

### 3.2 Four arguments that defuse it

**(i) The decisive one: ANGPTL4 induction and the exposure objection cannot both be true in retina.**

ANGPTL4 induction is **PPRE-dependent transactivation** — the full chain of ligand binding →
corepressor release → coactivator and Mediator recruitment → RXR heterodimer on a DR-1 element →
sustained transcription. That chain is the *most* occupancy-demanding thing PPARα does (§4).

The scout's central objection is that free retinal drug sits ~2 log₁₀ below the PPARα EC₅₀, giving
fractional occupancy on the order of 0.3%. If that is right, **retinal transactivation does not
happen — and retinal ANGPTL4 induction is a transactivation event.** The two objections are
mutually destructive:

> If retinal PPARα transactivation is too weak to induce CPT1A/ACOX1 and deliver benefit, it is too
> weak to induce ANGPTL4 and deliver harm. If it is strong enough to induce ANGPTL4, the exposure
> objection has collapsed and the metabolic benefit limb is live. **Whichever you believe, one of
> the two arguments must be abandoned.**

I do not think this has been noticed in the upstream documents, and it is the single most important
analytical point in this report. The scout lists ANGPTL4 in §7 as a factor that "sharpens" the
exposure objection; in fact it is **in tension with it**, not additive to it.

**(ii) Competitive occlusion by the dominant HIF input, at exactly the stage where ANGPTL4 matters.**
The ANGPTL4 locus carries both HREs and PPREs. In ischemic retina the HIF-1α input is enormous and
is the dominant driver of the many-fold Müller-cell induction. A marginal PPRE increment layered on
a promoter already driven hard by hypoxia is a small fractional addition and may be substantially
occluded by coactivator competition at a near-saturated locus. Conversely, at S0–S2 — where the PPRE
contribution would be relatively more visible — there is no significant retinal hypoxia, baseline
ANGPTL4 is low, and the absolute quantity produced is small. **The stage where PPARα could move
ANGPTL4 most is the stage where ANGPTL4 matters least, and vice versa.**

**(iii) The systemic paradox is already resolved empirically in the lipid axis.** PPARα agonism
simultaneously induces LPL (pro-TG-clearance) and ANGPTL4 (an LPL inhibitor), which is a genuine
internal contradiction in fibrate pharmacology. The *observed* net systemic effect is TG lowering —
i.e. the LPL induction plus APOC3 repression plus APOA5 induction dominate over ANGPTL4's
counter-effect. This is a worked precedent that PPARα-driven ANGPTL4 induction, while real, is not
large enough to invert the net direction of the programme in the compartment where engagement is
certain. It does not prove the retinal case, but it is the closest available analogue and it goes
the right way.

**(iv) The alternative route — plasma ANGPTL4 reaching a leaky retina — is real but second-order.**
This is the one limb that does not require retinal receptor occupancy, and it deserves to be named
because it survives argument (i): hepatic/adipose induction raises circulating ANGPTL4, and a
compromised blood–retinal barrier admits plasma proteins. The scout's bootstrapping problem works
against the drug here. But the magnitude comparison is unfavourable to the concern: in ischemic
retina, local paracrine Müller-cell production under full hypoxic drive dwarfs what a modest
fractional rise in a plasma pool contributes across a partially compromised barrier. This keeps the
concern from being dismissed outright; it does not make it decisive.

### 3.3 Verdict

> **ANGPTL4 is OVERSTATED as a falsifier and REAL as a stage-restricted safety flag.**
>
> It is **not** a fatal wrong-sign limb. It is **not** merely "overstated because systemic agonism
> may not raise retinal ANGPTL4" either — that framing is too weak, because it treats the point as
> an empirical maybe. The stronger claim is structural: **the induction mechanism is the same
> transactivation machinery the exposure objection says is unavailable, so the two objections cannot
> both stand.**
>
> Practically: **tolerable at S0–S2** (negligible drive, intact barrier, low absolute production,
> and the stage this mechanism targets anyway); **a genuine liability at S4–S5** (leaky barrier
> admits plasma ANGPTL4, dominant local drive, and no compensating benefit since §5.3 of the scout
> establishes PPARα cannot touch established neovascularization). It should **reduce a PPARα
> candidate's score at S4–S5 by roughly 2 points and leave S0–S2 scoring essentially unchanged.**
>
> **Confidence: moderate.** The structural argument is strong; the quantitative premises (fractional
> occupancy, relative HIF vs PPRE contribution at the ANGPTL4 locus in retina) are reasoned, not
> measured.

### 3.4 How to falsify this verdict — cheap and decisive

1. **Measure aqueous/vitreous ANGPTL4** in fibrate-treated vs untreated diabetic patients undergoing
   cataract surgery or vitrectomy, stratified by DR stage. Direct, feasible, and settles the
   systemic-delivery limb.
2. **Measure retinal CPT1A/ACOX1/ANGPTL4 transcript induction** after chronic oral fibrate in a
   diabetic rodent. If retinal transactivation targets go up robustly, the low-occupancy model is
   wrong, the ANGPTL4 risk is live, and §4's "pharmacokinetically dissociated ligand" synthesis
   collapses. **If they do not go up but retinal ICAM1/TNF/leukostasis go down, the synthesis in §4
   is confirmed.** This single experiment discriminates between the two competing readings of the
   whole hypothesis and should be the programme's top preclinical priority.
3. **Mandatory safety readout in any S0–S2 trial:** no excess progression to proliferative disease,
   no excess centre-involving macular edema, in the treated arm. Prespecify it.

---

## 4. Transrepression vs transactivation — does the inflammatory limb need less occupancy?

This is, as the brief suspects, genuinely important and under-appreciated. **Short answer: yes,
plausibly by 1–2 log₁₀, and that is exactly the size of the gap in question.**

### 4.1 The two mechanisms are not symmetric

| | **Transactivation** (CPT1A, ACOX1, ANGPTL4, IκBα) | **Transrepression** (RELA/p65, AP-1 targets: ICAM1, TNF, IL6, CCL2, NOS2, PTGS2, MMP9) |
|---|---|---|
| Requires PPRE | Yes (DR-1, RXR heterodimer) | **No** |
| Mechanism | Ligand → helix-12 repositioning → corepressor release → coactivator/Mediator recruitment → chromatin remodelling → Pol II → sustained output | Ligand-bound receptor physically tethers to p65/c-Jun and/or (SUMO-dependently) docks onto NCoR/SMRT complexes at inflammatory promoters, **preventing signal-dependent corepressor clearance** |
| Receptor fate | Participates in each transcriptional burst; occupancy needed at the moment of firing | Not consumed; a tethered receptor holds the complex. Can act **sub-stoichiometrically / cyclically across loci** |
| Output character | **Graded and threshold-limited** — mRNA → protein → metabolic flux is a multiplicative chain that must exceed a flux threshold to matter | **Blocking a derepression step — more digital.** Preventing a switch from flipping is cheaper than driving a rheostat |
| Needs RXR, coactivator supply, open PPRE chromatin | Yes, all three | No |

Four independent reasons transrepression should win at lower occupancy:

1. **Stoichiometry.** Transactivation output scales with the number of liganded receptor–PPRE
   complexes each productively assembling a full coactivator/Mediator machine. Transrepression is a
   *blocking* function at a promoter that is being actively derepressed; one tethered receptor can
   hold one locus.
2. **Catalytic character.** In the SUMOylation-dependent model the receptor stabilises the NCoR
   complex without being consumed, so a small liganded pool cycling between promoters can suppress
   multiple loci. Transactivation has no equivalent amplification.
3. **The precedent is superfamily-wide and is the entire basis of a drug-design field.** Dissociated
   glucocorticoids (SEGRMs — compound A, RU-24858 and successors) were designed on the explicit,
   reproducible observation that GR transrepression occurs at **~10–100× lower ligand concentration**
   than GR transactivation. The same dissociation is documented for LXR and PPARγ. For PPARα
   specifically, dose–response separation between suppression of NF-κB targets and induction of PPRE
   targets has been reported. **PPARα-specific quantification is thinner than GR's, but the
   mechanism is shared and the principle is established, not speculative.**
4. **Downstream nonlinearity in the specific DR endpoint.** The output that matters here is ICAM1
   surface density on retinal endothelium → firm leukocyte adhesion under shear → capillary plugging
   → endothelial apoptosis and dropout. Firm adhesion under shear requires a *density threshold* of
   ligand, so a 20–30% reduction in ICAM1 can produce a disproportionately larger reduction in
   leukostasis. **The inflammatory limb's phenotypic output amplifies a modest molecular effect; the
   metabolic limb's does not** (a 20% rise in CPT1A changes FAO flux by roughly 20%).

### 4.2 The honest caveats

- Transrepression still requires ligand **binding** — the same K_d governs the first step. At 0.1–0.4 µM
  free drug against a tens-of-µM EC₅₀, occupancy is ~0.3%. A 100× threshold advantage brings the
  *effective* position to roughly parity with EC₅₀-equivalent signalling for this limb — marginal,
  not comfortable. It converts "impossible" into "not excludable," which is a real but bounded win.
- The low receptor abundance in retina (§1.1) caps amplitude independently and is not rescued by the
  threshold advantage.
- Much of the GR dissociation data came from reporter systems and in vivo dissociation has proved
  harder to demonstrate than in vitro. Discount accordingly.
- **Part of PPARα's anti-inflammatory effect is itself transactivation** — IκBα induction is
  PPRE-dependent and gets **no** low-occupancy benefit. So the inflammatory limb is itself split, and
  only the direct tethering component is rescued.

### 4.3 The synthesis — and it is testable

Putting §3 and §4 together yields a specific, falsifiable prediction that I believe is the most
useful output of this analysis:

> **At the low fractional occupancy achievable in retina, oral PPARα agonism behaves as a
> *pharmacokinetically dissociated* ligand: it delivers NF-κB/AP-1 transrepression without metabolic
> transactivation — and therefore without ANGPTL4 induction.** The retina gets a selective
> anti-inflammatory profile not by ligand design but by exposure arithmetic.

This reframes the scoring axes the brief asked for:

| Axis | Status after this analysis |
|---|---|
| **Systemic lipid-lowering plausibility** (hepatic, OATP-concentrated) | **High confidence.** Engagement certain; direction net-positive; adds the FGF21 endocrine relay. |
| **Anti-inflammatory transrepression** (retinal endothelium) | **Marginal but NOT excludable** — upgraded from the scout's near-dismissal by the threshold argument and the ICAM1 nonlinearity. |
| **Retinal PPARα transactivation / metabolic limb** | **Low confidence — probably does not occur.** And this is *good news*: it is the same limb that would induce ANGPTL4. |

Prediction to test: oral fibrate in a diabetic animal should reduce retinal leukostasis, ICAM1 and
TNF **without** robustly inducing retinal CPT1A/ACOX1/ANGPTL4. Observing strong retinal FAO-gene
induction would falsify this synthesis and re-open the ANGPTL4 risk.

---

## 5. Isoform separation — PPARA vs PPARG vs PPARD in retina

| | **PPARA (NR1C1)** | **PPARD (NR1C2)** | **PPARG (NR1C3)** |
|---|---|---|---|
| Dominant tissue | Liver, heart, kidney cortex, BAT | **Ubiquitous — broadest of the three** | Adipose, macrophage |
| Relative retinal expression | Low–moderate; contested (§1.1) | **Reported the most abundant PPAR in retina** | Moderate; RPE, Müller, microglia, endothelium. Several datasets put it **above** PPARα |
| Core function | FAO, ketogenesis, lipoprotein handling, transrepression | FAO, endothelial function, wound healing, lipid oxidation, transrepression | Adipogenesis, insulin sensitisation, strongest transrepressor of the three |
| **Angiogenesis** | Neutral-to-anti (reduces VEGF-induced permeability and tube formation in retinal EC) | **PRO-angiogenic.** Induces VEGFA, promotes EC proliferation and tube formation; required for VEGF-driven angiogenesis in several models; implicated in driving pathological retinal neovascularization | Mildly pro-permeability (raises VEGF in adipose; capillary permeability) |
| **ANGPTL4 induction** | Yes | **Yes — at least as strongly; δ is arguably the dominant ANGPTL4 driver in muscle and endothelium** | Yes |
| Agonism liability in DR | ANGPTL4 (stage-flagged); hepatic enzymes; creatinine; myopathy with statins | **Pro-angiogenic + strongest ANGPTL4 drive — a directionally adverse profile for ischemic retina** | **Fluid retention via ENaC/SGK1 distal-nephron Na⁺ reabsorption → peripheral edema; class association with worsening macular edema** (brief §4, model §4.4) |

**On PPARγ, the isoform discipline the brief demands cuts both ways.** It is *not* correct to say
"PPARγ is bad for the retina." PPARγ's retinal cell-autonomous biology is good — it is the strongest
NF-κB transrepressor of the three and is anti-inflammatory in RPE, Müller and microglia. The
disqualifying problem is **systemic and renal**: ENaC-mediated fluid retention produces edema, and
in a disease whose principal vision-threatening complication is macular *edema*, a systemic
fluid-retaining mechanism is disqualifying regardless of the local pharmacology. The correct
statement is "PPARγ agonism's systemic fluid effect outweighs its retinal anti-inflammatory effect,"
and that precision matters because it means the γ liability does **not** transfer to α on
mechanistic grounds — fibrates do not share the ENaC/SGK1 effect.

### 5.1 Is seladelpar a clean falsification control? **No — it is confounded.**

Five reasons, in order of force:

1. **PPARδ is not a null arm in retina — it has its own, oppositely signed pharmacology.** If δ
   agonism is pro-angiogenic in retina, a seladelpar arm is not a neutral comparator; it is an arm
   with a plausible *harm* mechanism. "Seladelpar < pemafibrate" could then reflect δ-mediated harm
   rather than α-mediated benefit, and the inference "therefore PPARα is doing the work" does not
   follow.
2. **Shared transrepression machinery destroys the specificity of a positive result.** All three
   PPARs transrepress NF-κB through the same corepressor mechanism. If the operative limb is
   transrepression (§4), seladelpar would reproduce it and appear to "work" — without validating α
   at all. A positive seladelpar result is therefore ambiguous between "δ-specific" and "shared
   class transrepression."
3. **It carries the same wrong-sign limb, worse.** δ drives ANGPTL4 at least as hard as α. Seladelpar
   does not control for the ANGPTL4 concern; it amplifies it.
4. **Asymmetric inferential value.** A *negative* seladelpar result is weakly informative — it is
   equally explained by insufficient retinal exposure, the same objection facing every arm. A
   *positive* result is informative but, per (2), ambiguous. A control that is weak when negative and
   ambiguous when positive is not a good control.
5. **No project data.** Seladelpar (CHEMBL230158) is **absent from `ppar-class-drug-properties.tsv`**
   — the 13-row file contains troglitazone, gemfibrozil, clofibrate, pioglitazone (×2), rosiglitazone
   (×2), fenofibrate, fenofibric acid, pemafibrate, ciprofibrate, choline fenofibrate and elafibranor,
   and no seladelpar. The designated falsification control has no physicochemical backing in this
   project whatsoever.

**The control the programme actually needs.** The seladelpar arm tests the wrong null hypothesis. The
hypothesis genuinely at risk is not *"is it α or δ?"* — it is **"is it PPARα engagement at all, or is
it simply lipid lowering?"** (the scout's §7). The decisive control is therefore a
**non-PPAR lipid-lowering comparator titrated to matched triglyceride/remnant reduction.** If
matched lipid lowering by a non-PPAR mechanism reproduces the retinal effect, the PPARα-specific
hypothesis is dead regardless of isoform. If it does not, PPARα engagement is doing something beyond
lipid lowering. That is a clean, decidable test; the isoform arm is not.

**Consequence for elafibranor (A4):** as an α/δ dual it inherits δ's pro-angiogenic profile and a
doubled ANGPTL4 drive on top of its Michael-acceptor enone. At target level, δ co-agonism in this
indication is a **liability, not an additive benefit.** Score it accordingly.

---

## 6. Comparative target validation — the non-PPAR targets

### 6.1 AKR1B1 (epalrestat) — the weakest target in the set

- **Druggability: HIGH/KD.** Aldo-keto reductase with a deep, well-characterised anion-binding
  active site and a specificity pocket; many chemotypes made; approved agents exist in some markets.
  Druggability is not the problem.
- **Validation: Level 1 — and NEGATIVE.** The disease model (§4.4) records that multiple aldose
  reductase programmes showed no convincing effect on DR progression in humans despite strong animal
  data. Negative Level-1 evidence is the single most informative datum available about any target in
  this set, and it points the wrong way.
- **A built-in wrong-sign limb that is worse than ANGPTL4's.** AKR1B1 also **detoxifies 4-HNE and
  other reactive lipid aldehydes** (model row 10). Inhibiting it removes a detoxification function at
  the same catalytic site that carries the polyol flux. Unlike the ANGPTL4 flag — which is
  stage-dependent and, per §3, probably not engaged at achievable retinal occupancy — this one is
  **unavoidable and mechanistically obligate**: you cannot block the polyol reaction without
  blocking the aldehyde-detox reaction.
- **Unfavourable kinetics at hyperglycaemia.** Aldose reductase has a high K_m for glucose
  (tens of mM), so polyol flux is near first-order in glucose across the diabetic range. Partial
  inhibition at tolerated exposure leaves large residual flux at 12–20 mM glucose. The arithmetic is
  unforgiving in the same way the PPARα retinal arithmetic is — but with no compartment exemption.
- **Verdict: deprioritise.** Druggable, validated as *involved*, invalidated as *actionable*.

### 6.2 NFE2L2 / KEAP1 (dimethyl fumarate) — good target, liability-laden ligand

- **Druggability: NFE2L2 itself HARD (bZIP transcription factor); KEAP1 KD** via covalent cysteine
  ligands (C151 and others) with real clinical precedent, plus non-covalent KEAP1–NRF2 PPI inhibitors
  as an emerging class. Targeting the repressor rather than the TF is the right architecture.
- **Validation: Level 3 strong preclinical in DR models; Level 1 in other indications; no DR clinical.**
  NRF2 is described as **functionally deficient** in diabetic retina (model row 22) — and note that
  the restore-deficiency framing is **more defensible here than for PPARα**, because the deficiency
  is in a repressible system an activator can genuinely relieve, not in receptor protein number.
- **The brief's "antioxidant-only is null" prior does not straightforwardly apply.** Vitamin
  supplementation failed because stoichiometric scavengers cannot reach or sustain effective retinal
  concentrations. NRF2 is a *catalytic transcriptional programme* — NQO1, HMOX1, GCLC/GCLM, TXNRD1,
  G6PD, catalase, and importantly **GLO1** (methylglyoxal detox, the P2/AGE axis, model row 14) — and
  is independently anti-inflammatory via direct interference with RelA and suppression of pro-IL1B
  transcription. Inferring "NRF2 will fail because vitamin E failed" is invalid and the brief's prior
  should be applied with that distinction.
- **Ligand problems, however, are serious.** DMF is a promiscuous Michael acceptor: it acutely
  depletes glutathione, succinates many cysteine-containing proteins including GAPDH, and its
  mechanism is therefore not cleanly NRF2. And it causes **lymphopenia with PML risk** on chronic
  dosing — unacceptable-adjacent in a chronically infection-prone diabetic population requiring
  lifelong therapy.
- **Verdict: target 6/10, this ligand 5/10.** Worth pursuing via a cleaner KEAP1 ligand; DMF is a
  mechanistic probe, not the eventual drug.

### 6.3 Microglial targets (minocycline) — the biology is validated; the "target" is not defined

- **This is the key scoring point: "microglia" is a cell type, not a molecular target.** Minocycline's
  molecular target for microglial deactivation has never been established — proposed mediators
  include MMP inhibition via zinc chelation, 5-LOX, PARP1, caspase-1, mitochondrial calcium uniporter
  activity and p38 MAPK, with no consensus. **A candidate whose target is unspecified cannot be
  target-validated**, and should be scored on the phenotype axis only, with an explicit note that the
  target axis is unassessable.
- **The underlying biology is genuinely well validated.** Microglial activation in the neurovascular
  unit (P9/S0) is early, precedes vasculopathy, and is causally supported by depletion and CSF1R-
  inhibition studies. It addresses **unmet need #3 (neuroprotection independent of anatomy)**, which
  has *no* competing therapy at all — the largest white space in the set after P8.
- **The better handle is CSF1R** — KD, approved small-molecule inhibitors exist, well-defined
  pharmacology, measurable target engagement. If the pipeline wants to test the microglial
  hypothesis, CSF1R is the target; minocycline is a blunt instrument standing in for it.
- **Ocular safety is a specific problem, not a generic one.** Chronic minocycline causes cutaneous,
  scleral and conjunctival **pigmentation** and **benign intracranial hypertension with papilledema**
  — an ocular adverse mechanism in an ocular indication requiring lifelong dosing. Plus vestibular
  toxicity. (General pharmacology, not DR-specific.)
- **Verdict: biology 5.5/10, this ligand 3.5/10.**

### 6.4 AGTR1 (candesartan) — the best-druggable target in the comparator set

- **Druggability: HIGHEST in this entire report.** Class A GPCR, the single best-validated druggable
  family in medicine; a dozen ARBs with excellent oral PK; candesartan specifically is a potent,
  slowly-dissociating (insurmountable) antagonist with sustained receptor occupancy.
- **Validation: moderate-strong.** The retina has a complete local renin–angiotensin system
  independent of plasma RAS (model row 66); AT1R on Müller cells, endothelium, pericytes and ganglion
  cells drives NOX activation, VEGF induction, inflammation and neuronal loss; the counter-regulatory
  ACE2 → Ang-(1-7) → MAS1 arm is suppressed in diabetic retina. Genetic support modest; preclinical
  strong; human tissue expression established.
- **A genuine exposure advantage that parallels the FGF21 point.** AT1R is expressed on the **luminal**
  endothelial surface, so a blood-borne antagonist engages a meaningful fraction of the relevant
  receptor pool **without crossing the BRB.** Among all targets here, only AGTR1 and the humoral
  PPARα outputs have this property. It deserves explicit credit.
- **Ancillary benefit that matters in this exact population:** renoprotection, in a cohort where
  renal impairment is the norm (brief §5).
- **Real debits.** (i) **Deployment problem** — much of the diabetic population with retinopathy is
  already on RAS blockade for hypertension or nephropathy, so the marginal untreated population is
  narrow and any trial is really testing *dose intensification*, not initiation. (ii) **BP confound**
  — benefit cannot be cleanly attributed to retinal AT1R vs systemic blood-pressure reduction.
  (iii) Hyperkalemia and acute eGFR decline in CKD limit dose. (iv) Hypotension caps exposure.
- **Verdict: 6/10 target. Highest druggability, moderate validation, serious deployment constraint.**

### 6.5 The single-node precedent — does PPARα escape it?

The lesson the disease model draws from the AKR1B1 and PRKCB failures (§4.4) is: *single-branch
blockade downstream of the ROS node is insufficient; one branch, late in a redundant network.*

**Where PPARα genuinely does escape:**
- **Opposite sign of intervention.** Blocking one of N parallel damaging branches yields benefit
  roughly ∝ 1/N and the network reroutes. **Inducing a protective transcriptional programme that
  acts on many branches at once is not divided that way** — it is additive across modules rather than
  fractional within one.
- **Topological position.** PPARα acts on P8 (lipid, the under-served axis), P6 (NF-κB), and P5
  (CAT, AMPK/SIRT1) simultaneously. Crucially, NF-κB/RELA is the **convergence node** for P2, P3, P4
  and P5 (model row 21). Transrepression at RELA is therefore **downstream of convergence**, not
  downstream of one branch — the exact opposite topological position to AKR1B1, which sits on one
  branch upstream of everything.
- **It is a hub, not an enzyme.** The AKR1B1 and PRKCB programmes each removed one catalytic
  activity. PPARα agonism reprograms a transcriptional network.

**Where the escape fails, and this is the part that matters:**
- **The same breadth claim was made for PKCβ and it failed.** PKC is also a hub — it feeds VEGF
  induction, occludin phosphorylation and retinal blood flow simultaneously. Topological breadth was
  argued then, and it did not save the programme. That is a direct precedent against the breadth
  argument as currently deployed for PPARα.
- **Transcriptional hubs have their own redundancy.** NF-κB has many parallel activating inputs that
  partial transrepression only damps; PPARγ, PPARδ, LXR and GR converge on the same corepressor
  machinery, so the tissue may already be partly buffered against gaining more of it.
- **The decisive objection: the AKR1B1/PRKCB failures are most parsimoniously explained not by
  topology at all, but by insufficient retinal target engagement at tolerated systemic doses.** Both
  programmes had strong animal data at concentrations achievable in a dosed rodent eye, and both
  failed in humans at human-tolerated systemic exposure. **If that is the real lesson, it is a
  pharmacokinetic lesson masquerading as a topology lesson — and PPARα is squarely in the same trap,
  with an acidic, 99%-albumin-bound ligand facing an efflux-competent barrier.**

**Verdict: PPARα escapes the *topological* version of the criticism and does not escape the
*pharmacokinetic* version.** Since the brief itself identifies retinal exposure as the critical path,
the failed-precedent history should be read as **corroborating the scout's exposure concern**, not as
a point in PPARα's favour. Agents citing "PPARα is a hub, therefore it escapes the AKR1B1 precedent"
are using the weaker half of the argument.

**And the escape route that actually works is a different one.** PPARα's genuine distinction is not
topology — it is **compartment architecture**: a target engaged with certainty in the liver, acting
on the retina through humoral intermediates (reduced remnant lipoproteins, raised ApoA1/HDL, raised
FGF21). *No other target in this set has an engagement-certain compartment that is not the diseased
compartment.* AKR1B1, PRKCB, NFE2L2 and the microglial targets must all be engaged **in the retina**
to work, and so face the identical PK problem with no exemption. That — not hub-ness — is PPARα's
real differentiator, and it is an argument that does not require the retinal target to be valid at all.

---

## 7. Target-level ranking

Expected value = validation strength × druggability × **achievable engagement in the compartment
that matters** × directional cleanliness × unmet-need fit. Note that validation and expected value
dissociate sharply at the top of the list — VEGFA is the best-validated target in DR and one of the
lowest expected-value targets *for this programme*, because its need is already served.

| Rank | Target | Druggability | Validation (DR) | Engagement confidence | Direction | Unmet need served | **EV score** |
|---|---|---|---|---|---|---|---|
| **1** | **PPARA — hepatic/systemic limb** (lipid lowering + FGF21 relay) | **KD, high** | L2–3 moderate | **High** — OATP1B1/1B3 concentrate fibrate anions; hepatic engagement not in doubt | **Clean** — net TG lowering despite ANGPTL4; FGF21 and ApoA1 right-signed | #1 (early systemic DMT), #5 (lipid/exudate axis) | **7.5** |
| **2** | **RELA/NF-κB via PPARα transrepression** (retinal endothelium) | RELA direct HARD; **tractable indirectly** at low occupancy (§4) | L3 strong (ICAM1/CD18 KO causal), L4 strong | **Marginal but not excludable** (§4.1) | Clean; no ANGPTL4 coupling | #1, #2 (non-VEGF DME limb) | **6.5** |
| **3** | **AGTR1** | **KD, highest in report** (class A GPCR) | L3 strong + human tissue; modest genetic | **High for the luminal pool** — no BRB crossing needed | Clean | #1, #3; plus renoprotection | **6.0** |
| **4** | **NFE2L2 / KEAP1** | KEAP1 **KD** (covalent); NFE2L2 HARD | L3 strong preclinical; L1 in other indications | Moderate (DMF is small and neutral; penetrant) | Clean, broad programme incl. GLO1, CAT | #1, #3 | **6.0** |
| **5** | **ANGPTL4 — as an INHIBITION target** *(inversion; not in candidate set)* | TD / KD-biologic | L4 (intraocular fluid) + L3 | n/a | Clean (inhibit) | #2 (VEGF-independent permeability) | **5.5** |
| **6** | **Microglial activation axis — if defined as CSF1R** | KD via CSF1R | L3 strong (depletion/causal), L4 | Moderate | Clean, but immune-suppressive risk | **#3 — zero competition** | **5.5** |
| **7** | **PPARA — retinal metabolic/transactivation limb** | KD | L2–3 moderate | **Low — probably does not occur** (§4.3) | Mixed: ACOX1 and local LPL conditionally wrong-signed; **couples to ANGPTL4** | #1, #5 | **4.0** |
| **8** | **VEGFA / KDR** *(context benchmark, not scored as candidate)* | KD | **L1 — the strongest validation of anything here** | Certain (intravitreal) | Clean | **Already served** — fails on need, not on biology | **3.5** |
| **9** | **Microglial axis as addressed by minocycline** | Target undefined | Unassessable on target axis | Unknown | Unknown | #3 | **3.5** |
| **10** | **PPARD** | KD | L3 weak; retinal role least defined | Moderate (most abundant retinal PPAR) | **Leaning WRONG — pro-angiogenic, strongest ANGPTL4 driver** | — | **3.0** |
| **11** | **PPARG** | KD | **L1 negative ocular signal** (fluid retention/ME) | High | Retinal pharmacology right-signed; **systemic fluid effect disqualifying** | — | **2.5** |
| **12** | **AKR1B1** | KD | **L1 NEGATIVE** | Moderate | **Obligate wrong-sign limb (4-HNE detox loss); futile kinetics at hyperglycaemia** | #1 nominally | **2.0** |

**Three observations about this ranking.**

- **Splitting PPARA into rows 1 and 7 is the single most consequential analytical choice in this
  report.** Treating "PPARα" as one target averages a high-confidence hepatic mechanism with a
  low-confidence retinal one and produces a misleadingly middling score. They have different
  engagement confidence, different directional cleanliness and different falsification experiments,
  and they should be scored and tested separately.
- **Validation and expected value dissociate at both ends.** VEGFA has the best validation and low EV
  (need already served). PPARα-hepatic has moderate validation and the highest EV (compartment
  certainty plus the largest unmet need). Any ranking that sorts on validation alone inverts this.
- **Direction-of-effect risk is distributed very unevenly and is routinely under-weighted.** AKR1B1's
  wrong-sign limb is obligate and unavoidable; PPARδ's is intrinsic to the isoform; PPARα's
  (ANGPTL4) is stage-dependent and, per §3, probably not engaged at achievable retinal occupancy.
  These are three very different severities and should not be scored as one generic "wrong-sign risk."

---

## 8. Interrogating the project data honestly

**Files read:** `evidence/ppara-interactions.tsv`, `evidence/compound-dr-target-matrix.tsv`,
`evidence/ppar-class-drug-properties.tsv`.

### 8.1 What I verified, with numbers

| Finding | Verification |
|---|---|
| `ppara-interactions.tsv` has **143 data rows, 5 columns**: `compound, cid, source, action, evidence_pmid` | `wc -l` = 144 incl. header; header inspected |
| **No affinity, no assay type, no structured direction field.** Direction must be parsed out of CTD free-text `action` strings | Column list |
| The DR panel in the matrix is **27 genes**: AGER, AKR1B1, ANGPT2, BAX, BCL2, CASP3, CAT, EDN1, HIF1A, ICAM1, IL1B, IL6, KDR, MMP9, NFE2L2, NFKB1, NOS3, PPARA, PPARD, PPARG, PRKCB, SERPINE1, SLC2A1, SOD2, TGFB1, TNF, VEGFA | Union of `targets` column |
| **ZERO PPARα lipid target genes in the panel.** No ANGPTL4, CPT1A, ACOX1, HMGCS2, FABP1/4/5, LPL, APOA1/A2/A5, ABCA1 or FGF21 | Gene-list diff |
| Only **2 of 143** PPARA rows mention any of those genes — both are *cholesterol* rows where cholesterol is the **readout inside someone else's mechanism string**, not a ligand | grep |
| **10 of 15 candidates appear nowhere in the matrix.** Present: Quercetin (26 targets), Melatonin (19), Linoleic Acid (18), Linalool (12), Linolenic Acid (8). **Absent: fenofibric acid, fenofibrate, pemafibrate, elafibranor, seladelpar, icosapent ethyl, epalrestat, dimethyl fumarate, minocycline, candesartan** | per-candidate grep |
| **Seladelpar (CHEMBL230158) is absent from `ppar-class-drug-properties.tsv`.** The 13 rows are troglitazone, gemfibrozil, clofibrate, pioglitazone ×2, rosiglitazone ×2, fenofibrate, fenofibric acid, pemafibrate, ciprofibrate, choline fenofibrate, elafibranor | full column-1/2 dump |
| `molecular_species` and `bioavailability_score` are **empty for every row** — confirms scout disclosure 6 | column dump |
| Matrix target counts are **bibliometric, not biological**: CAT 100 compounds, NFE2L2 70, VEGFA 49, NFKB1 44, ICAM1 38, NOS3 35, AKR1B1 22, **PPARD 14 vs PPARG 64** | per-gene counts |

### 8.2 What the data CAN support

1. **PPARα is a genuine fatty-acid-binding receptor.** The `binds to and results in increased
   activity of PPARA` rows for linoleic, α-linolenic, oleic and octanoic acids, plus the
   coactivator-recruitment rows (`promotes the reaction [PPARA binds to NCOA2/NCOA1]`,
   `affects [PPARA binds to CREBBP]`) for linoleic acid, are a real mechanistic readout of agonism.
   This underwrites the druggability call in §1 and the privileged-chemical-space observation.
2. **Relative physicochemistry of the PPAR class**, which I did use: fenofibric acid QED 0.85 / Ro5v 0
   (best in class), pemafibrate QED 0.24 / Ro5v 1 / MW 490.6 / PSA 94.3 (drug-likeness penalty is
   real and data-backed), elafibranor QED 0.41 / Ro5v 1 / aLogP 5.16.
3. **Polyphenol promiscuity as a liability.** Quercetin at 26/27 panel genes is a frequent-hitter
   signature, and the per-gene counts show the matrix measures literature volume.
4. **One genuinely good mechanistic datum**: the linalool row
   `PPARA gene mutant form results in decreased susceptibility to linalool` — a receptor-mutant
   phenotype is much harder to explain away than an expression change. Single source.

### 8.3 What the data CANNOT support — and this is most of it

1. **No drug→target mechanism edge exists anywhere in this project.** The ChEMBL mechanism and target
   tables are near-empty test extracts with zero PPAR content (brief §9). **Therefore not one
   drug→target claim in this report is data-backed.** Every statement that fenofibric acid, pemafibrate,
   elafibranor, seladelpar, epalrestat, DMF, minocycline or candesartan engages its nominal target is
   **knowledge-based**, full stop.
2. **The ANGPTL4 question — the central question I was asked — is unanswerable with this data.**
   ANGPTL4 is not in the 27-gene panel, appears in zero PPARA rows, and no PPARα target gene of any
   kind is represented. §2 and §3 are **entirely knowledge-based reasoning.** I want this stated
   plainly rather than buried: the most consequential analysis in this report has zero project-data support.
3. **No affinity, potency, selectivity or isoform-ratio data of any kind.** Every EC₅₀, K_d,
   selectivity fold and protein-binding figure referenced anywhere in this pipeline is general
   pharmacology knowledge.
4. **Nothing about retinal cell-type expression, compartment, or exposure.** The §1.1 expression
   analysis, the §4 occupancy argument and the whole exposure debate are outside this dataset's reach.
5. **Direction-of-effect for a PPARα agonist on any target gene.** Not representable in this schema.
6. **CTD evidence is expression-level, from a toxicology resource.** The best-controlled PPARα
   activation evidence in the entire file belongs to a phthalate plasticiser (scout §2.1). Row count
   is not evidence weight — and in this file, row count is approximately a measure of how often a
   compound appears in toxicology studies.

### 8.4 Data-quality items I am adding to the record

- **Seladelpar has no row in `ppar-class-drug-properties.tsv`.** The brief's designated isoform
  falsification control has no physicochemical data in the project. Worth fixing before the ranker
  weights it.
- **The 27-gene DR panel has a structural blind spot on the P8 axis.** It contains the three PPAR
  receptors but **not one PPAR effector gene**. Since the disease model identifies P8 (lipid
  handling) as *the under-served axis* and the focus target is the P8 master regulator, the panel
  cannot evaluate the pathway the whole run is about. **Recommend adding ANGPTL4, CPT1A, ACOX1,
  HMGCS2, FABP4, LPL, APOA1, ABCA1, FGF21, PLTP, CD36 and SCARB1 to the panel** before any future run.
- **`compound-dr-target-matrix.tsv` has no approved-drug coverage at all.** Every row is a
  phytochemical or an environmental chemical. The matrix cannot be used to compare approved-drug
  candidates — ten of fifteen candidates are simply absent — and any ranking that weights "number of
  DR-panel targets hit" will **systematically favour promiscuous polyphenols over approved drugs** as
  a pure artifact of which database the column was built from. This is a scoring-level hazard, not
  just a coverage gap, and the ranker should be warned explicitly.

---

## 9. Candidate scores (target axis)

Scores are **target-axis expected value**: quality of the target engaged × confidence that this
molecule engages it × confidence it does so in the compartment that matters × directional cleanliness.
ADMET, formulation, trial design and cost are other agents' axes and are deliberately excluded except
where they bear directly on target engagement.

| ID | Candidate | Score | Confidence | Basis | One-line target rationale |
|---|---|---|---|---|---|
| A3 | Pemafibrate | **7.5** | moderate | knowledge-based | Cleanest isoform discipline (>2,000× excludes the γ fluid-retention liability entirely); hepatoselectivity is a **feature** for the row-1 mechanism; best CKD profile |
| A1 | Fenofibric acid | **7.0** | moderate | mixed | Same row-1 target with certain hepatic engagement; best drug-likeness in class (QED 0.85, data-backed); renal elimination is the debit |
| A2 | Fenofibrate | **6.5** | moderate | mixed | Target-identical to A1 plus a hydrolysis step; adds exposure/formulation information, no target information |
| D4 | Candesartan cilexetil | **6.0** | moderate | knowledge-based | Best-druggable target in the set; luminal AT1R engageable without crossing the BRB; deployment problem is the ceiling |
| B4 | Icosapent ethyl | **5.5** | low | mixed | Scores on the **systemic lipid axis**, not on PPARα; EPA's receptor contribution is probably small, its membrane/eicosanoid mechanism is the real one |
| D2 | Dimethyl fumarate | **5.0** | moderate | knowledge-based | Good target (KEAP1 covalently tractable, NRF2 genuinely deficient), dirty and immunosuppressive ligand |
| B2 | α-Linolenic acid | **4.5** | moderate | **data-backed** | Real binder+activator in the data; non-selective and sub-potent, but ω-3 downstream metabolism is right-signed |
| C2 | Melatonin | **4.5** | low | mixed | Weak for PPARα; but a real MT1/MT2 target story and **the only candidate with unambiguous retinal access** — a genuinely useful instrument |
| A4 | Elafibranor | **4.0** | moderate | knowledge-based | δ co-agonism is a **liability** here (pro-angiogenic, doubled ANGPTL4 drive); Michael-acceptor enone |
| D3 | Minocycline | **3.5** | low | knowledge-based | Validated biology, **undefined molecular target**; ocular AEs (pigmentation, papilledema) in an ocular indication |
| B1 | Linoleic acid | **3.0** | moderate | **data-backed** | Strongest binding evidence in the file, but ω-6 feeds the arachidonate → ALOX12/15 axis the model flags as KO-validated for pericyte loss — **downstream wrong sign** |
| B3 | Linalool | **3.0** | low | **data-backed** | Best single mechanistic datum in the natural-product set (PPARA-mutant dependency), single source, no product |
| A5 | Seladelpar | **2.5** | moderate | knowledge-based | Confounded control, not clean (§5.1); δ is pro-angiogenic and the strongest ANGPTL4 driver; **zero project data** |
| D1 | Epalrestat | **2.0** | moderate | knowledge-based | Level-1 **negative**; obligate 4-HNE-detox wrong-sign limb; futile kinetics at hyperglycaemia |
| C1 | Quercetin | **2.0** | moderate | **data-backed (negatively)** | Direction-incoherent for PPARα in the project's own data (antagonises GW 7647); 26/27 is bibliometric; the frequent-hitter control |

**Falsification statements for the two scores ≥ 7** (required by brief §10):

- **A3 pemafibrate (7.5) is falsified if:** a matched-lipid-lowering non-PPAR comparator reproduces
  any retinal benefit (kills PPARα specificity); **or** chronic oral dosing in a diabetic model fails
  to produce measurable reduction in retinal leukostasis/ICAM1 despite achieving full hepatic target
  engagement (kills the retinal transrepression limb and leaves only the humoral relay, which
  pemafibrate's hepatoselectivity does not optimise for); **or** plasma/intraocular ANGPTL4 rises
  with measurable retinal permeability increase at any stage.
- **A1 fenofibric acid (7.0) is falsified if:** the same first two conditions hold; **or** if, in
  renally impaired patients at tolerated dose, achieved systemic TG/remnant reduction falls short of
  the threshold at which the row-1 humoral mechanism is plausible — i.e. if the renal dose cap
  eliminates the mechanism's own effect size.

---

## 10. Structured output

```json
{
  "agent": "Molecular Target Analyst (P1)",
  "candidates": [
    {
      "name": "Pemafibrate",
      "score": 7.5,
      "confidence": "moderate",
      "evidence_basis": "knowledge-based",
      "pathway": "P8 (primary, systemic/hepatic), P6 (secondary, retinal transrepression)",
      "stage": "S0-S3",
      "compartment": "liver/plasma (high-confidence engagement) -> humoral relay to inner BRB; retinal vascular endothelium (marginal)",
      "route": "oral",
      "assessment": "Target-axis leader. Sub-nanomolar potency with >2000x isoform selectivity gives the cleanest possible separation from the PPARg fluid-retention/macular-edema liability the brief demands be scored separately, and it is the only molecule in the set potent enough that even ~0.3% fractional retinal occupancy sits in a plausible range for the transrepression limb. Its hepatoselective design, which the scout counts against it, is a FEATURE under this report's central finding: the engagement-certain compartment is the liver, and the mechanism reaching the retina is humoral (reduced remnant lipoproteins, raised ApoA1/HDL, raised FGF21), not pharmacokinetic.",
      "strengths": [
        "Highest isoform discipline in the set (>2000x vs gamma and delta) - fully excludes the PPARg macular-edema class liability on mechanistic grounds",
        "Hepatic/biliary elimination; no dose adjustment in moderate CKD, in a population where renal impairment is the norm",
        "Hepatoselectivity optimises the one limb whose target engagement is certain (OATP1B1/1B3-concentrated hepatic PPARa)",
        "Only molecule in the set with the potency to actually test the retinal transrepression hypothesis",
        "ANGPTL4 risk is defused by the logical argument in section 3.2(i): the PPRE transactivation needed to induce it is the same machinery the exposure objection says is unavailable"
      ],
      "concerns": [
        "QED 0.24, Ro5v 1, MW 490.6, PSA 94.3 - worst drug-likeness in the PPAR class (data-backed from ppar-class-drug-properties.tsv)",
        "Hepatoselective design actively suppresses the extrahepatic exposure the retinal limb needs - a negative result would be ambiguous between 'PPARa does not help the retina' and 'drug never arrived'",
        "Higher potency makes hepatic/systemic ANGPTL4 induction more certain, raising plasma ANGPTL4 that a leaky S4 barrier would admit",
        "Zero project-data support for any drug-target edge; not present in compound-dr-target-matrix.tsv at all",
        "Retinal receptor abundance caps signal amplitude independently of occupancy (section 1.1) - a small fraction of a small number"
      ],
      "key_data_points": [
        "ppar-class-drug-properties.tsv CHEMBL247951: MW 490.56, aLogP 5.55, PSA 94.26, Ro5v 1, QED 0.24, first_approval 2017, oral True",
        "therapeutic_areas field reads only 'Cardiovascular Diseases'",
        "Absent from compound-dr-target-matrix.tsv (no DR-panel target edges)",
        "molecular_species and bioavailability_score empty, as for every row in the file"
      ]
    },
    {
      "name": "Fenofibric acid",
      "score": 7.0,
      "confidence": "moderate",
      "evidence_basis": "mixed",
      "pathway": "P8 (primary, systemic), P6 (secondary)",
      "stage": "S0-S3",
      "compartment": "liver/plasma -> humoral relay; retinal endothelium marginal",
      "route": "oral",
      "assessment": "The pragmatic co-leader. Same row-1 target architecture as pemafibrate with certain hepatic engagement via OATP concentration, and by a wide margin the best drug-likeness in the class (QED 0.85, Ro5v 0, verified in project data). Weak intrinsic potency matters much less than it appears once the mechanism is relocated to the hepatic compartment where the drug is concentrated well above plasma; the binding limitation that counts is the ~99% albumin binding against a tens-of-micromolar EC50 in the retina, which this analysis concludes removes the transactivation limb - and with it the ANGPTL4 liability.",
      "strengths": [
        "QED 0.85, Ro5v 0 - best drug-likeness of all 13 PPAR-class drugs in the project file (data-backed)",
        "Hepatic engagement via OATP1B1/1B3 is not in doubt; the systemic lipid limb plus the FGF21 endocrine relay reach the retina without any BRB crossing",
        "Decades of chronic-use data in exactly this comorbidity profile; once-daily; inexpensive",
        "Addresses unmet needs #1 (early systemic disease-modifying therapy) and #5 (lipid/hard-exudate axis) - the two largest white spaces",
        "Active moiety avoids the prodrug-conversion variable"
      ],
      "concerns": [
        "Renal elimination as the acyl glucuronide, in a population where diabetic kidney disease is near-universal - dose cap may eliminate the mechanism's own effect size",
        "Reversible creatinine rise confounds eGFR monitoring in a nephropathy population",
        "Myopathy/rhabdomyolysis signal in combination with statins, which this population is near-universally on",
        "Retinal fractional occupancy on the order of 0.3% - the retinal transactivation limb almost certainly does not operate",
        "Only ~10x selective over PPARg; the gamma fluid-retention liability is not fully excluded on mechanistic grounds the way it is for pemafibrate"
      ],
      "key_data_points": [
        "ppar-class-drug-properties.tsv CHEMBL981: MW 318.76, aLogP 3.81, PSA 63.60, Ro5v 0, QED 0.85, first_approval 2008, oral True",
        "therapeutic_areas includes 'Diabetes Mellitus, Type 2' - noted, NOT used as DR evidence (T2D is not DR); see blinding compliance",
        "Absent from compound-dr-target-matrix.tsv",
        "No drug-target mechanism edge exists anywhere in the project for this or any other approved drug"
      ]
    },
    {
      "name": "Fenofibrate",
      "score": 6.5,
      "confidence": "moderate",
      "evidence_basis": "mixed",
      "pathway": "P8, P6",
      "stage": "S0-S3",
      "compartment": "gut/liver (hydrolysis) -> same as fenofibric acid",
      "route": "oral",
      "assessment": "At the target level this is fenofibric acid plus an obligate ester-hydrolysis step; it contributes exposure and formulation information, not target information. Scored just below A1 because the active moiety is the better-characterised entity and the prodrug adds an absorption variable without adding target selectivity or potency. Its value to the pipeline is as a formulation comparator testing whether prodrug delivery changes the achieved exposure.",
      "strengths": [
        "Prodrug conversion to fenofibric acid is confirmed in project data (esterases, hepatic, 'more or less completely converted')",
        "Inherits the entire row-1 hepatic/humoral mechanism intact",
        "Higher lipophilicity (aLogP 4.68 vs 3.81) during the pre-hydrolysis window is the only way the set tests whether a neutral lipophilic species improves tissue distribution"
      ],
      "concerns": [
        "Adds no target-level information beyond A1 - same receptor, same selectivity, same compartment",
        "Food-effect and formulation variability in absorption",
        "QED 0.55 vs 0.85 for the acid (data-backed)",
        "Inherits every one of A1's renal and statin-interaction concerns after conversion"
      ],
      "key_data_points": [
        "ppar-class-drug-properties.tsv CHEMBL672: MW 360.84, aLogP 4.68, PSA 52.60, Ro5v 0, QED 0.55, first_approval 1993",
        "therapeutic_areas lists ~11 entries with no retinal or macular entry - noted and explicitly excluded from reasoning",
        "Absent from compound-dr-target-matrix.tsv"
      ]
    },
    {
      "name": "Candesartan cilexetil",
      "score": 6.0,
      "confidence": "moderate",
      "evidence_basis": "knowledge-based",
      "pathway": "cross-cutting (local retinal RAS), feeds P5/P6/P7",
      "stage": "S0-S3",
      "compartment": "luminal retinal vascular endothelium (engageable WITHOUT crossing the BRB) + systemic",
      "route": "oral",
      "assessment": "The highest-druggability target in the entire report and the only non-PPAR candidate with a structural answer to the exposure objection: AT1R is expressed on the luminal endothelial surface, so a blood-borne insurmountable antagonist engages a meaningful receptor pool without BRB penetration. The retina has a complete local renin-angiotensin system driving NOX activation, VEGF induction and neuronal loss. Its ceiling is set not by biology but by deployment - much of this population is already RAS-blocked, so a trial really tests dose intensification.",
      "strengths": [
        "Class A GPCR - the best-validated druggable family in medicine; potent slowly-dissociating antagonist with sustained occupancy",
        "Luminal AT1R engagement requires no BRB crossing - a genuine exposure advantage shared only with PPARa's humoral outputs",
        "Local retinal RAS is validated at the human-tissue-expression level with modest genetic support (disease model row 66)",
        "Renoprotective in a cohort where renal impairment is the norm - a real ancillary benefit, not a nice-to-have",
        "Zero PPAR involvement makes it a clean mechanistic contrast for the pipeline"
      ],
      "concerns": [
        "Deployment problem - much of the target population is already on RAS blockade; the marginal untreated population is narrow",
        "Blood-pressure lowering is an unavoidable confounder; benefit cannot be cleanly attributed to retinal AT1R",
        "Hyperkalemia and acute eGFR decline cap the dose in CKD",
        "Hypotension limits exposure escalation in normotensive patients",
        "Ro5v 3 as the cilexetil ester (data-backed) - mitigated by obligate pre-systemic hydrolysis"
      ],
      "key_data_points": [
        "CHEMBL1014; ester prodrug, Ro5v 3 as cilexetil, hydrolysed during absorption to candesartan",
        "Disease model row 66 documents the complete local retinal RAS including the suppressed protective ACE2/Ang-(1-7)/MAS1 arm",
        "Absent from compound-dr-target-matrix.tsv - no project-data target edge"
      ]
    },
    {
      "name": "Icosapent ethyl",
      "score": 5.5,
      "confidence": "low",
      "evidence_basis": "mixed",
      "pathway": "P8 (systemic lipid), P8.6 (eicosanoid/resolvin)",
      "stage": "S0-S2",
      "compartment": "plasma/systemic; membrane incorporation",
      "route": "oral",
      "assessment": "Scores on the systemic lipid and eicosanoid axes rather than on PPARa. EPA's PPARa engagement is weak, non-selective and almost certainly a minor contributor at achievable concentrations; its better-validated mechanisms are membrane incorporation competing with arachidonate and E-series resolvin generation, plus genuine triglyceride lowering. Under this report's central finding that the systemic lipid limb is the defensible one, that is not a demotion - but the candidate should be understood as a lipid-axis agent, not a PPARa agent.",
      "strengths": [
        "The only way the replicated fatty-acid PPARa binding evidence in the project data reaches an approved oral product",
        "Chemically continuous with the data-backed linoleic/alpha-linolenic binding evidence (section 8.2)",
        "Right-signed downstream eicosanoid profile - competes with arachidonate, yields E-series resolvins, opposite direction to the omega-6 arm",
        "Genuine systemic triglyceride/remnant lowering - the row-1 mechanism, by a non-PPAR route",
        "Excellent chronic tolerability relative to every other candidate here"
      ],
      "concerns": [
        "PPARa contribution is probably small - micromolar, non-selective, and competing with an abundant endogenous fatty-acid pool for the same pocket",
        "Non-selective across alpha/gamma/delta, so the isoform discipline the brief demands is absent",
        "Effect size on the lipid axis is modest relative to a fibrate",
        "No project data at all (absent from both the matrix and the PPAR properties file)",
        "Bleeding-risk signal in a population frequently on antiplatelets"
      ],
      "key_data_points": [
        "CHEMBL2095209: MW 330.51, aLogP 6.47, PSA 26.30, Ro5v 1, oral, approved 2012 (from scout, blinded data)",
        "Class inference rests on the data-backed binding rows for linoleic acid (PMIDs 10403814, 15491415, 16731579, 19263263, 23843199, 35752307) and alpha-linolenic acid",
        "Absent from compound-dr-target-matrix.tsv"
      ]
    },
    {
      "name": "Dimethyl fumarate",
      "score": 5.0,
      "confidence": "moderate",
      "evidence_basis": "knowledge-based",
      "pathway": "P5 (oxidative/mitochondrial), spillover to P6 and P2 via GLO1",
      "stage": "S0-S2",
      "compartment": "systemic; small neutral molecule with real tissue penetration",
      "route": "oral",
      "assessment": "A good target carried by a problematic ligand. KEAP1 is covalently tractable with clinical precedent and NRF2 is genuinely functionally deficient in diabetic retina - making the restore-deficiency framing MORE defensible here than for PPARa, since the deficiency sits in a repressible system an activator can actually relieve. The brief's 'antioxidant-only is null' prior should be applied carefully: NRF2 is a catalytic transcriptional programme including GLO1 and catalase, not a stoichiometric scavenger. The ligand is the problem.",
      "strengths": [
        "KEAP1 C151 covalent modification is real, demonstrable target engagement with established clinical precedent in another indication",
        "MW 144, aLogP -0.11, PSA 52.6, neutral - by far the best physicochemistry for tissue penetration in the entire candidate set",
        "NRF2 programme spans the P5 oxidative axis AND the P2 AGE axis via GLO1 (model row 14) and intersects catalase - genuinely multi-module",
        "Independently anti-inflammatory via direct RelA interference, not only antioxidant",
        "Tests the Nrf2 limb of the PPARa hypothesis directly rather than through crosstalk - a well-designed comparator"
      ],
      "concerns": [
        "Lymphopenia with PML risk on chronic dosing - serious in a chronically infection-prone diabetic population needing lifelong therapy",
        "Promiscuous Michael acceptor - acutely depletes glutathione, succinates many proteins including GAPDH; the mechanism is not cleanly NRF2",
        "No DR clinical validation at any level; the brief's prior against antioxidant-only mechanisms applies partially",
        "GI intolerance and flushing limit adherence in chronic use",
        "Zero project-data support; absent from compound-dr-target-matrix.tsv"
      ],
      "key_data_points": [
        "CHEMBL2107333: MW 144.13, aLogP -0.11, PSA 52.60, Ro5v 0, oral, approved 2013",
        "NFE2L2 is the second-most-represented node in the project matrix (70 compounds) - but that count is bibliometric, not biological",
        "Disease model row 22 records NFE2L2 as 'functionally deficient' in diabetic retina; row 23 records KEAP1 as covalent-ligand tractable (KD)"
      ]
    },
    {
      "name": "Alpha-linolenic acid",
      "score": 4.5,
      "confidence": "moderate",
      "evidence_basis": "data-backed",
      "pathway": "P8",
      "stage": "S0-S2",
      "compartment": "systemic/membrane",
      "route": "oral (dietary)",
      "assessment": "One of only three compounds in all 143 PPARA rows with replicated binding-plus-activation evidence, which makes it the mechanistic anchor for the fatty-acid-sensor claim underpinning the whole druggability assessment. As a candidate it is weak - micromolar, non-selective across all three isoforms, and not a drug - but its downstream metabolism to EPA/DHA and the resolvin series is right-signed, which separates it meaningfully from linoleic acid.",
      "strengths": [
        "Genuine data-backed binding plus activation: 'binds to and results in increased activity of PPARA' across PMIDs 10403814, 16731579, 19667161",
        "Omega-3 downstream metabolism is right-signed for DR - feeds EPA/DHA, the ADIPOR1/ELOVL4 retinal retention axis (model rows 51-52), and pro-resolving mediators",
        "Hits 8 DR-panel genes including CAT, IL1B, IL6, NFE2L2, TNF and all three PPARs (data-backed)",
        "Establishes that natural-product chemical space is intrinsically privileged for this receptor"
      ],
      "concerns": [
        "Non-selective - also binds and activates PPARG, so the isoform discipline the brief demands is absent",
        "Micromolar affinity against an abundant competing endogenous fatty-acid pool - net pharmacological effect on receptor occupancy is likely negligible",
        "Not a drug product; dosing, formulation and exposure are undefined",
        "Poor conversion efficiency of ALA to EPA/DHA in humans limits the right-signed downstream argument",
        "CTD rows are literature-curated statements, not quantified affinity"
      ],
      "key_data_points": [
        "ppara-interactions.tsv: 'binds to and results in increased activity of PPARA' (PMID 10403814, 16731579, 19667161)",
        "compound-dr-target-matrix.tsv 'Linolenic Acid': 8 targets - CAT, IL1B, IL6, NFE2L2, PPARA, PPARD, PPARG, TNF; hits_PPARA YES",
        "One of exactly 3 compounds in 143 rows with replicated binding+activation evidence"
      ]
    },
    {
      "name": "Melatonin",
      "score": 4.5,
      "confidence": "low",
      "evidence_basis": "mixed",
      "pathway": "P5, P9",
      "stage": "S0-S1",
      "compartment": "neural retina, RPE, inner BRB - unambiguous access, synthesised in situ",
      "route": "oral",
      "assessment": "Weak for PPARa - its project rows are cisplatin-protection expression associations with no engagement evidence - but it earns its score on a different basis: it has a real GPCR target story (MT1/MT2, druggable class), is physiologically synthesised in retina, and is the one candidate in the set with unambiguously good retinal access. As the pipeline's exposure control it is a genuinely well-chosen instrument for testing whether access beats affinity, which is the single question the brief says is on the critical path.",
      "strengths": [
        "MW 232, neutral, crosses the BRB freely - the only candidate with no exposure objection at all",
        "MT1/MT2 are class A GPCRs (KD) and melatonin is physiologically synthesised in retina, so the receptor system is demonstrably present and active",
        "19/27 DR-panel genes in project data, spanning P5 and P9 nodes",
        "Direct mitochondrial and anti-apoptotic actions independent of receptor occupancy",
        "Outstanding chronic safety - the lowest-risk candidate in the set by a wide margin"
      ],
      "concerns": [
        "PPARA evidence is the weakest class - expression-protection rows only, no engagement",
        "Antioxidant-adjacent framing collides directly with the brief's prior against antioxidant-only mechanisms",
        "19/27 target count is bibliometric breadth, not demonstrated polypharmacology",
        "Short half-life and chronobiological effects complicate chronic dosing for a non-sleep endpoint",
        "Effect size in any vascular endpoint is likely small"
      ],
      "key_data_points": [
        "compound-dr-target-matrix.tsv: Melatonin, 19 targets, hits_PPARA YES - but the PPARA rows are expression-protection only",
        "249 CTD rows total (per scout), dominated by expression-level associations",
        "The brief designates it the exposure control (section 8, C2)"
      ]
    },
    {
      "name": "Elafibranor",
      "score": 4.0,
      "confidence": "moderate",
      "evidence_basis": "knowledge-based",
      "pathway": "P8, P6",
      "stage": "S0-S2",
      "compartment": "liver/systemic",
      "route": "oral",
      "assessment": "The PPARdelta co-agonism that is meant to add value is, on this analysis, a liability rather than a benefit. PPARdelta is the most abundantly expressed PPAR in retina, is pro-angiogenic, induces VEGFA, and is at least as strong an ANGPTL4 driver as PPARa - so a dual alpha/delta agonist carries a doubled wrong-sign limb in exactly the tissue of interest, plus the electrophilic enone. Potency is real but directed partly at the wrong isoform.",
      "strengths": [
        "Low-nanomolar potency at PPARa - a real engagement case, unlike the fibric acids",
        "Oral, approved 2024, so the development path is de-risked",
        "Tests the delta-co-agonism hypothesis explicitly, which has value as information even if the answer is negative",
        "Ro5v 1, QED 0.41 - better drug-likeness than pemafibrate (data-backed)"
      ],
      "concerns": [
        "PPARdelta is pro-angiogenic in retina and induces VEGFA - a directionally adverse co-mechanism in a neovascular disease",
        "Delta drives ANGPTL4 at least as hard as alpha, doubling the one wrong-sign limb this report takes seriously",
        "Michael-acceptor enone - covalent off-target reactivity and idiosyncratic-toxicity risk on chronic lifelong dosing",
        "aLogP 5.16 with Ro5v 1 (data-backed) - high lipophilicity compounds the protein-binding problem",
        "No isoform discipline: the brief explicitly demands alpha and delta/gamma be scored separately, and this molecule prevents that"
      ],
      "key_data_points": [
        "ppar-class-drug-properties.tsv CHEMBL3707395: MW 384.50, aLogP 5.16, PSA 63.60, Ro5v 1, QED 0.41, first_approval 2024",
        "SMILES confirms the enone Michael acceptor: CSc1ccc(C(=O)/C=C/c2...)cc1",
        "PPARD appears in 14 matrix rows vs PPARG 64 - a literature-volume artifact, not a biological ranking"
      ]
    },
    {
      "name": "Minocycline",
      "score": 3.5,
      "confidence": "low",
      "evidence_basis": "knowledge-based",
      "pathway": "P9, P6",
      "stage": "S0-S1",
      "compartment": "neural retina, microglia",
      "route": "oral",
      "assessment": "The target axis is unassessable for this candidate: minocycline's molecular target for microglial deactivation has never been established, with proposed mediators spanning zinc-chelation-dependent MMP inhibition, 5-LOX, PARP1, caspase-1 and p38. The underlying biology - microglial activation in the neurovascular unit - is genuinely validated and addresses the one unmet need (neuroprotection) with zero competition, but CSF1R is the defined, druggable handle on it and minocycline is a blunt stand-in. Ocular adverse effects are a specific rather than generic problem here.",
      "strengths": [
        "Microglial activation in the neurovascular unit is well validated at P9/S0 by depletion and causal studies",
        "Addresses unmet need #3 (neuroprotection independent of anatomy) which has no competing therapy at all",
        "Real CNS penetration despite PSA 164.63 - unusual for the tetracycline class and relevant to retinal access",
        "Oral, approved 1971, extremely well-characterised systemic safety at short duration"
      ],
      "concerns": [
        "No defined molecular target - cannot be target-validated at all; scorable only on the phenotype axis",
        "Chronic dosing causes scleral and conjunctival pigmentation, and benign intracranial hypertension with papilledema - ocular adverse mechanisms in an ocular indication",
        "Vestibular toxicity limits chronic adherence",
        "Chronic antibiotic exposure and microbiome/resistance consequences over a lifelong indication",
        "CSF1R inhibition would test the same hypothesis with defined, measurable target engagement"
      ],
      "key_data_points": [
        "CHEMBL1434: MW 457.48, aLogP 0.19, PSA 164.63, Ro5v 0, oral, approved 1971",
        "Absent from compound-dr-target-matrix.tsv - no project-data target edge",
        "Disease model places microglial/neurovascular degeneration at P9 with S0 onset, before visible vasculopathy"
      ]
    },
    {
      "name": "Linoleic acid",
      "score": 3.0,
      "confidence": "moderate",
      "evidence_basis": "data-backed",
      "pathway": "P8, with downstream P8.6 liability",
      "stage": "S0-S2",
      "compartment": "systemic/membrane",
      "route": "oral (dietary)",
      "assessment": "The strongest single body of binding evidence in the entire project dataset - the only compound in 143 rows with binding, activation AND coactivator-recruitment rows across six independent PMIDs - and simultaneously a candidate with a downstream wrong-sign problem. As an omega-6 it feeds the arachidonate pool and therefore the ALOX12/ALOX15 axis that the disease model flags as KO-validated for pericyte loss and Muller ER stress. Its scientific value is as the mechanistic anchor for PPARa-as-fatty-acid-sensor, not as a therapy.",
      "strengths": [
        "Best data-backed PPARa evidence in the project: binding + activation + NCOA1/NCOA2/CREBBP recruitment across PMIDs 10403814, 15491415, 16731579, 19263263, 23843199, 35752307",
        "Coactivator recruitment is a genuine mechanistic readout of agonism, not an expression association",
        "18/27 DR-panel genes with hits_PPARA YES (data-backed)",
        "Anchors the druggability argument that natural-product chemical space is privileged for this receptor"
      ],
      "concerns": [
        "Omega-6 - downstream metabolism feeds arachidonate and the ALOX12/ALOX15 axis the disease model records as strong KO-validated for pericyte loss (model row 59). A downstream wrong sign",
        "Non-selective across all three PPAR isoforms, including the gamma arm the brief wants excluded",
        "Micromolar affinity competing with an abundant endogenous pool - negligible net pharmacological effect on occupancy",
        "Not a drug product; no dosing, formulation or exposure definition",
        "A bare DGIdb row with empty action/evidence also exists - zero information, must not be counted as corroboration"
      ],
      "key_data_points": [
        "compound-dr-target-matrix.tsv: Linoleic Acid, 18 targets, hits_PPARA YES",
        "ppara-interactions.tsv: unique in carrying binding + activation + coactivator-recruitment rows",
        "Disease model row 59: ALOX12/ALOX15 validated 'P (strong, KO-validated)' for pericyte loss and VEGF induction"
      ]
    },
    {
      "name": "Linalool",
      "score": 3.0,
      "confidence": "low",
      "evidence_basis": "data-backed",
      "pathway": "P8",
      "stage": "S0-S1",
      "compartment": "systemic",
      "route": "oral (undefined)",
      "assessment": "Carries the single best-designed mechanistic datum in the project's natural-product set - a PPARA receptor-mutant phenotype altering susceptibility, which is far harder to explain away than any expression association - alongside binding, activation and PPARa-dependent SLC27A4 induction. But it is one report, one laboratory, and linalool is a volatile monoterpene with rapid first-pass metabolism, no product form and no exposure data. Scientifically interesting, not developable as presented.",
      "strengths": [
        "'PPARA gene mutant form results in decreased susceptibility to linalool' - genetic-dependency evidence, the highest-quality evidence type in the entire 143-row file",
        "Binding plus activation plus a PPARa-dependent transcriptional output (SLC27A4) in the same report",
        "12/27 DR-panel genes with hits_PPARA YES (data-backed)",
        "Best non-fatty-acid natural-product PPARa evidence available in this dataset"
      ],
      "concerns": [
        "Single source (PMID 24752549) - no independent replication anywhere in the file",
        "Volatile monoterpene with rapid metabolism and no defined product form, dose or exposure",
        "Selectivity across PPAR isoforms entirely uncharacterised",
        "Potency almost certainly weak; no affinity data exists in the project or is cited anywhere",
        "Fragrance-chemical class with sensitisation liabilities at chronic exposure"
      ],
      "key_data_points": [
        "ppara-interactions.tsv PMID 24752549: binds + increases activity + PPARA-mutant susceptibility row",
        "compound-dr-target-matrix.tsv 'Linalool, (+/-)-': 12 targets, hits_PPARA YES",
        "The only receptor-mutant dependency row in all 143 PPARA interactions"
      ]
    },
    {
      "name": "Seladelpar",
      "score": 2.5,
      "confidence": "moderate",
      "evidence_basis": "knowledge-based",
      "pathway": "P8 (delta), P6",
      "stage": "n/a - control arm",
      "compartment": "liver/systemic",
      "route": "oral",
      "assessment": "Designated the isoform falsification control, but it is confounded rather than clean. PPARdelta is the most abundantly expressed PPAR in retina, is pro-angiogenic, induces VEGFA, drives ANGPTL4 at least as strongly as PPARa, and shares the identical NF-kB transrepression machinery - so a positive result is ambiguous between delta-specific and shared-class transrepression, and a negative result is equally explained by exposure. A control that is weak when negative and ambiguous when positive is not a good control. The decisive control the programme actually needs is a matched-lipid-lowering non-PPAR comparator.",
      "strengths": [
        "Potent and genuinely delta-selective - it does cleanly separate the isoforms pharmacologically, whatever the inferential problems",
        "Oral, with an established development path",
        "If delta agonism were retinally protective it would be informative; the arm is not worthless, only confounded"
      ],
      "concerns": [
        "PPARdelta is pro-angiogenic in retina and induces VEGFA - this arm has its own plausible HARM mechanism, so it is not a neutral comparator",
        "Shares transrepression machinery with PPARa, so a positive result would not validate alpha",
        "Drives ANGPTL4 at least as hard as alpha - amplifies rather than controls for the wrong-sign concern",
        "Absent from ppar-class-drug-properties.tsv entirely (verified - the file has 13 rows, none seladelpar): the designated control has zero project-data backing",
        "Tests the wrong null hypothesis; the question at risk is 'PPARa engagement vs lipid lowering', not 'alpha vs delta'"
      ],
      "key_data_points": [
        "CHEMBL230158 does NOT appear in ppar-class-drug-properties.tsv - verified against the full 13-row file",
        "Absent from compound-dr-target-matrix.tsv",
        "PPARD appears in 14 matrix rows, PPARG in 64, PPARA in 36 - counts reflect toxicology literature volume, not retinal biology"
      ]
    },
    {
      "name": "Epalrestat",
      "score": 2.0,
      "confidence": "moderate",
      "evidence_basis": "knowledge-based",
      "pathway": "P1 (polyol)",
      "stage": "S0-S2",
      "compartment": "pericytes, Muller glia",
      "route": "oral",
      "assessment": "The weakest target in the set despite good druggability. The disease model records Level-1 NEGATIVE human evidence for aldose reductase inhibition in DR - the most informative single datum about any target here, pointing the wrong way. Worse, AKR1B1 also detoxifies 4-HNE and other reactive lipid aldehydes at the same catalytic site, so inhibition carries an obligate wrong-sign limb that, unlike ANGPTL4's, cannot be escaped by stage selection or by low occupancy. And the enzyme's high Km for glucose means partial inhibition leaves large residual flux at diabetic glucose concentrations.",
      "strengths": [
        "AKR1B1 is highly druggable - deep anion-binding active site, multiple chemotypes, approved in some markets",
        "The most mechanistically specific non-PPAR alternative in the set; AKR1B1 is in the DR panel",
        "Favourable physicochemistry: MW 319.41, aLogP 2.92, Ro5v 0, oral",
        "Directly addresses pericyte osmotic and oxidative stress, a genuine early S0-S2 lesion"
      ],
      "concerns": [
        "Level-1 NEGATIVE clinical evidence - multiple programmes, no convincing effect on DR progression despite strong animal data (disease model section 4.4)",
        "Obligate wrong-sign limb: AKR1B1 detoxifies 4-HNE and reactive aldehydes at the same site, so inhibition removes a protective function unavoidably (model row 10)",
        "High Km for glucose means polyol flux is near first-order across the diabetic range; partial inhibition leaves large residual flux",
        "Exemplifies precisely the failed single-branch-blockade pattern the brief says should lose points",
        "Carboxylic acid - shares the ionisation and protein-binding exposure problem with the fibrates, with no hepatic-concentration exemption"
      ],
      "key_data_points": [
        "CHEMBL56337: MW 319.41, aLogP 2.92, PSA 57.61, Ro5v 0, oral, approved 1992",
        "Disease model row 10 flags AKR1B1 validation as 'C (negative trials)' and notes its 4-HNE detoxification role",
        "Disease model section 4.4: 'no convincing effect on DR progression in humans despite strong animal data'",
        "22 compounds hit AKR1B1 in the matrix, all phytochemicals - epalrestat itself is absent"
      ]
    },
    {
      "name": "Quercetin",
      "score": 2.0,
      "confidence": "moderate",
      "evidence_basis": "data-backed",
      "pathway": "nominally P1/P5/P6/P7 - none specifically",
      "stage": "S0-S2",
      "compartment": "systemic (negligible exposure)",
      "route": "oral",
      "assessment": "The project's own data argues against it. Its seven PPARA rows are all expression-protection constructions, and one of them records quercetin ANTAGONISING the reference PPARa agonist GW 7647 - so it cannot be scored as a PPARa activator on this record. Its 26/27 DR-panel coverage is a bibliometric artifact of how heavily quercetin has been studied in toxicology, not demonstrated polypharmacology, and oral bioavailability under 2% means systemic exposure is negligible regardless. It functions well as the pipeline's frequent-hitter control.",
      "strengths": [
        "Broadest nominal DR-panel coverage in the dataset (26/27) with the best action-string ratio among the polyphenols",
        "Does hit genuinely relevant nodes nominally - NFE2L2, AKR1B1, VEGFA, ICAM1, MMP9",
        "Well-characterised safety from extensive dietary exposure",
        "Serves a real function as the frequent-hitter calibration control"
      ],
      "concerns": [
        "DIRECTION-INCOHERENT for PPARa in the project's own data - antagonises GW 7647 (PMID 18393431) while elsewhere appearing as a protector of PPARA expression",
        "All 7 PPARA rows are 'blunts an insult-induced fall in PPARA expression' - not target engagement in any row",
        "Oral bioavailability under 2% - systemic exposure cannot support any mechanism",
        "26/27 coverage is literature volume, not polypharmacology; classic PAINS/frequent-hitter profile the brief says should lose points",
        "No specific mechanistic argument distinguishes it from any other promiscuous polyphenol"
      ],
      "key_data_points": [
        "compound-dr-target-matrix.tsv: Quercetin, 26 targets, hits_PPARA YES - the highest count in the file",
        "PMID 18393431: 'Quercetin inhibits the reaction [GW 7647 results in increased activity of PPARA protein]' - antagonism of a reference agonist",
        "745 CTD rows (per scout) - the row count is a measure of study volume, not evidence weight"
      ]
    }
  ],
  "cross_cutting_observations": "Five target-level findings. (1) SPLIT PPARA INTO TWO TARGETS. The hepatic/systemic limb (OATP1B1/1B3-concentrated, engagement certain, outputs humoral - reduced remnant lipoproteins, raised ApoA1/HDL, raised FGF21) and the retinal limb (occupancy ~0.3%, engagement marginal) have different confidence, different directional cleanliness and different falsification experiments. Averaging them produces a misleadingly middling score. PPARa-hepatic is the highest-expected-value target in the set; PPARa-retinal-transactivation ranks 7th. (2) THE ANGPTL4 AND EXPOSURE OBJECTIONS ARE MUTUALLY DESTRUCTIVE. ANGPTL4 induction is PPRE-driven transactivation - the same machinery the exposure objection says is unavailable in retina. If retinal transactivation is too weak to help it is too weak to harm. The scout's section 7 treats ANGPTL4 as sharpening the exposure objection; it in fact conflicts with it. (3) TRANSREPRESSION BUYS 1-2 LOG10 OF EFFECTIVE POTENCY for the inflammatory limb only, on four independent grounds (blocking vs driving stoichiometry, non-consumption of the receptor, the superfamily-wide dissociated-ligand precedent, and the nonlinear ICAM1-density threshold for leukostasis under shear). Synthesis: at achievable retinal occupancy, oral PPARa agonism behaves as a PHARMACOKINETICALLY DISSOCIATED LIGAND - transrepression without transactivation, and therefore without ANGPTL4. Testable in one experiment. (4) LOW RECEPTOR ABUNDANCE AND LOW LIGAND EXPOSURE ARE DIFFERENT OBJECTIONS and are being conflated. Fractional occupancy is independent of receptor number; abundance caps signal AMPLITUDE, not whether signalling starts. They compound multiplicatively but have different remedies - occupancy is fixable with potency, amplitude is not. (5) THE FAILED-PRECEDENT LESSON IS PHARMACOKINETIC, NOT TOPOLOGICAL. PPARa escapes the topology version of the AKR1B1/PRKCB criticism (it induces a protective programme across modules and transrepresses at the NF-kB convergence node rather than blocking one branch) but does NOT escape the PK version - both failed programmes had strong animal data and failed at human-tolerated systemic exposure, exactly PPARa's situation. The precedent therefore CORROBORATES the scout's exposure concern rather than being answered by hub-ness. PPARa's real differentiator is compartment architecture, not topology: it is the only target here with an engagement-certain compartment that is not the diseased compartment.",
  "strongest_candidate": "Pemafibrate (7.5), with fenofibric acid (7.0) as the pragmatic co-leader on different grounds. Pemafibrate wins the target axis on isoform discipline (>2000x selectivity fully excludes the PPARg macular-edema class liability the brief demands be scored separately), on renal safety in a population where CKD is the norm, and because its hepatoselective design - which the scout counts against it - optimises exactly the limb this analysis finds defensible. Fenofibric acid wins on drug-likeness (QED 0.85, Ro5v 0, data-backed) and chronic-use experience, and loses on renal elimination in a nephropathy population. The choice is not between molecules but between mechanisms: if the operative limb is the systemic/humoral one, either works and fenofibric acid is cheaper; if it is retinal transrepression, only pemafibrate has the potency to test it.",
  "biggest_concern": "That the entire PPARa hypothesis may be a LIPID-LOWERING hypothesis wearing a receptor's name, and the candidate set as constructed cannot tell the difference. Every retinal limb depends on an occupancy argument that is unmeasured and probably unfavourable; the one limb with certain target engagement (hepatic) produces its retinal effect through intermediates - lower remnant lipoproteins, higher ApoA1/HDL, higher FGF21 - that a non-PPAR lipid-lowering agent would partly reproduce. The isoform control the brief specifies (seladelpar) tests alpha-vs-delta, which is the wrong question and is confounded anyway because PPARdelta is pro-angiogenic in retina. The question genuinely at risk is PPARa-engagement-versus-lipid-lowering, and NO arm of the current 15-candidate set addresses it. Secondary concern: the project's 27-gene DR panel contains all three PPAR receptors and not one PPAR effector gene, so the run's focus pathway is structurally invisible to its own data.",
  "question_for_other_agents": "To the ADMET and Clinical Feasibility agents: can you bound the retinal free-drug concentration achieved by oral pemafibrate versus oral fenofibric acid well enough to say whether either reaches 1-10% fractional PPARa occupancy in retinal endothelium? This report argues that transrepression needs 1-2 log10 less occupancy than transactivation, which would move the inflammatory limb from impossible to marginal - but that conclusion is entirely contingent on the occupancy number, which no one has yet bounded. To the Literature Reviewer: in your post-hoc unblinding section only, is there any human measurement of intraocular ANGPTL4 in fibrate-exposed versus unexposed diabetic patients? That single measurement would settle section 3 empirically rather than by argument. To the Candidate Ranker: please score PPARa-hepatic and PPARa-retinal as SEPARATE mechanisms rather than averaging them, and please do not use seladelpar as the falsification arm - add a matched-lipid-lowering non-PPAR comparator instead, because that is the control that tests the hypothesis actually at risk.",
  "data_gaps": "VERIFIED IN THIS RUN. (1) The 27-gene DR panel in compound-dr-target-matrix.tsv contains PPARA, PPARD and PPARG but ZERO PPARa effector genes - no ANGPTL4, CPT1A, ACOX1, HMGCS2, FABP1/4/5, LPL, APOA1/A2/A5, ABCA1 or FGF21. Only 2 of 143 PPARA rows mention any of them, and both are cholesterol rows where cholesterol is the readout inside another compound's mechanism string. The central question of this analysis is therefore unanswerable from project data. Recommend adding ANGPTL4, CPT1A, ACOX1, HMGCS2, FABP4, LPL, APOA1, ABCA1, FGF21, PLTP, CD36 and SCARB1 to the panel. (2) Ten of fifteen candidates appear NOWHERE in the matrix - every Group A drug, every Group D drug, and icosapent ethyl. Only quercetin (26), melatonin (19), linoleic acid (18), linalool (12) and linolenic acid (8) are present. The matrix contains no approved-drug coverage at all; every row is a phytochemical or environmental chemical. (3) SCORING HAZARD: because the matrix is built from a phytochemical/toxicology source, any ranking weighting 'number of DR-panel targets hit' will systematically favour promiscuous polyphenols over approved drugs as a pure database artifact. Per-gene counts confirm the bibliometric character - CAT 100 compounds, NFE2L2 70, VEGFA 49, NFKB1 44, ICAM1 38, AKR1B1 22, PPARD 14 vs PPARG 64. (4) Seladelpar (CHEMBL230158) is absent from ppar-class-drug-properties.tsv - the designated isoform falsification control has no physicochemical data in the project at all. (5) ppara-interactions.tsv carries only compound/cid/source/action/evidence_pmid - no affinity, no assay type, no structured direction field; direction must be parsed from CTD free text. (6) molecular_species and bioavailability_score are empty for every row, confirming scout disclosure 6. (7) No drug-to-target mechanism edge exists anywhere in the project (ChEMBL mechanism/target tables are near-empty test extracts with zero PPAR content), so NOT ONE drug-target claim in this report is data-backed.",
  "blinding_compliance": "FILES READ, exhaustively: disease-brief.md; disease-model.md sections 4.4, 5.1, 5.2 and 6 headings; agents/p0-ppara-scout.md sections 2, 4, 5, 6, 7, 8, 9; .claude/skills/target-profiler/SKILL.md; evidence/ppara-interactions.tsv; evidence/compound-dr-target-matrix.tsv; evidence/ppar-class-drug-properties.tsv. I did NOT open data/processed/chembl_approved_drugs.csv, anything under data/holdout/, or any answer-key file. I did not consult git history, git objects, or any other route to redacted values. I did not grep for redaction markers and made no attempt to identify which rows were redacted. DISCLOSURES, including negative decisions. (1) I did not use, and do not assert, any DR or DME indication, approval, guideline position or trial result for any of the 15 candidates. Fenofibric acid's therapeutic_areas field reads 'Alcoholism; Medulloblastoma; Hypercholesterolemia; Cholestasis; Hypertriglyceridemia; Diabetes Mellitus, Type 2' - I noticed the T2D entry and the absence of any retinal entry in both fibrate rows, and I treated neither as a signal in either direction. T2D is not DR and I did not reason from it. (2) PROTOCOL TENSION I want on the record: sections 6.1 and 6.5 lean on the AKR1B1 and PRKCB human trial failures, and section 5 leans on the PPARg fluid-retention/macular-edema class association. These ARE DR-specific clinical results. They were supplied to me as scoring priors by the orchestrator in disease-brief.md section 4 and disease-model.md section 4.4, and the task explicitly directed me to use the aldose-reductase and PKCb precedent. I used them as instructed and flagged every use. But they are DR clinical knowledge entering my reasoning, they materially lowered epalrestat's score and shaped section 6.5, and a strict reading of rule 2 would exclude them. The orchestrator should decide whether that is acceptable; I am not in a position to unsee briefing material. (3) The ANGPTL4 argument in sections 2 and 3 draws on retinal vascular biology - PPRE and HRE architecture at the ANGPTL4 locus, cANGPTL4's junctional effects, Muller-cell hypoxic induction - and on general nuclear-receptor pharmacology. No DR trial result informed it. I repeat the scout's disclosure 5 honestly: ANGPTL4's retinal role is studied predominantly in a DR/DME context and the line between 'general retinal physiology' and 'DR-specific literature' is genuinely thin there. I judge it within the allowance; I flag it rather than rely on the judgment silently. (4) The PPARdelta pro-angiogenic argument in section 5 comes from general vascular biology and oxygen-induced-retinopathy work, which is a developmental model, not DR. (5) The transrepression-occupancy argument in section 4 rests on glucocorticoid-receptor dissociated-ligand pharmacology and general nuclear-receptor mechanism - entirely non-DR. (6) NEGATIVE DECISIONS: I did not introduce, consider or score any anti-VEGF agent, intravitreal corticosteroid, or plasma kallikrein inhibitor, because selecting them would require the DR-specific knowledge the protocol forbids. I did list VEGFA/KDR in the section 7 target ranking as a CONTEXT BENCHMARK, scored 3.5 - the score is driven by 'need already served', which is an unmet-needs judgment taken from disease-brief.md section 3 rather than from any trial result I recalled. I flag it because it is the closest this report comes to reasoning from DR therapeutic status. (7) All potency, selectivity, protein-binding, EC50 and elimination-route figures are general pharmacology knowledge, not project data - the relevant project fields are empty. The entire exposure and occupancy argument is therefore knowledge-based reasoning, not a data-derived result. (8) OVERALL: compliant, with disclosure 2 (DR clinical precedents inherited from the briefing documents) as the one place where DR-specific clinical knowledge unavoidably entered, and disclosure 3 (ANGPTL4 retinal literature) as the thinnest line."
}
```

## SCOREBLOCK

*Generated mechanically by the orchestrator from this agent's own §10 JSON. No re-scoring.*

SCORE|Pemafibrate|7.5|moderate|knowledge-based|Target-axis leader. Sub-nanomolar potency with >2000x isoform selectivity gives the cleanest po
SCORE|Fenofibric acid|7.0|moderate|mixed|The pragmatic co-leader. Same row-1 target architecture as pemafibrate with certain hepatic eng
SCORE|Fenofibrate|6.5|moderate|mixed|At the target level this is fenofibric acid plus an obligate ester-hydrolysis step; it contribu
SCORE|Candesartan cilexetil|6.0|moderate|knowledge-based|The highest-druggability target in the entire report and the only non-PPAR candidate with a str
SCORE|Icosapent ethyl|5.5|low|mixed|Scores on the systemic lipid and eicosanoid axes rather than on PPARa. EPA's PPARa engagement i
SCORE|Dimethyl fumarate|5.0|moderate|knowledge-based|A good target carried by a problematic ligand. KEAP1 is covalently tractable with clinical prec
SCORE|Alpha-linolenic acid|4.5|moderate|data-backed|One of only three compounds in all 143 PPARA rows with replicated binding-plus-activation evide
SCORE|Melatonin|4.5|low|mixed|Weak for PPARa - its project rows are cisplatin-protection expression associations with no enga
SCORE|Elafibranor|4.0|moderate|knowledge-based|The PPARdelta co-agonism that is meant to add value is, on this analysis, a liability rather th
SCORE|Minocycline|3.5|low|knowledge-based|The target axis is unassessable for this candidate: minocycline's molecular target for microgli
SCORE|Linoleic acid|3.0|moderate|data-backed|The strongest single body of binding evidence in the entire project dataset - the only compound
SCORE|Linalool|3.0|low|data-backed|Carries the single best-designed mechanistic datum in the project's natural-product set - a PPA
SCORE|Seladelpar|2.5|moderate|knowledge-based|Designated the isoform falsification control, but it is confounded rather than clean. PPARdelta
SCORE|Epalrestat|2.0|moderate|knowledge-based|The weakest target in the set despite good druggability. The disease model records Level-1 NEGA
SCORE|Quercetin|2.0|moderate|data-backed|The project's own data argues against it. Its seven PPARA rows are all expression-protection co
