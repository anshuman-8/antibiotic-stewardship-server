import graphene
from .user import CreateUser
from .patient import RegisterPatient
from .patientDataForm import PatientDataForm


class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()
    RegisterPatient = RegisterPatient.Field()
    patientDataForm = PatientDataForm.Field()
