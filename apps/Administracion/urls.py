from django.urls import path, include

app_name = 'Vendedores'

urlpatterns = [
    path('vendedores/', include('apps.Administracion.Vendedores.urls')),
]
