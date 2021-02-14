import logging
logger = logging.getLogger('DataGouv')

from rest_framework import serializers

from datagouv.api.models import *
from datagouv.api.connectors.hubeau import HubEau


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

    class Meta(DataGouvSerializer.Meta):
        model = SyncEntities
        exclude = ['id', 'deleted']

    def create(self, validated_data):

        logger.info(f"SyncEntitiesSerializer create: {validated_data}")

        asked_operation = validated_data["asked_operation"]
        region_code = validated_data["region_code"]
        first_analyse_date = validated_data.get("date_debut_prelevement", None)  # Les résultats/ les analyses à partir de

        hubeau_connector = HubEau()

        if asked_operation == 'GET_STATIONS':
            logger.info(f"Get stations from Hub'Eau")

            try:

                hubeau_connector.get_stations(region_code)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while getting the stations.")

        elif asked_operation == 'SYNC_STATIONS':
            logger.info(f"Sync stations from Hub'Eau")

            try:

                hubeau_connector.save_entities_to_db("stations", region_code)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while synchronizing the stations.")

        elif asked_operation == 'GET_ANALYSES':
            logger.info(f"Get analyses from Hub'Eau")

            try:

                if first_analyse_date:
                    hubeau_connector.get_analyses(region_code, first_analyse_date)
                else:
                    hubeau_connector.get_analyses(region_code)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while getting the analyses.")

        elif asked_operation == 'SYNC_ANALYSES':
            logger.info(f"Sync analyses from Hub'Eau")

            try:

                if first_analyse_date:
                    hubeau_connector.save_entities_to_db("analyses", region_code, first_analyse_date)
                else:
                    hubeau_connector.save_entities_to_db("analyses", region_code)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while synchronizing the analyses.")

        validated_data["entities_found"] = hubeau_connector.nb_entities_found
        validated_data["entities_created"] = hubeau_connector.nb_entities_created
        validated_data["entities_failed_to_create"] = hubeau_connector.nb_entities_failed_to_create
        validated_data["entities_failed_to_create_or_update"] = hubeau_connector.nb_entities_failed
        validated_data["entities_updated"] = hubeau_connector.nb_entities_updated

        return SyncEntities(**validated_data)
