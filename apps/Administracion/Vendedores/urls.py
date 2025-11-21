from django.urls import path
from .views import VendedorApiView

app_name = 'Vendedores'

urlpatterns = [
    path('', VendedorApiView.as_view(), name='vendedor'),
]

