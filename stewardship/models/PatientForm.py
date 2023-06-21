from django.db import models
from stewardship.choice import *


class PatientForm(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    isAnalyzed = models.BooleanField(default=False)
    review_date = models.CharField(max_length=100)
    review_department = models.CharField(max_length=100)
    provisional_diagnosis = models.CharField(max_length=200)
    final_diagnosis = models.CharField(max_length=200)
    syndromic_diagnosis = models.CharField(max_length=200)
    diagnosis_choice = models.CharField(
        max_length=100, choices=DIAGNOSIS_CHOICES, default="null"
    )
    sepsis = models.ForeignKey("Sepsis", blank=True, on_delete=models.CASCADE)
    focus_of_infection = models.ForeignKey(
        "FocusOfInfection",
        blank=True,
        on_delete=models.CASCADE,
    )
    isculture_report = models.BooleanField()
    culture_report = models.ManyToManyField("CultureReport", blank=True, default=[])
    antibiotic_used = models.ManyToManyField("Antibiotic", blank=True, default=[])
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.fullName

    @property
    def hasDraftAnalysis(self):
        return self.analysisform_set.filter(draft=True).exists()
    

class Sepsis(models.Model):
    isSepsis = models.BooleanField(default=False)
    isSepticShock = models.BooleanField(default=False)
    isNeutropenicSepsis = models.BooleanField(default=False)

    def __str__(self):
        return "sepsis"


class FocusOfInfection(models.Model):
    isUTI = models.BooleanField(default=False)
    isCNS = models.BooleanField(default=False)
    isPneumonia = models.BooleanField(default=False)
    isSkin = models.BooleanField(default=False)
    isAbdominal = models.BooleanField(default=False)
    isPrimaryBacteraemia = models.BooleanField(default=False)
    isSecondaryBacteraemia = models.BooleanField(default=False)
    isCatheterLinesStents = models.BooleanField(default=False)
    isCAI = models.BooleanField(default=False)
    isHAI = models.BooleanField(default=False)
    other = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.other


class CultureReport(models.Model):
    time_sent = models.CharField(max_length=100)
    time_reported = models.CharField(max_length=100)
    sentBeforeAntibiotic = models.BooleanField(default=False)
    specimen_type = models.CharField(
        max_length=100, choices=SPECIMEN_CHOICES, default=""
    )
    site_of_collection = models.CharField(max_length=100)
    organism = models.CharField(max_length=100)
    antibiotic_sensitivity = models.ManyToManyField(
        "AntibioticSensitivity", blank=True, default=[]
    )
    multi_drug_resistant = models.CharField(
        max_length=100, choices=MDR_CHOICES, default=""
    )
    resistance = models.CharField(
        max_length=100, choices=RESISTANCE_CHOICES, default=""
    )
    Imaging = models.ForeignKey("Imaging", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        data = self.organism + " " + self.specimen_type
        return data


class Imaging(models.Model):
    isxRay = models.BooleanField(default=False)
    isUltraSound = models.BooleanField(default=False)
    isCTScan = models.BooleanField(default=False)
    isMRI = models.BooleanField(default=False)
    isPETScan = models.BooleanField(default=False)
    impression = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.impression


class Antibiotic(models.Model):
    initial_date = models.CharField(max_length=100)
    antibiotic = models.CharField(max_length=100)
    loading_dose = models.IntegerField(null=True, blank=True)
    maintenance_dose = models.IntegerField(null=True, blank=True)
    route = models.CharField(max_length=100)
    frequency = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    end_date = models.CharField(max_length=100)

    def __str__(self):
        return self.antibiotic


class ClinicalSign(models.Model):
    date = models.CharField(max_length=100)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    procalcitonin = models.CharField(max_length=100)
    white_blood_cell = models.CharField(max_length=100)
    neutrophil = models.CharField(max_length=100)
    s_creatinine = models.CharField(max_length=100)
    cratinine_clearance = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    blood_pressure = models.CharField(max_length=100)
    o2_saturation = models.CharField(max_length=100)

    def __str__(self):
        return self.date


class AntibioticSensitivity(models.Model):
    antibiotic = models.CharField(
        max_length=100, choices=ANTIBIOTIC_CHOICES, default="Select"
    )

    def __str__(self):
        return self.antibiotic
