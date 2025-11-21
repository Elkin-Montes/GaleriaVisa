from django.db import models

class Vendedor(models.Model):
    Nombre = models.CharField( max_length=100)
    Apellido = models.CharField( max_length=100)
    Cedula = models.CharField(max_length=39)
    Telefono = models.CharField(max_length=20)
    FechaNaciminiento = models.DateField()
    Correo = models.CharField(max_length=100)
    RFC = models.CharField( max_length=9)
    Activo = models.BigIntegerField( default= True)

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"



