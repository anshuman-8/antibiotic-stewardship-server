from django.db import models
from .choice import *
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True)
    isStaff = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Patient(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    fullName = models.CharField(max_length=100, verbose_name="Full Name")
    dateOfBirth = models.CharField(max_length=100, default=None)
    mrdNumber = models.CharField(max_length=100)
    dateofAdmission = models.CharField(max_length=100)
    patientLocation = models.CharField(
        max_length=100, choices=PATIENT_LOCATION, default=""
    )
    # department=models.CharField(max_length=100, choices=DEPARTMENT, default="Select")
    department = models.CharField(max_length=100)
    admittingDoctor = models.CharField(max_length=100)
    diagnostic = models.CharField(max_length=100)
    cormorbodities = models.CharField(max_length=100)
    height = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=100, blank=True)
    lastReviewDate = models.DateField(default=None, blank=True, null=True)
    lastAnalysisDate = models.DateField(default=None, blank=True, null=True)
    # gender = models.CharField(max_length=10, choices=PATIENT_GENDER, default=None)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullName + "-" + self.mrdNumber
    
    @property
    def hasDraft(self):
        return self.patientform_set.filter(draft=True).exists()
    


class AnalysisForm(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    doctor = models.CharField(max_length=100, default=None)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patientForm = models.ForeignKey("PatientForm", on_delete=models.CASCADE)
    drugAdministered = models.ForeignKey(
        "DrugAdministeredReview", blank=True, on_delete=models.CASCADE
    )
    patientOutcome = models.ForeignKey(
        "PatientOutcome", blank=True, on_delete=models.CASCADE
    )
    compliance = models.ForeignKey("Compliance", blank=True, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(
        "Recommendation", blank=True, on_delete=models.CASCADE
    )
    draft = models.BooleanField(default=False)


class PatientForm(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    isAnalyzed = models.BooleanField(default=False)
    # date = models.DateTimeField(auto_now_add=True)
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
    # clinical_signs = models.ForeignKey(
    #     "ClinicalSign", blank=True, on_delete=models.CASCADE
    # )
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.fullName


class Sepsis(models.Model):
    # id = models.AutoField(primary_key=True)
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
        # data = self.organism
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
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
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
    # id = models.AutoField(primary_key=True)
    antibiotic = models.CharField(
        max_length=100, choices=ANTIBIOTIC_CHOICES, default="Select"
    )

    def __str__(self):
        return self.antibiotic


class DrugAdministeredReview(models.Model):
    isRightDocumentation = models.BooleanField(default=False)
    isRightDrug = models.BooleanField(default=False)
    isRightDose = models.BooleanField(default=False)
    isRightRoute = models.BooleanField(default=False)
    isRightFrequency = models.BooleanField(default=False)
    isRightDuration = models.BooleanField(default=False)
    isRightIndication = models.BooleanField(default=False)
    isAppropriate = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.score


class PatientOutcome(models.Model):
    lenght_of_stay = models.IntegerField()
    date_of_discharge = models.CharField(max_length=100)
    outcome = models.CharField(
        max_length=100, choices=PATIENT_OUTCOME, default="Select"
    )

    def __str__(self):
        outcome = {"Outcome": self.outcome, "LOS": self.lenght_of_stay}
        return outcome


class Compliance(models.Model):
    # id = models.AutoField(primary_key=True)
    serum_creatinine = models.IntegerField(default=None)
    # procalcitonin = models.IntegerField
    isAppropriate = models.BooleanField(default=False)
    isRightDocumentation = models.BooleanField(default=False)
    isRecommendationFiled = models.BooleanField(default=True)
    isAntibioticChanged = models.BooleanField(default=False)
    isComplance = models.BooleanField(default=False)
    isDuration = models.BooleanField(default=False)
    isAntibiotisDoseChanged = models.BooleanField(default=False)

    def __str__(self):
        return self.serum_creatinine


class Recommendation(models.Model):
    indication = models.CharField(max_length=100, default=None)
    drug = models.CharField(max_length=100, default=None)
    dose = models.CharField(max_length=100, default=None)
    frequency = models.CharField(max_length=100, default=None)
    duration = models.CharField(max_length=100, default=None)
    deEscalation = models.CharField(max_length=100, default=None)
    isindication = models.BooleanField()
    isdrug = models.BooleanField(default=False)
    isdose = models.BooleanField(default=False)
    isfrequency = models.BooleanField(default=False)
    isduration = models.BooleanField(default=False)
    isdeEscalation = models.BooleanField(default=False)

    def __str__(self):
        return self.indication
