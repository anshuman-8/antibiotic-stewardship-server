from django.db import models
from choice import *


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
