import graphene
from stewardship.models import Patient, AnalysisForm, PatientForm
from stewardship.graphql.types.analysisForm import AnalysisFormObj


class AnalysisFormQuery(graphene.ObjectType):
    analysisForms = graphene.List(AnalysisFormObj)
    analysisForm = graphene.Field(AnalysisFormObj, id=graphene.ID())

    def resolve_analysisForms(self, info):
        return AnalysisForm.objects.all()

    def resolve_analysisForm(self, info, **kwargs):
        id = kwargs.get("id")
        return AnalysisForm.objects.get(id=id)
