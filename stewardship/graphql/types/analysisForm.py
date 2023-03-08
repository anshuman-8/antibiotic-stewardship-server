import graphene
from stewardship.graphql.types.patient import PatientObj
from stewardship.graphql.types.patientDataForm import PatientDataFormObj
from stewardship.models import (
    Patient,
    AnalysisForm,
    DrugAdministeredReview,
    PatientOutcome,
    Compliance,
    Recommendation,
)


class DrugAdministeredReviewObj(
    graphene.ObjectType, description="Drug Administered object"
):
    id = graphene.ID()
    isRightDocumentation = graphene.Boolean()
    isRightDrug = graphene.Boolean()
    isRightDose = graphene.Boolean()
    isRightRoute = graphene.Boolean()
    isRightFrequency = graphene.Boolean()
    isRightDuration = graphene.Boolean()
    isRightIndication = graphene.Boolean()
    isAppropriate = graphene.Boolean()
    score = graphene.Int()


class PatientOutcomeObj(graphene.ObjectType, description="Patient Outcome object"):
    id = graphene.ID()
    lenght_of_stay = graphene.Int()
    date_of_discharge = graphene.String()
    outcome = graphene.String()


class ComplianceObj(graphene.ObjectType, description="Compliance object"):
    id = graphene.ID()
    serum_creatinine = graphene.Int()
    # procalcitonin = graphene.Int()
    isAppropriate = graphene.Boolean()
    isRightDocumentation = graphene.Boolean()
    isRecommendationFiled = graphene.Boolean()
    isAntibioticChanged = graphene.Boolean()
    isComplance = graphene.Boolean()
    isDuration = graphene.Boolean()
    isAntibiotisDoseChanged = graphene.Boolean()


class RecommendationObj(
    graphene.ObjectType, description="Doctor's recommendation object"
):
    id = graphene.ID()
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


# Main AnalysisForm object


class AnalysisFormObj(graphene.ObjectType, description="the AnalysisForm object"):
    id = graphene.ID()
    date = graphene.String()
    doctor = graphene.String()
    patient = graphene.Field(lambda: PatientObj)
    patientForm = graphene.Field(lambda: PatientDataFormObj)
    drugAdministered = graphene.Field(lambda: DrugAdministeredReviewObj)
    patientOutcome = graphene.Field(lambda: PatientOutcomeObj)
    compliance = graphene.Field(lambda: ComplianceObj)
    recommendation = graphene.Field(lambda: RecommendationObj)

    # def resolve_patient(self, info):
    #     return Patient.objects.get(id=self.patient_id)
