from django.contrib import admin

from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ( 'fullName', 'mrdNumber',"dateofAdmission")

class AnalysisFormAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'date',"patientForm")

class PatientFormAdmin(admin.ModelAdmin):
    list_display = ( 'patient', 'review_date',"review_department")

admin.site.register(Patient, PatientAdmin)

admin.site.register(AnalysisForm,AnalysisFormAdmin)

admin.site.register(Recommendation)

admin.site.register(PatientForm)

admin.site.register(Sepsis)

admin.site.register(FocusOfInfection)

admin.site.register(CultureReport)

admin.site.register(Imaging)

admin.site.register(Antibiotic)

admin.site.register(ClinicalSign)

admin.site.register(AntibioticSensitivity)

admin.site.register(DrugAdministered)

admin.site.register(PatientOutcome)

admin.site.register(Compliance)


