from rest_framework import viewsets
from .models import Review, Vote, Reports, ReviewResponse
from .serializers import (
    ReviewSerializer, 
    VoteSerializer, 
    ReportsSerializer, 
    ReviewResponseSerializer
)
from rest_framework.permissions import IsAuthenticated

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated]

class ReviewResponseViewSet(viewsets.ModelViewSet):
    queryset = ReviewResponse.objects.all()
    serializer_class = ReviewResponseSerializer
    permission_classes = [IsAuthenticated]