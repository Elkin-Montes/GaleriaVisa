from django.urls import path, include


urlpatterns = [
    path('exposicion/', include('apps.Eventos.Exposicion.urls')),
]
