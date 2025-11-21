from django.db import models


class MediosDeObra(models.Model):
    Codigo = models.CharField( max_length=5)
    NombreMedio = models.CharField( max_length=100)
    Activo = models.BigIntegerField( default= True)

    class Meta:
        verbose_name = "Medio Obra"
        verbose_name_plural = "Medios Obras"

    def __str__(self):
        return self.Nombre