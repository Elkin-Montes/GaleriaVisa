from django.db import models


class TiposDeObra(models.Model):
    Codigo = models.CharField( max_length=5)
    NombreTipo = models.CharField( max_length=100)
    Activo = models.BigIntegerField( default= True)
    
    class Meta:

        verbose_name = "Tipo Obra"
        verbose_name_plural = "Tipos Obras"

    def __str__(self):
        return self.Nombre