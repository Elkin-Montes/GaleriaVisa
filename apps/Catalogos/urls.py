from django.urls import path, include

urlpatterns = [
    path('estiloobra/', include('apps.Catalogos.EstiloObra.urls')),
    path('medioobra/', include('apps.Catalogos.MedioObra.urls')),
    path('clientes/', include('apps.Catalogos.Clientes.urls')),
   # path('artistas/', include('apps.Catalogos.Artistas.urls')), eerror en fecha nacimiento
    path('tipoobra/', include('apps.Catalogos.TipoObra.urls')),
    path('propietario/', include('apps.Catalogos.Propietario.urls')),
    
    ]