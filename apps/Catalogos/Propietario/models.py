from django.db import models

class Propietario(models.Model):
    Nombre = models.CharField( max_length=100)
    Apellido = models.CharField( max_length=100)
    Cedula = models.CharField( max_length=39)
    Correo = models.CharField( max_length=100)
    Telefono = models.CharField( max_length=20)
    Activo = models.BigIntegerField( default= True)


class Meta:
    verbose_name = "Propietario"
    verbose_name_plural = "Propietarios"

def __str__(self):
    return f"{self.Nombre} {self.Apellido}"
