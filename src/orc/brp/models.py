"""
Tijdelijke implementatie van datamodellen voor Basisregistratie personen (BRP).
"""
import uuid

from django.db import models

from zds_schema.fields import BSNField


class NatuurlijkPersoon(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)

    naam = models.CharField(max_length=200)
    bsn = BSNField()
    telefoonnummer = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "natuurlijk persoon"
        verbose_name_plural = "natuurlijke personen"

    def __str__(self):
        return f"{self.bsn}"
