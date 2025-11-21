from django.db import models

class Artista(models.Model):
    Nombre = models.CharField( max_length=100)
    Apellido = models.CharField( max_length=100)
    Cedula = models.CharField( max_length=39)
    Telefono = models.CharField( max_length=20)
    FechaNaciminiento = models.DateField()
    Correo = models.CharField(max_length=100)
    Referencia = models.CharField( max_length=200)
    Activo = models.BigIntegerField( default= True)
        




def __str__(self):
    return f"{self.Nombre} {self.Apellido}"

