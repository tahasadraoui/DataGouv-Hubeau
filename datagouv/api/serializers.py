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

                hubeau_connector.save_stations_by_page_to_db(region_code)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while synchronizing the stations.")

        elif asked_operation == 'SYNC_ANALYSES':
            logger.info(f"Sync analyses from Hub'Eau")

            if not first_analyse_date:
                raise serializers.ValidationError(f"Missing parameter to sync analyses.")

            try:
                hubeau_connector.save_analyses_by_page_and_week_to_db(region_code, first_analyse_date)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while synchronizing the analyses.")

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
    average_results_by_departement = serializers.ListField(required=False)

    def create(self, validated_data):

        logger.info(f"MetricsSerializer create: {validated_data}")

        region_code = validated_data.get("region_code", None)
        number_of_items = validated_data.get("number_of_items", 10)

        stations_queryset = Station.objects.filter(analyse__resultat__isnull=False)

        if region_code:
            stations_queryset = stations_queryset.filter(code_region=region_code)

        response = {}

        # Average results by stations
        stations = stations_queryset.annotate(avg_results=Avg('analyse__resultat')).order_by('-avg_results')

        response["best_stations"] = stations[:number_of_items]

        stations = stations.order_by('avg_results')
        response["worst_stations"] = stations[:number_of_items]

        # Average results by departements
        stations = stations_queryset.values('code_departement') \
            .annotate(avg_results=Avg('analyse__resultat')) \
            .order_by('avg_results') \
            .values_list('avg_results', 'code_departement')

        response["average_results_by_departement"] = [{'code_departement': int(item[1]), 'avarage_result': item[0]} for item in stations]

        return response
