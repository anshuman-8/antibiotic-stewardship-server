import graphene
from stewardship.models import (
    Sepsis,
    Patient,
    FocusOfInfection,
    CultureReport,
    ClinicalSign,
    AntibioticSensitivity,
    Antibiotic,
    Imaging,
    PatientForm,
)
from stewardship.graphql.types import PatientDataFormObj
from stewardship.graphql.inputs import PatientFormInput
from main.api.API_Exceptions import APIException


class PatientFormResponse(graphene.ObjectType):
    success = graphene.Boolean()
    returning = graphene.Field(PatientDataFormObj)


class PatientDataForm(graphene.Mutation, description="Patient Daily data form"):
    class Arguments:
        inputs = graphene.Argument(
            PatientFormInput,
            required=True,
            description="inputs available for creation",
        )

    @staticmethod
    def mutate(self, info, inputs: PatientFormInput):
        patientObject = Patient.objects.get(id=inputs.patient)

        sepsis = Sepsis.objects.create(
            isSepsis=inputs.sepsis.isSepsis,
            isSepticShock=inputs.sepsis.isSepticShock,
            isNeutropenicSepsis=inputs.sepsis.isNeutropenicSepsis,
        )

        focusOfInfection = FocusOfInfection.objects.create(
            isUTI=inputs.focusOfInfection.isUTI,
            isCNS=inputs.focusOfInfection.isCNS,
            isPneumonia=inputs.focusOfInfection.isPneumonia,
            isSkin=inputs.focusOfInfection.isSkin,
            isAbdominal=inputs.focusOfInfection.isAbdominal,
            isPrimaryBacteraemia=inputs.focusOfInfection.isPrimaryBacteraemia,
            isSecondaryBacteraemia=inputs.focusOfInfection.isSecondaryBacteraemia,
            other=inputs.focusOfInfection.other,
        )

        culture_reports = []
        for culture_report_input in inputs.cultureReport:
            imaging = Imaging.objects.create(
                isxRay=culture_report_input.Imaging.isxRay,
                isCTScan=culture_report_input.Imaging.isCTScan,
                isMRI=culture_report_input.Imaging.isMRI,
                isUltraSound=culture_report_input.Imaging.isUltraSound,
                isPETScan=culture_report_input.Imaging.isPETScan,
                impression=culture_report_input.Imaging.impression,
            )
            antibioticSensitivityList = []
            for antibiotics in culture_report_input.antibioticSensitivity:
                antibioticSensitivity = AntibioticSensitivity.objects.create(
                    name=antibiotics,
                )
                antibioticSensitivityList.append(antibioticSensitivity)

            culture_report = CultureReport.objects.create(
                time_sent=culture_report_input.timeSent,
                time_reported=culture_report_input.timeReported,
                sentBeforeAntibiotic=culture_report_input.sentBeforeAntibiotic,
                Imaging=imaging,
                # antibiotic_sensitivity=antibioticSensitivityList
            )
            culture_report.antibiotic_sensitivity.set(antibioticSensitivityList)
            culture_reports.append(culture_report)

        antibiotics_used = []
        for antibiotic_used_input in inputs.antibioticUsed:
            antibiotic_used = Antibiotic.objects.create(
                initial_date=antibiotic_used_input.initialDate,
                antibiotic=antibiotic_used_input.antibiotic,
                loading_dose=antibiotic_used_input.loadingDose,
                maintenance_dose=antibiotic_used_input.maintenanceDose,
                route=antibiotic_used_input.route,
                frequency=antibiotic_used_input.frequency,
                duration=antibiotic_used_input.duration,
                end_date=antibiotic_used_input.endDate,
            )
            antibiotics_used.append(antibiotic_used)

        clinical_signs = ClinicalSign.objects.create(
            date=inputs.clinicalSign.date,
            procalcitonin=inputs.clinicalSign.procalcitonin,
            white_blood_cell=inputs.clinicalSign.whiteBloodCell,
            neutrophil=inputs.clinicalSign.neutrophil,
            s_creatinine=inputs.clinicalSign.sCreatinine,
            cratinine_clearance=inputs.clinicalSign.cratinineClearance,
            o2_saturation=inputs.clinicalSign.o2Saturation,
            blood_pressure=inputs.clinicalSign.bloodPressure,
            temperature=inputs.clinicalSign.temperature,
        )

        try:
            patientForm = PatientForm.objects.create(
                patient=patientObject,
                focus_of_infection=focusOfInfection,
                sepsis=sepsis,
                clinical_signs=clinical_signs,
                cultureReport =True
            )
            patientForm.culture_report.set(culture_reports)
            patientForm.antibiotic_used.set(antibiotics_used)
            print("Alert reached",patientForm)

        except Exception as e:
            print("Error: ", e)
            raise APIException(message=e, code=400)

        patientForm.save()
        return PatientFormResponse(success=True, returning=patientForm)

    Output = PatientFormResponse


class Mutation(graphene.ObjectType):
    patientDataForm = PatientDataForm.Field()
