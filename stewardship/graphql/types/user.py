import graphene
from stewardship.models import User


class UserBasicObj(graphene.ObjectType, description="the User object"):
    id = graphene.ID()
    userName = graphene.String()
    mrdNumber = graphene.String()

    def resolve_id(self, info):
        if isinstance(self, User):
            return self.id

    def resolve_username(self, info):
        if isinstance(self, User):
            return self.username

    def resolve_userType(self, info):
        if isinstance(self, User):
            type = ""
            if self.is_patient:
                type = "Patient"
            elif self.is_doctor:
                type = "Doctor"
            elif self.is_nurse:
                type = "Nurse"
            elif self.is_admin:
                type = "Admin"
            return type
