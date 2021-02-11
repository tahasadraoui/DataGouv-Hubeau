from rest_framework import serializers

# import datagouv.api

from api.models import Station
# from datagouv.api.models import Station

class DataGouvSerializer(serializers.Serializer):
    
    class Meta:
        abstract = True
        exclude = []

class StationSerializer(DataGouvSerializer):

    class Meta:
        model = Station