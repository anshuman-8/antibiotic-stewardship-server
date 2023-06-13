from django.utils import timezone
import graphene
from stewardship.models import Patient, PatientForm
from stewardship.graphql.types import PatientObj, PatientDataFormObj


class PatientQuery(graphene.ObjectType):
    patients = graphene.List(PatientObj)
    patient = graphene.Field(PatientObj, id=graphene.ID())
    activePatients = graphene.List(PatientObj)
    todayPatientList = graphene.List(PatientObj)

    def resolve_patients(self, info):
        return Patient.objects.all()

    def resolve_patient(self, info, **kwargs):
        id = kwargs.get("id")
        return Patient.objects.get(id=id)

    def resolve_activePatients(self, info):
        return Patient.objects.filter(active=True)

    def resolve_todayPatientList(self, info):
        result = Patient.objects.filter(
            active=True, lastReviewDate__lt=timezone.datetime.now().date()
        )
        result2 = Patient.objects.filter(active=True, lastReviewDate__isnull=True)
        return result | result2
