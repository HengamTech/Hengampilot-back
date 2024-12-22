from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusinessViewSet, SubscriptionVeiw,CategoryView

# Define the application namespace for URL reverse resolution
app_name = "business_management"

# Create a router instance for automatically generating URL patterns
router = DefaultRouter()

# Register the BusinessViewSet with the router for the 'businesses' endpoint
router.register(r"businesses", BusinessViewSet, basename="businesses")

# Register the SubscriptionVeiw with the router for the 'subscription' endpoint
router.register(r"subscription", SubscriptionVeiw, basename="subscription")
router.register(r"category", CategoryView, basename="catgory")

# Define the URL patterns for the app, including the routes generated by the router
urlpatterns = [
    path("", include(router.urls)),  # Include all routes generated by the router
]
