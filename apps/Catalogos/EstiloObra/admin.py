from django.contrib import admin
from .models import EstilosDeObra

@admin.register(EstilosDeObra)
class EstilosDeObraAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'NombreEstilo', 'Activo')
    search_fields = ('NombreEstilo',)
    list_filter = ('Activo',)
    ordering = ('Codigo',)

