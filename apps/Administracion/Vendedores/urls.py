from rest_framework.routers import DefaultRouter
from .views import VendedorViewSet


router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet, basename='vendedores')
urlpatterns = router.urls
