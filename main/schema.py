import graphene
import graphql_jwt
from stewardship.graphql.query import UserQuery, PatientQuery
from stewardship.graphql.mutations import Mutations 


class Query(UserQuery,PatientQuery, graphene.ObjectType):
    pass


class Mutation(Mutations, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
