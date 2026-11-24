# P2 — SAR Analyst: Can the Potency/Access Anti-Correlation Be Broken by Medicinal Chemistry?

**Agent:** SAR Analyst (Phase 2)
**Date:** 2026-10-05
**Run:** BLINDED benchmark run — compliance statement at §11
**Assignment:** extend `agents/p1-chemist.md` §9 (scaffold hopping). Round 1 routed question #4 here.

**Inputs read:** `disease-brief.md` (full) · `round1-synthesis.md` (full) · `agents/p1-chemist.md`
(§0–§4.4, §8, §9, SCOREBLOCK) · `.claude/skills/sar-analyst/SKILL.md` · `disease-model.md` §6.2–6.4 ·
`evidence/ppar-class-drug-properties.tsv` (13 rows, all fields) · `agents/p1-target.md` §4.1–4.3 ·
`agents/p1-admet.md` §9.3.

**Skill adaptation note.** The SAR skill's worked examples are from an Oral Mucositis context. I have
kept its method — matched-pair comparison, pharmacophore extraction, scaffold-hop assessment,
property-optimisation prediction — and applied it to the PPARα arm-I problem. The skill's data-source
paths point at `data/processed/`; per blinding protocol §1 I read the blinded evidence pack instead.

---

## 0. Verdict in one paragraph

**The constraint is not fundamental, it is unexplored — and the reason it is unexplored is that no
prior PPARα indication ever required it.** The AF-2 contact network is an **all-donor cage**: Ser280,
Tyr314, His440 and Tyr464 each donate an O–H or N–H to the ligand. The ligand therefore supplies only
*acceptors*. Geometry asks for a bidentate acceptor pair ~2.2–2.8 Å apart; it does **not** ask for a
formal charge. The charge buys **energy, not legality** — roughly 1.3–1.5 kcal/mol per contact of
charge assistance, which is 10²–10⁴ in affinity, and that is a real physical cost but a bounded one.
Three independent existence proofs say the neutral head is legal: (i) oleoylethanolamide binds and
activates PPARα with **higher ligand efficiency (LE ≈ 0.41) than fenofibric acid (0.29) or pemafibrate
(0.34)** while carrying no charge at all; (ii) the thiazolidinedione head — `[DATA]`, in this
project's own evidence file at pioglitazone MW 356.45 / aLogP 3.16 / PSA 68.29 / HBD 1 / Ro5v 0 /
QED 0.83 — engages the *identical* Ser/Tyr-or-His/His/Tyr quartet in PPARγ from a head whose pKa
(~6.5) leaves 10–25% of the molecule neutral at pH 7.4, inside the brief's BRB window; (iii) linalool
(11 heavy atoms, LE ≈ 0.55) shows the pocket accepts a small neutral ligand. The decisive arithmetic
is **lipophilic ligand efficiency**: every PPARα ligand in this analysis sits at LLE 0.9–3.5, and the
retinal target profile I derive in §7 closes the exposure gap **at LLE 3.5 — exactly what pemafibrate
already demonstrates.** The programme does not need a better LLE than anyone has achieved; it needs
the *same* LLE spent at logD 2.5–3 instead of logD 5.5. That reframes the verdict from "fundamental
barrier" to "a chemotype nobody has built, for a reason that was commercial rather than physical."
Against that: **designed transrepression bias (part c) is a trap** — it cannot raise occupancy, which
is the limiting term, and it would delete the hepatic transactivation limb that is the only *certain*
engagement in the whole run. And the honest strategic conclusion (§9) is that the chemistry is
tractable **and the programme is premature**: a $50k rodent experiment already specified in Round 1 §4
gates a $150–400M NCE programme, and the chemistry argues for running the experiment, not for
starting the programme.

---

## 1. (a) Is the carboxylic acid genuinely required? — mapping the AF-2 cage properly

### 1.1 The topology nobody has stated: the quartet is all-donor

The chemist's §2.1 table lists the four contacts correctly. The feature it does not draw out is the
one that answers the brief's question:

| Residue | Helix | Group | Role in the H-bond | Ligand must supply |
|---|---|---|---|---|
| **Ser280** | H3 | side-chain O–**H** | **donor** | acceptor |
| **Tyr314** | H5 | phenol O–**H** | **donor** | acceptor |
| **His440** | H11 | imidazole Nε2–**H** | **donor** | acceptor |
| **Tyr464** | **H12 / AF-2** | phenol O–**H** | **donor** | acceptor |

> **All four protein partners are hydrogen-bond donors. The ligand head contributes zero donors and
> four acceptor engagements.** A carboxylate satisfies this with two oxygens, each accepting twice.
> The *mechanistic* requirement is therefore: **a bidentate acceptor array, two acceptor atoms
> ~2.2–2.8 Å apart, with the attachment vector pointing out along arm I toward the Y-junction.**
> Formal negative charge is **not** a geometric requirement. It is an **acceptor-strength multiplier.**

This is the precise, falsifiable form of the answer to (a): **the anion is the conventional solution,
not the mechanistic one.** What the anion does is raise the hydrogen-bond basicity of the acceptor
atoms and add a long-range electrostatic term to a cage of polarised donors.

### 1.2 How much is the charge worth? — a quantitative answer via pK_BHX

The right currency is **hydrogen-bond basicity (pK_BHX, Laurence scale)**, not pKa. pK_BHX measures
how good an atom is at accepting an H-bond; ΔG per H-bond scales roughly 1.2–1.4 kcal/mol per
pK_BHX unit in a desolvated pocket.

| Acceptor | approx. pK_BHX | Δ vs carboxylate | Δ per contact |
|---|---|---|---|
| **Carboxylate O⁻** | ~4.3–4.8 | — | baseline |
| Phosphine oxide / phosphonamide P=O | ~3.0–3.5 | −1.0 to −1.6 | −1.3 to −2.1 kcal/mol |
| Amide C=O (secondary/tertiary) | ~2.3–2.6 | −1.8 to −2.3 | −2.3 to −3.1 kcal/mol |
| Sulfoxide S=O | ~2.5 | −1.9 | −2.5 kcal/mol |
| Pyridine-type ring N | ~1.8–1.9 | −2.5 | −3.2 kcal/mol |
| Sulfone / sulfonamide S=O | ~1.3–1.6 | −3.0 | −3.9 kcal/mol |
| Ketone C=O | ~1.1 | −3.3 | −4.3 kcal/mol |
| Alcohol O (as acceptor) | ~1.0–1.5 | −3.1 | −4.0 kcal/mol |
| Ether O | ~1.0 | −3.4 | −4.4 kcal/mol |

Reading this against the cage: a neutral head built from **amide carbonyls** loses roughly
2.3–3.1 kcal/mol per engaged contact. If a neutral head engages two of the four contacts well and two
weakly, total loss lands near **3.5–5.5 kcal/mol**, i.e. **10²–10⁴ in K_d**. That is the chemist's
"100–1,000× weaker than pemafibrate" prediction, now with a derivation behind it, and it is
**corroborated empirically**: OEA (neutral) ~120 nM–3 µM versus pemafibrate (anionic) ~0.1–1 nM — a
10²–10⁴ gap, in exactly the predicted band.

**The cost is real and is a physical limit, not an optimisation gap. It is also affordable** — §7.

### 1.3 The cost is asymmetric across the four contacts — and this is the key SAR finding

The four contacts are **not equally sensitive to losing charge assistance**, and the structural reason
determines what kind of pharmacology a neutral head produces.

- **Ser280 (H3) and Tyr314 (H5)** sit on structurally invariant helices. They are present in the apo
  receptor and contribute to *affinity*. These contacts are made first and are the most tolerant.
- **His440 (H11)** is on the helix that packs against H12. Intermediate.
- **Tyr464 is on H12 itself, and H12 is mobile.** The Tyr464 contact is not a binding contact in the
  ordinary sense — it is the contact that **pays for H12's loss of conformational entropy** when AF-2
  docks into the closed position. It is therefore made **last**, is the most solvent-exposed at the
  moment of formation, and is the single largest term in the open⇌closed free-energy difference.

> **Consequence.** Weakening the head group weakens all four, but only Tyr464's weakening changes the
> *conformational equilibrium*. A 1.5 kcal/mol loss at Tyr464 shifts the closed/open population by
> ~12-fold; 2.5 kcal/mol shifts it ~65-fold. The molecule still binds — arms II/III and the
> Ser280/Tyr314 contacts carry that — but H12 now spends a large fraction of its time open.
>
> **A neutral head therefore converts a full agonist into a partial agonist by construction.
> Efficacy degrades before affinity does.**

The chemist asserted this in §9.1; the mechanism above is why, and the "why" matters because it tells
you the *direction* of the resulting pharmacology rather than just its magnitude. It also connects
directly to part (c): **the very modification that destroys full agonism is the modification that
produces a partial agonist with reduced PPRE-driven transactivation.** The defect and the feature in
parts (a) and (c) are the same molecular event. I return to whether that is good news in §3 — it is
mostly not, and for a reason nobody in Round 1 has raised.

### 1.4 The isoform trap hiding in arm I — PPARα Tyr314 vs PPARγ His323

The brief's §4 demands isoform discipline. Arm I is where it is enforced, and this is decisive for the
head-group choice:

| | PPARα | PPARγ |
|---|---|---|
| H3 contact | Ser280 | Ser289 |
| H5 contact | **Tyr314** | **His323** |
| H11 contact | His440 | His449 |
| H12 contact | Tyr464 | Tyr473 |
| Arm I character | **narrower, more lipophilic** (Tyr314 + Phe273 line the channel) | wider, more polar entrance |

PPARα's arm I is the **smaller and more hydrophobic** of the two. That single fact explains the
empirical SAR the whole field runs on:

- **Small compact acidic heads → PPARα-competent.** Every α-preferring and α/γ-dual drug uses a
  carboxylate: the fibrates, and the glitazars (muraglitazar, tesaglitazar, aleglitazar) are
  α-alkoxy-propanoic acids, **not** thiazolidinediones.
- **Bulky heterocyclic acidic heads → PPARγ-preferring.** Every thiazolidinedione drug is γ-preferring
  (pioglitazone, rosiglitazone, troglitazone, lobeglitazone). The TZD ring is substantially larger in
  footprint than a carboxylate, and PPARα's narrower arm I penalises it.

> **Design rule that falls out, and it is the single most actionable sentence in this section:
> for PPARα, a replacement head must be SMALL. Footprint, not pKa, is the first filter. Shift the
> pKa with the smallest planar heterocycle that will carry two acceptors — which rules the TZD out
> and rules the 1,2,4-oxadiazol-5(4H)-one in.**

### 1.5 The bioisostere table, done quantitatively

The chemist's §4.4(ii) table is correct in direction and incomplete in dimensions. The brief asks for
pKa, logD, protein binding and OATP1B recognition for each. Here is the full matrix. logD values are
estimates from Δ(pH − pKa) applied to a constant fibrate-like body (aLogP 3.8), explicitly
knowledge-based and approximate.

| Head group | pKa | % neutral @ 7.4 | Footprint vs COOH | Acceptor array | Reaches Tyr464? | ΔlogD₇.₄ | PPB direction | OATP1B1/1B3 |
|---|---|---|---|---|---|---|---|---|
| **Carboxylate** (baseline) | 3.0–3.5 | 0.005% | 1.0× | bidentate O⁻/O⁻, 2.24 Å | **yes, strongly** | 0 | 99–99.8% | **strong substrate** |
| **Tetrazole** | 4.5–4.9 | 0.1–0.3% | **~1.5×** (larger, flatter) | 4 ring N, delocalised | partial — bulk fights a narrow arm I | +1.4 to +1.8 | **equal or higher** (anion more lipophilic, charge delocalised) | **still strong** — the sartans are all OATP1B substrates | 
| **Acylsulfonamide** | 3.5–4.5 | 0.03–0.1% | **~2.0×**, extended | SO₂ ×2 + C=O | poor — too extended | +0.5 to +1.4 | **higher** (bigger lipophilic anion) | **strong** |
| **Squaramide (NH,NH)** | 8–10 (as NH acid) | >90% | ~1.3× | **donor pair, not acceptor pair** | **no — wrong polarity** | +3 to +4 | lower | weak |
| **Squaric acid (OH)** | <2 | ~0 | 1.3× | bidentate | yes | −1 | high | strong |
| **Thiazolidine-2,4-dione** | **6.3–6.8** | **10–25%** | **~1.8×** | 2 C=O + N⁻ delocalised | yes **in PPARγ (proven)**; crowded in PPARα | **+2.8 to +3.3** | high (body-driven) | weak–moderate (pioglitazone is mainly CYP2C8) |
| **3-Hydroxyisoxazole** | 5.0–6.0 | 1–3% | ~1.2× | ring N + O⁻ | plausible | +1.9 to +2.6 | lower | reduced |
| **1,2,4-Oxadiazol-5(4H)-one** | **6.0–7.0** | **3–20%** | **~1.2× — nearly isosteric** | C=O + ring N/O, planar | **plausible, best of the acidic set** | **+2.9 to +3.9** | lower | **substantially reduced** |
| **Hydroxamic acid** | ~9 | >97% | ~1.1× | bidentate O,O (chelating) | geometrically yes | +3.9 | low | not a substrate |
| **Neutral amide + β-OH (NAE head)** | n/a | 100% | ~1.3× | amide C=O + OH, ~3.6 Å span | **weakly** (this is the lost contact) | +4.3 | moderate–high | **not a substrate** |
| **gem-Dicarboxamide (malonamide / cyclopropane-1,1-dicarboxamide)** | n/a | 100% | ~1.4× | **2 × C=O, syn-syn ~2.7–3.0 Å** | plausible but weak | +4.3 | moderate | **not a substrate** |
| **Phosphine oxide / phosphonamide P=O** | n/a | 100% | ~1.2× | **single strongest neutral acceptor** | plausible, one contact | +3.5 to +4.3 | **low** | **not a substrate** |

**Five conclusions from this table, in order of importance:**

1. **Almost every classical COOH bioisostere was invented to *preserve* acidity**, because most acid
   drugs need the charge. Tetrazole and acylsulfonamide — the two most used — are **the wrong tools
   for this problem** and make at least one term worse. Tetrazole in particular is a false friend:
   it raises pKa by only ~1.6 units (50× neutral fraction, not enough), **increases** footprint in a
   pocket that is already narrow at PPARα, and **retains full OATP1B recognition**.
2. **Only two acidic heads move pKa into the useful 6–7 window: the oxadiazolone and the TZD.** Of
   those, §1.4 rules the TZD out for PPARα on footprint and isoform grounds. **The
   1,2,4-oxadiazol-5(4H)-one is the correct acidic answer** and I upgrade the chemist's "recommended,
   moderate confidence" to the lead head-group recommendation for an α-selective design.
3. **Squaramide is disqualified on polarity, not on pKa.** It presents two N–H *donors*. The cage
   wants acceptors. This is worth stating because squaramide is a fashionable carboxylate replacement
   and would be a wasted synthetic cycle here.
4. **The phosphine oxide / phosphonamide is the most under-explored option in the table.** P=O is the
   strongest *neutral* H-bond acceptor available to medicinal chemistry (pK_BHX ~3.0–3.5, better than
   an amide by a full unit), it is permanently neutral, it is not an OATP1B recognition element, and
   it **lowers** PPB rather than raising it. Its weakness is that it presents **one** acceptor, not a
   pair, so it can engage at most two of the four donors. Realistic use: as the *distal* acceptor of a
   two-point head (e.g. a β-hydroxy-phosphinamide), not as the whole head. **I have not seen this
   tried at any PPAR and it is cheap to test.**
5. **Going neutral fixes the ionisation term and the OATP1B term. It does NOT fix the free-fraction
   term.** OEA is neutral and still ~99% bound, because fu is driven by **lipophilicity**, and
   lipophilicity is driven by the **pocket**. See §2.3 — this is the constraint that survives
   everything in this table, and it is the one that §7 has to design against.

---

## 2. (b) The N-acylethanolamine precedent — the strongest existence proof, and why it was abandoned

### 2.1 How OEA and PEA engage an all-donor cage with no charge

```
OEA  (oleoylethanolamide)   CCCCCCCC/C=C\CCCCCCCC(=O)NCCO
     MW 325.5 · neutral · logP ~5.9 · PSA 49.3 · HBD 2 · RTB 19 · 23 heavy atoms
PEA  (palmitoylethanolamide)  MW 299.5 · neutral · logP ~5.7 · RTB 17 · 21 heavy atoms
```

The ethanolamide head presents, reading outward from the chain:

```
   C(=O)        amide carbonyl   — ACCEPTOR,  pK_BHX ~2.4
   N–H          amide NH         — donor (spare; can donate to a backbone C=O or to Tyr314's O)
   CH2–CH2
   O–H          primary alcohol  — ACCEPTOR and donor, pK_BHX ~1.3
```

Two acceptors, spanned by a flexible three-bond N–C–C–O linker, giving an **adjustable 3.0–3.8 Å
separation** versus the carboxylate's rigid 2.24 Å. That flexibility is both the reason the head can
find two of the four donors and the reason it cannot find all four simultaneously: satisfying Ser280
and Tyr314 (the H3/H5 pair) costs the torsional arrangement that would reach His440 and Tyr464. **The
contact that gets dropped is the H12 one** — exactly the asymmetry derived in §1.3 — which predicts
that NAEs should behave as **partial agonists at PPARα**, and that is broadly what the reporter
literature shows (strong induction of some PPRE outputs, incomplete maxima in others, assay-dependent
EC50 spanning ~0.1–3 µM).

### 2.2 The ligand-efficiency result — this is the quantitative falsification of "the acid is required"

LE = 1.37 × pEC₅₀ / heavy-atom count. LLE = pEC₅₀ − logP.

| Compound | Head | HAC | pEC₅₀ (approx.) | **LE** | logP | **LLE** |
|---|---|---|---|---|---|---|
| **Linalool** | neutral tert-alcohol | **11** | ~4.4 (40 µM) | **0.55** | 3.3 | **1.1** |
| **Oleoylethanolamide** | **neutral amide-alcohol** | **23** | ~6.9 (120 nM) | **0.41** | 5.9 | **1.0** |
| Pemafibrate | carboxylate | 36 | ~9.0 (1 nM) | 0.34 | 5.55 | **3.45** |
| Elafibranor | carboxylate | 27 | ~7.5 (30 nM) | 0.38 | 5.16 | 2.3 |
| **Fenofibric acid** | carboxylate | 22 | ~4.7 (20 µM) | **0.29** | 3.81 | **0.9** |
| α-Linolenic acid | carboxylate | 20 | ~5.0 (10 µM) | 0.34 | 6.5 | −1.5 |

> **Two results, and both of them matter more than anything else in this report.**
>
> **(1) The neutral head is not paying a ligand-efficiency penalty.** OEA achieves 120 nM with
> 23 heavy atoms and no charge, at **LE 0.41 — higher than pemafibrate (0.34) and far higher than
> fenofibric acid (0.29).** If the carboxylate were mechanistically obligatory, neutral ligands would
> show a systematic LE deficit. They show the opposite. The charge is buying potency *per molecule*,
> not potency *per atom*.
>
> **(2) The entire PPARα field has catastrophic LLE.** Every ligand here sits between −1.5 and 3.5.
> Drug-like practice targets LLE ≥ 5. **LLE is precisely the metric that predicts free fraction and
> tissue distribution**, so "LLE ≤ 3.5 across the whole class" *is* the Round 1 structural finding,
> compressed into one number: potency was bought with lipophilicity, and lipophilicity is what
> albumin site II and OATP1B read.

This reframes the optimisation problem correctly. **The axis that has never been optimised at PPARα
is LLE at low logD.** Everyone optimised pEC₅₀, and since the receptor is a lipid sensor with a
1,300–1,400 Å³ hydrophobic cavity, pEC₅₀ optimisation walks straight up the logP axis.

### 2.3 The constraint that survives going neutral — and it is receptor-intrinsic

**PPARα is a fatty-acid sensor.** Its cavity is large and predominantly hydrophobic because its job is
to read lipid flux. Binding energy in such a pocket comes from burying hydrophobic surface. Therefore:

> **Any potent PPARα ligand is lipophilic; any lipophilic ligand is highly plasma-protein bound.
> This is a property of the receptor, not of the carboxylate, and neutral ligands do not escape it.**
> OEA is neutral, carries no charge, and is still ~99% bound (it rides albumin and lipoproteins
> exactly as a non-esterified fatty acid does).

So the neutral-head hop recovers the **ionisation** term (~4 logs of permeant fraction), the **efflux**
term (MRP/BCRP anion recognition), and the **OATP1B hepatic-sink** term — but it does **not** recover
the **fu** term unless logD comes down with it. **That is why §7's design target leads with logD, not
with potency.** It is the term the chemotype hop alone does not fix.

### 2.4 Why the chemotype was never developed — the honest answer, and it is not "it can't work"

Four reasons, ranked by how much each actually explains:

1. **The field forked to the enzyme instead of the ligand — this is the dominant reason.** Because
   NAEs are hydrolysed in minutes by **FAAH** (and PEA additionally by **NAAA**), the pharmacological
   strategy that won was *raise endogenous NAE tone by inhibiting FAAH*, not *make a stable NAE
   analogue*. Enormous effort went into FAAH inhibitors; essentially none went into rigidified,
   hydrolysis-resistant NAE analogues optimised at PPARα. **The absence of a potent neutral PPARα
   agonist is substantially a historical accident of programme selection, not a demonstrated
   impossibility.** This is the single most important thing I can say about (b), and it is the fact
   that makes the §7 proposals a real opportunity rather than a rediscovery of a known dead end.
2. **Polypharmacology.** OEA also engages **GPR119** (an entire incretin-secretagogue programme was
   built on OEA-like scaffolds), **TRPV1**, and **GPR55**; PEA engages GPR55 and produces "entourage"
   effects at cannabinoid receptors. Any NAE-derived series carries that burden and must be
   counter-screened from day one. For DR specifically, GPR119 agonism is not obviously harmful — but
   TRPV1 agonism in a tissue with sensory innervation and a pain/irritation readout is a real flag.
3. **Flexibility.** RTB 19 at MW 325 is a conformational-entropy disaster and it caps achievable
   affinity: every rotamer frozen on binding costs ~0.4–0.7 kcal/mol. Rigidifying is the obvious fix
   and it is **the cheapest available potency gain in this whole analysis** — see §7, Concept 1.
4. **No commercial pull.** PPARα's indications were dyslipidaemia and, latterly, NASH/PBC — all
   **hepatic**. For a hepatic target, high PPB and OATP1B uptake are *features*. Nobody ever needed a
   PPARα ligand with high free fraction and low hepatic extraction, so nobody built one.

### 2.5 Could it be optimised, and what breaks first?

Yes, and the path is unusually clear because both anchors already exist.

```
  linalool          OEA                    TARGET
  11 HA             23 HA                  22–27 HA
  neutral           neutral                neutral
  RTB 4             RTB 19                 RTB ≤ 7
  logP 3.3          logP 5.9               logD7.4 2.5–3.2
  ~40 µM            ~120 nM–3 µM           0.3–3 µM
  LE 0.55           LE 0.41                LE ≥ 0.40
  LLE 1.1           LLE 1.0                LLE ≥ 3.3
      \____________________  ____________________/
                           \/
          the unoccupied region: rigid, neutral, 300–400 Da
```

**Optimisation sequence, in order:** (1) replace the C18 chain with a rigid 2-ring body — this buys
RTB 19 → 6 and is worth 1–2 logs of affinity from entropy alone; (2) block FAAH/NAAA by
**α,α-gem-dimethyl substitution next to the amide** — the identical Thorpe–Ingold/α-CH-removal trick
the fibrates used on their acid (chemist §1), which is a pleasing symmetry and a well-precedented
FAAH-blocking modification; (3) trim logP from 5.9 toward 3 by replacing aliphatic carbon with
aromatic/heteroaromatic carbon at constant volume; (4) only then optimise potency.

**What breaks first, in the order it will actually break:**

1. **Emax, not EC₅₀.** Per §1.3, the Tyr464 contact is the first casualty of a neutral head. You will
   get compounds that bind at 300 nM and transactivate to 25% of a fibrate maximum, and you will
   spend a year arguing about whether that is a success.
2. **The potency floor imposed by the LE/logP coupling.** Every rigidifying aromatic you add to buy
   affinity adds logP. Holding logD ≤ 3 while climbing from 3 µM to 300 nM is the actual medicinal
   chemistry problem and it is where the programme lives or dies.
3. **FAAH in the target tissue.** Retina expresses FAAH. The metabolic liability sits exactly where
   you want the drug. gem-Dimethyl blockade is likely sufficient but must be demonstrated in retinal
   homogenate, not plasma.
4. **PPARδ cross-reactivity.** Neutral, compact, lipophilic ligands are the chemotype PPARδ likes,
   PPARδ is the most abundant retinal PPAR (Target Analyst §5), is pro-angiogenic, and induces
   ANGPTL4 at least as strongly. **A neutral PPARα programme has a worse isoform-selectivity starting
   point than the acid programme did**, because the carboxylate was itself part of the α-selectivity.
   This is a genuine cost of the hop and nobody has stated it.

---

## 3. (c) Partial agonism and dissociated ligands — designable in principle, a trap in practice

### 3.1 What structurally drives the transactivation/transrepression split

Three distinct, well-characterised structural routes to a dissociated nuclear-receptor ligand:

| Route | Structural mechanism | Precedent | Applicable to PPARα? |
|---|---|---|---|
| **(i) Weaken the H12 contact** | Head group cannot pay for AF-2 closure; H12 samples open states; coactivator groove forms intermittently. Binding retained via arms II/III. | PPARγ partial agonists; the neutral-head case derived in §1.3 | **Yes, and it is unavoidable** once the head is neutral |
| **(ii) Bind the alternate subsite** | Ligand occupies the **β-sheet / Ω-loop** region near the arm II entrance, never entering arm I at all; stabilises the H3/β-sheet region and blocks CDK5-mediated phosphorylation; no H12 engagement whatsoever | **MRL-24, nTZDpa, SR1664** at PPARγ Ser342 — crystallographically established | **Plausible but unmapped at PPARα.** The α equivalent subsite exists topologically; no characterised α chemotype occupies it |
| **(iii) Preserve ligand-dependent SUMOylation while blocking coactivator exchange** | Transrepression runs through ligand-induced receptor SUMOylation → docking on NCoR/SMRT at NF-κB-dependent promoters, preventing signal-dependent corepressor clearance. This requires ligand *binding* and a conformational change, but **not** H12 docking | PPARγ K365 SUMO-dependent transrepression; GR SEGRMs | **Yes mechanistically; unquantified for PPARα** |

So: **yes, the split is structurally designable in principle.** Routes (i) and (iii) are the realistic
ones; route (ii) would be a genuine discovery programme with no α starting point.

### 3.2 The empirical record, stated plainly — and it is bad

The brief asks for honest feasibility. The honest answer is that **this field has a thirty-year record
and zero systemic approvals.**

| Programme | Target | Dissociation demonstrated? | Outcome |
|---|---|---|---|
| Compound A, RU-24858 | GR | Yes, in vitro, repeatedly | Never developed; in vivo dissociation did not hold |
| ZK-216348 | GR | Yes | Discontinued |
| Fosdagrocorat (PF-04171327) | GR | Yes, partial separation in Ph2 RA | Discontinued |
| Mapracorat | GR | Yes | Reached **topical ophthalmic** only |
| Velsecorat (AZD7594) | GR | Yes | **Inhaled** only |
| INT131 (SPPARMγ) | PPARγ | Yes — reduced oedema at matched HbA1c in Ph2 | Not developed further |
| Balaglitazone (SPPARMγ) | PPARγ | Partial | Not approved in major markets |

> **Thirty years, two receptors, a dozen serious programmes, and the only molecules that reached
> patients did so by the local route — topical eye drops and inhalers — i.e. by solving the delivery
> problem the hard way rather than by the dissociation.** For PPARα specifically there is not even
> the in vitro validation set that GR and PPARγ have.

The structural reason the field keeps failing is worth naming, because it is a medicinal-chemistry
problem rather than a biology problem: **there is no structure-based readout for transrepression
bias.** A crystal structure shows you a closed or open H12; it does not show you the conformational
*ensemble* that permits p65 tethering and SUMO-dependent NCoR stabilisation. Every SEGRM/SPPARM
programme was therefore driven by **phenotypic ratio screening** (transactivation reporter ÷ NF-κB
reporter), which gives shallow, cell-line-dependent, assay-format-dependent SAR with no clean potency
metric to optimise against. Design cycles are long and the ratio routinely fails to translate in vivo.

### 3.3 The argument that settles it for THIS programme — and it is not the track record

Even granting that a dissociated PPARα ligand could be built, **it is the wrong thing to build here**,
for two reasons that Round 1's own findings make decisive.

**Reason 1 — bias does not raise occupancy, and occupancy is the limiting term.**

```
occupancy  ∝  fu × C_plasma × Kp,uu / EC50          ← Round 1's central equation
```

Transrepression bias changes **what the receptor does once occupied**. It does not appear anywhere in
that expression. Round 1 §6 and Target Analyst §4.2 already establish that the retinal limb's problem
is that occupancy is ~0.3%, and that transrepression's 10–100× threshold advantage converts
"impossible" to "marginal, not comfortable." **Designing bias does not move that number at all.** If
you want more anti-inflammatory amplitude you need more occupancy — which is a delivery problem, which
is what §7 addresses. **Bias is orthogonal to the actual bottleneck.**

**Reason 2 — and this is the decisive one — designed bias would delete the only certain engagement in
the entire run.**

Round 1 established, with no agent dissenting, that **hepatic PPARα engagement is CERTAIN** (OATP1B
concentrates fibrate anions 10–100× in liver) and that the systemic lipoprotein-lowering limb is the
best-evidenced mechanism available. **That limb is PPRE-driven transactivation**: LPL↑, APOA1/APOA5↑,
APOC3↓, CPT1A/ACOX1/HMGCS2↑, FGF21↑. A transrepression-biased ligand would **ablate it in the liver**,
where the drug definitely arrives, in order to purify a retinal effect in a compartment where the drug
barely arrives at all.

And what would it buy? Protection against ANGPTL4 induction — a risk Round 1 §4 **demoted to a
stage-restricted flag with a cheap plasma-biomarker solution**, and whose surviving route is
*hepatic* ANGPTL4 reaching retinal endothelium from the luminal side.

> **The trade is: spend 8–10 years and an NCE to delete your best-evidenced mechanism, in order to
> manage a demoted risk you can already monitor with a plasma assay.** That is a strictly
> net-negative design objective for this programme, and it holds regardless of whether dissociation
> is technically achievable.

**So my verdict on (c) differs from the chemist's §9.2.** The chemist called the transrepression-biased
ligand "the sharpest idea in this report." The logic is sound and the disease-model mapping is correct,
but it optimises the wrong variable and pays for it with the one limb that works. I would **not** run it.

**The one caveat that keeps it alive at all.** If the Round 1 §4 rodent experiment comes back showing
robust retinal **transactivation** (CPT1A/ACOX1/ANGPTL4 up) — i.e. the low-occupancy model is wrong
and retinal engagement is much better than predicted — then the ANGPTL4 risk becomes live, the
exposure objection collapses, and a bias-engineered ligand becomes a sensible second-generation
objective. **Bias is a contingent follow-on, not a lead strategy.** It should be revisited only on that
specific experimental result.

**A corollary worth banking: you get partial agonism for free anyway.** Per §1.3, any neutral-head
design is a partial agonist by construction, and per Target Analyst §4.3 any low-occupancy fibrate is
a *pharmacokinetically* dissociated ligand. The retina is going to see a dissociated profile whether
or not anyone designs one. **Designing it adds cost and deletes the hepatic limb; not designing it
costs nothing.**

---

## 4. (d) Escaping OATP1B — the overlap is substantial but not complete, and charge is the seam

### 4.1 The two pharmacophores, superimposed

| Recognition element | **OATP1B1/1B3** | **PPARα arm I + arms II/III** | Separable? |
|---|---|---|---|
| **Anionic centre** | **Near-obligatory.** The translocation pathway is positively polarised; the high-affinity substrate set is overwhelmingly anionic (statin hydroxy-acids, fibrates, bile acids, bilirubin, glucuronides, sulfates, repaglinide, valsartan, olmesartan, bosentan) | **Not required** — §1.1 shows the cage needs acceptors, not charge | **YES — this is the seam** |
| **High lipophilicity (logP > 3)** | Affinity rises steeply with logP and buried surface | Required — it is a lipid sensor, 1,300–1,400 Å³ cavity | **NO — fully overlapping** |
| **Elongated topology** (acid head + long hydrophobic body; the "statin shape") | Strongly favoured; affinity tracks molecular length and surface | Arms II/III need *volume*; they can be filled by a **compact branched** body as well as an extended one | **PARTIALLY — real, exploitable** |
| **Planar aromatic surface for π-stacking** | Favoured | Favoured | NO |
| **Absence of a basic centre** | Required (cations break recognition) | Indifferent | **YES, but see §4.3** |
| **MW 400–700** | Favoured | ≥ ~300 needed; 350–450 is ample | **PARTIALLY** |

### 4.2 The three moves, ranked by (OATP1B loss ÷ PPARα loss)

**Move 1 — remove the charge. Best ratio by a wide margin.**
Neutralising the head is **strongly negative** for OATP1B (it removes the single dominant recognition
element) and only **moderately negative** for PPARα (it costs acceptor strength, §1.2, not legality).
Caveat stated honestly: neutrality is not a *guarantee* of escape — digoxin and the taxanes are
neutral OATP1B3 substrates — so the hypothesis must be tested in a transfected-cell uptake assay
early, not assumed. But as a design hypothesis it is the one move with a strongly asymmetric payoff.

**Move 2 — go compact and branched instead of extended. Genuinely separable, and under-used.**
OATP1B affinity tracks molecular *length* and *surface*; PPARα's Y-cavity needs *volume*, and volume
can be delivered by branching from a short central scaffold rather than by extension. Pemafibrate is
the maximally extended version (RTB 13, 36 heavy atoms, two long arms) — **a compact branched ligand
is the topological opposite and is the shape the fibrate field never explored**, because extension was
how it bought potency. Target: ≤ 7 rotatable bonds, longest dimension ≤ ~14 Å, 2–3 rings arranged
around a quaternary or spiro centre rather than in a line.

**Move 3 — add a weak base. Do NOT do this.**
It would break OATP1B recognition decisively. It would also (i) create P-gp substrate liability at the
inner BRB, which is the barrier we are trying to cross, and (ii) create **melanin binding** — melanin
binds cationic and basic drugs preferentially through its polyanionic indolequinone surface, producing
an RPE/choroidal depot that lowers free drug and creates an unpredictable release profile
(disease-model §6.1). Net: trading one efflux problem for two.

> **A correction to the §6.2 rubric worth flagging.** disease-model §6.2 lists "Neutral or weak base
> favoured" under Ionisation. For the **posterior segment specifically**, the weak-base half of that
> is wrong: basicity is favourable for brain penetration but is the principal driver of melanin
> binding in a melanin-rich tissue. **For the retina the correct guidance is "neutral and non-basic."**
> This is a small fix to a rubric that four Round 1 agents have scored against.

### 4.3 Answer to the brief's question

**The overlap is not complete.** It is complete on lipophilicity and aromatic surface, partial on
topology, and **absent on charge** — and charge is the dominant OATP1B term. The separable space
therefore exists and has a specific address: **neutral, non-basic, compact-branched, logD ≤ 3,
MW ≤ 400, ≤ 7 RTB.** That is also, not coincidentally, the §6.2 BRB-permeant window. **Tissue
selectivity can be redirected away from liver, and the redirection is a byproduct of the same change
that fixes the barrier.** One structural move buys both.

---

## 5. (e) Prodrug strategies, assessed concretely — and the structural reason they fail

### 5.1 What actually hydrolyses esters, by tissue

| Enzyme | Where | Retina-enriched? | Usable as a retinal trigger? |
|---|---|---|---|
| **CES1** | liver (dominant), lung macrophages | **No** | No — it is the organ you must survive |
| **CES2** | gut wall, kidney, liver | **No** | No — cleaves on first pass |
| **AADAC** | liver, gut | No | No |
| **BChE / PON1** | plasma (PON1 is HDL-associated) | No | No — cleaves in transit |
| **Alkaline phosphatase** | intestinal brush border, liver, bone, **and RPE basolateral membrane** | Present at RPE but **not enriched** | **No** — a phosphate ester is cleaved at the intestinal brush border before absorption. Phosphate prodrugs are solubility prodrugs, never distribution prodrugs |
| **RPE65** | **RPE-specific isomerohydrolase** | **Yes — the only genuinely retina-specific hydrolase in the eye** | **NO — and this should be killed explicitly, see below** |
| **FAAH** | broad, **including retina** (RPE, ganglion cells, Müller) | Present, not selective | **Partially** — a fatty-acid *amide* promoiety is far more plasma-stable than an ester and is retina-competent. Best available handle |
| **NAAA** | lysosomal; macrophage/microglia | Present in retinal microglia | Partially, same caveat |
| **PLA2G4A (cPLA2α)** | broad, in retina; in the disease model's own target panel | Present, not selective | Yes for *phospholipid* conjugates (§5.3) |

**The RPE65 idea must be explicitly killed, and nobody has done so.** The ADMET agent's §9.3(a) lists
RPE65 as a candidate retina-enriched activator. It is the only truly RPE-specific hydrolase available
— and that is exactly why it is disqualifying. RPE65 is the isomerohydrolase of the **visual cycle**;
it converts all-trans-retinyl ester to 11-cis-retinol. A xenobiotic ester designed as an RPE65
substrate is, by construction, a **competitive inhibitor of the visual cycle**. Pharmacological RPE65
inhibition produces delayed dark adaptation and night blindness — it has been pursued deliberately as
a therapeutic strategy in other retinal diseases precisely because it blunts the visual cycle. **A
chronic oral drug for an asymptomatic early-stage population cannot carry a dose-dependent
night-blindness mechanism.** Remove RPE65 from the option list.

> **The achievable claim is "plasma-stable and retina-competent," never "retina-selective." There is
> no hydrolase with a drug-grade selectivity window for retina over liver.** The chemist said this;
> I confirm it and add that the one apparent exception is actively harmful.

### 5.2 The structural objection that kills the prodrug route — the futile cycle

This is the argument that I think changes the assessment, and neither Round 1 agent made it.

Both the chemist's §4.4 and the ADMET agent's §9.3 frame the problem as **"get it in."** The real
problem has two halves:

```
  get it IN          — a neutral prodrug can plausibly do this
  and KEEP it there  — the liberated carboxylate CANNOT do this
```

The whole premise of masking the acid is that the anion is the problem. But the anion is the problem
**at the barrier in both directions**. The efflux transporters that exclude the acid — **ABCC1/4/5
(MRP) and ABCG2 (BCRP)**, sited on the inner BRB endothelium and the RPE — are organic-anion
exporters. The moment your prodrug is cleaved inside a retinal cell, you have generated, inside the
cell, exactly the species those pumps are built to export. **You have paid for delivery and then
handed the cargo to the pump.**

> **Prodrug + anionic payload + anion-effluxing barrier = a futile cycle.** Steady-state retinal
> concentration is set by (cleavage rate in) ÷ (efflux rate out), and efflux is active and
> concentrative while cleavage is first-order and non-selective. The achievable Kp,uu is improved,
> but it is improved *multiplicatively on a term that is still being actively driven below 1*.

Partial mitigation, stated honestly: intracellular **FABP** binding would buffer the free
concentration available to the pumps. Retina expresses FABP5 and FABP7. But FABP5's nuclear-chaperone
partner is **PPARδ**, not PPARα (FABP1→PPARα is liver-specific), so this would preferentially feed the
wrong isoform — the pro-angiogenic, ANGPTL4-inducing one. The mitigation cuts the wrong way.

**Conclusion for (e): a prodrug cannot rescue an anionic payload at an anion-effluxing barrier. If
you are going to the trouble of making a new chemical entity, make the payload itself neutral (§7)
rather than making a neutral wrapper for an anionic payload.** That single sentence is the strategic
output of part (e).

### 5.3 The carrier route (MFSD2A / LPC) — and a wrong-sign risk nobody has identified

The chemist §4.4(iii) and the ADMET agent §9.3(c) both rate the **LPC–MFSD2A conjugate** as the
highest-value delivery concept, on the correct grounds that carrier-mediated uptake makes passive
permeability irrelevant, that MFSD2A at the inner BRB is genuinely concentrative, and that icosapent
ethyl in the candidate set is an existence proof that the retina imports exogenous lipid this way.

I agree it is the most *structurally specific* idea available. I rate it **lower than they do**, on
three grounds, the third of which is new:

1. **Acyl-chain tolerance is probably narrow and is the whole question.** MFSD2A's physiological cargo
   is lysophosphatidylcholine bearing a long (≥C14), flexible, polyunsaturated acyl chain — LPC-DHA is
   the design substrate. A rigid aryl ketone or biaryl is not a fatty acid. The lipid-binding groove
   of an MFS-fold transporter is shape-complementary to an extended flexible chain. **Probability the
   transporter accepts a fibrate-like acyl group: I would put it below 30%, and it is a cheap
   experiment to find out.**
2. **Plasma lability.** Free LPC has a plasma half-life of minutes, acted on by LCAT, lysophospholipases
   and autotaxin. A conjugate must out-run all three.
3. **The autotaxin→LPA wrong-sign risk — new, and specific to this disease.** Autotaxin (ENPP2) is the
   plasma lysophospholipase D that converts **LPC → lysophosphatidic acid (LPA)**. LPA is a potent
   pro-permeability, pro-inflammatory, pro-fibrotic lipid mediator acting through LPAR1–6 on
   endothelium. So a circulating LPC-conjugated PPARα agonist is a **substrate for conversion into an
   LPA analogue** — i.e. into a pro-permeability agonist — **in a disease whose defining lesion is
   vascular permeability.** This is not a theoretical tox concern; it is a mechanism-level wrong-sign
   risk of exactly the kind the brief demands be surfaced for ANGPTL4, and it sits on the delivery
   vehicle rather than on the drug. **It must be measured (plasma ATX turnover of the conjugate, and
   LPAR agonism of the product) before any medicinal chemistry is committed.**

**Net on (e): the carrier route is the best of the delivery-vehicle ideas and it is still a
low-probability, high-information experiment. Run the two cheap assays (MFSD2A uptake of a conjugate;
ATX turnover) before anything else. Do not build a programme on it.**

---

## 6. Pharmacophore model — the minimal requirement, restated for a neutral ligand

```
═══════════════════════════════════════════════════════════
PPARα PHARMACOPHORE — minimal feature set, charge-agnostic
═══════════════════════════════════════════════════════════

  F1  BIDENTATE ACCEPTOR PAIR         (arm I head)
        two acceptor heteroatoms, 2.2–3.2 Å apart
        combined pK_BHX ≥ ~4.5 across the pair
        attachment vector ~120–140° from the acceptor midpoint
        → must reach Tyr464 (H12) for FULL agonism
        → reaching only Ser280/Tyr314 gives a PARTIAL agonist

  F2  SMALL HEAD FOOTPRINT            (α vs γ discrimination)
        ≤ ~1.3× carboxylate van der Waals footprint
        PPARα arm I is narrower than PPARγ's (Tyr314 + Phe273)
        → rules OUT thiazolidinedione, acylsulfonamide, tetrazole
        → rules IN  carboxylate, oxadiazolone, hydroxyisoxazole,
                    compact neutral dicarbonyl / amide-alcohol

  F3  HYDROPHOBIC LINKER              (channel between arm I and the Y-junction)
        2–4 atoms, preferably with a quaternary or stereogenic α-centre
        (Thorpe–Ingold pre-organisation + β-oxidation blockade)

  F4  AROMATIC / HYDROPHOBIC BODY     (arms II and III)
        200–350 Å³ of buried hydrophobic volume
        ** deliverable by BRANCHING from a short core, not only by EXTENSION **
        branching = equal PPARα volume at lower OATP1B recognition

  F5  (optional) DISTAL POLAR VECTOR  (arm III / solvent channel)
        tolerated; the place to park polarity to pull logD down
        without touching arm I  ← the LLE lever nobody pulled

ANTI-FEATURES for this indication:
  ✗ permanent anion           → OATP1B + MRP/BCRP + albumin site II
  ✗ basic centre              → P-gp + melanin depot
  ✗ chromophore > 320 nm      → illuminated target organ (benzophenone, polyene,
                                 tetracycline, rhodanine)
  ✗ Michael acceptor / electrophile → chronic dosing
  ✗ extended linear topology  → OATP1B recognition
  ✗ RTB > 8                   → permeability + entropy
═══════════════════════════════════════════════════════════
```

**Feature F5 is the one the field never used.** In a fatty-acid-sensing receptor with a solvent
channel at the arm III exit, polarity parked on the distal vector lowers logD without touching the
binding energetics. Pemafibrate has a methoxyphenoxypropyl arm there — lipophilic. **Every PPARα
programme put lipophilicity where it could have put polarity, because no indication ever asked for
free fraction.** This is where the 1–2 logs of LLE improvement in §7 come from, and it is a mundane,
ordinary medicinal chemistry move. That is the point: **the required chemistry is not exotic.**

---

## 7. (f) Design proposals — three concepts, with what kills each

**Shared design window** (disease-model §6.2 as corrected in §4.2 above, plus chronic-dosing and
illuminated-organ constraints): MW ≤ 420 · logD₇.₄ 2.3–3.3 · TPSA 55–85 Å² · HBD ≤ 2 · RTB ≤ 7 ·
**neutral and non-basic at pH 7.4** · not a P-gp/BCRP substrate · PPB ≤ 95% · no absorbance > 320 nm ·
no electrophile · ≥ 100× selective over PPARγ **and over PPARδ**.

### 7.1 The arithmetic the design must satisfy — and it closes

```
TARGET PROFILE                        FENOFIBRIC ACID (for comparison)
  EC50 (free-drug corrected)  500 nM    ~20 µM
  logD7.4                     2.8       ~ −0.5 to +0.5 (anion)
  fu (plasma)                 0.10      0.01
  Kp,uu (retina)              0.5       ≤ 0.1 (anion, MRP/BCRP, no uptake carrier)
  dose                        100 mg    145 mg
  total plasma Cmax           5–10 µM   30–45 µM
  ────────────────────────────────────  ──────────────────────────
  free plasma                 0.5–1.0 µM   0.1–0.4 µM
  free retinal interstitium   0.25–0.5 µM  0.01–0.04 µM
  free retinal / EC50         0.5–1.0      0.0005–0.002
  FRACTIONAL OCCUPANCY        ~33–50%      ~0.05–0.2%
```

**A ~300–1,000× improvement in retinal fractional occupancy.** Decomposed: ~40× from potency, ~10×
from free fraction, ~5–50× from Kp,uu. Note that **the potency term is the smallest of the three** —
the opposite of where the entire field spent its effort.

**Is the required LLE achievable?** LLE = pEC₅₀ − logD = 6.3 − 2.8 = **3.5.**

> **Pemafibrate already demonstrates LLE 3.45.** The design does not require a better LLE than anyone
> has achieved at PPARα. It requires **the same LLE spent at the low-logD end of the line.** That is
> the single most important sentence in this report, and it is why my verdict in §9 is "tractable"
> rather than "fundamental."

### 7.2 Concept A — "OXA-COMPACT": oxadiazolone head on a compact branched body

*The pKa-shift route, corrected for PPARα's narrow arm I.*

| | |
|---|---|
| **Head** | **1,2,4-oxadiazol-5(4H)-one**, pKa 6.0–7.0 → **3–20% neutral at pH 7.4** (~10³× fenofibric acid's permeant fraction), footprint only ~1.2× a carboxylate so it fits PPARα arm I where a TZD would not (§1.4) |
| **Linker** | α,α-gem-dimethyl or α-spirocyclopropyl ether — Thorpe–Ingold pre-organisation + β-oxidation blockade + minimal acyl-glucuronide migration (the α,α-disubstitution lesson from chemist §1) |
| **Body** | **branched, not extended**: a 2-aryl-oxazole or 2-aryl-imidazole core with a short *meta* substituent, total 2 rings, longest dimension ≤ 14 Å. Deliberately NOT pemafibrate's linear two-arm topology (§4.2 Move 2) |
| **Arm III vector** | small polar group (morpholine-free: a methylsulfone, an oxetane, or a primary amide) to pull logD down without touching arm I — feature F5 |
| **Predicted** | MW 365–400 · logD₇.₄ **2.6–3.2** · TPSA 78–92 Å² · HBD 1 · RTB 5–6 · ~85–95% ionised but with a 3–20% neutral reservoir · aromatic rings 2 |
| **Expected potency** | **EC₅₀ 50–500 nM**, Emax 60–90% (the head is still anionic in the bound state, so Tyr464 is largely preserved — this is the concept with the best efficacy retention) |
| **Precedent strength** | **Highest.** This is the smallest change from a validated chemotype; existing fibrate SAR transfers directly |

**What most likely kills it:**
1. **TPSA creep.** The oxadiazolone is more polar than a carboxylic acid in its neutral form; add an
   F5 polar vector and you are at 90 Å², the edge of the window. You will be fighting TPSA and logD
   in opposite directions all programme.
2. **The neutral reservoir may not behave as a reservoir.** The 3–20% figure assumes rapid
   equilibration across the membrane at the unstirred layer. If membrane partitioning of the neutral
   species is slow relative to transit time, the pH-partition advantage under-delivers. This is a
   known failure mode of pKa-shift strategies and it is measured, not predicted, in a PAMPA/Caco-2
   pH-gradient assay — **the first experiment to run.**
3. **It is still partly an anion**, so residual OATP1B and MRP recognition persists at 80–95% of the
   population. This concept **improves** both terms; it does not eliminate them. Expect hepatic
   extraction to remain substantial.
4. Metabolic lability of the oxadiazolone ring (reductive ring-opening) is a known class issue and
   must be checked in hepatocytes early.

### 7.3 Concept B — "NAE-LOCK": rigidified neutral N-acylethanolamine mimetic

*The chemist's §9.3 idea, made structurally concrete and with the head group specified.*

| | |
|---|---|
| **Head, option B1** | **4,4-dimethyl-oxazolidin-2-one** — presents C=O (acceptor) + ring O (acceptor) at a locked ~2.3 Å spacing, i.e. **the carboxylate's geometry with no charge**; the gem-dimethyl blocks hydrolytic reopening |
| **Head, option B2** | **cyclopropane-1,1-dicarboxamide** — two amide C=O locked syn-syn at ~2.7–3.0 Å by the cyclopropane; a precedented, metabolically robust motif (it is cabozantinib's central linker), and the quaternary carbon reproduces the fibrates' β-oxidation blockade |
| **Head, option B3** | **α,α-dimethyl-N-(2-hydroxyethyl)amide** — the literal OEA head with FAAH blockade installed; simplest synthesis, weakest acceptors |
| **Body** | 2-ring rigid biaryl ether or 2-arylbenzoxazole. **Explicitly NOT fenofibrate's benzophenone** — a diaryl ketone is a type-II photosensitiser with absorbance near 340 nm, which §6's anti-feature list forbids in a continuously illuminated organ. This is a constraint the chemist raised and then partly violated by proposing to reuse the fibrate body |
| **Predicted** | MW 340–395 · logD₇.₄ **2.5–3.4 (neutral — same as logP)** · TPSA 60–85 Å² · HBD 1–2 · RTB 5–7 · **permanently neutral** |
| **Expected potency** | **EC₅₀ 0.3–5 µM**, **Emax 25–55% (partial agonist by construction, §1.3)** |
| **Precedent strength** | Moderate — anchored on OEA's demonstrated LE 0.41, but no rigidified-NAE SAR series exists to borrow from |

**What most likely kills it, in the order it will happen:**
1. **Emax, not EC₅₀.** The neutral head loses Tyr464 first (§1.3). You will get a 400 nM binder that
   transactivates to 30% of fibrate maximum and spend a year deciding whether that is a drug. For the
   *transrepression* limb that is acceptable or even good; for the lipid limb it is not.
2. **PPARδ selectivity.** Compact neutral lipophilic ligands are δ's preferred chemotype, δ is the
   most abundant retinal PPAR, is pro-angiogenic, and induces ANGPTL4 at least as strongly (Target
   Analyst §5). **The carboxylate was itself part of PPARα's selectivity; removing it degrades the
   isoform margin.** Counter-screening against δ must be in the primary cascade, not the secondary.
3. **FAAH in the target tissue.** gem-Dimethyl blockade must be demonstrated in *retinal* homogenate.
4. **HBD 2 and TPSA.** Two donors in the head plus a polar body puts you at the permeability limit.
   B1 (oxazolidinone, HBD 1) is the better head on this axis than B2 or B3.
5. **The logP/potency coupling.** Every rigidifying aryl added to climb from 3 µM to 300 nM adds
   ~0.4 logP. Holding logD ≤ 3.3 through that climb is the programme's central difficulty.

### 7.4 Concept C — "LINALOOL-GROW": fragment growth from the access end

*The idea nobody proposed, and on ligand-efficiency grounds it is the most rational starting point.*

The entire field started from the potency end (a strong acid, LE 0.29) and optimised toward
lipophilicity, destroying access. **Start from the access end instead.** Linalool is, on the project's
own evidence, a PPARα-engaging fragment — the blinded data records **PPARA-dependent SLC27A4
induction, abolished in a PPARA mutant**, which is the only genetic-dependency engagement evidence in
the entire candidate set. And:

```
linalool   C10H18O · 11 heavy atoms · neutral · logP 3.3 · TPSA 20.2 · RTB 4 · QED ~0.50
           EC50 ~40 µM → pEC50 4.4 → LE = 1.37 × 4.4 / 11 = 0.55
           §6.2 rubric: 7/8 (chemist §8)
```

**LE 0.55 is the highest in the candidate set** — 1.9× fenofibric acid's. That is the classic signature
of an unexploited fragment hit. Growing from 11 to 24 heavy atoms at a conservative 0.30 LE/heavy-atom
increment (well below the fragment's own LE, i.e. assuming efficiency decay) lands at:

```
pEC50 = (0.55 × 11 + 0.30 × 13) / 1.37 × (1.37/1)  →  pEC50 ≈ 6.9  (≈ 130 nM)
MW ≈ 330 · logD ≈ 3.0 if growth is aromatic/polar-balanced · RTB ≈ 6 · neutral
```

— which is **the §7.1 target profile, reached from a direction nobody has tried.** The growth vectors
are the tertiary alcohol (convert to the F1 bidentate head: an oxazolidinone, a dicarboxamide, or
retain the OH and add a proximal acceptor) and the isoprenyl terminus (replace with a rigid aryl to
fill arm II).

**What most likely kills it:**
1. **The fragment may not be real.** Linalool's PPARα evidence is **single-source** (disease-brief
   §8, B3). Monoterpenoid alcohols are notorious non-specific membrane perturbants and detergent-like
   assay artifacts at tens of µM. **The 40 µM could be noise, in which case LE 0.55 is a fiction.**
   This must be confirmed — an orthogonal direct-binding assay (SPR or ITC against purified LBD, plus
   the GW 6471 antagonist-reversal control the project's own data applies to dibutyl phthalate) is a
   two-week, low-cost gate and should run first.
2. **LE inflation at low heavy-atom count.** LE systematically overstates very small fragments; the
   metric's growth projection is optimistic by construction. Treat the pEC₅₀ 6.9 projection as a
   ceiling, not an expectation.
3. **Selectivity from a terpenoid start is unknown and probably poor** — small neutral lipophiles hit
   all three PPARs plus a long tail of lipid-binding proteins.
4. **No IP position** on a natural product fragment; the composition-of-matter claim has to come
   entirely from the grown molecule.

### 7.5 Ranking the three

| | Concept A (OXA-COMPACT) | Concept B (NAE-LOCK) | Concept C (LINALOOL-GROW) |
|---|---|---|---|
| Confidence in the chemistry | **High** | Moderate | Low–moderate |
| Distance from validated SAR | Smallest | Medium | Largest |
| Expected potency | Best (50–500 nM) | 0.3–5 µM | Unknown |
| Expected Emax | **Best (60–90%)** | 25–55% | Unknown |
| Fixes OATP1B? | Partially | **Fully** | **Fully** |
| Fixes fu? | Partially | Only if logD held ≤ 3.3 | **Best — starts low** |
| Isoform risk | Low (acidic heads are α-competent) | **High (δ)** | **High (all three)** |
| Cost to first answer | Lowest | Medium | Lowest (it is an assay, not a synthesis) |

**Recommended sequencing: run C's validation assay first (two weeks, trivial cost, and it either
creates a fragment programme or closes a Round 1 evidence gap), start A as the lead series, hold B as
the backup for the case where A's residual anionic character proves to be the blocking term.**

---

## 8. Matched-pair summary — what the series actually taught

| Pair | Transformation | ΔlogP | ΔRTB | ΔQED | Δ potency | Δ retinal access | SAR lesson |
|---|---|---|---|---|---|---|---|
| Fenofibric acid → Pemafibrate | add 2nd arm, α-mono-alkyl stereocentre | **+1.74** `[DATA]` | **+8** `[DATA]` | **−0.61** `[DATA]` | **~10⁴–10⁵ ↑** | **↓↓** | Potency and access are anti-correlated; the move that fills arms II/III is the move albumin and OATP1B read |
| Fenofibric acid → Fenofibrate | esterify | +0.87 `[DATA]` | +1 | −0.30 `[DATA]` | → 0 (inert) | → 0 (cleaved presystemically) | A neutral wrapper on an anionic payload solves formulation, never distribution |
| Fenofibric acid → Elafibranor | add chalcone + thioether | +1.35 `[DATA]` | +2 | −0.44 `[DATA]` | ~10³ ↑ | ↓ | Same trade, plus a chronic-dosing electrophile |
| **Carboxylate → TZD head** (fenofibric acid vs pioglitazone) | **Δ pKa 3.1 → 6.5** | −0.65 `[DATA]` | +2 | **−0.02** `[DATA]` | (isoform-switched) | **↑↑ (~10³ permeant fraction)** | **A PPAR-arm-I head CAN sit in the BRB window at QED 0.83, Ro5v 0 — data-backed in this project's own file** |
| Linoleic acid → OEA | acid → ethanolamide | −1.1 | +5 | ~+0.1 | ~10²–10³ ↑ | ↑↑ (neutral) | **The one transformation in the whole analysis that improves potency AND access simultaneously** |
| Linalool → (target) | grow 11 → 24 heavy atoms | +0 if balanced | +2 | +0.2 | ~10²·⁵ ↑ projected | ≈ flat | Growth from the access end preserves what potency-first optimisation destroyed |

> **The fifth row is the headline.** Across this entire analysis, **acid → neutral amide is the only
> single transformation that moves potency and access in the same direction.** Every other move in
> the series traded one for the other. That is the structural case for the hop, in one line.

---

## 9. (g) Honest verdict

### 9.1 Is the constraint fundamental?

**No — and I can say why in three independent ways.**

1. **Topologically.** The AF-2 cage is all-donor (§1.1). It requires a bidentate acceptor array, not a
   charge. The charge is an acceptor-strength multiplier worth 10²–10⁴ in affinity — real, bounded,
   and affordable (§1.2).
2. **Empirically.** Three existence proofs, each of a different kind: **OEA** (neutral, binds, LE 0.41
   — *higher* than either fibrate, which is the quantitative falsification of "the acid is required");
   **the thiazolidinedione head** (`[DATA]`, pioglitazone MW 356.45 / aLogP 3.16 / PSA 68.29 / HBD 1 /
   RTB 7 / Ro5v 0 / **QED 0.83** — a PPAR arm-I-engaging head on an approved oral drug sitting inside
   the BRB window); **linalool** (neutral, LE 0.55, 7/8 on the rubric).
3. **Arithmetically.** The §7.1 target profile closes the retinal exposure gap at **LLE 3.5**, which
   **pemafibrate already achieves**. The programme does not need to beat the field's demonstrated
   efficiency ceiling. It needs to spend the same budget at logD 2.8 instead of logD 5.5.

**Why it has never been done is not mysterious and is not physical: PPARα's indications were all
hepatic, and for a hepatic target high PPB and OATP1B uptake are features. Nobody ever needed a PPARα
ligand with a high free fraction.** The chemical space is empty because it was never commercially
interesting, not because it is forbidden.

### 9.2 What would it take?

| Phase | Work | Time | Scale |
|---|---|---|---|
| **Gate 0 — the experiment that must come first** | Round 1 §4's chronic oral fibrate in a diabetic rodent: retinal CPT1A/ACOX1/ANGPTL4 (transactivation) vs ICAM1/TNF/leukostasis (transrepression) | **6–9 months** | **~$50–150k** |
| Gate 0b (parallel, cheap) | Confirm linalool's PPARα binding by SPR/ITC + GW 6471 reversal; measure MFSD2A uptake of a model conjugate; measure ATX turnover of an LPC conjugate | 2–4 months | <$100k |
| Hit finding | Build the §6 pharmacophore; virtual + fragment screen against the neutral/compact window; synthesise Concept A first wave (~150 compounds) | 12–18 months | $3–6M |
| Lead optimisation | The real work: hold logD ≤ 3.3 while climbing to ≤ 500 nM, at ≥ 100× over PPARγ **and** PPARδ. Assay cascade must be **free-drug-corrected EC₅₀, measured fu, measured Kp,uu in a species with a comparable BRB** — none of which is standard, all of which must be built | 24–36 months | $15–30M |
| Preclinical → Ph1 | Standard, plus ocular tox in a pigmented species (melanin) and a phototoxicity package | 18–24 months | $25–50M |
| Ph2a with a retinal biomarker | Endpoint is the unresolved strategic risk — early-DR regulatory endpoints are not established (disease-model §6.4) | 24–36 months | $60–200M+ |
| **Total to a Ph2a retinal readout** | | **7–10 years** | **$150–400M** |

**Probability of technical success to a Ph2a retinal biomarker readout: I would put it at 15–25%**,
conditional on Gate 0 reading positive. The dominant risks in order are: (i) Gate 0 reads negative and
there is no target; (ii) Emax collapses with the neutral head and the partial agonist does nothing
measurable; (iii) PPARδ selectivity cannot be achieved from a neutral compact chemotype; (iv) the
regulatory endpoint for early DR never materialises, which is a programme risk larger than any of the
chemistry risks.

### 9.3 The verdict, stated as the brief asked

> **Tractable, and premature.**
>
> The medicinal chemistry is a real, ordinary, buildable programme — not a violation of physics and
> not even an exotic one. The required moves (shrink the head, shift the pKa or neutralise it, branch
> instead of extend, park polarity on the distal vector) are standard. What makes it a hard programme
> is not any single step but that **no assay cascade exists for the thing being optimised** — nobody
> has ever run a PPARα programme against free-drug retinal exposure, so the metrics, the models and
> the translation are all unbuilt.
>
> **And it should not start yet.** A ~$100k rodent experiment, already specified in Round 1 §4,
> determines whether there is a retinal target at all. Spending $300M and nine years before running
> it would be indefensible. **The chemistry's contribution to the strategic question is this: it does
> not argue against running the experiment, and it says that if the experiment reads positive, the
> molecule is designable.** That converts Round 1's "no fibrate can test the retinal limb" from a
> terminal finding into a sequencing instruction.
>
> **Near-term, the practical conclusion is close to the negative answer the orchestrator anticipated,
> for a different reason.** The systemic lipoprotein-lowering mechanism is deliverable *today* with a
> generic acid whose hepatic engagement is certain. The retinal mechanism needs a decade and an NCE.
> **Run them sequentially, not in parallel: commit to the systemic mechanism now, run Gate 0 alongside
> it for ~$100k, and let its result decide whether the retinal programme is ever started.**

### 9.4 Three corrections I am making to prior reports

1. **To the chemist's §9.2 (transrepression-biased ligand = "the sharpest idea in this report").**
   The logic is right and the objective is wrong. Designed bias cannot raise occupancy, which is the
   limiting term, and it would ablate the hepatic transactivation limb — the only *certain* engagement
   in the entire run — to manage a risk Round 1 already demoted and already has a plasma biomarker
   for. **Net-negative. Demote to a contingent follow-on.** (§3.3)
2. **To the chemist's §4.4 and the ADMET agent's §9.3(a) on prodrugs.** The framing is "get it in";
   the actual problem is "get it in and keep it there." A liberated carboxylate inside a retinal cell
   is the exact substrate the MRP/BCRP exporters at that barrier are built for — **a futile cycle**.
   And **RPE65, named as a candidate retina-enriched activator, must be struck from the list**: a
   prodrug designed as its substrate is a competitive visual-cycle inhibitor, i.e. a dose-dependent
   night-blindness mechanism in an asymptomatic population. (§5.1–5.2)
3. **To the LPC/MFSD2A delivery concept (chemist §4.4(iii), ADMET §9.3(c), both rating it highest).**
   A circulating LPC conjugate is an **autotaxin substrate**, and autotaxin converts LPC into **LPA** —
   a pro-permeability, pro-inflammatory endothelial mediator — **in a disease defined by vascular
   permeability.** A wrong-sign risk on the delivery vehicle, of the same class as the ANGPTL4 risk
   the brief requires be surfaced. Measurable cheaply; must be measured before commitment. (§5.3)

And one correction to the shared rubric: **disease-model §6.2's "neutral or weak base favoured" is
half-wrong for the posterior segment.** Basicity drives melanin binding in a melanin-rich tissue. For
the retina the guidance should read **"neutral and non-basic."** (§4.2)

---

## 10. Scoring — axis: structural optimisability

**What I am scoring.** Not efficacy, not exposure, not clinical viability — **how much headroom this
chemotype has left for the problem defined in this run.** A compound can be the best molecule in the
set and score low here if its series is exhausted (pemafibrate), or be pharmacologically worthless and
score high if its chemotype has an unexploited direction (linalool, linoleic acid). This axis is
deliberately orthogonal to the other six and **must not be averaged with them** — Round 1 §7 is
explicit on that and this axis would mislead worst of all if averaged.

| # | Compound | Score | Headroom assessment |
|---|---|---|---|
| 1 | **Linalool** | **7** | Highest LE in the set (0.55, 11 heavy atoms), 7/8 on the BRB rubric, neutral, and the only genetic-dependency engagement evidence in the project data. A fragment hit with a 13-heavy-atom growth vector straight into the §7.1 target window. Gated on confirming the binding is real. |
| 2 | **Melatonin** | **6** | Structurally an N-acyl-aminoethyl indole — a rigid, neutral, small N-acylamine with **8/8** on the rubric and QED 0.84: the Concept-B head and physicochemistry already assembled, lacking only arms II/III bulk. Excellent template, no PPARα SAR to grow along. |
| 3 | **Linoleic acid** | **5** | Worthless as a compound (endogenous at saturating levels, RTB 14, logP ~7, peroxidisable, n-6 wrong-sign). But its chemotype is one amidation away from the NAE head — **the only transformation in this analysis that improves potency and access together**. The chemotype has the headroom even though the molecule has none. |
| 4 | **Fenofibric acid** | **4** | The acid series is exhausted on potency, but one cheap unexplored move remains: swap the head for an oxadiazolone on the same validated body (~10³ permeant fraction) and strip the benzophenone chromophore. Best-built molecule in the class (QED 0.85) and therefore the best body to start from. |
| 5 | **Alpha-linolenic acid** | **4** | As linoleic acid, one notch down: more peroxidisable, sub-1% DHA yield, and dominated by icosapent ethyl within its own chemotype. |
| 6 | **Icosapent ethyl** | **4** | The PUFA chemotype's one distinctive asset is the MFSD2A/LPC carrier route — genuinely differentiated, and now carrying a named wrong-sign risk (autotaxin→LPA, §5.3). Five bis-allylic sites cannot be designed out without leaving the chemotype. |
| 7 | **Elafibranor** | **3** | The enone is removable (at the cost of the NRF2 limb and some potency) and the head is addressable, but the molecule starts at logP 5.16 / Ro5v 1 and its α/δ dual profile points at the pro-angiogenic, ANGPTL4-inducing isoform. Optimising it means optimising away from itself. |
| 8 | **Dimethyl fumarate** | **3** | The reactive Michael acceptor *is* the mechanism, so the principal liability is not separable from the activity. Successor chemistry (diroximel, monomethyl fumarate) optimised tolerability, not mechanism — which is the available headroom and it is small. |
| 9 | **Candesartan cilexetil** | **3** | Among the most thoroughly optimised chemotypes in medicine; essentially no headroom left. Partly moot — a cell-surface GPCR needs no membrane crossing, so this report's central constraint does not bite. |
| 10 | **Ezetimibe** | **3** | Already hard-optimised out of an ACAT programme, and its mechanism is topologically immune to the access problem (it acts at the intestinal brush border; the circulating glucuronide recycles back to the lumen). Little headroom and little need for any. |
| 11 | **Fenofibrate** | **2** | Its only optimisable axis is the prodrug axis, and §5 closes it: no retina-enriched hydrolase exists, RPE65 is disqualifying, and a liberated anion is re-exported by the barrier's own pumps. A neutral wrapper cannot rescue an anionic payload. |
| 12 | **Pemafibrate** | **2** | The terminal molecule of its series. QED 0.24, RTB 13, logP 5.55, 1/8 on the rubric `[DATA]`. Every move that would improve retinal access gives back the potency that is its entire justification. Lowest headroom in the set for this goal. |
| 13 | **Seladelpar** | **2** | A δ chemotype by structure, so optimising it optimises the wrong isoform; additionally carries the most acyl-migration-prone glucuronide head in the set. |
| 14 | **Epalrestat** | **2** | The rhodanine is replaceable and was replaced by later ARIs — but the target carries negative human clinical validation, so the headroom leads nowhere. Also a photoisomerising chromophore in an illuminated organ. |
| 15 | **Minocycline** | **2** | A 70-year-old scaffold explored to exhaustion; the chelating, melanin-binding, photo-oxidising chromophore is intrinsic to the tetracycline core and cannot be removed while remaining a tetracycline. |
| 16 | **Quercetin** | **1** | Catechol PAINS on six independent mechanisms, direction-incoherent at PPARα (antagonises GW 7647), aglycone absent from circulation. Optimising a frequent hitter optimises assay artifact. Lowest headroom, highest confidence. |

**Falsification conditions for the two scores ≥ 7** (per disease-brief §10):
- **Linalool at 7** is falsified if an orthogonal direct-binding assay (SPR/ITC on purified PPARα LBD,
  with GW 6471 antagonist reversal) fails to reproduce engagement at ≤ 100 µM, or if the effect proves
  detergent-like/non-saturable. The LE 0.55 that drives the score is entirely contingent on the 40 µM
  figure being a real K_d. This is a two-week, sub-$50k experiment and it should be run.

---

## 11. Blinding compliance statement

**Files read.** `disease-brief.md` (full); `round1-synthesis.md` (full); `agents/p1-chemist.md`
(§0–§4.4, §5 header, §8, §9, §10 header, SCOREBLOCK); `.claude/skills/sar-analyst/SKILL.md` (full);
`disease-model.md` §6.2–6.4; `evidence/ppar-class-drug-properties.tsv` (all 13 rows, all columns);
`agents/p1-target.md` §4.1–4.3 and grep-level excerpts; `agents/p1-admet.md` §9.3 and grep-level
excerpts; directory listings of the run tree and `evidence/`.

**Files NOT read, by protocol §1.** `data/processed/chembl_approved_drugs.csv`; anything under
`data/holdout/`; any `answer-key*` file. I did not use git history, git objects, or any other route to
recover redacted values, and I did not attempt to infer which rows were redacted. I did not open the
unblinded processed directory at any point; every descriptor I cite as `[DATA]` came from
`evidence/ppar-class-drug-properties.tsv` inside the run tree.

**Knowledge used, and its basis.** This analysis is almost entirely **general medicinal chemistry,
structural biology and physical organic chemistry** — PPAR LBD architecture and residue numbering,
hydrogen-bond basicity scales, carboxylate bioisostere pKa values, transporter pharmacophores,
esterase and amidase tissue distribution, ligand-efficiency metrics, and the development history of
dissociated nuclear-receptor ligands. All of that is permitted by protocol §3.

**Honest disclosures, including negative decisions.**

1. **I used the clinical development history of the SEGRM and SPPARMγ fields** (compound A, RU-24858,
   ZK-216348, fosdagrocorat, mapracorat, velsecorat, INT131, balaglitazone) to argue in §3.2 that
   designed dissociation has a thirty-year record with no systemic approval. **None of these
   programmes is a DR or DME programme** — they are rheumatology, respiratory, dermatology and
   diabetes programmes — so this is non-DR clinical knowledge and permitted. Mapracorat's topical
   *ophthalmic* development is the closest call in the report; I used it only as evidence about the
   **route** by which dissociated ligands reached patients, not as evidence about any retinal disease,
   and no score depends on it.
2. **I used the PPARγ class's fluid-retention and macular-oedema association** in §1.4 and §7.2 to
   argue the TZD head is disqualifying for this indication. **This fact is supplied by the brief
   itself** (disease-brief §4, "Isoform discipline"), so using it is sanctioned rather than a leak.
3. **I used the thiazolidinediones' physicochemistry as data.** Troglitazone, pioglitazone and
   rosiglitazone are rows in `evidence/ppar-class-drug-properties.tsv` and I used their MW/aLogP/PSA/
   HBD/RTB/Ro5v/QED fields directly. I also used general knowledge of troglitazone's withdrawal for
   idiosyncratic hepatotoxicity and of the TZD ring's oxidative ring-opening — general pharmacology,
   not DR-related.
4. **Negative decision disclosed.** I scored **Epalrestat 2** partly on the ground that its target
   "carries negative human clinical validation." That phrase is **inherited verbatim from Round 1's
   synthesis** (§7, the Epalrestat row, sourced to the Target Analyst) rather than independently
   asserted by me, and the disease-brief §4 scoring priors independently instruct that "single-branch
   blockade downstream of the ROS node (the P1 and P3 precedents)" should lose points. I note it
   because the underlying fact is DR-adjacent; the score itself rests on my own axis (the rhodanine is
   replaceable but the headroom leads nowhere), and would be 2–3 on chemotype-maturity grounds alone.
5. **A residual I cannot fully excise.** I know the DR/DME trial status of several compounds in this
   set from pretraining. My scoring axis — structural optimisability of the chemotype — is
   indication-agnostic and I did not consult that knowledge in assigning any score; the rank order
   here (linalool and melatonin above pemafibrate and fenofibrate) is close to the inverse of what
   DR-status knowledge would produce, which is itself weak evidence that the axis was applied
   honestly. But per Round 1 §10, dataset blinding removes the project's data signal, not the model's
   pretrained knowledge, and the scoring step should read this report that way.

**No agent-to-agent leakage of DR status.** Nothing I read in the Round 1 agent reports contained
DR-specific drug-indication claims; the Literature Reviewer's post-hoc unblinding section does not
exist yet and I did not seek it.

---

## SCOREBLOCK

SCORE|Linalool|7|moderate|mixed|Highest ligand efficiency in set; fragment hit with clean growth vector into target window
SCORE|Melatonin|6|moderate|mixed|Rigid neutral N-acylamine, 8/8 BRB rubric; ideal template but no PPARa SAR to grow
SCORE|Linoleic acid|5|moderate|mixed|Acid-to-ethanolamide is the only transformation improving potency and access together
SCORE|Fenofibric acid|4|high|mixed|Potency exhausted, but oxadiazolone head swap on validated body remains cheap and unexplored
SCORE|Alpha-linolenic acid|4|moderate|mixed|Same NAE chemotype headroom as linoleic acid, more peroxidisable and dominated within class
SCORE|Icosapent ethyl|4|low|knowledge-based|MFSD2A carrier route differentiated but narrow acyl tolerance and autotaxin-to-LPA wrong-sign risk
SCORE|Elafibranor|3|moderate|mixed|Enone removable and head addressable, but starts logP 5.16 with pro-angiogenic delta limb
SCORE|Dimethyl fumarate|3|high|knowledge-based|Reactive Michael acceptor is the mechanism; successors optimised tolerability only, not mechanism
SCORE|Candesartan cilexetil|3|high|knowledge-based|Sartan chemotype fully mature; cell-surface target makes access constraint largely moot
SCORE|Ezetimibe|3|moderate|knowledge-based|Already hard-optimised; brush-border mechanism topologically immune to the access problem
SCORE|Fenofibrate|2|high|mixed|Prodrug axis closed: no retinal hydrolase, RPE65 disqualifying, liberated anion re-effluxed
SCORE|Pemafibrate|2|high|data-backed|Terminal molecule of its series; QED 0.24, RTB 13, 1/8 rubric, no non-destructive move left
SCORE|Seladelpar|2|high|mixed|Delta chemotype by structure; optimising it optimises the wrong isoform, plus migration-prone glucuronide
SCORE|Epalrestat|2|moderate|mixed|Rhodanine replaceable but headroom leads to a target with negative validation; photoisomerising chromophore
SCORE|Minocycline|2|high|knowledge-based|Seventy-year-old scaffold exhausted; chelating photo-oxidising chromophore intrinsic to tetracycline core
SCORE|Quercetin|1|high|mixed|Catechol PAINS on six mechanisms and direction-incoherent; optimising a frequent hitter optimises artifact
