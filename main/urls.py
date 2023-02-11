from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include
from stewardship.urls import *
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from graphene_django.views import GraphQLView

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
