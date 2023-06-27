import graphene
from stewardship.models import PatientForm, Patient, ClinicalSign
from stewardship.graphql.types.patientDataForm import (
    PatientDataFormObj,
    ClinicalSignObj,
)


class PatientDataFormQuery(graphene.ObjectType):
    patientForms = graphene.List(PatientDataFormObj)
    patientForm = graphene.Field(PatientDataFormObj, id=graphene.ID())
    patientsForm = graphene.List(
        PatientDataFormObj,
        patientId=graphene.ID(required=True),
        date=graphene.String(required=True),
    )
    allClinicalSigns = graphene.List(
        PatientDataFormObj,
        startDate=graphene.String(required=True),
        endDate=graphene.String(required=True),
    )
    formsForAnalysis = graphene.List(PatientDataFormObj)
    getClinicalSigns = graphene.List(
        ClinicalSignObj,
        patient=graphene.ID(required=True),
        startDate=graphene.String(required=True),
        endDate=graphene.String(required=True),
    )
    getDraftForms = graphene.List(PatientDataFormObj)

    def resolve_patientForms(self, info):
        return PatientForm.objects.all()

    def resolve_patientForm(self, info, **kwargs):
        id = kwargs.get("id")
        return PatientForm.objects.get(id=id)

    def resolve_patientsForm(self, info, **kwargs):
        patientId = kwargs.get("patientId")
        date = kwargs.get("date")
        return PatientForm.objects.filter(patient=patientId, review_date=date)

    def resolve_allClinicalSigns(self, info, **kwargs):
        startDate = kwargs.get("startDate")
        endDate = kwargs.get("endDate")
        return PatientForm.objects.filter(review_date__range=[startDate, endDate])

    def resolve_formsForAnalysis(self, info, **kwargs):
        try:
            return PatientForm.objects.filter(isAnalyzed=False, draft=False, patient__active=True)
        except Patient.DoesNotExist:
            return PatientForm.objects.none()

    def resolve_getClinicalSigns(self, info, **kwargs):
        patient = kwargs.get("patient")
        startDate = kwargs.get("startDate")
        endDate = kwargs.get("endDate")
        return ClinicalSign.objects.filter(
            patient=patient, date__range=[startDate, endDate]
        )

    def resolve_fetchDraftForms(self, info, **kwargs):
        patient = kwargs.get("patient")
        try:
            return PatientForm.objects.filter(
                draft=True, patient__id=patient, patient__active=True
            )
        except Patient.DoesNotExist:
            return PatientForm.objects.none()
        
