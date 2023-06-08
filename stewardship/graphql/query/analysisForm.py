import graphene
from stewardship.models import Patient, AnalysisForm, PatientForm
from stewardship.graphql.types.analysisForm import AnalysisFormObj


class AnalysisFormQuery(graphene.ObjectType):
    analysisForms = graphene.List(AnalysisFormObj)
    analysisForm = graphene.Field(AnalysisFormObj, id=graphene.ID())
    patientAnalysisForms = graphene.List(
        AnalysisFormObj, patientId=graphene.ID(required=True)
    )

    def resolve_analysisForms(self, info):
        return AnalysisForm.objects.all()

    def resolve_analysisForm(self, info, **kwargs):
        id = kwargs.get("id")
        return AnalysisForm.objects.get(id=id)

    def resolve_patientAnalysisForms(self, info, **kwargs):
        patientId = kwargs.get("patientId")
        return AnalysisForm.objects.filter(patient=patientId)
