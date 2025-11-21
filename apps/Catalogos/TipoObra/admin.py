from django.contrib import admin
from .models import TiposDeObra

@admin.register(TiposDeObra)
class TiposDeObraAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'NombreTipo', 'Activo')
    search_fields = ('Codigo', 'NombreTipo')
    list_filter = ('Activo',)
    ordering = ('Codigo',)
