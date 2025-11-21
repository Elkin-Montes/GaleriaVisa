from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendedor
from .serializers import VendedorSerializer

class VendedorApiView(APIView):
    def get(self, request):
        Serializer = VendedorSerializer(Vendedor.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=Serializer.data)
        #return Response({'Vendedor': Vendedor.objects.all()})

    def post(self, request):
        serializer = VendedorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
    #obcion2
    #def post(self, request):
       # Vendedor.objects.create(Nombre=request.data['Nombre'], Apellido=request.data['Apellido'],
       # Cedula=request.data['Cedula'], Telefono=request.data['Telefono'],
       # FechaNaciminiento=request.data['FechaNaciminiento'], Correo=request.data['Correo'],
   # RFC=request.data['RFC'])
     # return Response(status=status.HTTP_201_CREATED, data={"message": "Vendedor creado exitosamente"})

