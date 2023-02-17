import graphene
from stewardship.models import PatientForm
from stewardship.graphql.types.patientDataForm import PatientDataFormObj


class PatientDataFormQuery(graphene.ObjectType):
    forms = graphene.List(PatientDataFormObj)
    form = graphene.Field(PatientDataFormObj, id=graphene.ID())

    def resolve_forms(self, info):
        return PatientForm.objects.all()

    def resolve_form(self, info, **kwargs):
        id = kwargs.get("id")
        return PatientForm.objects.get(id=id)
