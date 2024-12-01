from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, NotificationViewSet

# Set the app name for namespace purposes
app_name = "user_management"

# Create a router for automatic URL routing
router = DefaultRouter()

# Register the UserViewSet with the router
# This will automatically create routes for the User model's CRUD operations
router.register(r"users", UserViewSet, basename="url_user_view")

# Register the NotificationViewSet with the router
# This will automatically create routes for the Notifications model's CRUD operations
router.register(r"notifications", NotificationViewSet, basename="url_notification_view")

# URL patterns for the user_management app
# The include(router.urls) will include all the routes generated by the DefaultRouter
urlpatterns = [
    path(
        "", include(router.urls)
    ),  # This will include all generated URLs from the router
]
