"""Five concrete scaffolds, costed end to end.

Step 7 of ``docs/prompts/dr-solve-open-questions-prompt.md``.

Each scaffold is carried through the whole chain in one place: structure ->
descriptors -> logD -> free fraction -> retinal partition -> occupancy ->
efficacy -> net transcriptional output, against fenofibric acid as the
incumbent.  Doing it in one module is the point.  The failure this chain exists
to correct was a term being quoted as if it were the product, and the only
reliable defence is to never compute a term without computing the product.

The retinal partition is **not** re-derived here.  It comes from the Step 5
model in ``src/analysis/ocular_exposure``, which is calibrated against the one
measured ocular concentration of a fibrate after systemic dosing that exists.
These scaffolds are fed to it as ordinary compounds.

What is computed, and what is assumed
--------------------------------------
Computed: every descriptor (RDKit), logD from cLogP and the assigned pKa,
retinal Kp,uu and the free-drug margin (Step 5 model), Emax (the H12 model in
``h12_efficacy``), and the product.

Assumed, with ranges: the pKa of each head type; plasma clearance, because
there is no compound to measure; potency, which is argued from ligand
efficiency and acceptor basicity rather than measured; and the free-fraction
relationship below.  **None of these is a measurement and the note says so for
each one.**  A predicted potency for a molecule nobody has made is an opinion
with error bars, and the honest treatment is to show how wide the bars are.
"""

from __future__ import annotations

import csv
import dataclasses
import math
import pathlib

import numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem import Crippen, Descriptors, QED, rdMolDescriptors

from ..ocular_exposure import model as oc_model
from ..ocular_exposure import potency as oc_potency
from ..ocular_exposure.compounds import Compound
from ..ocular_exposure.parameters import ASSUMED, Param
from . import h12_efficacy

RDLogger.DisableLog("rdApp.*")

_REPO = pathlib.Path(__file__).resolve().parents[3]
OUT = _REPO / "data" / "processed" / "ppara_nonacidic_scaffolds.tsv"

N_DRAWS = 100_000
SEED = 20261109

# --- free fraction ---------------------------------------------------------
#
# Fitting this on the four Step 5 compounds was tried and rejected, and the
# reason is a result rather than a technicality.  Across fenofibric acid,
# pemafibrate, elafibranor and seladelpar, fu moves only ~2-fold while logD
# moves ~1.7 log units - a slope near 0.2, against the 0.5-0.7 that lipophilic
# binding gives.  Their binding is dominated by albumin site-II *anion*
# recognition, not by lipophilicity, so the acid series is not a valid anchor
# for a neutral ligand.  That is precisely why going neutral is interesting,
# and precisely why the neutral relationship has to come from elsewhere.
#
#     log10(1/fu - 1) = A + B * logD(7.4)
#
# B is the lipophilicity slope for neutral drugs.  A carries the scatter, which
# is large: spot-checked against propranolol (logD 1.2, fu 0.13 -> predicted
# 0.12) and diazepam (logD 2.8, fu 0.02 -> predicted 0.018) it is good, and
# against carbamazepine (fu 0.26 -> predicted 0.03) it is an order of magnitude
# out.  The A range below spans roughly that scatter rather than hiding it.
FU_SLOPE_B = (0.45, 0.70)
FU_INTERCEPT_A = (-0.60, 0.60)

# For an *anionic* head the same equation must not be used, and the reason is
# the finding above: these acids are bound by charge, not by lipophilicity, so
# a logD-driven relation fitted to neutrals predicts fenofibric acid to be ~80%
# unbound when it is measured at 1%.  The anion branch is therefore anchored
# directly on the four Step 5 compounds: slope 0.2 (their observed fu-vs-logD
# behaviour) and an intercept set to reproduce fenofibric acid's measured
# fu = 0.01 at its logD of -0.49, with the range spanning the measured
# 0.005-0.02 interval.  Cross-check: this returns fu = 0.0045 for pemafibrate
# at logD 1.25, inside its measured 0.001-0.02.
FU_ANION_SLOPE_B = (0.15, 0.25)
FU_ANION_INTERCEPT_A = (1.70, 2.40)

# Below this pKa a head is >95% ionised at pH 7.4 and takes the anion branch.
ANION_PKA_CUTOFF = 6.0

# --- potency ---------------------------------------------------------------
#
# Potency is *derived* rather than asserted, from lipophilic ligand efficiency:
#
#     pEC50 = LLE + logP
#
# The source run's SAR analysis tabulates LLE across the PPARalpha ligand set
# and the split in that table is the whole argument of this module:
#
#     anionic heads   pemafibrate 3.45, elafibranor 2.3, fenofibric acid 0.9
#     neutral heads   oleoylethanolamide 1.0, linalool 1.1
#
# Its section 7.1 then sets a design target of LLE 3.5 and justifies it with
# "pemafibrate already demonstrates LLE 3.45".  That transfers an *anionic*
# LLE onto a *neutral* design.  The two neutral ligands in its own table sit at
# LLE ~1.0, two and a half log units below, and the acceptor-basicity argument
# in section 1.2 of that same report predicts exactly such a gap.  So the
# neutral LLE ceiling is set from the neutral data, not the anionic data, and
# the deficit is scaled by how much acceptor basicity each head gives up
# against a carboxylate - with oleoylethanolamide as the calibration point.
# The penalty range is not asserted: it is set so the model reproduces the one
# neutral PPARalpha ligand with a measured EC50.  ``calibration_check`` below
# runs that test and it is the reason to believe any potency figure in this
# module - oleoylethanolamide, logP 5.9, neutral amide-alcohol head, predicted
# ~126 nM against a measured 120 nM - 3 uM.
LLE_ANION = (2.0, 3.5)  # the demonstrated anionic range
LLE_PENALTY_AT_OEA = (1.0, 2.5)  # LLE units a fully neutral head gives up
PKBHX_CARBOXYLATE_MID = 4.55
PKBHX_OEA_MID = 1.55

# Oleoylethanolamide, the calibration point.
OEA_LOGP = 5.9
OEA_MEASURED_EC50_nM = (120.0, 3000.0)


@dataclasses.dataclass(frozen=True)
class Scaffold:
    key: str
    name: str
    smiles: str
    head: str  # key into h12_efficacy.HEADS
    head_label: str
    pka: tuple[float, float] | None  # None = not ionisable
    pka_basis: str
    # Acceptor basicity of the atom that serves His440/Tyr464.  Potency is
    # derived from this via LLE, not asserted.
    pkbhx_distal: tuple[float, float]
    ec50_basis: str
    dose_mg: float
    clearance_l_h: tuple[float, float]
    selectivity_strategy: str
    breaks_first: str
    rationale: str


SCAFFOLDS = (
    Scaffold(
        key="OXZ-1",
        name="4-Aryl-oxazolidin-2-one, sulfone-capped diaryl ether",
        smiles="O=C1OCC(N1)c1ccc(cc1)Oc1ccc(cc1)S(C)(=O)=O",
        head="oxazolidinone",
        head_label="oxazolidin-2-one",
        pka=None,
        pka_basis="cyclic carbamate; not ionisable at physiological pH",
        pkbhx_distal=(2.3, 2.6),
        ec50_basis=(
            "the only neutral head that reproduces the measured 2.22 A "
            "geminal pair; carbonyl distal acceptor at pK_BHX 2.3-2.6 against "
            "the carboxylate's 4.3-4.8, i.e. a 2-3 kcal/mol deficit spread "
            "over two contacts, anchored on OEA's measured 120 nM-3 uM"
        ),
        dose_mg=100.0,
        clearance_l_h=(5.0, 20.0),
        selectivity_strategy=(
            "geometric: hold the acceptor span at 2.2-2.3 A. Measured here, "
            "PPARgamma's engaged acceptors span 4.46 A, so a tight geminal "
            "pair is intrinsically alpha-shaped. Against delta, which also "
            "takes a tight pair (3TKM, 2.10 A), geometry gives nothing - "
            "delta must be bought on arm II sterics and counter-screened"
        ),
        breaks_first=(
            "PPARdelta selectivity. Delta's cage accepts the same tight "
            "geminal pair this head is built around, delta is the most "
            "abundant retinal PPAR, and it is pro-angiogenic"
        ),
        rationale=(
            "the lead. Best measured geometric match of any neutral head "
            "(2.29 A against a required 2.22 +/- 0.06), permanently neutral, "
            "and the methylsulfonyl sits on the distal vector where polarity "
            "lowers logD without touching arm I"
        ),
    ),
    Scaffold(
        key="SULF-1",
        name="alpha,alpha-Dimethyl sulfonylmethyl aryl ether",
        smiles="CS(=O)(=O)CC(C)(C)Oc1ccc(cc1)-c1ccc(cc1)C#N",
        head="sulfone",
        head_label="methyl sulfone",
        pka=None,
        pka_basis="sulfone; not ionisable",
        pkbhx_distal=(1.3, 1.6),
        ec50_basis=(
            "geminal S-O pair at 2.52 A is inside the measured window, but "
            "sulfonyl oxygens are weak acceptors (pK_BHX 1.3-1.6), the "
            "largest basicity deficit of any competent head. Potency is "
            "projected low and the range is wide"
        ),
        dose_mg=200.0,
        clearance_l_h=(5.0, 20.0),
        selectivity_strategy=(
            "none from the head - a weak symmetric acceptor pair discriminates "
            "nothing. Selectivity must come entirely from arm II/III sterics, "
            "which is the weakest selectivity position of the five"
        ),
        breaks_first=(
            "potency. A 3 kcal/mol acceptor deficit against a receptor whose "
            "incumbent ligands are already only 1-30 nM is unlikely to be "
            "recovered from the arms alone"
        ),
        rationale=(
            "the cheapest test of the geometric hypothesis. Permanently "
            "neutral, smallest competent neutral head at 1.46x the "
            "carboxylate, trivially synthesised from the fibrate body. Its "
            "value is as an experiment, not as a candidate"
        ),
    ),
    Scaffold(
        key="PHOS-1",
        name="Methyl phosphonamidate, biaryl ether body",
        smiles="COP(=O)(N)COc1ccc(cc1)-c1ccc(OC)cc1",
        head="phosphonamidate",
        head_label="phosphonamidate",
        pka=None,
        pka_basis="phosphonamidate; not ionisable at physiological pH",
        pkbhx_distal=(3.0, 3.5),
        ec50_basis=(
            "P=O is the strongest neutral acceptor available (pK_BHX 3.0-3.5), "
            "a deficit of only ~1.3 units against the carboxylate. Offsetting "
            "that, the computed geminal span is 2.58 A - outside the measured "
            "window, so some of the advantage is spent on strain"
        ),
        dose_mg=50.0,
        clearance_l_h=(3.0, 15.0),
        selectivity_strategy=(
            "the P centre is stereogenic, so the two P-substituents can be "
            "used to probe arm I asymmetry directly - a selectivity handle "
            "none of the carbon heads has"
        ),
        breaks_first=(
            "the span. 2.58 A is 0.36 A wide of the measured requirement and "
            "a tetrahedral P cannot be compressed the way an sp2 carbon can. "
            "After that, metabolic and hydrolytic stability of the P-N bond"
        ),
        rationale=(
            "the highest-information scaffold in the set and the one nobody "
            "has tried at any PPAR. Strongest neutral acceptors, lowest "
            "protein binding of the five, not an OATP1B recognition element"
        ),
    ),
    Scaffold(
        key="ACID-LOW",
        name="Fibrate acid retained, lipophilicity stripped",
        smiles="CC(C)(Oc1ccc(cc1)-c1ccncc1)C(O)=O",
        head="carboxylate",
        head_label="carboxylate (control arm)",
        pka=(3.0, 3.5),
        pka_basis="2-aryloxy-2-methylpropanoic acid, measured",
        pkbhx_distal=(4.3, 4.8),
        ec50_basis=(
            "the head is the validated one, so potency is set by the body. "
            "Stripping the lipophilic arm costs affinity against pemafibrate "
            "but the chemotype's SAR transfers directly"
        ),
        dose_mg=100.0,
        clearance_l_h=(1.0, 5.0),
        selectivity_strategy=(
            "the carboxylate is itself part of alpha selectivity, which is "
            "the strongest starting position of the five"
        ),
        breaks_first=(
            "nothing in the chemistry - the exposure. It is still an anion, "
            "so OATP1B hepatic uptake and MRP/BCRP efflux at the barrier "
            "both persist. This arm exists to show what the acid can and "
            "cannot do once lipophilicity is removed as a confound"
        ),
        rationale=(
            "the control. If this closes the exposure gap, no neutral head is "
            "needed and the programme is a medicinal-chemistry tidy-up rather "
            "than a new chemotype. It is included to be falsified"
        ),
    ),
    Scaffold(
        key="HYDX-1",
        name="Fibrate hydroxamic acid, benzophenone removed",
        smiles="ONC(=O)C(C)(C)Oc1ccc(cc1)-c1ccc(F)cc1",
        head="hydroxamic_acid",
        head_label="hydroxamic acid",
        pka=(8.5, 9.5),
        pka_basis="acetohydroxamic acid, measured",
        pkbhx_distal=(2.2, 2.8),
        ec50_basis=(
            "chelating O,O pair, smallest competent head at 1.27x the "
            "carboxylate, but the computed span is 2.64 A - outside the "
            "measured window - so the H12 contact is modelled as lost"
        ),
        dose_mg=150.0,
        clearance_l_h=(8.0, 30.0),
        selectivity_strategy=(
            "footprint. At 1.27x it is the only neutral head small enough to "
            "exploit alpha's arm I being tighter than gamma's"
        ),
        breaks_first=(
            "off-target metal chelation. A hydroxamate is a zinc binder: HDAC, "
            "the matrix metalloproteinases and carbonic anhydrase are all in "
            "range, and MMP inhibition in retina is not a neutral liability. "
            "Hydroxamate mutagenicity via Lossen rearrangement is the second"
        ),
        rationale=(
            "included because it is the smallest neutral competent head and "
            "the footprint argument is the one the source analysis leaned on. "
            "Carried with its liabilities stated rather than quietly dropped"
        ),
    ),
)


# --- descriptors -----------------------------------------------------------


def descriptors(smiles: str) -> dict[str, float]:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"bad SMILES: {smiles}")
    return {
        "mw": Descriptors.MolWt(mol),
        "clogp": Crippen.MolLogP(mol),
        "tpsa": Descriptors.TPSA(mol),
        "hbd": rdMolDescriptors.CalcNumHBD(mol),
        "hba": rdMolDescriptors.CalcNumHBA(mol),
        "rtb": rdMolDescriptors.CalcNumRotatableBonds(mol),
        "rings_aromatic": rdMolDescriptors.CalcNumAromaticRings(mol),
        "heavy_atoms": mol.GetNumHeavyAtoms(),
        "qed": QED.qed(mol),
        "fsp3": rdMolDescriptors.CalcFractionCSP3(mol),
    }


def free_fraction(logd: np.ndarray, rng, anionic: bool) -> np.ndarray:
    """Fraction unbound in plasma, on the branch that matches the charge state.

    Using the neutral branch for an anion is not a small error: it predicts
    fenofibric acid at ~80% unbound against a measured 1%.
    """
    n = len(logd)
    if anionic:
        a = rng.uniform(*FU_ANION_INTERCEPT_A, n)
        b = rng.uniform(*FU_ANION_SLOPE_B, n)
    else:
        a = rng.uniform(*FU_INTERCEPT_A, n)
        b = rng.uniform(*FU_SLOPE_B, n)
    return np.clip(1.0 / (1.0 + 10.0 ** (a + b * logd)), 1e-5, 1.0)


# --- putting a scaffold through the Step 5 model ---------------------------


def as_compound(
    s: Scaffold,
    d: dict[str, float],
    fu_med: float,
    c_avg_ng_ml: tuple[float, float, float],
) -> Compound:
    """Wrap a scaffold so the Step 5 ocular model can evaluate it.

    pKa for a non-ionisable head is set to 14, which makes
    Henderson-Hasselbalch return logD = logP - i.e. the neutral case - without
    needing a separate code path inside the Step 5 model.
    """
    lo, med, hi = c_avg_ng_ml
    pka = s.pka or (14.0, 14.0)
    return Compound(
        key=s.key,
        name=s.name,
        chembl="",
        mw=d["mw"],
        logp=d["clogp"],
        pka=Param.uniform(
            f"pka.{s.key}",
            pka[0],
            pka[1],
            units="pKa",
            provenance=ASSUMED,
            source=s.pka_basis,
        ),
        dose_mg=s.dose_mg,
        c_avg=Param.lognormal_ci(
            f"c_avg.{s.key}",
            med,
            lo,
            hi,
            units="ng/mL",
            provenance=ASSUMED,
            source=f"{s.dose_mg:g} mg/day over an assumed "
            f"CL/F of {s.clearance_l_h[0]:g}-"
            f"{s.clearance_l_h[1]:g} L/h",
        ),
        c_max=Param.lognormal_ci(
            f"c_max.{s.key}",
            med * 2.5,
            lo * 2.5,
            hi * 2.5,
            units="ng/mL",
            provenance=ASSUMED,
            source="assumed peak-to-average ratio 2.5",
        ),
        fu_plasma=Param.lognormal_ci(
            f"fu.{s.key}",
            fu_med,
            fu_med / 4.0,
            fu_med * 4.0,
            units="fraction",
            provenance=ASSUMED,
            source="neutral-drug logD-PPB relation",
        ),
        ec50_gene="PPARA",
        pk_source="assumed - no compound exists",
        note=s.rationale,
    )


def derived_ec50_nM(s: Scaffold, clogp: float, rng, n: int) -> np.ndarray:
    """EC50 derived from lipophilic ligand efficiency, not asserted.

        pEC50 = LLE + logP

    with the LLE ceiling taken from the anionic series and then reduced, for a
    neutral head, in proportion to the acceptor basicity it gives up against a
    carboxylate.  Oleoylethanolamide calibrates the scale: it gives up the most
    basicity of any ligand with a measured PPARalpha EC50, and it sits 1.8-3.0
    LLE units below pemafibrate.
    """
    lle = rng.uniform(*LLE_ANION, n)
    pkbhx = rng.uniform(*s.pkbhx_distal, n)
    deficit = np.clip(PKBHX_CARBOXYLATE_MID - pkbhx, 0.0, None)
    penalty = rng.uniform(*LLE_PENALTY_AT_OEA, n) * (
        deficit / (PKBHX_CARBOXYLATE_MID - PKBHX_OEA_MID)
    )
    pec50 = lle - penalty + clogp
    return 10.0 ** (9.0 - pec50)  # nM


def calibration_check(n: int = 200_000, seed: int = SEED) -> dict[str, float]:
    """Predict oleoylethanolamide's EC50 and compare with the measured value.

    This is the test that decides whether the derived potencies mean anything.
    OEA is the only neutral ligand in the set with a measured PPARalpha EC50,
    so it is the only available anchor for the neutral branch of the LLE model.
    If this check drifts away from the measured 120 nM - 3 uM band, every
    potency in this module is wrong by the same factor.
    """
    rng = np.random.default_rng(seed)
    lle = rng.uniform(*LLE_ANION, n)
    penalty = rng.uniform(*LLE_PENALTY_AT_OEA, n)  # OEA is the full deficit
    ec50 = 10.0 ** (9.0 - (lle - penalty + OEA_LOGP))
    lo, med, hi = _q(ec50)
    return {
        "predicted_median_nM": med,
        "predicted_lo_nM": lo,
        "predicted_hi_nM": hi,
        "measured_lo_nM": OEA_MEASURED_EC50_nM[0],
        "measured_hi_nM": OEA_MEASURED_EC50_nM[1],
        "in_band": float(OEA_MEASURED_EC50_nM[0] <= med <= OEA_MEASURED_EC50_nM[1]),
    }


def potency_from_draws(s: Scaffold, ec50: np.ndarray) -> oc_potency.Potency:
    """Wrap a derived EC50 sample as a Potency for the Step 5 model.

    The model samples a lognormal from a median and a geometric SD, so the
    derived distribution is summarised that way.  The spread is real - it is
    the LLE range and the basicity range propagated - and must survive, which
    is why the gsd is taken from the sample rather than floored at a default.
    """
    log_e = np.log(ec50)
    return oc_potency.Potency(
        gene="PPARA",
        chembl=s.key,
        n_determinations=0,
        median_nM=float(np.exp(np.median(log_e))),
        gsd=float(np.exp(np.std(log_e))),
        censored_nM=(),
        values_nM=(),
    )


@dataclasses.dataclass
class Profile:
    scaffold: Scaffold
    desc: dict[str, float]
    logd: tuple[float, float, float]
    fu: tuple[float, float, float]
    ec50_nM: tuple[float, float, float]
    kpuu_neural_retina: tuple[float, float, float]
    margin_endothelium: tuple[float, float, float]
    margin_neural_retina: tuple[float, float, float]
    emax_tissue: tuple[float, float, float]
    output_endothelium: tuple[float, float, float]  # margin x Emax
    fold_vs_fenofibric: float
    # Dose that would put free retinal endothelium concentration at the free
    # EC50, after the efficacy loss.  This is the number that decides the
    # scaffold, because it is the one that does not depend on the arbitrary
    # starting dose: everything upstream scales linearly with dose.
    dose_for_occupancy_mg: tuple[float, float, float]


def _q(x, qs=(2.5, 50, 97.5)):
    return tuple(float(v) for v in np.percentile(x, qs))


def evaluate(
    s: Scaffold, rng, emax_by_head: dict[str, np.ndarray], n: int = N_DRAWS
) -> Profile:
    d = descriptors(s.smiles)

    pka_draw = rng.uniform(s.pka[0], s.pka[1], n) if s.pka else None
    logd = (
        d["clogp"] - np.log10(1.0 + 10.0 ** (7.4 - pka_draw))
        if pka_draw is not None
        else np.full(n, d["clogp"])
    )
    anionic = s.pka is not None and 0.5 * (s.pka[0] + s.pka[1]) < ANION_PKA_CUTOFF
    fu = free_fraction(logd, rng, anionic=anionic)

    # Steady-state average plasma concentration from dose and assumed CL/F.
    cl = rng.uniform(*s.clearance_l_h, n)
    c_avg = s.dose_mg / (cl * 24.0) * 1000.0  # ng/mL
    c_lo, c_med, c_hi = _q(c_avg)

    ec50 = derived_ec50_nM(s, d["clogp"], rng, n)
    cmp = as_compound(s, d, float(np.median(fu)), (c_lo, c_med, c_hi))
    res = oc_model.run(cmp, potency_from_draws(s, ec50), n=n, seed=SEED)

    emax = emax_by_head[s.head][:n]
    out_endo = res.margins["endothelium"] * emax

    # Everything from plasma concentration onwards is linear in dose, so the
    # dose that would reach an effective margin of 1 is just the starting dose
    # scaled by the shortfall.  Reporting this instead of a fixed-dose margin
    # removes the arbitrary choice of starting dose from the comparison.
    dose_needed = s.dose_mg / np.clip(out_endo, 1e-12, None)

    return Profile(
        scaffold=s,
        desc=d,
        logd=_q(logd),
        fu=_q(fu),
        ec50_nM=_q(ec50),
        kpuu_neural_retina=_q(res.kpuu_neural_retina),
        margin_endothelium=_q(res.margins["endothelium"]),
        margin_neural_retina=_q(res.margins["neural_retina"]),
        emax_tissue=_q(emax),
        output_endothelium=_q(out_endo),
        fold_vs_fenofibric=float("nan"),
        dose_for_occupancy_mg=_q(dose_needed),
    )


def reference_output(n: int = N_DRAWS) -> float:
    """Fenofibric acid's retinal endothelium margin, as a full agonist.

    Efficacy is 1.0 by definition for the carboxylate, so the reference output
    is the margin itself.  Taken from the Step 5 model unchanged.
    """
    from ..ocular_exposure.compounds import FENOFIBRIC_ACID

    pot = oc_potency.load(FENOFIBRIC_ACID.chembl, "PPARA")
    res = oc_model.run(FENOFIBRIC_ACID, pot, n=n, seed=SEED)
    return float(np.median(res.margins["endothelium"]))


def run(n: int = N_DRAWS, seed: int = SEED) -> list[Profile]:
    rng = np.random.default_rng(seed)
    eff = {e.head.key: e.emax_tissue for e in h12_efficacy.run(n=n, seed=seed)}
    ref = reference_output(n)
    out = []
    for s in SCAFFOLDS:
        p = evaluate(s, rng, eff, n=n)
        p.fold_vs_fenofibric = p.output_endothelium[1] / ref
        out.append(p)
    return out


def write(rows: list[Profile]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(
            [
                "key",
                "name",
                "smiles",
                "head",
                "mw",
                "clogp",
                "tpsa",
                "hbd",
                "hba",
                "rtb",
                "aromatic_rings",
                "heavy_atoms",
                "qed",
                "fsp3",
                "logd74_med",
                "logd74_lo",
                "logd74_hi",
                "fu_med",
                "fu_lo",
                "fu_hi",
                "ec50_derived_nM_med",
                "ec50_derived_nM_lo",
                "ec50_derived_nM_hi",
                "kpuu_neural_retina_med",
                "kpuu_neural_retina_lo",
                "kpuu_neural_retina_hi",
                "margin_endothelium_med",
                "margin_endothelium_lo",
                "margin_endothelium_hi",
                "margin_neural_retina_med",
                "emax_tissue_med",
                "emax_tissue_lo",
                "emax_tissue_hi",
                "output_endothelium_med",
                "output_endothelium_lo",
                "output_endothelium_hi",
                "fold_vs_fenofibric_acid",
                "dose_for_occupancy_mg_med",
                "dose_for_occupancy_mg_lo",
                "dose_for_occupancy_mg_hi",
                "pkbhx_distal_lo",
                "pkbhx_distal_hi",
                "ec50_basis",
                "selectivity_strategy",
                "breaks_first",
                "rationale",
            ]
        )
        for p in rows:
            s, d = p.scaffold, p.desc
            w.writerow(
                [
                    s.key,
                    s.name,
                    s.smiles,
                    s.head_label,
                    f"{d['mw']:.1f}",
                    f"{d['clogp']:.2f}",
                    f"{d['tpsa']:.1f}",
                    int(d["hbd"]),
                    int(d["hba"]),
                    int(d["rtb"]),
                    int(d["rings_aromatic"]),
                    int(d["heavy_atoms"]),
                    f"{d['qed']:.2f}",
                    f"{d['fsp3']:.2f}",
                    f"{p.logd[1]:.2f}",
                    f"{p.logd[0]:.2f}",
                    f"{p.logd[2]:.2f}",
                    f"{p.fu[1]:.4f}",
                    f"{p.fu[0]:.4f}",
                    f"{p.fu[2]:.4f}",
                    f"{p.ec50_nM[1]:.4g}",
                    f"{p.ec50_nM[0]:.4g}",
                    f"{p.ec50_nM[2]:.4g}",
                    f"{p.kpuu_neural_retina[1]:.4f}",
                    f"{p.kpuu_neural_retina[0]:.4f}",
                    f"{p.kpuu_neural_retina[2]:.4f}",
                    f"{p.margin_endothelium[1]:.4g}",
                    f"{p.margin_endothelium[0]:.4g}",
                    f"{p.margin_endothelium[2]:.4g}",
                    f"{p.margin_neural_retina[1]:.4g}",
                    f"{p.emax_tissue[1]:.3f}",
                    f"{p.emax_tissue[0]:.3f}",
                    f"{p.emax_tissue[2]:.3f}",
                    f"{p.output_endothelium[1]:.4g}",
                    f"{p.output_endothelium[0]:.4g}",
                    f"{p.output_endothelium[2]:.4g}",
                    f"{p.fold_vs_fenofibric:.1f}",
                    f"{p.dose_for_occupancy_mg[1]:.4g}",
                    f"{p.dose_for_occupancy_mg[0]:.4g}",
                    f"{p.dose_for_occupancy_mg[2]:.4g}",
                    s.pkbhx_distal[0],
                    s.pkbhx_distal[1],
                    s.ec50_basis,
                    s.selectivity_strategy,
                    s.breaks_first,
                    s.rationale,
                ]
            )


def main() -> None:
    cal = calibration_check()
    print("Calibration - oleoylethanolamide EC50 (the neutral-branch anchor)")
    print(
        f"  predicted {cal['predicted_median_nM']:.0f} nM "
        f"[{cal['predicted_lo_nM']:.0f}-{cal['predicted_hi_nM']:.0f}]  "
        f"measured {cal['measured_lo_nM']:.0f}-{cal['measured_hi_nM']:.0f} nM"
        f"  -> {'PASS' if cal['in_band'] else 'FAIL'}\n"
    )

    rows = run()
    write(rows)
    hdr = (
        f"{'key':9s} {'MW':>6s} {'logD':>5s} {'fu':>7s} {'Kp,uu':>6s} "
        f"{'margin':>9s} {'Emax':>6s} {'output':>9s} {'x FFA':>7s} "
        f"{'dose mg':>12s}"
    )
    print(hdr)
    print("-" * len(hdr))
    for p in rows:
        print(
            f"{p.scaffold.key:9s} {p.desc['mw']:6.1f} {p.logd[1]:5.2f} "
            f"{p.fu[1]:7.4f} {p.ec50_nM[1]:8.0f} {p.kpuu_neural_retina[1]:6.3f} "
            f"{p.margin_endothelium[1]:9.4f} {p.emax_tissue[1]:6.2f} "
            f"{p.output_endothelium[1]:9.4f} {p.fold_vs_fenofibric:7.1f} "
            f"{p.dose_for_occupancy_mg[1]:12.4g}"
        )
    print("\nmargin = free retinal endothelium concentration / free EC50")
    print("output = margin x Emax; x FFA = output relative to fenofibric acid")
    print("dose mg = oral dose/day that would put free retinal drug at the")
    print("          free EC50 after the efficacy loss (linear extrapolation)")
    print(f"\nwrote {OUT.relative_to(_REPO)}")


if __name__ == "__main__":
    main()


def logp_sweep(
    head_pkbhx=(2.3, 2.6),
    anionic=False,
    n: int = 40_000,
    seed: int = SEED,
    logp_range=(0.0, 6.5),
    steps: int = 27,
    ec50_floor_nM: float | None = None,
):
    """Free-drug retinal margin as a function of lipophilicity.

    This exists to test the single most load-bearing claim in the source
    analysis: that the field "put lipophilicity where it could have put
    polarity, because no indication ever asked for free fraction", and that
    the same ligand efficiency spent at logD 2.8 instead of 5.5 would close
    the retinal gap.

    The two terms pull in opposite directions and the claim is really an
    assertion about which wins:

        raising logP   improves potency     by ~1.0 log per unit (pEC50 = LLE + logP)
        raising logP   worsens free fraction by ~0.45-0.70 log per unit

    So the sweep reports where the product actually peaks.  Molecular weight is
    held fixed so the barrier model's size term does not confound the
    lipophilicity term - this is a logP scan, not a scan over real molecules.
    """
    rng = np.random.default_rng(seed)
    pka = (3.0, 3.5) if anionic else None
    out = []
    for logp in np.linspace(*logp_range, steps):
        pka_draw = rng.uniform(*pka, n) if pka else None
        logd = (
            logp - np.log10(1.0 + 10.0 ** (7.4 - pka_draw))
            if pka_draw is not None
            else np.full(n, logp)
        )
        fu = free_fraction(logd, rng, anionic=anionic)

        lle = rng.uniform(*LLE_ANION, n)
        pkbhx = rng.uniform(*head_pkbhx, n)
        deficit = np.clip(PKBHX_CARBOXYLATE_MID - pkbhx, 0.0, None)
        penalty = rng.uniform(*LLE_PENALTY_AT_OEA, n) * (
            deficit / (PKBHX_CARBOXYLATE_MID - PKBHX_OEA_MID)
        )
        ec50 = 10.0 ** (9.0 - (lle - penalty + logp))
        if ec50_floor_nM is not None:
            # Constant LLE implies potency improves 1:1 with logP for ever,
            # which is the assumption LLE exists to question.  Flooring EC50
            # at the best value ever measured in the class (pemafibrate, 1 nM)
            # is the empirical cap, and it is how this sweep is stress-tested.
            ec50 = np.maximum(ec50, ec50_floor_nM)

        probe = Scaffold(
            key="probe",
            name="probe",
            smiles="CC(=O)O",
            head="oxazolidinone",
            head_label="probe",
            pka=pka,
            pka_basis="sweep",
            pkbhx_distal=head_pkbhx,
            ec50_basis="sweep",
            dose_mg=100.0,
            clearance_l_h=(5.0, 20.0),
            selectivity_strategy="",
            breaks_first="",
            rationale="",
        )
        cl = rng.uniform(5.0, 20.0, n)
        c_avg = 100.0 / (cl * 24.0) * 1000.0
        c_lo, c_med, c_hi = _q(c_avg)
        cmp = as_compound(
            probe,
            {"mw": 350.0, "clogp": logp},
            float(np.median(fu)),
            (c_lo, c_med, c_hi),
        )
        res = oc_model.run(cmp, potency_from_draws(probe, ec50), n=n, seed=seed)
        out.append(
            (
                float(logp),
                float(np.median(logd)),
                float(np.median(fu)),
                float(np.median(ec50)),
                float(np.median(res.margins["endothelium"])),
            )
        )
    return out
