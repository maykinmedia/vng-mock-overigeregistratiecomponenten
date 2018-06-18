from django.contrib import admin

from .models import DomeinData


@admin.register(DomeinData)
class DomeinDataAdmin(admin.ModelAdmin):
    list_display = ['__str__']
