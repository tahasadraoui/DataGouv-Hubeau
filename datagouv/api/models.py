from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from safedelete.config import HARD_DELETE
from safedelete.models import SafeDeleteModel

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

    code_station = models.CharField(max_length=MAXIMUM_CODE_SIZE, unique=True, help_text="Identifiant de la station de mesure dans le référentiel national Sandre")
    libelle_station = models.CharField(max_length=MAXIMUM_CODE_SIZE, help_text="Libellé national de la station de mesure")
    code_departement = models.CharField(max_length=MAXIMUM_CODE_SIZE, help_text="Code INSEE du département")
    code_region = models.IntegerField(help_text="Code INSEE du département", validators=[MinValueValidator(1), MaxValueValidator(200)])
    libelle_region = models.CharField(max_length=MAXIMUM_CODE_SIZE, help_text="Nom du département")
    uri_station = models.CharField(max_length=MAXIMUM_CODE_SIZE, blank=True, null=True)

    def __str__(self):
        return f"Code station de mesures: {self.code_station}, Libelle {self.libelle_station}, Région {self.libelle_region}"


class Analyse(DataGouvModel):
    """
        Permet de rechercher les analyses physico-chimiques effectuées sur les échantillons confectionnés,
        lors des opérations de prélèvement sur les différentes stations.
        (conductivité, nitrates, substances pesticides ..)
    """

    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    nom_producteur = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    code_producteur = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    nom_reseau = models.CharField(max_length=MAXIMUM_CODE_SIZE, blank=True, null=True)
    code_reseau = models.CharField(max_length=MAXIMUM_CODE_SIZE, blank=True, null=True)
    incertitude_analytique = models.IntegerField(blank=True, null=True)
    resultat = models.IntegerField(help_text="Résultat de l'analyse physico-chimique et microbiologique")
    date_prelevement = models.DateField(help_text="Date du début du prélèvement d'échantillons")
    heure_prelevement = models.TimeField(help_text="Heure du début du prélèvement d'échantillon")
    date_analyse = models.DateField(help_text="Date de l'analyse physico-chimique et microbiologique", blank=True, null=True)
    heure_analyse = models.TimeField(help_text="Heure de l'analyse physico-chimique et microbiologique", blank=True, null=True)

    def __str__(self):
        return f"Analyse sur la station {self.station.code_station}, producteur {self.nom_producteur}, sur le réseau {self.nom_reseau}, la date de {self.date_analyse} {self.heure_analyse}"


class SyncEntities(DataGouvModel):

    class Meta:
        managed = False

    GET_STATIONS = 'GET_STATIONS'
    SYNC_STATIONS = 'SYNC_STATIONS'
    GET_ANALYSES = 'GET_ANALYSES'
    SYNC_ANALYSES = 'SYNC_ANALYSES'
    SYNC_CHOICES = (
        (GET_STATIONS, 'Get stations'),
        (SYNC_STATIONS, 'Sync stations'),
        (GET_ANALYSES, 'Get analyses'),
        (SYNC_ANALYSES, 'Sync analyses'),
    )

    asked_operation = models.CharField(choices=SYNC_CHOICES, max_length=SHORT_CHAR_SIZE, default=GET_STATIONS)
    region_code = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    entities_found = models.IntegerField(blank=True, null=True)
    entities_created = models.IntegerField(blank=True, null=True)
    entities_failed_to_create = models.IntegerField(blank=True, null=True)
    entities_failed_to_create_or_update = models.IntegerField(blank=True, null=True)
    entities_updated = models.IntegerField(blank=True, null=True)
    date_debut_prelevement = models.DateField(blank=True, null=True)
