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
            isAppropriate=inputs.drugAdministeredReview.isAppropriate,
            score=inputs.drugAdministeredReview.score,
        )

        patientOutcome = PatientOutcome.objects.create(
            length_of_stay=inputs.patientOutcome.length_of_stay,
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
            isdeEscalation=inputs.recommendation.isdeEscalation,
        )

        compliance = Compliance.objects.create(
            serum_creatinine=inputs.compliance.serum_creatinine,
            isAppropriate=inputs.compliance.isAppropriate,
            isRightDocumentation=inputs.compliance.isRightDocumentation,
            isRecommendationFiled=inputs.compliance.isRecommendationFiled,
            isAntibioticDoseChanged=inputs.compliance.isAntibioticDoseChanged,
            isComplance=inputs.compliance.isComplance,
            isAntibioticChanged=inputs.compliance.isAntibioticChanged,
            isDuration=inputs.compliance.isDuration,
            comments=inputs.compliance.comments,
        )

        try:
            analysisForm = AnalysisForm.objects.create(
                doctor=inputs.doctor,
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
        patientFormObject.isAnalyzed = True
        patientFormObject.save()

        return AnalysisFormResponse(success=True, returning=analysisForm)

    Output = AnalysisFormResponse



class EditAnalysisForm(graphene.Mutation):
    class Arguments:
        analysis_id = graphene.ID(required=True, description="ID of the analysis form to edit")
        inputs = graphene.Argument(AnalysisFormInput, required=True, description="Updated inputs for the analysis form")

    success = graphene.Boolean()
    updated_analysis = graphene.Field(AnalysisFormObj)

    @staticmethod
    def mutate(self, info, id, inputs):
        try:
            analysis_form = AnalysisForm.objects.get(id=id)
        except AnalysisForm.DoesNotExist:
            raise APIException(message="Analysis form not found", code=400)

        drugAdministeredReview = DrugAdministeredReview.objects.create(
            isRightDocumentation=inputs.drugAdministeredReview.isRightDocumentation,
            isRightDrug=inputs.drugAdministeredReview.isRightDrug,
            isRightDose=inputs.drugAdministeredReview.isRightDose,
            isRightRoute=inputs.drugAdministeredReview.isRightRoute,
            isRightFrequency=inputs.drugAdministeredReview.isRightFrequency,
            isRightDuration=inputs.drugAdministeredReview.isRightDuration,
            isRightIndication=inputs.drugAdministeredReview.isRightIndication,
            isAppropriate=inputs.drugAdministeredReview.isAppropriate,
            score=inputs.drugAdministeredReview.score,
        )

        patientOutcome = PatientOutcome.objects.create(
            length_of_stay=inputs.patientOutcome.length_of_stay,
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
            isdeEscalation=inputs.recommendation.isdeEscalation,
        )

        compliance = Compliance.objects.create(
            serum_creatinine=inputs.compliance.serum_creatinine,
            isAppropriate=inputs.compliance.isAppropriate,
            isRightDocumentation=inputs.compliance.isRightDocumentation,
            isRecommendationFiled=inputs.compliance.isRecommendationFiled,
            isAntibioticDoseChanged=inputs.compliance.isAntibioticDoseChanged,
            isComplance=inputs.compliance.isComplance,
            isAntibioticChanged=inputs.compliance.isAntibioticChanged,
            isDuration=inputs.compliance.isDuration,
            comments=inputs.compliance.comments,
        )

        try:
            analysis_form.doctor=inputs.doctor,
            # patient=patientObject,
            # patientForm=patientFormObject,
            analysis_form.compliance=compliance,
            analysis_form.drugAdministered=drugAdministeredReview,
            analysis_form.patientOutcome=patientOutcome,
            analysis_form.recommendation=recommendation,

        except Exception as e:
            raise APIException(message=e, code=400)

        # Save the updated analysis form
        analysis_form.save()

        return AnalysisFormResponse(success=True, returning=analysis_form)

    Output = AnalysisFormResponse


class Mutation(graphene.ObjectType):
    patientDataForm = AnalysisDataForm.Field()
