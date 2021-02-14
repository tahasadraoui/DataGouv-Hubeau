from django.test import TestCase

from datagouv.api.models import Station, Analyse


class AnalyseTestCase(TestCase):

    def setUp(self):

        super().setUp()

    def test_str_analyse(self):

        # Station
        station = Station.objects.create(
            code_station="04026200",
            libelle_station="CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
            code_departement="48",
            code_region="76",
            libelle_region="OCCITANIE",
            uri_station="http://id.eaufrance.fr/STQ/04026200"
        )
    
        # Analyse
        analyse = Analyse.objects.create(
            station=station,
            nom_producteur="FEDERATION DE LA GIRONDE POUR LA PECHE ET LA PROTECTION DU MILIEU AQUATIQUE",
            code_producteur="78184958300021",
            nom_reseau=None,
            code_reseau=None,
            incertitude_analytique=0,
            resultat=104,
            date_prelevement="2018-03-15",
            heure_prelevement="09:35:00",
            date_analyse="2018-03-18",
            heure_analyse="12:35:00"
        )

        self.assertEqual(analyse.__str__(), "Analyse sur la station 04026200, producteur FEDERATION DE LA GIRONDE POUR LA PECHE ET LA PROTECTION DU MILIEU AQUATIQUE, sur le réseau None, la date de 2018-03-18 12:35:00")
