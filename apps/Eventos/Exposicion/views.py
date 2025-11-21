from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Exposicion
from .serializers import ExposicionSerializer

class ExposicionViewSet(viewsets.ModelViewSet):
    queryset = Exposicion.objects.all()
    serializer_class = ExposicionSerializer

    def list(self, request):
        return super().list(request)
    
    def create(self, request):
        return super().create(request)
    
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)
    
    def update(self, request, pk=None):
        return super().update(request, pk)
    
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        return super().destroy(request, pk)

