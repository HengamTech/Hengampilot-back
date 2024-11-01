from rest_framework import viewsets
from .models import Review, Vote, Reports, ReviewResponse
from .serializers import (
    ReviewSerializer, 
    VoteSerializer, 
    ReportsSerializer, 
    ReviewResponseSerializer
)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

class ReviewResponseViewSet(viewsets.ModelViewSet):
    queryset = ReviewResponse.objects.all()
    serializer_class = ReviewResponseSerializer