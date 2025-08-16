Broken data row (#8 returned)
=============================
### Raw data
```
CHEMBL404,TAZOBACTAM,Not available,"infection; Pseudomonas infection; pancreatic carcinoma; abscess; osteomyelitis; pneumonia; Otitis media; septic shock; bacterial pneumonia; Cholecystitis, Acute; diabetic foot; Sepsis; urinary tract infection; infectious disease; ventilator-associated pneumonia; bacterial disease; kidney disease; pyelonephritis; Enterobacteriaceae Infections; graft versus host disease; hematopoietic and lymphoid cell neoplasm; influenza; COVID-19",Not available,Not available,Not available,Not available,Not available,Not available,Not available
```

### Broken into columns (each row is 1 column):
```
CHEMBL404,
TAZOBACTAM,
Not available,
infection; Pseudomonas infection; pancreatic carcinoma; abscess; osteomyelitis; pneumonia; Otitis media; septic shock; bacterial pneumonia; Cholecystitis, Acute; diabetic foot; Sepsis; urinary tract infection; infectious disease; ventilator-associated pneumonia; bacterial disease; kidney disease; pyelonephritis; Enterobacteriaceae Infections; graft versus host disease; hematopoietic and lymphoid cell neoplasm; influenza; COVID-19,
Not available,
Not available,
Not available,
Not available,
Not available,
Not available,
Not available
```

Note that row #4 has a common in it: "Cholecystitis, Acute". This breaks the csv.

-----------------------------------------------------------------------------

Working data row
================
Raw:
```
CHEMBL19,METHAZOLAMIDE,Not available,altitude sickness; cervical cancer; open-angle glaucoma; glaucoma,Not available,Not available,Carbonic anhydrase IV; Carbonic anhydrase VII; Carbonic anhydrase I; Carbonic anhydrase II,SINGLE PROTEIN,Carbonic anhydrase I inhibitor; Carbonic anhydrase VII inhibitor; Carbonic anhydrase IV inhibitor; Carbonic anhydrase II inhibitor,Not available,Not available
```

Broken into columns:
```
CHEMBL19,
METHAZOLAMIDE,
Not available,
altitude sickness; cervical cancer; open-angle glaucoma; glaucoma,
Not available,
Not available,
Carbonic anhydrase IV; Carbonic anhydrase VII; Carbonic anhydrase I; Carbonic anhydrase II,
SINGLE PROTEIN,
Carbonic anhydrase I inhibitor; Carbonic anhydrase VII inhibitor; Carbonic anhydrase IV inhibitor; Carbonic anhydrase II inhibitor,
Not available,
Not available
```
