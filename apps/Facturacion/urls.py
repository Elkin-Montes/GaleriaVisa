from django.urls import path, include

urlpatterns = [
    path('salida/', include('apps.Facturacion.Salidas.urls')),]