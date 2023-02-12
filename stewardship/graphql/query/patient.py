import graphene
from stewardship.models import Patient
from stewardship.graphql.types.patient import PatientObj


class PatientQuery(graphene.ObjectType):
    patients = graphene.List(PatientObj)
    patient = graphene.Field(PatientObj, id=graphene.ID())

    def resolve_patients(self, info):
        return Patient.objects.all()

    def resolve_patient(self, info, **kwargs):
        id = kwargs.get("id")
        return Patient.objects.get(id=id)
