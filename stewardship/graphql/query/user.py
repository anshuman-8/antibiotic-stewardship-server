import graphene
from stewardship.models import User
from stewardship.graphql.types.user import UserBasicObj


class UserQuery(graphene.ObjectType):
    users = graphene.List(UserBasicObj)
    user = graphene.Field(UserBasicObj, id=graphene.ID())

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        try:
            id = kwargs.get("id")
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return User.objects.none()
