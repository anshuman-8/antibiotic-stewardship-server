import graphene
from stewardship.models import User
from stewardship.graphql.types.user import UserBasicObj

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserBasicObj)
    user = graphene.Field(UserBasicObj, id=graphene.ID())
    id = graphene.ID()
    firstName = graphene.String()
    lastName = graphene.String()
    email = graphene.String()

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        return User.objects.get(id=id)

    def resolve_firstName(self, info):
        if isinstance(self, User):
            return self.first_name

    def resolve_lastName(self, info):
        if isinstance(self, User):
            return self.last_name

    def resolve_email(self, info):
        if isinstance(self, User):
            return self.email
