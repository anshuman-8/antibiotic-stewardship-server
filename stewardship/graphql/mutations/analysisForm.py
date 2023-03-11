import graphene
from stewardship.models import (
    AnalysisForm,
    Patient,
    Compliance,
    DrugAdministeredReview,
    PatientOutcome,
    Recommendation,
    PatientForm,
)
from stewardship.graphql.types import AnalysisFormObj
from stewardship.graphql.inputs import AnalysisFormInput
from main.api.API_Exceptions import APIException


class AnalysisFormResponse(graphene.ObjectType):
    success = graphene.Boolean()
    returning = graphene.Field(AnalysisFormObj)


class AnalysisDataForm(
    graphene.Mutation, description="Patient review data analysis form"
):
    class Arguments:
        inputs = graphene.Argument(
            AnalysisFormInput,
            required=True,
            description="inputs available for creation",
        )

    @staticmethod
    def mutate(self, info, inputs: AnalysisFormInput):
        print(inputs)
        patientObject = Patient.objects.get(id=inputs.patient)
        patientFormObject = PatientForm.objects.get(id=inputs.patientForm)

        drugAdministeredReview = DrugAdministeredReview.objects.create(
            isRightDocumentation=inputs.drugAdministeredReview.isRightDocumentation,
            isRightDrug=inputs.drugAdministeredReview.isRightDrug,
            isRightDose=inputs.drugAdministeredReview.isRightDose,
            isRightRoute=inputs.drugAdministeredReview.isRightRoute,
            isRightFrequency=inputs.drugAdministeredReview.isRightFrequency,
            isRightDuration=inputs.drugAdministeredReview.isRightDuration,
            isRightIndication=inputs.drugAdministeredReview.isRightIndication,
            isAppropriate = inputs.drugAdministeredReview.isAppropriate,
            score=inputs.drugAdministeredReview.score,
        )

        patientOutcome = PatientOutcome.objects.create(
            lenght_of_stay=inputs.patientOutcome.lenght_of_stay,
            date_of_discharge=inputs.patientOutcome.date_of_discharge,
            outcome=inputs.patientOutcome.outcome,
        )
        
        recommendation = Recommendation.objects.create(
            indication=inputs.recommendation.indication,
            drug=inputs.recommendation.drug,
            dose=inputs.recommendation.dose,
            frequency=inputs.recommendation.frequency,
            duration=inputs.recommendation.duration,
            deEscalation=inputs.recommendation.deEscalation,
            isindication=inputs.recommendation.isindication,
            isdrug=inputs.recommendation.isdrug,
            isdose=inputs.recommendation.isdose,
            isfrequency=inputs.recommendation.isfrequency,
            isduration=inputs.recommendation.isduration,
            isdeEscalation=inputs.recommendation.isdeEscalation
        )

        compliance = Compliance.objects.create(
            serum_creatinine=inputs.compliance.serum_creatinine,
            # procalcitonin=inputs.compliance.procalcitonin,
            isAppropriate=inputs.compliance.isAppropriate,
            isRightDocumentation=inputs.compliance.isRightDocumentation,
            isRecommendationFiled=inputs.compliance.isRecommendationFiled,
            isAntibiotisDoseChanged=inputs.compliance.isAntibiotisDoseChanged,
            isComplance=inputs.compliance.isComplance,
            # duration = inputs.compliance.duration
        )

        try:
            analysisForm = AnalysisForm.objects.create(
                doctor = inputs.doctor,
                patient=patientObject,
                patientForm=patientFormObject,
                compliance=compliance,
                drugAdministered=drugAdministeredReview,
                patientOutcome=patientOutcome,
                recommendation=recommendation,
            )

        except Exception as e:
            raise APIException(message=e, code=400)

        analysisForm.save()
        patientFormObject.isAnalyzed=True
        patientFormObject.save()
        
        return AnalysisFormResponse(success=True, returning=analysisForm)

    Output = AnalysisFormResponse


class Mutation(graphene.ObjectType):
    patientDataForm = AnalysisDataForm.Field()
