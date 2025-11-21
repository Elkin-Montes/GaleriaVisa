from rest_framework.routers import DefaultRouter
from .views import ExposicionViewSet

router = DefaultRouter()

router.register('', ExposicionViewSet, basename='exposicion')

urlpatterns = router.urls