from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from datagouv.api.models import *
from datagouv.api.serializers import *


class DataGouvDefaultViewSet(viewsets.GenericViewSet):

    class Meta:
        abstract = True

    filter_backends = (DjangoFilterBackend,)
    permission_classes = (AllowAny,)


class StationViewSet(DataGouvDefaultViewSet):
    """
    API des stations
    """

    queryset = Station.objects.all()
    serializer_class = StationSerializer
