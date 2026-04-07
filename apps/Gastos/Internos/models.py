from django.db import models
from apps.Inventario.Obras.models import Obras
from apps.Eventos.Exposicion.models import Exposicion
from apps.Seguridad.Usuarios.models import User

#si hay error, revisar el "responsable", no se si esta bien implementado.

class GastoInterno(models.Model):
    Descripcion = models.CharField(max_length=200)
    Tipo_Gasto = models.CharField(max_length=100,verbose_name="Tipo de Gasto", help_text="Ejemplo: Materiales, Servicios, etc.")
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha = models.DateField(verbose_name="Fecha del Gasto")

    Exposicion = models.ForeignKey(Exposicion, on_delete=models.PROTECT, null=True, blank=True,
                                related_name='gastos', verbose_name="Exposición Relacionada", 
                                help_text="Seleccione la exposición relacionada con este gasto, si aplica.")
    
    Obras = models.ManyToManyField(Obras, blank=True, related_name='gastos', verbose_name="Obras Relacionadas",
                                help_text="Seleccione las obras relacionadas con este gasto, si aplica.")

    FechaCreacion = models.DateTimeField(auto_now_add=True) 
    Responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Responsable del Gasto",
                                help_text="Seleccione el usuario responsable de este gasto.")
    Activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gasto Interno"
        verbose_name_plural = "Gastos Internos"
    
    def __str__(self):
        return self.Descripcion
