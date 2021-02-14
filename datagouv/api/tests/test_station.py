from django.test import TestCase

from datagouv.api.models import Station


class StationTestCase(TestCase):

    def setUp(self):

        super().setUp()

    def test_str_station(self):

        station = Station.objects.create(
            code_station="04026200",
            libelle_station="CHAPEAUROUX à CHATEAUNEUF-DE-RANDON",
            code_departement="48",
            code_region="76",
            libelle_region="OCCITANIE",
            uri_station="http://id.eaufrance.fr/STQ/04026200"
        )

        self.assertEqual(station.__str__(), "Code station de mesures: 04026200, Libelle CHAPEAUROUX à CHATEAUNEUF-DE-RANDON, Région OCCITANIE")
