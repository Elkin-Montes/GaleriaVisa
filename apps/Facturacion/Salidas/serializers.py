from rest_framework.serializers import ModelSerializer
from .models import Factura, DetalleFactura

class FacturaSerializer(ModelSerializer):
    class Meta:
        model = Factura
        fields = ['IdCliente', 'IdVendedor', 'Estado', 'Total', 'FechaCreacion']

class DetalleFacturaSerializer(ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = ['IdFactura', 'IdObra', 'Precio']