import graphene
from stewardship.models import User
from stewardship.graphql.types import UserBasicObj
from stewardship.graphql.inputs import UserCreateInput
from main.api.API_Exceptions import APIException


class UserCreationResponse(graphene.ObjectType):
    success = graphene.Boolean()
    returning = graphene.Field(UserBasicObj)


class CreateUser(graphene.Mutation, description="create a user"):
    class Arguments:
        inputs = graphene.Argument(
            UserCreateInput, required=True, description="inputs available for creation"
        )
        password = graphene.String(required=True)
        username = graphene.String(required=True)

    Output = UserCreationResponse

    @staticmethod
    def mutate(self, info, inputs: UserCreateInput, password, username):
        user = User.objects.create(
            username=username, email=inputs.email, is_active=True
        )


import graphene
from stewardship.models import User
from stewardship.graphql.inputs import UserCreateInput
from stewardship.graphql.types import UserBasicObj


class UserCreationResponse(graphene.ObjectType):
    success = graphene.Boolean()
    returning = graphene.Field(UserBasicObj)


class CreateUser(graphene.Mutation, description="create a user"):
    class Arguments:
        inputs = graphene.Argument(
            UserCreateInput, required=True, description="inputs available for creation"
        )
        password = graphene.String(required=True)
        username = graphene.String(required=True)

    Output = UserCreationResponse

    def mutate(self, info, inputs: UserCreateInput, password, username):
        user = User.objects.create(
            username=input.username,
            email=input.email,
            first_name=input.firstName,
            last_name=input.lastName,
        )
        user.set_password(input.password)
        user.save()
        return UserCreationResponse(success=True, returning=user)

        user.set_password(password)
        user.bio = inputs.bio
        EmailAddress.objects.create(user=user, user_email=inputs.email, is_primary=True)
        user.save()
        return UserCreationResponse(success=True, returning=user)


class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()
