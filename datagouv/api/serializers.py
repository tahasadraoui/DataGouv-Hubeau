from rest_framework import serializers

from datagouv.api.models import *


class DataGouvSerializer(serializers.Serializer):

    class Meta:
        abstract = True
        exclude = []


class StationSerializer(DataGouvSerializer):

    class Meta:
        model = Station
        fields = '__all__'
