from django.db import models

class EstilosDeObra(models.Model):
    Codigo = models.CharField( max_length=5)
    NombreEstilo = models.CharField( max_length=100)
    Activo = models.BigIntegerField( default= True)

    class Meta:
        verbose_name = "Estilo Obra"
        verbose_name_plural = "Estilos Obras"

    def __str__(self):
        return self.Nombre