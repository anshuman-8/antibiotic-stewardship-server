from django.db import models
from .choice import *
# Create your models here.

class Stewardship(models.Model):
    name = models.CharField(max_length=100)
    review_date=models.DateField()
    review_department=models.CharField(max_length=100)
    provisional_diagnosis=models.CharField(max_length=200)
    final_diagnosis=models.CharField(max_length=200)
    syndromic_diagnosis=models.CharField(max_length=200)
    surity=models.CharField(max_length=100, choices=SURITY_CHOICES, default="Select")
    sepsis=models.ManyToManyField("Sepsis", blank=True)
    focus_of_infection=models.ManyToManyField("FocusOfInfection", blank=True)
    cultureReport=models.BooleanField()
    culture_report=models.ManyToManyField("CultureReport", blank=True)
    antibiotic_used=models.ManyToManyField("Antibiotic", blank=True)
    clinical_signs=models.ManyToManyField("ClinicalSign", blank=True)
    def __str__(self):
        return self.name

class Sepsis(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class FocusOfInfection(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CultureReport(models.Model):
    time_sent=models.DateTimeField()
    time_reported=models.DateTimeField()
    specimen_type=models.CharField(max_length=100, choices=SPECIMEN_CHOICES, default="Select")
    site_of_collection=models.CharField(max_length=100)
    organism=models.CharField(max_length=100)
    antibiotic_sensitivity=models.ManyToManyField("AntibioticSensitivity", blank=True)
    multi_drug_resistant=models.CharField(max_length=100, choices=MDR_CHOICES, default="Select")
    resistance=models.CharField(max_length=100, choices=RESISTANCE_CHOICES, default="Select")
    Imaging=models.ManyToManyField("Imaging", blank=True)
    impression=models.CharField(max_length=100)
    def __str__(self):
        return self.specimen_type

class Imaging(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Antibiotic(models.Model):
    initial_date=models.DateField()
    antibiotic=models.CharField(max_length=100)
    loading_dose=models.IntegerField()
    maintenance_dose=models.IntegerField()
    route=models.CharField(max_length=100)
    frequency=models.IntegerField()
    duration=models.IntegerField()
    end_date=models.DateField()
    def __str__(self):
        return self.antibiotic

class ClinicalSign(models.Model):
    date=models.DateField()
    procalcitonin=models.CharField(max_length=100)
    white_blood_cell=models.CharField(max_length=100)
    neutrophil=models.CharField(max_length=100)
    s_creatinine=models.CharField(max_length=100)
    cratinine_clearance=models.CharField(max_length=100)
    temperature=models.CharField(max_length=100)
    blood_pressure=models.CharField(max_length=100)
    o2_saturation=models.CharField(max_length=100)
    def __str__(self):
        return self.procalcitonin

    def __str__(self):
        return self.white_blood_cell
    
    def __str__(self):
        return self.neutrophil
    
    def __str__(self):
        return self.s_creatinine

class AntibioticSensitivity(models.Model):
    name = models.CharField(max_length=100, choices=ANTIBIOTIC_CHOICES, default="Select")
    
    def __str__(self):
        return self.name