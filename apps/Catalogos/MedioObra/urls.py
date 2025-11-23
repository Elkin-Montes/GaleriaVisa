from rest_framework.routers import DefaultRouter
from .views import MedioObraViewSet

router = DefaultRouter()
router.register(r'medioobra', MedioObraViewSet, basename='medioobra')

urlpatterns = router.urls
