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


from api.views import *


oa = openapi.Info(
    title="DataGouv FR API",
    default_version='v1',
    description="This API allows caller to manage DataGouv Region 76 entities",
    license=openapi.License(name="DataGouv License"),
)

schema_view = get_schema_view(
    oa,
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=OpenAPISchemaGenerator,
)

router = routers.DefaultRouter()
# router.register(r'stations', StationViewSet)

urlpatterns = [
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
