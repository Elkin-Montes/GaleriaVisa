from django.urls import path, include

urlpatterns = [
    path('gastos/', include('apps.Gastos.Internos.urls')),]