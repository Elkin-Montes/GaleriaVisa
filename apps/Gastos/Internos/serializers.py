from rest_framework.serializers import ModelSerializer
from .models import GastoInterno

class GastoInternoSerializer(ModelSerializer):
    class Meta:
        model = GastoInterno
        fields = ['Descripcion', 'Tipo_Gasto', 'Monto', 'Fecha', 'FechaCreacion', 'Responsable', 'Activo']