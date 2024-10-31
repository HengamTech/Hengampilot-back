from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReviewViewSet, VoteViewSet, ReportsViewSet, ReviewResponseViewSet

app_name = "review_rating"

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'reports', ReportsViewSet)
router.register(r'review_responses', ReviewResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]