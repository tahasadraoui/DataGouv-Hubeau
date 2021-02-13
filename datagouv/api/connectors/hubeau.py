from datagouv.api.models import *
import logging
logger = logging.getLogger(__name__)


class HubEau:
    """
        Un connecteur permettant de récupérer des entités différentes,
        de l'API Qualité des cours d'eau.
    """

    def __init__(self, api_url):

        self.api_url = api_url

    def report(self):
        pass

    def sync_stations(self):
        pass

    def sync_analyses(self):
        pass
