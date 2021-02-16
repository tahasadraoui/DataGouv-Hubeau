import logging
logger = logging.getLogger('DataGouv')

from django.db.models.functions import Round

from rest_framework import serializers

from datagouv.api.models import *
from datagouv.api.connectors.hubeau import HubEau
from django.db.models import Count
import decimal


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

                hubeau_connector.synchronize_entities("stations", region_code)

            except Exception as e:
                logger.error(e)
                raise serializers.ValidationError(f"An error occured while synchronizing the stations.")

        elif asked_operation == 'SYNC_ANALYSES':
            logger.info(f"Sync analyses from Hub'Eau")

            if not first_analyse_date:
                raise serializers.ValidationError(f"Missing parameter to sync analyses.")

            try:
                hubeau_connector.synchronize_entities("analyses", region_code, first_analyse_date)

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
    weighted_average_results_by_departement = serializers.ListField(required=False)

    def create(self, validated_data):

        logger.info(f"MetricsSerializer create: {validated_data}")

        region_code = validated_data.get("region_code", None)
        number_of_items = validated_data.get("number_of_items", 10)

        stations_queryset = Station.objects.filter(analyse__resultat__isnull=False)

        if region_code:
            stations_queryset = stations_queryset.filter(code_region=region_code)

        response = {}

        # try:
        if 1:

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
            
            response["average_results_by_departement"] = []
            average_results_by_departement = {}
            
            for item in stations:
                response["average_results_by_departement"].append({'code_departement': int(item[1]), 'avarage_result': round(item[0], 4)})
                average_results_by_departement[int(item[1])] = round(item[0], 4)

            # Best departements; average results must be weighted by number of stations (cours d'eau)
            # Formula: if number of stations (cours d'eau) in departemenet < 10 --> result of dep * 0.8

            stations_by_departement = Station.objects.values('code_departement').annotate(code_dep_count=Count('code_departement'))
            cours_eau_by_departement = {item["code_departement"]: item["code_dep_count"]  for item in stations_by_departement}

            weighted_average_results_by_departement = []
            for departement, avg_results in average_results_by_departement.items():
                if int(cours_eau_by_departement[departement]) < 150:
                    weighted_average_results_by_departement.append({"code_departement": departement, "avarage_result": round(avg_results * decimal.Decimal(0.8), 4), "nb": cours_eau_by_departement[departement]})
                else:
                    weighted_average_results_by_departement.append({"code_departement": departement, "avarage_result": avg_results, "nb": cours_eau_by_departement[departement]})
            response["weighted_average_results_by_departement"] = weighted_average_results_by_departement

            return response

        # except Exception as e:
        #     logger.error(e)
        #     raise serializers.ValidationError("An error has occured while generating metrics.")
