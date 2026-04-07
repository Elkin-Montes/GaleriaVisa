from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from .models import EstilosDeObra

class EstiloObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstilosDeObra
        fields = [ 'Codigo', 'NombreEstilo', ]

    Codigo = serializers.CharField(
        validators=[
            UniqueValidator(queryset=EstilosDeObra.objects.all()),
            RegexValidator(regex=r'^\d{4}$', message='El código debe tener el formato 0000')
        ]
    )