"""Measured pharmacology for the efflux axis, pulled from ChEMBL.

The knowledge graph cannot rank this axis.  Its ``Compound-TARGETS-Gene``
edges are 95% Comparative Toxicogenomics Database, and on these nine genes
they are expression-change sentences rather than binding measurements -- see
``gnn_rank.edge_semantics``.  So the ranking has to rest on affinity data the
repository does not yet hold, which is what this module fetches.

The resolution path is the same one ``src/scrapers/chembl/chembl_target_axis.py``
established in Step 1 (gene symbol -> UniProt accession -> ChEMBL target ->
activities), re-expressed here as a parameterised function instead of a
script hardcoded to the DR panel, so that the efflux axis does not have to
overwrite Step 1's outputs to reuse its method.

Only human SINGLE PROTEIN targets are kept.  Activities are restricted to
IC50/EC50/Ki/Kd in nM with a ``pchembl_value``, which is the field ChEMBL
populates only when it could convert the reported value to a -log10 molar
potency; rows without it are missing data, not weak binding.
"""

from __future__ import annotations

import dataclasses
import time
from pathlib import Path

import pandas as pd
import requests

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"
CHEMBL_BASE = "https://www.ebi.ac.uk/chembl/api/data"
ACTIVITY_TYPES = ["IC50", "EC50", "Ki", "Kd"]
RATE_LIMIT_DELAY = 0.2
PAGE_LIMIT = 1000

_SESSION = requests.Session()
_SESSION.headers.update(
    {"User-Agent": "ospf-efflux-axis", "Accept": "application/json"}
)


def _get(url: str, params: dict | None = None) -> dict | None:
    resp = _SESSION.get(url, params=params, timeout=60)
    time.sleep(RATE_LIMIT_DELAY)
    if resp.status_code != 200:
        print(f"  ERROR {resp.status_code} {resp.url}")
        return None
    return resp.json()


def _paginate(path: str, key: str, params: dict) -> list[dict]:
    """Follow ChEMBL's ``page_meta.next`` until exhausted."""
    out: list[dict] = []
    url = f"{CHEMBL_BASE}/{path}.json"
    params = {**params, "limit": PAGE_LIMIT}
    while url:
        page = _get(url, params)
        params = None  # the `next` link already carries the query string
        if not page:
            break
        out.extend(page.get(key, []))
        nxt = page.get("page_meta", {}).get("next")
        url = f"https://www.ebi.ac.uk{nxt}" if nxt else None
    return out


# --- target resolution ------------------------------------------------------


@dataclasses.dataclass
class Resolved:
    gene: str
    uniprot: str
    chembl_id: str | None
    pref_name: str | None
    target_type: str | None
    status: str


def resolve_target(gene: str, uniprot: str) -> Resolved:
    """UniProt accession -> ChEMBL SINGLE PROTEIN target.

    The accession is supplied by ``axis.py`` rather than looked up, because a
    gene-symbol search returns paralogues (searching NR1H3 also returns LXR
    targets for mouse and rat and two protein-family pseudo-targets) and the
    axis is small enough that the accessions are worth pinning.
    """
    data = _get(
        f"{CHEMBL_BASE}/target.json",
        {"target_components__accession": uniprot, "limit": 20},
    )
    targets = (data or {}).get("targets", [])
    single = [
        t
        for t in targets
        if t.get("target_type") == "SINGLE PROTEIN"
        and t.get("organism") == "Homo sapiens"
    ]
    if not single:
        return Resolved(gene, uniprot, None, None, None, "unresolved")
    t = single[0]
    return Resolved(
        gene,
        uniprot,
        t["target_chembl_id"],
        t.get("pref_name"),
        t.get("target_type"),
        "resolved",
    )


# --- activities and mechanisms ---------------------------------------------

_ACTIVITY_FIELDS = [
    "molecule_chembl_id",
    "standard_type",
    "standard_relation",
    "standard_value",
    "standard_units",
    "pchembl_value",
    "assay_chembl_id",
    "assay_type",
    "assay_description",
    "document_chembl_id",
    "target_organism",
    "data_validity_comment",
]


def fetch_activities(gene: str, target_id: str) -> pd.DataFrame:
    rows = _paginate(
        "activity",
        "activities",
        {
            "target_chembl_id": target_id,
            "standard_type__in": ",".join(ACTIVITY_TYPES),
            "standard_units": "nM",
            "pchembl_value__isnull": "false",
        },
    )
    if not rows:
        return pd.DataFrame(columns=["gene", "chembl_target_id", *_ACTIVITY_FIELDS])
    df = pd.DataFrame(rows)
    for c in _ACTIVITY_FIELDS:
        if c not in df:
            df[c] = None
    df = df[_ACTIVITY_FIELDS].copy()
    df.insert(0, "chembl_target_id", target_id)
    df.insert(0, "gene", gene)
    return df


def fetch_mechanisms(gene: str, target_id: str) -> pd.DataFrame:
    rows = _paginate("mechanism", "mechanisms", {"target_chembl_id": target_id})
    cols = [
        "molecule_chembl_id",
        "mechanism_of_action",
        "action_type",
        "max_phase",
        "mechanism_comment",
    ]
    if not rows:
        return pd.DataFrame(columns=["gene", "chembl_target_id", *cols])
    df = pd.DataFrame(rows)
    for c in cols:
        if c not in df:
            df[c] = None
    df = df[cols].copy()
    df.insert(0, "chembl_target_id", target_id)
    df.insert(0, "gene", gene)
    return df


def fetch_molecules(chembl_ids: list[str]) -> pd.DataFrame:
    """Molecule properties for the candidates, in batches of 50.

    ``cx_logd`` and ``cx_most_apka``/``cx_most_bpka`` are requested explicitly:
    Step 5 found them null for the fibrates, and whether they are populated for
    a *neutral* chemotype is itself part of this step's answer.
    """
    want = [
        "full_mwt",
        "alogp",
        "cx_logp",
        "cx_logd",
        "cx_most_apka",
        "cx_most_bpka",
        "psa",
        "hba",
        "hbd",
        "rtb",
        "aromatic_rings",
        "heavy_atoms",
        "qed_weighted",
        "num_ro5_violations",
        "molecular_species",
    ]
    out = []
    for i in range(0, len(chembl_ids), 50):
        chunk = chembl_ids[i : i + 50]
        data = _get(
            f"{CHEMBL_BASE}/molecule.json",
            {"molecule_chembl_id__in": ",".join(chunk), "limit": 50},
        )
        for mol in (data or {}).get("molecules", []):
            props = mol.get("molecule_properties") or {}
            struct = mol.get("molecule_structures") or {}
            out.append(
                {
                    "molecule_chembl_id": mol["molecule_chembl_id"],
                    "pref_name": mol.get("pref_name"),
                    "max_phase": mol.get("max_phase"),
                    "first_approval": mol.get("first_approval"),
                    "oral": mol.get("oral"),
                    "canonical_smiles": struct.get("canonical_smiles"),
                    **{k: props.get(k) for k in want},
                }
            )
    return pd.DataFrame(out)


def pull_axis(axis_genes) -> dict[str, pd.DataFrame]:
    """Resolve every axis gene and pull its pharmacology."""
    resolutions, activities, mechanisms = [], [], []
    for g in axis_genes:
        r = resolve_target(g.symbol, g.uniprot)
        print(f"{g.symbol:6s} {g.uniprot} -> {r.chembl_id} ({r.status})")
        if r.chembl_id:
            a = fetch_activities(g.symbol, r.chembl_id)
            m = fetch_mechanisms(g.symbol, r.chembl_id)
            print(f"        {len(a):5d} activities, {len(m):3d} mechanisms")
            activities.append(a)
            mechanisms.append(m)
        resolutions.append(
            {
                **dataclasses.asdict(r),
                "gene_class": g.gene_class,
                "arm": g.arm,
                "ligandable": g.ligandable,
                "n_activities": len(activities[-1]) if r.chembl_id else 0,
                "n_mechanisms": len(mechanisms[-1]) if r.chembl_id else 0,
            }
        )
    empty = pd.DataFrame()
    return {
        "targets": pd.DataFrame(resolutions),
        "activities": pd.concat(activities, ignore_index=True) if activities else empty,
        "mechanisms": pd.concat(mechanisms, ignore_index=True) if mechanisms else empty,
    }
