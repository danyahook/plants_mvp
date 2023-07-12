from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PlantViewSet

router = SimpleRouter()
router.register('plants', PlantViewSet, basename='plant')

urlpatterns = router.urls
