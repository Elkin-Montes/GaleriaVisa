from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from .models import MediosDeObra

class MedioObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediosDeObra
        fields = [ 'Codigo', 'NombreMedio', ]

    
    Codigo = serializers.CharField(
        validators=[
            UniqueValidator(queryset=MediosDeObra.objects.all()),
            RegexValidator(regex=r'^\d{4}$', message='El código debe tener el formato 0000')
        ]
    )