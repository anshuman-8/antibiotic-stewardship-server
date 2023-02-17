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

    def mutate(self, info, inputs: PatientFormInput):
        # print("Form inputs: ", inputs)

        patientObject = Patient.objects.get(id=inputs.patient)

        patientForm = PatientForm.objects.create(

            patient=patientObject,
            sepsis=Sepsis.objects.create(
                isSepsis=inputs.sepsis.isSepsis,
                isSepticShock=inputs.sepsis.isSepticShock,
                isNeutropenicSepsis=inputs.sepsis.isNeutropenicSepsis,
            ),
            focusOfInfection=FocusOfInfection.objects.create(
                isUTI=inputs.focusOfInfection.isUTI,
                isCNS=inputs.focusOfInfection.isCNS,
                isPneumonia=inputs.focusOfInfection.isPneumonia,
                isSkin=inputs.focusOfInfection.isSkin,
                isAbdominal=inputs.focusOfInfection.isAbdominal,
                isPrimaryBacteraemia=inputs.focusOfInfection.isPrimaryBacteraemia,
                isSecondaryBacteraemia=inputs.focusOfInfection.isSecondaryBacteraemia,
                other=inputs.focusOfInfection.other,
            ),
        )

        culture_reports = []
        for culture_report_input in inputs.cultureReport:
            print(culture_report_input.Imaging)
            imaging = Imaging.objects.create(
                isxRay=culture_report_input.Imaging.isxRay,
                isCTScan=culture_report_input.Imaging.isCTScan,
                isMRI=culture_report_input.Imaging.isMRI,
                isUltraSound=culture_report_input.Imaging.isUltraSound,
                isPETScan=culture_report_input.Imaging.isPETScan,
                impression=culture_report_input.Imaging.impression,
            )
            culture_report = CultureReport.objects.create(
                time_sent=culture_report_input.timeSent,
                time_reported=culture_report_input.timeReported,
                sentBeforeAntibiotic=culture_report_input.sentBeforeAntibiotic,
                Imaging=imaging,
            )
            culture_reports.append(culture_report)

        antibiotics_used = []
        for antibiotic_used_input in inputs.antibioticUsed:
            antibiotic_used = Antibiotic.objects.create(
                initial_date=antibiotic_used_input.initialDate,
                antibiotic=antibiotic_used_input.antibiotic,
                loading_dose=antibiotic_used_input.loading_dose,
                maintenance_dose=antibiotic_used_input.maintenance_dose,
                route=antibiotic_used_input.route,
                frequency=antibiotic_used_input.frequency,
                duration=antibiotic_used_input.duration,
                end_date=antibiotic_used_input.end_date,
            )
            antibiotics_used.append(antibiotic_used)

        clinical_signsList = []
        for clinical_sign_input in inputs.clinicalSign:
            clinical_signs = ClinicalSign.objects.create(
                initial_date=clinical_sign_input.initial_date,
                clinicalSign=clinical_sign_input.clinicalSign,
                end_date=clinical_sign_input.end_date,
            )
            clinical_signsList.append(clinical_signs)


        patientForm.antibiotic_used.set(antibiotics_used)
        patientForm.clinical_signs.set(clinical_signsList)
        patientForm.culture_report.set(culture_reports)
        
        patientForm.save()
        return PatientFormResponse(success=True, returning=patientForm)

    Output = PatientFormResponse


class Mutation(graphene.ObjectType):
    patientDataForm = PatientDataForm.Field()
