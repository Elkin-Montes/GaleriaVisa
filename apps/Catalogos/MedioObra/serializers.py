from rest_framework.serializers import ModelSerializer
from .models import MediosDeObra

class MedioObraSerializer(ModelSerializer):
    class Meta:
        model = MediosDeObra
        fields = [ 'Codigo', 'NombreMedio', ]