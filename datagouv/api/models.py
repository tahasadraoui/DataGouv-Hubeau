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

    code = models.CharField(max_length=MAXIMUM_CODE_SIZE, unique=True)
    libelle = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    code_departement = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    code_region = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    libelle_region = models.CharField(max_length=MAXIMUM_CODE_SIZE)
    longitude = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE, blank=True, null=True)
    date_debut_prelevement = models.DateField(blank=True, null=True)
    date_fin_prelevement = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Code station de mesures: {self.code}, Libelle {self.libelle}, Code région {self.code_region}"


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
    incertitude_analytique = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE, blank=True, null=True)
    resultat = models.DecimalField(max_digits=8, decimal_places=2, max_length=MAXIMUM_CODE_SIZE, blank=True, null=True)
    date_prelevement = models.DateField(blank=True, null=True)
    heure_prelevement = models.TimeField(blank=True, null=True)
    date_analyse = models.DateField(blank=True, null=True)
    heure_analyse = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"Analyse sur la station {self.station.code}, producteur {self.nom_producteur},  sur le réseau {self.nom_reseau}"


class SyncEntities(DataGouvModel):

    class Meta:
        managed = False
    
    SYNC_ALL = 'SYNC_ALL'
    SYNC_STATIONS = 'SYNC_STATIONS'
    SYNC_ANALYSES = 'SYNC_ANALYSES'
    SYNC_CHOICES = (
        (SYNC_ALL, 'Sync all'),
        (SYNC_STATIONS, 'Sync stations'),
        (SYNC_ANALYSES, 'Sync analyses'),
    )

    asked_operation = models.CharField(choices=SYNC_CHOICES, max_length=SHORT_CHAR_SIZE)
