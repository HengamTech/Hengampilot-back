from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import AuditLog
from .serializers import AuditLogSerializer

# ViewSet for handling read-only access to AuditLog data
class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    # Define the queryset that this viewset will operate on
    queryset = AuditLog.objects.all()
    
    # Specify the serializer class that will be used to convert model instances to JSON
    serializer_class = AuditLogSerializer
    
    # Define the permissions required to access the viewset (admin or authenticated users)
    permission_classes = [IsAdminUser, IsAuthenticated]
    
    # Specify the filter backends used to filter and search the data
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # Define which fields the user can filter by (filterset fields)
    filterset_fields = ['action_type', 'content_type', 'user']
    
    # Define which fields the user can search by (search fields)
    search_fields = ['changes']
