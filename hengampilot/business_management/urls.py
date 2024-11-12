from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusinessViewSet, SubscriptionVeiw

app_name = "business_management"

router = DefaultRouter()
router.register(r"businesses", BusinessViewSet, basename="businesses")
router.register(r"subscription", SubscriptionVeiw, basename="subscription")
urlpatterns = [
    path("", include(router.urls)),
]


