from rest_framework import viewsets

from .models import Review, Vote, Reports, ReviewResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .serializers import (
    ReviewSerializer,
    VoteSerializer,
    ReportsSerializer,
    ReviewResponseSerializer,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .tasks import add_review_view, add_report_view
from user_management.models import User


# ViewSet for handling reviews
class ReviewViewSet(viewsets.ModelViewSet):
    # Set the queryset for the viewset
    queryset = Review.objects.all()
    # Specify the serializer to be used
    serializer_class = ReviewSerializer
    # Set permission class to ensure only authenticated users can access the viewset
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve", "view_reviews"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="view_reviews",
    )
    def view_reviews(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    # Custom action for adding a review (this triggers a background task)
    @action(detail=False, methods=["post"])
    def add_review(self, request):
        # Extract review data from the request
        review_data = request.data
        # Trigger the background task to process the review addition
        add_review_view.apply_async(args=[review_data])
        # Respond with an accepted status code indicating that the task has been initiated
        return Response(
            {"message": "Review addition task initiated successfully"},
            status=status.HTTP_202_ACCEPTED,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "username", str, description="The username of the user.", required=False
            ),
            OpenApiParameter(
                "id", str, description="The user ID (UUID).", required=False
            ),
        ],
        responses={
            200: ReviewSerializer(many=True),
            400: "Bad Request",
            404: "User not found",
        },
    )
    @action(detail=False, methods=["get"], url_path="reviews-by-user")
    def reviews_by_user(self, request):
        username = request.query_params.get("username")
        user_id = request.query_params.get("id")

        if not username and not user_id:
            return Response(
                {"detail": "Either 'username' or 'id' query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # username or id
            if username:
                user = User.objects.get(username=username)
            elif user_id:
                user = User.objects.get(id=user_id)

            # review from specific user
            reviews = Review.objects.filter(user=user)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )


# ViewSet for handling votes
class VoteViewSet(viewsets.ModelViewSet):
    # Set the queryset for the viewset
    queryset = Vote.objects.all()
    # Specify the serializer to be used
    serializer_class = VoteSerializer
    # Set permission class to ensure only authenticated users can access the viewset
    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "username", str, description="The username of the user.", required=False
            ),
            OpenApiParameter(
                "id", str, description="The user ID (UUID).", required=False
            ),
        ],
        responses={
            200: ReviewSerializer(many=True),
            400: "Bad Request",
            404: "User not found",
        },
    )
    @action(detail=False, methods=["get"], url_path="reviews-liked-by-user")
    def reviews_liked_by_user(self, request):
        username = request.query_params.get("username")
        user_id = request.query_params.get("id")

        if not username and not user_id:
            return Response(
                {"detail": "Either 'username' or 'id' query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            if username:
                user = User.objects.get(username=username)
            elif user_id:
                user = User.objects.get(id=user_id)

            votes = Vote.objects.filter(user=user)

            reviews_liked = [vote.review for vote in votes]
            serializer = ReviewSerializer(reviews_liked, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )


# ViewSet for handling reports
class ReportsViewSet(viewsets.ModelViewSet):
    # Set the queryset for the viewset
    queryset = Reports.objects.all()
    # Specify the serializer to be used
    serializer_class = ReportsSerializer
    # Set permission class to ensure only authenticated users can access the viewset
    permission_classes = [IsAuthenticated]

    # Custom action for adding a report (this triggers a background task)
    @action(detail=False, methods=["post"])
    def add_report(self, request):
        # Extract report data from the request
        report_data = request.data
        # Trigger the background task to process the report creation
        add_report_view.apply_async(args=[report_data])
        # Respond with an accepted status code indicating that the task has been initiated
        return Response(
            {"message": "Report creation task initiated successfully"},
            status=status.HTTP_202_ACCEPTED,
        )


# ViewSet for handling review responses
class ReviewResponseViewSet(viewsets.ModelViewSet):
    # Set the queryset for the viewset
    queryset = ReviewResponse.objects.all()
    # Specify the serializer to be used
    serializer_class = ReviewResponseSerializer
    # Set permission class to ensure only authenticated users can access the viewset
    permission_classes = [IsAuthenticated]
