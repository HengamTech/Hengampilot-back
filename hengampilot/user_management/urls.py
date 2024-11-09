from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, NotificationViewSet

app_name = "user_management"

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="url_user_view")
router.register(r"notifications", NotificationViewSet, basename="url_notification_view")

urlpatterns = [
    path("", include(router.urls)),
]
