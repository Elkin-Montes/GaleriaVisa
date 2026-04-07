from rest_framework.routers import DefaultRouter
from .views import ExposicionViewSet, ObrasEnExposicionViewSet

router = DefaultRouter()

router.register(r'exposicion', ExposicionViewSet, basename='exposicion')
router.register(r'obras_en_exposicion', ObrasEnExposicionViewSet, basename='obras-en-exposicion')

urlpatterns = router.urls