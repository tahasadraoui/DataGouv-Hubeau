from django.db import models

from safedelete.models import SafeDeleteModel

from safedelete.config import HARD_DELETE

# Constantes associées au modèle
SHORT_VARCHAR_SIZE = 50
MAXIMUM_CODE_SIZE = 200
DEFAULT_VARCHAR_SIZE = 255


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
        Station
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
        return f"Code station: {self.code}, Libelle {self.libelle}, Code région {self.code_region}"
