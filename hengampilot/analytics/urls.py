from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuditLogViewSet

app_name = 'analytics'

router = DefaultRouter()
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]