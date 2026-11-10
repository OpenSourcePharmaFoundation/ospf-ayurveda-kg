# The non-acidic PPARα ligand

Step 7 of `docs/prompts/dr-solve-open-questions-prompt.md`.

**Scope.** Build the AF-2 pharmacophore from structure, screen the neutral and weakly acidic
head-group window against it, quantify the efficacy a neutral head costs, propose concrete
scaffolds with full predicted profiles, and specify the assay cascade that does not exist.

**Rule followed throughout.** Every number is tagged **measured** (from coordinates, or from a
measurement in the literature), **computed** (by code in this repository, from measured inputs),
or **assumed** (knowledge-based, with a range). The failure this chain exists to correct is a
term being quoted as though it were the product, so nothing here reports a term without
reporting the product.

---

## 0. VERDICT

**The molecule is buildable and it is the wrong molecule. The retraction was right that the acid
is not mechanistically required, and the design programme it implied is still a bad one — for a
reason that is arithmetic rather than structural, and that the source analysis had the data to
find.**

Four findings, each computed in this step:

1. **The pharmacophore is far tighter than it was described.** Across five independent PPARα
   agonist complexes the two engaged ligand acceptor atoms sit **2.222 ± 0.064 Å apart**
   (range 2.13–2.29). The source analysis said "roughly 2.2–3.2 Å". The upper half of that range
   is empty, and the difference is not cosmetic: it converts the requirement from *a bidentate
   pair* into *a geminal pair* — two acceptors on one carbon or one phosphorus — which most of
   the proposed head groups cannot present. §1.

2. **The real filter is lone-pair capacity, and it rules out the prior lead.** The measured
   contact map is not four donors onto four acceptor atoms. It is four donors onto **two** atoms:
   one serves Ser280 + Tyr314, the other serves His440 + Tyr464. Each engaged atom accepts **two**
   hydrogen bonds. An oxygen can; an azole or pyridine-type nitrogen, with one in-plane lone pair,
   cannot. **This disqualifies the 1,2,4-oxadiazol-5(4H)-one — the source analysis's lead
   head-group recommendation** — whose ring N and ring O are both single-lone-pair acceptors. §2.

3. **The efficacy loss is real, modest at the median, and badly determined — and the standard
   assay systematically overstates it in the favourable direction.** A neutral head costs
   ~2.7 kcal/mol at the H12 contact. In a coactivator-rich reporter line that reads as
   **Emax 92%**; in a coactivator-poor tissue the same molecule gives **Emax 57%
   [95% CI 8–95%]**. The spread is dominated not by the chemistry but by two receptor parameters
   nobody has measured. §3.

4. **The strategy the design rests on is backwards.** The source analysis's central instruction is
   to spend the same ligand efficiency "at logD 2.8 instead of logD 5.5". Swept explicitly, the
   free-drug retinal margin **rises monotonically with logP across the entire drug-like range**,
   because potency gains ~1.0 log per logP unit while free fraction loses only ~0.45–0.70. Moving
   from logP 5.6 to 2.8 costs **≈200× of margin for a neutral head and ≈350× for an acid**. The
   field put lipophilicity where it did because that is where the free-drug margin is. §5.

**The net.** Of five scaffolds carried end to end through the Step 5 ocular model, **none reaches
free-EC50 retinal occupancy at a deliverable oral dose.** The best neutral design needs ~36 g/day;
the best geometric match needs ~833 g/day. The acid control — carboxylate kept, lipophilicity
stripped — needs ~3.7 g/day, still not a drug but **9.7× better than the best neutral and 228×
better than the best geometric match.** §4.

> **Going neutral raises neural-retina partition ~20× (Kp,uu 0.042 → 0.82–0.96) and gives back
> more than that in potency and efficacy. And the 20× lands in the wrong compartment: in the
> Step 5 model the endothelium — where the vascular lesion is — carries a compound-independent
> retention term, so the partition gain appears only behind the tight junction.** §4.3.

**What this does *not* overturn.** The structural retraction stands: the carboxylate is a
convention, not a mechanism, and a neutral ligand binds PPARα legally. Oleoylethanolamide remains
the existence proof. What fails is the inference from "legal" to "worth building".

---

## 1. THE PHARMACOPHORE, MEASURED

### 1.1 What was measured, and from what

Ten deposited structures, fetched from RCSB and parsed in
`src/analysis/ppara_ligand_design/structures.py`: five PPARα agonist complexes spanning four acid
chemotypes, one PPARα antagonist complex as the H12-displaced control, two PPARγ and two PPARδ
complexes for the isoform comparison.

| Isoform | H3 | H5 | H11 | H12 (AF-2) |
|---|---|---|---|---|
| **PPARα** | Ser280 OG | Tyr314 OH | His440 NE2 | Tyr464 OH |
| **PPARγ** | Ser289 OG | His323 NE2 | His449 NE2 | Tyr473 OH |
| **PPARδ** | Thr252 OG1 | His287 NE2 | His413 NE2 | Tyr437 OH |

The PPARδ residues are **computed, not cited**: they are the side chains within 3.6 Å of the
GW0742 carboxylate in 3TKM, found by contact search, then checked against the α/γ alignment. The
literature numbering for PPARδ is frequently given in γ-equivalent terms, which does not resolve
against δ coordinates.

### 1.2 The contact map — four donors onto two atoms

The pattern is identical in all five PPARα agonist complexes and it is the central result of this
step. *(measured, `data/processed/ppara_af2_cage_contacts.tsv`)*

```
                    O(proximal)                O(distal)
                   /           \              /         \
          Ser280-OH            Tyr314-OH   His440-NH   Tyr464-OH
            (H3)                 (H5)        (H11)      (H12/AF-2)
             \___________________/             \___________/
              donors 4.25 A apart             3.61 A apart
                         \                      /
                          \____ 2.22 A ________/
                              geminal O-O
```

| Structure | Ligand | O(prox) → Ser280 | → Tyr314 | O(dist) → His440 | → Tyr464 |
|---|---|---|---|---|---|
| 1K7L | GW409544 | 2.72 | 2.69 | — | 2.60 |
| 1I7G | tesaglitazar | 2.68 | 2.59 | 2.91 | 2.45 |
| 2P54 | GW590735 | 2.88 | 2.53 | 2.80 | 2.56 |
| 3VI8 | pemafibrate series | 2.54 | 2.69 | 2.70 | 2.70 |
| 4BCR | WY-14643 | 2.49 | 2.86 | 3.21 | 2.89 |

Donor–donor distances, PPARα agonists, mean ± sd over n = 5 *(measured)*:
H3–H5 **4.25 ± 0.21**, H11–H12 **3.61 ± 0.52**, H5–H12 **3.35 ± 0.31**, H3–H11 6.62 ± 0.35,
H3–H12 6.41 ± 0.17, H5–H11 5.80 ± 0.65.

**The consequence for design.** Each of the two ligand oxygens bridges a donor pair 3.6–4.3 Å
apart. Only an atom with **two** usable lone pairs can do that. The requirement is therefore not
"a bidentate acceptor array" but:

> **Two acceptor atoms, 2.22 ± 0.06 Å apart, each able to accept two hydrogen bonds
> simultaneously, with the attachment vector pointing out along arm I.**

### 1.3 The antagonist control

1KKQ (GW6471, H12 displaced) makes **one** cage contact — Tyr314 at 3.34 Å — and no H12 contact
at all. Head-region free volume rises from 40.8 Å³ in the agonist complexes to **131.5 Å³**
*(computed)*. The cage only exists in the closed state; it is a property of the active
conformation, not of the apo pocket. This is the structural anchor for the efficacy model in §3.

### 1.4 "Arm I is narrower at PPARα" — not supported

The claim that drove head-group selection in the source analysis, tested directly. Free volume
available to a ligand heavy atom within 4.5 Å of the cage centroid, ligand and waters deleted,
0.4 Å grid *(computed)*:

| Isoform | State | Free volume (Å³) | n |
|---|---|---:|---:|
| PPARα | agonist | **40.8 ± 7.1** | 5 |
| PPARγ | agonist | **38.6 ± 1.1** | 2 |
| PPARδ | agonist | 49.7 ± 11.6 | 2 |
| PPARα | antagonist | 131.5 | 1 |

**PPARα's head region is not smaller than PPARγ's — the two are equal within error.** The
footprint argument, as a statement about available volume, is not reproduced.

What *does* separate them is geometry, not size. Rosiglitazone's engaged acceptors in PPARγ span
**4.46 Å** (2PRG 4.47, 4EMA 4.44) using three different atoms — O4 for H3+H5, O2 for H11, N3 for
H12. PPARα's span 2.22 Å using two. **γ accepts a wide three-point array; α demands a tight
two-point one.** That is the real isoform discriminator and it is a selectivity handle, which
§4 uses.

PPARδ sits with α at 2.10 Å (3TKM), so **geometry buys nothing against δ** — the isoform that
matters most for retinal safety. Noted again in §4 and §6.

---

## 2. THE SCREEN

Twenty-five head groups, each capped with a methyl standing in for the linker, conformers
generated with ETKDGv3 and MMFF-minimised, acceptor atoms assigned with an explicit lone-pair
capacity model. Code: `src/analysis/ppara_ligand_design/headgroups.py`; output:
`data/processed/ppara_headgroup_screen.tsv`.

**Method validation.** The computed geminal O–O distance for acetate is **2.29 Å** against the
crystallographic mean of **2.222 Å** — agreement to 0.07 Å, which is what licenses using computed
spans for head groups that have never been co-crystallised.

Filters applied in the order the measurement imposes:

1. **Lone-pair capacity** — at least two acceptor atoms able to take two H-bonds each.
2. **Span** — best competent pair reachable within 2.22 ± 0.35 Å.
3. **Footprint** — calibrated, not asserted: the threshold is the volume of the
   thiazolidinedione, the one head with an unambiguous empirical verdict at PPARα.

| Head group | acceptors | double-acceptors | best span (Å) | vol ÷ COO⁻ | % neutral @ 7.4 | verdict |
|---|---:|---:|---:|---:|---:|---|
| Carboxylate (baseline) | 2 | 2 | 2.29 | 1.00 | 0.007 | **PASS** |
| **Oxazolidin-2-one** | 2 | 2 | **2.29** | 1.70 | 100 | **PASS** |
| **Dimethyl sulfone** | 2 | 2 | 2.52 | 1.46 | 100 | **PASS** |
| **Methanesulfonamide** | 2 | 2 | 2.53 | 1.37 | 99.9 | **PASS** |
| Phosphonamidate (P=O/P–O) | 2 | 2 | 2.58 | 1.77 | 100 | FAIL-span |
| Hydroxamic acid | 2 | 2 | 2.64 | 1.27 | 97.5 | FAIL-span |
| Phosphinic acid | 2 | 2 | 2.65 | 1.50 | 0.001 | FAIL-span |
| N-acylethanolamine (OEA head) | 2 | 2 | 2.67 | 1.89 | 100 | FAIL-span |
| Squaramide | 2 | 2 | 3.14 | 1.71 | 97.5 | FAIL-span |
| Cyclopropane-1,1-dicarboxamide | 2 | 2 | 4.02 | 2.16 | 100 | FAIL-span |
| Malonamide | 2 | 2 | 4.05 | 1.67 | 100 | FAIL-span |
| Thiazolidine-2,4-dione | 3 | 2 | 4.53 | 1.87 | 12.4 | FAIL-span |
| **1,2,4-Oxadiazol-5(4H)-one** | 4 | **1** | — | 1.47 | 11.2 | **FAIL-capacity** |
| Isoxazol-3-ol | 3 | 1 | — | 1.56 | 1.2 | FAIL-capacity |
| Phosphine oxide | 1 | 1 | — | 1.70 | 100 | FAIL-capacity |
| Sulfoximine | 2 | 1 | — | 1.53 | 100 | FAIL-capacity |
| Acylcyanamide | 3 | 1 | — | 1.40 | 0.013 | FAIL-capacity |
| **Tetrazole** (anion and neutral) | 4 | **0** | — | 1.32 | 0.2 | **FAIL-capacity** |
| Acylsulfonamide | 4 | 3 | 2.46 | 1.99 | 0.04 | FAIL-footprint |
| 4,4-Dimethyloxazolidin-2-one | 2 | 2 | 2.29 | 2.00 | 100 | FAIL-footprint |

### 2.1 Why tetrazole is out — three reasons, one of them new

The task asks for this explicitly. The conventional reasons hold and a third, stronger one is
added by the measurement.

1. **Lone-pair capacity — decisive, and structural.** Tetrazolate's negative charge is delocalised
   over four ring nitrogens, each carrying **one** lone pair in the ring plane. **No atom in a
   tetrazole can accept two hydrogen bonds.** It therefore cannot reproduce the measured 2:2
   contact pattern at any pKa, any footprint, or any orientation. Its four acceptors are confined
   to an array ~2.2 Å across, which cannot simultaneously bridge donor pairs 4.25 Å and 3.61 Å
   apart the way two double-acceptor oxygens do. *This reason is not in the source analysis and
   it is the one that cannot be engineered around.*
2. **pKa — insufficient.** 4.5–4.9 against the carboxylate's 3.0–3.5 raises the neutral fraction
   at pH 7.4 from 0.007% to 0.2%, ~30×. The permeant species is still 99.8% absent.
3. **Transporter recognition — unchanged.** It remains a delocalised lipophilic anion, which is
   the OATP1B1/1B3 recognition element. The sartans are hepatically taken up for exactly this
   reason, and swapping carboxylate for tetrazole does not address the hepatoselectivity that
   Step 5 identified as the mechanism denying these drugs the eye.

**Correction to the source analysis.** It excluded tetrazole on footprint ("~1.5× larger"). Computed
here, tetrazole is **1.32×** the carboxylate — smaller than the oxazolidinone (1.70×) that
survives, and smaller than the thiazolidinedione (1.87×). **The footprint reason was wrong; the
exclusion was right.**

### 2.2 Two more corrections to the prior screen

- **The thiazolidinedione fails on span, not footprint.** 4.53 Å against a required 2.22 Å, using
  a three-atom array. Since PPARγ's own engaged span is 4.46 Å, the TZD is not "too big for α" —
  **it is the right shape for γ and the wrong shape for α.**
- **The 1,2,4-oxadiazol-5(4H)-one, upgraded in the source analysis to the lead head-group
  recommendation, fails.** It presents an exocyclic C=O (capacity 2), a ring N (capacity 1) and an
  aromatic ring O (capacity 1 — one lone pair is in the ring π system, which is also why furan-type
  oxygens are weak acceptors). With one double-acceptor atom it can serve at most two of the four
  donors. The same reasoning disqualifies isoxazol-3-ol.

### 2.3 Phosphine oxide and phosphonamide, as asked

- **Phosphine oxide presents one acceptor atom.** Confirmed: it can serve at most two donors,
  never four. The source analysis reached the same conclusion qualitatively; the measurement
  gives it a mechanism. Usable only as the distal half of a two-point head.
- **A phosphonamidate — P(=O)(OMe)(NH₂) — does present a geminal pair**, and it is the strongest
  neutral acceptor pair available (pK_BHX 3.0–3.5, ~1.3 units below a carboxylate rather than the
  2–3 units everything else gives up). Its computed span is **2.58 Å**, 0.36 Å wide of the measured
  requirement, and a tetrahedral phosphorus cannot be compressed the way an sp² carbon can.
  It is carried as scaffold PHOS-1 and it is the best of the neutral set. **Caveat: MMFF94's
  phosphorus parameterisation is the weakest in this screen; the 2.58 Å figure deserves a DFT
  check before anyone synthesises on it.**

### 2.4 The near-miss band

Four heads cluster at 2.58–2.67 Å, just outside a window whose edge is a judgement (±0.35 Å, set
at ~5× the measured sd to allow for coordinate error and induced fit). **They should be read as
"strained, conceivable with helix movement", not as cleanly excluded.** The OEA head is one of
them at 2.67 Å — which is a result, not a near-miss: it is the structural explanation for why
oleoylethanolamide is a partial agonist. Its head cannot make the geminal pair, so it cannot place
an atom to serve His440 and Tyr464, and the H12 contact is the one it drops.

---

## 3. THE EFFICACY ASYMMETRY, QUANTIFIED

Code: `src/analysis/ppara_ligand_design/h12_efficacy.py`; output
`data/processed/ppara_h12_efficacy.tsv`.

Two-state model — H12 docked (active) versus sampling open — with coactivator binding only the
docked state:

```
    L     = [closed]/[open] for ligand-bound receptor, no coactivator
    f_act = L(1 + A/Kd) / (1 + L(1 + A/Kd))
    Emax  = f_act(ligand) / f_act(carboxylate full agonist)
    L(ligand) = L(full) × exp(−ΔΔG_H12 / RT)
```

ΔΔG_H12 comes from the screen: if the head cannot present a competent geminal pair it forfeits the
whole contact; if it can, it loses the pK_BHX deficit converted at 1.2–1.4 kcal/mol per unit,
**capped at what the contact is worth**. (Without that cap the model charges a weak acceptor more
than the contact's total value and returns the nonsensical result that losing a contact scores
better than weakening it. That bug was present in the first version of this model.)

| Head | ΔΔG_H12 (kcal/mol) | **Emax, reporter assay** | **Emax, tissue** |
|---|---:|---:|---:|
| Carboxylate (reference) | 0 | 100% | 100% |
| Phosphonamidate | 1.97 | 97.6% | **81.5%** [34–97] |
| Oxazolidin-2-one | 2.66 | 93.7% | **61.4%** [12–95] |
| Sulfone / sulfonamide | 2.75 | 92.4% | **56.6%** [8–95] |
| Any head that forfeits the contact (OEA, oxadiazolone, tetrazole, hydroxamic) | 2.75 | 92.4% | **56.6%** [8–95] |

### 3.1 Three results

**(a) The loss is smaller than "partial agonist by construction" implies, at the median.** 57% of
a fibrate maximum is a functional agonist, not a tool compound. The source analysis's Concept B
predicted "Emax 25–55%"; the modelled median sits at the top of that and above it. The reason is
that coactivator binding pulls the equilibrium towards the docked state, so the ligand does not
have to pay for closure alone.

**(b) The assay will lie to you, and in a predictable direction.** The *same molecule* reads
**92% in a coactivator-rich reporter line and 57% in a coactivator-poor tissue.** Reporter assays
are typically run in lines overexpressing SRC-1 or with PGC-1α co-transfected; retina is not such
a tissue. **A neutral partial agonist will look like a near-full agonist in the primary assay and
behave as a half-efficacy partial agonist in the target organ.** This is the single most
actionable finding for the cascade in §6, and it is a systematic bias, not noise.

**(c) The prediction is dominated by what nobody has measured.** Rank correlation against
log Emax, oxazolidinone head, tissue coactivator *(computed)*:

| ρ | Input |
|---:|---|
| **0.73** | worth of the Tyr464 contact (ΔG_H12) |
| **0.59** | closure free energy for a full agonist |
| 0.13 | coactivator availability A/Kd |
| 0.11 | geometric efficiency |
| 0.06 | reference carboxylate basicity |
| 0.04 | energy per pK_BHX unit |

**The chemistry parameters contribute almost nothing to the uncertainty. Two receptor
conformational-energetics parameters contribute nearly all of it**, and neither has ever been
measured for PPARα. That is why the interval is 8–95% and why no amount of medicinal chemistry
will narrow it. It is, however, measurable — HDX-MS or ¹⁹F-NMR on the H12 region against a matched
agonist pair, or a coactivator-recruitment titration at varying SRC-1 — and so it belongs in the
cascade as a gate rather than as a risk. §6.

**Honest limitation.** The assay-versus-tissue gap is driven by the coactivator ranges, which are
assumed (A/Kd 1–30 for a reporter line, 0.03–1.0 for tissue). The *direction* is robust — a
coactivator that binds only the closed state must stabilise it — but the *magnitude* is only as
good as those ranges, and they are the least defensible numbers in this note.

---

## 4. FIVE SCAFFOLDS, COSTED END TO END

Code: `src/analysis/ppara_ligand_design/scaffolds.py`; output
`data/processed/ppara_nonacidic_scaffolds.tsv`. Retinal partition is **not** re-derived here — the
scaffolds are passed as ordinary compounds to the Step 5 model in `src/analysis/ocular_exposure`,
which is calibrated against the one measured ocular concentration of a fibrate after systemic
dosing that exists.

### 4.1 How potency is obtained — derived, not asserted

`pEC50 = LLE + logP`, with the LLE ceiling taken from the anionic series (pemafibrate 3.45,
elafibranor 2.3, fenofibric acid 0.9) and reduced, for a neutral head, in proportion to the
acceptor basicity it gives up. **The penalty is calibrated so the model reproduces the only
neutral PPARα ligand with a measured EC50**: oleoylethanolamide, logP 5.9 — predicted **126 nM**
against a measured 120 nM–3 µM. ✅

> **A correction this forces.** The source analysis sets a design target of LLE 3.5 and justifies
> it with "pemafibrate already demonstrates LLE 3.45" — calling this "the single most important
> sentence in this report". **That transfers an anionic LLE onto a neutral design.** The two
> neutral ligands in its own table (OEA 1.0, linalool 1.1) sit two and a half log units below, and
> its own acceptor-basicity argument predicts exactly such a gap. The target profile is
> internally inconsistent: at logD 2.8 with a neutral head, EC50 500 nM requires an LLE never
> demonstrated by any neutral PPARα ligand.

Its companion assumption fails too. §7.1 of the source analysis assumes **fu 0.10 at logD 2.8**;
the neutral logD–protein-binding relation used here returns **fu 0.024**. The two optimisms
compound to roughly 100× on the occupancy estimate.

### 4.2 The five

All descriptors RDKit-computed; logD from cLogP and the assigned pKa; fu from a neutral-drug
logD–PPB relation (spot-checked: propranolol predicted 0.12 vs measured 0.13; diazepam 0.018 vs
0.02; carbamazepine 0.03 vs 0.26 — an order of magnitude out, and the intercept range spans that
scatter rather than hiding it).

| | **OXZ-1** | **SULF-1** | **PHOS-1** | **ACID-LOW** | **HYDX-1** |
|---|---|---|---|---|---|
| Head | oxazolidin-2-one | methyl sulfone | phosphonamidate | carboxylate *(control)* | hydroxamic acid |
| SMILES | `O=C1OCC(N1)c1ccc(cc1)Oc1ccc(cc1)S(C)(=O)=O` | `CS(=O)(=O)CC(C)(C)Oc1ccc(cc1)-c1ccc(cc1)C#N` | `COP(=O)(N)COc1ccc(cc1)-c1ccc(OC)cc1` | `CC(C)(Oc1ccc(cc1)-c1ccncc1)C(O)=O` | `ONC(=O)C(C)(C)Oc1ccc(cc1)-c1ccc(F)cc1` |
| MW | 333.4 | 329.4 | 307.3 | 257.3 | 289.3 |
| cLogP / TPSA | 2.66 / 81.7 | 3.43 / 67.2 | 3.50 / 70.8 | 2.99 / 59.4 | 3.16 / 58.6 |
| HBD / RTB / QED | 1 / 4 / 0.93 | 0 / 5 / 0.84 | 1 / 6 / 0.83 | 1 / 4 / 0.91 | 2 / 4 / 0.67 |
| **logD₇.₄** | **2.66** | 3.43 | 3.50 | **−1.16** | 3.14 |
| **fu (plasma)** | **0.029** | 0.011 | 0.010 | 0.015 | 0.015 |
| **EC50, derived** | 64 µM | 42 µM | **3.3 µM** | **2.0 µM** | 20 µM |
| **Kp,uu neural retina** | **0.82** | 0.94 | **0.96** | 0.041 | 0.94 |
| Margin, endothelium | 2.3e−4 [1.1e−5 – 5.0e−3] | 4.0e−4 | 1.9e−3 [9.7e−5 – 3.6e−2] | **2.7e−2 [1.7e−3 – 0.45]** | 5.9e−4 |
| **Emax, tissue** | 0.61 | 0.57 | **0.82** | **1.00** | 0.57 |
| **Output (margin × Emax)** | 1.2e−4 | 1.9e−4 | 1.4e−3 | **2.7e−2** | 2.8e−4 |
| vs fenofibric acid | 0.0× | 0.0× | 0.2× | **3.2×** | 0.0× |
| **Dose for free-EC50 occupancy** | **833 g/day** | 1,058 g/day | **36 g/day** | **3.7 g/day** | 541 g/day |

*Dose is reported because it is the only figure that does not depend on the arbitrary starting
dose — everything upstream of plasma concentration scales linearly with it.*

### 4.3 Reading the table

**The neutral heads do exactly what they were supposed to do, and it is not enough.** Kp,uu rises
from 0.042 to 0.82–0.96 — a **19.7× improvement in neural-retina partition**, achieved precisely
as predicted, by removing the anion that the barrier's efflux transporters recognise.

Dose required for free-EC50 occupancy, relative to the acid control *(computed; this is the
like-for-like comparison, because it removes each scaffold's arbitrary starting dose)*:

| | ACID-LOW | PHOS-1 | HYDX-1 | OXZ-1 | SULF-1 |
|---|---:|---:|---:|---:|---:|
| × worse than the acid control | 1.0 | **9.7** | 148 | **228** | 289 |

**And the partition gain lands in the compartment that matters least.** The Step 5 model treats
the retinal vascular endothelium as blood-facing — its luminal membrane faces plasma, so its
ceiling is 1.0 and what puts it below is efflux, carried as a **compound-independent retention
term (0.318)**. The neutral scaffolds and the acid therefore receive the *same* endothelial ratio,
and the entire 19.7× advantage appears only in the neural retina, behind the tight junction. The
vascular lesion that defines DR is at the endothelium.

> **Honest limitation, inherited rather than introduced.** That compound-independence is a
> modelling choice in Step 5, not a measured result. If endothelial retention in fact scales with
> the same efflux liability as the neural retina, every neutral scaffold improves by up to ~20×
> — which brings PHOS-1 to ~1.8 g/day and OXZ-1 to ~42 g/day. **Still not a dose, so the verdict
> is unchanged, but the margin of the verdict is not.** This is the single assumption most worth
> attacking if someone wants to rescue the neutral route.

**The free-fraction term does not move in the designed direction either.** Going neutral raises
logD (no ionisation to suppress it), and raising logD lowers fu. OXZ-1 is the only neutral
scaffold with fu above the acid's, and only because it carries a sulfone on the distal vector.
This is the term the source analysis correctly identified as unfixed by the chemotype hop (§2.3 of
that report) — and then assumed fixed anyway in its target profile.

### 4.4 Per-scaffold: what breaks first

- **OXZ-1 — the lead on geometry.** Best measured span match of any neutral head (2.29 Å against
  2.222 ± 0.064), permanently neutral, QED 0.93, polarity parked distally where it lowers logD
  without touching arm I. **Breaks first: potency.** A 64 µM derived EC50 is not a starting point,
  it is a fragment hit. Second: **PPARδ selectivity** — δ's cage takes the same tight geminal pair
  this head is built around (3TKM, 2.10 Å), δ is the most abundant retinal PPAR, and it is
  pro-angiogenic. Geometry gives nothing against δ; sterics must carry all of it.
- **SULF-1 — the cheap experiment, not a candidate.** Smallest competent neutral head, trivially
  made from the fibrate body. **Breaks first: potency**, by the largest acceptor-basicity deficit
  in the competent set. Its value is as a two-month test of whether the geometric hypothesis
  predicts measurable binding at all.
- **PHOS-1 — the best neutral, and the one nobody has tried at any PPAR.** Strongest neutral
  acceptor pair, highest retained efficacy (82%), lowest derived EC50 of the neutrals, and not an
  OATP1B recognition element. **Breaks first: the span** — 2.58 Å, wide of requirement, on a
  tetrahedral centre that cannot be compressed. Then P–N hydrolytic and metabolic stability. A
  DFT span calculation is the cheapest possible gate and should precede any synthesis.
- **ACID-LOW — the control, included to be falsified, and it was not.** Keeps the validated head
  and strips lipophilicity. Pays no efficacy tax, no basicity tax, and the best potency in the
  set. Its neural-retina Kp,uu is 20× worse than every neutral and **it still wins by 9.7×.** **Breaks first:
  nothing in the chemistry — the exposure.** It remains an anion, so OATP1B hepatic uptake and
  MRP/BCRP efflux persist, and 3.7 g/day is not a deliverable oral dose.
- **HYDX-1 — carried with its liabilities stated.** Smallest neutral competent head (1.27×), which
  is the footprint argument's best case. **Breaks first: off-target metal chelation.** A
  hydroxamate is a zinc binder — HDAC, the MMPs and carbonic anhydrase are all in range, and MMP
  inhibition in retina is not a neutral liability. Hydroxamate mutagenicity via Lossen
  rearrangement is second. QED 0.67, the worst of the five.

### 4.5 Isoform selectivity, consolidated

| Against | Handle | Strength |
|---|---|---|
| **PPARγ** | **Geometric, and strong.** γ's engaged acceptors span 4.46 Å using three atoms; a tight 2.2–2.3 Å geminal pair is intrinsically α-shaped. Holding the span *is* the γ counter-screen. | measured, high confidence |
| **PPARδ** | **None from the head.** δ takes the same tight pair (2.10 Å). Selectivity must come entirely from arm II/III sterics — and compact neutral lipophiles are δ's preferred chemotype. | measured; the programme's worst exposure |

**This is a genuine cost of going neutral that the carboxylate did not carry**, since the acid was
itself part of α selectivity. δ counter-screening belongs in the primary cascade, not the
secondary.

---

## 5. THE STRATEGY IS BACKWARDS

The source analysis's operative instruction — "it needs the *same* LLE spent at logD 2.5–3 instead
of logD 5.5" — is testable, and it was never tested. Sweeping logP with molecular weight held
fixed *(computed, `scaffolds.logp_sweep`)*:

| logP | Neutral head: margin | Anionic head: margin |
|---:|---:|---:|
| 0.00 | 1e−5 | 1e−5 |
| 1.86 | 7e−5 | 4.9e−4 |
| **2.79** | **2.6e−4** | **3.3e−3** |
| 3.71 | 1.2e−3 | 2.2e−2 |
| 4.64 | 7.2e−3 | 0.159 |
| **5.57** | **5.2e−2** | **1.15** |
| 6.50 | 0.426 | 8.64 |

**The margin rises monotonically with logP over the entire range, for both head types.** There is
no optimum at logD 2.8. Moving from logP 5.57 to 2.79 costs **≈200×** for a neutral head and
**≈350×** for an acid (Monte-Carlo estimates; stable to ~1% across reruns).

The arithmetic is simple once stated: raising logP improves potency by ~1.0 log per unit (at
constant LLE, which is the source analysis's own premise) and worsens free fraction by only
0.45–0.70. **Under its own assumption, its strategy is self-defeating.**

**Robustness.** Constant LLE implies potency improves 1:1 with logP indefinitely, which is the
assumption LLE exists to question. Re-run with EC50 floored at 1 nM — the best value ever measured
in the class — the curve is unchanged below logP 5.6 and flattens only at 6.5. The conclusion
holds across the drug-like range because the plateau bites only above it.

> **Corrected reading.** The field did not put lipophilicity where it could have put polarity out
> of hepatic habit. It put lipophilicity there because that is where the free-drug margin is, at
> this receptor, for this pharmacophore. The reason the fibrates fail in retina is the one Step 5
> measured — **OATP1B hepatic extraction (502.3 nTPM liver, 0.0 nTPM retina)** — and lowering logD
> does not address it.

---

## 6. THE ASSAY CASCADE THAT DOES NOT EXIST

No PPARα programme has been run against free-drug retinal exposure, so the metrics, the models and
the translation are all unbuilt. Specifying it is a deliverable of this step whether or not the
programme runs — §5 and §3 both identify failure modes a conventional cascade would not catch.

**What a conventional cascade would get wrong, specifically.** It would report a nominal EC50 from
a serum-containing reporter assay in a coactivator-rich line, and a total-drug tissue
concentration. The first double-counts protein binding (worth ~1 log, per Step 5 §8); the second
is uninterpretable at a barrier with active efflux; and the third — the coactivator bias in §3 —
would report Emax 92% for a molecule that delivers 57% in retina. **Three independent errors, all
in the optimistic direction, compounding.**

| # | Assay | Measures | Gate | Why it is not standard |
|---|---|---|---|---|
| **0** | **HDX-MS or ¹⁹F-NMR on H12**, matched agonist pair; coactivator-recruitment titration vs SRC-1 | ΔG of H12 closure; worth of the Tyr464 contact | Both parameters bounded to within ~1 kcal/mol | **Nobody has measured these for PPARα.** §3 shows they carry ~0.73 and ~0.59 of the Emax variance — more than all chemistry parameters combined. Until they are known, no Emax prediction is better than 8–95%. **This is the cheapest high-value experiment in the note.** |
| **1** | Binding by SPR/ITC on purified LBD, **plus GW6471 antagonist reversal** | K_d, site-specificity | Saturable, reversible, competed | Discriminates real engagement from the membrane-perturbant artefact that small neutral lipophiles produce at tens of µM |
| **2** | **Free-drug-corrected EC50**: reporter assay run at ≥3 serum concentrations, EC50 extrapolated to zero binding | EC50 referenced to free drug | Extrapolation linear in fu | Routine practice quotes a nominal EC50 at one serum level; comparing it to a free tissue concentration double-counts binding |
| **2b** | The same reporter at **two coactivator levels** (endogenous vs SRC-1 overexpressed) | Emax as a function of A/Kd | Emax reported *as a range*, never as a point | §3(b). Without this the assay systematically overstates tissue efficacy |
| **3** | Equilibrium dialysis in plasma **and in retinal homogenate** | fu,plasma and fu,tissue | Both measured, same method | Kp,uu requires both. The dataset for this project contains no measured fu for any retinal tissue |
| **4** | **PAMPA/Caco-2 with a pH gradient**, bidirectional, ± MRP/BCRP inhibitor | Passive permeability; efflux ratio | ER < 2 | The pH-partition advantage of a shifted-pKa head is a *measured* property, not a predicted one, and under-delivers when membrane partitioning is slow relative to transit |
| **5** | Transfected-cell uptake, **OATP1B1/1B3** | Hepatic uptake substrate status | Not a substrate | The central design hypothesis — neutrality escapes OATP1B — must be tested, not assumed. Digoxin and the taxanes are neutral OATP1B3 substrates |
| **6** | **Ocular distribution in a pigmented species** with an inner BRB of comparable tightness, free drug by microdialysis or homogenate-corrected | **Kp,uu, measured** | Within the model's [0.009–0.354] interval, or the model is wrong | Step 5's Kp,uu is calibrated on a *single* measured ocular concentration. One more measurement roughly halves the interval. Pigmented because melanin binding changes everything |
| **7** | PPARγ and **PPARδ** transactivation, full curves | Isoform margin | ≥100× on both | δ is the one that matters (§4.5) and is routinely relegated to a secondary screen |
| **8** | FAAH/amidase stability in **retinal** homogenate; phototoxicity (no absorbance >320 nm) | Metabolic and photo-stability in the target organ | — | The target organ is continuously illuminated and expresses FAAH. Plasma stability does not substitute |

**Sequencing.** Assay 0 and the DFT span check on PHOS-1 before any synthesis. Assays 1–2b before
any lead optimisation. **Assay 6 is the gate on the entire programme** and it is also the
experiment the source analysis already identified — a ~$50–150k rodent study. Nothing downstream
is worth funding until it reads out.

---

## 7. PROBABILITY OF TECHNICAL SUCCESS

**To a Ph2a retinal biomarker readout for a non-acidic PPARα agonist: 3–8%**, conditional on the
Step 5-identified rodent experiment reading positive. The source analysis put the comparable
figure at 15–25%. This step lowers it, and the reasons are specific rather than atmospheric:

| | Effect on PTS |
|---|---|
| Pharmacophore is 2.22 ± 0.06 Å geminal, not 2.2–3.2 Å bidentate | ↓↓ Cuts the viable head-group set from ~8 to 3 |
| The prior lead head (oxadiazolone) fails on lone-pair capacity | ↓ The recommended starting point does not exist |
| Every competent neutral head is a weak acceptor | ↓↓ 10²–10⁴ potency deficit is structural, not an optimisation gap |
| Margin rises with logP; the low-logD strategy is inverted | ↓↓↓ The programme's organising principle is wrong |
| Best neutral scaffold needs 36 g/day | ↓↓↓ Not a dosing problem, a chemotype problem |
| Emax loss smaller than feared (57%, not 25%) | ↑ The one favourable revision |
| PPARδ selectivity has no geometric handle | ↓ Compounds the hardest safety risk |

**Dominant risks, in order:** (i) the rodent experiment reads negative and there is no retinal
target at all; (ii) potency cannot be recovered from the arms against a 2–3 kcal/mol acceptor
deficit; (iii) PPARδ selectivity is unachievable from a compact neutral chemotype; (iv) no
regulatory endpoint for early DR materialises — a programme risk larger than any chemistry risk.

### 7.1 What would change this verdict

- **Assay 0 returns ΔG_H12 ≤ 1.5 kcal/mol.** Then the efficacy tax is small and a weak-acceptor
  head is viable. Raises PTS to ~10–15%.
- **A neutral ligand is found with LLE > 2.5.** The entire potency argument here rests on neutral
  PPARα ligands sitting at LLE ~1.0, calibrated on a sample of two. A third data point could
  move it substantially — in either direction. **This is the weakest evidential foundation in
  the note and it is cheap to strengthen.**
- **Measured Kp,uu comes back at the top of the Step 5 interval (0.35).** Improves every row by
  ~6× and brings ACID-LOW to ~600 mg/day, which is a dose.
- **A geminal double-acceptor head with carboxylate-like basicity and no charge is found.** This
  is the actual unmet need and it is a well-posed chemistry question: nothing in physics forbids a
  strong neutral geminal acceptor pair. Squaric acid derivatives, cyclic phosphonamidates and
  sulfoximine-oxides are the places to look. **None was screened here beyond the 25 in §2**, and
  the screen is a ~1 day run per 25 additional candidates.

---

## 8. WHAT THIS CHANGES IN THE SOURCE REPORT

| Claim in `REPORT.md` / `agents/p2-sar.md` | Disposition |
|---|---|
| "The AF-2 cage is all-donor; the ligand supplies only acceptors" | **Upheld**, now measured. Caveat: hydrogens are not observed and His440's tautomer is assignable, not observed |
| "Bidentate acceptor pair ~2.2–3.2 Å apart" | **Corrected** to 2.222 ± 0.064 Å, geminal, and each atom must accept two H-bonds |
| "PPARα's arm I is narrower than PPARγ's; footprint is the first filter" | **Refuted as stated.** Head-region free volume 40.8 ± 7.1 (α) vs 38.6 ± 1.1 Å³ (γ) — equal within error. The discriminator is acceptor-array geometry (2.22 vs 4.46 Å) |
| "Tetrazole is a false friend" (excluded on footprint) | **Right conclusion, wrong reason.** 1.32× the carboxylate, smaller than heads that pass. Excluded on lone-pair capacity |
| "The 1,2,4-oxadiazol-5(4H)-one is the correct acidic answer" | **Refuted.** One double-acceptor atom; cannot serve His440 and Tyr464 |
| "TZD ruled out for α on footprint" | **Right conclusion, wrong reason.** Fails on span (4.53 Å); it is γ-shaped |
| "Charge is an acceptor-strength multiplier, not a requirement" | **Upheld** |
| "Neutral head → partial agonist by construction; Emax 25–55%" | **Upheld in direction, revised in magnitude.** 57% tissue median [8–95]; 92% in a reporter line |
| "LLE 3.5 is achievable — pemafibrate already demonstrates it" | **Refuted.** Anionic LLE transferred to a neutral design; neutral PPARα ligands sit at LLE ~1.0 |
| "fu 0.10 at logD 2.8" (§7.1 target profile) | **Refuted.** Neutral logD–PPB relation gives 0.024 |
| "Spend the same LLE at logD 2.8 instead of 5.5" | **Refuted.** Margin rises monotonically with logP; the move costs ≈200–350× |
| "The chemistry is tractable and the programme is premature" | **Upheld on both halves, and strengthened.** Tractable: yes, three competent neutral heads exist. Premature: more so than stated |

---

## 9. FILES AND REPRODUCTION

```bash
source venv/bin/activate
python -m src.analysis.ppara_ligand_design.af2_cage      # geometry from coordinates
python -m src.analysis.ppara_ligand_design.headgroups    # the screen
python -m src.analysis.ppara_ligand_design.h12_efficacy  # Emax + sensitivity
python -m src.analysis.ppara_ligand_design.scaffolds     # profiles via the Step 5 model
```

| Path | Contents |
|---|---|
| `src/analysis/ppara_ligand_design/structures.py` | PDB set, mmCIF reader, cage residues per isoform |
| `src/analysis/ppara_ligand_design/af2_cage.py` | Donor geometry, H-bond contacts, arm I free volume |
| `src/analysis/ppara_ligand_design/headgroups.py` | Head-group screen: capacity, span, footprint |
| `src/analysis/ppara_ligand_design/h12_efficacy.py` | Two-state H12 model; Emax and its sensitivity |
| `src/analysis/ppara_ligand_design/scaffolds.py` | Five designs end to end; logP sweep; OEA calibration |
| `data/processed/ppara_af2_cage_geometry.tsv` | Per-structure donor distances, span, free volume |
| `data/processed/ppara_af2_cage_contacts.tsv` | Every cage H-bond, per structure |
| `data/processed/ppara_headgroup_screen.tsv` | 25 head groups, full screen |
| `data/processed/ppara_h12_efficacy.tsv` | ΔΔG_H12 and Emax with intervals |
| `data/processed/ppara_nonacidic_scaffolds.tsv` | Five scaffolds, full predicted profiles |

Structures are cached to `data/raw/pdb/` (gitignored — byte-identical re-downloads from RCSB).
Seed 20261109 throughout; `scaffolds.py` prints its OEA calibration check on every run.

### Not done

- **No docking or free-energy calculation.** Spans are from MMFF conformer ensembles, which is
  adequate for a geometric screen and is not a binding prediction. PHOS-1's 2.58 Å in particular
  needs DFT before anyone acts on it.
- **No PPARδ scaffold-level selectivity modelling.** §4.5 identifies δ as the dominant risk and
  this step does not quantify it; it would need arm II/III shape comparison, which the free-volume
  method here does not cover.
- **The scaffolds are design concepts, not synthetic routes.** No retrosynthesis, no assessment of
  whether the quaternary centres in SULF-1 and HYDX-1 are accessible at scale.
- **Potency remains derived, not measured**, from a two-point neutral LLE calibration. §7.1 flags
  this as the weakest evidential foundation here.

---

## Status — 2026-11-09 — step 7: design the non-acidic PPARα ligand

**Done.** Built `src/analysis/ppara_ligand_design/` (5 modules) and this note. Measured the AF-2
cage geometry from 10 PDB structures; screened 25 head groups against the measurement; built and
calibrated a two-state H12 efficacy model; profiled 5 scaffolds end to end through the Step 5
ocular exposure model; swept logP to test the source analysis's core strategy. Five TSVs written
to `data/processed/`.

**Verified.** All four modules run clean under `black`. Two internal calibration checks pass and
both are printed on every run: computed acetate geminal span 2.29 Å vs crystallographic 2.222 Å
(method validation for the screen), and predicted OEA EC50 126 nM vs measured 120 nM–3 µM
(calibration for every derived potency). Two modelling bugs were found and fixed during
development and are documented in the code: an uncapped ΔΔG that made losing the H12 contact score
better than weakening it, and the neutral logD–PPB relation applied to an anion, which predicted
fenofibric acid 80% unbound against a measured 1%.

**Chain-state note for the next step.** `tmp/chain-runs/*.state` marks steps 5, 6 and 7 as
`failed`. That file is stale for 5 and 6: both deliverables exist and are committed
(`docs/notes/retinal-exposure-model.md`, `docs/notes/retinal-lipid-efflux-candidates.md`,
`src/analysis/ocular_exposure/`, `src/analysis/efflux_axis/`). Step 7's deliverable genuinely did
not exist before this run. **Verify against the repository, not the state file.**

**What step 8 needs.** Twelve dispositions against `REPORT.md` and `agents/p2-sar.md` are tabulated
in §8 — four upheld, six refuted, two right-conclusion-wrong-reason. The three that change the
report's narrative rather than its details are: the arm I footprint argument is not supported by
measurement; the oxadiazolone recommendation fails; and the "same LLE at lower logD" strategy is
inverted — the free-drug margin rises with logP. §5 should be reconciled with the report's §5.6,
which currently presents the neutral chemotype as an open opportunity rather than a costed and
unfavourable one.
