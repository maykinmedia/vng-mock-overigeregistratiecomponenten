"""
Tijdelijke implementatie van datamodellen voor Basisregistratie personen (BRP).
"""
import uuid

from django.db import models


class InzageVerzoek(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)

    inzage_wmo = models.BooleanField(
        help_text='Indicatie Inzage WMO'
    )
    inzage_jeugd = models.BooleanField(
        help_text='Indicatie Inzage Jeugd'
    )
    inzage_participatie = models.BooleanField(
        help_text='Indicatie Inzage Participatie'
    )
    inzage_veiligheidskamer = models.BooleanField(
        help_text='Indicatie Inzage Veiligheidskamer'
    )
    inzage_schuldhulpverlening = models.BooleanField(
        help_text='Indicatie Inzage Schuldhulpverlening'
    )
    inzage_overige_regelingen = models.BooleanField(
        help_text='Indicatie Inzage Overige regelingen'
    )
    onderwerp_overige_regelingen = models.CharField(
        max_length=200, blank=True,
        help_text='Onderwerp bij Overige Regelingen'
    )
    inzage_algemeen = models.BooleanField(
        help_text='Indicatie Inzage Algemeen'
    )
    reden_inzage_algemeen = models.CharField(
        max_length=200, blank=True,
        help_text='Reden Algemeen'
    )
    antwoord_per_email = models.BooleanField(
        help_text='Indicatie Antwoord per e-mail'
    )

    class Meta:
        verbose_name = "inzage verzoek"
        verbose_name_plural = "inzage verzoeken"

    def __str__(self):
        return f"{self.uuid}"
