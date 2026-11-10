"""Minimal NCBI E-utilities client for the FGF21 concentration-bridge literature sweep.

The point of putting this in the repo rather than running ad-hoc curl is
reproducibility: every number in ``docs/notes/fgf21-concentration-bridge.md``
should be traceable to a PMID that this module can re-fetch.

No API key is used, so E-utilities caps us at 3 requests/second; ``_THROTTLE``
keeps us under that.
"""

import json
import time
import urllib.parse
import urllib.request

from src.analysis.retina_expression.census_client import fix_proxy_env

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
_THROTTLE = 0.4  # seconds between requests (E-utilities: 3/s without a key)


def _get(endpoint: str, params: dict) -> str:
    # The sandbox advertises its egress proxy as ``localhost:<port>``, which does
    # not resolve here; ``urllib`` needs it rewritten to 127.0.0.1.  Same fix the
    # Census client applies, reused rather than duplicated.
    fix_proxy_env()
    url = f"{BASE}/{endpoint}?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as fh:
        body = fh.read().decode("utf-8", errors="replace")
    time.sleep(_THROTTLE)
    return body


def esearch(term: str, retmax: int = 40, db: str = "pubmed") -> list[str]:
    """Return record IDs for a query.

    ``db="pmc"`` searches *full text*, which is the only way to find papers by
    the concentrations they report: absolute values live in Results tables, not
    in abstracts.
    """
    body = _get(
        "esearch",
        {
            "db": db,
            "term": term,
            "retmax": retmax,
            "retmode": "json",
            "sort": "relevance",
        },
    )
    return json.loads(body)["esearchresult"].get("idlist", [])


def efetch_abstracts(pmids: list[str]) -> str:
    """Return the MEDLINE text record for a batch of PMIDs."""
    if not pmids:
        return ""
    return _get(
        "efetch",
        {
            "db": "pubmed",
            "id": ",".join(pmids),
            "rettype": "abstract",
            "retmode": "text",
        },
    )
