from rest_framework.serializers import ModelSerializer
from .models import Exposicion, ObrasEnExposicion

class ExposicionSerializer(ModelSerializer):
    class Meta:
        model = Exposicion
        fields = ['Titulo', 'Lugar', 'FechaInicio', 'FechaFinalizacion', 'FechaCreacion', 'Activo']

    def validate(self, attrs):
        return super().validate(attrs)
    
class ObrasEnExposicionSerializer(ModelSerializer):
    class Meta:
        model = ObrasEnExposicion
        fields = ['Exposicion', 'Obra', 'Vendida', 'FechaExposicion', 'FechaCreacion', 'Activo']

    def validate(self, attrs):
        return super().validate(attrs)