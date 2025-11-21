from rest_framework.serializers import ModelSerializer
from .models import Vendedor

class VendedorSerializer(ModelSerializer):
    class Meta:
        model = Vendedor
        fields = [ 'Nombre', 'Apellido', 'Cedula', 'Telefono', 'FechaNaciminiento', 'Correo', 'RFC']