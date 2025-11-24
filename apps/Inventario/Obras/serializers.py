from rest_framework.serializers import ModelSerializer
from .models import Obras

class ObrasSerializer(ModelSerializer):
    class Meta:
        model = Obras
        fields = ('Titulo', 'IdArtista', 'IdEstilo', 'IdMedio', 'IdTipoObra', 'IdPropietario', 'PrecioSugerido', 'FueVendida', 'PrecioVenta')