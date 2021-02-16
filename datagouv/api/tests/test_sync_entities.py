import responses

from django.conf import settings
from django.test import TestCase

from rest_framework.test import APIClient

from datagouv.api.models import Station, Analyse

STATIONS_76_URL = settings.HUBEAU_API_URL + "station_pc?code_region=76&exact_count=true&format=json&size=1000"
STATIONS_76_FIRST_PAGE_URL = settings.HUBEAU_API_URL + "station_pc?code_region=76&exact_count=true&format=json&size=1000&page=1"
STATIONS_76_SECOND_PAGE_URL = settings.HUBEAU_API_URL + "station_pc?code_region=76&exact_count=true&format=json&size=1000&page=2"
ANALYSES_76_URL = settings.HUBEAU_API_URL + "analyse_pc?code_region=76&exact_count=true&format=json&size=1000"
ANALYSES_76_FIRST_PAGE_URL = settings.HUBEAU_API_URL + "analyse_pc?code_region=76&exact_count=true&format=json&size=1000&page=1"
ANALYSES_76_DATE_URL = settings.HUBEAU_API_URL + "analyse_pc?code_region=76&exact_count=true&format=json&size=1000&date_debut_prelevement=2004-03-01"


class SyncEntitiesTestCase(TestCase):

    def setUp(self):

        super().setUp()

        # Client
        self.client = APIClient()

        # URLs
        self.sync_entities_api_url = "/api/sync_entities/"

        # Responses: Intercept HTTP calls to mock
        # Stations region 76 first page
        responses.add(
            responses.GET,
            STATIONS_76_URL,
            json={
                "count": 4,
                "first": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_region=76&exact_count=true&format=json&page=1&size=1000",
                "last": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_region=76&exact_count=true&format=json&page=1&size=1000",
                "prev": None,
                "next": None,
                "api_version": "1.1.0",
                "data": [
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "durete": None,
                        "coordonnee_x": 754765.47,
                        "coordonnee_y": 6395335.55,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.690753249,
                        "latitude": 44.654968291,
                        "code_commune": "48043",
                        "libelle_commune": "CHÂTEAUNEUF-DE-RANDON",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K21-0300",
                        "nom_cours_eau": "le Chapeauroux",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K21-0300",
                        "code_masse_deau": "GR0234",
                        "code_eu_masse_deau": "FRGR0234",
                        "nom_masse_deau": "LE CHAPEAUROUX ET SES AFFLUENTS DEPUIS LA SOURCE JUSQU'A LA CONFLUENCE AVEC LA CLAMOUSE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR0234",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2004-02-27",
                        "finalite": "Non renseignée",
                        "localisation_precise": "AVAL CONFLUENCE BOUTARESSE",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 960784,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.69075324893397,
                                44.6549682906883
                            ]
                        }
                    },
                    {
                        "code_station": "04026300",
                        "libelle_station": "ALLIER à LA BASTIDE-PUYLAURENT",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026300",
                        "durete": None,
                        "coordonnee_x": 771585.1,
                        "coordonnee_y": 6390856,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.90223627,
                        "latitude": 44.613115134,
                        "code_commune": "48021",
                        "libelle_commune": "LA BASTIDE-PUYLAURENT",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K---0080",
                        "nom_cours_eau": "l'Allier",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K---0080",
                        "code_masse_deau": "GR1491",
                        "code_eu_masse_deau": "FRGR1491",
                        "nom_masse_deau": "L'ALLIER ET SES AFFLUENTS DEPUIS LA SOURCE JUSQU'A LAVEYRUNE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR1491",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2010-11-30",
                        "finalite": "Non renseignée",
                        "localisation_precise": "AVAL LA BASTIDE",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 596178,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.90223627029585,
                                44.6131151335763
                            ]
                        }
                    },
                    {
                        "code_station": "04026400",
                        "libelle_station": "ALLIER à LUC",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026400",
                        "durete": None,
                        "coordonnee_x": 769876.91,
                        "coordonnee_y": 6396732.63,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.881535436,
                        "latitude": 44.666190798,
                        "code_commune": "48086",
                        "libelle_commune": "LUC",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K---0080",
                        "nom_cours_eau": "l'Allier",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K---0080",
                        "code_masse_deau": "GR0145",
                        "code_eu_masse_deau": "FRGR0145",
                        "nom_masse_deau": "L'ALLIER DEPUIS LAVEYRUNE JUSQU'A LANGOGNE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR0145",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2011-03-31",
                        "finalite": "Non renseignée",
                        "localisation_precise": "AVAL LUC",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 604067,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.88153543595519,
                                44.6661907978865
                            ]
                        }
                    },
                    {
                        "code_station": "04026500",
                        "libelle_station": "ALLIER à CHASSERADES",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026500",
                        "durete": None,
                        "coordonnee_x": 767378.6,
                        "coordonnee_y": 6385344,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.848476604,
                        "latitude": 44.563916272,
                        "code_commune": "48027",
                        "libelle_commune": "LE BLEYMARD",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K---0080",
                        "nom_cours_eau": "l'Allier",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K---0080",
                        "code_masse_deau": "GR1491",
                        "code_eu_masse_deau": "FRGR1491",
                        "nom_masse_deau": "L'ALLIER ET SES AFFLUENTS DEPUIS LA SOURCE JUSQU'A LAVEYRUNE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR1491",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": "les prélèvement doivent être fait en amont de la confluence avec le ruisseau de Fontaleyres qui arrive près du pont",
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2013-05-14",
                        "finalite": "Non renseigné",
                        "localisation_precise": "LIEU-DIT CHABALIER - AMONT DU PONT ET CONFLUENCE AVEC RU DE FONTALEYRES",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 585469,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.84847660371236,
                                44.5639162718591
                            ]
                        }
                    }]},
            status=206
        )

        responses.add(
            responses.GET,
            STATIONS_76_FIRST_PAGE_URL,
            json={
                "count": 4,
                "first": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_region=76&exact_count=true&format=json&page=1&size=1000",
                "last": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_region=76&exact_count=true&format=json&page=1&size=1000",
                "prev": None,
                "next": None,
                "api_version": "1.1.0",
                "data": [
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "durete": None,
                        "coordonnee_x": 754765.47,
                        "coordonnee_y": 6395335.55,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.690753249,
                        "latitude": 44.654968291,
                        "code_commune": "48043",
                        "libelle_commune": "CHÂTEAUNEUF-DE-RANDON",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K21-0300",
                        "nom_cours_eau": "le Chapeauroux",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K21-0300",
                        "code_masse_deau": "GR0234",
                        "code_eu_masse_deau": "FRGR0234",
                        "nom_masse_deau": "LE CHAPEAUROUX ET SES AFFLUENTS DEPUIS LA SOURCE JUSQU'A LA CONFLUENCE AVEC LA CLAMOUSE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR0234",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2004-02-27",
                        "finalite": "Non renseignée",
                        "localisation_precise": "AVAL CONFLUENCE BOUTARESSE",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 960784,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.69075324893397,
                                44.6549682906883
                            ]
                        }
                    },
                    {
                        "code_station": "04026300",
                        "libelle_station": "ALLIER à LA BASTIDE-PUYLAURENT",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026300",
                        "durete": None,
                        "coordonnee_x": 771585.1,
                        "coordonnee_y": 6390856,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.90223627,
                        "latitude": 44.613115134,
                        "code_commune": "48021",
                        "libelle_commune": "LA BASTIDE-PUYLAURENT",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K---0080",
                        "nom_cours_eau": "l'Allier",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K---0080",
                        "code_masse_deau": "GR1491",
                        "code_eu_masse_deau": "FRGR1491",
                        "nom_masse_deau": "L'ALLIER ET SES AFFLUENTS DEPUIS LA SOURCE JUSQU'A LAVEYRUNE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR1491",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2010-11-30",
                        "finalite": "Non renseignée",
                        "localisation_precise": "AVAL LA BASTIDE",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 596178,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.90223627029585,
                                44.6131151335763
                            ]
                        }
                    },
                    {
                        "code_station": "04026400",
                        "libelle_station": "ALLIER à LUC",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026400",
                        "durete": None,
                        "coordonnee_x": 769876.91,
                        "coordonnee_y": 6396732.63,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.881535436,
                        "latitude": 44.666190798,
                        "code_commune": "48086",
                        "libelle_commune": "LUC",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K---0080",
                        "nom_cours_eau": "l'Allier",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K---0080",
                        "code_masse_deau": "GR0145",
                        "code_eu_masse_deau": "FRGR0145",
                        "nom_masse_deau": "L'ALLIER DEPUIS LAVEYRUNE JUSQU'A LANGOGNE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR0145",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2011-03-31",
                        "finalite": "Non renseignée",
                        "localisation_precise": "AVAL LUC",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 604067,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.88153543595519,
                                44.6661907978865
                            ]
                        }
                    },
                    {
                        "code_station": "04026500",
                        "libelle_station": "ALLIER à CHASSERADES",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026500",
                        "durete": None,
                        "coordonnee_x": 767378.6,
                        "coordonnee_y": 6385344,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.848476604,
                        "latitude": 44.563916272,
                        "code_commune": "48027",
                        "libelle_commune": "LE BLEYMARD",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K---0080",
                        "nom_cours_eau": "l'Allier",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K---0080",
                        "code_masse_deau": "GR1491",
                        "code_eu_masse_deau": "FRGR1491",
                        "nom_masse_deau": "L'ALLIER ET SES AFFLUENTS DEPUIS LA SOURCE JUSQU'A LAVEYRUNE",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR1491",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": "les prélèvement doivent être fait en amont de la confluence avec le ruisseau de Fontaleyres qui arrive près du pont",
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2013-05-14",
                        "finalite": "Non renseigné",
                        "localisation_precise": "LIEU-DIT CHABALIER - AMONT DU PONT ET CONFLUENCE AVEC RU DE FONTALEYRES",
                        "nature": "M",
                        "altitude_point_caracteristique": 0,
                        "point_kilometrique": 585469,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.84847660371236,
                                44.5639162718591
                            ]
                        }
                    }]},
            status=206
        )

        # Stations region 76 second page
        responses.add(
            responses.GET,
            STATIONS_76_SECOND_PAGE_URL,
            json={
                "count": 3,
                "first": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_region=76&exact_count=true&format=json&page=1&size=1000",
                "last": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_region=76&exact_count=true&format=json&page=2&size=1000",
                "prev": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_region=76&exact_count=true&format=json&page=1&size=1000",
                "next": None,
                "api_version": "1.1.0",
                "data": [
                    {
                        "code_station": "04420008",
                        "libelle_station": "ALLIER A LANGOGNE",
                        "uri_station": "http://id.eaufrance.fr/STQ/04420008",
                        "durete": None,
                        "coordonnee_x": 765992.0,
                        "coordonnee_y": 6406327.0,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.833806976,
                        "latitude": 44.752942775,
                        "code_commune": "48080",
                        "libelle_commune": "LANGOGNE",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": None,
                        "nom_cours_eau": None,
                        "uri_cours_eau": None,
                        "code_masse_deau": None,
                        "code_eu_masse_deau": None,
                        "nom_masse_deau": None,
                        "uri_masse_deau": None,
                        "code_eu_sous_bassin": None,
                        "nom_sous_bassin": None,
                        "code_bassin": None,
                        "code_eu_bassin": None,
                        "nom_bassin": None,
                        "uri_bassin": None,
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2019-02-22",
                        "finalite": "2",
                        "localisation_precise": "Allier en aval direct du seuil de Naussac 2",
                        "nature": "A",
                        "altitude_point_caracteristique": 0.0,
                        "point_kilometrique": None,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.83380697622291,
                                44.7529427747047
                            ]
                        }
                    },
                    {
                        "code_station": "04420009",
                        "libelle_station": "RAU DE LA REAL A CHASTANIER",
                        "uri_station": "http://id.eaufrance.fr/STQ/04420009",
                        "durete": None,
                        "coordonnee_x": 760329.0,
                        "coordonnee_y": 6405564.0,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.762166742,
                        "latitude": 44.746589043,
                        "code_commune": "48041",
                        "libelle_commune": "CHASTANIER",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": None,
                        "nom_cours_eau": None,
                        "uri_cours_eau": None,
                        "code_masse_deau": None,
                        "code_eu_masse_deau": None,
                        "nom_masse_deau": None,
                        "uri_masse_deau": None,
                        "code_eu_sous_bassin": None,
                        "nom_sous_bassin": None,
                        "code_bassin": None,
                        "code_eu_bassin": None,
                        "nom_bassin": None,
                        "uri_bassin": None,
                        "type_entite_hydro": "2",
                        "commentaire": None,
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2019-02-22",
                        "finalite": "2",
                        "localisation_precise": "Reals apres arrivee de la derivation de la retenue d auroux sur le chapeauroux",
                        "nature": "A",
                        "altitude_point_caracteristique": 0.0,
                        "point_kilometrique": None,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.76216674159844,
                                44.7465890425064
                            ]
                        }
                    },
                    {
                        "code_station": "04421000",
                        "libelle_station": "RAU DU SAP A AUROUX",
                        "uri_station": "http://id.eaufrance.fr/STQ/04421000",
                        "durete": None,
                        "coordonnee_x": 756579.8,
                        "coordonnee_y": 6404258.0,
                        "code_projection": "26",
                        "libelle_projection": "RGF93 / Lambert 93",
                        "longitude": 3.714654552,
                        "latitude": 44.735147275,
                        "code_commune": "48010",
                        "libelle_commune": "AUROUX",
                        "code_departement": "48",
                        "libelle_departement": "LOZERE",
                        "code_region": "76",
                        "libelle_region": "OCCITANIE",
                        "code_cours_eau": "K2144500",
                        "nom_cours_eau": "la Fouillouse",
                        "uri_cours_eau": "http://id.eaufrance.fr/CEA/K2144500",
                        "code_masse_deau": "GR1831",
                        "code_eu_masse_deau": "FRGR1831",
                        "nom_masse_deau": "LE FOUILLOUSE ET SES AFFLUENTS DEPUIS LA SOURCE JUSQU'A LA CONFLUENCE AVEC LE CHAPEAUROUX",
                        "uri_masse_deau": "http://id.eaufrance.fr/MDO/GR1831",
                        "code_eu_sous_bassin": "FRG_ALA",
                        "nom_sous_bassin": "Allier - Loire amont",
                        "code_bassin": "G",
                        "code_eu_bassin": "FRG",
                        "nom_bassin": "La Loire, les cours d'eau côtiers vendéens et bretons",
                        "uri_bassin": "http://id.eaufrance.fr/SEH/G",
                        "type_entite_hydro": "2",
                        "commentaire": "Rejet de lagunage de la mine en amont.",
                        "date_creation": "1900-01-01",
                        "date_arret": None,
                        "date_maj_information": "2012-02-02",
                        "finalite": "Non renseigné",
                        "localisation_precise": "ROUTE DE LE SAP À PARPAILLON",
                        "nature": "M",
                        "altitude_point_caracteristique": 0.0,
                        "point_kilometrique": 998067.0,
                        "premier_mois_annee_etiage": None,
                        "superficie_bassin_versant_reel": None,
                        "superficie_bassin_versant_topo": None,
                        "geometry": {
                            "type": "Point",
                            "crs": {
                                "type": "name",
                                "properties": {
                                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                }
                            },
                            "coordinates": [
                                3.71465455191597,
                                44.735147274981
                            ]
                        }
                    }
                ]
            },
            status=206
        )

        # Analyses region 76
        responses.add(
            responses.GET,
            ANALYSES_76_URL,
            json={
                "count": 3,
                "first": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc?code_region=76&page=1&size=1000",
                "last": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc?code_region=76&page=679301&size=1000",
                "prev": None,
                "next": None,
                "api_version": "1.1.0",
                "data": [
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "23",
                        "libelle_fraction": "Eau brute",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/23",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1305",
                        "libelle_parametre": "MES",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1305",
                        "resultat": 2,
                        "code_groupe_parametre": [
                            "192",
                            "191",
                            "165",
                            "164",
                            "32"
                        ],
                        "libelle_groupe_parametre": [
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau résiduaire",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau douce",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Physique"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/192",
                            "http://id.eaufrance.fr/GPR/191",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/32"
                        ],
                        "code_unite": "162",
                        "symbole_unite": "mg/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/162",
                        "code_remarque": "10",
                        "mnemo_remarque": "Résultat < au seuil de quantification",
                        "code_insitu": "2",
                        "libelle_insitu": "Laboratoire",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    },
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "3",
                        "libelle_fraction": "Phase aqueuse de l'eau (filtrée, centrifugée...)",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/3",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1340",
                        "libelle_parametre": "NO3-",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1340",
                        "resultat": 3,
                        "code_groupe_parametre": [
                            "193",
                            "192",
                            "191",
                            "166",
                            "165",
                            "164",
                            "47"
                        ],
                        "libelle_groupe_parametre": [
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau saline",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau résiduaire",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau douce",
                            "Paramètres de l'analyse régulière du contrôle de surveillance de l'état chimique des eaux souterraines",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Paramètres azotés"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/193",
                            "http://id.eaufrance.fr/GPR/192",
                            "http://id.eaufrance.fr/GPR/191",
                            "http://id.eaufrance.fr/GPR/166",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/47"
                        ],
                        "code_unite": "173",
                        "symbole_unite": "mg(NO3)/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/173",
                        "code_remarque": "1",
                        "mnemo_remarque": "Résultat > seuil de quantification et < au seuil de saturation ou Résultat = 0",
                        "code_insitu": "2",
                        "libelle_insitu": "Laboratoire",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    },
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "23",
                        "libelle_fraction": "Eau brute",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/23",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1311",
                        "libelle_parametre": "O2 dissous",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1311",
                        "resultat": 8.9,
                        "code_groupe_parametre": [
                            "166",
                            "165",
                            "164",
                            "46"
                        ],
                        "libelle_groupe_parametre": [
                            "Paramètres de l'analyse régulière du contrôle de surveillance de l'état chimique des eaux souterraines",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Autres éléments minéraux"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/166",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/46"
                        ],
                        "code_unite": "175",
                        "symbole_unite": "mg(O2)/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/175",
                        "code_remarque": "1",
                        "mnemo_remarque": "Résultat > seuil de quantification et < au seuil de saturation ou Résultat = 0",
                        "code_insitu": "1",
                        "libelle_insitu": "In situ",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    }
                ]
            },
            status=206
        )

        responses.add(
            responses.GET,
            ANALYSES_76_FIRST_PAGE_URL,
            json={
                "count": 3,
                "first": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc?code_region=76&page=1&size=1000",
                "last": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc?code_region=76&page=679301&size=1000",
                "prev": None,
                "next": None,
                "api_version": "1.1.0",
                "data": [
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "23",
                        "libelle_fraction": "Eau brute",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/23",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1305",
                        "libelle_parametre": "MES",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1305",
                        "resultat": 2,
                        "code_groupe_parametre": [
                            "192",
                            "191",
                            "165",
                            "164",
                            "32"
                        ],
                        "libelle_groupe_parametre": [
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau résiduaire",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau douce",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Physique"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/192",
                            "http://id.eaufrance.fr/GPR/191",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/32"
                        ],
                        "code_unite": "162",
                        "symbole_unite": "mg/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/162",
                        "code_remarque": "10",
                        "mnemo_remarque": "Résultat < au seuil de quantification",
                        "code_insitu": "2",
                        "libelle_insitu": "Laboratoire",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    },
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "3",
                        "libelle_fraction": "Phase aqueuse de l'eau (filtrée, centrifugée...)",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/3",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1340",
                        "libelle_parametre": "NO3-",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1340",
                        "resultat": 3,
                        "code_groupe_parametre": [
                            "193",
                            "192",
                            "191",
                            "166",
                            "165",
                            "164",
                            "47"
                        ],
                        "libelle_groupe_parametre": [
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau saline",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau résiduaire",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau douce",
                            "Paramètres de l'analyse régulière du contrôle de surveillance de l'état chimique des eaux souterraines",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Paramètres azotés"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/193",
                            "http://id.eaufrance.fr/GPR/192",
                            "http://id.eaufrance.fr/GPR/191",
                            "http://id.eaufrance.fr/GPR/166",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/47"
                        ],
                        "code_unite": "173",
                        "symbole_unite": "mg(NO3)/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/173",
                        "code_remarque": "1",
                        "mnemo_remarque": "Résultat > seuil de quantification et < au seuil de saturation ou Résultat = 0",
                        "code_insitu": "2",
                        "libelle_insitu": "Laboratoire",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    },
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "23",
                        "libelle_fraction": "Eau brute",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/23",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1311",
                        "libelle_parametre": "O2 dissous",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1311",
                        "resultat": 8.9,
                        "code_groupe_parametre": [
                            "166",
                            "165",
                            "164",
                            "46"
                        ],
                        "libelle_groupe_parametre": [
                            "Paramètres de l'analyse régulière du contrôle de surveillance de l'état chimique des eaux souterraines",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Autres éléments minéraux"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/166",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/46"
                        ],
                        "code_unite": "175",
                        "symbole_unite": "mg(O2)/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/175",
                        "code_remarque": "1",
                        "mnemo_remarque": "Résultat > seuil de quantification et < au seuil de saturation ou Résultat = 0",
                        "code_insitu": "1",
                        "libelle_insitu": "In situ",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    }
                ]
            },
            status=206
        )

        # Analyses region 76 with date
        responses.add(
            responses.GET,
            ANALYSES_76_DATE_URL,
            json={
                "count": 3,
                "first": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc?code_region=76&page=1&size=1000",
                "last": "https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc?code_region=76&page=679301&size=1000",
                "prev": None,
                "next": None,
                "api_version": "1.1.0",
                "data": [
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "23",
                        "libelle_fraction": "Eau brute",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/23",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1305",
                        "libelle_parametre": "MES",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1305",
                        "resultat": 2,
                        "code_groupe_parametre": [
                            "192",
                            "191",
                            "165",
                            "164",
                            "32"
                        ],
                        "libelle_groupe_parametre": [
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau résiduaire",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau douce",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Physique"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/192",
                            "http://id.eaufrance.fr/GPR/191",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/32"
                        ],
                        "code_unite": "162",
                        "symbole_unite": "mg/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/162",
                        "code_remarque": "10",
                        "mnemo_remarque": "Résultat < au seuil de quantification",
                        "code_insitu": "2",
                        "libelle_insitu": "Laboratoire",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    },
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "3",
                        "libelle_fraction": "Phase aqueuse de l'eau (filtrée, centrifugée...)",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/3",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1340",
                        "libelle_parametre": "NO3-",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1340",
                        "resultat": 3,
                        "code_groupe_parametre": [
                            "193",
                            "192",
                            "191",
                            "166",
                            "165",
                            "164",
                            "47"
                        ],
                        "libelle_groupe_parametre": [
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau saline",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau résiduaire",
                            "Avis relatif aux limites de quantification des couples «paramètre-matrice» de l'agrément des laboratoires effectuant des analyses dans le domaine de l'eau et des milieux aquatiques, matrice Eau douce",
                            "Paramètres de l'analyse régulière du contrôle de surveillance de l'état chimique des eaux souterraines",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Paramètres azotés"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/193",
                            "http://id.eaufrance.fr/GPR/192",
                            "http://id.eaufrance.fr/GPR/191",
                            "http://id.eaufrance.fr/GPR/166",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/47"
                        ],
                        "code_unite": "173",
                        "symbole_unite": "mg(NO3)/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/173",
                        "code_remarque": "1",
                        "mnemo_remarque": "Résultat > seuil de quantification et < au seuil de saturation ou Résultat = 0",
                        "code_insitu": "2",
                        "libelle_insitu": "Laboratoire",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    },
                    {
                        "code_station": "04026200",
                        "libelle_station": "CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
                        "uri_station": "http://id.eaufrance.fr/STQ/04026200",
                        "code_support": "3",
                        "libelle_support": "Eau",
                        "uri_support": "http://id.eaufrance.fr/SUP/3",
                        "code_fraction": "23",
                        "libelle_fraction": "Eau brute",
                        "uri_fraction": "http://id.eaufrance.fr/FAN/23",
                        "date_prelevement": "2004-03-01",
                        "heure_prelevement": "09:00:00",
                        "date_analyse": "2004-03-01",
                        "heure_analyse": "09:00:00",
                        "code_parametre": "1311",
                        "libelle_parametre": "O2 dissous",
                        "uri_parametre": "http://id.eaufrance.fr/PAR/1311",
                        "resultat": 8.9,
                        "code_groupe_parametre": [
                            "166",
                            "165",
                            "164",
                            "46"
                        ],
                        "libelle_groupe_parametre": [
                            "Paramètres de l'analyse régulière du contrôle de surveillance de l'état chimique des eaux souterraines",
                            "Paramètres physico-chimiques pour les plans d'eau",
                            "Paramètres physico-chimiques pour les cours d'eau",
                            "Autres éléments minéraux"
                        ],
                        "uri_groupe_parametre": [
                            "http://id.eaufrance.fr/GPR/166",
                            "http://id.eaufrance.fr/GPR/165",
                            "http://id.eaufrance.fr/GPR/164",
                            "http://id.eaufrance.fr/GPR/46"
                        ],
                        "code_unite": "175",
                        "symbole_unite": "mg(O2)/L",
                        "uri_unite": "http://id.eaufrance.fr/URF/175",
                        "code_remarque": "1",
                        "mnemo_remarque": "Résultat > seuil de quantification et < au seuil de saturation ou Résultat = 0",
                        "code_insitu": "1",
                        "libelle_insitu": "In situ",
                        "code_difficulte_analyse": "0",
                        "mnemo_difficulte_analyse": "Difficultés inconnues",
                        "limite_detection": None,
                        "limite_quantification": None,
                        "limite_saturation": None,
                        "incertitude_analytique": -2147483648,
                        "code_methode_fractionnement": "0",
                        "nom_methode_fractionnement": "Méthode inconnue",
                        "uri_methode_fractionnement": "http://id.eaufrance.fr/MET/0",
                        "code_methode_analyse": "0",
                        "nom_methode_analyse": "Méthode inconnue",
                        "uri_methode_analyse": "http://id.eaufrance.fr/MET/0",
                        "rendement_extraction": None,
                        "code_methode_extraction": None,
                        "nom_methode_extraction": None,
                        "uri_methode_extraction": None,
                        "code_accreditation": "0",
                        "mnemo_accreditation": "Inconnu",
                        "agrement": "0",
                        "code_statut": "3",
                        "mnemo_statut": "Donnée contrôlée niveau 2 (données validées)",
                        "code_qualification": "1",
                        "libelle_qualification": "Correcte",
                        "commentaires_analyse": None,
                        "commentaires_resultat_analyse": None,
                        "code_reseau": "0500000148",
                        "nom_reseau": "Réseau Complémentaire Départemental de suivi de la qualité des eaux superficielles de la Lozère (48)",
                        "uri_reseau": "http://id.eaufrance.fr/DC/0500000148",
                        "code_producteur": "22480001100013",
                        "nom_producteur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_producteur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_preleveur": "22480001100013",
                        "nom_preleveur": "CONSEIL DÉPARTEMENTAL DE LOZÈRE",
                        "uri_preleveur": "http://id.eaufrance.fr/INT/22480001100013",
                        "code_laboratoire": "22480001100021",
                        "nom_laboratoire": "Laboratoire départemental d'analyses de la Lozère",
                        "uri_laboratoire": "http://id.eaufrance.fr/INT/22480001100021"
                    }
                ]
            },
            status=206
        )

    @responses.activate
    def test_sync_stations(self):

        # Empty DB
        self.assertEqual(Station.objects.count(), 0)

        # 1. Create
        payload = {
            "asked_operation": "SYNC_STATIONS",
            "region_code": 76
        }

        response = self.client.post(self.sync_entities_api_url, data=payload)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'asked_operation': 'SYNC_STATIONS',
            'region_code': 76,
            'entities_found': 4,
            'entities_created': 4,
            'entities_failed_to_create': 0,
            'entities_failed_to_create_or_update': 0,
            'entities_updated': 0,
            'date_debut_prelevement': None
        }
        )

        self.assertEqual(Station.objects.count(), 4)

        # 2. Update
        payload = {
            "asked_operation": "SYNC_STATIONS",
            "region_code": 76
        }

        response = self.client.post(self.sync_entities_api_url, data=payload)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'asked_operation': 'SYNC_STATIONS',
            'region_code': 76,
            'entities_found': 4,
            'entities_created': 0,
            'entities_failed_to_create': 0,
            'entities_failed_to_create_or_update': 0,
            'entities_updated': 4,
            'date_debut_prelevement': None
        }
        )

    @responses.activate
    def test_sync_analyses(self):

        # Empty DB
        self.assertEqual(Station.objects.count(), 0)
        self.assertEqual(Analyse.objects.count(), 0)

        # 1. Create stations
        payload = {
            "asked_operation": "SYNC_STATIONS",
            "region_code": 76
        }

        response = self.client.post(self.sync_entities_api_url, data=payload)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'asked_operation': 'SYNC_STATIONS',
            'region_code': 76,
            'entities_found': 4,
            'entities_created': 4,
            'entities_failed_to_create': 0,
            'entities_failed_to_create_or_update': 0,
            'entities_updated': 0,
            'date_debut_prelevement': None
        }
        )

        self.assertEqual(Station.objects.count(), 4)
        self.assertEqual(Analyse.objects.count(), 0)

        # 2. Create analyses
        payload = {
            "asked_operation": "SYNC_ANALYSES",
            "region_code": 76,
            "date_debut_prelevement": "2004-03-01"
        }

        response = self.client.post(self.sync_entities_api_url, data=payload)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'asked_operation': 'SYNC_ANALYSES',
            'region_code': 76,
            'entities_found': 3,  # ANALYSES_76_DATE_URL with count = 3
            'entities_created': 3,
            'entities_failed_to_create': 0,
            'entities_failed_to_create_or_update': 0,
            'entities_updated': 0,
            'date_debut_prelevement': "2004-03-01"
        }
        )

        self.assertEqual(Station.objects.count(), 4)
        self.assertEqual(Analyse.objects.count(), 3)

    def test_invalid_asked_operation(self):

        #
        payload = {
            "asked_operation": "SYNC_ALL",
        }

        response = self.client.post(self.sync_entities_api_url, data=payload)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "asked_operation": [
                "\"SYNC_ALL\" is not a valid choice."
            ],
            "region_code": [
                "This field is required."
            ]
        })
