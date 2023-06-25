import graphene
import base64
import csv
from stewardship.models import (
    Patient,
    AnalysisForm,
    PatientForm,
)


def generate_csv_and_encode(patientId):

    patient_data = get_patient_details(patientId)
    csv_file_path = f'./reports/patient_{patientId}_details.csv'
    fieldnames = [
        'Patient ID', 'Full Name', 'Date of Birth', 'MRD Number', 'Date of Admission',
        'Patient Location', 'Department', 'Admitting Doctor', 'Diagnostic', 'Comorbidities',
        'Last Review Date', 'Last Analysis Date', 'Active',
        'Form ID', 'Is Analyzed', 'Review Date', 'Review Department', 'Provisional Diagnosis',
        'Final Diagnosis', 'Syndromic Diagnosis', 'Diagnosis Choice',
        'Culture Report', 'Antibiotic Used',
        'Analysis Form ID', 'Analysis Date', 'Doctor', 'Drug Administered', 'Patient Outcome',
        'Compliance', 'Recommendation'
    ]

    try: 
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            patientCSVObject = {
            'Patient ID': patient_data['patient']['id'],
            'Full Name': patient_data['patient']['fullName'],
            'Date of Birth': patient_data['patient']['dateOfBirth'],
            'MRD Number': patient_data['patient']['mrdNumber'],
            'Date of Admission': patient_data['patient']['dateofAdmission'],
            'Patient Location': patient_data['patient']['patientLocation'],
            'Department': patient_data['patient']['department'],
            'Admitting Doctor': patient_data['patient']['admittingDoctor'],
            'Diagnostic': patient_data['patient']['diagnostic'],
            'Comorbidities': patient_data['patient']['cormorbodities'],
            'Last Review Date': patient_data['patient']['lastReviewDate'],
            'Last Analysis Date': patient_data['patient']['lastAnalysisDate'],
            'Active': patient_data['patient']['active'],
        }
        
            for patient_form in patient_data['patientForms']:
                newRow=({
                    'Form ID': patient_form['id'],
                    'Is Analyzed': patient_form['isAnalyzed'],
                    'Review Date': patient_form['review_date'],
                    'Review Department': patient_form['review_department'],
                    'Provisional Diagnosis': patient_form['provisional_diagnosis'],
                    'Final Diagnosis': patient_form['final_diagnosis'],
                    'Syndromic Diagnosis': patient_form['syndromic_diagnosis'],
                    'Diagnosis Choice': patient_form['diagnosis_choice'],
                    'Culture Report': patient_form['culture_report'],
                    'Antibiotic Used': patient_form['antibiotic_used'],
                    'Analysis Form ID': patient_form['analysisForms'][0]['id'] if len(patient_form['analysisForms']) > 0 else (''),
                    'Analysis Date': patient_form['analysisForms'][0]['date'] if len(patient_form['analysisForms']) > 0 else (''),
                    'Doctor': patient_form['analysisForms'][0]['doctor'] if len(patient_form['analysisForms']) > 0 else (''),
                    'Drug Administered': patient_form['analysisForms'][0]['drugAdministered'] if len(patient_form['analysisForms']) > 0 else (''),
                    'Patient Outcome': patient_form['analysisForms'][0]['patientOutcome'] if len(patient_form['analysisForms']) > 0 else (''),
                    'Compliance': patient_form['analysisForms'][0]['compliance'] if len(patient_form['analysisForms']) > 0 else (''),
                    'Recommendation': patient_form['analysisForms'][0]['recommendation'] if len(patient_form['analysisForms']) > 0 else ('')
                })
                writer.writerow( patientCSVObject | newRow)

        with open(csv_file_path, 'rb') as file:
            encoded_csv = base64.b64encode(file.read()).decode('utf-8')

    except Exception as e:
        print("Error",e)
        encoded_csv = ''

    return encoded_csv

def get_patient_details(patient_id):
    patient = Patient.objects.get(id=patient_id) 
    patient_forms = PatientForm.objects.filter(patient=patient)
    response = {
        'patient': {
            'id': patient.id,
            'fullName': patient.fullName,
            'dateOfBirth': patient.dateOfBirth,
            'mrdNumber': patient.mrdNumber,
            'dateofAdmission': patient.dateofAdmission,
            'patientLocation': patient.patientLocation,
            'department': patient.department,
            'admittingDoctor': patient.admittingDoctor,
            'diagnostic': patient.diagnostic,
            'cormorbodities': patient.cormorbodities,
            'lastReviewDate': patient.lastReviewDate,
            'lastAnalysisDate': patient.lastAnalysisDate,
            'active': patient.active,
        },
        'patientForms': [],
    }
    # print("\n\n\nthe data::",len(patient_forms))
    i=0
    for patient_form in patient_forms:
        i+=1
        patient_form_data = {
            'id': patient_form.id,
            'isAnalyzed': patient_form.isAnalyzed,
            'review_date': patient_form.review_date,
            'review_department': patient_form.review_department,
            'provisional_diagnosis': patient_form.provisional_diagnosis,
            'final_diagnosis': patient_form.final_diagnosis,
            'syndromic_diagnosis': patient_form.syndromic_diagnosis,
            'diagnosis_choice': patient_form.diagnosis_choice,
            'culture_report': list(patient_form.culture_report.values()),
            'antibiotic_used': list(patient_form.antibiotic_used.values()),
            'analysisForms': [],
        }

        try:
            if(patient_form.isAnalyzed):
                analysis_forms = AnalysisForm.objects.filter(patientForm=patient_form)
                for analysis_form in analysis_forms:
                    compliance_data = {
                        'serum_creatinine': analysis_form.compliance.serum_creatinine,
                        'isAppropriate': analysis_form.compliance.isAppropriate,
                        'isRightDocumentation': analysis_form.compliance.isRightDocumentation,
                        'isRecommendationFiled': analysis_form.compliance.isRecommendationFiled,
                        'isAntibioticChanged': analysis_form.compliance.isAntibioticChanged,
                        # 'isCompliance': analysis_form.compliance.isCompliance,
                        'isDuration': analysis_form.compliance.isDuration,
                        'isAntibioticDoseChanged': analysis_form.compliance.isAntibioticDoseChanged,
                        'comments': analysis_form.compliance.comments,
                    }
                    patient_outcome_data = {
                        'length_of_stay': analysis_form.patientOutcome.length_of_stay,
                        'date_of_discharge': analysis_form.patientOutcome.date_of_discharge,
                        'outcome': analysis_form.patientOutcome.outcome,
                    }
                    drug_administered_data = {
                        'isRightDocumentation': analysis_form.drugAdministered.isRightDocumentation,
                        'isRightDrug': analysis_form.drugAdministered.isRightDrug,
                        'isRightDose': analysis_form.drugAdministered.isRightDose,
                        'isRightRoute': analysis_form.drugAdministered.isRightRoute,
                        'isRightFrequency': analysis_form.drugAdministered.isRightFrequency,
                        'isRightDuration': analysis_form.drugAdministered.isRightDuration,
                        'isRightIndication': analysis_form.drugAdministered.isRightIndication,
                        'isAppropriate': analysis_form.drugAdministered.isAppropriate,
                        'score': analysis_form.drugAdministered.score,
                    }
                    analysis_form_data = {
                        'id': analysis_form.id,
                        'date': analysis_form.date,
                        'doctor': analysis_form.doctor,
                        'recommendation': analysis_form.recommendation,
                        # 'drugAdministered': analysis_form.drugAdministered,
                        # 'patientOutcome': analysis_form.patientOutcome,
                        # 'compliance': analysis_form.compliance,
                    }
                    analysis_form_data['compliance'] = compliance_data
                    analysis_form_data['patientOutcome'] = patient_outcome_data
                    analysis_form_data['drugAdministered'] = drug_administered_data

                    patient_form_data['analysisForms'].append(analysis_form_data)
        except Exception as e:
            print("Error waala",e)

        response['patientForms'].append(patient_form_data)
    return response

class GenerateCSVOuput(graphene.ObjectType):
    encoded_csv = graphene.String()
    success = graphene.Boolean()

class GenerateCSV(graphene.Mutation):
    class Arguments:
        patientId = graphene.ID()


    @staticmethod
    def mutate(self, info, patientId ):
        encoded_csv = generate_csv_and_encode(patientId)
        if encoded_csv == '' or encoded_csv == None:
            return GenerateCSVOuput(encoded_csv='', success=False)
        return GenerateCSVOuput(encoded_csv=encoded_csv, success=True)
    
    Output = GenerateCSVOuput


class Mutation(graphene.ObjectType):
    generateCSV = GenerateCSV.Field()