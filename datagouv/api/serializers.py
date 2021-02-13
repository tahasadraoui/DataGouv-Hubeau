from datagouv.api.models import *
from rest_framework import serializers
import logging
logger = logging.getLogger('DataGouv')


class DataGouvSerializer(serializers.ModelSerializer):

    class Meta:
        abstract = True
        exclude = ['deleted']


class StationSerializer(DataGouvSerializer):

    class Meta:
        model = Station


class AnalyseSerializer(DataGouvSerializer):

    class Meta:
        model = Analyse


class SyncEntitiesSerializer(DataGouvSerializer):

    class Meta:
        model = SyncEntities
        exclude = ['id', 'deleted']

    def create(self, validated_data):

        logger.info(f"SyncEntitiesSerializer create: {validated_data}")

        asked_operation = validated_data["asked_operation"]
        code_station = validated_data.get("code_station", None)

        if asked_operation == 'SYNC_ALL':
            logger.info(f"Sync all entities from Hub'Eau: stations + analyses: Not implemented yet")

        elif asked_operation == 'SYNC_STATIONS':
            logger.info(f"Sync stations from Hub'Eau")

            if not code_station:
                raise serializers.ValidationError("The station's code is required to synchronize a station")

        elif asked_operation == 'SYNC_ANALYSES':
            logger.info(f"Sync analyses from Hub'Eau")

            if not code_station:
                raise serializers.ValidationError("The station's code is required to synchronize a station's analytics")

        return SyncEntities(**validated_data)
