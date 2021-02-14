import logging
logger = logging.getLogger('DataGouv')

from django.db.models.functions import Round

from rest_framework import serializers

from datagouv.api.models import *
from datagouv.api.connectors.hubeau import HubEau


class DataGouvSerializer(serializers.ModelSerializer):

    class Meta:
        abstract = True
        exclude = ['deleted']


class StationSerializer(DataGouvSerializer):

    results_average = serializers.FloatField(required=False)

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

        if asked_operation == 'SYNC_STATIONS':
            logger.info(f"Sync stations from Hub'Eau")

            try:

                hubeau_connector.save_entities_by_page_to_db("stations", region_code)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while synchronizing the stations.")

        elif asked_operation == 'SYNC_ANALYSES':
            logger.info(f"Sync analyses from Hub'Eau")

            # try:

            if first_analyse_date:
                hubeau_connector.save_entities_by_page_to_db("analyses", region_code, first_analyse_date)
            else:
                hubeau_connector.save_entities_by_page_to_db("analyses", region_code)

            # except Exception as e:
            #     logger.error(e)
            #     raise serializers.ValidationError(f"An error occured while synchronizing the analyses.")

        validated_data["entities_found"] = hubeau_connector.nb_entities_found
        validated_data["entities_created"] = hubeau_connector.nb_entities_created
        validated_data["entities_failed_to_create"] = hubeau_connector.nb_entities_failed_to_create
        validated_data["entities_failed_to_create_or_update"] = hubeau_connector.nb_entities_failed
        validated_data["entities_updated"] = hubeau_connector.nb_entities_updated

        return SyncEntities(**validated_data)


class MetricsSerializer(serializers.Serializer):

    best_stations = StationSerializer(many=True, required=False)
    worst_stations = StationSerializer(many=True, required=False)
    number_of_items = serializers.IntegerField(required=False)
    region_code = serializers.IntegerField(required=False)

    # class Meta(DataGouvSerializer.Meta):
    #     model = Metrics
    #     exclude = ['id', 'deleted']

    def create(self, validated_data):

        logger.info(f"MetricsSerializer create: {validated_data}")

        region_code = validated_data.get("region_code", None)
        number_of_items = validated_data.get("number_of_items", 10)

        stations = Station.objects.filter(analyse__resultat__isnull=False)
        if region_code:
            stations = stations.filter(code_region=region_code)

        response = {}

        stations = stations.annotate(avg_results=Avg('analyse__resultat')).order_by('avg_results')
        response["best_stations"] = stations[:number_of_items]

        stations = stations.order_by('-avg_results')
        response["worst_stations"] = stations[:number_of_items]

        return response
