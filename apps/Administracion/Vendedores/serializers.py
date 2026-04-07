from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Vendedor

class VendedorSerializer(ModelSerializer):
    class Meta:
        model = Vendedor
        fields = [ 'Nombre', 'Apellido', 'Cedula', 'Telefono', 'FechaNaciminiento', 'Correo', 'RFC']

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
    RFC= serializers.CharField(
        validators=[
            RegexValidator(regex=r'^[A-ZÑ&]{3}\d{4}$', message='El RFC debe tener el formato XXX0000')
            ]
        )