from django.contrib import admin
from django.urls import path
from django.urls import include
from stewardship.urls import *
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('', include('stewardship.urls')),
]
