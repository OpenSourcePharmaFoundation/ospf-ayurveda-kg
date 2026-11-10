"""Fetch PubMed Central full text so dosing numbers can be read, not recalled.

Abstracts almost never carry the administered dose or the in-vitro
concentration; those live in Methods.  This pulls the open-access full text and
strips tags, leaving plain text that can be grepped for units.
"""

import re
import sys
import urllib.request

from src.analysis.retina_expression.census_client import fix_proxy_env

BIOC = (
    "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi"
    "/BioC_xml/{pmcid}/unicode"
)


def fetch(pmcid: str) -> str:
    fix_proxy_env()
    with urllib.request.urlopen(BIOC.format(pmcid=pmcid), timeout=120) as fh:
        xml = fh.read().decode("utf-8", errors="replace")
    # BioC wraps each passage's prose in <text>...</text>; that is all we want.
    parts = re.findall(r"<text>(.*?)</text>", xml, flags=re.S)
    out = "\n".join(parts)
    for a, b in (("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&"), ("&quot;", '"')):
        out = out.replace(a, b)
    return out


if __name__ == "__main__":
    sys.stdout.write(fetch(sys.argv[1]))
