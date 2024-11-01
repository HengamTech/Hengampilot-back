from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeatureRequestViewSet

app_name = 'platform_management'

router = DefaultRouter()
router.register(r'feature-requests', FeatureRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]