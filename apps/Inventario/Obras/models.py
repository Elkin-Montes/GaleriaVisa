from django.db import models
from apps.Catalogos.Artistas.models import Artista
from apps.Catalogos.EstiloObra.models import EstilosDeObra
from apps.Catalogos.MedioObra.models import MediosDeObra
from apps.Catalogos.TipoObra.models import TiposDeObra
from apps.Catalogos.Propietario.models import Propietario

class Obras(models.Model):
    Titulo = models.CharField(max_length=150)
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
        return f"{self.Titulo} ({self.Fue_vendida})"