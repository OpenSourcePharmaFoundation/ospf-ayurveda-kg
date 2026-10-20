# Holdout Blinding Protocol — Diabetic Retinopathy Benchmark Run
Date: 2026-10-05
Purpose: Run the discovery pipeline without access to which drugs are already used for
diabetic retinopathy, so a later scoring step can measure rediscovery rate.

## What was blinded

Builder: `src/holdout/blind_dataset.py --disease diabetic-retinopathy`

- **Source (untouched):** `data/processed/`
- **Blinded tree (pipeline input):** `data/processed-blinded-diabetic-retinopathy/`
- **Answer key (pipeline must NOT read):** `data/holdout/diabetic-retinopathy/answer-key.json`

The original tree is never mutated. The blinded tree is a full copy with
indication text redacted, so an interrupted run cannot leave redacted data
sitting in the git-tracked `data/processed/`.

## Redaction rule

Semicolon-delimited indication terms matching any of these are dropped from
`indication_class` and `therapeutic_areas` in `chembl_approved_drugs.csv`:

retinopath · macular (o)edema · macular retinal edema · macular degeneration ·
vitreoretinopath · choroidal neovascular · retinal neovascular · diabetic macular ·
retinal vein occlusion · wet mac

Result: **154 cells redacted across 79 drugs.** Verification sweep over the whole
blinded tree returns **0 residual matches**.

### Hardening after the Phase 0 scout report

The first build wrote a visible `[REDACTED-HOLDOUT]` marker when every term in a
field was removed, and left a stray leading separator when only the first term was
removed. The PPARα scout noticed the markers, correctly declined to exploit them,
and disclosed the count — which is exactly the right behaviour and also proof that
the side channel was real. A marker says "this drug had an ocular indication"
without naming it, which reconstructs much of the key by elimination.

The scrubber now rejoins surviving terms cleanly and leaves a fully-scrubbed field
empty. A scrubbed row is indistinguishable from an ordinary one: pemafibrate and
ciprofibrate now read identically, and 660 of 3,276 drugs have an empty
`therapeutic_areas` field in the untouched source, so emptiness carries no signal.
The tree was regenerated before Phase 1. Zero `REDACTED` strings remain.

## What was deliberately NOT blinded

- Diabetes, metabolic, dyslipidemia and cardiovascular indications. These are
  background disease context, not a statement about retinopathy treatment.
  Fenofibrate retains "Dyslipidemias; Metabolic Syndrome; Hypercholesterolemia"
  and loses only "Diabetic Retinopathy".
- All target-interaction data (`pubchem_*`, `chembl_drug_targets.csv`,
  `chembl_drug_mechanisms.csv`) — byte-identical to source. PPARA biology is the
  signal under test, not the answer.
- Non-ocular indications of redacted drugs.

## Correction to the earlier inventory

A previous partial run recorded "ChemBL Drug Indications — Hits for DR: 0" and
concluded the dataset carried no DR indication data. That check only covered
`chembl_drug_indications.csv` (which genuinely has 0 DR rows). It missed
`chembl_approved_drugs.csv`, where 44 drugs carry retinopathy/macular-edema terms
in free-text columns, **including both PPARα agonists in the dataset**. Running
unblinded on that basis would have been a leaked benchmark.

## Known limitation — model priors are not blinded

Dataset blinding removes the project's *data* signal. It cannot remove what the
language model already knows from training (e.g. fenofibrate's FIELD and ACCORD-Eye
results). This run therefore measures mechanistic-path plausibility under data
blinding, not true naive rediscovery.

Mitigation applied: discovery agents (Phases 1-3) are instructed to reason from
mechanism and blinded data and NOT to cite or rely on known DR indication/trial
status as evidence. The Literature Reviewer is permitted to surface DR-specific
trial evidence but must confine it to a clearly separated POST-HOC UNBLINDING
section, which is excluded from scoring inputs. The final report records both
the blinded ranking and the post-hoc check separately.
