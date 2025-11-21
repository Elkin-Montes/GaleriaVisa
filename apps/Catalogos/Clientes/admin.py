from django.contrib import admin
from .models import Clientes

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'Cedula', 'Correo', 'Telefono', 'Activo')
    search_fields = ('Nombre', 'Apellido', 'Cedula', 'Correo', 'Telefono')
    list_filter = ('Activo',)
    ordering = ('Apellido', 'Nombre')
