from django.contrib import admin

from .models import InzageVerzoek


@admin.register(InzageVerzoek)
class InzageVerzoekAdmin(admin.ModelAdmin):
    list_display = ['uuid',]
