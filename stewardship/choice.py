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
        "CRE (Carbapenem resistant enterobactereciae)",
        "CRE (Carbapenem resistant enterobactereciae)",
    ),
    (
        "CRAB (Carbapenem resistant acenetobacter)",
        "CRAB (Carbapenem resistant acenetobacter)",
    ),
    (
        "ESBL (Extended spectrum Beta lactamase)",
        "ESBL (Extended spectrum Beta lactamase)",
    ),
    (
        "MRSA (Methicillin resistant Staph Aureus)",
        "MRSA (Methicillin resistant Staph Aureus)",
    ),
    (
        "VRE (Vancomycin resistant Enterococcus)",
        "VRE (Vancomycin resistant Enterococcus)",
    ),
    ("Col Re( Colistin resistant)", "Col Re (colistin Resistant)"),
    ("NA", "NA"),
]

DIAGNOSIS_CHOICES = [
    ("probable", "probable"),
    ("definite", "definite"),
    ("NONE", "NONE"),
]

PATIENT_GENDER = [("Male", "Male"), ("Female", "Female"), ("Others", "Others")]

PATIENT_LOCATION = [("ICU", "ICU"), ("WARD", "WARD"), ("NONE", "NONE")]

PATIENT_OUTCOME = [("DEAD", "DEAD"), ("ALIVE", "ALIVE")]
