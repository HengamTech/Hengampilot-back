from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuditLogViewSet

# Define the app name for reverse URL resolution
app_name = 'analytics'

# Create a DefaultRouter instance to automatically generate URL patterns for viewsets
router = DefaultRouter()

# Register the AuditLogViewSet with the router under the path 'audit-logs'
router.register(r'audit-logs', AuditLogViewSet)

# Define the URL patterns for the app
urlpatterns = [
    # Include the generated URLs from the router into the app's URL configuration
    path('', include(router.urls)),
]
