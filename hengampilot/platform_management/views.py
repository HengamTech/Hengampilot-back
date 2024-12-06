from django.shortcuts import render
from rest_framework import viewsets
from .models import FeatureRequest
from .serializers import FeatureRequestSerializer
from rest_framework.permissions import IsAuthenticated

class FeatureRequestViewSet(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer
    permission_classes = [IsAuthenticated]


