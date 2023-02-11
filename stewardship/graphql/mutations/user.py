import graphene
from stewardship.models import User
from stewardship.graphql.types import UserBasicObj
from stewardship.graphql.inputs import UserCreateInput
from main.api.API_Exceptions import APIException


class UserCreationResponse(graphene.ObjectType):
    success = graphene.Boolean()
    returning = graphene.Field(UserBasicObj)


class CreateUser(graphene.Mutation, description="Create a user"):
    class Arguments:
        inputs = graphene.Argument(
            UserCreateInput, required=True, description="inputs available for creation"
        )

    def mutate(self, info, inputs: UserCreateInput):
        user = User.objects.create(
            username=inputs.username,
            email=inputs.email,
            isStaff=inputs.isStaff,
            isAdmin=inputs.isAdmin,
            # first_name=inputs.firstName,
            # last_name=inputs.lastName,
        )
        user.set_password(inputs.password)
        user.save()
        return UserCreationResponse(success=True, returning=user)

    
    Output = UserCreationResponse


