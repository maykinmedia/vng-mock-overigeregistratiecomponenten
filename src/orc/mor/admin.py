from django.contrib import admin

from .models import MeldingOpenbareRuimte


@admin.register(MeldingOpenbareRuimte)
class MeldingOpenbareRuimteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uuid')
