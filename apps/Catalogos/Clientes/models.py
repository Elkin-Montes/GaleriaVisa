from django.db import models

class Clientes(models.Model):
    Nombre = models.CharField( max_length=100)
    Apellido = models.CharField( max_length=100)
    Cedula = models.CharField( max_length=39)
    Correo = models.CharField( max_length=100)
    Telefono = models.CharField( max_length=20)
    Activo = models.BigIntegerField( default= True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"


