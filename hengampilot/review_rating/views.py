from rest_framework import viewsets
from .models import Review, Vote, Reports, ReviewResponse
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (
    ReviewSerializer,
    VoteSerializer,
    ReportsSerializer,
    ReviewResponseSerializer,
)
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from .tasks import add_review_view, add_report_view


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def add_review(self, request):
        review_data = request.data
        add_review_view.apply_async(args=[review_data])
        return Response(
            {"message": "Review addition task initiated successfully"},
            status=status.HTTP_202_ACCEPTED,
        )


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def add_report(self, request):
        report_data = request.data
        add_report_view.apply_async(args=[report_data])
        return Response(
            {"message": "Report creation task initiated successfully"},
            status=status.HTTP_202_ACCEPTED,
        )


class ReviewResponseViewSet(viewsets.ModelViewSet):
    queryset = ReviewResponse.objects.all()
    serializer_class = ReviewResponseSerializer
    permission_classes = [IsAuthenticated]
