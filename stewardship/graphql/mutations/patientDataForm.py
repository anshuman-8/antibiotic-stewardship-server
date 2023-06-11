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
        print("\n\nPatient Data Form :   ",inputs)
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
            isCatheterLinesStents=inputs.focusOfInfection.isCatheterLinesStents,
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
                    antibiotic=antibiotics,
                )
                antibioticSensitivityList.append(antibioticSensitivity)

            culture_report = CultureReport.objects.create(
                time_sent=culture_report_input.timeSent,
                time_reported=culture_report_input.timeReported,
                sentBeforeAntibiotic=culture_report_input.sentBeforeAntibiotic,
                multi_drug_resistant=culture_report_input.multiDrugResistance,
                specimen_type=culture_report_input.specimenType,
                site_of_collection=culture_report_input.siteOfCollection,
                organism=culture_report_input.organism,
                resistance = culture_report_input.resistance,
                Imaging=imaging,
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

        clinical_signsList = []
        for clinical_signs_input in inputs.clinicalSign:
            clinical_signs = ClinicalSign.objects.create(
                date=clinical_signs_input.date,
                patient=patientObject,
                procalcitonin=clinical_signs_input.procalcitonin,
                white_blood_cell=clinical_signs_input.whiteBloodCell,
                neutrophil=clinical_signs_input.neutrophil,
                s_creatinine=clinical_signs_input.sCreatinine,
                cratinine_clearance=clinical_signs_input.cratinineClearance,
                o2_saturation=clinical_signs_input.o2Saturation,
                blood_pressure=clinical_signs_input.bloodPressure,
                temperature=clinical_signs_input.temperature,
            )
            clinical_signsList.append(clinical_signs)

        try:
            patientForm = PatientForm.objects.create(
                patient=patientObject,
                review_date=inputs.reviewDate,
                review_department=inputs.reviewDepartment,
                provisional_diagnosis=inputs.provisionalDiagnosis,
                final_diagnosis=inputs.finalDiagnosis,
                syndromic_diagnosis=inputs.syndromicDiagnosis,
                diagnosis_choice=inputs.diagnosisChoice,
                focus_of_infection=focusOfInfection,
                sepsis=sepsis,
                isculture_report=True,
                draft = inputs.draft
            )
            patientForm.culture_report.set(culture_reports)
            patientForm.antibiotic_used.set(antibiotics_used)

        except Exception as e:
            print("Error: ", e)
            raise APIException(message=e, code=400)
        print(inputs.draft)
        if inputs.draft == False:
            patientObject.lastReviewDate = inputs.reviewDate
            patientObject.save()

        if PatientForm.objects.filter(patient=inputs.patient, draft=True).exists():
            form = PatientForm.objects.get(patient=inputs.patient, draft=True)
            form.delete()
                
        patientForm.save()

        return PatientFormResponse(success=True, returning=patientForm)

    Output = PatientFormResponse


class Mutation(graphene.ObjectType):
    patientDataForm = PatientDataForm.Field()
