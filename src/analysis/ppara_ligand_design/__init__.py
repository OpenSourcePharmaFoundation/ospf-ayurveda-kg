"""Non-acidic PPARalpha ligand design (Step 7).

The AF-2 cage geometry is measured from deposited coordinates rather than
recalled, candidate head groups are screened against that measurement, the
efficacy cost of a neutral head is modelled explicitly, and the resulting
scaffolds are carried through the Step 5 ocular exposure model so that the
margin and the efficacy are multiplied rather than quoted separately.

Modules
-------
``structures``    PDB set, mmCIF reader, and the cage residues per isoform.
``af2_cage``      Donor geometry, H-bond contacts, arm I free volume.
``headgroups``    Head-group screen: lone-pair capacity, span, footprint.
``h12_efficacy``  Two-state H12 model; how much Emax a neutral head costs.
``scaffolds``     Five designs, profiled end to end against fenofibric acid.
"""
