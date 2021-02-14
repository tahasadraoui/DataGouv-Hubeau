from datagouv.api.connectors.hubeau import HubEau
from datagouv.api.models import *
from rest_framework import serializers
import logging
logger = logging.getLogger('DataGouv')


class DataGouvSerializer(serializers.ModelSerializer):

    class Meta:
        abstract = True
        exclude = ['deleted']


class StationSerializer(DataGouvSerializer):

    class Meta(DataGouvSerializer.Meta):
        model = Station


class AnalyseSerializer(DataGouvSerializer):

    class Meta(DataGouvSerializer.Meta):
        model = Analyse


class SyncEntitiesSerializer(DataGouvSerializer):

    stations_found = serializers.IntegerField(required=False)
    analyses_found = serializers.IntegerField(required=False)

    class Meta(DataGouvSerializer.Meta):
        model = SyncEntities
        exclude = ['id', 'deleted']

    def create(self, validated_data):

        logger.info(f"SyncEntitiesSerializer create: {validated_data}")

        asked_operation = validated_data["asked_operation"]
        region_code = validated_data.get("region_code", None)

        if asked_operation == 'SYNC_ALL':
            logger.info(f"Sync all entities from Hub'Eau: stations + analyses: Not implemented yet")

        else:

            # Compulsory
            if not region_code:
                raise serializers.ValidationError("The station's region code is required to synchronize a station")

            if asked_operation == 'SYNC_STATIONS':
                logger.info(f"Sync stations from Hub'Eau")

                entities = "stations"

            if asked_operation == 'SYNC_ANALYSES':
                logger.info(f"Sync analyses from Hub'Eau")

                entities = "analyses"

            hubeau_connector = HubEau()

            try:

                entities_found = hubeau_connector.sync_entites_by_region_code("stations", region_code)
                logger.info(f"{len(entities_found)} {entities} found, by region code {region_code}")

                validated_data[f"{entities}_found"] = len(entities_found)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError("An error occured while getting the {entities}.")

        return SyncEntities(**validated_data)
