"""Measure the AF-2 donor cage, instead of asserting it.

Step 7 of ``docs/prompts/dr-solve-open-questions-prompt.md``.

The source analysis makes three structural claims that the whole non-acidic
design rests on, and states all three from memory:

1. the four AF-2 contacts are all hydrogen-bond *donors*, so the ligand head
   supplies only acceptors;
2. the geometry wants a bidentate acceptor pair "roughly 2.2-3.2 A apart";
3. PPARalpha's arm I is "narrower" than PPARgamma's, so head-group footprint
   is the first filter.

Claims 1 and 2 are read straight off deposited coordinates.  Claim 3 is the one
that actually drives head-group selection and it had no number at all attached
to it, so this module computes one: a grid free-volume integral over the head
region of each isoform's arm I, with the ligand deleted.

Three things this does *not* do, stated here so the note does not overclaim
-----------------------------------------------------------------------------
* **Hydrogen positions are not in these structures.**  X-ray at this resolution
  does not see hydrogens, so "donor" is an assignment from chemistry (Ser/Thr
  hydroxyl, Tyr phenol, His imidazole N-H), not an observation.  What *is*
  observed is the heavy-atom distance and the absence of any competing acceptor
  geometry, and for His it is ambiguous by construction - a histidine can
  tautomerise.  The all-donor claim is therefore supported, not proved, and the
  one residue that could break it is His440.
* **Free volume is not binding affinity.**  The grid integral says what fits.
  It says nothing about what the pocket pays to desolvate.
* **Crystal conformations are one snapshot of an ensemble.**  Side chains move.
  The spread across independent structures is reported for exactly this reason:
  where several structures agree, the number is a receptor property; where they
  disagree, the spread is the honest uncertainty.
"""

from __future__ import annotations

import csv
import dataclasses
import itertools
import math
import pathlib
import statistics

import numpy as np

from . import structures
from .structures import CAGE, ENTRIES, Atom

_REPO = pathlib.Path(__file__).resolve().parents[3]
OUT_GEOMETRY = _REPO / "data" / "processed" / "ppara_af2_cage_geometry.tsv"
OUT_CONTACTS = _REPO / "data" / "processed" / "ppara_af2_cage_contacts.tsv"

# A heavy-atom pair closer than this, with at least one N/O, is counted as a
# hydrogen bond.  3.5 A is the conventional donor-acceptor cutoff; it is
# deliberately generous, because the question here is which contacts exist at
# all, not how good each one is.
HBOND_MAX = 3.5

# Van der Waals radii (A), Bondi.  Only the elements that occur in these
# structures are listed; anything else falls back to carbon.
VDW = {
    "C": 1.70,
    "N": 1.55,
    "O": 1.52,
    "S": 1.80,
    "F": 1.47,
    "P": 1.80,
    "CL": 1.75,
    "BR": 1.85,
    "I": 1.98,
}

# Grid for the free-volume integral.  0.4 A spacing over a 9 A box is ~1.4e4
# points per structure, which is fast and finer than the coordinate error.
GRID_SPACING = 0.4
GRID_RADIUS = 4.5

# A ligand heavy atom may be placed at a grid point if it clears every protein
# heavy atom by at least the sum of van der Waals radii less this tolerance.
# 0.4 A of tolerance is roughly the compression seen in real close contacts;
# without it the integral reports near-zero volume for every isoform and
# discriminates nothing.
VDW_TOLERANCE = 0.4


def _vdw(element: str) -> float:
    return VDW.get(element.upper(), 1.70)


def _dist(a: Atom, b: Atom) -> float:
    return math.dist(a.xyz, b.xyz)


@dataclasses.dataclass
class CageMeasurement:
    pdb_id: str
    isoform: str
    state: str
    ligand: str
    chain: str
    donor_distances: dict[str, float]  # "H3-H5" -> A
    hbonds: list[tuple[str, str, float]]  # (helix, ligand atom, distance)
    acceptor_pair_span: float | None  # A, between the two engaged ligand atoms
    n_contacts: int
    head_free_volume: float  # A^3
    centroid: tuple[float, float, float]


def _primary_chain(atoms: list[Atom], isoform: str, ligand: str) -> str | None:
    """Pick the chain whose cage is complete and which actually holds a ligand.

    Several of these entries have two or three copies in the asymmetric unit
    and the copies are not equivalent - in 2XYW only one chain's ligand is
    fully ordered.  Choosing the chain with a complete cage *and* the most
    ligand atoms avoids measuring a half-occupied site.
    """
    best, best_n = None, -1
    for chain in sorted({a.chain for a in atoms if a.group == "ATOM"}):
        cage = _cage_atoms(atoms, isoform, chain)
        if len(cage) != 4:
            continue
        n = sum(1 for a in atoms if a.resname == ligand and a.chain == chain)
        if n > best_n:
            best, best_n = chain, n
    return best


def _cage_atoms(atoms: list[Atom], isoform: str, chain: str) -> dict[str, Atom]:
    """The four donor heavy atoms, keyed by helix."""
    want = CAGE[isoform]
    found: dict[str, Atom] = {}
    for helix, (resseq, resname, atom_name) in want.items():
        for a in atoms:
            if (
                a.group == "ATOM"
                and a.chain == chain
                and a.resseq == resseq
                and a.name == atom_name
                and a.resname == resname
                and a.altloc in (".", "A", "?")
            ):
                found[helix] = a
                break
    return found


def _ligand_atoms(atoms: list[Atom], ligand: str, chain: str) -> list[Atom]:
    return [
        a
        for a in atoms
        if a.resname == ligand
        and a.chain == chain
        and a.element != "H"
        and a.altloc in (".", "A", "?")
    ]


def _head_free_volume(
    atoms: list[Atom], centroid: tuple[float, float, float], ligand: str
) -> float:
    """Volume (A^3) around the cage centroid that a ligand heavy atom could occupy.

    The ligand is deleted first - the question is how much room the *protein*
    leaves, not how much the incumbent ligand happens to use.  Waters are
    deleted too: a water in the head region is displaceable by a ligand atom
    and counting it as an obstruction would understate the pocket.

    Grid points are kept if they clear every protein heavy atom by the sum of
    van der Waals radii (probe taken as carbon) less ``VDW_TOLERANCE``.  The
    integral is over a sphere of ``GRID_RADIUS`` about the centroid, so the two
    isoforms are compared over the same region of space, referenced to their
    own cage rather than to a superposition - which is what makes the
    comparison independent of any alignment choice.
    """
    obstruction = np.array(
        [a.xyz for a in atoms if a.group == "ATOM" and a.element != "H"]
    )
    radii = np.array(
        [_vdw(a.element) for a in atoms if a.group == "ATOM" and a.element != "H"]
    )

    steps = int(2 * GRID_RADIUS / GRID_SPACING) + 1
    axis = np.linspace(-GRID_RADIUS, GRID_RADIUS, steps)
    gx, gy, gz = np.meshgrid(axis, axis, axis, indexing="ij")
    pts = np.stack([gx.ravel(), gy.ravel(), gz.ravel()], axis=1)
    pts = pts[np.linalg.norm(pts, axis=1) <= GRID_RADIUS] + np.array(centroid)

    # Block-wise so the (points x atoms) distance matrix stays small.
    min_clear = np.full(len(pts), True)
    probe = _vdw("C")
    for i in range(0, len(obstruction), 512):
        blk = obstruction[i : i + 512]
        rad = radii[i : i + 512]
        d = np.linalg.norm(pts[:, None, :] - blk[None, :, :], axis=2)
        min_clear &= np.all(d >= (rad + probe - VDW_TOLERANCE)[None, :], axis=1)

    return float(min_clear.sum() * GRID_SPACING**3)


def measure(entry) -> CageMeasurement | None:
    atoms = structures.parse(structures.fetch(entry.pdb_id))
    chain = _primary_chain(atoms, entry.isoform, entry.ligand)
    if chain is None:
        return None
    cage = _cage_atoms(atoms, entry.isoform, chain)
    lig = _ligand_atoms(atoms, entry.ligand, chain)

    donor_distances = {
        f"{a}-{b}": _dist(cage[a], cage[b])
        for a, b in itertools.combinations(["H3", "H5", "H11", "H12"], 2)
    }

    # Hydrogen bonds from each donor to any ligand N/O within the cutoff; the
    # shortest per helix is the engaged contact.
    hbonds: list[tuple[str, str, float]] = []
    engaged: dict[str, Atom] = {}
    for helix, donor in cage.items():
        cands = [
            (la, _dist(donor, la))
            for la in lig
            if la.element in ("O", "N") and _dist(donor, la) <= HBOND_MAX
        ]
        if cands:
            la, d = min(cands, key=lambda t: t[1])
            hbonds.append((helix, la.name, d))
            engaged[helix] = la

    # The bidentate span: the distance between the two *distinct* ligand atoms
    # engaging the cage that are furthest apart.  If a single atom serves every
    # donor there is no pair and the span is undefined, which is itself a
    # result worth recording.
    uniq = {(a.name, a.xyz) for a in engaged.values()}
    span = (
        max(math.dist(p, q) for (_, p), (_, q) in itertools.combinations(uniq, 2))
        if len(uniq) >= 2
        else None
    )

    centroid = tuple(
        float(statistics.fmean([a.xyz[i] for a in cage.values()])) for i in range(3)
    )
    vol = _head_free_volume(atoms, centroid, entry.ligand)

    return CageMeasurement(
        pdb_id=entry.pdb_id,
        isoform=entry.isoform,
        state=entry.state,
        ligand=entry.ligand_name,
        chain=chain,
        donor_distances=donor_distances,
        hbonds=sorted(hbonds),
        acceptor_pair_span=span,
        n_contacts=len(hbonds),
        head_free_volume=vol,
        centroid=centroid,  # type: ignore[arg-type]
    )


PAIRS = [f"{a}-{b}" for a, b in itertools.combinations(["H3", "H5", "H11", "H12"], 2)]


def run() -> list[CageMeasurement]:
    out = []
    for e in ENTRIES:
        m = measure(e)
        if m is not None:
            out.append(m)
    return out


def write(measurements: list[CageMeasurement]) -> None:
    OUT_GEOMETRY.parent.mkdir(parents=True, exist_ok=True)
    with OUT_GEOMETRY.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(
            [
                "pdb_id",
                "isoform",
                "state",
                "ligand",
                "chain",
                "n_cage_contacts",
                "acceptor_pair_span_A",
                "head_free_volume_A3",
            ]
            + [f"d_{p}_A" for p in PAIRS]
        )
        for m in measurements:
            w.writerow(
                [
                    m.pdb_id,
                    m.isoform,
                    m.state,
                    m.ligand,
                    m.chain,
                    m.n_contacts,
                    (
                        ""
                        if m.acceptor_pair_span is None
                        else f"{m.acceptor_pair_span:.2f}"
                    ),
                    f"{m.head_free_volume:.1f}",
                ]
                + [f"{m.donor_distances[p]:.2f}" for p in PAIRS]
            )

    with OUT_CONTACTS.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(
            [
                "pdb_id",
                "isoform",
                "state",
                "ligand",
                "helix",
                "cage_residue",
                "ligand_atom",
                "distance_A",
            ]
        )
        for m in measurements:
            cage = CAGE[m.isoform]
            for helix, atom_name, d in m.hbonds:
                resseq, resname, donor_atom = cage[helix]
                w.writerow(
                    [
                        m.pdb_id,
                        m.isoform,
                        m.state,
                        m.ligand,
                        helix,
                        f"{resname}{resseq}.{donor_atom}",
                        atom_name,
                        f"{d:.2f}",
                    ]
                )


def main() -> None:
    ms = run()
    write(ms)
    for m in ms:
        span = "n/a" if m.acceptor_pair_span is None else f"{m.acceptor_pair_span:.2f}"
        print(
            f"{m.pdb_id} {m.isoform} {m.state:10s} {m.ligand[:28]:28s} "
            f"contacts={m.n_contacts} span={span:>5s} "
            f"vol={m.head_free_volume:6.1f} A^3"
        )
    print(f"\nwrote {OUT_GEOMETRY.relative_to(_REPO)}")
    print(f"wrote {OUT_CONTACTS.relative_to(_REPO)}")


if __name__ == "__main__":
    main()
