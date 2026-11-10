"""Henderson-Hasselbalch for a monoprotic acid.

Two quantities come out of this module and they do different jobs.

``log_d`` is the apparent partition coefficient at a stated pH.  It drives
*passive permeability*, and for these compounds it is four log units below
logP: at pKa ~3.1 and pH 7.4 the neutral species is 6 parts in 10^5, and only
the neutral species crosses a lipid bilayer by diffusion.

``ph_partition`` is the equilibrium ratio of free drug between two aqueous
compartments at different pH.  It is the term people reach for when they say
an acid is "trapped" somewhere, and for a pKa-3 acid it is almost exactly
10^(pH_in - pH_out) -- a factor of two between cytosol and plasma, not the
orders of magnitude that ion trapping gives a base in a lysosome.

The distinction matters for the model's structure.  **Passive permeability
cancels out of a steady-state partition ratio across a purely passive
barrier**: if the only routes in and out are the same route, the ratio is one
however slow it is, and low permeability buys time to equilibrium, not a lower
plateau.  Permeability only lowers the plateau when it competes with a
*different* clearance route -- active efflux, or bulk flow out of the
compartment.  That is why ``barrier.py`` is written as a competition between
clearances and not as a permeability cut-off.
"""

from __future__ import annotations

import numpy as np


def fraction_neutral(pka, ph=7.4):
    """Fraction of a monoprotic acid present as the neutral species."""
    return 1.0 / (1.0 + np.power(10.0, np.asarray(ph) - np.asarray(pka)))


def log_d(logp, pka, ph=7.4):
    """logD at a stated pH for a monoprotic acid."""
    return np.asarray(logp) + np.log10(fraction_neutral(pka, ph))


def ph_partition(pka, ph_in, ph_out):
    """Equilibrium free-drug ratio in / out for a monoprotic acid.

    Derived by requiring the *neutral* species to be equal on both sides:

        Cu,in / Cu,out = (1 + 10^(pH_in - pKa)) / (1 + 10^(pH_out - pKa))
    """
    pka = np.asarray(pka)
    num = 1.0 + np.power(10.0, np.asarray(ph_in) - pka)
    den = 1.0 + np.power(10.0, np.asarray(ph_out) - pka)
    return num / den
