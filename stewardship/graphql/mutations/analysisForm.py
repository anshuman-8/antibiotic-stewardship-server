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
        id = graphene.ID(required=True, description="ID of the analysis form to edit")
        inputs = graphene.Argument(
            AnalysisFormInput,
            required=True,
            description="Updated inputs for the analysis form",
        )

    success = graphene.Boolean()
    updated_analysis = graphene.Field(AnalysisFormObj)

    @staticmethod
    def mutate(self, info, id, inputs):
        try:
            analysis_form = AnalysisForm.objects.get(id=id)
        except AnalysisForm.DoesNotExist:
            raise APIException(message="Analysis form not found", code=400)
        print(inputs)
        try:
            analysis_form.doctor = inputs.doctor

            drugAdministeredRevObj = analysis_form.drugAdministered
            drugAdministeredRevObj.isRightDocumentation = validate_boolean(
                inputs.drugAdministeredReview.isRightDocumentation,
            )
            drugAdministeredRevObj.isRightDrug = validate_boolean(
                inputs.drugAdministeredReview.isRightDrug,
            )
            drugAdministeredRevObj.isRightDose = validate_boolean(
                inputs.drugAdministeredReview.isRightDose,
            )
            drugAdministeredRevObj.isRightRoute = validate_boolean(
                inputs.drugAdministeredReview.isRightRoute,
            )
            drugAdministeredRevObj.isRightFrequency = validate_boolean(
                inputs.drugAdministeredReview.isRightFrequency,
            )
            drugAdministeredRevObj.isRightDuration = validate_boolean(
                inputs.drugAdministeredReview.isRightDuration,
            )
            drugAdministeredRevObj.isRightIndication = validate_boolean(
                inputs.drugAdministeredReview.isRightIndication,
            )
            drugAdministeredRevObj.isAppropriate = validate_boolean(
                inputs.drugAdministeredReview.isAppropriate,
            )
            drugAdministeredRevObj.score = (inputs.drugAdministeredReview.score)

            patientOutcomeObj = analysis_form.patientOutcome
            patientOutcomeObj.length_of_stay = (inputs.patientOutcome.length_of_stay)
            patientOutcomeObj.date_of_discharge = (
                inputs.patientOutcome.date_of_discharge,
            )
            patientOutcomeObj.outcome = (inputs.patientOutcome.outcome)

            recommendationObj = analysis_form.recommendation
            recommendationObj.indication = (inputs.recommendation.indication)
            recommendationObj.drug = (inputs.recommendation.drug)
            recommendationObj.dose = (inputs.recommendation.dose)
            recommendationObj.frequency = (inputs.recommendation.frequency)
            recommendationObj.duration = (inputs.recommendation.duration)
            recommendationObj.deEscalation = (inputs.recommendation.deEscalation)
            recommendationObj.isindication = validate_boolean(
                inputs.recommendation.isindication,
            )
            recommendationObj.isdrug = validate_boolean(
                inputs.recommendation.isdrug,
            )
            recommendationObj.isdose = validate_boolean(
                inputs.recommendation.isdose,
            )
            recommendationObj.isfrequency = validate_boolean(
                inputs.recommendation.isfrequency,
            )
            recommendationObj.isduration = validate_boolean(
                inputs.recommendation.isduration,
            )
            recommendationObj.isdeEscalation = validate_boolean(
                inputs.recommendation.isdeEscalation,
            )

            complianceObj = analysis_form.compliance
            complianceObj.serum_creatinine = (inputs.compliance.serum_creatinine)
            complianceObj.isAppropriate = validate_boolean(
                inputs.compliance.isAppropriate,
            )
            complianceObj.isRightDocumentation = validate_boolean(
                inputs.compliance.isRightDocumentation,
            )
            complianceObj.isRecommendationFiled = validate_boolean(
                inputs.compliance.isRecommendationFiled,
            )
            complianceObj.isAntibioticDoseChanged = validate_boolean(
                inputs.compliance.isAntibioticDoseChanged,
            )
            complianceObj.isComplance = validate_boolean(
                inputs.compliance.isComplance,
            )
            complianceObj.isAntibioticChanged = validate_boolean(
                inputs.compliance.isAntibioticChanged,
            )
            complianceObj.isDuration = validate_boolean(
                inputs.compliance.isDuration,
            )
            complianceObj.comments = (inputs.compliance.comments)

            drugAdministeredRevObj.save()
            patientOutcomeObj.save()
            recommendationObj.save()
            complianceObj.save()

            analysis_form.save()
        except Exception as e:
            raise APIException(message=e, code=400)

        return AnalysisFormResponse(success=True, returning=analysis_form)

    Output = AnalysisFormResponse


def validate_boolean(value):
    print(value)
    if value:
        return True
    else:
        return False
