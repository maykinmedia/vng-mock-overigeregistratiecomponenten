# inspired by: https://www.amsterdam.nl/bestuur-organisatie/organisatie/dienstverlening/basisinformatie/basisinformatie/producten-diensten/  # noqa
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductOfDienst(models.Model):
    uuid = models.UUIDField(_("uuid"), unique=True, default=uuid.uuid4)
    naam = models.CharField(_("naam"), max_length=80)
    omschrijving = models.TextField(_("omschrijving"), blank=True)
    webpagina = models.URLField(_("webpagina"), blank=True)

    class Meta:
        verbose_name = _("product of dienst")
        verbose_name_plural = _("producten en diensten")

    def __str__(self):
        return self.naam
