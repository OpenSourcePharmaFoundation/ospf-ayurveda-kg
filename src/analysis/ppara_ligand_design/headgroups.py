"""Screen candidate head groups against the measured cage geometry.

Step 7 of ``docs/prompts/dr-solve-open-questions-prompt.md``.

``af2_cage`` measures what the receptor actually asks for.  This module asks,
for each candidate head group, whether it can supply it.  The screen is
deliberately geometric first and electronic second, because that is the order
the measurement imposes: a head that cannot reproduce the array is not rescued
by having the right pKa.

The three filters, in the order they are applied
-------------------------------------------------
1. **Acceptor-pair span.**  Across five independent PPARalpha agonist
   complexes the two engaged ligand acceptor atoms sit 2.22 +/- 0.06 A apart
   (range 2.13-2.29).  That is a geminal pair - two acceptors on one carbon or
   one phosphorus - not a 1,2- or 1,3-array.  The source analysis quoted
   "2.2-3.2 A"; the upper half of that range is empty, and several head groups
   that the wider range admits are excluded by the narrower one.

2. **Lone-pair capacity.**  The measured contact map is not four donors onto
   four acceptor atoms.  It is four donors onto *two* atoms: the proximal
   acceptor takes Ser280 and Tyr314 (donors 4.25 A apart), the distal acceptor
   takes His440 and Tyr464 (3.61 A apart).  Each engaged atom therefore has to
   accept **two** hydrogen bonds at once.  An oxygen - sp2 or sp3 - has two
   available lone pairs and can.  A pyridine-type or azole ring nitrogen has
   one lone pair in the ring plane and cannot, at any pKa or footprint.  This
   filter is why the tetrazole fails on physics rather than on convention.

3. **Footprint.**  Volume of the head fragment relative to acetate, computed
   on the same capping group for every entry so the ratio means something.

What is computed here and what is asserted
-------------------------------------------
Computed: acceptor atom identity, lone-pair capacity, every achievable
acceptor-acceptor span over an ETKDG conformer ensemble, fragment volume,
TPSA, and the resulting geometric verdict.

Asserted, with the source named in the table: pKa, and the Laurence pK_BHX
hydrogen-bond basicity used to put a number on acceptor strength.  Neither is
calculable to useful accuracy from a SMILES string, and pretending otherwise
is the failure mode this chain exists to correct.  Both are carried as ranges.
"""

from __future__ import annotations

import csv
import dataclasses
import itertools
import math
import pathlib

import numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem, Descriptors

RDLogger.DisableLog("rdApp.*")

_REPO = pathlib.Path(__file__).resolve().parents[3]
OUT = _REPO / "data" / "processed" / "ppara_headgroup_screen.tsv"

# Measured from data/processed/ppara_af2_cage_geometry.tsv (PPARalpha agonists,
# n = 5).  Kept as module constants so the screen and the note cannot drift
# apart from the measurement.
ALPHA_SPAN_MEAN = 2.222
ALPHA_SPAN_SD = 0.064
# +/- 3 sd, widened to 0.35 A to allow for the ~0.2 A coordinate error at these
# resolutions and for the induced fit a new chemotype would get.  A head whose
# best competent pair falls outside this cannot make the 2:2 contact pattern
# without moving a helix.
SPAN_WINDOW = (ALPHA_SPAN_MEAN - 0.35, ALPHA_SPAN_MEAN + 0.35)

# Measured from the same file: rosiglitazone's engaged acceptor atoms in PPARG
# span 4.46 A.  A head that lands here is a gamma head, not an alpha head.
GAMMA_SPAN = 4.46

N_CONFS = 300
SEED = 20261109


@dataclasses.dataclass(frozen=True)
class HeadGroup:
    key: str
    name: str
    smiles: str  # capped with a methyl standing in for the linker
    charge_state: str  # "neutral" | "anion"
    pka: tuple[float, float] | None  # acidic pKa range, None if not ionisable
    pka_source: str
    pkbhx: tuple[float, float]  # Laurence H-bond basicity of the best acceptor
    note: str


# pKa values are knowledge-based, from the measured values of the unsubstituted
# parent heterocycle or acid, and carry a range wide enough to cover the
# substituent effects of a real ligand body.  pK_BHX values are from the
# Laurence hydrogen-bond basicity scale as tabulated in the source run's SAR
# analysis (agents/p2-sar.md section 1.2), which is where this project's
# numbers for them come from.
HEADS = (
    HeadGroup(
        "carboxylate",
        "Carboxylate (baseline)",
        "CC(=O)[O-]",
        "anion",
        (3.0, 3.5),
        "2-aryloxy-2-methylpropanoic acid, measured",
        (4.3, 4.8),
        "the incumbent; every PPARalpha drug uses it",
    ),
    HeadGroup(
        "carboxylic_acid",
        "Carboxylic acid (neutral form)",
        "CC(=O)O",
        "neutral",
        (3.0, 3.5),
        "as above",
        (1.5, 2.0),
        "the 0.005% of fenofibric acid that is permeant at pH 7.4",
    ),
    HeadGroup(
        "tetrazole",
        "Tetrazol-5-yl (anion)",
        "Cc1nnn[n-]1",
        "anion",
        (4.5, 4.9),
        "5-methyltetrazole, measured",
        (2.0, 2.6),
        "the reflexive carboxylate bioisostere",
    ),
    HeadGroup(
        "tetrazole_neutral",
        "Tetrazol-5-yl (neutral)",
        "Cc1nnn[nH]1",
        "neutral",
        (4.5, 4.9),
        "as above",
        (1.8, 2.2),
        "neutral tautomer, 0.1-0.3% of the population at pH 7.4",
    ),
    HeadGroup(
        "acylsulfonamide",
        "Acylsulfonamide (anion)",
        "CC(=O)[N-]S(C)(=O)=O",
        "anion",
        (3.5, 4.5),
        "N-acyl methanesulfonamide, measured",
        (1.3, 2.6),
        "extended bidentate, widely used to hold acidity",
    ),
    HeadGroup(
        "oxadiazolone",
        "1,2,4-Oxadiazol-5(4H)-one (anion)",
        "Cc1noc(=O)[n-]1",
        "anion",
        (6.0, 7.0),
        "3-substituted 1,2,4-oxadiazol-5(4H)-one, measured",
        (2.4, 3.0),
        "the source analysis's lead acidic head",
    ),
    HeadGroup(
        "oxadiazolone_neutral",
        "1,2,4-Oxadiazol-5(4H)-one (neutral)",
        "Cc1noc(=O)[nH]1",
        "neutral",
        (6.0, 7.0),
        "as above",
        (2.2, 2.6),
        "3-20% neutral at pH 7.4 - the permeant reservoir",
    ),
    HeadGroup(
        "hydroxyisoxazole",
        "Isoxazol-3-ol (anion)",
        "Cc1cc([O-])no1",
        "anion",
        (5.0, 6.0),
        "isoxazol-3-ol, measured",
        (2.8, 3.4),
        "compact, partially ionised",
    ),
    HeadGroup(
        "hydroxyisoxazole_neutral",
        "Isoxazol-3-ol (neutral)",
        "Cc1cc(O)no1",
        "neutral",
        (5.0, 6.0),
        "as above",
        (1.3, 1.8),
        "neutral tautomer",
    ),
    HeadGroup(
        "phosphine_oxide",
        "Dimethylphosphine oxide",
        "CP(C)(C)=O",
        "neutral",
        None,
        "not ionisable",
        (3.0, 3.5),
        "strongest neutral acceptor available; single oxygen",
    ),
    HeadGroup(
        "phosphonamide",
        "Methylphosphonamide",
        "CP(C)(N)=O",
        "neutral",
        None,
        "not ionisable at physiological pH",
        (3.0, 3.5),
        "P=O plus an N-H donor on the same centre",
    ),
    HeadGroup(
        "phosphinic_acid",
        "Phosphinic acid (anion)",
        "CP(C)([O-])=O",
        "anion",
        (2.0, 3.0),
        "dimethylphosphinic acid, measured",
        (4.0, 4.6),
        "geminal P-O pair, permanently charged",
    ),
    HeadGroup(
        "phosphonamidate",
        "Methyl methylphosphonamidate",
        "COP(C)(N)=O",
        "neutral",
        None,
        "not ionisable",
        (3.0, 3.5),
        "geminal P=O / P-O pair - the phosphorus head that is a pair "
        "rather than a single acceptor",
    ),
    HeadGroup(
        "sulfone",
        "Dimethyl sulfone",
        "CS(C)(=O)=O",
        "neutral",
        None,
        "not ionisable",
        (1.3, 1.6),
        "geminal S-O pair, permanently neutral, weak acceptors",
    ),
    HeadGroup(
        "sulfoximine",
        "Sulfoximine",
        "CS(C)(=N)=O",
        "neutral",
        None,
        "not ionisable at physiological pH",
        (1.6, 2.4),
        "S=O plus a stronger S=N acceptor on the same centre",
    ),
    HeadGroup(
        "oxazolidinone_plain",
        "Oxazolidin-2-one",
        "CC1COC(=O)N1",
        "neutral",
        None,
        "not ionisable",
        (2.3, 2.6),
        "the source analysis's neutral head option B1, undecorated",
    ),
    HeadGroup(
        "oxazolidinone",
        "4,4-Dimethyloxazolidin-2-one",
        "CC1(C)COC(=O)N1",
        "neutral",
        None,
        "not ionisable",
        (2.3, 2.6),
        "option B1 with the gem-dimethyl hydrolysis block installed - "
        "carried separately to price the block",
    ),
    HeadGroup(
        "cyclopropane_dicarboxamide",
        "Cyclopropane-1,1-dicarboxamide",
        "NC(=O)C1(C(N)=O)CC1",
        "neutral",
        None,
        "not ionisable",
        (2.3, 2.6),
        "the source analysis's neutral head option B2",
    ),
    HeadGroup(
        "malonamide",
        "Malonamide",
        "NC(=O)CC(N)=O",
        "neutral",
        None,
        "not ionisable",
        (2.3, 2.6),
        "flexible gem-dicarbonyl analogue",
    ),
    HeadGroup(
        "nae_head",
        "N-acylethanolamine head (OEA)",
        "CC(=O)NCCO",
        "neutral",
        None,
        "not ionisable",
        (1.3, 2.6),
        "the existence proof: neutral, binds, LE 0.41",
    ),
    HeadGroup(
        "thiazolidinedione",
        "Thiazolidine-2,4-dione (anion)",
        "CC1SC(=O)[N-]C1=O",
        "anion",
        (6.3, 6.8),
        "thiazolidine-2,4-dione, measured",
        (2.3, 2.8),
        "the gamma head; measured here against alpha's geometry",
    ),
    HeadGroup(
        "squaramide",
        "Squaramide",
        "NC1=C(N)C(=O)C1=O",
        "neutral",
        (8.0, 10.0),
        "squaramide N-H, measured",
        (2.0, 2.5),
        "fashionable replacement; presents donors not acceptors",
    ),
    HeadGroup(
        "hydroxamic_acid",
        "Hydroxamic acid",
        "CC(=O)NO",
        "neutral",
        (8.5, 9.5),
        "acetohydroxamic acid, measured",
        (2.2, 2.8),
        "chelating O,O pair, essentially fully neutral at 7.4",
    ),
    HeadGroup(
        "acyl_cyanamide",
        "Acylcyanamide (anion)",
        "CC(=O)[N-]C#N",
        "anion",
        (3.0, 4.0),
        "N-acylcyanamide, measured",
        (1.5, 2.0),
        "compact acidic alternative",
    ),
    HeadGroup(
        "sulfonamide",
        "Methanesulfonamide",
        "CS(N)(=O)=O",
        "neutral",
        (10.0, 11.0),
        "methanesulfonamide, measured",
        (1.3, 1.6),
        "geminal S-O pair, neutral at 7.4",
    ),
)


# --- acceptor model --------------------------------------------------------
#
# RDKit's shipped BaseFeatures definition marks only one oxygen of a
# carboxylate as an acceptor, which would silently destroy the baseline this
# whole screen is referenced to.  So the definition is written out here.
#
# ``capacity`` is the number of hydrogen bonds the atom can accept at once:
# any oxygen has two usable lone pairs, an sp2 or sp3 nitrogen has one.  That
# single number is what the measured 2:2 contact pattern turns into a filter.
# Patterns are written in atomic-number form (``[#8]`` not ``[O]``) on purpose:
# an uppercase ``O`` in SMARTS matches *aliphatic* oxygen only, so the obvious
# spelling silently skips every aromatic ring oxygen - which is exactly the
# atom the oxadiazolone and the hydroxyisoxazole depend on.
#
# Capacity is the number of hydrogen bonds the atom can accept simultaneously:
#   * an oxo/oxide oxygen (C=O, P=O, S=O, carboxylate O-) carries two in-plane
#     lone pairs and takes two;
#   * an aliphatic ether or hydroxyl oxygen likewise has two;
#   * an *aromatic* ring oxygen (furan-, oxazole-, oxadiazole-type) has put one
#     lone pair into the ring pi system and has one left, so it takes one -
#     and it is a weak acceptor for the same reason;
#   * a pyridine- or azole-type ring nitrogen has a single in-plane lone pair
#     and takes one;
#   * a pyrrole-type N-H has donated its lone pair to the ring and takes none.
ACCEPTOR_PATTERNS = (
    # (SMARTS, capacity, label)
    ("[#8X1]", 2, "oxo/oxide O"),  # C=O, P=O, S=O, N-oxide, carboxylate O-
    ("[#8X2H1;!a]", 2, "hydroxyl O"),
    ("[#8X2H0;a]", 1, "aromatic ring O (one lone pair in the ring pi)"),
    ("[#8X2H0;!a]", 2, "ether/ester O"),
    ("[nX3H1]", 0, "pyrrole-type N-H (lone pair in the ring pi)"),
    ("[nX3H0]", 0, "substituted pyrrole-type N (lone pair in the ring pi)"),
    ("[nX2]", 1, "aromatic ring N"),
    ("[NX1]#*", 1, "nitrile N"),
    ("[NX2]=*", 1, "imine N"),
    ("[NX3;H0;!$(N[C,S,P]=[O,S]);!$(Na)]", 1, "tertiary amine N"),
    ("[N-;$([N-][C,S,P]=[O,S])]", 1, "acylamide/sulfonamide anion N"),
)


@dataclasses.dataclass(frozen=True)
class Acceptor:
    idx: int
    symbol: str
    capacity: int
    label: str


def acceptors(mol: Chem.Mol) -> list[Acceptor]:
    """Acceptor atoms with their lone-pair capacity.

    Patterns are applied in order and the first match wins, so the specific
    pyrrole-type nitrogen rule (capacity 0) has to precede the general
    aromatic one.  Capacity 0 entries are kept rather than dropped: a head
    group that presents only capacity-0 atoms is a distinct and reportable
    kind of failure, not an absence of data.
    """
    assigned: dict[int, Acceptor] = {}
    for smarts, capacity, label in ACCEPTOR_PATTERNS:
        patt = Chem.MolFromSmarts(smarts)
        if patt is None:
            raise ValueError(f"bad SMARTS: {smarts}")
        for match in mol.GetSubstructMatches(patt):
            i = match[0]
            if i in assigned:
                continue
            a = mol.GetAtomWithIdx(i)
            if a.GetSymbol() not in ("O", "N"):
                continue
            assigned[i] = Acceptor(i, a.GetSymbol(), capacity, label)
    return [assigned[i] for i in sorted(assigned)]


def _confs(mol: Chem.Mol) -> Chem.Mol:
    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = SEED
    params.pruneRmsThresh = 0.25
    AllChem.EmbedMultipleConfs(mol, numConfs=N_CONFS, params=params)
    if mol.GetNumConformers() == 0:
        params.useRandomCoords = True
        AllChem.EmbedMultipleConfs(mol, numConfs=N_CONFS, params=params)
    AllChem.MMFFOptimizeMoleculeConfs(mol, maxIters=2000)
    return mol


def _spans(
    mol: Chem.Mol, accs: list[Acceptor]
) -> dict[tuple[int, int], tuple[float, float]]:
    """Min and max achievable distance for each acceptor pair over the ensemble."""
    out: dict[tuple[int, int], tuple[float, float]] = {}
    for a, b in itertools.combinations(accs, 2):
        ds = []
        for conf in mol.GetConformers():
            p = conf.GetAtomPosition(a.idx)
            q = conf.GetAtomPosition(b.idx)
            ds.append(math.dist((p.x, p.y, p.z), (q.x, q.y, q.z)))
        if ds:
            out[(a.idx, b.idx)] = (min(ds), max(ds))
    return out


@dataclasses.dataclass
class Screen:
    head: HeadGroup
    n_acceptors: int
    n_competent: int  # acceptors with capacity >= 2
    acceptor_labels: str
    best_span: float | None  # closest achievable span, competent pairs only
    best_span_pair: str
    best_span_any: float | None  # ignoring capacity
    fits_alpha: bool
    volume: float
    volume_ratio: float
    tpsa: float
    neutral_fraction: float | None
    verdict: str
    reason: str


def _neutral_fraction(pka: tuple[float, float] | None) -> float | None:
    """Fraction of a monoprotic acid that is neutral at pH 7.4."""
    if pka is None:
        return 1.0
    mid = 0.5 * (pka[0] + pka[1])
    return 1.0 / (1.0 + 10 ** (7.4 - mid))


def measure_one(head: HeadGroup) -> Screen:
    """Geometry and size only.  Thresholds are applied later, in ``run``,
    because one of them is calibrated against another row of this same table."""
    mol = Chem.MolFromSmiles(head.smiles)
    if mol is None:
        raise ValueError(f"bad SMILES for {head.key}: {head.smiles}")
    accs = acceptors(mol)
    molh = _confs(mol)
    spans = _spans(molh, accs)

    competent = [a for a in accs if a.capacity >= 2]
    comp_idx = {a.idx for a in competent}

    def closest(pairs) -> tuple[float | None, str]:
        best, best_key = None, ""
        for (i, j), (lo, hi) in pairs:
            # Any distance in [lo, hi] is reachable; the achievable value
            # closest to the target is what the head can actually present.
            d = min(max(ALPHA_SPAN_MEAN, lo), hi)
            if best is None or abs(d - ALPHA_SPAN_MEAN) < abs(best - ALPHA_SPAN_MEAN):
                best, best_key = (
                    d,
                    f"{molh.GetAtomWithIdx(i).GetSymbol()}{i}-"
                    f"{molh.GetAtomWithIdx(j).GetSymbol()}{j}",
                )
        return best, best_key

    best_span, best_pair = closest(
        [(k, v) for k, v in spans.items() if k[0] in comp_idx and k[1] in comp_idx]
    )
    best_any, _ = closest(list(spans.items()))

    fits = best_span is not None and SPAN_WINDOW[0] <= best_span <= SPAN_WINDOW[1]
    return Screen(
        head=head,
        n_acceptors=len(accs),
        n_competent=len(competent),
        acceptor_labels="; ".join(f"{a.symbol}{a.idx}({a.capacity})" for a in accs),
        best_span=best_span,
        best_span_pair=best_pair,
        best_span_any=best_any,
        fits_alpha=fits,
        volume=AllChem.ComputeMolVolume(molh),
        volume_ratio=float("nan"),  # filled in by run(), relative to acetate
        tpsa=Descriptors.TPSA(mol),
        neutral_fraction=_neutral_fraction(head.pka),
        verdict="",
        reason="",
    )


def _verdict(row: Screen, tzd_ratio: float) -> tuple[str, str]:
    """Apply the thresholds, in the order the measurement imposes.

    The two hard filters are physical: lone-pair capacity, then the measured
    geminal span.  Footprint comes last and is *calibrated rather than
    asserted* - the threshold is the volume of the thiazolidinedione, the one
    head group with an unambiguous empirical verdict at PPARalpha (every TZD
    drug is gamma-preferring).  A head smaller than the known-incompetent head
    cannot honestly be excluded on size.

    That ordering is what reverses the source analysis on two specific heads.
    It excluded both the TZD and the tetrazole on footprint; here the TZD fails
    on span and the tetrazole on lone-pair capacity, and neither fails on size.
    """
    pkbhx = 0.5 * (row.head.pkbhx[0] + row.head.pkbhx[1])
    if row.n_competent < 2:
        return "FAIL-capacity", (
            f"{row.n_competent} of {row.n_acceptors} acceptor atoms can take "
            "two H-bonds; the measured 2:2 contact pattern needs two that can"
        )
    if not row.fits_alpha:
        side = "too wide" if row.best_span > SPAN_WINDOW[1] else "too close"
        return "FAIL-span", (
            f"best competent pair reaches {row.best_span:.2f} A, {side} for "
            f"the measured {SPAN_WINDOW[0]:.2f}-{SPAN_WINDOW[1]:.2f} A window"
        )
    if row.volume_ratio > tzd_ratio:
        return "FAIL-footprint", (
            f"{row.volume_ratio:.2f}x the carboxylate, above the "
            f"{tzd_ratio:.2f}x of the thiazolidinedione that alpha rejects"
        )
    return "PASS", (
        f"competent pair at {row.best_span:.2f} A, {row.volume_ratio:.2f}x "
        f"footprint, best-acceptor basicity pK_BHX {pkbhx:.1f}"
    )


def run() -> list[Screen]:
    rows = [measure_one(h) for h in HEADS]
    by_key = {r.head.key: r for r in rows}
    baseline = by_key["carboxylate"].volume
    for r in rows:
        r.volume_ratio = r.volume / baseline
    tzd_ratio = by_key["thiazolidinedione"].volume_ratio
    for r in rows:
        r.verdict, r.reason = _verdict(r, tzd_ratio)
    return rows


def write(rows: list[Screen]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(
            [
                "key",
                "name",
                "smiles",
                "charge_state",
                "pka_lo",
                "pka_hi",
                "pct_neutral_pH7.4",
                "pkbhx_lo",
                "pkbhx_hi",
                "n_acceptors",
                "n_double_acceptors",
                "acceptor_atoms",
                "best_competent_span_A",
                "best_any_span_A",
                "fits_alpha_window",
                "volume_A3",
                "volume_vs_carboxylate",
                "tpsa",
                "verdict",
                "reason",
                "pka_source",
                "note",
            ]
        )
        for r in rows:
            h = r.head
            w.writerow(
                [
                    h.key,
                    h.name,
                    h.smiles,
                    h.charge_state,
                    "" if h.pka is None else h.pka[0],
                    "" if h.pka is None else h.pka[1],
                    (
                        ""
                        if r.neutral_fraction is None
                        else f"{100*r.neutral_fraction:.4g}"
                    ),
                    h.pkbhx[0],
                    h.pkbhx[1],
                    r.n_acceptors,
                    r.n_competent,
                    r.acceptor_labels,
                    "" if r.best_span is None else f"{r.best_span:.2f}",
                    "" if r.best_span_any is None else f"{r.best_span_any:.2f}",
                    int(r.fits_alpha),
                    f"{r.volume:.1f}",
                    f"{r.volume_ratio:.2f}",
                    f"{r.tpsa:.1f}",
                    r.verdict,
                    r.reason,
                    h.pka_source,
                    h.note,
                ]
            )


def main() -> None:
    rows = run()
    write(rows)
    print(
        f"{'head group':38s} {'acc':>3s} {'2LP':>3s} {'span':>5s} "
        f"{'vol':>5s} {'%neut':>7s}  verdict"
    )
    for r in rows:
        span = "  -  " if r.best_span is None else f"{r.best_span:5.2f}"
        nf = "" if r.neutral_fraction is None else f"{100*r.neutral_fraction:7.3g}"
        print(
            f"{r.head.name[:38]:38s} {r.n_acceptors:3d} {r.n_competent:3d} "
            f"{span} {r.volume_ratio:5.2f} {nf}  {r.verdict}"
        )
    print(f"\nwrote {OUT.relative_to(_REPO)}")


if __name__ == "__main__":
    main()
