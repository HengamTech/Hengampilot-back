from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReviewViewSet, VoteViewSet, ReportsViewSet, ReviewResponseViewSet

# Define the app name for namespacing the URLs in the project
app_name = "review_rating"

# Create a DefaultRouter instance that will automatically generate the URL patterns
router = DefaultRouter()

# Register the viewsets with the router, making them available for automatic URL routing
router.register(r"reviews", ReviewViewSet)  # URL pattern for managing reviews
router.register(r"votes", VoteViewSet)  # URL pattern for managing votes on reviews
router.register(
    r"reports", ReportsViewSet
)  # URL pattern for managing reports on reviews
router.register(
    r"review_responses", ReviewResponseViewSet
)  # URL pattern for managing review responses

# Define the URL patterns for this app, including the automatically generated URL patterns from the router
urlpatterns = [
    path(
        "", include(router.urls)
    ),  # Include all generated URL patterns under the base path
]
