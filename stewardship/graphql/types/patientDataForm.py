import graphene
from stewardship.graphql.types.patient import PatientObj
from stewardship.models import (
    Patient,
    Sepsis,
    FocusOfInfection,
    CultureReport,
    Antibiotic,
    ClinicalSign,
)


class SepsisObj(graphene.ObjectType, description="Sepsis object"):
    id = graphene.ID()
    isSepsis = graphene.Boolean()
    isSepticShock = graphene.Boolean()
    isNeutropenicSepsis = graphene.Boolean()


class FocusOfInfectionObj(graphene.ObjectType, description="Focus of Infection object"):
    id = graphene.ID()
    isUTI = graphene.Boolean()
    isCNS = graphene.Boolean()
    isPneumonia = graphene.Boolean()
    isSkin = graphene.Boolean()
    isAbdominal = graphene.Boolean()
    isPrimaryBacteraemia = graphene.Boolean()
    isSecondaryBacteraemia = graphene.Boolean()
    other = graphene.String()


class ImagingObj(graphene.ObjectType, description="Imaging object"):
    id = graphene.ID()
    isxRay = graphene.Boolean()
    isUltraSound = graphene.Boolean()
    isCTScan = graphene.Boolean()
    isMRI = graphene.Boolean()
    isPETScan = graphene.Boolean()
    impression = graphene.String()


class AntibioticSensitivityObj(
    graphene.ObjectType, description="Antibiotic Sensitivity object"
):
    id = graphene.ID()
    antibiotic = graphene.String()
    # sensitivity = graphene.String()


class CultureReportObj(graphene.ObjectType, description="Culture Report object"):
    id = graphene.ID()
    time_sent = graphene.String()
    time_reported = graphene.String()
    sentBeforeAntibiotic = graphene.Boolean()
    specimen_type = graphene.String()
    site_of_collection = graphene.String()
    organism = graphene.String()
    antibiotic_sensitivity = graphene.List(AntibioticSensitivityObj)
    multi_drug_resistant = graphene.String()
    resistance = graphene.String()
    Imaging = graphene.List(ImagingObj)


class AntibioticObj(graphene.ObjectType, description="Antibiotic object"):
    id = graphene.ID()
    initial_date = graphene.String()
    antibiotic = graphene.String()
    loading_dose = graphene.Int()
    maintenance_dose = graphene.Int()
    route = graphene.String()
    frequency = graphene.Int()
    duration = graphene.Int()
    end_date = graphene.String()


class ClinicalSignObj(graphene.ObjectType, description="Clinical Sign object"):
    id = graphene.ID()
    date = graphene.String()
    procalcitonin = graphene.String()
    white_blood_cell = graphene.String()
    neutrophil = graphene.String()
    s_creatinine = graphene.String()
    cratinine_clearance = graphene.String()
    temperature = graphene.String()
    blood_pressure = graphene.String()
    o2_saturation = graphene.String()


# Main PatientDataForm object


class PatientDataFormObj(graphene.ObjectType, description="the PatientDataForm object"):
    id = graphene.ID()
    patient = graphene.Field(lambda: PatientObj)
    review_date = graphene.String()
    review_department = graphene.String()
    provisional_diagnosis = graphene.String()
    final_diagnosis = graphene.String()
    syndromic_diagnosis = graphene.String()
    diagnosis_choice = graphene.String()
    sepsis = graphene.List(lambda: SepsisObj)
    focus_of_infection = graphene.List(lambda: FocusOfInfectionObj)
    culture_report = graphene.Boolean()
    culture_reports = graphene.List(lambda: CultureReportObj)
    antibiotics_used = graphene.List(lambda: AntibioticObj)
    clinical_signs = graphene.List(lambda: ClinicalSignObj)

    def resolve_diagnosis_choice(self, info):
        return self.diagnosis_choice

    def resolve_sepsis(self, info):
        return self.sepsis.all()

    def resolve_focus_of_infection(self, info):
        return self.focus_of_infection.all()

    def resolve_culture_report(self, info):
        return self.culture_report

    def resolve_culture_reports(self, info):
        return self.culture_report.all()

    def resolve_antibiotics_used(self, info):
        return self.antibiotic_used.all()

    def resolve_clinical_signs(self, info):
        return self.clinical_signs.all()
