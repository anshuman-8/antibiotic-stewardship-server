from .user import UserQuery
from .patient import PatientQuery
from .patientDataForm import PatientDataFormQuery
from .analysisForm import AnalysisFormQuery

__all__ = [
    "UserQuery",
    "PatientQuery",
    "PatientDataFormQuery",
    "AnalysisFormQuery",
]

# class Query(graphene.ObjectType):
#     UserQuery
#     PatientQuery
#     PatientDataFormQuery
#     AnalysisFormQuery