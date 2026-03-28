from django.db import models

class GastoInterno(models.Model):
    Descripcion = models.CharField(max_length=200)
    Tipo_Gasto = models.CharField(max_length=100)
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha = models.DateField()
    FechaCreacion = models.DateTimeField(auto_now_add=True) 
    Responsable = models.CharField(max_length=100)
    Activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gasto Interno"
        verbose_name_plural = "Gastos Internos"
    
    def __str__(self):
        return self.Descripcion
