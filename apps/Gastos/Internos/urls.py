from rest_framework.routers import DefaultRouter
from .views import GastoInternoViewSet

router = DefaultRouter()

router.register(r'interno', GastoInternoViewSet, basename='gasto-interno')

urlpatterns = router.urls