import graphene
from stewardship.models import Patient
from stewardship.graphql.types import PatientObj
from stewardship.graphql.inputs import PatientCreateInput
from main.api.API_Exceptions import APIException


class PatientRegisterResponse(graphene.ObjectType):
    success = graphene.Boolean()
    returning = graphene.Field(PatientObj)


class RegisterPatient(graphene.Mutation, description="Register a patient"):
    class Arguments:
        inputs = graphene.Argument(
            PatientCreateInput,
            required=True,
            description="inputs available for creation",
        )

    def mutate(self, info, inputs: PatientCreateInput):
        patient = Patient.objects.create(
            fullName=inputs.fullName,
            dateOfBirth=inputs.dateOfBirth,
            mrdNumber=inputs.mrdNumber,
            dateofAdmission=inputs.dateOfAdmission,
            patientLocation=inputs.patientLocation,
            department=inputs.department,
            admittingDoctor=inputs.admittingDoctor,
            diagnostic=inputs.diagnostic,
            cormorbodities=inputs.cormorbodities,
            height=inputs.height,
            weight=inputs.weight,
            # gender=inputs.gender,
            active=True,
        )
        patient.save()
        return PatientRegisterResponse(success=True, returning=patient)

    Output = PatientRegisterResponse


class DischargePatient(graphene.Mutation, description="Discharge a patient"):
    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        patient = Patient.objects.get(id=id)
        patient.active = False
        patient.save()
        return True

    Output = graphene.Boolean()


class Mutation(graphene.ObjectType):
    createUser = RegisterPatient.Field()
    dischargePatient = DischargePatient.Field()
