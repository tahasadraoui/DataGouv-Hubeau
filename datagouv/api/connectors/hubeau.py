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

    def save_entities(self, entity, data, first_analyse_date=None):
        """
        """

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

    def save_entities_by_page_to_db(self, entity, region_code, first_analyse_date=None):
        """
            This method allows to get a given type of entity (station, analyse) by its region code,
            and iterate over all pages from the paginted API response.
            It's possible to get a sample, by specifying the maximum pages argument
            
            It gets and saves them, page by page, as it gets each one.
        """

        if entity == "stations":

            url = self.stations_url + f"?code_region={region_code}&exact_count=true&format=json&size=20"

        elif entity == "analyses":

            if first_analyse_date:
                # https://hubeau.eaufrance.fr/page/api-qualite-cours-deau-tuto
                url = self.analyses_url + f"?code_region={region_code}&date_debut_prelevement={first_analyse_date}&exact_count=true&format=json&size=20"
            
                end_date = first_analyse_date + datetime.timedelta(days=15)

                url += f"&date_fin_prelevement={str(end_date)}"
            
            else:
                url = self.analyses_url + f"?code_region={region_code}&exact_count=true&format=json&size=20"

        page = 1

        response = self.session.get(f"{url}&page={page}")
        if response.status_code == 206:

            logger.info(f"Count {entity}: {response.json()['count']}")
            logger.info(f"Last url: {response.json()['last']}")

            while response.json()["next"]:

                if response.status_code == 206:

                    if hasattr(settings, 'MAXIMUM_PAGES') and page == settings.MAXIMUM_PAGES:
                        self.save_entities(entity, response.json()["data"])
                        break

                    else:

                        self.save_entities(entity, response.json()["data"])
                        page += 1
                        response = self.session.get(f"{url}&page={page}")

                else:
                    logger.error(f"Error occured while getting stations: {response.status_code}, {response.text}")
                    return False

        else:
            logger.error(f"Error occured while getting stations: {response.status_code}, {response.text}")
            return False
