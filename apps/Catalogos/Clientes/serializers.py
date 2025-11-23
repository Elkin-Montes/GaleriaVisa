from rest_framework.serializers import ModelSerializer
from .models import Clientes

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = [ 'Nombre','Apellido', 'Cedula', 'Correo', 'Telefono' ]