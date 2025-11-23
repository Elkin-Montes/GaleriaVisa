from rest_framework import viewsets
from rest_framework.response import Response
from .models import MediosDeObra
from .serializers import MedioObraSerializer

class MedioObraViewSet(viewsets.ModelViewSet):
    queryset = MediosDeObra.objects.all()
    serializer_class = MedioObraSerializer

    def list(self, request,):
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
    
    