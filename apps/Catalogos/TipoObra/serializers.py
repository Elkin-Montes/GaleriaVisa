from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from .models import TiposDeObra

class TipoObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposDeObra
        fields = [ 'Codigo', 'NombreTipo', ]

    Codigo = serializers.CharField(
        validators=[
            UniqueValidator(queryset=TiposDeObra.objects.all()),
            RegexValidator(regex=r'^\d{4}$', message='El código debe tener el formato 0000')
        ]
    )