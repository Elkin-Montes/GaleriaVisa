from rest_framework.serializers import ModelSerializer
from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = [ 'Nombre','Apellido', 'Cedula', 'Correo', 'Telefono' ]

    #VALIDACION PARA CADA UNO DE LOS CAMPOS
    Cedula = serializers.CharField(
            validators=[
                RegexValidator(regex=r'^\d{3}-\d{6}-\d{4}[A-Z]$', message='La cédula debe tener el formato XXX-XXXXXX-XXXXA')
            ]
        )
    Telefono = serializers.CharField(
        validators=[
            RegexValidator(regex=r'^\d{4}-\d{4}$', message='El teléfono debe tener el formato XXXX-XXXX')
            ]
        )
    Correo = serializers.EmailField(
        validators=[
            RegexValidator(regex=r'^[\w\.-]+@[\w\.-]+\.\w+$', message='Ingrese un correo electrónico válido')
            ]
        )