from django.test import TestCase

from rest_framework.test import APIClient

from datagouv.api.views import MetricsViewSet
from datagouv.api.models import Analyse, Station


class MetricsTestCase(TestCase):

    maxDiff = None

    def setUp(self):

        super().setUp()

        # Client
        self.client = APIClient()

        # URLs
        self.metrics_api_url = "/api/metrics/"

        # View
        self.metrics_create_view = MetricsViewSet.as_view(actions={'post': 'create'})

        # Stations
        self.allier_station = Station.objects.create(
            code_station="04026950",
            libelle_station="ALLIER à LANGOGNE",
            code_departement=48,
            code_region=76,
            libelle_region="OCCITANIE",
            uri_station="http://id.eaufrance.fr/STQ/04026950"
        )

        self.chapeauroux_station = Station.objects.create(
            code_station="04027225",
            libelle_station="CHAPEAUROUX à AUROUX",
            code_departement=48,
            code_region=76,
            libelle_region="OCCITANIE",
            uri_station="http://id.eaufrance.fr/STQ/04027225"
        )

        self.st_denis_station = Station.objects.create(
            code_station="05061200",
            libelle_station="La Tourmente au niveau de St-Denis-lès-Martel",
            code_departement=46,
            code_region=76,
            libelle_region="OCCITANIE",
            uri_station="http://id.eaufrance.fr/STQ/05061200"
        )

        self.condat_station = Station.objects.create(
            code_station="05061228",
            libelle_station="La Tourmente à Condat",
            code_departement=46,
            code_region=75,
            libelle_region="OCCITANIE",
            uri_station="http://id.eaufrance.fr/STQ/05061228"
        )

        # Analyses
        # Allier, region 76, dep 48
        # incertitude_analytique 30.0, resultat 0.40
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="30.0000",
            resultat="0.4000",
            date_prelevement="2020-06-02",
            heure_prelevement="09:57:00",
            date_analyse="2020-06-03",
            heure_analyse="04:01:00",
            station=self.allier_station
        )

        # incertitude_analytique 25.0, resultat 0.5
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="25.0000",
            resultat="0.5000",
            date_prelevement="2020-06-02",
            heure_prelevement="09:57:00",
            date_analyse="2020-06-02",
            heure_analyse="23:14:00",
            station=self.allier_station
        )

        # Chapeauroux, region 76, dep 48
        # incertitude_analytique 40.0, resultat 0.15
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="40.0000",
            resultat="0.1500",
            date_prelevement="2020-06-09",
            heure_prelevement="09:00:00",
            date_analyse="2020-06-10",
            heure_analyse="04:01:00",
            station=self.chapeauroux_station
        )

        # incertitude_analytique 10.0, resultat 21.0
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="10.0000",
            resultat="21.0000",
            date_prelevement="2020-06-02",
            heure_prelevement="09:57:00",
            date_analyse="2020-06-02",
            heure_analyse="23:14:00",
            station=self.chapeauroux_station
        )

        # St Denis, region 76, dep 46
        # incertitude_analytique 37.0, resultat 0.29
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="37.0000",
            resultat="0.2900",
            date_prelevement="2020-06-02",
            heure_prelevement="09:57:00",
            date_analyse="2020-06-03",
            heure_analyse="04:01:00",
            station=self.st_denis_station
        )

        # incertitude_analytique 15.0, resultat 8.90
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="15.0000",
            resultat="8.9000",
            date_prelevement="2020-06-02",
            heure_prelevement="09:57:00",
            date_analyse="2020-06-02",
            heure_analyse="23:14:00",
            station=self.st_denis_station
        )

        # Condat, region 75, dep 46
        # incertitude_analytique 35.0, resultat 0.004
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="35.0000",
            resultat="0.0040",
            date_prelevement="2020-06-02",
            heure_prelevement="09:57:00",
            date_analyse="2020-06-03",
            heure_analyse="04:01:00",
            station=self.condat_station
        )

        # incertitude_analytique 5.0000, resultat 0.018
        Analyse.objects.create(
            nom_producteur="AGENCE DE L'EAU LOIRE-BRETAGNE",
            code_producteur="18450301900012",
            nom_reseau="Réseau de référence pérenne de la qualité des cours d'eau du bassin  Loire, cours d'eau côtiers vendéens et bretons",
            code_reseau="0400000943",
            incertitude_analytique="5.0000",
            resultat="0.0180",
            date_prelevement="2020-06-02",
            heure_prelevement="09:57:00",
            date_analyse="2020-06-02",
            heure_analyse="23:14:00",
            station=self.condat_station
        )

    def test_no_region_code(self):

        response = self.client.post(self.metrics_api_url)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 201)
        data = response.json()

        # Dep 48 avg result, 0.40 + 0.5 + 0.15 + 21.0 --> 22.5 / 4 --> 5.5125
        # Dep 46 avg result, 0.29 + 8.90 + 0.004 + 0.018 --> 9.212 / 4 --> 2.303
        self.assertEqual(data, {
            'best_stations': [
                {'id': self.chapeauroux_station.id, 'results_average': 10.575, 'code_station': '04027225', 'libelle_station': 'CHAPEAUROUX à AUROUX',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04027225'},
                {'id': self.st_denis_station.id, 'results_average': 4.595, 'code_station': '05061200', 'libelle_station': 'La Tourmente au niveau de St-Denis-lès-Martel',
                    'code_departement': 46, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/05061200'},
                {'id': self.allier_station.id, 'results_average': 0.45, 'code_station': '04026950', 'libelle_station': 'ALLIER à LANGOGNE',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04026950'},
                {'id': self.condat_station.id, 'results_average': 0.011, 'code_station': '05061228', 'libelle_station': 'La Tourmente à Condat',
                    'code_departement': 46, 'code_region': 75, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/05061228'}],
            'worst_stations': [
                {'id': self.condat_station.id, 'results_average': 0.011, 'code_station': '05061228', 'libelle_station': 'La Tourmente à Condat',
                    'code_departement': 46, 'code_region': 75, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/05061228'},
                {'id': self.allier_station.id, 'results_average': 0.45, 'code_station': '04026950', 'libelle_station': 'ALLIER à LANGOGNE',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04026950'},
                {'id': self.st_denis_station.id, 'results_average': 4.595, 'code_station': '05061200', 'libelle_station': 'La Tourmente au niveau de St-Denis-lès-Martel',
                    'code_departement': 46, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/05061200'},
                {'id': self.chapeauroux_station.id, 'results_average': 10.575, 'code_station': '04027225', 'libelle_station': 'CHAPEAUROUX à AUROUX',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04027225'}
            ],
            'average_results_by_departement': {'46': 2.303, '48': 5.5125}}
        )

    def test_with_region_code(self):

        payload = {
            "region_code": 76
        }

        response = self.client.post(self.metrics_api_url, data=payload)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 201)
        data = response.json()

        # Assert sans la station Condat --> 0.29 + 8.90 --> 9.19 / 2 --> 4.595
        self.assertEqual(data, {
            'best_stations': [
                {'id': self.chapeauroux_station.id, 'results_average': 10.575, 'code_station': '04027225', 'libelle_station': 'CHAPEAUROUX à AUROUX',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04027225'},
                {'id': self.st_denis_station.id, 'results_average': 4.595, 'code_station': '05061200', 'libelle_station': 'La Tourmente au niveau de St-Denis-lès-Martel',
                    'code_departement': 46, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/05061200'},
                {'id': self.allier_station.id, 'results_average': 0.45, 'code_station': '04026950', 'libelle_station': 'ALLIER à LANGOGNE',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04026950'},
            ],
            'worst_stations': [
                {'id': self.allier_station.id, 'results_average': 0.45, 'code_station': '04026950', 'libelle_station': 'ALLIER à LANGOGNE',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04026950'},
                {'id': self.st_denis_station.id, 'results_average': 4.595, 'code_station': '05061200', 'libelle_station': 'La Tourmente au niveau de St-Denis-lès-Martel',
                    'code_departement': 46, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/05061200'},
                {'id': self.chapeauroux_station.id, 'results_average': 10.575, 'code_station': '04027225', 'libelle_station': 'CHAPEAUROUX à AUROUX',
                    'code_departement': 48, 'code_region': 76, 'libelle_region': 'OCCITANIE', 'uri_station': 'http://id.eaufrance.fr/STQ/04027225'}
            ],
            'average_results_by_departement': {'46': 4.595, '48': 5.5125}}
        )
