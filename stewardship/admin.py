from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Stewardship)

admin.site.register(Sepsis)

admin.site.register(FocusOfInfection)

admin.site.register(CultureReport)

admin.site.register(Imaging)

admin.site.register(Antibiotic)

admin.site.register(ClinicalSign)

admin.site.register(AntibioticSensitivity)