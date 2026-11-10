"""PDB structure set and a minimal mmCIF reader.

Step 7 of ``docs/prompts/dr-solve-open-questions-prompt.md``.  The SAR agent in
the source run asserted that the PPARalpha AF-2 contact network is all-donor,
that the geometry wants a bidentate acceptor pair "~2.2-3.2 A apart", and that
PPARalpha's arm I is "narrower" than PPARgamma's.  Every one of those claims is
checkable against deposited coordinates and none of them was checked.  This
module fetches the coordinates so ``af2_cage`` can measure them.

Structure selection, and why each entry is here
-----------------------------------------------
The set has to support three separate measurements, so it is chosen for
contrast rather than for quality:

* **PPARalpha + full agonist** (1I7G, 2P54, 3VI8, 1K7L, 4BCR) - the cage in its
  active, H12-closed state with a carboxylate head bound.  These give the donor
  geometry and the H-bond distances the pharmacophore has to reproduce.  They
  deliberately span four different acid chemotypes (an alpha-aryloxy acid, a
  tyrosine-based agonist, pemafibrate, tesaglitazar, a fibrate) so a distance
  that holds across all of them is a property of the receptor rather than of
  one ligand.
* **PPARalpha + antagonist** (1KKQ, GW6471) - H12 is displaced.  This is the
  negative control for the efficacy model in ``h12_efficacy``: it shows what
  the cage looks like when the Tyr464 contact is *not* paid for, and it is the
  reason that model is anchored on a structure rather than on an assertion.
* **PPARgamma** (2PRG, 4EMA) and **PPARdelta** (3TKM, 2XYW) - the isoform
  comparison.  "Arm I is narrower at alpha" is the single most actionable claim
  in the source analysis (it is what rules the thiazolidinedione out and the
  oxadiazolone in) and it was stated without a number.  Measuring the same free
  volume in all three isoforms turns it into one.

Caching
-------
Files land in ``data/raw/pdb/`` and are gitignored: they are byte-identical
re-downloads from RCSB, so caching them is a courtesy to the network and not a
data artefact worth versioning.
"""

from __future__ import annotations

import dataclasses
import pathlib
import subprocess
import urllib.request

_REPO = pathlib.Path(__file__).resolve().parents[3]
CACHE = _REPO / "data" / "raw" / "pdb"
RCSB = "https://files.rcsb.org/download/{pdb_id}.cif"

# Residues that are solvent, cryoprotectant or crystallisation additive.  They
# are not part of the pocket and must not count towards its free volume.
SOLVENT = {
    "HOH",
    "SO4",
    "GOL",
    "EDO",
    "CL",
    "NA",
    "ACT",
    "PO4",
    "MG",
    "ZN",
    "DMS",
    "TRS",
    "PEG",
    "MPD",
    "IOD",
    "CA",
    "K",
    "BR",
    "NO3",
    "FMT",
    "CAC",
    "EPE",
    "NI",
    "MN",
    "BME",
    "TLA",
    "CIT",
    "PGE",
    "1PE",
    "P6G",
    "MES",
    "BOG",
    "LDA",
    "OLC",
    "UNX",
    "NH4",
    "FLC",
    "SCN",
}


@dataclasses.dataclass(frozen=True)
class Entry:
    pdb_id: str
    isoform: str  # PPARA | PPARG | PPARD
    ligand: str  # PDB chemical component id of the bound ligand
    ligand_name: str
    state: str  # agonist | antagonist
    note: str


# The four cage residues per isoform, with the donor heavy atom named.
#
# PPARalpha and PPARgamma are a Ser/Tyr-or-His/His/Tyr quartet; PPARdelta
# replaces the H3 serine with a threonine.  All of them donate: Ser OG and Thr
# OG1 are hydroxyls, Tyr OH is a phenol, His NE2 carries the imidazole N-H in
# the tautomer seen in these complexes.  That is the "all-donor" claim, and
# ``af2_cage`` checks it rather than taking it on trust.
CAGE = {
    "PPARA": {
        "H3": (280, "SER", "OG"),
        "H5": (314, "TYR", "OH"),
        "H11": (440, "HIS", "NE2"),
        "H12": (464, "TYR", "OH"),
    },
    "PPARG": {
        "H3": (289, "SER", "OG"),
        "H5": (323, "HIS", "NE2"),
        "H11": (449, "HIS", "NE2"),
        "H12": (473, "TYR", "OH"),
    },
    # PPARdelta keeps its own numbering rather than gamma-equivalent numbering.
    # These four were not taken from a paper: they are the residues whose side
    # chains lie within 3.6 A of the GW0742 carboxylate in 3TKM, found by
    # contact search and then checked against the gamma/alpha alignment.
    "PPARD": {
        "H3": (252, "THR", "OG1"),
        "H5": (287, "HIS", "NE2"),
        "H11": (413, "HIS", "NE2"),
        "H12": (437, "TYR", "OH"),
    },
}

ENTRIES = (
    Entry(
        "1K7L",
        "PPARA",
        "544",
        "GW409544",
        "agonist",
        "tyrosine-based full agonist co-crystallised with an SRC-1 "
        "coactivator peptide; the canonical active-state alpha structure",
    ),
    Entry(
        "1I7G",
        "PPARA",
        "AZ2",
        "tesaglitazar (AZ 242)",
        "agonist",
        "alpha/gamma dual alpha-alkoxy-propanoic acid",
    ),
    Entry(
        "2P54",
        "PPARA",
        "735",
        "GW590735",
        "agonist",
        "alpha-selective carboxylic acid agonist",
    ),
    Entry(
        "3VI8",
        "PPARA",
        "13M",
        "pemafibrate analogue (K-877 series)",
        "agonist",
        "the most potent fibrate chemotype in the DR candidate set, bound",
    ),
    Entry(
        "4BCR",
        "PPARA",
        "WY1",
        "WY-14643 / pirinixic acid",
        "agonist",
        "the classical alpha tool agonist; smallest acid head in the set",
    ),
    Entry(
        "1KKQ",
        "PPARA",
        "471",
        "GW6471",
        "antagonist",
        "antagonist with H12 displaced and a corepressor peptide bound; "
        "the structural control for the H12 efficacy model",
    ),
    Entry(
        "2PRG",
        "PPARG",
        "BRL",
        "rosiglitazone",
        "agonist",
        "thiazolidinedione head in gamma's arm I - the head that does not "
        "fit alpha, measured where it does fit",
    ),
    Entry(
        "4EMA",
        "PPARG",
        "BRL",
        "rosiglitazone",
        "agonist",
        "second rosiglitazone complex; replicate for gamma",
    ),
    Entry(
        "3TKM",
        "PPARD",
        "GW0",
        "GW0742",
        "agonist",
        "delta-selective carboxylic acid agonist engaging all four donors",
    ),
    Entry(
        "2XYW",
        "PPARD",
        "08S",
        "sulfonylthiadiazole",
        "agonist",
        "a non-carboxylate delta ligand that reaches only the H3 threonine - "
        "kept as the counter-example of a head that binds without the cage",
    ),
)

BY_ID = {e.pdb_id: e for e in ENTRIES}


def fetch(pdb_id: str) -> pathlib.Path:
    """Return a local path to the mmCIF, downloading once if needed.

    ``curl`` is tried first and ``urllib`` second.  That ordering is not
    cosmetic: under the sandboxed network this repository is developed in,
    egress goes through a local filtering proxy that Python's socket layer
    cannot resolve, while curl honours the same proxy environment correctly.
    Preferring curl is what makes this module runnable in the environment it
    was written in; the urllib branch keeps it runnable without curl.
    """
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{pdb_id}.cif"
    if path.exists() and path.stat().st_size > 0:
        return path

    url = RCSB.format(pdb_id=pdb_id)
    try:
        subprocess.run(["curl", "-sSfL", "-o", str(path), url], check=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        with urllib.request.urlopen(url, timeout=60) as r:
            path.write_bytes(r.read())

    if not path.exists() or path.stat().st_size == 0:
        raise RuntimeError(f"failed to download {pdb_id} from {url}")
    return path


@dataclasses.dataclass(frozen=True)
class Atom:
    group: str  # ATOM | HETATM
    name: str  # auth atom name, e.g. "OG"
    resname: str  # auth component id, e.g. "SER"
    chain: str  # auth asym id
    resseq: int  # auth seq id
    element: str
    x: float
    y: float
    z: float
    altloc: str

    @property
    def xyz(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)


def parse(path: pathlib.Path) -> list[Atom]:
    """Read ``_atom_site`` records out of an mmCIF.

    A full mmCIF parser is not needed and would be a dependency; the atom loop
    is fixed-column-order *per file* and the column order is declared in the
    header immediately above it, which is all this needs.  Alternate
    conformations are kept and filtered at the point of use, because which
    altloc is right depends on which ligand copy is being measured.
    """
    cols: list[str] = []
    out: list[Atom] = []
    in_loop = False
    for line in path.read_text().splitlines():
        if line.startswith("_atom_site."):
            cols.append(line.strip().split(".", 1)[1])
            in_loop = True
            continue
        if in_loop and line[:4] in ("ATOM", "HETA"):
            rec = dict(zip(cols, line.split()))
            try:
                out.append(
                    Atom(
                        group=rec["group_PDB"],
                        name=rec["auth_atom_id"].strip('"'),
                        resname=rec["auth_comp_id"],
                        chain=rec["auth_asym_id"],
                        resseq=int(rec["auth_seq_id"]),
                        element=rec["type_symbol"],
                        x=float(rec["Cartn_x"]),
                        y=float(rec["Cartn_y"]),
                        z=float(rec["Cartn_z"]),
                        altloc=rec["label_alt_id"],
                    )
                )
            except (KeyError, ValueError):
                continue
        elif in_loop and out and line.startswith("#"):
            in_loop = False
    return out
