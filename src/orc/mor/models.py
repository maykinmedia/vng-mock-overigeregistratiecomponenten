import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class MeldingOpenbareRuimte(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)

    hoofdcategorie = models.CharField(max_length=255)
    subcategorie = models.CharField(max_length=255)

    locatie_beschrijving = models.TextField(blank=True, help_text="Aanvullende omschrijving locatie")

    # overige (ongestructureerde) data
    data = JSONField(default=dict)

    class Meta:
        verbose_name = "melding openbare ruimte"
        verbose_name_plural = "meldingen openbare ruimte"

    def __str__(self):
        return f"Melding {self.hoofdcategorie}/{self.subcategorie}"
