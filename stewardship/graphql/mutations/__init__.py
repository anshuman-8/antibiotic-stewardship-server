import graphene
from .user import CreateUser
from .patient import RegisterPatient, DischargePatient
from .patientDataForm import PatientDataForm
from .analysisForm import AnalysisDataForm, EditAnalysisForm
from .generateCSV import GenerateCSV


class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()
    RegisterPatient = RegisterPatient.Field()
    patientDataForm = PatientDataForm.Field()
    analysisDataForm = AnalysisDataForm.Field()
    editAnalysisDataForm = EditAnalysisForm.Field()
    dischargePatient = DischargePatient.Field()
    generateCSV = GenerateCSV.Field()

