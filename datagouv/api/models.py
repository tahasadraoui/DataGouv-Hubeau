from django.db import models

from safedelete.models import SafeDeleteModel

from safedelete.config import HARD_DELETE

# Constantes associées au modèle
SHORT_CHAR_SIZE = 20
MAXIMUM_CODE_SIZE = 200


class DataGouvModel(SafeDeleteModel):
    id = models.AutoField(primary_key=True)
    _safedelete_policy = HARD_DELETE

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Station(DataGouvModel):
    """
        Stations (lieux de mesures physiochimiques) sur les cours d'eau ou plans d'eau,
        où des prélèvements d'eau ont eu lieu,
        en vue de faire des analyses de la qualité de l'eau
    """

    code = models.CharField(max_length=MAXIMUM_CODE_SIZE, unique=True, help_text="Identifiant de la station de mesure dans le référentiel national Sandre")
    libelle = models.CharField(max_length=MAXIMUM_CODE_SIZE, help_text="Libellé national de la station de mesure")
    code_departement = models.CharField(max_length=MAXIMUM_CODE_SIZE, help_text="Code INSEE du département")
    region_code = models.CharField(max_length=MAXIMUM_CODE_SIZE, help_text="Code INSEE du département")
    libelle_region = models.CharField(max_length=MAXIMUM_CODE_SIZE, help_text="Nom du département")
    longitude = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE)
    longitude = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE)
    date_debut_prelevement = models.DateField()
    date_fin_prelevement = models.DateField()
    nature = models.DateField(help_text="Nature de la station de mesure")

    def __str__(self):
        return f"Code station de mesures: {self.code}, Libelle {self.libelle}, Code région {self.region_code}"


class Analyse(DataGouvModel):
    """
        Permet de rechercher les analyses physico-chimiques effectuées sur les échantillons confectionnés,
        lors des opérations de prélèvement sur les différentes stations.
        (conductivité, nitrates, substances pesticides ..)
    """

    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    nom_producteur = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    code_producteur = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    nom_reseau = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    code_reseau = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    incertitude_analytique = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE)
    resultat = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE, help_text="Résultat de l'analyse physico-chimique et microbiologique")
    date_prelevement = models.DateField(help_text="Date du début du prélèvement d'échantillons")
    heure_prelevement = models.TimeField(help_text="Heure du début du prélèvement d'échantillon")
    date_analyse = models.DateField(help_text="Date de l'analyse physico-chimique et microbiologique")
    heure_analyse = models.TimeField(help_text="Heure de l'analyse physico-chimique et microbiologique")

    def __str__(self):
        return f"Analyse sur la station {self.station.code}, producteur {self.nom_producteur},  sur le réseau {self.nom_reseau}"


class SyncEntities(DataGouvModel):

    class Meta:
        managed = False

    SYNC_STATIONS = 'SYNC_STATIONS'
    SYNC_ANALYSES = 'SYNC_ANALYSES'
    SYNC_ALL = 'SYNC_ALL'
    SYNC_CHOICES = (
        (SYNC_STATIONS, 'Sync stations'),
        (SYNC_ANALYSES, 'Sync analyses'),
        (SYNC_ALL, 'Sync all'),
    )

    asked_operation = models.CharField(choices=SYNC_CHOICES, max_length=SHORT_CHAR_SIZE, default=SYNC_STATIONS)
    region_code = models.CharField(max_length=SHORT_CHAR_SIZE, blank=True, null=True)
    stations_found = models.IntegerField(blank=True, null=True)
    analyses_found = models.IntegerField(blank=True, null=True)
