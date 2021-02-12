from rest_framework import serializers

from datagouv.api.models import *


class DataGouvSerializer(serializers.ModelSerializer):

    class Meta:
        abstract = True
        exclude = []


class StationSerializer(DataGouvSerializer):

    class Meta:
        model = Station
        fields = '__all__'


class AnalyseSerializer(DataGouvSerializer):

    class Meta:
        model = Analyse
        fields = '__all__'
