"""datagouv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator

from rest_framework import permissions, routers

from datagouv.api.views import *


oa = openapi.Info(
    title="Data Gouv FR API: L'API Chimie des cours d'eau de Hub'Eau",
    description="Simplifier l'accès aux données sur l'eau",
    default_version='v1',
    terms_of_service="https://api.gouv.fr/les-api/api_hubeau_qualite_rivieres",
)

schema_view = get_schema_view(
    oa,
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=OpenAPISchemaGenerator,
)

router = routers.DefaultRouter()
router.register(r'stations', StationViewSet)
router.register(r'analyses', AnalyseViewSet)
router.register(r'sync_entities', SyncEntitiesViewSet, basename="sync_entities")
router.register(r'metrics', MetricsViewSet, basename="metrics")

urlpatterns = [
    url(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(router.urls)),
]
