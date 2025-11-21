from django.contrib import admin
from .models import Vendedor

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'Cedula', 'Telefono', 'FechaNaciminiento', 'Correo', 'Activo')
    search_fields = ('Nombre', 'Apellido', 'Cedula', 'Correo')
    list_filter = ('Activo',)
    ordering = ('Apellido', 'Nombre')


