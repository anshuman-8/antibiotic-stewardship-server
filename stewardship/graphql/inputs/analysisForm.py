import graphene
from graphene_django import DjangoObjectType
from stewardship.models import Patient, AnalysisForm


class DrugAdministeredReviewInput(
    graphene.InputObjectType, description="Drug Administered Input"
):
    isRightDocumentation = graphene.Boolean()
    isRightDrug = graphene.Boolean()
    isRightDose = graphene.Boolean()
    isRightRoute = graphene.Boolean()
    isRightFrequency = graphene.Boolean()
    isRightDuration = graphene.Boolean()
    isRightIndication = graphene.Boolean()
    isAppropriate = graphene.Boolean()
    score = graphene.Int()


class PatientOutcomeInput(
    graphene.InputObjectType, description="Patient Outcome Input"
):
    length_of_stay = graphene.Int()
    date_of_discharge = graphene.String()
    outcome = graphene.String()


class ComplianceInput(graphene.InputObjectType, description="Compliance Input"):
    serum_creatinine = graphene.Int()
    # duration = graphene.Int(),
    # procalcitonin = graphene.Int()
    isAppropriate = graphene.Boolean()
    isRightDocumentation = graphene.Boolean()
    isRecommendationFiled = graphene.Boolean()
    isAntibioticChanged = graphene.Boolean()
    isComplance = graphene.Boolean()
    isDuration = graphene.Boolean()
    isAntibioticDoseChanged = graphene.Boolean()
    comments = graphene.String()


class RecommendationInput(
    graphene.InputObjectType, description="Doctor's recommendation input"
):
    indication = graphene.String()
    drug = graphene.String()
    dose = graphene.String()
    frequency = graphene.String()
    duration = graphene.String()
    deEscalation = graphene.String()
    isindication = graphene.Boolean()
    isdrug = graphene.Boolean()
    isdose = graphene.Boolean()
    isfrequency = graphene.Boolean()
    isduration = graphene.Boolean()
    isdeEscalation = graphene.Boolean()


class AnalysisFormInput(graphene.InputObjectType):
    # date = graphene.String()
    doctor = graphene.String()
    patient = graphene.ID()
    patientForm = graphene.ID()
    drugAdministeredReview = graphene.Field(DrugAdministeredReviewInput)
    patientOutcome = graphene.Field(PatientOutcomeInput)
    compliance = graphene.Field(ComplianceInput)
    recommendation = graphene.Field(RecommendationInput)
    # draft = graphene.Boolean()
