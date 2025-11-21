from django.urls import path, include

app_name = 'exposicion'

urlpatterns = [
    path('exposicion/', include('apps.Eventos.Exposicion.urls')),
]
