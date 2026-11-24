"""Free-fraction arithmetic, and the serum correction on a published EC50.

The inconsistency this module exists to remove: a free tissue concentration
compared against a *nominal* EC50 from a cell assay run in serum-containing
medium counts protein binding twice.  The tissue number has already had the
free fraction taken out of it; the EC50 has not, because the albumin in the
assay medium bound some of the dose and the reported EC50 is the total that
was added.

The correction is the binding-dilution relation.  If binding is linear in
albumin concentration -- true well below saturation, which is where an EC50
sits -- then

    1/fu - 1 = K * [albumin]

so a medium holding a fraction ``s`` of the albumin of plasma has

    fu_assay = 1 / (1 + (1/fu_plasma - 1) * s)

and the free EC50 is ``EC50_nominal * fu_assay``.  Correcting LOWERS the EC50,
i.e. it runs in the compounds' favour.  It is applied here for exactly that
reason: a correction that only ever worsened the answer would be suspect.

Size of the effect, at the extremes of the assay prior:

    fu_plasma = 0.01, 0.7% FBS  ->  fu_assay = 0.72   (1.4x)
    fu_plasma = 0.01, 10%  FBS  ->  fu_assay = 0.15   (6.6x)
    fu_plasma = 0.003, 10% FBS  ->  fu_assay = 0.052  (19x, = 1.3 log)

which is the "worth about a log" the step description anticipates -- true at
the high-serum end, and a third of that at the low-serum end.  The spread
between those two is itself one of the larger uncertainties in the model, and
``sensitivity.py`` is asked to rank it against the others.
"""

from __future__ import annotations

import numpy as np


def fu_in_medium(fu_plasma, serum_fraction, albumin_ratio):
    """Free fraction in an assay medium holding diluted serum.

    ``serum_fraction``  volume fraction of neat serum in the medium
    ``albumin_ratio``   albumin of that serum relative to human plasma
    """
    fu_plasma = np.asarray(fu_plasma, dtype=float)
    s = np.asarray(serum_fraction) * np.asarray(albumin_ratio)
    return 1.0 / (1.0 + (1.0 / fu_plasma - 1.0) * s)


def free_ec50(ec50_nominal, fu_plasma, serum_fraction, albumin_ratio):
    """Free-drug EC50 from a nominal EC50 measured in serum-containing medium."""
    return np.asarray(ec50_nominal) * fu_in_medium(
        fu_plasma, serum_fraction, albumin_ratio
    )
