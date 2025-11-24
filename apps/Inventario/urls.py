from django.urls import path,include

urlpatterns = [
    path(r'Obras', include('apps.Inventario.Obras.urls')),]