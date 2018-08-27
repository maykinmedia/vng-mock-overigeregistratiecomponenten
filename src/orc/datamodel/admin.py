from django.contrib import admin

from .models import Adres, NietNatuurlijkPersoon, VerblijfsObject


@admin.register(Adres)
class AdresAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(VerblijfsObject)
class VerblijfsObjectAdmin(admin.ModelAdmin):
    list_display = ['identificatie', 'hoofdadres']
    list_select_related = ('hoofdadres',)


@admin.register(NietNatuurlijkPersoon)
class NietNatuurlijkPersoonAdmin(admin.ModelAdmin):
    list_display = ['__str__']
