from rest_framework.serializers import ModelSerializer
from .models import Artista

class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = [ 'Nombre','Apellido', 'Cedula', 'Telefono','FechaNacimiento','Correo','Referencia']