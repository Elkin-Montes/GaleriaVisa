from django.db import models
from apps.Catalogos.Artistas.models import Artista
from apps.Catalogos.EstiloObra.models import EstilosDeObra
from apps.Catalogos.MedioObra.models import MediosDeObra
from apps.Catalogos.TipoObra.models import TiposDeObra
from apps.Catalogos.Propietario.models import Propietario
#from apps.Facturacion.Salidas.models import Factura, DetalleFactura

class Obras(models.Model):
    Titulo = models.CharField(max_length=150)
    Descripcion = models.TextField(null = True, blank = True)
    Estado = models.CharField(choices=[('disponible', 'Disponible'),('exhibicion', 'En exhibición'), ('vendida', 'Vendida')], max_length=20, default='disponible')
    IdArtista = models.ForeignKey(Artista,on_delete=models.PROTECT)
    IdEstilo = models.ForeignKey(EstilosDeObra,on_delete=models.PROTECT)
    IdMedio = models.ForeignKey(MediosDeObra, on_delete=models.PROTECT)
    IdTipoObra = models.ForeignKey(TiposDeObra, on_delete=models.PROTECT)
    IdPropietario = models.ForeignKey(Propietario, on_delete=models.PROTECT)
    PrecioSugerido = models.DecimalField(max_digits=10, decimal_places=2)
    FueVendida = models.BooleanField(default=False)
    PrecioVenta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Activo = models.BigIntegerField( default= True)

    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"

    def __str__(self):
        return f"{self.Titulo} ({self.FueVendida})"
    

#estos campos permitien la conexion de obras con factura, para que obras tenga precio de venta
#  y estado de vendida, sin necesidad de agregar campos a la tabla obras,
#  y sin necesidad de hacer consultas adicionales a la tabla factura para saber si una obra esta vendida o no.
# por ahora permanece desabilitada.
#7/4/26

    #@property
    #def esta_vendida(self):
    #   return self.DetalleFactura_set.exists()
    
    # @property
    #def precio_venta(self):
    #    detalle = self.DetalleFactura_set.first()
    #    return detalle.Precio if detalle else None