import graphene
from graphene_django import DjangoObjectType
from stewardship.models import User


class UserCreateInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    firstName = graphene.String(required=True)
    lastName = graphene.String(required=True)
