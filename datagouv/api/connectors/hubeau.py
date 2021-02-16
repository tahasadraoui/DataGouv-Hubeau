import time
import datetime
import decimal
import requests
import logging
logger = logging.getLogger('DataGouv')

from django.conf import settings

from rest_framework import serializers

from datagouv.api.models import *


class HubEau:
    """
        Un connecteur permettant de récupérer des entités (stations, analyses) différentes,
        de l'API Qualité des cours d'eau. Et les sauvegarder dans la base des données
    """

    def __init__(self):

        self.api_url = settings.HUBEAU_API_URL
        self.stations_path = "station_pc"
        self.analyses_path = "analyse_pc"

        self.stations_url = f"{self.api_url}{self.stations_path}"
        self.analyses_url = f"{self.api_url}{self.analyses_path}"

        self.session = requests.session()

        # Records
        self.nb_entities_found = 0
        self.nb_entities_created = 0
        self.nb_entities_failed_to_create = 0
        self.nb_entities_updated = 0
        self.nb_entities_failed = 0

    def save_entities(self, entity, data):
        """
            This method saves the received entities to the DB
        """

        self.nb_entities_found += len(data)

        if entity == "stations":
            EntityModel = Station

        elif entity == "analyses":
            EntityModel = Analyse

        entity_fields = [field.name for field in EntityModel._meta.fields]
        entity_fields.remove("deleted")
        entity_fields.remove("id")

        # Analyses
        if "station" in entity_fields:
            entity_fields.remove("station")

        for item in data:
            try:
                entity_values = {field: item[field] for field in entity_fields}

                # Analyse -- Station ForeignKey
                if entity == "analyses":
                    entity_values["station"] = Station.objects.get(code_station=item["code_station"])
                    if entity_values["incertitude_analytique"]:
                        entity_values["incertitude_analytique"] = round(decimal.Decimal(entity_values["incertitude_analytique"]), 4)
                    if entity_values["resultat"]:
                        entity_values["resultat"] = round(decimal.Decimal(entity_values["resultat"]), 4)

                obj, created = EntityModel.objects.get_or_create(**entity_values)

                if created:
                    self.nb_entities_created += 1
                else:
                    self.nb_entities_updated += 1
            except Exception as e:
                logger.error(e)
                self.nb_entities_failed += 1

    def synchronize_entities(self, entity, region_code, first_analyse_date=None):
        """
            This is a proxy method that prepares the URL to sync the entities (stations, analyses)
        """

        if entity == "stations":
            url = self.stations_url + f"?code_region={region_code}&exact_count=true&format=json&size=1000"
        elif entity == "analyses":
            url = self.analyses_url + f"?code_region={region_code}&exact_count=true&format=json&size=1000"
            if first_analyse_date:
                url += f"&date_debut_prelevement={first_analyse_date}"
        else:
            raise serializers.ValidationError(f"An unsupported entity type given to sync: {entity}")

        self.sync_entities(entity, region_code, url)

    def sync_entities(self, entity, region_code, url):
        """
            A recursive method keeps going through the 'next' in the API response,
            to get all pages & objects
        """

        response = requests.get(url)

        if response:
            self.save_entities(entity, response.json()["data"])
            if response.json().get("next", None):
                self.sync_entities(entity, region_code, response.json()["next"])
        else:
            logger.error(f"Error occured while getting {entity}: {response.status_code}, {response.text}")
