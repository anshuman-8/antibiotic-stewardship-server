import graphene
from graphene_django import DjangoObjectType
from stewardship.models import Patient


class ImagingInput(graphene.InputObjectType):
    isxRay = graphene.Boolean()
    isUltraSound = graphene.Boolean()
    isCTScan = graphene.Boolean()
    isMRI = graphene.Boolean()
    isPETScan = graphene.Boolean()
    impression = graphene.String()


class AntibioticSensitivityInput(graphene.InputObjectType):
    name = graphene.String()


class CultureReportInput(graphene.InputObjectType):
    timeSent = graphene.String()
    timeReported = graphene.String()
    sentBeforeAntibiotic = graphene.Boolean()
    specimenType = graphene.String()
    siteOfCollection = graphene.String()
    organism = graphene.String()
    antibioticSensitivity = graphene.List(AntibioticSensitivityInput)
    multiDrugResistant = graphene.String()
    resistance = graphene.String()
    Imaging = graphene.Field(ImagingInput)


class SepesisInput(graphene.InputObjectType):
    isSepsis = graphene.Boolean()
    isSepticShock = graphene.Boolean()
    isNeutropenicSepsis = graphene.Boolean()


class FocusOfInfectionInput(graphene.InputObjectType):
    isUTI = graphene.Boolean()
    isCNS = graphene.Boolean()
    isPneumonia = graphene.Boolean()
    isSkin = graphene.Boolean()
    isAbdominal = graphene.Boolean()
    isPrimaryBacteraemia = graphene.Boolean()
    isSecondaryBacteraemia = graphene.Boolean()
    other = graphene.String()


class AntibioticInput(graphene.InputObjectType):
    initialDate = graphene.String()
    antibiotic = graphene.String()
    loadingDose = graphene.Int()
    maintenanceDose = graphene.Int()
    route = graphene.String()
    frequency = graphene.Int()
    duration = graphene.Int()
    endDate = graphene.String()


class ClinicalSignInput(graphene.InputObjectType):
    date = graphene.String()
    procalcitonin = graphene.String()
    whiteBloodCell = graphene.String()
    neutrophil = graphene.String()
    sCreatinine = graphene.String()
    cratinineClearance = graphene.String()
    temperature = graphene.String()
    bloodPressure = graphene.String()
    o2Saturation = graphene.String()


class PatientFormInput(graphene.InputObjectType):
    patient = graphene.ID()
    reviewDate = graphene.String()
    reviewDepartment = graphene.String()
    provisionalDiagnosis = graphene.String()
    finalDiagnosis = graphene.String()
    syndromicDiagnosis = graphene.String()
    diagnosisChoice = graphene.String()
    sepsis = graphene.Field(SepesisInput)
    focusOfInfection = graphene.Field(FocusOfInfectionInput)
    cultureReport = graphene.List(CultureReportInput)
    antibioticUsed = graphene.List(AntibioticInput)
    clinicalSign = graphene.Field(ClinicalSignInput)
