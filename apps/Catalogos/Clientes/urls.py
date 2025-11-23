from rest_framework.routers import DefaultRouter
from .views import ClientesViewSet

router = DefaultRouter()
router.register(r'clientes', ClientesViewSet, basename='clientes')
urlpatterns = router.urls
