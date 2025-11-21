from django.contrib import admin
from .models import MediosDeObra

@admin.register(MediosDeObra)
class MediosDeObraAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'NombreMedio', 'Activo')
    search_fields = ('NombreMedio',)
    list_filter = ('Activo',)
    ordering = ('Codigo',)


