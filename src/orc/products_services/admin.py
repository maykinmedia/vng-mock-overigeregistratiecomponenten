from django.contrib import admin

from .models import ProductOfDienst


@admin.register(ProductOfDienst)
class ProductOfDienstAdmin(admin.ModelAdmin):
    list_display = ('naam', 'uuid', 'webpagina')
