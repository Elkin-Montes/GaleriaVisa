from django.contrib import admin
from .models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('IdCliente', 'IdVendedor', 'Estado', 'Total', 'FechaCreacion', 'Activo')
    search_fields = ('IdCliente__Nombre', 'IdVendedor__Nombre', 'Estado')
    list_filter = ('Estado', 'Activo', 'FechaCreacion')
    ordering = ('FechaCreacion',)