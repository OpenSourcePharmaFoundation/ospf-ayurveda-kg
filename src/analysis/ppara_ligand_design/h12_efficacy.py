"""How much maximal efficacy a neutral head costs, and whether it matters.

Step 7 of ``docs/prompts/dr-solve-open-questions-prompt.md``.

The structural argument is settled and this module does not re-litigate it:
Tyr464 sits on helix 12, H12 is mobile, and the Tyr464 contact is what pays for
AF-2 closure.  Weaken the head and that contact is the first to stop being
worth paying for, so a neutral head gives a partial agonist by construction.

The question the source analysis left open is the one that decides the
programme: **how much** efficacy is lost.  "Partial agonist" spans everything
from 85% of a fibrate maximum, which is a drug, to 8%, which is a tool
compound.  This module puts a number and an interval on it, and then does the
thing that actually matters - multiplies it by the exposure gain the neutral
head buys, because the programme only makes sense if the product goes up.

The model
---------
Two states, as the crystallography supports: H12 docked (active) and H12
sampling open.  Coactivator binds only the docked state, so it pulls the
equilibrium towards it - which is why the same ligand reads as a stronger
partial agonist in a coactivator-rich cell than in a poor one.

    L       = [closed]/[open] for ligand-bound receptor, no coactivator
    f_act   = L(1 + A/Kd) / (1 + L(1 + A/Kd))
    E_max   = f_act(ligand) / f_act(full agonist)

The ligand enters through L only:

    L(ligand) = L(full) * exp(-ddG_H12 / RT)

``ddG_H12`` is the stabilisation the ligand fails to deliver to the H12
contact, relative to a carboxylate.  It is built from two measured things:

* **Geometry.**  If the head cannot present a competent acceptor pair at the
  measured 2.22 A span (``headgroups``), it cannot place an atom to serve
  His440 and Tyr464 at all, and the whole H12 contact is lost rather than
  weakened.  This is the OEA case and it is why OEA is a partial agonist.
* **Basicity.**  If it can, the contact is made but weaker, and the loss is
  the pK_BHX deficit against a carboxylate times the per-unit energy.

Why the transcriptional step is modelled separately
----------------------------------------------------
Receptor activation is not transcription.  A PPRE-driven programme can carry
spare-receptor amplification, so a receptor at 30% activation does not
necessarily give 30% of the gene response.  The direction of that non-linearity
is not knowable from here, so it is carried as a Hill exponent spanning both
possibilities (amplifying and attenuating) rather than assumed to be 1.  It is
one of the larger uncertainties in the answer and the note says so.
"""

from __future__ import annotations

import csv
import dataclasses
import pathlib

import numpy as np

_REPO = pathlib.Path(__file__).resolve().parents[3]
OUT = _REPO / "data" / "processed" / "ppara_h12_efficacy.tsv"

R_KCAL = 1.98720425e-3  # kcal / (mol K)
T_K = 310.15  # 37 C
RT = R_KCAL * T_K  # 0.6164 kcal/mol

N_DRAWS = 200_000
SEED = 20261109

# --- parameter ranges, each with its basis -------------------------------
#
# Every one of these is a range, not a point, and the sensitivity block at the
# end of this module reports which of them the answer is actually sensitive to.

# Energy per unit of Laurence hydrogen-bond basicity, in a desolvated pocket.
# The source run's SAR analysis uses 1.2-1.4 kcal/mol per pK_BHX unit; that is
# the figure adopted here and it is knowledge-based, not measured in this
# project.
DDG_PER_PKBHX = (1.2, 1.4)

# pK_BHX of a carboxylate oxygen - the acceptor the design has to replace.
PKBHX_CARBOXYLATE = (4.3, 4.8)

# Free energy of H12 closure for a carboxylate full agonist, no coactivator.
# Not directly measured for PPARalpha.  Bounded instead by two observations:
# a full agonist must end up essentially fully active in a coactivator-rich
# reporter assay (so it cannot be small), and the apo receptor must retain
# meaningful basal H12 opening (so it cannot be very large).
DG_CLOSE_FULL = (-3.5, -1.8)

# What the Tyr464 contact itself is worth.  This is the ceiling on what any
# head-group change can cost at H12: a contact cannot be weakened by more than
# its own value.  Without this cap the model happily charges a weak acceptor
# more than the whole contact is worth, which produced the nonsense result
# that losing the contact entirely scored *better* than weakening it.
# Range is that of a single charge-assisted hydrogen bond to a mobile helix.
DG_H12_CONTACT = (1.5, 4.0)

# Coactivator availability as A/Kd.  This is the tissue term, and it turns out
# to be the one that decides the answer.  A reporter line overexpressing SRC-1
# sits at the top of the assay range; a cell relying on endogenous PGC-1alpha
# sits an order of magnitude below it.
COA_ASSAY = (1.0, 30.0)
COA_TISSUE = (0.03, 1.0)

# Transcriptional transfer: output ~ f_act^h.  h < 1 amplifies (spare
# receptors), h > 1 attenuates (cooperative PPRE occupancy).  Spanning both.
HILL = (0.6, 1.6)

# The fraction of the H12 contact that survives when the head is geometrically
# competent but weaker.  A head that makes the pair still has to orient it;
# this allows for the contact being partly lost to geometry even when the span
# is right.
GEOMETRIC_EFFICIENCY = (0.6, 1.0)


@dataclasses.dataclass(frozen=True)
class Head:
    key: str
    name: str
    pkbhx_distal: tuple[float, float]  # basicity of the atom serving H11/H12
    reaches_h12: bool  # from the measured span screen in headgroups.py
    note: str


# ``reaches_h12`` is taken from ``headgroups.py``: a head whose best competent
# acceptor pair falls inside the measured span window can place an atom at the
# distal position; one that cannot, cannot.
HEADS = (
    Head(
        "carboxylate",
        "Carboxylate (reference full agonist)",
        PKBHX_CARBOXYLATE,
        True,
        "the incumbent",
    ),
    Head(
        "oxazolidinone",
        "Oxazolidin-2-one",
        (2.3, 2.6),
        True,
        "neutral, geometrically competent, carbonyl distal acceptor",
    ),
    Head(
        "sulfone",
        "Sulfone",
        (1.3, 1.6),
        True,
        "neutral, geometrically competent, weak S=O acceptors",
    ),
    Head(
        "sulfonamide",
        "Sulfonamide",
        (1.3, 1.6),
        True,
        "neutral, geometrically competent, weak S=O acceptors",
    ),
    Head(
        "phosphonamidate",
        "Phosphonamidate",
        (3.0, 3.5),
        True,
        "strongest neutral acceptor pair; span is marginal (2.58 A)",
    ),
    Head(
        "hydroxamic_acid",
        "Hydroxamic acid",
        (2.2, 2.8),
        False,
        "span 2.64 A - outside the window, contact treated as lost",
    ),
    Head(
        "nae_head",
        "N-acylethanolamine (OEA)",
        (1.3, 1.8),
        False,
        "span 2.67 A - the empirical anchor for a lost H12 contact",
    ),
    Head(
        "oxadiazolone",
        "1,2,4-Oxadiazol-5(4H)-one",
        (2.4, 3.0),
        False,
        "one competent acceptor only; cannot serve His440 and Tyr464",
    ),
    Head(
        "tetrazole",
        "Tetrazole",
        (2.0, 2.6),
        False,
        "no acceptor atom can take two H-bonds",
    ),
)


def _u(rng, lo_hi, n):
    lo, hi = lo_hi
    return rng.uniform(lo, hi, n)


@dataclasses.dataclass
class Efficacy:
    head: Head
    ddg_h12: np.ndarray  # kcal/mol lost at the H12 contact
    emax_assay: np.ndarray  # relative to a carboxylate full agonist
    emax_tissue: np.ndarray
    output_assay: np.ndarray  # after the transcriptional transfer
    output_tissue: np.ndarray


def _f_active(dg_close: np.ndarray, coa: np.ndarray) -> np.ndarray:
    L = np.exp(-dg_close / RT)
    Lc = L * (1.0 + coa)
    return Lc / (1.0 + Lc)


def run(n: int = N_DRAWS, seed: int = SEED) -> list[Efficacy]:
    rng = np.random.default_rng(seed)

    # Shared draws: these are properties of the receptor and the assay, not of
    # the head group, so every head must see the same ones or the comparison
    # between heads carries noise that is not real.
    per_pkbhx = _u(rng, DDG_PER_PKBHX, n)
    pkbhx_coo = _u(rng, PKBHX_CARBOXYLATE, n)
    dg_full = _u(rng, DG_CLOSE_FULL, n)
    coa_assay = _u(rng, COA_ASSAY, n)
    coa_tissue = _u(rng, COA_TISSUE, n)
    hill = _u(rng, HILL, n)
    geom = _u(rng, GEOMETRIC_EFFICIENCY, n)
    dg_h12 = _u(rng, DG_H12_CONTACT, n)

    # The full-agonist reference, against which every Emax is normalised.
    ref_assay = _f_active(dg_full, coa_assay)
    ref_tissue = _f_active(dg_full, coa_tissue)

    out = []
    for h in HEADS:
        pkbhx = _u(rng, h.pkbhx_distal, n)
        if h.reaches_h12:
            # Contact made but weaker: the basicity deficit converted to
            # energy, discounted by how well the pair can actually be
            # oriented, and capped at what the contact is worth.  The cap is
            # what makes a very weak acceptor converge on the lost-contact
            # case rather than overshooting past it.
            deficit = np.clip(pkbhx_coo - pkbhx, 0.0, None) * per_pkbhx
            ddg = np.minimum(deficit / geom, dg_h12)
        else:
            # Contact not made at all: the ligand forfeits all of it.
            ddg = dg_h12.copy()

        dg_lig = dg_full + ddg
        f_assay = _f_active(dg_lig, coa_assay)
        f_tissue = _f_active(dg_lig, coa_tissue)
        emax_assay = f_assay / ref_assay
        emax_tissue = f_tissue / ref_tissue
        out.append(
            Efficacy(
                head=h,
                ddg_h12=ddg,
                emax_assay=emax_assay,
                emax_tissue=emax_tissue,
                output_assay=emax_assay**hill,
                output_tissue=emax_tissue**hill,
            )
        )
    return out


def q(x: np.ndarray, qs=(2.5, 50, 97.5)) -> tuple[float, ...]:
    return tuple(float(v) for v in np.percentile(x, qs))


def sensitivity(n: int = 50_000, seed: int = SEED) -> list[tuple[str, float]]:
    """Which unmeasured input drives the Emax answer, for a neutral head.

    This is a rank-correlation screen, not a Sobol decomposition: it reports
    monotone influence on log Emax and will understate a purely interactive
    term.  It is enough for the only question being asked of it - whether the
    spread in the Emax prediction is a property of the chemistry or of the
    receptor parameters nobody has measured.
    """
    from scipy import stats

    rng = np.random.default_rng(seed)
    draws = {
        "per_pkbhx (energy per pK_BHX unit)": _u(rng, DDG_PER_PKBHX, n),
        "pkbhx_carboxylate (reference basicity)": _u(rng, PKBHX_CARBOXYLATE, n),
        "dg_close_full (closure energy, full agonist)": _u(rng, DG_CLOSE_FULL, n),
        "dg_h12_contact (worth of the Tyr464 contact)": _u(rng, DG_H12_CONTACT, n),
        "coactivator A/Kd (tissue)": _u(rng, COA_TISSUE, n),
        "geometric_efficiency": _u(rng, GEOMETRIC_EFFICIENCY, n),
    }
    # Evaluate for the oxazolidinone head: neutral, competent, the lead case.
    pkbhx = _u(rng, (2.3, 2.6), n)
    deficit = (
        np.clip(draws["pkbhx_carboxylate (reference basicity)"] - pkbhx, 0.0, None)
        * draws["per_pkbhx (energy per pK_BHX unit)"]
    )
    ddg = np.minimum(
        deficit / draws["geometric_efficiency"],
        draws["dg_h12_contact (worth of the Tyr464 contact)"],
    )
    dgf = draws["dg_close_full (closure energy, full agonist)"]
    coa = draws["coactivator A/Kd (tissue)"]
    emax = _f_active(dgf + ddg, coa) / _f_active(dgf, coa)

    out = [
        (name, float(abs(stats.spearmanr(v, np.log(emax + 1e-12)).statistic)))
        for name, v in draws.items()
    ]
    return sorted(out, key=lambda t: -t[1])


def write(rows: list[Efficacy]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(
            [
                "key",
                "name",
                "reaches_h12",
                "ddg_h12_kcal_med",
                "ddg_h12_kcal_lo",
                "ddg_h12_kcal_hi",
                "emax_assay_med",
                "emax_assay_lo",
                "emax_assay_hi",
                "emax_tissue_med",
                "emax_tissue_lo",
                "emax_tissue_hi",
                "txn_output_tissue_med",
                "txn_output_tissue_lo",
                "txn_output_tissue_hi",
                "note",
            ]
        )
        for r in rows:
            dl, dm, dh = q(r.ddg_h12)
            al, am, ah = q(r.emax_assay)
            tl, tm, th = q(r.emax_tissue)
            ol, om, oh = q(r.output_tissue)
            w.writerow(
                [
                    r.head.key,
                    r.head.name,
                    int(r.head.reaches_h12),
                    f"{dm:.2f}",
                    f"{dl:.2f}",
                    f"{dh:.2f}",
                    f"{am:.3f}",
                    f"{al:.3f}",
                    f"{ah:.3f}",
                    f"{tm:.3f}",
                    f"{tl:.3f}",
                    f"{th:.3f}",
                    f"{om:.3f}",
                    f"{ol:.3f}",
                    f"{oh:.3f}",
                    r.head.note,
                ]
            )


def main() -> None:
    rows = run()
    write(rows)
    print(f"{'head':34s} {'ddG_H12':>16s} {'Emax assay':>18s} " f"{'Emax tissue':>18s}")
    for r in rows:
        dl, dm, dh = q(r.ddg_h12)
        al, am, ah = q(r.emax_assay)
        tl, tm, th = q(r.emax_tissue)
        print(
            f"{r.head.name[:34]:34s} {dm:5.2f} [{dl:4.2f}-{dh:4.2f}] "
            f"{am:6.1%} [{al:4.1%}-{ah:5.1%}] "
            f"{tm:6.1%} [{tl:4.1%}-{th:5.1%}]"
        )
    print("\nSensitivity of Emax (oxazolidinone head, tissue coactivator),")
    print("|Spearman rho| against log Emax:")
    for name, rho in sensitivity():
        print(f"   {rho:5.2f}  {name}")

    print(f"\nwrote {OUT.relative_to(_REPO)}")


if __name__ == "__main__":
    main()
