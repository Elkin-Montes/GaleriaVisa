from rest_framework.routers import DefaultRouter
from .views import FacturaViewSet, DetalleFacturaViewSet

router = DefaultRouter()
router.register(r'facturas', FacturaViewSet, basename='factura')
router.register(r'detalles_factura', DetalleFacturaViewSet, basename='detallefactura')
urlpatterns = router.urls