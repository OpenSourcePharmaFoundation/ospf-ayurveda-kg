// Alstonia scholaris
CREATE (p1:Plant {
    name: "Alstonia scholaris (L.) R.Br.",
    family: "APOCYNACEAE",
    common_name: "Chatium, Chattiyan",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000009268&column=szBarcode"
})
CREATE (u1:Usage {name: "Chronic diarrhea"})
CREATE (u2:Usage {name: "Asthma"})
CREATE (u3:Usage {name: "Cardiac"})
CREATE (u4:Usage {name: "Haemostatic"})
CREATE (u5:Usage {name: "Beri-beri"})
CREATE (u6:Usage {name: "Dropsy"})
CREATE (u7:Usage {name: "Congested liver"})
CREATE (u8:Usage {name: "Sores"})
CREATE (u9:Usage {name: "Ulcers"})
CREATE (u10:Usage {name: "Tumours"})
CREATE (u11:Usage {name: "Rheumatic swellings"})
CREATE (u12:Usage {name: "Caustic to open abscesses"})
CREATE (p1)-[:USED_FOR {part: "bark"}]->(u1)
CREATE (p1)-[:USED_FOR {part: "bark"}]->(u2)
CREATE (p1)-[:USED_FOR {part: "bark"}]->(u3)
CREATE (p1)-[:USED_FOR {part: "bark"}]->(u4)
CREATE (p1)-[:USED_FOR {part: "leaf"}]->(u5)
CREATE (p1)-[:USED_FOR {part: "leaf"}]->(u6)
CREATE (p1)-[:USED_FOR {part: "leaf"}]->(u7)
CREATE (p1)-[:USED_FOR {part: "latex"}]->(u8)
CREATE (p1)-[:USED_FOR {part: "latex"}]->(u9)
CREATE (p1)-[:USED_FOR {part: "latex"}]->(u10)
CREATE (p1)-[:USED_FOR {part: "latex"}]->(u11)
CREATE (p1)-[:USED_FOR {part: "ash"}]->(u12)

// Azadirachta indica
CREATE (p2:Plant {
    name: "Azadirachta indica (L.) A.Juss.",
    family: "MELIACEAE",
    common_name: "Nim",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000009901&column=szBarcode"
})
CREATE (u13:Usage {name: "Skin troubles"})
CREATE (u14:Usage {name: "Antiseptic properties"})
CREATE (u15:Usage {name: "Boils"})
CREATE (u16:Usage {name: "Eczema"})
CREATE (u17:Usage {name: "Ulcers"})
CREATE (u18:Usage {name: "Tonic"})
CREATE (u19:Usage {name: "Stomachic"})
CREATE (u20:Usage {name: "Purgative"})
CREATE (u21:Usage {name: "Emollient"})
CREATE (p2)-[:USED_FOR {part: "bark"}]->(u13)
CREATE (p2)-[:USED_FOR {part: "leaf"}]->(u14)
CREATE (p2)-[:USED_FOR {part: "leaf"}]->(u15)
CREATE (p2)-[:USED_FOR {part: "leaf"}]->(u16)
CREATE (p2)-[:USED_FOR {part: "leaf"}]->(u17)
CREATE (p2)-[:USED_FOR {part: "flower"}]->(u18)
CREATE (p2)-[:USED_FOR {part: "flower"}]->(u19)
CREATE (p2)-[:USED_FOR {part: "berry"}]->(u20)
CREATE (p2)-[:USED_FOR {part: "berry"}]->(u21)

// Cassia fistula
CREATE (p3:Plant {
    name: "Cassia fistula L.",
    family: "CAESALPINIACEAE",
    common_name: "Amaltas",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000003513&column=szBarcode"
})
CREATE (u22:Usage {name: "Febrifugal"})
CREATE (u23:Usage {name: "Astringent"})
CREATE (u24:Usage {name: "Antibilious"})
CREATE (p3)-[:USED_FOR {part: "flower"}]->(u20)
CREATE (p3)-[:USED_FOR {part: "flower"}]->(u22)
CREATE (p3)-[:USED_FOR {part: "flower"}]->(u23)
CREATE (p3)-[:USED_FOR {part: "flower"}]->(u24)

// Cyperus rotundus
CREATE (p4:Plant {
    name: "Cyperus rotundus L.",
    family: "CYPERACEAE",
    common_name: "Motha, Mutha (Beng.)",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000003241&column=szBarcode"
})
CREATE (u25:Usage {name: "Diuretic"})

CREATE (u26:Usage {name: "Diaphoretic"})
CREATE (u27:Usage {name: "Astringent"})
CREATE (u28:Usage {name: "Stomach complaints"})
CREATE (u29:Usage {name: "Bowel complaints"})
CREATE (p4)-[:USED_FOR {part: "root"}]->(u25)
CREATE (p4)-[:USED_FOR {part: "root"}]->(u26)
CREATE (p4)-[:USED_FOR {part: "root"}]->(u27)
CREATE (p4)-[:USED_FOR {part: "root"}]->(u28)
CREATE (p4)-[:USED_FOR {part: "root"}]->(u29)

// Santalum album
CREATE (p5:Plant {
    name: "Santalum album L.",
    family: "SANTALACEAE",
    common_name: "Safed chandan, Sandal",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000013362&column=szBarcode"
})
CREATE (u30:Usage {name: "Expectorant"})
CREATE (p5)-[:USED_FOR {part: "wood"}]->(u25)
CREATE (p5)-[:USED_FOR {part: "wood"}]->(u26)
CREATE (p5)-[:USED_FOR {part: "wood"}]->(u30)
CREATE (p5)-[:USED_FOR {part: "oil"}]->(u25)
CREATE (p5)-[:USED_FOR {part: "oil"}]->(u26)
CREATE (p5)-[:USED_FOR {part: "oil"}]->(u30)

// Terminalia chebula
CREATE (p6:Plant {
    name: "Terminalia chebula (Gaertn.) Retz.",
    family: "COMBRETACEAE",
    common_name: "Harre",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000009564&column=szBarcode"
})
CREATE (u31:Usage {name: "Laxative"})
CREATE (u32:Usage {name: "Constituent of Triphala"})
CREATE (p6)-[:USED_FOR {part: "fruit"}]->(u31)
CREATE (p6)-[:USED_FOR {part: "fruit"}]->(u19)
CREATE (p6)-[:USED_FOR {part: "fruit"}]->(u32)

// Trichosanthes dioica
CREATE (p7:Plant {
    name: "Trichosanthes dioica Roxb.",
    family: "CUCURBITACEAE",
    common_name: "Parwal",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000009419&column=szBarcode"
})
CREATE (u33:Usage {name: "Suitable for convalescents"})
CREATE (u34:Usage {name: "Helps control cancer-like conditions"})
CREATE (p7)-[:USED_FOR {part: "fruit"}]->(u31)
CREATE (p7)-[:USED_FOR {part: "fruit"}]->(u33)
CREATE (p7)-[:USED_FOR {part: "fruit"}]->(u34)

// Vetiveria zizanioides
CREATE (p8:Plant {
    name: "Vetiveria zizanioides (L.) Roberty",
    family: "POACEAE",
    common_name: "Khasa, Bena",
    link: "https://archive.bsi.gov.in/echoHerbarium-Details/en?link=CAL0000003170&column=szBarcode"
})
CREATE (u35:Usage {name: "Stimulant"})
CREATE (u36:Usage {name: "Colic"})
CREATE (u37:Usage {name: "Flatulence"})
CREATE (u38:Usage {name: "Obstinate vomiting"})
CREATE (u39:Usage {name: "Rheumatism"})
CREATE (u40:Usage {name: "Lumbago"})
CREATE (u41:Usage {name: "Sprains"})
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u26)
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u35)
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u36)
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u37)
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u38)
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u39)
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u40)
CREATE (p8)-[:USED_FOR {part: "oil"}]->(u41)
