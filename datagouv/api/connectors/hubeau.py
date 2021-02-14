import requests
import logging
logger = logging.getLogger('DataGouv')

from django.conf import settings

from rest_framework import serializers

from datagouv.api.models import *


class HubEau:
    """
        Un connecteur permettant de récupérer des entités différentes,
        de l'API Qualité des cours d'eau.
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

    def get_entities_by_region_code(self, url, region_code, page=1):
        """
            This method allows to get a given type of entity (station, analyse) by its region code,
            and iterate over all pages from the paginted API response.
            It's possible to get a sample, by specifying the maximum pages argument
        """

        result = []

        response = self.session.get(f"{url}&page={page}")
        if response.status_code == 206:

            if hasattr(settings, 'MAXIMUM_PAGES') & page == settings.MAXIMUM_PAGES:
                return response.json()["data"]

            if response.json()["next"]:

                result.extend(response.json()["data"])

                page += 1
                result.extend(self.get_entities_by_region_code(url, region_code, page))

            else:
                return response.json()["data"]
        else:
            logger.error(f"Error occured while getting stations: {response.status_code}, {response.text}")
            return False

        return result

    def get_stations(self, region_code):

        url = self.stations_url + f"?code_region={region_code}&exact_count=true&format=json&size=20"

        result = self.get_entities_by_region_code(url, region_code)
        if result:
            self.nb_entities_found = len(result)

        return result

    def get_analyses(self, region_code, first_analyse_date=None):

        if first_analyse_date:
            # https://hubeau.eaufrance.fr/page/api-qualite-cours-deau-tuto
            url = self.analyses_url + f"?code_region={region_code}&date_debut_prelevement={first_analyse_date}&exact_count=true&format=json&size=20"
        else:
            url = self.analyses_url + f"?code_region={region_code}&exact_count=true&format=json&size=20"

        result = self.get_entities_by_region_code(url, region_code)

        if result:
            self.nb_entities_found = len(result)

        return result

    def save_entities_to_db(self, entity, region_code, first_analyse_date=None):
        """
            This method creates or updates entities (stations, analyses) in the DB.
            - A station is identified by its code (unique)
        """

        if entity == "stations":
            entities = self.get_stations(region_code)
            EntityModel = Station

        elif entity == "analyses":
            if first_analyse_date:
                entities = self.get_analyses(region_code, first_analyse_date)
            else:
                entities = self.get_analyses(region_code)
            EntityModel = Analyse

        self.nb_entities_found = len(entities)

        entity_fields = [field.name for field in EntityModel._meta.fields]
        entity_fields.remove("deleted")
        entity_fields.remove("id")

        # Analyses
        if "station" in entity_fields:
            entity_fields.remove("station")

        # Empty DB
        if not EntityModel.objects.count():
            logger.info(f"We have an empty DB. We will save all received {entity}")

            for item in entities:
                try:
                    entity_values = {field: item[field] for field in entity_fields}

                    # Analyse -- Station ForeignKey
                    if entity == "analyses":
                        entity_values["station"] = Station.objects.get(code_station=item["code_station"])

                    EntityModel.objects.create(**entity_values)
                    self.nb_entities_created += 1
                except Exception as e:
                    logger.error(e)
                    self.nb_entities_failed_to_create += 1

            self.nb_entities_created = EntityModel.objects.count()

        else:

            for item in entities:
                try:
                    entity_values = {field: item[field] for field in entity_fields}

                    # Analyse -- Station ForeignKey
                    if entity == "analyses":
                        entity_values["station"] = Station.objects.get(code_station=item["code_station"])

                    obj, created = EntityModel.objects.get_or_create(**entity_values)

                    if created:
                        self.nb_entities_created += 1
                    else:
                        self.nb_entities_updated += 1
                except Exception as e:
                    logger.error(e)
                    self.nb_entities_failed += 1
