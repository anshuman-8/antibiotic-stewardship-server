from django.db import models
from stewardship.choice import *


class AnalysisForm(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    doctor = models.CharField(max_length=100, default=None)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
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
    length_of_stay = models.IntegerField()
    date_of_discharge = models.CharField(max_length=100)
    outcome = models.CharField(
        max_length=100, choices=PATIENT_OUTCOME, default="Select"
    )

    def __str__(self):
        # outcome = {"Outcome": self.outcome, "LOS": self.length_of_stay}
        return self.outcome+" - Duration-"+self.length_of_stay+"Days"


class Compliance(models.Model):
    serum_creatinine = models.IntegerField(default=None)
    isAppropriate = models.BooleanField(default=False)
    isRightDocumentation = models.BooleanField(default=False)
    isRecommendationFiled = models.BooleanField(default=True)
    isAntibioticChanged = models.BooleanField(default=False)
    isComplance = models.BooleanField(default=False)
    isDuration = models.BooleanField(default=False)
    isAntibioticDoseChanged = models.BooleanField(default=False)
    comments = models.CharField(max_length=100, blank=True, null=True)

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