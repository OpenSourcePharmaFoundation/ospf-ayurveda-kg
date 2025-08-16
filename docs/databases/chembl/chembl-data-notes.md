What data to grab from ChemBL
=============================
Make requests to /chembl/api/data/drug/

1. Drug name
  - Make FDA name the default

2. ATC classification (what is does?)
   - Division of active substances into different groups according to:
    - The organ or system on which they act
    - Their therapeutic, pharmacological and chemical properties.
  - Drugs are classified in groups at five different levels.
     - The code contains the level
        - e.g. C02CA01
          - C                 02    C         A     01
            /\                /\    /\        /\    /\
          Cardiovascular      ||    ||        ||    ||
                              ||    ||        ||    ||
            Therapeutic subgroup    ||        ||    ||
                                    ||        ||    ||
              Pharmacological subgroup        ||    ||
                                              ||    ||
                               Chemical subgroup    ||
                                                    ||
                                    Chemical substance
  - https://www.who.int/tools/atc-ddd-toolkit/atc-classification

3. Black box warning, if present
   - Find a way to grab this

4. Chirality

5. Indication class

6. Max phase


Think about these
- Do we need to grab black box warnings if present?

No need to gather
- Applicants
- availability_type
- Is there a black box warning?
- first_approval
- first_in_class



Definitions
- ATC: Anatomical Therapeutic Chemical
