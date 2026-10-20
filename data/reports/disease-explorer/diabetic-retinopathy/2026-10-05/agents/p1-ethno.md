# P1 — Traditional Medicine / Ethnobotany Analysis
## Diabetic Retinopathy (BLINDED RUN)

**Agent:** Traditional Medicine Expert (ethnobotany-expert methodology, adapted from an
Oral Mucositis context to diabetic retinopathy)
**Date:** 2026-10-05
**Remit:** disease-brief.md §8 candidate set; disease-model.md §7 constraints

---

## 0. HEADLINE — read this if you read nothing else

Three findings, in descending order of importance to the pipeline:

1. **The traditional/computational "chemical-class convergence" (disease-model §7.5 point 4)
   is an ARTIFACT.** I tested it quantitatively rather than asserting either way. Eight of
   the nine project plants that have any chemistry cover **26–27 of the 27 DR-panel genes** —
   including *Santalum album*, which has no eye or diabetes use in the data. *Trichosanthes
   dioica* achieves **27/27 from seven compounds**, four of which are vitamin C, oleic acid,
   linoleic acid and niacin. **Ascorbic acid alone covers 23/27.** DR-target breadth has
   essentially **zero discriminating power** between plants, between chemotypes, or between
   traditionally-indicated and traditionally-irrelevant species. §3 gives the arithmetic.

2. **I found a new data-quality defect — in the disease model's own §7.4 analysis.** The
   claim that **8 of 13** IMPPAT plants carry eye/diabetes uses is wrong; the true figure is
   **6 of 13**. The two extra plants (*Alstonia scholaris*, *Santalum album*) were admitted on
   a "vision" keyword that matches **100% false positives** — the bibliographic string
   *"Forest **Divisions** (Maharashtra)"*. This is precisely the failure mode §7.4 warned
   downstream agents about in a different file, occurring inside the warning itself. Separately,
   `medicinal_plants_with_uses.csv` is **worse** than flagged: **1,907 of 1,915 rows (99.6%)
   are "UNKNOWN USE"**, and the eight rows with real text mention no eye, vision or diabetes
   use at all. §2 documents both.

3. **Traditional medicine contributes essentially nothing to this specific candidate set.**
   I say that plainly because it is where the evidence lands, and the brief invited a null
   answer. The entire traditional DR pharmacopoeia — *Salvia miltiorrhiza*, *Panax
   notoginseng*, *Astragalus*, *Pueraria*, *Vaccinium myrtillus*, *Pinus pinaster*, *Crocus
   sativus*, *Ginkgo biloba*, *Curcuma longa*, *Phyllanthus emblica*, *Terminalia bellirica*,
   *Gymnema sylvestre*, *Boerhavia diffusa* — **is absent from this project's data**, along
   with every one of its marker compounds (curcumin, berberine, piperine, puerarin, tanshinone
   IIA, salvianolic acid B, astragaloside IV, notoginsenosides, crocin, crocetin, anthocyanins,
   resveratrol, zeaxanthin). §6 states the verdict and §7 says what the null finding is
   nonetheless worth.

A corollary for the ranker: **strike "n DR targets hit" from the scoring criteria.** It is a
bibliometric statistic, not a pharmacological one, and §3.3 shows it cannot separate a drug
candidate from vitamin C.

---

## 1. The traditional corpus — what it actually says, and how good it is

### 1.1 Ayurveda: madhumeha and the Shalakya Tantra eye tradition

**The textual facts are solid; the inferential chain to DR is not.**

*Prameha* (a group of ~20 urinary disorders) and specifically *madhumeha* ("honey-urine")
are extensively described in the classical corpus (Charaka Samhita, Sushruta Samhita), with
recognised chronicity and systemic sequelae. Ophthalmology is a formal surgical/clinical
branch — *Shalakya Tantra* — with a developed nosology: *timira* (progressive dimming,
staged by depth of *patala*/tunic involvement), *kacha*, *linganasha* (classically cataract).

The critical appraisal point: **"madhumehajanya timira" is a modern Ayurvedic coinage, not an
ancient category.** The classical texts describe diabetes and they describe progressive
dimming of vision; they do not causally link them in the way DR requires. Twentieth- and
twenty-first-century Ayurvedic clinicians constructed the bridge retrospectively. On my
evidence scale this is **Level 2 (Related Indication)**, not Level 5 (Classical Authority) —
and the difference matters, because a retrofitted indication carries none of the empirical
weight that justifies taking traditional use seriously in the first place. Centuries of
observation of *timira* is centuries of observation of cataract and age-related dimming in a
population with ~1% diabetes prevalence and a life expectancy below the ~15-year latency DR
requires. **There is no plausible route by which classical Ayurvedic practitioners
accumulated empirical experience of diabetic retinopathy specifically.** This is the single
most important caveat in this section and it is usually elided.

What *is* genuine is the **Chakshushya** (eye-benefiting) and **Rasayana** (rejuvenative)
category, which recurs with real consistency:

| Dravya | Sanskrit | Classical standing | In project data? |
|---|---|---|---|
| Triphala (*T. chebula* + *T. bellirica* + *P. emblica*) | — | Level 4–5 for *netra* (eye) use; the most-cited Chakshushya formulation | **1 of 3** (chebula only) |
| *Glycyrrhiza glabra* | Yashtimadhu | Level 4, Rasayana/Chakshushya | Yes |
| *Tinospora cordifolia* | Guduchi | Level 4, Rasayana; named in eye formulations | Plant listed, **zero chemistry** |
| *Curcuma longa* | Haridra | Level 4 | **No** |
| *Boerhavia diffusa* | Punarnava | Level 3–4, anti-oedema | **No** |
| *Asparagus racemosus* | Shatavari | Level 3 | **No** |
| Saptamrita Lauha, Mahatriphala Ghrita | — | Compound formulations, explicitly *netra-roga* | **No** |
| *Gymnema sylvestre*, *Pterocarpus marsupium*, *Momordica charantia*, *Salacia reticulata*, *Trigonella*, *Syzygium cumini* | — | Antidiabetic (prameha-hara), Level 4 | **No** |

**Evidence quality on efficacy: uniformly weak.** The modern Ayurvedic DR trial literature
is small, usually unblinded, single-centre, and reports symptom or Snellen-acuity outcomes
without standardised DRSS grading, OCT central subfield thickness, or fundus-photograph
adjudication. No study in this literature would satisfy a regulator. **Hypothesis-generating
only** — which is the constraint the disease model handed me, and I find nothing that
justifies relaxing it.

### 1.2 TCM: the largest DR trial literature, and why that does not help

TCM has the most clinically developed traditional signal for DR specifically — **Compound
Danshen** preparations (*Salvia miltiorrhiza* + *Panax notoginseng* + borneol), **Qiming
granule**, **Hexue Mingmu tablet**, **Fufang Xueshuantong** — with many Chinese RCTs reporting
microaneurysm-count and acuity improvements in NPDR.

The appraisal is unambiguous and I will not soften it. **Systematic reviews, Cochrane
included, consistently conclude the evidence is insufficient.** The specific defects are
structural rather than incidental:
- Randomisation and allocation concealment usually unreported or inadequate; blinding rare.
- Outcomes non-standardised and frequently composite TCM "syndrome efficacy" scores that
  have no mapping onto DRSS or OCT.
- Short follow-up (often 1–3 months) against a disease whose natural history is measured in
  years — far too short for a structural DR endpoint to mean anything.
- **Publication bias concentrated in one country**, with a documented near-absence of
  negative trials. This is the decisive defect: it makes the *volume* of the literature
  uninformative rather than reassuring.
- Multi-herb decoctions of uncharacterised composition, so even a true positive would not
  identify an active principle.

**Relevance to this run: nil.** None of these formulations, and none of their marker
constituents, exists in the project's data (verified — §3.4). I cannot interrogate them, and
their trial literature cannot raise my confidence in anything in the candidate set.

### 1.3 Western / European herbal

The canonical microvascular-and-retina tradition: **bilberry (*Vaccinium myrtillus*)
anthocyanins** for capillary fragility and night vision; **French maritime pine bark
(*Pinus pinaster*) oligomeric proanthocyanidins**; ***Ginkgo biloba*** for ocular blood flow;
**grape-seed proanthocyanidins**; **lutein/zeaxanthin**; **saffron (crocin/crocetin)**.

Two honest observations:
- The bilberry "night vision" tradition has a **documented origin myth** (WWII RAF
  aircrew) that is not supported by subsequent controlled work, and several well-conducted
  dark-adaptation studies are null. It is a cautionary case of a tradition that is younger
  and thinner than its reputation.
- The pine-bark and grape-seed studies in early DR are small, mostly open-label, and
  heavily sponsor-associated.

**Chemically this entire group is flavonoid / anthocyanin / proanthocyanidin** — and that is
exactly the observation §7.3 of the disease model flagged as either meaningful convergence or
shared bias. §3 resolves it.

### 1.4 Cross-system consistency — the one argument that survives

If three independent traditions converge on a plant or chemotype, that is usually the
strongest ethnobotanical evidence available, because the traditions did not share a
literature. Here the convergence is **on polyphenol-rich astringent plant material** across
Ayurveda (Kashaya rasa — tannins), TCM (Danshen phenolic acids) and European herbalism
(anthocyanins). But polyphenols are the astringent, bitter, coloured fraction of *every*
temperate and tropical medicinal flora. Three traditions converging on polyphenols is close
to three traditions converging on "plants." **The cross-cultural argument is weaker here than
it looks**, and §3 shows the same is true of the computational signal.

---

## 2. Interrogating the project's own data — two QC defects found

### 2.1 `imppat_plant_therapeutic_uses.json` — the real figure is 6 of 13, not 8 of 13

I re-derived the §7.4 claim from the raw JSON rather than accepting it. Verified MeSH-term
hits, by plant (uses are IMPPAT's MeSH mappings of literature-sourced traditional uses):

| Plant | Eye / vision terms | Diabetes | Vascular-adjacent | Verdict |
|---|---|---|---|---|
| *Azadirachta indica* | Eye diseases, Conjunctivitis, Endophthalmitis, Graves ophthalmopathy | Yes (×4) | **Capillary permeability** (×2), Edema | **Confirmed** |
| *Cassia fistula* | Eye diseases (×2), **Blindness**, Graves ophthalmopathy | Yes (×6) | Edema, Cardiovascular | **Confirmed** |
| *Terminalia chebula* | Eye diseases, Graves ophthalmopathy | Yes (×2) | Edema, Cardiovascular | **Confirmed** |
| *Glycyrrhiza glabra* | Conjunctivitis, Endophthalmitis, Graves ophthalmopathy | Yes | Edema | **Confirmed** |
| *Cyperus rotundus* | Conjunctivitis, Endophthalmitis | Yes | Edema | **Confirmed** |
| *Trichosanthes dioica* | — | Yes (×2) | Edema (×2) | **Confirmed (diabetes only)** |
| *Alstonia scholaris* | **none** | no | Edema, Cardiovascular | ❌ **model claim not supported** |
| *Santalum album* | **none** | no | Cardiovascular | ❌ **model claim not supported** |
| *Picrorhiza kurrooa* | none | no | none | — |
| *Vetiveria zizanioides*, *Solanum xanthocarpum*, *Tinspora cordifolia*, *Adhatoda vasica* | **zero therapeutic-use records at all** | | | — |

**The defect.** §7.4 credits *Alstonia scholaris* and *Santalum album* with a "vision" use.
I reproduced the hit and traced every instance. `Alstonia scholaris` returns 6 matches for
`vision`, `Santalum album` returns 8, `Azadirachta indica` returns 12 — and **every single
one is the substring "vision" inside the bibliographic citation "Medicinal Plants Of Nagpur
And Wardha Forest *Divisions* (Maharashtra)."** Not one is a therapeutic use. This is the
same common-name/citation keyword artifact that §7.4 correctly diagnosed in
`medicinal_plants_with_uses.csv`, reproduced one paragraph earlier in the model's own
analysis of a different file.

**Two further corrections to the denominator:**
- **4 of 13 plants carry zero therapeutic-use records.** The honest denominator is **9**, not
  13. So the figure is **6 of 9 (67%)** among plants with any data — which sounds more
  impressive than 6/13 but is a different and much weaker claim, because 9 plants is not a
  sample from which enrichment can be inferred.
- **Term precision is poor.** "Graves ophthalmopathy" is an autoimmune orbitopathy — not a
  retinal disease, and its recurrence across four plants suggests a coarse MeSH mapping of a
  generic "eye complaint" use rather than four independent observations. "Endophthalmitis"
  (intraocular infection) likewise almost certainly back-maps a traditional antimicrobial
  eyewash use. **Nothing in this file names a retinal condition.** Zero rows match
  `retin`. The genuinely interesting single row is *Azadirachta indica* →
  **Capillary permeability**, the only microvascular-mechanism term in the file; I would not
  build on one MeSH mapping of unknown provenance.

**Net:** the "independent convergence between the classical corpus and the project's own
database" claim is **weakened but not destroyed**. *Terminalia chebula* and *Glycyrrhiza
glabra* genuinely are classical Chakshushya/Rasayana dravyas that independently carry eye
uses in IMPPAT. That is real. It is also two plants, in a 13-plant sample, of species so
ubiquitous in South Asian materia medica that they carry uses for nearly everything —
*Terminalia chebula* has 145 recorded uses and *Cassia fistula* has 332. A plant with 332
indications will hit any indication you search for. **This is the base-rate problem, and it
is fatal to an enrichment argument.**

### 2.2 `medicinal_plants_with_uses.csv` — worse than flagged

The model told me not to trust keyword hits here. Verified, and the file is emptier than the
warning implies:

- **1,907 of 1,915 rows (99.6%) have `Uses == "UNKNOWN USE"`.** This is a BSI *herbarium
  listing* with a use column that is almost entirely unpopulated — not a therapeutic-use
  database.
- Keyword counts across the whole file: `diabet` **0**, `retin` **0**, `ophthalm` **0**,
  `vision` **0**, `cataract` **0**, `blind` **0**, `glaucoma` **0**, `conjunctiv` **0**.
  `eye` returns 4 rows — all common-name artifacts (*Summer Pheasant's **Eye***,
  ***Eye**bright*, *Black-**Eye**d Susan*, and *Phaseolus adenanthus* whose Bengali name
  merely contains the letters) and **all four carry "UNKNOWN USE"**. §7.4's call was correct.
- **New finding:** the **eight** rows that *do* carry real use text are **exactly eight of
  the project's own 13 IMPPAT plants** — so the file is not an independent source at all;
  its only content is a redundant, lower-resolution gloss on plants we already have. And
  critically, **not one of those eight descriptions mentions eyes, vision or diabetes.**
  *Cassia fistula* is "purgative, febrifugal, astringent, antibilious." *Terminalia chebula*
  is "laxative, stomachic, tonic ... a constituent of triphala." *Azadirachta indica* is skin
  and antiseptic. *Trichosanthes dioica* is laxative and digestible.

**This is a mild independent *disconfirmation*, not a corroboration.** The one other
project source that records traditional uses for these same species **fails to replicate**
the IMPPAT eye/diabetes annotations. Two sources, one signal, one silence. I weight the
IMPPAT eye claims down accordingly.

### 2.3 Phytochemistry of the eye/diabetes plants → DR-target matrix

Compounds from the six verified eye/diabetes plants that appear in
`evidence/compound-dr-target-matrix.tsv` (PPARA column from the matrix):

| Plant | n phytochem | in matrix | Notable contributions (DR targets) |
|---|---:|---:|---|
| *Glycyrrhiza glabra* | 312 | **63** | Quercetin 26, Genistein 23, Apigenin 21, Kaempferol 20, Rutin 19, Geraniol 18 ✦, Nicotinic acid 16 ✦, Linalool 12 ✦, Glabridin 3, Liquiritigenin 3 |
| *Azadirachta indica* | 236 | 39 | Quercetin 26, Palmitic 21 ✦, Kaempferol 20, Melatonin 19 ✦, Oleic 19 ✦, Rutin 19 ✦, Linoleic 18 ✦, Myricetin 13 ✦, α-Linolenic 8 ✦, Azadirachtin 5 |
| *Cassia fistula* | 104 | 30 | Quercetin 26, Palmitic 21 ✦, Kaempferol 20, Oleic 19 ✦, Linoleic 18 ✦, Ellagic 17, Cianidanol 16 ✦, Emodin 16, Procyanidin B2 10 |
| *Cyperus rotundus* | 171 | 22 | Quercetin 26, Luteolin 19, Oleic 19 ✦, Linoleic 18 ✦, Oleanolic 14 ✦(wrong-sign), Linalool 12 ✦, Stearic 10 ✦, α-Linolenic 8 ✦ |
| *Terminalia chebula* | 51 | 20 | Palmitic 21 ✦, Oleic 19 ✦, Linoleic 18 ✦, Ellagic 17, Gallic 16, Ferulic 11, Caffeic 10, pentagalloylglucose 4 |
| *Trichosanthes dioica* | 14 | 7 | Ascorbic 23, Oleic 19 ✦, Linoleic 18 ✦, Nicotinic 16 ✦, Thiamine 9, Riboflavin 8 |

✦ = carries at least one PPARA row.

**Read the right column, then read it again.** The highest-contributing compounds are, almost
without exception, **ubiquitous plant primary metabolites and the twenty most-studied dietary
flavonoids**. The compounds shared across the most plants are: oleic acid (6/9 plants),
linoleic acid (6/9), palmitic acid (5/9), lupeol (5/9), betulinic acid (4/9), stigmasterol
(4/9), quercetin (4/9), stearic acid (4/9) — **and D-fructose (4/9), sucrose (2/9),
D-glucose (3/9), which the brief §8 explicitly names as curation defects.** The plant-specific
chemistry that actually distinguishes these species — glabridin, liquiritigenin,
licochalcones, azadirachtin, nimbin, chebulagic/chebulinic acids, the cyperenes — sits at the
*bottom* of the target-count distribution (3–5 targets) or is absent from the matrix entirely.

**The traditional identity of these plants is contributing nothing to their apparent DR
relevance.** Their apparent relevance is carried by compounds they share with lettuce.

---

## 3. THE CONVERGENCE QUESTION — tested, and the verdict is ARTIFACT

The disease model asked whether the polyphenol/flavonoid/terpenoid convergence between the
three traditions and the project's DR-target hits is genuine, and told me to take the
alternative explanation seriously. I ran four tests. All four point the same way.

### 3.1 Test 1 — DR-target coverage is saturated, so it cannot discriminate

| Plant | eye/diabetes use? | n phytochem | matrix hits | **DR panel covered** |
|---|---|---:|---:|---:|
| *Glycyrrhiza glabra* | ✔ | 312 | 63 | **27/27** |
| *Azadirachta indica* | ✔ | 236 | 39 | 26/27 |
| *Cyperus rotundus* | ✔ | 171 | 22 | 26/27 |
| ***Santalum album*** | ✘ | 107 | 9 | **26/27** |
| *Cassia fistula* | ✔ | 104 | 30 | 26/27 |
| ***Alstonia scholaris*** | ✘ | 84 | 19 | **26/27** |
| *Terminalia chebula* | ✔ | 51 | 20 | 26/27 |
| ***Trichosanthes dioica*** | ✔ | **14** | **7** | **27/27** |
| *Picrorhiza kurrooa* | ✘ | 6 | 1 | 17/27 |

**Eight of nine plants cover 26 or 27 of the 27 DR-panel genes.** Sandalwood — a fragrance
wood whose only use record in either project file is "diuretic, diaphoretic, expectorant" —
covers 26/27. *Trichosanthes dioica* covers the **entire panel from seven compounds**:

```
Ascorbic acid       ->  23/27     (vitamin C, by itself)
+ Oleic acid        ->  25/27
+ Linoleic acid     ->  26/27
+ Nicotinic acid    ->  27/27     complete
  (thiamine, riboflavin, serotonin add nothing)
```

**Vitamin C, two fatty acids and niacin cover the entire diabetic-retinopathy target panel.**
A metric that cannot distinguish a drug candidate from a multivitamin is not measuring
pharmacology.

### 3.2 Test 2 — plant "DR relevance" is catalogue size

Pearson **r(n phytochemicals, n matrix hits) = 0.911**. A plant's apparent engagement with
DR biology is almost entirely a function of how thoroughly its chemistry has been catalogued.
*Glycyrrhiza glabra* leads the field because licorice is one of the most chemically
characterised plants on earth (312 constituents in IMPPAT), not because it is retinally
active.

Null model, sampling *k* compounds at random from the 153-compound matrix (4,000 draws each):

| k | mean coverage | P(≥26/27) |
|---:|---:|---:|
| 3 | 16.6 | 0.023 |
| 5 | 19.7 | 0.040 |
| 7 | 21.7 | 0.078 |
| 10 | 23.3 | 0.169 |
| 20 | 25.4 | **0.577** |
| 40 | 26.2 | **0.954** |
| 63 | 26.4 | 0.997 |

Every plant with ≥20 matrix compounds is **more likely than not** to hit 26/27 by chance
alone. *Glycyrrhiza* (63) and *Azadirachta* (39) are squarely in the regime where the null
model predicts their result. The observed plants do slightly *better* than random at low
*k* — but only because their compounds are the heavily-annotated ones (vitamin C, the
common fatty acids), which is the bias, not a correction for it.

### 3.3 Test 3 — the panel itself is a generic stress-response readout

How many of the 153 matrix compounds annotate each DR-panel gene:

```
TNF      128 (84%)  ┤████████████████████████████████████████████
CASP3    119 (78%)  ┤██████████████████████████████████████████
IL6      105 (69%)  ┤█████████████████████████████████████
CAT      100 (65%)  ┤███████████████████████████████████
BAX      100 (65%)  ┤███████████████████████████████████
BCL2      99 (65%)  ┤███████████████████████████████████
IL1B      95 (62%)  ┤█████████████████████████████████
NFE2L2    70 (46%)  ┤████████████████████████
PPARG     64 (42%)  ┤██████████████████████
TGFB1     56 (37%)  ┤███████████████████
VEGFA     49 (32%)  ┤█████████████████
MMP9      48 (31%)  ┤█████████████████
NFKB1     44 (29%)  ┤███████████████
SOD2      43 (28%)  ┤███████████████
ICAM1     38 (25%)  ┤█████████████
HIF1A     37 (24%)  ┤█████████████
PPARA     36 (24%)  ┤████████████
NOS3      35 (23%)  ┤████████████
SERPINE1  25 (16%)  ┤████████
AKR1B1    22 (14%)  ┤███████
EDN1      19 (12%)  ┤██████
SLC2A1    17 (11%)  ┤█████
AGER      17 (11%)  ┤█████
KDR       15 (10%)  ┤█████
PPARD     14  (9%)  ┤████
PRKCB     11  (7%)  ┤███
ANGPT2     1  (1%)  ┤
```

The top seven genes — TNF, CASP3, IL6, CAT, BAX, BCL2, IL1B, each annotated by 62–84% of all
compounds — are **the standard rodent qPCR panel for "this cell experienced stress."** They
are not DR genes; they are the genes everyone measures. Coverage of this panel is a measure
of how many papers were written about a compound.

The genes that are actually **DR-specific** — ANGPT2 (1 compound), PRKCB (11), KDR (15),
AGER (17), AKR1B1 (22) — are nearly empty. **The angiopoietin axis is covered by exactly one
compound in 153** (nicotinic acid), and the polyol pathway's 22 "AKR1B1 hits" include
**D-fructose, D-galactose, D-glucose, citric acid, benzoic acid, hexanal and methyl
salicylate** — sugars that are aldose-reductase *substrates* and solvents/flavourants, not
inhibitors. Even the narrow, DR-specific slice of the panel is contaminated by the same
substrate/perturbagen confusion the brief flagged at §8.

### 3.4 Test 4 — the traditional DR pharmacopoeia is not in the dataset at all

Searched the 153-compound matrix for every marker compound of every tradition in §1:

| Compound | Tradition | In matrix? |
|---|---|---|
| Curcumin | Ayurveda (Haridra) | **✘** |
| Piperine | Ayurveda (Trikatu, yogavahi) | **✘** |
| Berberine | Ayurveda / TCM | **✘** |
| Puerarin | TCM (*Pueraria*) | **✘** |
| Tanshinone IIA, Salvianolic acid B | TCM (Danshen) | **✘** |
| Notoginsenosides | TCM (*P. notoginseng*) | **✘** |
| Astragaloside IV, Calycosin | TCM (*Astragalus*) | **✘** |
| Crocin, Crocetin | Saffron | **✘** |
| Cyanidin / anthocyanins | Bilberry | **✘** |
| Resveratrol | Western | **✘** |
| Zeaxanthin | Macular carotenoid | **✘** |
| Silymarin, Baicalein | TCM / Western | **✘** |
| Ginkgo flavone glycosides | *Ginkgo biloba* | **✘** |

Present instead: Quercetin, Rutin, Lutein, Linalool, Geraniol, the common fatty acids —
i.e. the **ubiquitous** members of the class, not the traditionally-indicated ones. And at
the plant level, *Tinospora cordifolia* (Guduchi, a core Rasayana) is listed with **zero
phytochemicals**; *Phyllanthus emblica* and *Terminalia bellirica* — the other two thirds of
Triphala, the single most-cited Chakshushya formulation — are absent entirely.

### 3.5 VERDICT on (c): **ARTIFACT.** High confidence.

The convergence claimed at disease-model §7.5 point 4 is **between two things that are not
independent and one of which is not measuring what it appears to measure.**

- The traditional side of the "convergence" is **my own knowledge**, not the project's data.
  The project's data contains **none** of the plants any tradition actually uses for DR.
- The computational side is a **study-volume ranking**. Target breadth correlates at r=0.91
  with catalogue size, saturates at 26–27/27 for almost every plant, is achieved by vitamin C
  plus three nutrients, and is carried by a panel whose top genes are generic stress markers
  annotated for 62–84% of all compounds.
- The mechanism of the illusion is exactly the one the brief asked me to take seriously:
  **polyphenols and fatty acids are ubiquitous in edible plants, over-represented in
  natural-product screening libraries, and over-studied in CTD — a toxicology resource — so
  they top any coverage ranking regardless of therapeutic relevance.** Dibutyl phthalate at
  22 targets and D-fructose at 21 are the proof: a plasticiser and a sugar out-rank most of
  the pharmacopoeia.

**What would falsify my verdict:** a demonstration that traditionally-indicated plants are
enriched for *DR-specific* targets (AKR1B1 by genuine inhibition, PRKCB, KDR, AGER, ANGPT2)
after conditioning on catalogue size and CTD row count; or binding-affinity data, rather than
CTD action strings, showing selective sub-micromolar engagement by a traditional constituent.
Neither is obtainable from this dataset. I would also revise if the project ingested the
actual traditional DR plants and they still clustered at the top — that would be a real test,
and it has not been run.

---

## 4. The PPARα–natural-product bridge: doing the arithmetic

PPARα's endogenous ligands are fatty acids, so natural-product space is intrinsically
privileged for this target (disease-model §5.2f). The question is whether any traditional
preparation can deliver a PPARα-active dose. **I did the arithmetic rather than asserting.**

### 4.1 What it would take

Dose required to reach EC50 as a whole-body concentration, assuming **100% bioavailability,
zero clearance, zero protein binding** — i.e. a generous lower bound that no real preparation
approaches (V ≈ 42 L total body water, 70 kg adult):

| Compound | EC50 (in vitro, literature range) | MW | **Ideal-case dose to reach EC50** |
|---|---|---:|---:|
| Linoleic acid | 10–50 µM | 280.4 | **118 – 589 mg** |
| α-Linolenic acid | ~10 µM | 278.4 | **117 mg** |
| Linalool | 25–100 µM | 154.2 | **162 – 648 mg** |
| Geraniol | ~50 µM | 154.2 | **324 mg** |

### 4.2 What a traditional preparation actually delivers

| Preparation | Delivers |
|---|---:|
| **Fatty acids** | |
| *Terminalia chebula* churna 6 g (fruit ~5% lipid, LA ~30% of it) | **90 mg** linoleic |
| *Azadirachta indica* leaf 10 g (~3% lipid, LA ~15%) | **45 mg** |
| *Cyperus rotundus* churna 5 g (~2% lipid, LA ~25%) | **25 mg** |
| *Ghrita* vehicle, 10 g ghee (LA ~2%) | **200 mg** |
| ***Taila* vehicle, 10 mL sesame oil (LA ~42%)** | **3,780 mg** |
| *Background Western dietary linoleic acid* | **12,000 – 17,000 mg/day** |
| *Icosapent ethyl (B4), therapeutic dose* | **4,000 mg/day** |
| **Terpenoids** | |
| *Cyperus rotundus* 5 g (EO ~0.8% of rhizome, linalool ~4% of EO) | **1.6 mg** linalool |
| Coriander seed 10 g (EO ~0.8%, linalool ~70% — the richest common source) | **56 mg** |
| *Glycyrrhiza glabra* 6 g (geraniol a trace volatile) | **0.06 mg** geraniol |

### 4.3 Reading the numbers — two different failures

**Terpenoids: hopeless, straightforwardly.** *Cyperus rotundus* delivers **1.6 mg** of
linalool against an idealised **162 mg** requirement — a **100-fold shortfall before any
pharmacokinetics**. Linalool and geraniol are fragrance monoterpenes with extensive
first-pass oxidation and glucuronidation and half-lives of minutes to a couple of hours; the
realistic shortfall is **three orders of magnitude or more**, and sustaining 25 µM would
require continuous gram-scale dosing of a compound with GRAS flavouring limits far below
that and dose-limiting mucosal irritation and CNS depression. Even the richest conceivable
dietary source (coriander, which no tradition uses for the eye) falls short. **There is no
traditional preparation, in any of the three traditions, that delivers a PPARα-active
terpenoid dose. This route is closed.**

**Fatty acids: the failure is the opposite one, and it is more interesting.** The dose is not
unreachable — it is **already permanently exceeded by endogenous physiology**:

```
Plasma total NEFA, fasting                 300 – 800 µM   (up to ~2,000 µM, uncontrolled T2D)
  of which linoleate (~12%)                 35 –  95 µM   <-- at or ABOVE the in-vitro EC50
Free (albumin-unbound) NEFA                  1 –  10 nM
Intracellular FA flux via CD36/FABP      micromolar, continuously replenished
```

**The PPARα fatty-acid ligand channel is a tonically occupied, homeostatically buffered
nutrient-sensing system.** Circulating linoleate already sits at or above the concentration
at which it activates PPARα in vitro, around the clock, in everyone — and it is *higher* in
the uncontrolled diabetic, which is the patient population here. A 90 mg dose of linoleic
acid from *Terminalia chebula* churna is a **0.5–0.7% perturbation** of a 12,000–17,000 mg
daily dietary background feeding a pool that is already saturating. It is not a
pharmacological intervention; it is a rounding error on lunch.

**The reductio that settles it.** The *taila* (sesame-oil) vehicle of a classical Ayurvedic
oil preparation delivers **3,780 mg of linoleic acid — roughly 40× more than the herb it
carries**, and ghee delivers twice the herb's contribution. If any traditional preparation
had PPARα pharmacology attributable to fatty acids, **the active principle would be the
cooking oil**, and the herb would be the excipient. That conclusion is absurd as pharmacology
but it is the honest output of the arithmetic, and it tells you the premise is wrong.

**The contrast that makes the point.** Icosapent ethyl (B4) is dosed at **4,000 mg/day of a
single >96%-pure ω-3 ethyl ester** — ~45× the herb's fatty-acid contribution, of one defined
molecular species, at a dose large enough to shift plasma fatty-acid composition measurably.
**That is the only way this chemical class reaches a pharmacological dose, and it is a
pharmaceutical product, not a plant.** The scout was right to promote it as the druggable
form of the Group B finding, and my arithmetic independently confirms the reasoning.

### 4.4 The access/affinity anti-correlation — the one genuinely interesting structural finding

Scoring the natural-product candidates against disease-model §6.2 honestly:

| Compound | MW | cLogP | TPSA | HBD | RotB | Ionised at 7.4? | PPB | §6.2 verdict |
|---|---:|---:|---:|---:|---:|---|---|---|
| **Linalool** (B3) | 154 | ~3.0 | 20 | 1 | 4 | **No** | low | ✅ **passes every criterion** |
| **Geraniol** | 154 | ~3.2 | 20 | 1 | 4 | **No** | low | ✅ passes every criterion |
| **Melatonin** (C2) | 232 | ~1.1 | 54 | 2 | 4 | **No** | ~50% | ✅ passes; retina synthesises it |
| **Linoleic acid** (B1) | 280 | **~7.0** | 37 | 1 | **14** | **Yes (anion)** | **>99.9%** | ❌ cLogP, RotB, ionisation, PPB |
| **α-Linolenic acid** (B2) | 278 | **~6.5** | 37 | 1 | **13** | **Yes (anion)** | **>99.9%** | ❌ same |
| **Icosapent ethyl** (B4) | 331 | **6.47** | 26 | 0 | **~15** | No (ester) → **EPA, anion** | >99% as EPA | ❌ after hydrolysis |
| **Quercetin** (C1) | 302 | ~1.5 | **131** | **5** | 1 | partly | ~99% | ❌ TPSA, HBD; oral F <2% |

**Across the entire natural-product set, retinal access and PPARα affinity are
anti-correlated.** The compounds with real, replicated binding-plus-activation evidence
(linoleic, α-linolenic) are the ones that **cannot** reach the retina — too lipophilic, too
flexible, permanently anionic, >99.9% albumin-bound, and facing exactly the free-fraction
problem the scout identified for fenofibric acid, only worse. The compounds that sail through
every §6.2 criterion (linalool, geraniol, melatonin) are the ones with **no potency** — a
single-source CTD row apiece, EC50s in the tens of micromolar, and clearance that makes those
concentrations unattainable.

This is a sharper restatement of the pipeline's central tension and it is worth handing to the
ranker: **the PPARα pocket's preference for lipophilic carboxylic acids is not merely a
problem for fibrates — it is a structural property of the target that penalises every ligand
chemotype, natural or synthetic, on exactly the axis the blood-retinal barrier cares about.**
The one chemotype that escapes the acid penalty (neutral monoterpene alcohols) escapes it by
being too small and too weakly binding to be a drug.

Linalool's genetic-dependency row (`PPARA gene mutant form results in decreased susceptibility
to linalool`, PMID 24752549) remains, as the scout noted, the **best single piece of PPARα
pharmacology in the natural-product set** — a receptor-mutant phenotype is much harder to
explain away than an expression change. Combined with an ideal §6.2 profile, that makes
linalool the only natural product here worth a sentence as a **chemical starting point** —
a neutral, BRB-permeant, low-MW PPARα-touching scaffold is a rare combination — while being
plainly useless as a candidate in its own right. I score it accordingly: low as a drug,
noted as a structure.

### 4.5 ANGPTL4 wrong-sign risk

The brief requires any agent scoring a PPARα candidate highly to address the ANGPTL4
induction risk in ischemic retina. **I score no natural product above 5, so the requirement
is not triggered.** For completeness: the risk is *mechanistically irrelevant* to the Group B
natural products for the same reason they fail as candidates — they cannot achieve the
receptor occupancy that would drive a PPARα target-gene programme in the first place. A
compound too weak to induce CPT1A is too weak to induce ANGPTL4. **The absence of wrong-sign
risk here is a consequence of the absence of pharmacology, and must not be read as a safety
advantage.** That asymmetry is a general trap in natural-product scoring and the ranker
should watch for it.

---

## 5. Formulation logic — defensible versus arbitrary

The skill's core competence is distinguishing a rationally designed combination from an
arbitrary one. Applying it:

### 5.1 Genuinely defensible

**Trikatu / piperine (yogavahi).** The strongest pharmacological rationale in Ayurvedic
formulation theory, and it is real: piperine inhibits **CYP3A4, UGT-mediated glucuronidation
and P-glycoprotein**, raising systemic exposure of co-administered compounds — the classic
demonstration being a multi-fold increase in curcumin AUC. For a polyphenol, whose dominant
failure mode is precisely extensive first-pass phase-II conjugation, this addresses the exact
right defect. **The tradition identified a real pharmacokinetic problem and a real solution to
it, centuries before the enzymology existed.** That deserves to be said clearly.

**But it is unusable here, and the reason is instructive.** (i) Piperine is **not in the
project's data** — no matrix row, no IMPPAT plant. (ii) In *this* patient population it is
**actively dangerous**: §5 of the brief describes diabetic adults on metformin, insulin,
statins, RAS blockers, antiplatelets and diuretics, with renal impairment as the norm. A
non-selective CYP3A4/P-gp/UGT inhibitor dosed chronically into that regimen raises statin
exposure (myopathy — already a flagged PPAR-class liability), and interacts unpredictably
across the board. **The yogavahi principle is pharmacologically sound and clinically
contraindicated in precisely the population this analysis targets.** That is a genuine
ethnobotanical insight with a genuinely negative conclusion.

**Compound Danshen (*Salvia miltiorrhiza* + *Panax notoginseng* + borneol).** The most
defensible multi-component design in any tradition for this disease, on three distinct
grounds: complementary chemistry (water-soluble phenolic acids + triterpene saponins, so the
decoction extracts two chemically non-overlapping fractions); complementary mechanism; and
**borneol as a deliberate penetration enhancer** — a small, neutral, lipophilic bicyclic
monoterpene with documented tight-junction-modulating and BBB-permeability-enhancing activity,
designated in TCM theory as a *channel-guiding* (引经) herb whose role is explicitly to carry
the other constituents to the head and eyes. **That is the same functional concept as
yogavahi, arrived at independently, and it is the single most mechanistically interesting idea
traditional medicine offers this analysis** — because the pipeline's critical path item is
blood-retinal-barrier penetration. It is also the one that most urgently needs a safety
objection: an agent that non-specifically loosens the BRB in a disease **defined by
pathological BRB breakdown** is wrong-sign by construction. Enhancing penetration of a barrier
whose failure *is* the pathology is not a delivery strategy, it is the disease. Not in the
project's data either.

**Triphala.** Defensible as designed: three astringent fruits combining hydrolysable tannins
and gallic acid (*T. chebula*, *T. bellirica*) with ascorbate and emblicanins (*P. emblica*),
giving broader phenolic coverage than any one fruit and a plausible toxicity-mitigation
rationale (the mild laxative action of chebula balanced across the three). **Only 1 of 3
components is in this project.** And note the irony §3 exposes: *P. emblica*'s famed vitamin C
content is exactly the compound that, by itself, "covers" 23/27 of the DR panel — Triphala's
best-known constituent is this analysis's most conspicuous false positive.

**Mahatriphala Ghrita / Saptamrita Lauha** (classical *netra-roga* formulations). The *ghrita*
(ghee) base is a defensible lipid vehicle for lipophilic constituents — a genuine formulation
insight, and the correct intuition for the flavonoid-aglycone solubility problem. Saptamrita
Lauha additionally contains processed iron (*lauha bhasma*), which in a diabetic population
with CKD is a liability, not a tonic. Neither formulation nor its distinctive components are
in the project's data.

### 5.2 Arbitrary, or at least undemonstrated

Most multi-plant combinations in the corpus do **not** have a demonstrable pharmacological
rationale. The honest appraisal is that they are organised by *Ayurvedic* logic — balancing
*rasa*, *virya* and *vipaka*, matching *dosha* — which is an internally coherent, sophisticated
system that is **not a pharmacological rationale** and should not be translated into one
retrospectively. The discipline the skill demands here is to resist the temptation: a
formulation balancing *ushna* and *sheeta* dravyas is doing something real within its own
framework, and inventing a modern mechanism for it is the error, not the insight.

Within this project's six eye/diabetes plants specifically, there is **no classical
formulation combining them**, and I will not construct one. *Cyperus rotundus* + *Glycyrrhiza
glabra* + *Terminalia chebula* is not a traditional combination; proposing it because the
three happen to be the plants in our database would be exactly the manufactured relevance the
brief told me not to produce.

### 5.3 The anupana/samskara dimension, honestly

*Kwatha* (decoction) biases extraction toward polar glycosides and tannins — the fraction with
the **worst** oral bioavailability and the least chance of crossing a BRB. *Churna* preserves
volatiles but delivers them at the milligram doses §4.2 shows are inadequate. *Taila* and
*ghrita* improve lipophilic extraction, but §4.3 shows the vehicle then dominates the fatty-acid
pharmacology. **Every traditional processing route, analysed properly, makes the
bioavailability problem worse or makes the vehicle the active agent.** This is not a criticism
of Ayurveda — these methods were optimised for GI-acting and topically-acting indications,
where they work well. They were never optimised to deliver a molecule across the blood-retinal
barrier, and it would be remarkable if they did.

---

## 6. HONEST VERDICT on (f): the null answer

**Does traditional medicine contribute anything to this specific analysis beyond hypothesis
generation that modern pharmacology has not already covered?**

**No. For this candidate set, in this disease, with this data, the contribution is null.** I
state that plainly, as the brief invited, and I want to be precise about what is and is not
being claimed.

**What is NOT being claimed.** Not that Ayurveda, TCM or European herbalism are without value;
not that traditional plants lack pharmacology; not that the ethnobotanical approach is
unsound. The yogavahi/borneol penetration-enhancement concept is a genuine, independently
rediscovered pharmacological insight and I have said so.

**What IS being claimed**, specifically:

1. **Every hypothesis the traditional corpus generates for DR is already covered by the
   modern candidate set, usually in a better-characterised form.** Tradition's contribution
   would be "polyphenols and fatty acids engage lipid and inflammatory biology." Group B
   already contains the fatty acids with actual binding data and the one dosable product
   (icosapent ethyl) that delivers them at a pharmacological dose; Group C already contains
   quercetin as an explicit frequent-hitter control. **Tradition adds no compound, no target
   and no mechanism that is not already in the set.**

2. **The project's data cannot support an ethnobotanical analysis of DR even in principle.**
   13 plants, of which 4 have no uses and 4 have no chemistry; 6 with verified eye/diabetes
   MeSH terms, none naming a retinal condition; a second "uses" file that is 99.6% empty and
   silently *fails to replicate* the first; and a compound matrix containing **none** of the
   plants or marker molecules any tradition actually uses for this disease. Absence is not
   evidence of absence — the disease model was right to say so — but it is a hard ceiling on
   what I can conclude.

3. **The one quantitative argument that looked like it favoured tradition — chemotype
   convergence — is an artifact**, and demonstrating that is the most useful thing in this
   report. It is a negative result that **removes** a scoring criterion rather than adding one.

4. **The PPARα-natural-product bridge does not carry load.** The arithmetic is unambiguous:
   terpenoids fall 100–1000× short; fatty acids fail for the opposite reason — the receptor's
   ligand pool is endogenously saturated and homeostatically buffered, and the vehicle out-doses
   the herb 40:1. **No traditional preparation delivers a PPARα-active dose of anything.**

**The honest ethnobotanical summary of diabetic retinopathy is this:** it is a disease of
industrial-era longevity and industrial-era glycemic exposure, whose pathology develops over
15+ years in a population that historically did not survive to accumulate it, in a tissue no
pre-modern practitioner could see. There is no plausible mechanism by which empirical
traditional observation could have accumulated knowledge of it. **The traditions have genuine
knowledge of diabetes and genuine knowledge of eye disease; the conjunction is a modern
retrofit.** Reporting that is more useful than manufacturing a candidate.

---

## 7. What the null finding is nonetheless worth

Four things the ranker should actually take from this:

1. **Strike "n DR targets hit" from the scoring criteria.** §3 shows it is bibliometric. If
   breadth is scored at all, score the **action ratio** (scout §3.1) and weight DR-specific
   genes (AKR1B1 by genuine inhibition, PRKCB, KDR, AGER, ANGPT2) rather than the generic
   TNF/CASP3/IL6/BAX/BCL2 stress block that 62–84% of compounds annotate.

2. **Two QC defects are now documented**, one of them in the disease model's own analysis
   (§2.1, §2.2). Any downstream agent quoting "8 of 13 IMPPAT plants" should quote **6 of 13**,
   and should know that the second uses file disconfirms rather than corroborates.

3. **The access/affinity anti-correlation (§4.4)** is a real structural finding about the
   PPARα ligand class that generalises beyond natural products and sharpens the pipeline's
   central question.

4. **The penetration-enhancement concept (§5.1)** is the only genuinely non-redundant idea
   tradition offers — and it carries a wrong-sign objection severe enough that surfacing the
   objection is the contribution, not the idea.

---

## 8. Candidate assessments

### B1 — Linoleic acid — **2/10**
Real, replicated binding-plus-activation evidence across ≥4 PMIDs with coactivator recruitment
(NCOA1/NCOA2/CREBBP) — the best-evidenced PPARα natural product in the file. It is nonetheless
not a candidate: non-selective (binds and activates PPARγ too, carrying that isoform's
macular-oedema liability), permanently anionic, cLogP ~7, 14 rotatable bonds, >99.9%
albumin-bound, and — decisively — **endogenously present at 35–95 µM, at or above its own
EC50, continuously.** Plant sources deliver 25–90 mg against a 12,000–17,000 mg/day dietary
background. Pathway P8, stage S0–S3, compartment systemic; oral route is moot.
*Strengths:* genuine binding evidence; validates the fatty-acid-sensor mechanism.
*Concerns:* saturated endogenously; non-selective; §6.2 failure on four axes; not a drug.

### B2 — α-Linolenic acid — **2/10**
Identical analysis to B1 (binds and activates, PMIDs 10403814/16731579/19667161; also
activates PPARγ). Marginally better theoretical case as an ω-3 whose downstream metabolites
have independent anti-inflammatory biology, but ALA→EPA conversion in humans is <5–10% and
poorer still in males and in insulin resistance — which is this population. Same saturation
and §6.2 failures. **Its only meaningful route to a dose is the pharmaceutical ω-3 product
(B4), not a plant.**

### B3 — Linalool — **3/10**
The most interesting failure in the set. Carries the **best single piece of PPARα pharmacology
among natural products** — a receptor-mutant dependency row (`PPARA gene mutant form results
in decreased susceptibility to linalool`, PMID 24752549) plus PPARα-dependent SLC27A4
induction — and it **passes every §6.2 criterion**: MW 154, cLogP ~3.0, TPSA 20, 1 HBD, 4
rotatable bonds, neutral, low PPB. That combination (BRB-permeant + PPARα-touching) is rare
and genuinely worth noting. It fails on dose: *Cyperus rotundus* delivers ~1.6 mg against an
idealised 162 mg requirement, a 100× shortfall before accounting for near-complete first-pass
oxidation and a half-life of minutes to hours. Single-source evidence. **Score it as a
chemical starting point, not a candidate.** P8/P6, S0–S2, neural retina reachable, oral.
*Falsifier for any higher score:* an oral PK study showing sustained plasma linalool ≥10 µM at
a tolerated dose. I do not expect one to exist.

### B4 — Icosapent ethyl — **5/10** *(assessed only within my remit)*
**The only member of the traditional-chemistry class that reaches a pharmacological dose.**
4,000 mg/day of a single >96%-pure ω-3 ethyl ester is ~45× any herbal fatty-acid contribution
and large enough to shift plasma fatty-acid composition measurably — which is precisely the
point §4.3 makes: this chemotype becomes a drug only when it stops being a plant. Chemically
continuous with the B1/B2 binding evidence. Hydrolysed to EPA, which is anionic, >99%
protein-bound and cLogP ~6.5, so **retinal PPARα engagement remains implausible**; any benefit
would be systemic (triglyceride-rich remnant lowering, P8.1/P8.2) plus EPA's
PPARα-independent membrane and eicosanoid biology. Pathway P8 primary, P6 secondary; stage
S0–S3; compartment systemic rather than retinal; oral, chronic, well tolerated in renal
impairment — a genuine fit to the §5 population where most PPAR-class agents are not.
*Concerns:* bleeding risk on antiplatelets (common in this population); atrial-fibrillation
signal in the ω-3 class; large pill burden; mechanism likely systemic-only. Scored 5 rather
than higher because **I cannot assess its DR-specific plausibility from an ethnobotanical
remit** — defer to the ADMET and clinical agents.
*Falsifier for 7+:* evidence that systemic triglyceride lowering of this magnitude does not
alter retinal lipid handling.

### C1 — Quercetin — **2/10**
My analysis **strengthens** the case against it. Its 26/27 target breadth is the clearest
single illustration of §3: it has 745 CTD rows, more than the next two compounds combined, an
action ratio of 0.35, and it is a textbook assay frequent-hitter (catechol redox cycling and
H₂O₂ generation in media, fluorescence quenching, colloidal aggregation, promiscuous ATP-pocket
binding). Its PPARα record is not merely weak but **direction-incoherent** — PMID 18393431 has
quercetin *antagonising* GW 7647. §6.2: TPSA 131, 5 HBD, oral bioavailability <2% with
near-complete first-pass glucuronidation and sulfation; the circulating species are conjugates,
not the aglycone. Present in 4 of 9 project plants, which is exactly the ubiquity that makes it
uninformative. **Carry only as the frequent-hitter negative control, as the scout proposed.**
*Concerns:* promiscuity as liability; direction-incoherent PPARα evidence; bioavailability;
its breadth is a bibliometric artifact.

### C2 — Melatonin — **4/10**
Not a traditional-medicine candidate in any meaningful sense (it is an endogenous indoleamine
that happens to appear in *Azadirachta indica*'s phytochemical list), so my remit is limited.
Within it: its PPARα evidence is among the weakest in the file — cisplatin-protection
expression rows only, no engagement. But it is **the one compound in the entire set with
unambiguously favourable retinal access** — MW 232, neutral, amphipathic, ~50% PPB, crosses
the BRB freely, and the retina physiologically synthesises it with its own receptors (MT1/MT2)
and circadian role. It is the correct **exposure control** for the pipeline's central question:
does access beat affinity? P9/P5, S0–S2, neural retina.
*Concerns:* PPARα claim does not survive scrutiny; "antioxidant" as the dominant mechanism is
explicitly on the brief's §4 lose-points list; sedation on chronic dosing.

### Not assessable from this remit
**A1 Fenofibric acid, A2 Fenofibrate, A3 Pemafibrate, A4 Elafibranor, A5 Seladelpar, D1
Epalrestat, D2 Dimethyl fumarate, D3 Minocycline, D4 Candesartan cilexetil** — synthetic
agents with no traditional-medicine dimension. Scoring them from an ethnobotanical remit would
be guessing. **Recorded as `not assessable`, deliberately, rather than assigned a number.**
One cross-remit note: **epalrestat (D1)** is the only candidate addressing AKR1B1 with genuine
inhibitory pharmacology, which matters given §3.3's finding that the project's 22 "AKR1B1
hits" are largely sugars that are aldose-reductase *substrates*.

---

## 9. Blinding Compliance Statement

**Files read (all within permitted paths):**
- `data/reports/disease-explorer/diabetic-retinopathy/2026-10-05/disease-brief.md` (full)
- `.../disease-model.md` §5.2, §6.1–6.4, §7 (full), §8
- `.../agents/p0-ppara-scout.md` §2, §3, §6, §7
- `.claude/skills/ethnobotany-expert/SKILL.md`
- `data/processed-blinded-diabetic-retinopathy/imppat_plant_therapeutic_uses.json`
- `data/processed-blinded-diabetic-retinopathy/imppat_plant_part_phytochemicals.json`
- `data/processed-blinded-diabetic-retinopathy/medicinal_plants_with_uses.csv`
- `data/processed-blinded-diabetic-retinopathy/phytochem_imppatid_pubchem_id_url.csv`
- `data/processed-blinded-diabetic-retinopathy/chembl_natural_products.csv` (header + grep)
- `.../evidence/compound-dr-target-matrix.tsv`, `ppara-interactions.tsv`,
  `ppar-class-drug-properties.tsv`

**Files NOT read, deliberately:** `data/processed/` (the unblinded tree) in its entirety;
`data/holdout/` in its entirety; anything named `answer-key*`. I did not use git history, git
objects, or any other route to recover redacted values, and I made no attempt to infer which
rows were redacted. I listed `data/processed-blinded-diabetic-retinopathy/` and noted it
contains a `chembl_approved_drugs.csv`; **I did not open it**, since I had no need of it and
the brief names a file of that name as sensitive.

**Did DR-specific knowledge influence my judgment? Disclosures, including negative ones:**

1. **Yes, in one scoped place, and it was assigned to me.** Task item (a) explicitly
   instructed me to appraise "TCM's DR-specific trial literature and its quality problems"
   and Western herbal DR traditions. §1.2 and §1.3 therefore discuss DR trials of Compound
   Danshen, Qiming granule, bilberry and pine-bark extract. This is **traditional-preparation
   trial evidence, not the indication status of any candidate**, it duplicates material the
   disease model itself placed in §7.2–7.3 and handed me, and **none of it concerns any of
   the 15 candidates** — none of those preparations or their marker compounds exists in the
   candidate set or the project data. **No score in this report was raised or lowered by it.**

2. **I did not use, and actively avoided seeking, the DR/DME indication status of any Group
   A–D candidate.** I hold general pharmacology for fenofibrate, pemafibrate, icosapent ethyl,
   minocycline, candesartan and epalrestat, and used only non-DR facts: PPARα EC50s and
   isoform selectivity, protein binding, elimination route, physicochemistry, and class safety.
   B4's score rests entirely on dose arithmetic, physicochemistry and the §5 population
   profile. I explicitly declined to reason about whether any candidate has DR precedent, and
   I scored B4 **down** to 5 partly because I would not substitute DR knowledge for the
   DR-specific assessment I cannot make from this remit.

3. **Negative decision disclosed.** I considered and rejected discussing lutein/zeaxanthin
   supplementation trials in retinal disease. Lutein is present in the project's matrix (5
   targets) and in two project plants, so it was legitimately in scope — but the trial
   literature I know is retinal-disease-specific, so I excluded it rather than risk leakage.
   Zeaxanthin is absent from the data in any case. Similarly, I avoided any statement about
   whether ω-3 supplementation has been studied for retinal endpoints.

4. **A genuine grey area, disclosed.** My §6 argument that DR is "a disease of industrial-era
   longevity ... no pre-modern practitioner could see" uses DR epidemiology and natural
   history (15+ year latency, ophthalmoscopy required for diagnosis). This is **disease
   knowledge, not drug-indication knowledge**, and protocol §1.3 permits general
   physiology and non-DR clinical knowledge — but the latency figure is DR-specific and the
   disease model states it openly at §1.2/§2. I judged it permitted and flag it for audit.

5. **No candidate's score was derived from DR trial or approval status, by inclusion or by
   exclusion.** Every score traces to: CTD evidence grade, the §4 dose arithmetic, the §6.2
   physicochemical rubric, and the §3 artifact analysis — all reproducible from the blinded
   files and the scripts described in this report.

---

## SCOREBLOCK

SCORE|Fenofibric acid|NA|low|knowledge-based|Synthetic fibrate; no traditional-use dimension to assess
SCORE|Fenofibrate|NA|low|knowledge-based|Synthetic ester prodrug; no traditional-use dimension to assess
SCORE|Pemafibrate|NA|low|knowledge-based|Designed SPPARMalpha; no traditional-use dimension to assess
SCORE|Elafibranor|NA|low|knowledge-based|Synthetic dual agonist; no traditional-use dimension to assess
SCORE|Seladelpar|NA|low|knowledge-based|Synthetic isoform control; no traditional-use dimension to assess
SCORE|Linoleic acid|2|high|data-backed|Real binding, but endogenously saturated; herbal dose is dietary rounding error
SCORE|Alpha-linolenic acid|2|high|data-backed|Same saturation problem; poor ALA-to-EPA conversion in insulin resistance
SCORE|Linalool|3|moderate|mixed|Best natural-product PPARalpha evidence and ideal physicochemistry, but 100-1000x dose shortfall
SCORE|Icosapent ethyl|5|low|mixed|Dosable only as pharmaceutical, not plant; traditional contribution itself nil
SCORE|Quercetin|2|high|data-backed|Frequent-hitter control; breadth bibliometric, PPARalpha evidence direction-incoherent, ubiquitous
SCORE|Melatonin|4|moderate|data-backed|Endogenous, not traditional; scored for retinal access, not ethnobotany
SCORE|Epalrestat|NA|low|knowledge-based|Synthetic ARI; no traditional-use dimension to assess
SCORE|Dimethyl fumarate|NA|low|knowledge-based|Synthetic NRF2 activator; no traditional-use dimension to assess
SCORE|Minocycline|NA|low|knowledge-based|Semisynthetic tetracycline; no traditional-use dimension to assess
SCORE|Candesartan cilexetil|NA|low|knowledge-based|Synthetic ARB; no traditional-use dimension to assess
