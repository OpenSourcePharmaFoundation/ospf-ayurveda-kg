"""External calibration: measured ocular partition for drugs that are not
anionic efflux substrates, at the analogous blood-aqueous barrier.

The model's neural-retina ``Kp,uu`` is calibrated on one mouse experiment.  One
experiment is not a calibration, it is a point.  This module supplies the
independent check: human studies in which a systemically dosed drug was
measured in aqueous humour *and* in plasma in the same patients, at cataract
surgery.

Aqueous humour is the useful comparator because it is effectively
protein-free -- total protein is of order 0.5 mg/mL against plasma's 70 -- so
the measured aqueous concentration *is* a free concentration, and

    Kp,uu = (C_aqueous / C_plasma,total) / fu_plasma

converts a published ratio into the same quantity the model computes.  Doing
that conversion is the whole point: the raw aqueous-to-plasma ratios in this
literature are often read as "penetration", when for a highly-bound drug they
are mostly a statement about plasma binding.

What the check establishes: at a tight-junction ocular barrier, a drug that is
**not** an anionic efflux substrate reaches a free concentration roughly half
of free plasma.  The model puts an anionic fibrate an order of magnitude below
that, and the reason is the efflux machinery measured in human retinal
endothelium.  If the model instead returned ~0.5 for a fibrate it would be
saying the pumps do not exist.

Caveat, stated rather than buried: the blood-aqueous barrier (ciliary
epithelium and iris vessels) is not the blood-retinal barrier.  Both are
tight-junction barriers with ABC and SLC transporters, but they are different
tissues, and this is a plausibility check, not a substitute measurement.
"""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True)
class OcularAnchor:
    drug: str
    charge: str
    aqueous_over_plasma: tuple[float, float]  # measured ratio, lo-hi
    fu_plasma: tuple[float, float]  # published range
    source: str

    def kpuu(self) -> tuple[float, float]:
        """Convert the published ratio into a free/free partition ratio."""
        lo = self.aqueous_over_plasma[0] / self.fu_plasma[1]
        hi = self.aqueous_over_plasma[1] / self.fu_plasma[0]
        return lo, hi


ANCHORS = [
    OcularAnchor(
        "aciclovir",
        "neutral",
        (3.26 / 8.74, 3.26 / 8.74),
        (0.78, 0.91),
        "Hung 1984, Br J Ophthalmol 68:192, PMID 6696872 -- 5 x 400 mg oral before "
        "cataract extraction; aqueous 3.26 µM vs plasma 8.74 µM (means)",
    ),
    OcularAnchor(
        "levofloxacin",
        "zwitterion",
        (0.33, 0.57),
        (0.62, 0.76),
        "Pea 2005, Antimicrob Agents Chemother 49:2554, PMID 15917572 -- 2 x 500 mg oral; "
        "aqueous-to-plasma 0.33-0.57 over 1.5-6 h",
    ),
    OcularAnchor(
        "pefloxacin",
        "zwitterion",
        (0.50, 0.89),
        (0.70, 0.80),
        "Salvanet-Bouccara 1991, J Fr Ophtalmol 14:260, PMID 1955654 -- 400 mg bd x 3 d; "
        "aqueous-to-serum 0.50-0.89 (mean 0.68), n=38",
    ),
    # The one acid in the set, and it is a negative result rather than a ratio:
    # it bounds, it does not calibrate.
    OcularAnchor(
        "indometacin (acid, 99% bound)",
        "anion",
        (0.0, 0.0),
        (0.01, 0.01),
        "Sanders 1983, Arch Ophthalmol 101:1614, PMID 6626018 -- oral dosing gave a mean "
        "aqueous level BELOW the assay's limit against a mean serum level of 642 ng/mL; "
        "a bound, not a measurement",
    ),
]

# Mechanistic anchor for the efflux term itself, at the retinal barrier proper.
EFFLUX_ANCHOR = (
    "Fujii 2015, Drug Metab Dispos 43:1956, PMID 26431714 -- pravastatin, an anionic "
    "statin acid, at the rat BRB: retinal uptake index BELOW that expected from its "
    "lipophilicity, vitreal elimination rate constant 1.66x that of the bulk-flow marker "
    "mannitol, and efflux reduced by pravastatin, digoxin and benzylpenicillin. The "
    "authors' conclusion is that retina-to-blood transport is dominant. That is the "
    "direction the model's efflux term encodes, measured for the closest structural "
    "analogue anyone has studied at this barrier."
)


def table() -> list[list[str]]:
    rows = []
    for a in ANCHORS:
        lo, hi = a.kpuu()
        ratio = (
            f"{a.aqueous_over_plasma[0]:.2f}"
            if a.aqueous_over_plasma[0] == a.aqueous_over_plasma[1]
            else f"{a.aqueous_over_plasma[0]:.2f}-{a.aqueous_over_plasma[1]:.2f}"
        )
        kp = (
            "< detection"
            if hi == 0
            else (f"{lo:.2f}" if abs(hi - lo) < 1e-9 else f"{lo:.2f}-{hi:.2f}")
        )
        rows.append(
            [
                a.drug,
                a.charge,
                ratio,
                f"{a.fu_plasma[0]:.2f}-{a.fu_plasma[1]:.2f}",
                kp,
                a.source,
            ]
        )
    return rows
