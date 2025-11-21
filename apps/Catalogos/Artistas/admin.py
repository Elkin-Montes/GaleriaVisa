from django.contrib import admin
from .models import Artista

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'Cedula', 'Telefono', 'FechaNaciminiento', 'Correo', 'Referencia', 'Activo')
    search_fields = ('Nombre', 'Apellido', 'Cedula', 'Correo')
    list_filter = ('Activo',)
    ordering = ('Apellido', 'Nombre')
