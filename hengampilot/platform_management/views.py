from django.shortcuts import render
from rest_framework import viewsets
from .models import FeatureRequest
from .serializers import FeatureRequestSerializer
from .permission import AllowAnyGet

# ViewSet for FeatureRequest model
class FeatureRequestViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all FeatureRequest records
    queryset = FeatureRequest.objects.all()
    
    # Define the serializer to use for FeatureRequest data
    serializer_class = FeatureRequestSerializer
    
    # Restrict access to authenticated users only
    permission_classes = [AllowAnyGet]
