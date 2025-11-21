from django.db import models

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
