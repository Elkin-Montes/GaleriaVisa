from rest_framework.serializers import ModelSerializer
from .models import EstilosDeObra

class EstiloObraSerializer(ModelSerializer):
    class Meta:
        model = EstilosDeObra
        fields = [ 'Codigo', 'NombreEstilo', ]