import graphene
from .user import UserBasicObj
from .patient import PatientObj
from .patientDataForm import PatientDataFormObj
from .analysisForm import AnalysisFormObj

# class ReportObj(graphene.ObjectType, description="Patient daily Object"):
#     id = graphene.ID()
#     lenght_of_stay = graphene.Int()
#     date_of_discharge = graphene.String()
#     outcome = graphene.String()

__all__ = ["UserBasicObj", "PatientObj", "PatientDataFormObj", "AnalysisFormObj"]
