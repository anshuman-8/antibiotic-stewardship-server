from django.db import models
from .choice import *

class Patient(models.Model):
    fullName = models.CharField(max_length=100)
    dob=models.DateField()
    mrdNumber=models.CharField(max_length=100)
    dateofAdmission=models.DateField()
    patientLocation=models.CharField(max_length=100, choices=PATIENT_LOCATION, default="Select")
    # department=models.CharField(max_length=100, choices=DEPARTMENT, default="Select")
    department=models.CharField(max_length=100)
    admittingDoctor=models.CharField(max_length=100)
    diagnostic=models.CharField(max_length=100)
    cormorbodities=models.CharField(max_length=100)
    height=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)


class AnalysisForm(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patientForm = models.ForeignKey("PatientForm", on_delete=models.CASCADE)
    drugAdministered = models.ManyToManyField("DrugAdministered", blank=True)
    patientOutcome = models.ManyToManyField("PatientOutcome", blank=True)
    compliance = models.ManyToManyField("Compliance", blank=True)
    recommendation = models.ManyToManyField("Recommendation", blank=True)


class PatientForm(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    review_date=models.DateField()
    review_department=models.CharField(max_length=100)
    provisional_diagnosis=models.CharField(max_length=200)
    final_diagnosis=models.CharField(max_length=200)
    syndromic_diagnosis=models.CharField(max_length=200)
    diagnosis_choice=models.CharField(max_length=100, choices=DIAGNOSIS_CHOICES, default="Select")
    sepsis=models.ManyToManyField("Sepsis", blank=True)
    focus_of_infection=models.ManyToManyField("FocusOfInfection", blank=True)
    cultureReport=models.BooleanField()
    culture_report=models.ManyToManyField("CultureReport", blank=True)
    antibiotic_used=models.ManyToManyField("Antibiotic", blank=True)
    clinical_signs=models.ManyToManyField("ClinicalSign", blank=True)
    
    def __str__(self):
        return self.patient.fullName


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
    isxRay=models.BooleanField(default=False)
    isUltraSound=models.BooleanField(default=False)
    isCTScan=models.BooleanField(default=False)
    isMRI=models.BooleanField(default=False)
    isPETScan=models.BooleanField(default=False)
    impression = models.CharField(max_length=100, default="")

    
    def __str__(self):
        return self.impression

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
        data = {"Date":self.date}
        return data

class AntibioticSensitivity(models.Model):
    name = models.CharField(max_length=100, choices=ANTIBIOTIC_CHOICES, default="Select")
    
    def __str__(self):
        return self.name

class DrugAdministered(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class PatientOutcome(models.Model):
    lenght_of_stay=models.IntegerField()
    date_of_discharge=models.DateField()
    outcome = models.CharField(max_length=100, choices=PATIENT_OUTCOME, default="Select")
    
    def __str__(self):
        outcome = {"Outcome":self.outcome, "LOS":self.lenght_of_stay}
        return outcome

class Compliance(models.Model):
    serum_creatinine=models.IntegerField
    procalcitonin=models.IntegerField
    # compliance_choice=models.CharField(max_length=100)
    isAppropriate=models.BooleanField(default=False)
    isRightDocumentation=models.BooleanField(default=False)
    isRecommendationFiled=models.BooleanField(default=True)
    isAntibioticChanged=models.BooleanField(default=False)
    isComplance=models.BooleanField(default=False)
    isDuration=models.BooleanField(default=False)
    isAntibioticDoseChanged=models.BooleanField(default=False)

    def __str__(self):
        return self.serum_creatinine


class Recommendation(models.Model):
    indication=models.CharField(max_length=100,default=None)
    drug=models.CharField(max_length=100,default=None)
    dose=models.CharField(max_length=100,default=None)
    frequency=models.CharField(max_length=100,default=None)
    duration=models.CharField(max_length=100,default=None)
    deEscalation=models.CharField(max_length=100,default=None)
    isindication=models.BooleanField()
    isdrug=models.BooleanField(default=False)
    isdose=models.BooleanField(default=False)    
    isfrequency=models.BooleanField(default=False)
    isduration=models.BooleanField(default=False)
    isdeEscalation=models.BooleanField(default=False)

    
    def __str__(self):
        return self.indication