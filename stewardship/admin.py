from django.contrib import admin

from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = ("fullName", "mrdNumber", "dateofAdmission")
    search_fields = ("fullName", "mrdNumber", "dateofAdmission")


class AnalysisFormAdmin(admin.ModelAdmin):
    list_display = ("patient", "date", "patientForm")


class PatientFormAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "patient",
        "review_date"
    )
    search_fields = ("patient", "review_date", "review_department", "provisional_diagnosis")


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "isAdmin",
        "isStaff",
    )
    list_filter = ("isStaff", "isAdmin")
    search_fields = ("username", "email")


admin.site.register(User, UserAdmin)

admin.site.register(Patient, PatientAdmin)

admin.site.register(AnalysisForm, AnalysisFormAdmin)

admin.site.register(PatientForm, PatientFormAdmin)

admin.site.register(Recommendation)

admin.site.register(Sepsis)

admin.site.register(FocusOfInfection)

admin.site.register(CultureReport)

admin.site.register(Imaging)

admin.site.register(Antibiotic)

admin.site.register(ClinicalSign)

admin.site.register(AntibioticSensitivity)

admin.site.register(DrugAdministeredReview)

admin.site.register(PatientOutcome)

admin.site.register(Compliance)
