# P1 — Medicinal Chemist: Structural Analysis of the Diabetic Retinopathy Candidate Set

**Agent:** Medicinal Chemist
**Date:** 2026-10-05
**Run:** BLINDED benchmark run — see §12 for the compliance statement
**Inputs:** `disease-brief.md`; `disease-model.md` §5, §5.2, §6; `agents/p0-ppara-scout.md` §1.2, §3.1, §4, §6, §8; `.claude/skills/chemist/SKILL.md`; `evidence/ppar-class-drug-properties.tsv`; `evidence/compound-dr-target-matrix.tsv`; `evidence/ppara-interactions.tsv`; `data/processed-blinded-diabetic-retinopathy/chembl_approved_drugs.csv` and `chembl_natural_products.csv`

---

## 0. Verdict in one paragraph

The structures say the PPARα programme has an **unsolvable-as-posed delivery problem**, and that
the problem is located in a single functional group. PPARα full agonism requires a carboxylate
that makes a charge-assisted four-point hydrogen bond to Ser280/Tyr314/His440/**Tyr464**, and the
Tyr464 contact is on helix 12 itself — the carboxylate is not merely an affinity element, it is the
mechanical staple that locks AF-2 shut and creates the coactivator groove. That same carboxylate is
>99.99% ionised at pH 7.4, which costs roughly four orders of magnitude of permeant fraction, flips
the molecule into the MRP/BCRP efflux phenotype at the blood–retinal barrier, and parks it on
albumin's Sudlow site II. Worse, the two properties are **coupled rather than merely coexistent**:
every structural move that raised potency across this series (fenofibric acid → pemafibrate, ~10⁴–10⁵
fold) added lipophilic bulk to arms II/III, and that bulk is precisely the recognition element for
albumin site II and for OATP1B1-mediated hepatic uptake. Potency and tissue access are
**anti-correlated by construction** in the fibrate chemotype. Melatonin — the one compound in the
fifteen that satisfies every physicochemical criterion in disease-model §6.2 — proves the access
term is chemically achievable; it is just not achievable by an acid. The productive conclusions are
therefore (i) score the fibrates on *systemic* plausibility where no retinal transit is required,
(ii) stop optimising potency within the acid series, and (iii) if retinal PPARα engagement is
genuinely the goal, hop to a neutral head group and accept partial agonism — which, as §9 argues,
may also defuse the ANGPTL4 wrong-sign risk.

---

## 1. A correction to the brief's framing of the pharmacophore

The brief (STEP 2a) states that *"All Group A acids share an α,α-disubstituted aryloxy-isobutyric
acid motif."* Read against the SMILES, this is not accurate, and the inaccuracy is informative.

| ID | Compound | Acid head (from SMILES) | α-substitution | Chiral? |
|---|---|---|---|---|
| A1 | Fenofibric acid | `...Oc1ccc(...)cc1)C(=O)O` on `CC(C)(O-Ar)` | **α,α-gem-dimethyl** | no |
| A2 | Fenofibrate | same, as isopropyl ester | α,α-gem-dimethyl | no |
| A3 | **Pemafibrate** | `CC[C@@H](O-Ar)C(=O)O` | **α-ethyl, α-H — monosubstituted** | **yes, (R)** |
| A4 | Elafibranor | `OC(C)(C)C(=O)O` on 2,6-dimethylphenoxy | α,α-gem-dimethyl | no |
| A5 | **Seladelpar** | `OCC(=O)O` on a tolyl thioether | **unsubstituted aryloxy-acetic** | stereocentre elsewhere |
| — | Ciprofibrate | `CC(C)(O-Ar)C(=O)O` | α,α-gem-dimethyl | no |
| — | Gemfibrozil | `OCCCC(C)(C)C(=O)O` | gem-dimethyl but **homologated** (O is γ, not α) | no |

Three distinct heads, not one. And the pattern tracks isoform preference with striking regularity:

- **α,α-gem-dimethyl aryloxy-isobutyric → PPARα-preferring, weak** (fenofibric acid, ciprofibrate,
  clofibric acid, and the acid head of elafibranor).
- **α-monoalkyl, α-stereogenic 2-aryloxyalkanoic → SPPARMα, potent and highly α-selective**
  (pemafibrate).
- **Unsubstituted aryloxy-acetic with a thioether linker → PPARδ** (seladelpar; this is
  structurally the GW-501516/δ-agonist head, not a fibrate head).

**Why this matters for the run.** Seladelpar was carried as the "isoform falsification control."
The structure independently corroborates that assignment: it is a δ ligand *by chemotype*, not just
by label. That strengthens the control — if it scores at or above the α-selective agents on
DR-relevant mechanism, the result is not an artifact of mislabelling.

**Why gem-dimethyl exists at all** (three reasons, all structural):

1. **Thorpe–Ingold pre-organisation.** The quaternary α-carbon restricts rotation about Cα–O and
   Cα–C(=O), locking the carboxylate into the bioactive torsion and paying less conformational
   entropy on binding.
2. **Metabolic blockade — the dominant reason.** Acyl-CoA synthetase and the β-oxidation spiral
   require an α-CH. A quaternary α-carbon cannot enter β-oxidation, so the molecule is not consumed
   as the fatty-acid mimic it structurally resembles. This is why fibrates have ~20 h half-lives
   while their endogenous ligand analogues (linoleic acid, ALA, EPA) turn over in minutes to hours.
   Pemafibrate retains one α-H and correspondingly shifts to oxidative (CYP2C8/2C9) clearance —
   which is, as it happens, the profile you want in CKD.
3. **Acyl glucuronide detoxification.** Acyl glucuronides of carboxylic acid drugs undergo acyl
   migration to protein-reactive isomers (the idiosyncratic-hepatotoxicity mechanism for the
   profens). Migration rate falls steeply with α-branching. So the α,α-disubstituted fibrates make
   the *least* reactive glucuronides; pemafibrate's α-monosubstituted acid is intermediate;
   **seladelpar's unsubstituted aryloxyacetic acid is the most migration-prone head in the set** —
   a reactive-metabolite flag that nobody has raised for it.

---

## 2. (a) The fibrate pharmacophore: why the acid is required, and what it costs

### 2.1 Why the carboxylate is mechanically obligatory

The PPARα ligand-binding domain is a 13-helix α-helical sandwich enclosing a **Y-shaped (T-shaped)
cavity of ~1,300–1,400 Å³** — unusually large for a nuclear receptor, which is why it accepts
everything from a C18 fatty acid to a 36-heavy-atom SPPARMα.

**Arm I** is the polar sub-pocket, bounded by helix 3, helix 5, helix 11 and the **AF-2 helix
(H12)**. The agonist carboxylate sits there and makes a four-point, charge-assisted hydrogen-bond
network:

| Residue | Helix | Interaction with the ligand carboxylate |
|---|---|---|
| **Ser280** | H3 | O–H ··· ⁻O donor |
| **Tyr314** | H5 | phenol O–H ··· ⁻O donor |
| **His440** | H11 | imidazole Nε2–H ··· ⁻O donor |
| **Tyr464** | **H12 / AF-2** | phenol O–H ··· ⁻O donor — **this is the switch** |

Three points follow, and the third is the one the brief is asking about:

1. **The bonds are charge-assisted, so the anion is the binding species.** A neutral carboxylic acid
   can donate one H-bond; a carboxylate accepts four, each reinforced by the electrostatic field of
   the formal negative charge. Charge-assisted H-bonds are worth roughly 1.5–3 kcal/mol each against
   ~0.5–1.5 for neutral ones. Over four contacts that is a 4–8 kcal/mol difference — 10³–10⁶ in
   affinity. **The receptor does not want an acid; it wants a carboxylate.** This is why fenofibrate
   the isopropyl ester is pharmacologically inert at PPARα rather than merely weaker, and why the
   scout correctly calls it an *obligate* prodrug.
2. **Tyr464 is on H12, so the ligand physically staples AF-2 shut.** In the apo/antagonist state H12
   is mobile. Agonist binding anchors it in the "closed" position against H3/H11, and the closed H12
   together with H3 and H4 forms the hydrophobic cleft with the charge clamp (Lys292/Glu462) that
   reads the **LXXLL NR-box** of coactivators — NCOA1/SRC-1, NCOA2/TIF2, CREBBP/p300, PGC-1α. Note
   the blinded evidence file independently shows this: `ppara-interactions.tsv` records *"Linoleic
   acid promotes the reaction [PPARA protein binds to NCOA2 protein] | ... NCOA1 ... | ... CREBBP"*
   (PMID:19263263). That is the H12-clamp → coactivator-recruitment cascade, observed in the
   project's own data.
3. **Therefore the carboxylate is not an affinity handle you can trade away — it is the allosteric
   trigger for transactivation.** This is the single most important structural fact in the whole
   analysis, and it is the reason "just make it neutral" does not work naively. It is also the
   reason §9's escape route is *partial agonism / transrepression bias*, not full agonism with a
   neutral head.

### 2.2 What the permanent charge costs

Aryloxy-isobutyric acids have **pKa ≈ 3.0–3.5** (fenofibric acid ~3.1). The α-ether oxygen is
strongly electron-withdrawing by induction, pulling the pKa ~1.5 units below a simple aliphatic
gem-dimethyl acid — which is why gemfibrozil, whose ether oxygen is three carbons away, sits at
pKa ~4.7 instead.

At pH 7.4, Henderson–Hasselbalch gives:

```
log([A-]/[HA]) = pH - pKa = 7.4 - 3.1 = 4.3
→ neutral fraction ≈ 5 x 10^-5   (about 1 molecule in 20,000)
```

Five consequences, each structurally determined:

**(i) logD collapses.** aLogP 3.81 is the *neutral* species' partition coefficient. The species that
actually exists is the anion:
`logD7.4 ≈ logP − (pH − pKa) ≈ 3.81 − 4.3 ≈ −0.5`, floored in practice around 0 to +0.5 by ion-pair
partitioning. **The descriptor table in `ppar-class-drug-properties.tsv` reports `logd` as empty for
every row** — so any ranker reading `alogp` as a permeability proxy for these compounds is reading
the wrong number by four orders of magnitude. Worth stating explicitly; it is the single most
likely analytic error in this run.

**(ii) Desolvation dominates.** A carboxylate's hydration enthalpy is on the order of −80 kcal/mol.
Entering the hydrocarbon core of a bilayer (ε ≈ 2) requires shedding that shell. This, not size, is
why small acids are poor passive permeants while a larger neutral molecule like melatonin crosses
easily.

**(iii) The transporter phenotype flips.** At pH 7.4 these molecules stop being passive diffusers
and become organic-anion transporter clients:
- **Liver: a concentrating advantage.** OATP1B1/OATP1B3 (SLCO1B1/1B3) actively import lipophilic
  anions, producing hepatocyte concentrations far above plasma.
- **Retina: a concentrating *disadvantage*.** Per disease-model §6.1, the inner BRB endothelium and
  RPE express **ABCB1, ABCG2, ABCC1/4/5** — and the RPE's rich uptake set (MCT1/3/4, SLC19A1,
  SLC6A6, LAT1) contains **no OATP1B-family member**. The same anionic character that the liver
  reads as "import me" the BRB reads as "efflux me."
  This asymmetry is the whole ballgame, and it is a property of the functional group, not of any
  individual molecule.

**(iv) Albumin site II is purpose-built for this chemotype.** Sudlow site II (subdomain IIIA) is the
physiological carrier site for non-esterified fatty acids, bilirubin and other bulky lipophilic
anions. An aryl-substituted gem-dimethyl carboxylate with logP ~3.8 is close to the canonical site-II
ligand. Binding affinity at site II rises with lipophilicity — so **within this series, raising logP
to raise PPARα potency raises albumin affinity in lockstep.** Observed: fenofibric acid (logP 3.81)
~99% bound, fu ≈ 1%; pemafibrate (logP 5.55) >99.8% bound, fu ≈ 0.2%.

**(v) The exposure budget.** Assembling the terms (order-of-magnitude estimate, clearly labelled as
such, using the scout §6.1 numbers plus a generic CNS-barrier Kp,uu for an anionic efflux substrate):

```
fenofibric acid, 145 mg/day
  total plasma Cmax        ~30-45 uM
  x fu (~1%)               ~0.1-0.4 uM free in plasma
  x Kp,uu,retina (<=0.1, anionic MRP/BCRP substrate, no uptake carrier)
                           ~0.01-0.04 uM free in retinal interstitium
  vs PPARa EC50            ~20 uM (tens of uM)
  ---------------------------------------------------------------
  shortfall                ~10^3 fold
```

Two orders of magnitude of that is albumin plus weak potency, which the scout already quantified;
the third order is the barrier term, which is where the chemistry adds to the arithmetic. And this
is before accounting for the fact that PPARα is **intracellular**, so the anion must additionally
cross a plasma membrane to reach it.

### 2.3 The tension, stated formally

> The pharmacophore requires a **desolvated-on-binding anion** making four charge-assisted H-bonds
> to a buried polar sub-pocket. The barrier requires a **neutral, readily desolvatable** species.
> These are the same atom. No substituent change elsewhere on the molecule can decouple them.

Only three things can: separate the two requirements **in time** (a prodrug that is neutral in
transit and anionic at the receptor — §4), **in space** (hijack a carrier so passive permeability is
irrelevant — §4.4, §9.3), or **in chemotype** (abandon full agonism for a neutral partial
agonist/transrepressor — §9.2). Everything else is rearranging deck chairs.

---

## 3. (b) Pemafibrate versus fenofibric acid as structures

### 3.1 Parsing pemafibrate

`CC[C@@H](Oc1cccc(CN(CCCOc2ccc(OC)cc2)c2nc3ccccc3o2)c1)C(=O)O`

| Fragment | Identity | Role |
|---|---|---|
| `CC[C@@H](O–)C(=O)O` | (R)-2-aryloxy**butanoic** acid | Arm I head; α-ethyl, one α-H, single stereocentre |
| `Oc1cccc(...)c1` | **meta**-disubstituted phenoxy | central scaffold — note *meta*, not the fibrates' *para* |
| `CN(...)...` | benzylic CH₂ to a tertiary N | **the branch point that creates the Y** |
| `c2nc3ccccc3o2` | **benzoxazol-2-yl** on N | rigid planar bicycle into one hydrophobic arm |
| `CCCOc2ccc(OC)cc2` | 3-(4-methoxyphenoxy)propyl | flexible tether into the other arm |

So: a three-armed, Y-shaped ligand. Head into arm I, benzoxazole into one branch, methoxyphenoxypropyl
into the other. Fenofibric acid, by contrast, is linear and two-armed — acid head plus a single
4-(4-chlorobenzoyl)phenyl body.

### 3.2 What the extension buys

**Potency — and it is earned, not bulked.** The decisive test is ligand efficiency, which normalises
affinity by size:

```
LE = 1.37 x pEC50 / heavy atoms

fenofibric acid : pEC50 ~4.7 (20 uM) / 22 HA  -> LE ~0.29 kcal/mol/HA
pemafibrate     : pEC50 ~10  (0.1 nM) / 36 HA -> LE ~0.38 kcal/mol/HA
```

Pemafibrate is not merely larger; it is **more efficient per atom**. Adding 14 heavy atoms while
*raising* LE means those atoms are making real, complementary contacts in arms II and III — the
extension is designed, not accreted. Fenofibric acid occupies maybe a quarter of a 1,300 Å³ cavity;
pemafibrate fills it. That is the honest structural basis for the ~10⁵-fold potency gap.

**Selectivity — and it cannot come from the head.** The Ser/Tyr/His/Tyr quartet is near-identical
across isoforms (PPARγ: Ser289/His323/His449/Tyr473; PPARδ: Thr289/His323/His449/Tyr437). Arm I
therefore cannot discriminate. **>2,000-fold α-selectivity must be read out of arm topology**, and
pemafibrate's reader is the Y geometry itself:

- The branch angle is fixed by the tertiary nitrogen, and critically that nitrogen is **not a basic
  amine** — it is the exocyclic 2-amino nitrogen of a benzoxazole, so its lone pair is delocalised
  into the C2=N of the heterocycle (amidine-like). The N is flattened and the branch angle is
  *locked*. This is a genuine conformational-control trick: you get a rigid Y without a ring.
- The **benzoxazole** is planar, rigid, and presents one H-bond acceptor (ring N) plus a weak one
  (ring O) in a narrow slot. A bulkier or floppier group would clash; a flat bicycle threads.
- The methoxyphenoxypropyl arm is flexible enough to find the second channel but terminates in a
  small, polarisable methoxyaryl cap.

**Conclusion for (b), first half:** the extension buys potency through cavity filling at improving
ligand efficiency, and selectivity through locked three-dimensional branch geometry. Neither is
available to fenofibric acid, which is simply too small to read the cavity's shape.

### 3.3 What it costs — scored against disease-model §6.2

| §6.2 criterion | Target | Fenofibric acid | Pemafibrate |
|---|---|---|---|
| MW | <500, ideally <400 | **318.76 ✓** | 490.56 ✗ (marginal) |
| cLogP | ~2–4 | **3.81 ✓** | 5.55 ✗ |
| TPSA | <90 Å², ideally <70 | **63.60 ✓** | 94.26 ✗ |
| HBD | ≤2–3 | **1 ✓** | 1 ✓ |
| Rotatable bonds | ≤8 | **5 ✓** | **13 ✗✗** |
| Ionisation | neutral / weak base | ✗ (acid) | ✗ (acid) |
| Efflux liability | not P-gp/BCRP | ✗ (anion) | ✗✗ (large lipophilic anion) |
| PPB | <~98% | ✗ (~99%) | ✗✗ (>99.8%) |
| **Pass rate** | | **5 / 8** | **1 / 8** |
| Ro5 violations | 0–1 | **0** | 1 |
| QED | higher better | **0.85 — best in class** | **0.24 — worst in class** |

**Fenofibric acid is the best-shaped molecule in the entire PPARα class and it fails on exactly one
criterion: ionisation. Pemafibrate fails on five.** That is the cleanest statement of the trade.

The sleeper problem is **RTB 13**. Veber's rule caps at 10. Beyond the entropic cost (~0.5–1 kcal/mol
per rotor on binding), a highly flexible molecule presents a larger *effective* polar surface area in
water and pays a much bigger conformational-desolvation penalty at a membrane — which matters
disproportionately for a tissue like retina that must rely on passive transit because it has no
uptake carrier for this chemotype. For the liver, where OATP does the work, RTB 13 is nearly free.
**The flexibility penalty is paid only by the tissue you care about.**

### 3.4 Which features drive hepatoselectivity — and why they are inseparable from the potency

OATP1B1/1B3 substrate recognition has a well-characterised pharmacophore. Pemafibrate matches it on
every count, and matches it *because of the features that make it potent*:

| OATP1B recognition element | Pemafibrate's version | Also the reason it is potent/selective? |
|---|---|---|
| **Anionic group** (binding site is positively polarised; essentially all substrates are carboxylates/sulfates/glucuronides) | the 2-aryloxybutanoate | **Yes** — it is the arm-I head |
| **High lipophilicity on a large scaffold** (affinity rises with logP and molecular surface) | logP 5.55 over 36 heavy atoms | **Yes** — that bulk fills arms II/III |
| **Extended hydrophobic tail distal to the anion** (statin topology: acid head, big lipophilic body) | benzoxazole + methoxyphenoxypropyl arms | **Yes** — that is the Y |
| **Planar aromatic surface for π-stacking** | 4 aromatic rings | **Yes** |
| **No basic centre** (a cation would break recognition) | benzoxazol-2-ylamine N is non-basic by conjugation | **Yes** — the same conjugation locks the branch angle |

> **The central finding of §3.** Hepatoselectivity is not an independent design choice layered onto
> pemafibrate; it is the **direct, unavoidable consequence of the potency strategy within this
> chemotype.** A large lipophilic anion with an extended hydrophobic tail and no basic centre *is*
> an OATP1B substrate and *is* an albumin site-II ligand. You cannot build sub-nanomolar PPARα
> affinity this way and then ask the molecule not to go to the liver.

**Consequence for the pipeline.** Pemafibrate is simultaneously the only molecule potent enough to
ask "is PPARα agonism sufficient?" and the molecule least able to deliver an answer about the
retina. A negative retinal result with pemafibrate is **uninterpretable** — exactly as the scout
warned (§6.3) — and the structure explains *why* in a way the pharmacology alone does not: the
ambiguity is designed into the molecule.

**Free-drug comparison, both directions:**

```
                     fenofibric acid      pemafibrate
EC50 (PPARa)         ~20 uM               ~0.1-1 nM
plasma total Cmax    ~30-45 uM            ~15-30 nM
fu                   ~1%                  ~0.2%
free plasma          ~0.1-0.4 uM          ~0.03-0.06 nM
free / EC50          ~1/100 (2 logs short)  ~1/10-1/30 (1-1.5 logs short)
then x Kp,uu,retina  worse than baseline  WORSE STILL (bigger anion,
                                           higher efflux liability,
                                           hepatic first-pass sink)
```

Pemafibrate buys back roughly one order of magnitude of the plasma shortfall through potency — and
gives at least that much back at the barrier. **Net: a wash, achieved at the cost of QED 0.85 → 0.24.**

---

## 4. (c) Prodrug logic — three esters, three different jobs, none of them delivery

### 4.1 Fenofibrate — an isopropyl ester that solves a manufacturing problem

`CC(C)OC(=O)C(C)(C)Oc1ccc(C(=O)c2ccc(Cl)cc2)cc1`

| | Fenofibric acid (A1) | Fenofibrate (A2) | Direction |
|---|---|---|---|
| MW | 318.76 | 360.84 | up |
| aLogP | 3.81 | **4.68** | **up** |
| PSA | 63.60 | 52.60 | down |
| HBD | 1 | 0 | down |
| Ionised at 7.4 | >99.99% | **0%** | neutral |
| QED | **0.85** | 0.55 | **down** |

Note the direction of travel: the ester is **more lipophilic and less soluble** than the acid, not
more soluble. Its oral absorption is **dissolution-rate-limited with a large positive food effect** —
which is why micronised and nanocrystal formulations exist. **The ester does not improve absorption;
it creates the absorption problem.** The clinching evidence is in the data: the file also contains
**choline fenofibrate** (CHEMBL1201745), which is a *salt of the acid* — the exact opposite
physicochemical strategy — marketed specifically to remove the food effect the ester introduced. Two
marketed forms of one drug pointing in opposite directions is a strong signal that the ester was
never a permeability solution.

What it actually was: a crystalline, chemically stable, manufacturable, patentable form of an oily
acid, quantitatively cleaved by carboxylesterases. The project data confirms completeness —
`chembl_drug_metabolism.csv`: *FENOFIBRATE → FENOFIBRIC ACID, enzyme "Esterases", "more or less
completely converted into this metabolite."*

**Retinal verdict: no benefit, and structurally it cannot provide one.** The neutral species is
consumed presystemically; it never reaches systemic circulation in quantity, let alone the BRB.
**A prodrug cleaved before the barrier it was meant to cross is, for that barrier, not a prodrug.**

### 4.2 Icosapent ethyl — an ethyl ester that solves a purification problem, and costs absorption

`CC/C=C\C/C=C\C/C=C\C/C=C\C/C=C\CCCC(=O)OCC` — all-*cis*-5,8,11,14,17-EPA ethyl ester.
MW 330.51, aLogP **6.47**, PSA 26.30, HBD 0, **RTB 14**, Ro5v 1, **QED 0.21**.

What the ethyl ester does: (i) stabilises an autoxidation-prone oil into a distillable, purifiable
form — it is how you isolate ~96% single-species EPA out of a triglyceride fish-oil matrix; (ii)
changes the absorption route, and **for the worse**. Free fatty acids are absorbed directly; ethyl
esters require luminal pancreatic-lipase hydrolysis before micellar uptake, which is why EE
formulations have a pronounced fat-meal dependence and lower bioavailability than free-acid or
re-esterified-triglyceride forms. Again: **a pharmaceutical solution, not a delivery solution, and
it costs absorption.**

**But this is the one case with a genuine retinal route — and it is not the ester.** EPA does not
reach retina as free drug diffusing across a barrier. It is incorporated into plasma phospholipids
and lipoproteins and taken up by the retina's **physiological** lipid machinery: **MFSD2A** at the
inner BRB (which transports lysophosphatidylcholine esters of long-chain PUFA and is how the retina
acquires DHA), **ADIPOR1**-dependent retention, and FATP/CD36. Both MFSD2A and ADIPOR1 are in the
disease model's own target table (#52, P8.4). **Carrier-mediated uptake makes Lipinski irrelevant** —
which is exactly why QED 0.21 understates this compound and why it points straight at §4.4.

Liability to state plainly: **five bis-allylic CH₂ groups** (C–H BDE ~76 kcal/mol) make EPA
extremely peroxidisable, yielding 4-HNE-type aldehydes and F₃-isoprostanes. The disease model's P5
axis *is* oxidative/mitochondrial stress, and photoreceptor outer segments are already the most
PUFA-rich membranes in the body. Loading more peroxidisable PUFA into that tissue has a credible
wrong-sign limb absent adequate antioxidant status. Also: EPA is a weak, non-selective µM PPARα
ligand, so even perfectly delivered it is not a potent agonist.

### 4.3 Candesartan cilexetil — a cascade double ester that solves a steric problem

`CCOc1nc2cccc(C(=O)OC(C)OC(=O)OC3CCCCC3)c2n1Cc1ccc(-c2ccccc2-c2nn[nH]n2)cc1`

The benzimidazole-7-carboxylic acid is masked as a **1-(cyclohexyloxycarbonyloxy)ethyl** —
an (alkoxycarbonyloxy)alkyl double ester. Activation is a two-step cascade:

```
esterase cleaves the OUTER carbonate
   -> unstable 1-hydroxyethyl hemiacetal ester
   -> spontaneous chemical collapse, expelling acetaldehyde + cyclohexanol + CO2
   -> free candesartan carboxylic acid
```

**Why a double ester rather than a simple one?** Because a simple alkyl ester of a *hindered* aryl
carboxylic acid flanked by a fused benzimidazole is too hydrolytically stable — it would pass
through intact. The acyloxyalkyl design relocates the enzymatically cleaved bond away from the
hindered acid to an unhindered carbonate, then lets chemistry finish the job. This is the canonical
solution for hindered acids (pivampicillin, olmesartan medoxomil, and **tenofovir disoproxil
fumarate — also present in this very CSV**).

**A methodological warning for the ranker.** Candesartan cilexetil's descriptors — MW 610.67,
aLogP 6.32, PSA 143.34, **Ro5v 3**, **QED 0.14** — are the worst in the candidate set. They are also
*meaningless*, because they describe a molecule engineered to be destroyed during absorption.
Scoring QED 0.14 against this panel is a category error. Score the released candesartan
(MW 440.5, far better QED).

**Retinal verdict: no delivery benefit — but the exposure objection is much weaker here, for a
reason specific to the target.** Released candesartan is a **di**-anion at pH 7.4 (carboxylate
pKa ~4; tetrazole pKa ~4.9) at ~99.8% protein binding — strictly worse than fenofibric acid for
passive BRB transit. **However, AT1R is a cell-surface GPCR.** Candesartan never has to cross a
plasma membrane; it has to reach the retinal interstitium and bind an extracellular/transmembrane
site on endothelium, pericytes and Müller cells. This is a genuine and under-appreciated asymmetry:

> **The "acid cannot get in" objection is far more damaging to an intracellular nuclear-receptor
> target than to a cell-surface receptor target.** Fenofibric acid, pemafibrate and epalrestat all
> need to reach a *cytosolic or nuclear* protein. Candesartan does not. Same chemotype liability,
> materially different consequence.

Minor note: the cascade releases stoichiometric **acetaldehyde**. At 8–32 mg/day that is a few tens
of µmol — trivial, and I flag it only for completeness. Also relevant to §9: the **tetrazole** here
is a carboxylate bioisostere with pKa ~4.9 — i.e. an *acidity-preserving* isostere, which is the
wrong kind for our problem.

### 4.4 So: could a different prodrug strategy solve §2?

**First, the general diagnosis.** All three esters above are **absorption/formulation prodrugs
hydrolysed at or before the portal circulation**. None is a *distribution* prodrug. That is not an
accident of these three molecules — it is a fact about enzyme geography: carboxylesterases are
concentrated in gut wall (CES2), plasma (CES1/BChE, in rodents especially) and liver (CES1). Any
simple ester dosed orally is hydrolysed in the first tissue that matters, and the retina is the last
tissue that matters. **To reach retina, a prodrug must survive the liver — which means surviving the
best esterase organ in the body on the way to one of the worst.**

**Design brief for a retina-targeted PPARα prodrug:**

| Requirement | Target |
|---|---|
| Plasma stability | t½ > several hours against CES/BChE/PON1 |
| MW | < 450 (so the promoiety must be small) |
| cLogP | 2–4 (neutral species) |
| TPSA | < 70 Å² |
| HBD | ≤ 1 |
| RTB | ≤ 8 |
| Charge at 7.4 | neutral |
| Efflux | not a P-gp/BCRP substrate |
| Cleavage | competent in retina, ideally biased there |

**A species-translation trap to flag up front:** human plasma essentially lacks CES1/CES2, whereas
rodent plasma is rich in both. A prodrug that is beautifully stable in human plasma will be
annihilated in rat. **The preclinical model will systematically mislead in the pessimistic
direction** — and the converse (a prodrug that survives rat plasma may be over-stabilised for human
use). Any ester-prodrug programme here must run human-plasma and human-hepatocyte stability first.

**Four concrete designs, ranked:**

**(i) Hindered simple ester of fenofibric acid — the cheap shot. Verdict: fails.**
Swap isopropyl for neopentyl, 1-adamantyl, *tert*-butyl or cyclopropylmethyl to slow hydrolysis.
Resulting profile: MW ~360–400, neutral, cLogP 4.5–5.5, TPSA ~52, HBD 0, RTB 6–8. Fails on **cLogP**
(membrane and melanin trapping in RPE/choroid, very high PPB) and fails on **cleavage selectivity** —
hepatic CES1 still takes most of it on first pass, and there is no reason the retina would be
favoured. You would also be dosing a *more* lipophilic molecule into a melanin-rich tissue, which
produces an unpredictable depot rather than free drug (disease-model §6.1). **Marginal at best.**

**(ii) Carboxylate bioisostere instead of a prodrug. Verdict: mostly a dead end, with one exception.**
The honest problem: **almost every COOH bioisostere was invented to *preserve* acidity**, because
most acid drugs need the charge. Running the pKa table against our requirement (raise pKa toward 7):

| Isostere | pKa | Neutral fraction at 7.4 | Verdict |
|---|---|---|---|
| Carboxylic acid | 3.1 | 0.005% | baseline |
| Tetrazole | 4.9 | 0.3% | **wrong direction** |
| Acylsulfonamide | 4.5 | 0.1% | **wrong direction** |
| Squaric acid | <2 | ~0 | **wrong direction** |
| 3-Hydroxyisoxazole | 5–6 | 1–3% | marginal gain |
| **1,2,4-Oxadiazol-5(4H)-one / 3-hydroxy-1,2,4-oxadiazole** | **6–7** | **3–20%** | **best option — see §9.1** |
| Hydroxamic acid | ~9 | >97% | charge solved, but metallophilic off-targets (HDAC/MMP), Lossen-rearrangement genotoxicity flag, hydrolytic lability |

**(iii) Transporter-hijacking prodrug — the structurally specific route.** Carrier-mediated uptake
makes passive permeability irrelevant, so Ro5/TPSA stop applying. The retina's exploitable carriers
(disease-model §6.1) are MCT1/3/4, SLC19A1, SLC6A6, LAT1 at the RPE, and **MFSD2A** at the inner BRB.

- **LAT1 conjugate.** Attach the fibrate acid to a phenylalanine/tyrosine-like promoiety so the
  conjugate reads as a large neutral amino acid. Precedent exists (L-dopa, melphalan, gabapentin;
  ketoprofen–amino-acid conjugates show brain uptake). **Problem:** LAT1's pharmacophore requires a
  free α-amino-acid motif next to a *small-to-medium* lipophilic side chain. A fenofibroyl group is
  a very large side chain, and LAT1's tolerance is limited. The conjugate is also zwitterionic, so
  if transport fails you have made things strictly worse. *Moderate plausibility.*
- **MFSD2A / lysophosphatidylcholine conjugate — the best idea in this section.**
  MFSD2A at the inner BRB transports **LPC esters of long-chain fatty acids** and is the
  physiological route by which the retina acquires DHA. Design: an **sn-2 fibroyl (or short-linker
  fibrate) lysophosphatidylcholine**. The retina imports it via its own DHA pathway; intracellular
  phospholipase A2 — abundant, and **PLA2G4A is target #56 in the disease model's own panel** —
  liberates the free acid *inside the cell*, which is exactly where the nuclear receptor is. The
  design converts the problem "get an anion across a membrane" into "get a lipid onto a lipid
  carrier," which the retina already does every day. Properties look terrible by Ro5 (MW ~650,
  zwitterionic phosphocholine head) — **and that is fine, because Ro5 does not govern carrier
  uptake.**
  *Risks, stated honestly:* LPC conjugates are cleared fast by plasma LCAT/lysophospholipases;
  MFSD2A's acyl-chain tolerance for a rigid aryl ketone rather than a flexible polyene is genuinely
  unknown and could be zero; and delivery would hit every MFSD2A tissue (brain, placenta), so
  reproductive toxicology would be an early gate. **Speculative — but it is the only option in this
  whole analysis that is both structurally specific and matched to a carrier the retina
  demonstrably has.** Note also that it is the same logic by which icosapent ethyl's EPA gets in
  (§4.2), so there is a working precedent in the candidate set itself.
- **Amidase-cleaved promoiety.** There is no esterase meaningfully enriched in retina over liver —
  say so plainly rather than pretending. But the retina does express **FAAH/NAAA**, and a
  fatty-acid-*amide* promoiety (N-acylethanolamine-like) is a more retina-competent handle than a
  plain ester and is markedly more plasma-stable. "Retina-selective" would be overclaiming;
  **"plasma-stable and retina-competent" is the achievable target**, and it is enough.

**(iv) The honest alternative: do not fix §2 — change the goal.**
If the operative mechanism is systemic lipoprotein lowering (disease-model §5.2b; scout §7), then no
retinal exposure is required, the target organ is the liver, and **everything that looks like a
defect becomes a feature**: pemafibrate's hepatoselectivity is correct targeting, and fenofibric
acid's QED 0.85 with decades of chronic-use data is a well-built molecule aimed at the right organ.
**Structural analysis genuinely cannot adjudicate between the systemic and retina-intrinsic
framings.** What it *can* do — and this is my deliverable to the ranker — is say which molecule wins
under each:

| If the mechanism is… | Structurally correct choice | Why |
|---|---|---|
| Systemic lipid/lipoprotein lowering | **Fenofibric acid / choline fenofibrate** | Liver is the target organ, OATP delivers it there, QED 0.85, Ro5v 0, once-daily, cheap. Renal elimination is the one liability. |
| Systemic, in a CKD population | **Pemafibrate** | Same logic, hepatobiliary clearance, no CKD dose adjustment |
| Retina-intrinsic PPARα engagement | **None of the fifteen** | Every direct agonist here is an anion against an intracellular receptor behind an effluxing barrier with no uptake carrier. This requires new chemistry (§9). |

---

## 5. (d) The natural-product set

**Data note:** `chembl_natural_products.csv` in the blinded directory is a **26-row test extract**
(consistent with `data-quality-findings.md`). Linoleic acid, α-linolenic acid, linalool and quercetin
have **no descriptor rows anywhere in the blinded ChEMBL tables**. Descriptors below are therefore
general medicinal-chemistry knowledge, explicitly flagged as such per the blinding protocol §3 —
not project data. Only melatonin (CHEMBL45) and icosapent ethyl (CHEMBL2095209) have data-backed rows.

| Compound | MW | logP | PSA | HBD | RTB | est. QED | Ro5v | Source |
|---|---|---|---|---|---|---|---|---|
| Linoleic acid | 280.4 | ~7.0 | 37.3 | 1 | 14 | ~0.35 | 1 | knowledge |
| α-Linolenic acid | 278.4 | ~6.5 | 37.3 | 1 | 14 | ~0.35 | 1 | knowledge |
| Linalool | 154.25 | ~3.3 | 20.2 | 1 | 4 | ~0.50 | 0 | knowledge |
| Quercetin | 302.24 | ~1.5 | **131.4** | **5** | 1 | ~0.44 | 1 | knowledge |
| Melatonin | **232.28** | **1.86** | **54.12** | 2 | 4 | **0.84** | **0** | **data** |
| Icosapent ethyl | 330.51 | **6.47** | 26.30 | 0 | **14** | **0.21** | 1 | **data** |

### 5.1 Linoleic acid (18:2 n-6)

**Structure:** `CCCCC/C=C\C/C=C\CCCCCCCC(=O)O` — all-*cis*, two bis-allylic CH₂.

**The disqualifying argument is pharmacological, not toxicological, and it is purely structural:**
linoleic acid is an *endogenous* ligand present in plasma at tens of µM as NEFA (millimolar
esterified). Its PPARα EC50 is in the same µM range. **You cannot agonise a receptor with a molecule
that already saturates it at physiological concentration.** Supplementation shifts the fatty-acid
*ratio* marginally; it does not shift receptor occupancy. This applies to the entire endogenous
fatty-acid class and is the reason the scout's §5.2(g) "trivially expected fatty-acid binding"
observation is correct — the blinded data's strongest PPARA binding evidence is for molecules that
cannot be drugs *because* they are already there.

**Wrong-sign risk, specific to this disease.** n-6 linoleate is the precursor of arachidonate
(Δ6-desaturase → elongase → Δ5-desaturase). Arachidonate is the substrate for **ALOX12/ALOX15**
(target #59, 12/15-HETE → pericyte loss, Müller ER stress — the model marks this **KO-validated,
"P (strong)"**) and **PTGS2** (#57, PGE2 → permeability, VEGF induction). **Dosing an n-6 precursor
into a disease whose P8.6 module is driven by n-6 eicosanoids has an explicit, mechanistically
specific wrong-sign limb.** No other agent in this pipeline will reach that from structure alone.

**Assay liabilities:** C18 fatty acids are classic colloidal aggregators/detergents above their CMC
(tens of µM for soaps) — they nonspecifically inhibit enzymes and perturb membranes. Many
"binds to and increases activity of PPARA" reporter rows sit at or above CMC. Two bis-allylic
positions make it peroxidisable. **PAINS:** no catalogued substructure alert, but a well-known
frequent-hitter *mechanism*.

**Verdict: not a drug. Score 2.**

### 5.2 α-Linolenic acid (18:3 n-3)

Everything above applies, with two differences in opposite directions.

**Favourable:** the n-3 series leads to EPA/DHA, and DHA is the retina's signature lipid (ELOVL4 #51,
ADIPOR1 #52 — both **Mendelian/genetically validated** in the model's table). Direction is right.

**Unfavourable, and decisive:** human Δ6-desaturase conversion is **~5–8% ALA→EPA and <0.5%
ALA→DHA**. **ALA is therefore a prodrug with a sub-1% yield for the species you actually want** —
and icosapent ethyl, sitting in the same candidate set, delivers the intended species directly. On
pure structural logic, carrying both and preferring ALA would be indefensible. ALA also has **three**
bis-allylic positions versus linoleate's two, making it the more peroxidisable of the pair.

**Verdict: dominated by B4 on the same axis. Score 2.**

### 5.3 Linalool

**Structure:** `CC(C)=CCCC(C)(O)C=C` — 3,7-dimethylocta-1,6-dien-3-ol, an acyclic monoterpene
**tertiary allylic alcohol**.

**The paper profile is the best in Group B:** MW 154, neutral, PSA 20.2, HBD 1, RTB 4, Ro5v 0. It
would cross the BRB without difficulty. This is the only Group B compound with favourable access.

**But it cannot be potent, and this is a hard physical argument.** Linalool has **15 heavy atoms**
against a ~1,300 Å³ pocket. Even at an exceptional ligand efficiency of 0.4 kcal/mol/HA:

```
pEC50_max = (0.4 x 15) / 1.37 = ~4.4  ->  EC50 ~40 uM
```

**There is not enough molecule to generate meaningful affinity**, regardless of what the single CTD
row says. (The row — *"linalool binds to and results in increased activity of PPARA protein"*, with
a PPARA-mutant susceptibility observation — is one of the better-controlled entries in the file, and
I am not disputing that it binds. I am saying binding at 15 heavy atoms means weak binding.)

**Liabilities:** volatile (vapour pressure ~0.1 mmHg at 25 °C) — a real formulation and
dose-reproducibility problem. The **tertiary allylic alcohol autoxidises in air to linalool
hydroperoxides and epoxides**, which are well-characterised **contact sensitisers** (among the
highest-ranked fragrance allergens in European patch-test series) and are reactive electrophiles that
will confound assays run on aged stock. Rapid glucuronidation and first-pass clearance. And the
project's own evidence row specifies **"Linalool, (+/-)-"** — a racemate, so the data does not even
identify which enantiomer binds.

**PAINS:** no catalogued alert for linalool itself; the autoxidation products are the concern.

**Verdict: score 2 as a candidate. But keep it as a structural existence proof** — a small, neutral,
BRB-permeant terpenoid alcohol does engage this pocket. That matters for §9.

### 5.4 Quercetin — the frequent-hitter control, and it earns the title

**Structure:** `O=c1c(O)c(-c2ccc(O)c(O)c2)oc2cc(O)cc(O)c12` — 3,5,7,3',4'-pentahydroxyflavone.

Three structural features drive everything:
1. **Catechol B-ring** (3',4'-dihydroxy)
2. **Two chelation pockets**: 3-OH/4-keto and 5-OH/4-keto
3. **Full planar conjugation** through C2=C3 into both rings

**PAINS status:** quercetin matches the **`catechol_A`** PAINS filter and appears on essentially
every published frequent-hitter list. Six distinct interference mechanisms, all structural:

1. **Redox cycling.** The catechol (E°' ~0.33 V) oxidises to semiquinone then ***ortho*-quinone**,
   reducing O₂ and generating **tens of µM H₂O₂ in standard culture medium over hours**. Many
   "quercetin is antioxidant/protective" and "quercetin modulates NFE2L2" results are H₂O₂-mediated
   hormesis. Note the irony: this *is* a real NRF2 mechanism — H₂O₂ and the quinone both modify
   KEAP1 cysteines — but it is the signature of a redox-cycling catechol, not of specific ligand
   pharmacology.
2. **Latent covalent electrophile.** The *o*-quinone is a Michael acceptor forming adducts on protein
   cysteines and depleting GSH. Same chemistry as dimethyl fumarate, but **generated in situ and
   wholly non-selective**.
3. **Metal chelation.** Both keto-enol pockets bind Fe³⁺/Cu²⁺ avidly. This produces genuine Fenton
   suppression, *and* assay interference by stripping metal cofactors from metalloenzymes — note
   **MMP9 is in quercetin's own 26-target list**, and MMP9 is a zinc metalloproteinase — *and* a
   pro-oxidant mode with free copper.
4. **Colloidal aggregation.** Planar, poorly soluble, logP ~1.5 → aggregates at 10–50 µM that
   nonspecifically sequester and inhibit enzymes. This is the commonest source of false positives in
   exactly the µM screens that generate CTD rows.
5. **Optical interference.** Strong absorbance near 370 nm plus intrinsic weak fluorescence —
   quenches and distorts the fluorogenic readouts most of these assays use.
6. **ATP-pocket promiscuity.** The flavone scaffold is a canonical ATP-competitive kinase hinge
   binder (the chemotype that gave quercetin → genistein → LY294002). Broad, real, and unselective.

**ADME — the aglycone is not the circulating species.** Five phenolic OH groups mean extensive
presystemic **UGT1A/SULT1A** conjugation in enterocyte and liver, plus **COMT** O-methylation of the
catechol to isorhamnetin. Oral bioavailability <2% (scout §3.2). **What circulates is
quercetin-3-glucuronide, quercetin-3'-sulfate and isorhamnetin — anionic, high-PSA, BRB-excluded.**
The blinded evidence file says this out loud without meaning to: `ppara-interactions.tsv` carries a
separate row for **"quercetin 3-O-glucuronide."** The data knows the circulating species is a
different molecule from the one in the assays.

**Is the 26-target profile designed polypharmacology or an annotation artifact? — Artifact, with a
small genuine core.** Four lines of evidence:

- **Rank tracks study volume.** 745 CTD rows, more than the next two compounds combined (scout §3.1).
  Ascorbic acid scores 23 targets and D-fructose 21 in the same table. That is bibliometrics.
- **The action ratio is 0.35** (9 of 26 targets have an action string). It is the *best* in the set —
  so there is a real core — but 17 of 26 are expression associations.
- **The surviving targets are not 26 independent pharmacologies; they are ~3 programmes read out
  many ways.** NFE2L2↑ / CAT↑ / SOD2↑ is **one** event. NFKB1↓ / TNF↓ / IL6↓ / IL1B↓ / ICAM1↓ is
  **one** event (and is downstream of the first). BAX / BCL2 / CASP3 is **one** event (downstream of
  both). Collapse the redundancy and quercetin has roughly **three** mechanisms, two consequent on
  the first — which is precisely the signature of a redox-cycling catechol. **Breadth here is a
  reason to discount, not to celebrate.**
- **Direction-incoherence at the focus target.** Its only *action-level* PPARA row is
  *"Quercetin inhibits the reaction [GW 7647 results in increased activity of PPARA protein]"*
  (PMID:18393431) — i.e. **antagonism of a reference PPARα agonist** — while its other rows are
  "prevents the decrease in PPARA mRNA caused by streptozocin/fructose/dietary fat." Those are
  different assays measuring different things, and the one that measures *activity* points the wrong
  way.

Disease-brief §4 independently penalises "antioxidant as the sole mechanism" and "promiscuous
polyphenols without a specific mechanistic argument." Quercetin is the archetype of both.

**Verdict: score 2.** Correctly carried as the frequent-hitter control; it performs that role well.

### 5.5 Icosapent ethyl — covered in §4.2

**Score 4** — the only Group B entity with a real, carrier-mediated route into retina and an approved
product behind it, against an ester that costs absorption, QED 0.21, RTB 14, weak non-selective µM
PPARα activity, and a genuine peroxidation liability in the most PUFA-rich and most
oxidatively-stressed tissue in the body.

---

## 6. (e) Melatonin as the exposure control

**Structure:** `COc1ccc2[nH]cc(CCNC(C)=O)c2c1` — *N*-acetyl-5-methoxytryptamine.
**Data-backed descriptors (CHEMBL45):** MW **232.28**, aLogP **1.86**, PSA **54.12**, HBA 2, HBD 2,
RTB 4, aromatic rings 2, heavy atoms 17, **Ro5v 0**, **QED 0.84**.

### 6.1 Why it crosses when the fibrate acids do not — six structural reasons

1. **No ionisable group anywhere in the physiological window.** The indole N–H is an extremely weak
   acid (pKa ~17); the amide N–H is non-acidic and the amide nitrogen is non-basic (lone pair
   delocalised into C=O, pKaH ≈ −1); the aryl methyl ether is neutral. **Melatonin is >99.99%
   neutral at pH 7.4 — the exact complement of fenofibric acid's >99.99% ionised.** Therefore
   **logD7.4 = logP = 1.86**, with no pH-partition penalty at all. Fenofibric acid's logD is ~−0.5
   from a logP of 3.81. *The more lipophilic molecule is the one that cannot cross.*
2. **It satisfies every §6.2 criterion simultaneously — the only compound in the fifteen that does.**

   | §6.2 criterion | Target | Melatonin | Pass |
   |---|---|---|---|
   | MW | <400 | 232.28 | ✓ |
   | cLogP (= logD here) | ~2–4 | 1.86 | ✓ (just under, but neutral) |
   | TPSA | <70 Å² | 54.12 | ✓ |
   | HBD | ≤2–3 | 2 | ✓ |
   | RTB | ≤8 | 4 | ✓ |
   | Ionisation | neutral | neutral | ✓ |
   | Efflux | not P-gp/BCRP | small, flat, HBA 2 — outside recognition space | ✓ |
   | PPB | <98% | ~50–60% | ✓ |
   | | | | **8 / 8** |

3. **Not an efflux substrate.** P-gp recognition correlates with MW >400, HBA-rich, amphiphilic and
   often basic character. Melatonin at MW 232 with HBA 2 and no basic centre is simply not in the
   recognition space. BCRP liability likewise low.
4. **Protein binding ~50–60% → fu ≈ 40–50%.** That is **~45× fenofibric acid's free fraction and
   ~225× pemafibrate's.** This single number carries most of the exposure difference, and it is a
   direct consequence of having no anionic group for albumin site II to grip.
5. **Amphipathic balance in the "crosses and leaves again" band.** The methoxyindole is a flat,
   modestly lipophilic plate; the *N*-acetylethylamine tail supplies two H-bond-capable groups that
   maintain aqueous solubility. logP ~1.9 partitions into a bilayer *and back out*. Contrast
   pemafibrate at logP 5.55: even if it were neutral it would partition into membranes and into
   RPE/choroidal melanin and stay there (disease-model §6.1 on melanin as a double-edged depot).
6. **The retina handles it natively.** Photoreceptors express AANAT/ASMT and synthesise melatonin
   locally; MT1/MT2 are present. The tissue has endogenous handling for this exact molecule.
   *(Physiology, not drug-indication knowledge — permitted under blinding §3.)*

### 6.2 What this implies for affinity versus access

Retinal receptor occupancy is a product, not a potency:

```
Occupancy ~ ( fu x C_plasma,total x Kp,uu,retina ) / EC50
```

| | Fenofibric acid | Pemafibrate | Melatonin |
|---|---|---|---|
| EC50 at its primary target | ~20 µM (PPARα) | ~0.1–1 nM (PPARα) | low nM (MT1/MT2) |
| fu, plasma | ~1% | ~0.2% | **~40–50%** |
| Ionised at 7.4 | >99.99% | >99.99% | **<0.01%** |
| §6.2 criteria passed | 5/8 | **1/8** | **8/8** |
| Kp,uu retina (est.) | low — efflux substrate, no uptake carrier | **lowest** — efflux + hepatic sink | **~1** — free diffusion |
| QED | 0.85 | **0.24** | 0.84 |

**The pipeline-level finding.** Going from fenofibric acid to pemafibrate improved the **denominator
by 4–5 logs** and simultaneously **degraded every term in the numerator**: fu fell 5-fold
(1% → 0.2%), and Kp,uu fell further still because hepatoselective OATP uptake was *deliberately
engineered in*. You cannot out-run a multi-log access deficit with a potency gain when the potency
gain is itself *causing* part of the deficit (§3.4). **Within this chemotype, potency and access are
not merely in tension — they are anti-correlated by construction.**

Melatonin makes that legible by holding the access term at its ceiling. Its own weakness is the exact
mirror image: **near-perfect access to a target whose engagement may not be the mechanism that
matters.** Its high-affinity pharmacology (MT1/MT2, low nM) is real and reachable at oral doses; but
most of the 19-target CTD breadth is radical-scavenging and antioxidant activity requiring **µM–mM**,
which oral dosing does not reach, and disease-brief §4 explicitly penalises antioxidant-only
mechanisms. Its PPARA evidence is the weakest class in the file (cisplatin-protection expression
rows only — I read them; they are not engagement).

> **So the correct conclusion is not "melatonin is the drug." It is: the access term is achievable by
> chemistry in this disease — just not by this chemotype — and the PPARα programme has not solved
> it.** That is what sets up §9, and it is the single most useful thing structure contributes to this
> run.

---

## 7. (f) Structural alerts across the full set

### 7.1 Elafibranor — the chalcone enone (flag, but calibrate)

`CSc1ccc(C(=O)/C=C/c2cc(C)c(OC(C)(C)C(=O)O)c(C)c2)cc1`

An **(E)-chalcone**: aryl ketone conjugated to a *trans*-alkene conjugated to a second aryl ring.
A genuine Michael acceptor — but a **moderate** one, and the structure says why:

- Both termini are aryl-conjugated, delocalising the LUMO and reducing β-carbon electrophilicity.
- The β-carbon bears a **2,6-dimethylphenyl**. *Ortho,ortho*-dimethyl substitution twists that ring
  out of conjugation **and** places two methyls directly flanking the attack trajectory. This is
  substantial steric shielding at the reactive position.

So: a slow, largely reversible thiol-adduct former, not a covalent warhead. Consequences anyway:
GSH depletion on chronic dosing; **plausible KEAP1 cysteine modification — meaning elafibranor may
carry an NRF2 limb confounding its PPAR pharmacology**, which nobody has flagged and which matters
because D2 (dimethyl fumarate) is in this set specifically to test the NRF2 node; haptenation /
idiosyncratic hepatotoxicity risk; and **PAINS: chalcones are a catalogued frequent-hitter class**
(`ene_one_ene_A` family).

Two further structural notes:
- Its known **active metabolite is the alcohol reduction product of this ketone** — reduced by
  carbonyl reductases and aldo-keto reductases. Note that **AKR1B1, epalrestat's target in this very
  set, is an aldo-keto reductase**; the chalcone ketone is the kind of substrate AKRs act on. A
  mechanistic cross-link worth one line.
- The **thioether (S-Me)** is an FMO/CYP S-oxidation soft spot → sulfoxide/sulfone, a metabolic
  liability and a possible reactive-metabolite source.

Descriptors: aLogP 5.16, PSA 63.60, RTB 7, Ro5v 1, QED 0.41. Acid head unchanged, so all of §2
applies in full. **For chronic lifelong dosing in a polypharmacy population, a reactive-ish chalcone
is the wrong starting point.**

### 7.2 Dimethyl fumarate — thiol reactivity, and a prodrug paradox inverse to fenofibrate's

`COC(=O)/C=C/C(=O)OC`. MW 144.13, aLogP −0.11, PSA 52.60, HBD 0, Ro5v 0, QED 0.40.

A ***trans*-1,2-diester-activated alkene — a deliberate, highly reactive Michael acceptor**, far more
electrophilic than the chalcone because *both* β-carbons are ester-activated with no aryl
delocalisation and no steric shielding whatsoever.

**The paradox.** DMF is >99% consumed by glutathione in gut and plasma before reaching circulation.
The circulating species is **monomethyl fumarate (MMF — CHEMBL589586, also in the blinded file:
MW 130.10, aLogP −0.20, PSA 63.60, QED 0.41)**, which is a **carboxylic acid** and a much weaker
electrophile. But the KEAP1 Cys151 succination mechanism requires the *diester*; MMF succinates
poorly.

> **Fenofibrate's prodrug paradox inverted:** for fenofibrate the metabolite is active and the parent
> inert; for DMF **the parent is the active species and the "metabolite" largely is not** — yet the
> metabolite is what circulates. This is why there is a live, unresolved argument about whether DMF's
> effects are KEAP1-mediated at all, versus GSH-depletion hormesis, HCAR2/GPR109A agonism by MMF, or
> GAPDH succination. **For this pipeline that matters directly: "NRF2 activator" may not be what DMF
> is.** D2 was carried to test the Nrf2 limb cleanly; structurally it does not test it cleanly.

**Selectivity:** fumarate succinates many cysteines — GAPDH Cys152 (inhibiting glycolysis), IRAK4,
PKCθ, STING, NLRP3. Broadly immunomodulatory by cysteine promiscuity; hence lymphopenia and PML risk.

**A DR-specific structural concern no other agent will reach.** Thiol-reactive electrophiles consume
GSH. The diabetic retina's **P1 polyol pathway drains NADPH** (AKR1B1 consumes it reducing glucose to
sorbitol), and **NADPH is required to regenerate GSH from GSSG via glutathione reductase**. The
tissue is therefore in a pre-existing NADPH/GSH deficit *by the disease's own mechanism*. **Dosing a
fast, promiscuous thiol electrophile into a tissue whose GSH regeneration capacity is already
compromised is a plausible wrong-sign interaction** — the hormetic window could be narrower in
diabetic retina than anywhere this drug has been used.

**Access:** excellent for the parent (MW 144, neutral, PSA 52.6) and largely illusory in practice,
because the parent is consumed presystemically and MMF is an anion with the §2 problem.

### 7.3 Minocycline — chelation, melanin, and a chromophore in an illuminated organ

`CN(C)c1ccc(O)c2c1C[C@H]1C[C@H]3[C@H](N(C)C)C(O)=C(C(N)=O)C(=O)[C@@]3(O)C(O)=C1C2=O`
MW 457.48, aLogP 0.19, **PSA 164.63**, HBD 5, HBA 9, RTB 3, QED 0.40, 5 stereocentres.

**First, a caveat on the rubric itself.** PSA 164.6 is **nearly double** the <90 Å² BRB threshold,
HBD 5 is at the Lipinski ceiling, and the molecule is **zwitterionic** at pH 7.4 (dimethylamino pKa
~7.8 and ~9.5; phenolic-diketone/tricarbonylmethane pKa ~3.3 and ~7.8). By disease-model §6.2 it
should not cross. **Yet minocycline is the tetracycline with real CNS penetration.** The structural
reason: it is the **most lipophilic tetracycline**, because 6-deoxy-6-demethyl removes both an HBD
and a polar centre while 7-dimethylamino adds lipophilic bulk — giving it a far larger accessible
*neutral-tautomer / neutral-zwitterion* population than tetracycline. **This is the one molecule in
the set where the 2D descriptor rubric is simply wrong, and the reason is tautomer and
zwitterion-neutral-species availability, which 2D descriptors do not capture.** Flagging this for the
ranker: do not mechanically penalise minocycline on PSA.

**Chelation.** Two classic bidentate metal-binding motifs: the BCD-ring **β-diketone /
tricarbonylmethane** (C11–C12–C12a enol) and the A-ring **amide–enol**. Consequences:
(i) Ca²⁺/Mg²⁺/Fe²⁺/Al³⁺ binding → the food/antacid/iron absorption interaction and bone/tooth
deposition; (ii) **its MMP9 activity *is* Zn²⁺ chelation**, not a designed active-site interaction —
so it is low-potency and non-selective across the metzincins, and the ranker should discount
"inhibits MMP9" accordingly; (iii) Fe-chelates are redox-active.

**Photo-oxidation — and this is my strongest independent objection in Group D.** The extended
enolised polyketide chromophore absorbs in the near-UV/visible. Tetracyclines are classic phototoxins.
Minocycline's basic amines and its oxidation products bind **melanin** avidly, and the well-known
blue-black scleral and dermal pigmentation of long-term minocycline is the clinical readout of
exactly this chemistry: melanin/iron-chelate deposition of photo-oxidation products.

> **The retina is the only tissue in the body that is deliberately and continuously illuminated, and
> the RPE/choroid behind it is the body's densest melanin depot.** Chronically dosing a near-UV/visible
> chromophore that photo-oxidises, into a melanin-rich, light-exposed tissue, for a lifelong
> indication, is close to a worst-case structural profile. This argues for scoring minocycline well
> below where its microglial/neuroprotective mechanism alone would place it.

Also: C4 epimerisation under acid gives 4-epi-minocycline, and anhydro/epianhydro degradation products
are nephrotoxic — a stability liability in a renally-impaired population. And note the coupling once
again: the vestibular toxicity tracks the lipophilicity/CNS penetration that is the *reason* the drug
reaches retina. **Access and liability are the same property.**

### 7.4 Epalrestat — the rhodanine, and why the PAINS flag is only half right

`CC(/C=C1\SC(=S)N(CC(=O)O)C1=O)=C\c1ccccc1`
MW 319.41, aLogP 2.92, PSA 57.61, HBD 1, RTB 4, Ro5v 0, **QED 0.68**, 1 aromatic ring.

**Substructure:** a **2-thioxo-1,3-thiazolidin-4-one (rhodanine)** carrying a **5-arylidene**
exocyclic alkene and an **N-acetic acid**, with a second exocyclic alkene extending to phenyl — a
cross-conjugated diene with defined (Z/E) geometry.

**Rhodanines are the canonical PAINS class** — explicitly flagged by Baell & Holloway, with an
extensive "rhodanines: problematic compounds in drug discovery" literature. The liabilities are all
structural:
1. The **5-arylidene exocyclic alkene is conjugated to both the C4 carbonyl and the C2
   thiocarbonyl** — doubly activated, genuinely electrophilic; thiol addition and retro-Michael are
   documented.
2. The **thiocarbonyl (C=S)** is soft, thiophilic and metal-chelating.
3. Planar extended conjugation + poor solubility → **colloidal aggregation**.
4. Strong visible/near-UV absorbance — rhodanines are literally used as dyes → **optical assay
   interference**.
5. **Photoisomerisation** of the exocyclic alkene (the SMILES specifies a defined geometry) —
   and once again, this is a chromophore being proposed for chronic dosing into an illuminated organ.
6. Frequent hits across unrelated target classes.

**The honest counterweight, which is what a chemist is for.** Epalrestat is a marketed drug with a
**mechanistically coherent, structure-based** story at AKR1B1: aldose reductase has a large
lipophilic **"specificity pocket"** that opens to accommodate exactly this kind of flat hydrophobic
arylidene, and the **N-acetic acid carboxylate binds the AKR1B1 anion site** (Tyr48 / His110 /
Trp111, adjacent to the NADP⁺ nicotinamide) — the shared pharmacophore of every carboxylic-acid ARI
(tolrestat, zopolrestat, zenarestat). **So epalrestat's rhodanine is a genuine binding element for
this particular target, not a screening artifact.** The PAINS flag is a warning about its *other*
reported activities, not about AKR1B1. Making that distinction is precisely the medicinal chemist's
job, and collapsing it would be lazy.

**But it fails for the same reason the fibrates do.** Epalrestat is a **carboxylic acid** (pKa ~3–4)
and **AKR1B1 is cytosolic** — in pericytes and Müller cells, behind the same barrier.

> **Two of the best-shaped small molecules in this entire set — fenofibric acid (QED 0.85) and
> epalrestat (QED 0.68) — are both well-constructed, Ro5-clean, orally-dosed acids aimed at
> intracellular targets behind an effluxing barrier with no uptake carrier for anions. They fail for
> the identical structural reason, arrived at independently on two different pathways (P8 and P1).**
> That convergence is itself a finding: it says the access problem is a property of the *barrier and
> the chemotype*, not of any one pharmacology.

### 7.5 Alerts the brief did not name (independent scan of the set)

- **Pemafibrate.** The **2-aminobenzoxazole** can in principle ring-open to a 2-aminophenol
  derivative, which oxidises to a quinone-imine. Low risk here (tertiary N, stabilised ring), flagged
  for completeness. The **4-methoxyphenyl ether** is a CYP2C8/2C9 *O*-demethylation soft spot →
  4-hydroxyphenyl ether → oxidisable toward a quinone. Both minor.
- **All fibrate acids.** **Acyl glucuronide formation** is a class reactive-metabolite alert (acyl
  migration → protein adducts → idiosyncratic hepatotoxicity). Mitigated by α,α-disubstitution
  (§1). Ranking by migration propensity: **seladelpar (unsubstituted) > pemafibrate (α-mono) >
  fenofibric acid / elafibranor (α,α-di)**. The oldest chemistry is the safest here.
- **Seladelpar.** **Thioether** → S-oxidation liability (and a new stereocentre on oxidation);
  trifluoromethylphenyl ether; RTB 11; aLogP 5.05; QED 0.49. Plus the acyl-glucuronide point above.
- **Icosapent ethyl.** Five bis-allylic positions = peroxidation; RTB 14; lipase-dependent absorption.
- **Candesartan cilexetil.** Stoichiometric **acetaldehyde** release on activation (trivial at
  therapeutic dose — noted and dismissed); **tetrazole** = an acidity-*preserving* bioisostere, i.e.
  the wrong kind for §2; **di-anionic** released drug.
- **Quercetin.** Covered in §5.4 — the most alert-laden molecule in the set by a wide margin.

---

## 8. Cross-set structural summary table

| ID | Compound | MW | logP | PSA | RTB | Ro5v | QED | Charge @7.4 | §6.2 pass | Key structural alert |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Fenofibric acid | 318.76 | 3.81 | 63.60 | 5 | 0 | **0.85** | anion | 5/8 | acyl glucuronide (low, α,α-di) |
| A2 | Fenofibrate | 360.84 | 4.68 | 52.60 | 6 | 0 | 0.55 | neutral→anion | n/a (prodrug) | dissolution-limited; cleaved presystemically |
| A3 | Pemafibrate | 490.56 | 5.55 | 94.26 | **13** | 1 | **0.24** | anion | **1/8** | OATP1B substrate by design; benzoxazole (minor) |
| A4 | Elafibranor | 384.50 | 5.16 | 63.60 | 7 | 1 | 0.41 | anion | 2/8 | **chalcone Michael acceptor**; S-Me oxidation |
| A5 | Seladelpar | 444.47 | 5.05 | 64.99 | 11 | 1 | 0.49 | anion | 2/8 | most migration-prone acyl glucuronide; thioether |
| B1 | Linoleic acid | 280.4* | ~7.0* | 37.3* | 14* | 1* | ~0.35* | anion | 2/8 | aggregator/detergent; peroxidisable; **n-6 → ALOX12/15 wrong-sign** |
| B2 | α-Linolenic acid | 278.4* | ~6.5* | 37.3* | 14* | 1* | ~0.35* | anion | 2/8 | as B1, more peroxidisable; <0.5% DHA yield |
| B3 | Linalool | 154.25* | ~3.3* | 20.2* | 4* | 0* | ~0.50* | **neutral** | 7/8 | autoxidises → sensitising hydroperoxides; volatile; too small for affinity |
| B4 | Icosapent ethyl | 330.51 | 6.47 | 26.30 | **14** | 1 | **0.21** | neutral→anion | 2/8 | 5 bis-allylic sites; lipase-dependent absorption |
| C1 | Quercetin | 302.24* | ~1.5* | 131.4* | 1* | 1* | ~0.44* | neutral | 3/8 | **catechol PAINS: redox cycling, quinone, chelation, aggregation, optical** |
| C2 | Melatonin | **232.28** | **1.86** | **54.12** | 4 | **0** | **0.84** | **neutral** | **8/8** | none significant |
| D1 | Epalrestat | 319.41 | 2.92 | 57.61 | 4 | 0 | 0.68 | anion | 5/8 | **rhodanine PAINS** (but genuine at AKR1B1); chromophore/photoisomerisation |
| D2 | Dimethyl fumarate | 144.13 | −0.11 | 52.60 | 2 | 0 | 0.40 | neutral | 7/8* | **reactive Michael acceptor**; parent consumed presystemically; GSH drain |
| D3 | Minocycline | 457.48 | 0.19 | **164.63** | 3 | 0 | 0.40 | zwitterion | 3/8 (rubric misleads) | **chelation; melanin binding; photo-oxidising chromophore** |
| D4 | Candesartan cilexetil | 610.67 | 6.32 | 143.34 | 10 | **3** | **0.14** | neutral→**di-anion** | n/a (prodrug) | cascade ester (descriptors meaningless); released drug di-anionic |

\* knowledge-based, not in blinded data (see §5 data note). D2's pass rate applies to the parent,
which does not survive to the barrier.

**Three patterns fall out of this table:**

1. **Every direct PPARα agonist is an anion, and the §6.2 pass rate falls monotonically as potency
   rises** (A1 5/8 → A4 2/8 → A5 2/8 → A3 1/8). The series optimised itself away from the target
   tissue.
2. **The two best-drug-likeness molecules in the set (A1 QED 0.85, C2 QED 0.84) sit at opposite ends
   of the access/affinity trade** — one has the target and not the access, the other has the access
   and an uncertain target.
3. **Only two compounds are both neutral and small enough to cross (C2 melatonin, B3 linalool), and
   one of them is a fragrance volatile.** The chemical space of "neutral, drug-like, BRB-permeant,
   PPARα-engaging" is **empty in this candidate set**. That is the gap §9 addresses.

---

## 9. (g) Scaffold-hopping proposal — non-acidic PPARα engagement

**Design constraints** (disease-model §6.2 + chronic oral dosing in a comorbid population):
MW < 450 · cLogP 2–4 · TPSA < 70 Å² · HBD ≤ 2 · RTB ≤ 8 · **neutral at pH 7.4** · not a P-gp/BCRP
substrate · PPB < 98% · no chromophore absorbing above ~320 nm (§7.3/§7.4 — this is a light-exposed
target organ, and it is a constraint nobody has stated) · no reactive electrophile (chronic dosing).

### 9.1 Option 1 — do not abolish the charge, shift the pKa (highest value-per-risk)

The insight that makes this the first recommendation: **you do not need a neutral molecule, you need
a meaningful neutral *fraction*.** Moving pKa from 3.1 to 6.5 raises the permeant fraction by a
factor of ~2,000 while leaving a large ionised population available to bind.

| Head | pKa | Neutral at 7.4 | Gain vs COOH | Verdict |
|---|---|---|---|---|
| Carboxylic acid | 3.1 | 0.005% | 1× | baseline |
| **1,2,4-Oxadiazol-5(4H)-one** | **6–7** | **3–20%** | **~10³** | **recommended** |
| 3-Hydroxyisoxazole | 5–6 | 1–3% | ~10² | second choice |
| Tetrazole / acylsulfonamide | 4.5–4.9 | 0.1–0.3% | ~50× | insufficient |
| Hydroxamic acid | ~9 | >97% | ~10⁴ | charge solved; metallophilic off-targets, Lossen genotoxicity flag |

The 1,2,4-oxadiazol-5-one is planar with a two-oxygen donor/acceptor array that can plausibly reach
Ser280/Tyr314/His440/Tyr464. **Trade-off, stated honestly:** you will lose affinity — charge-assisted
H-bonds are worth 1.5–3 kcal/mol each — and **efficacy will degrade before affinity does**, because
the H12/Tyr464 clamp is the most charge-dependent contact in the network. Expect to land on a
**partial agonist**. Given §9.2, that may be a feature rather than a bug. *Confidence: moderate.
This is incremental, cheap, and testable with existing SAR.*

### 9.2 Option 2 — abandon arm I entirely: a transrepression-biased, non-acidic ligand

**This is the sharpest idea in this report, and it follows from re-reading the disease model rather
than from chemistry alone.**

Nuclear receptors have a well-precedented non-canonical binding mode: ligands that **never reach arm
I** and instead bind the **β-sheet / Ω-loop region** on the opposite face, stabilising the
H11/H12 interface indirectly. In the PPAR family this is best characterised for the **PPARγ partial
agonists** (the indole- and *N*-sulfonyl-indole series, MRL-24 / nTZDpa chemotypes), which bind near
Ser342 in the β-sheet and act by blocking Cdk5-mediated Ser273 phosphorylation rather than by
transactivation. **The direct PPARα analogue of that subsite is comparatively under-explored.**

Why this is the right target for *this* disease, from the model's own text:

1. **Disease-model §5.2(d) says the limb that maps onto DR's P6 leukostasis hub is
   *transrepression*** — ligand-bound PPARα physically inhibiting NFKB1/RELA and AP-1 and inducing
   IκBα, suppressing TNF/IL6/IL1B/ICAM1/VCAM1/CCL2/NOS2/PTGS2/MMP9. **Transrepression does not
   require the H12 clamp.** It is a protein–protein mechanism, mechanistically separable from
   PPRE-driven transactivation.
2. **Disease-brief §7 names ANGPTL4 induction as the wrong-sign risk.** ANGPTL4 is a **classic
   PPRE-driven transactivation output.** A transrepression-biased ligand would therefore
   **structurally decouple the anti-inflammatory benefit from the pro-permeability liability** —
   it is the only proposal in this analysis that addresses the brief's wrong-sign requirement by
   *design* rather than by monitoring.
3. Freed from arm I, the ligand need not be an acid at all — so it can be built inside the §6.2
   window: 350–400 Da, 2–3 rings, cLogP 3, TPSA ~55, HBD 1, RTB ≤ 6, neutral.

**Trade-offs, honestly:** partial and non-canonical-site ligands have shallow, assay-dependent SAR
and no clean potency metric, making medicinal-chemistry optimisation slow and regulatory
characterisation awkward. And **transrepression without transactivation forfeits the lipid-handling
programme** (CPT1A, ACOX1, HMGCS2, FABP, ABCA1) — which was half the P8 thesis. You would be trading
the lipid axis for the inflammation axis and for retinal access. *Confidence: speculative on
feasibility, high on the logic.*

### 9.3 Option 3 — copy nature: the neutral endogenous PPARα agonists

**Nature already solved the "neutral PPARα agonist" problem, and this candidate set walked past it.**
The *N*-acylethanolamines **oleoylethanolamide (OEA)** and **palmitoylethanolamide (PEA)** are
**endogenous, neutral PPARα agonists** active in the sub-µM to low-µM range:

```
OEA: CCCCCCCC/C=C\CCCCCCCC(=O)NCCO
     MW 325.5, NEUTRAL (primary amide + primary alcohol), logP ~5.9, PSA 49.3, HBD 2, RTB 19
PEA: MW 299.5, neutral, logP ~5.7
```

**Proof of principle that the head group need not be a carboxylate**: an amide C=O plus an
ethanolamide O–H can present two of the four H-bond partners the Ser/Tyr/His/Tyr quartet wants,
without any formal charge. The remaining problems are (i) RTB 19 — far too floppy — and (ii) rapid
hydrolysis by **FAAH/NAAA**.

**Concrete proposal — the headline design:**

> Take OEA's **neutral amide-alcohol head**, block the hydrolysis (**gem-dimethyl α to the amide**,
> a classic FAAH-blocking modification — note this reuses the same Thorpe–Ingold/metabolic-blockade
> trick the fibrates used on their acid, §1 — or an *N*-methyl or oxazoline), and graft it onto a
> **rigid fibrate-like biaryl or aryl-ketone body** instead of a C18 chain.
>
> **Target profile:** MW 340–400 · 1–2 aromatic rings · cLogP 3–4 · TPSA 55–65 Å² · HBD 1–2 ·
> **RTB ≤ 8** · neutral · no basic centre · no chromophore above 320 nm · not a P-gp/BCRP substrate.
>
> That profile fits **every** §6.2 window while still presenting a bidentate H-bond head toward
> Ser280/Tyr314/His440/Tyr464.

**Trade-offs:** expect **100–1,000× lower potency than pemafibrate** — neutral heads cannot match
charge-assisted binding, and that is a physical limit, not an optimisation gap. (Note the arithmetic
cuts the right way, though: pemafibrate wastes its potency on a 0.2% free fraction and a hepatic
sink. A 1,000-fold weaker ligand with a 40% free fraction and Kp,uu ≈ 1 is **ahead** at the
receptor.) FAAH/NAAA resistance must be engineered in, and the retina itself expresses FAAH, so the
metabolic liability sits in the target tissue. *Confidence: moderate on feasibility — this is the
best-grounded proposal here because it starts from an existing neutral agonist rather than from
scratch.*

**The design-space argument, stated once:** linalool (MW 154, neutral, PSA 20) shows the pocket
accepts a small neutral terpenoid alcohol but is too small for affinity (§5.3). OEA (MW 325,
neutral) has real affinity but RTB 19 makes it too floppy. **Between them lies an unoccupied region —
rigid, neutral, 300–400 Da PPARα ligands — and that is where I would look.** Both anchors are
*in or adjacent to this candidate set*, which is what makes the proposal concrete rather than
hand-waving.

### 9.4 Option 4 — carrier-mediated delivery (see §4.4(iii))

The **MFSD2A / lysophosphatidylcholine conjugate** route deserves restating here because it is the
only proposal that makes passive permeability irrelevant rather than merely better, and because
**icosapent ethyl in this very candidate set is an existence proof that the retina imports exogenous
lipid by this machinery.** Ro5 does not govern carrier uptake. Risks as in §4.4.

### 9.5 What I would NOT do

- **Topical.** Disease-brief §4 and disease-model §6.3 both set a strong prior against, and nothing
  in any of these structures changes the corneal-barrier/clearance-sink argument.
- **Intravitreal fibrate.** Small-molecule vitreous half-life is hours to a day or two
  (disease-model §6.3), so you would need a depot — and once you are implanting a depot you have
  surrendered the oral advantage that was the entire rationale (unmet needs #1 and #8).
- **More potency in the acid series.** This has already been run to exhaustion: 10⁴–10⁵ fold from
  fenofibric acid to pemafibrate, and it made the access problem *worse*, not better (§3.4, §8
  pattern 1). **Potency is the wrong axis. Free fraction and Kp,uu are the right ones, and no
  programme in this set has optimised either.**

---

## 10. Scoring — all 15 candidates

**Scoring stance.** I am scoring **what the structure says about likely behaviour in DR**, not
overall pharmacological promise. Per disease-brief §7 I keep *systemic lipid-lowering plausibility*
and *retinal PPARα occupancy* as separate considerations and say which one each score rests on. My
ceiling is **6**: no molecule in this set is structurally fit for the stated goal of retinal PPARα
engagement, and I decline to award 7+ for fitness against a reframed goal that structure alone
cannot establish. The spread 2–6 is used deliberately.

| ID | Compound | Score | Confidence | Basis | One-line structural verdict |
|---|---|---:|---|---|---|
| A1 | Fenofibric acid | **6** | moderate | mixed | Best-built molecule in the class (QED 0.85, Ro5v 0, 5/8 on §6.2); fails on exactly one criterion — ionisation — and that one is fatal for an intracellular retinal target but irrelevant for a hepatic one |
| A3 | Pemafibrate | **5** | high | mixed | Superb pharmacology, worst molecule (QED 0.24, RTB 13, 1/8 on §6.2); hepatoselectivity is inseparable from the potency, so it cannot answer the retinal question it was chosen to answer |
| C2 | Melatonin | **5** | moderate | data-backed (descriptors) | The only 8/8 on §6.2 and fu ~45%; proves access is solvable; its weakness is the mirror image — perfect access, uncertain target |
| D4 | Candesartan cilexetil | **5** | moderate | mixed | Prodrug descriptors are meaningless; released di-anion is a poor permeant **but AT1R is a cell-surface GPCR**, so it never crosses a membrane — materially weaker exposure objection than any intracellular-target acid here |
| A2 | Fenofibrate | **4** | high | data-backed | The same molecule wearing a mask that comes off before it matters; the ester creates a dissolution problem rather than solving a permeability one. Judge the acid |
| A4 | Elafibranor | **4** | moderate | mixed | Acid head + chalcone Michael acceptor + logP 5.16 + QED 0.41; dual α/δ adds mechanism, the enone adds covalent/PAINS liability and a confounding NRF2 limb |
| B4 | Icosapent ethyl | **4** | moderate | mixed | The only Group B entity with a real carrier-mediated route into retina (MFSD2A/ADIPOR1); against QED 0.21, RTB 14, weak non-selective µM PPARα, and five peroxidisable bis-allylic sites in the wrong tissue |
| D2 | Dimethyl fumarate | **4** | moderate | mixed | Excellent parent physicochemistry that never survives to the barrier; promiscuous cysteine succination; and a specific wrong-sign risk against a retina whose NADPH/GSH axis is already drained by polyol flux |
| A5 | Seladelpar | **3** | high | mixed | Structurally a δ ligand (unsubstituted aryloxyacetic + thioether = the GW-501516 head), which **validates** its falsification-control role; as a candidate: acid, logP 5.05, RTB 11, most migration-prone acyl glucuronide in the set |
| D1 | Epalrestat | **3** | moderate | mixed | Rhodanine PAINS flag is only half right — it is a genuine AKR1B1 binding element — but it is an acid against a cytosolic target, failing for the identical reason as the fibrates, plus a photoisomerising chromophore in a lit organ |
| D3 | Minocycline | **3** | moderate | mixed | Genuinely penetrant (descriptor rubric misleads here); but chelation-derived MMP9 activity is low-potency and non-selective, and a melanin-binding, photo-oxidising chromophore dosed chronically into the body's one continuously illuminated tissue is close to worst-case |
| B1 | Linoleic acid | **2** | high | mixed | Endogenous at concentrations already at/above its EC50 — cannot be agonised into action; n-6 → arachidonate → ALOX12/15 and PTGS2, an explicit wrong-sign limb in this disease |
| B2 | α-Linolenic acid | **2** | high | mixed | As B1; n-3 direction is right but <0.5% conversion to DHA makes it a sub-1%-yield prodrug for a species B4 delivers directly; more peroxidisable than B1 |
| B3 | Linalool | **2** | high | mixed | Best access profile in Group B and 15 heavy atoms — LE arithmetic caps it near 40 µM; volatile; autoxidises to sensitising hydroperoxides; racemic in the evidence row |
| C1 | Quercetin | **2** | high | mixed | Catechol PAINS on six independent mechanisms; aglycone essentially absent from circulation; 26 targets collapse to ~3 redundant programmes; only action-level PPARA row is **antagonism** |

**Falsifiers for the two highest scores** (per disease-brief §10, which requires one at 7+; I supply
them at 5–6 for symmetry):

- **A1 Fenofibric acid (6)** — falsified if a retina-specific PPARα knockout abolishes the protective
  phenotype while systemic lipid lowering is preserved. That would mean benefit requires retinal
  occupancy, which this molecule's ionisation forbids, and the score should fall to **3**.
  Conversely confirmed if benefit tracks apoB/remnant-particle lowering with no dose–response at
  the retina.
- **A3 Pemafibrate (5)** — falsified by a measured retinal Kp,uu < 0.05 in a species with a
  comparable barrier: its sub-nM potency would then be irrelevant and the score falls to **3**.
  Also falsified in the other direction if ocular microdialysis shows unexpected retinal
  accumulation, which would raise it to **7** as the only molecule potent enough to test the
  hypothesis cleanly.
- **C2 Melatonin (5)** — falsified if oral dosing yields retinal free concentrations <10 nM *and*
  MT1/MT2 engagement moves no DR-relevant endpoint; its value then collapses to a pure negative
  control.

---

## 11. Answers to the brief's seven questions, compressed

**(a)** The carboxylate makes a four-point **charge-assisted** H-bond network to
Ser280/Tyr314/His440/**Tyr464**, and because Tyr464 sits on H12 the ligand physically staples AF-2
shut to create the LXXLL coactivator groove. It is the allosteric trigger, not just an affinity
handle. The cost: pKa ~3.1 → >99.99% anionic at pH 7.4 → logD ~−0.5 against logP 3.81, a ~10⁴ loss
of permeant fraction, flip into the MRP/BCRP efflux phenotype at a barrier with **no OATP1B uptake
counterpart**, and ~99% binding at albumin Sudlow site II. The full budget is ~10³-fold short of
EC50 at the retina. The tension is irreducible because it is one atom serving both roles. **See §2.**

**(b)** Pemafibrate's benzoxazole/phenoxyalkyl Y-extension buys ~10⁵-fold potency *at improving
ligand efficiency* (0.29 → 0.38 kcal/mol/HA — the atoms are earning their place) and >2,000-fold
isoform selectivity, which **cannot come from the conserved head** and must be read out of locked
branch geometry. It costs QED 0.85 → 0.24, RTB 5 → 13, and §6.2 pass rate 5/8 → 1/8. Hepatoselectivity
is driven by **anionic head + logP 5.55 over 36 heavy atoms + extended hydrophobic tail distal to
the anion + 4 aromatic rings + no basic centre** — every one of which is also a potency or
selectivity element. **It is not separable from the design. See §3.**

**(c)** Fenofibrate's isopropyl ester solves a manufacturing problem and *creates* a dissolution
problem (choline fenofibrate, the salt of the acid, was marketed to undo it). Icosapent ethyl's
ethyl ester solves a purification problem and *costs* absorption. Candesartan cilexetil's cascade
double ester solves a steric-hindrance problem. **All three are absorption/formulation prodrugs
hydrolysed at or before the portal circulation; none is a distribution prodrug, and that is a fact
about esterase geography, not about these three molecules.** None improves retinal delivery. A
different strategy could: the best candidates are a **pKa-shifted head (oxadiazolone, §9.1)**, a
**transporter-hijacking MFSD2A/LPC conjugate** that makes passive permeability irrelevant (§4.4iii) —
for which **icosapent ethyl is an existence proof in this very set** — and a **FAAH-resistant
neutral acylethanolamide hybrid (§9.3)**. Simple hindered esters fail on logP and on hepatic
first-pass cleavage. **See §4.**

**(d)** Linoleic acid and ALA are endogenous ligands already present at/above their EC50 — they
cannot be dosed into agonism — and linoleate's n-6 lineage feeds ALOX12/15 and PTGS2, a
disease-specific wrong-sign limb. Linalool has the best access profile in the group and too few
heavy atoms to be potent. Quercetin is the frequent-hitter archetype on six independent structural
mechanisms, is <2% bioavailable with the aglycone absent from circulation, and its 26 targets
collapse to roughly three redundant programmes: **annotation artifact with a small genuine
redox-cycling core, not designed polypharmacology** — and its sole action-level PPARA row is
*antagonism*. **See §5.**

**(e)** Melatonin is neutral at pH 7.4 because it has no ionisable group in the physiological window
(indole N–H pKa ~17; amide N non-basic), so **logD = logP = 1.86** with no pH-partition penalty; at
MW 232, PSA 54, HBD 2, RTB 4 it is the **only compound in the fifteen to satisfy all eight §6.2
criteria**, and fu ~45% is ~45× fenofibric acid's and ~225× pemafibrate's. The implication: occupancy
is `fu × C × Kp,uu / EC50`, and this chemotype optimised the denominator by 4–5 logs while degrading
every numerator term — **potency and access are anti-correlated by construction here.** Melatonin
shows the access term is achievable; it is just not achievable by an acid. **See §6.**

**(f)** Elafibranor's chalcone is a real but **sterically damped** Michael acceptor (2,6-dimethyl
flanking the β-carbon) — flag it, and note it may carry a confounding NRF2 limb. Dimethyl fumarate
is a genuinely fast, promiscuous thiol electrophile whose **active parent does not survive to
circulation**, with a disease-specific GSH-depletion wrong-sign risk. Minocycline's two chelation
motifs make its "MMP9 inhibition" non-selective zinc chelation, and its melanin-binding,
photo-oxidising chromophore is close to worst-case for chronic dosing into a continuously illuminated
organ. Epalrestat's rhodanine is a textbook PAINS class **but a genuine structure-based AKR1B1
binding element** — the flag applies to its other reported activities, not this one. Additional
alerts the brief did not name: acyl-glucuronide migration (worst for seladelpar, best for the
α,α-disubstituted fibrates), seladelpar and elafibranor thioether S-oxidation, pemafibrate's
benzoxazole and *O*-demethylation soft spots. **See §7.**

**(g)** Four routes, in order of value-per-risk: (1) **shift pKa to 6–7** with a
1,2,4-oxadiazol-5-one head — a ~10³ gain in permeant fraction for maybe 10× affinity, accepting
partial agonism; (2) **abandon arm I** for a β-sheet/Ω-loop **transrepression-biased** non-acidic
ligand — which also **structurally decouples the NF-κB benefit from the PPRE-driven ANGPTL4
wrong-sign risk**, the only proposal here that addresses disease-brief §7 by design; (3) **copy the
endogenous neutral agonists** — a rigidified, FAAH-resistant OEA/PEA-like amide-alcohol head on a
rigid aryl body, targeting MW 340–400 / cLogP 3–4 / TPSA 55–65 / RTB ≤8 / neutral; (4)
**carrier-mediated delivery** via MFSD2A. Do **not** pursue topical, intravitreal depots (which
forfeit the oral rationale), or further potency in the acid series — that axis has been run to
exhaustion and made things worse. **See §9.**

---

## 12. Blinding compliance statement

**Files read (all within the permitted blinded set):**
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/disease-brief.md` (full)
- `.../disease-model.md` — heading scan plus §5, §5.1, §5.2, §6, §6.1–6.4 in full
- `.../agents/p0-ppara-scout.md` — §1.2, §3.1, §3.2, §4, §6, §6.1–6.3, §7 in full; heading scan of the rest
- `.../evidence/ppar-class-drug-properties.tsv` (full), `.../evidence/compound-dr-target-matrix.tsv`
  (header + targeted greps), `.../evidence/ppara-interactions.tsv` (header + targeted greps)
- `data/processed-blinded-diabetic-retinopathy/chembl_approved_drugs.csv` and
  `chembl_natural_products.csv` — targeted field extraction for the 15 candidates
- `.claude/skills/chemist/SKILL.md`

**Files NOT read, per protocol §1:** nothing under `data/processed/`; nothing under `data/holdout/`;
no file matching `answer-key*`. I did not inspect git history, git objects, or any other route to
redacted values. I made no attempt to determine which rows were redacted and did not reason by
elimination about what is missing.

**Knowledge used, per protocol §3 (permitted categories):** general medicinal chemistry (SMILES
parsing, functional-group reactivity, pKa estimation, Henderson–Hasselbalch, ligand efficiency,
PAINS/frequent-hitter literature, acyl-glucuronide migration SAR, bioisostere pKa tables); general
ADMET (albumin Sudlow sites, OATP1B/P-gp/BCRP/MRP/LAT1/MFSD2A substrate pharmacophores, CES
distribution and the human-vs-rodent plasma-esterase difference, melanin binding, phototoxicity of
polyketide chromophores); structural biology of the PPAR LBD (Y-cavity, the
Ser280/Tyr314/His440/Tyr464 network, H12/AF-2 mechanics, the LXXLL charge clamp, the PPARγ
partial-agonist β-sheet site); PPARα isoform pharmacology and SPPARMα design concepts; and the
non-DR clinical/pharmacological profiles of these agents (dyslipidemia, PBC/MASH, MS, acne,
hypertension indications; CKD dosing; statin DDIs).

**DR/DME-specific knowledge: not used.** I did not use, assert, or rely on the fact that any
candidate is indicated for, approved for, guideline-recommended for, or trialled in DR or DME. Every
conclusion above derives from structure, physicochemistry, transporter/barrier biology, or the
disease model's own pathway tables.

**Honest disclosures, including negative decisions:**

1. **The strongest evidence that the blind held.** I am aware that some agents in this set have
   DR/DME-adjacent clinical literature. I did not consult or invoke it, and the structural verdict I
   reached — that the fibrate acids almost certainly do **not** achieve retinal PPARα engagement —
   **runs against** the direction unblinded knowledge would have pushed me. If I had been leaning on
   forbidden knowledge, A1 and A3 would have scored higher, not been capped at 6 and 5. I flag this
   as the clearest internal check available to me.
2. **No DR-motivated exclusions.** I scored all 15 candidates and added none. I excluded nothing on
   DR-specific grounds. Where the scout had already excluded agents for protocol reasons (§4,
   intravitreal steroids and anti-VEGF), I did not revisit or second-guess that, since doing so
   would require the knowledge being withheld.
3. **Minocycline's photo-oxidation objection** (§7.3) was reached from the chromophore structure
   plus general tetracycline phototoxicity and melanin-binding pharmacology, combined with the
   disease model's own §6.1 statement about RPE/choroidal melanin. The step "the retina is
   continuously illuminated" is anatomy, not DR knowledge.
4. **Melatonin's retinal synthesis** (AANAT/ASMT in photoreceptors, MT1/MT2 expression) is
   physiology, explicitly permitted under §3, and is also already stated in the scout's §3.2.
5. **Icosapent ethyl and candesartan** have substantial cardiovascular and renal outcome literature.
   That is non-DR clinical knowledge and permitted; I used it only to affirm chronic-dosing
   tolerability, never as efficacy evidence in DR, and it did not move either score.
6. **The linoleate wrong-sign argument** (§5.1) was built from the disease model's own target table
   (#57 PTGS2, #59 ALOX12/ALOX15, the latter marked KO-validated) plus general fatty-acid
   biochemistry. No DR drug knowledge involved.
7. **Grey area I want on the record.** Section §9.3 proposes a neutral acylethanolamide-derived
   PPARα chemotype. OEA/PEA pharmacology is general (metabolic and analgesic literature), not DR
   literature, and I used it only as a structural existence proof for a non-acidic head. I believe
   this is cleanly inside §3, but it is the proposal where I was reasoning furthest from the
   supplied data, so I flag it and mark it speculative in the text.
8. **Data limitation affecting four scores.** Linoleic acid, α-linolenic acid, linalool and
   quercetin have **no descriptor rows in the blinded ChEMBL tables** —
   `chembl_natural_products.csv` is a 26-row test extract. Their physicochemical values in §5 and §8
   are knowledge-based and marked with an asterisk throughout. Their scores are correspondingly
   `evidence_basis: mixed` with the structural reasoning, not the project data, carrying the weight.

**Research disclaimer.** All of the above is computational and inferential structural reasoning.
Every potency, pKa, protein-binding and Kp,uu figure quoted is an estimate or general-literature
value, not a measurement from this project's data, and every proposal in §9 requires experimental
validation.

---

## SCOREBLOCK

SCORE|Fenofibric acid|6|moderate|mixed|Best-built acid in class but permanently anionic; works only if mechanism is systemic
SCORE|Fenofibrate|4|high|data-backed|Obligate ester prodrug; creates dissolution problem rather than solving permeability — judge the acid
SCORE|Pemafibrate|5|high|mixed|Hepatoselectivity structurally inseparable from potency; 1/8 on BRB rubric, QED 0.24
SCORE|Elafibranor|4|moderate|mixed|Acid head plus chalcone Michael acceptor; confounding NRF2 limb, logP 5.16
SCORE|Seladelpar|3|high|mixed|Structurally a delta chemotype, validating its control role; most migration-prone acyl glucuronide
SCORE|Linoleic acid|2|high|mixed|Endogenous at saturating concentrations; n-6 feeds ALOX12/15 and PTGS2 — wrong-sign limb
SCORE|Alpha-linolenic acid|2|high|mixed|Same endogenous-ligand problem; sub-1% DHA yield makes it dominated by icosapent ethyl
SCORE|Linalool|2|high|mixed|Excellent access but fifteen heavy atoms cap affinity near 40 micromolar; volatile sensitiser
SCORE|Icosapent ethyl|4|moderate|mixed|Real carrier-mediated retinal route via MFSD2A, but weak agonist and highly peroxidisable
SCORE|Quercetin|2|high|mixed|Catechol PAINS on six mechanisms; aglycone absent from circulation; only action row antagonism
SCORE|Melatonin|5|moderate|mixed|Only compound passing all eight BRB criteria; access solved, target relevance uncertain
SCORE|Epalrestat|3|moderate|mixed|Rhodanine genuine at AKR1B1, but an acid against a cytosolic target; photoisomerising chromophore
SCORE|Dimethyl fumarate|4|moderate|mixed|Active parent consumed presystemically; promiscuous succination; GSH drain into NADPH-depleted retina
SCORE|Minocycline|3|moderate|mixed|Penetrant, but photo-oxidising melanin-binding chromophore dosed chronically into a continuously illuminated tissue
SCORE|Candesartan cilexetil|5|moderate|mixed|Prodrug descriptors meaningless; di-anionic drug, but cell-surface GPCR needs no membrane crossing
