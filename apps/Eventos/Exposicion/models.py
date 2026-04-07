from django.db import models
from apps.Inventario.Obras.models import Obras

class Exposicion(models.Model):
    Titulo = models.CharField(max_length=50)
    Lugar = models.CharField(max_length=50)
    Tematica = models.CharField(max_length=200, null=True, blank=True)
    FechaInicio = models.DateField()
    FechaFinalizacion = models.DateField()
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    Activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Exposición"
        verbose_name_plural = "Exposiciones"

    def __str__(self):
        return self.titulo
    
class ObrasEnExposicion(models.Model):
    Exposicion = models.ForeignKey(Exposicion, on_delete=models.PROTECT)
    Obra = models.ForeignKey(Obras, on_delete=models.PROTECT)
    Vendida = models.BooleanField(default=False)
    FechaExposicion = models.DateField()
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    Activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('Obra', 'Exposicion')
        verbose_name = "Obra en Exposición"
        verbose_name_plural = "Obras en Exposición"

    def __str__(self):
        return f"{self.Obra} en {self.Exposicion}"

Obra = models.ManyToManyField(
    Obras, through='ObrasEnExposicion', related_name='exposiciones_participadas')