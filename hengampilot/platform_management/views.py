from django.shortcuts import render
from rest_framework import viewsets
from .models import FeatureRequest
from .serializers import FeatureRequestSerializer

class FeatureRequestViewSet(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer



