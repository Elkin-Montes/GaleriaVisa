from rest_framework.serializers import ModelSerializer
from .models import TiposDeObra

class TipoObraSerializer(ModelSerializer):
    class Meta:
        model = TiposDeObra
        fields = [ 'Codigo', 'NombreTipo', ]