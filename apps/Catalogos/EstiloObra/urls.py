from rest_framework.routers import DefaultRouter
from .views import EstiloObraViewSet

router = DefaultRouter()
router.register(r'estiloobra', EstiloObraViewSet, basename='estiloobra')
urlpatterns = router.urls