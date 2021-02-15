from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework

from datagouv.api.models import *


class StationFilterClass(django_filters.FilterSet):

    class Meta:
        model = Station
        fields = '__all__'


class AnalyseFilterClass(django_filters.FilterSet):

    class Meta:
        model = Analyse
        fields = '__all__'
