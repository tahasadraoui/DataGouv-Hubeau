from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from datagouv.api.models import *
from datagouv.api.serializers import *


class DataGouvDefaultViewSet(viewsets.GenericViewSet):

    class Meta:
        abstract = True

    filter_backends = (DjangoFilterBackend,)
    permission_classes = (AllowAny,)


class DataGouvViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      DataGouvDefaultViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass


class StationViewSet(DataGouvViewSet):
    """
    API des stations
    """

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class AnalyseViewSet(DataGouvViewSet):
    """
    API des analyses
    """

    queryset = Analyse.objects.all()
    serializer_class = AnalyseSerializer


class SyncEntities(DataGouvViewSet):
    """
    API qui permettent de synchroniser des entités différentes (stations, analyses..)
    """

    serializer_class = SyncEntitiesSerializer
    http_method_names = ['post']