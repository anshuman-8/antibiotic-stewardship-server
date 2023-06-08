import graphene
from stewardship.models import Patient


class PatientObj(graphene.ObjectType, description="the Patient object"):
    id = graphene.ID()
    fullName = graphene.String()
    mrdNumber = graphene.String()
    dateOfBirth = graphene.String()
    dateOfAdmission = graphene.String()
    patientLocation = graphene.String()
    department = graphene.String()
    admittingDoctor = graphene.String()
    diagnostic = graphene.String()
    lastReviewDate = graphene.String()
    lastAnalysisDate = graphene.String()
    cormorbodities = graphene.String()
    height = graphene.String()
    weight = graphene.String()
    # gender = graphene.String()
    active = graphene.Boolean()
    hasDraft = graphene.Boolean()
    # patientLocation = graphene.String()


    def resolve_dateOfBirth(self, info):
        if isinstance(self, Patient):
            # result = self.dob.strftime("%d-%m-%Y")
            return self.dateOfBirth
        

    def resolve_dateOfAdmission(self, info):
        if isinstance(self, Patient):
            # result = self.dateofAdmission.strftime("%d-%m-%Y")
            return self.dateofAdmission

    def resolve_username(self, info):
        if isinstance(self, Patient):
            return self.fullName
