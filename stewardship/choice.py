SPECIMEN_CHOICES = [
    ("blood", "blood"),
    ("urine", "urine"),
    ("sputum", "sputum"),
    ("CSF", "CSF"),
    ("Wound", "Wound"),
    ("Pus", "Pus"),
    ("Bal", "Bal"),
    ("Stool", "Stool"),
    ("Mini Bal", "Mini Bal"),
    ("Aseptic Fluid", "Aseptic Fluid"),
    ("Pleural Fluid", "Pleural Fluid"),
    ("TISSUE", "TISSUE"),
]

# Antibiotic Sensitivity Choices
ANTIBIOTIC_CHOICES = [
    ("Ampicillin", "Ampicillin"),
    ("Amoxicillin/Clavulanic", "Amoxicillin/Clavulanic"),
    ("Gentamicin", "Gentamicin"),
    ("Co-trimoxazole", "Co-trimoxazole"),
    ("Ciprofloxacin", "Ciprofloxacin"),
    ("Cloxacillin", "Cloxacillin"),
    ("Cefixime", "Cefixime"),
    ("Tetracycline", "Tetracycline"),
    ("Levofloxacin", "Levofloxacin"),
    ("Doxycycline", "Doxycycline"),
    ("Norfloxacin", "Norfloxacin"),
    ("Penicillin", "Penicillin"),
    ("Erythromycin", "Erythromycin"),
    ("Linezolid", "Linezolid"),
    ("Vancomycin", "Vancomycin"),
    ("Imipenem", "Imipenem"),
    ("Moxifloxacin", "Moxifloxacin"),
    ("Ceftriaxone", "Ceftriaxone"),
]

# Multi Drug Resistant Choices
MDR_CHOICES = [
    ("MDR", "MDR"),
    ("Non MDR", "Non MDR"),
    ("PS(Pan sensitive)", "PS(Pan sensitive)"),
    ("NA(No organism)", "NA(No organism)"),
]

# Resistance Choices
RESISTANCE_CHOICES = [
    (
        "CRE( Carbapenemase resistant enterobactereciae)",
        "CRE( Carbapenemase resistant enterobactereciae)",
    ),
    (
        "ESBL(Extended spectrum beta lactamase)",
        "ESBL(Extended spectrum beta lactamase)",
    ),
    (
        "MRSA(Methicillin resistant staphylococcus aureus)",
        "MRSA(Methicillin resistant staphylococcus aureus)",
    ),
    (
        "VRE(Vancomycin resistant enterococcus)",
        "VRE(Vancomycin resistant enterococcus)",
    ),
    (
        "CRAB( Carbapenem resistant acinetobacter baumannii)",
        "CRAB( Carbapenem resistant acinetobacter baumannii)",
    ),
    ("Col Re( Colistin resistant)", "Col Re( Colistin resistant)"),
    ("NA-None of the above", "NA-None of the above"),
]

DIAGNOSIS_CHOICES = [
    ("probable", "probable"),
    ("definite", "definite"),
    ("NONE", "NONE"),
]

PATIENT_LOCATION = [("ICU", "ICU"), ("WARD", "WARD"), ("NONE", "NONE")]

PATIENT_OUTCOME = [("DEAD", "DEAD"), ("ALIVE", "ALIVE")]

PATIENT_OUTCOME = [("DEAD", "DEAD"), ("ALIVE", "ALIVE")]