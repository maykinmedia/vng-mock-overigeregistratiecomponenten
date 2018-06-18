from django.contrib.postgres.fields import JSONField
from django.db import models


class DomeinData(models.Model):
    data = JSONField()

    class Meta:
        verbose_name = 'domeindata'
        verbose_name_plural = 'domeindata'

    def __str__(self) -> str:
        if isinstance(self.data, dict):
            return str(list(self.data.keys))[:50]
        return str(self.data)[:50]


class Adres(models.Model):
    straatnaam = models.CharField(
        max_length=50, help_text='De officiële straatnaam zoals door het bevoegd gemeentelijk orgaan is vastgesteld, '
                                 'zo nodig ingekort conform de specificaties van de NEN 5825.'
    )
    postcode = models.CharField(max_length=7)
    woonplaatsnaam = models.CharField(max_length=80)
    huisnummer = models.CharField(max_length=5)
    huisletter = models.CharField(max_length=1, blank=True)
    huisnummertoevoeging = models.CharField(max_length=4, blank=True)

    class Meta:
        verbose_name = 'Adres'
        verbose_name_plural = 'Adressen'

    def __str__(self):
        return f"{self.straatnaam} {self.huisnummer}, {self.postcode} {self.woonplaatsnaam}"


class VerblijfsObject(models.Model):
    """
    Minimale modellering van een adres.
    """
    identificatie = models.CharField(max_length=50)
    hoofdadres = models.ForeignKey('Adres', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Verblijfsobject'
        verbose_name_plural = 'Verblijfsobjecten'

    def __str__(self):
        return self.identificatie
