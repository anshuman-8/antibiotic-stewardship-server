import graphene
from stewardship.models import User


class UserBasicObj(graphene.ObjectType, description="the User object"):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    userType = graphene.String()

    def resolve_id(self, info):
        if isinstance(self, User):
            return self.id

    # def resolve_username(self, info):
    #     if isinstance(self, User):
    #         return self.username

    def resolve_userType(self, info):
        if isinstance(self, User):
            type = ""
            if self.isAdmin:
                type = "Admin"
            elif self.isStaff:
                type = "Staff"
            return type
