import graphene
from graphene_django import DjangoObjectType
from stewardship.models import Patient


class PatientCreateInput(graphene.InputObjectType):
    fullName = graphene.String(required=True)
    mrdNumber = graphene.String(required=True)
    dateOfBirth = graphene.String(required=True)
    dateOfAdmission = graphene.String(required=True)
    # patient location is enum between ward or icu
    patientLocation =  graphene.String(required=True)
    department = graphene.String(required=True)
    admittingDoctor = graphene.String(required=True)
    diagnostic = graphene.String(required=True)
    cormorbodities = graphene.String(required=True)
    height = graphene.Int()
    weight = graphene.Int()
    # patientLocation = graphene.String()

