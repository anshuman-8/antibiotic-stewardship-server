import graphene
from .user import CreateUser
from .patient import RegisterPatient, DischargePatient
from .patientDataForm import PatientDataForm
from .analysisForm import AnalysisDataForm


class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()
    RegisterPatient = RegisterPatient.Field()
    patientDataForm = PatientDataForm.Field()
    analysisDataForm = AnalysisDataForm.Field()
    dischargePatient = DischargePatient.Field()
