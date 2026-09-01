"""Sensitivity: how each named unresolved question moves the ranking."""
CAP=1.5
def comp(anchor, raw): return round(anchor + max(-CAP,min(CAP,raw)),2)

S=[
("CamSA mouse study is therapeutic-dose / epidemic strain / survival (tier 6.5, not 4.0)",
 "CamSA", 4.50, comp(6.5-0.50-0.25-0.25, 1.70), "Bile-acid germination dose-response, $50-100K"),
("Ribaxamase Phase 2b does NOT support a Phase 3 endpoint",
 "Ribaxamase", 7.70, comp(2.00-0.50, 1.20), "Diligence pass, $150-300K"),
("Ribaxamase Phase 2b fully verified as reported (removes -1.0 unverified deduction)",
 "Ribaxamase", 7.70, comp(8.0-0.50, 1.20), "Diligence pass, $150-300K"),
("Niclosamide selectivity ratio (anti-TcdB vs uncoupling) returns >10x",
 "Niclosamide", 4.75, comp(5.75, -1.00+0.70), "Selectivity assay, $60-120K"),
("Niclosamide anaerobic fecal-slurry stability FAILS (redox gate -> FAIL)",
 "Niclosamide", 4.75, "DISQUALIFIED", "Fecal-slurry panel, $80-150K"),
("Berberine spo0A effect NOT reproduced in vivo (removes -0.5 anchor deduction)",
 "Berberine", 4.15, comp(5.50, -0.85), "spo0A in vivo, $150-300K"),
("Ibezapolstat: axis base rate weighted -0.5 rather than -0.8-for-8 (-1.5)",
 "Ibezapolstat", 6.25, comp(6.5-0.50-0.25, 1.70), "Only a Phase 3 resolves this"),
("UDCA free fecal-water conc exceeds a measured anti-germination IC50",
 "UDCA", 4.00, comp(2.00+0.50+1.50, 1.90), "IC50 assay then Stage 0, $50-100K + $1-3M"),
("Anti-germinant CLASS question answered NO (kills C1 cluster together)",
 "CamSA/UDCA/TUDCA", "4.50/4.00/2.30", "all -> DISQUALIFIED", "Dedicated design; NOBODY has proposed one"),
]
print(f"{'IF THIS RESOLVES...':<74} | {'CANDIDATE':<18} | {'NOW':<16} | {'THEN':<16} | RESOLVED BY")
print("-"*185)
for q,c,now,then,exp in S:
    print(f"{q:<74} | {c:<18} | {str(now):<16} | {str(then):<16} | {exp}")
