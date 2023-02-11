import graphene
from .user import CreateUser
from .patient import RegisterPatient

class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()
    RegisterPatient = RegisterPatient.Field()
