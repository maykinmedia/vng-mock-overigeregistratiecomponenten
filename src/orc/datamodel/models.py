import uuid as _uuid

from django.db import models


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


class NietNatuurlijkPersoon(models.Model):
    uuid = models.UUIDField(default=_uuid.uuid4)

    rsin = models.CharField(
        max_length=17,  # BsVesNummerOfId
        help_text='Het door een kamer toegekend uniek nummer voor de '
                  'INGESCHREVEN NIET-NATUURLIJK PERSOON',
    )
    statutaire_naam = models.TextField(
        max_length=500, blank=True,
        help_text='Naam van de niet-natuurlijke persoon zoals deze is '
                  'vastgelegd in de statuten (rechtspersoon) of in de '
                  'vennootschapsovereenkomst is overeengekomen (Vennootschap '
                  'onder firma of Commanditaire vennootschap).'
    )
    datum_aanvang = models.DateField(
        help_text='De datum van aanvang van de NIET-NATUURLIJK PERSOON'
    )
    datum_beeindiging = models.DateField(
        null=True, blank=True,
        help_text='De datum van beëindiging van de NIET-NATUURLIJK PERSOON.'
    )

    class Meta:
        verbose_name = "niet-natuurlijk persoon"
        verbose_name_plural = "niet-natuurlijke personen"

    def __str__(self):
        return f"{self.rsin}"
