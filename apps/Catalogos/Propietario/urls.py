from rest_framework.routers import DefaultRouter
from .views import PropietarioViewSet

router = DefaultRouter()
router.register(r'propietarios', PropietarioViewSet, basename='propietario')
urlpatterns = router.urls