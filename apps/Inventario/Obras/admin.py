from django.contrib import admin
from .models import Obras

@admin.register(Obras)
class ObrasAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'IdArtista', 'IdEstilo', 'IdMedio','IdTipoObra', 'IdPropietario', 'PrecioSugerido', 'FueVendida', 'PrecioVenta', 'Activo')
    search_fields = ('Titulo', 'IdArtista__nombre', 'IdPropietario__nombre')
    list_filter = ('Activo','FueVendida','PrecioSugerido')
    ordering = ('Titulo',)