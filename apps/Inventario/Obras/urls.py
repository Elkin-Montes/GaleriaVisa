from rest_framework.routers import DefaultRouter
from .views import ObrasViewSet

router = DefaultRouter()
router.register(r'obras', ObrasViewSet, basename='obras')
urlpatterns = router.urls
