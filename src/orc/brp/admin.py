from django.contrib import admin

from .models import NatuurlijkPersoon


@admin.register(NatuurlijkPersoon)
class NatuurlijkPersoonAdmin(admin.ModelAdmin):
    list_display = ['bsn', 'naam', 'email', 'telefoonnummer']
