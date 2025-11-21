from rest_framework.serializers import ModelSerializer
from .models import Exposicion

class ExposicionSerializer(ModelSerializer):
    class Meta:
        model = Exposicion
        fields = ['Titulo', 'Lugar', 'FechaInicio', 'FechaFinalizacion', 'FechaCreacion', 'Activo']