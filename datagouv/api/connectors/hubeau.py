import requests
import logging
logger = logging.getLogger('DataGouv')

from rest_framework import serializers

from datagouv.api.models import *


class HubEau:
    """
        Un connecteur permettant de récupérer des entités différentes,
        de l'API Qualité des cours d'eau.
    """

    def __init__(self):

        self.api_url = "https://hubeau.eaufrance.fr/api/v1/"
        self.stations_path = "qualite_rivieres/station_pc"
        self.analyses_path = "qualite_rivieres/analyse_pc"

        self.stations_url = f"{self.api_url}{self.stations_path}"
        self.analyses_url = f"{self.api_url}{self.analyses_path}"

        self.session = requests.session()

    def report(self):
        pass

    def get_entities_by_region_code(self, url, region_code, page=1):
        """
            This method allows to get a given type of entity (station, analyse) by its region code,
            and iterate over all pages from the paginted API response.
            It's possible to get a sample, by specifying the maximum pages argument
        """

        result = []

        response = self.session.get(f"{url}&page={page}")
        if response.status_code == 206:

            if page == 1:
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

    def sync_entites_by_region_code(self, entity, region_code, first_analyse_date=None):
        """
        """

        logger.info(f"Sync {entity} by region code {region_code}")

        if entity not in ["stations", "analyses"]:
            raise serializers.ValidationError(f"An invalid type of entity was given to synchronise: {entity}")

        if entity == "stations":
            url = self.stations_url + f"?code_region={region_code}&exact_count=true&format=json&size=20"

        elif entity == "analyses":
            if first_analyse_date:
                url = self.analyses_url + f"?code_region={region_code}&date_debut_prelevement={first_analyse_date}&exact_count=true&format=json&size=20"
            else:
                url = self.analyses_url + f"?code_region={region_code}&exact_count=true&format=json&size=20"

        return self.get_entities_by_region_code(url, region_code)
