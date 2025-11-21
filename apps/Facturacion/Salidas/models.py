from django.db import models
from apps.Catalogos.Clientes.models import Clientes
from apps.Administracion.Vendedores.models import Vendedor
from apps.Inventario.Obras.models import Obras

class Factura(models.Model):
    IdCliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    IdVendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    Estado = models.CharField(max_length=20)
    Total = models.DecimalField( max_digits=12, decimal_places=2)
    FechaCreacion = models.DateField(auto_now_add=True)
    Activo = models.BigIntegerField( default= True)
    
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f"{self.Estado} ({self.FechaCreacion})"


class DetalleFactura(models.Model):
    IdFactura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    IdObra = models.ForeignKey(Obras, on_delete=models.PROTECT)
    Precio = models.DecimalField(max_digits=12, decimal_places=2)
    Activo = models.BooleanField( default=True)    
    
    class Meta:
        verbose_name = "DetalleFactura"
        verbose_name_plural = "DetallesFacturas"



