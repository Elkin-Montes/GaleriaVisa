from rest_framework.routers import DefaultRouter
from .views import TipoObraViewSet

router = DefaultRouter()
router.register(r'tipo_obra', TipoObraViewSet, basename='tipo-obra')
urlpatterns = router.urls

