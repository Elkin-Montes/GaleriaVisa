from rest_framework.serializers import ModelSerializer
from .models import Propietario

class PropietarioSerializer(ModelSerializer):
    class Meta:
        model = Propietario
        fields = [ 'Nombre','Apellido', 'Cedula', 'Correo', 'Telefono' ]