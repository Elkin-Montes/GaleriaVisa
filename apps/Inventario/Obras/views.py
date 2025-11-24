from rest_framework import viewsets
from .models import Obras
from .serializers import ObrasSerializer

class ObrasViewSet(viewsets.ModelViewSet):
    queryset = Obras.objects.all()
    serializer_class = ObrasSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create (self, request, *args, **kwargs):
        # Custom logic for creating an Obra can be added here
        return super().create(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # Custom logic for updating an Obra can be added here
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
