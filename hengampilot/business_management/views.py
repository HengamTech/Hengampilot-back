from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Business, Subscription, Category
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .serializers import (
    BusinessSerializer,
    BusinessCreateSerializer,
    BusinessUpdateSerializer,
    SubscriptionSerializer,
    CategorySerializer,  # doesn't exists
)

from review_rating.models import Review
from review_rating.serializers import ReviewSerializer
from .tasks import manage_subscription


# ViewSet for managing Business operations (CRUD)
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()  # Get all Business records
    serializer_class = (
        BusinessSerializer  # Default serializer class for the Business model
    )
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    filter_backends = [
        DjangoFilterBackend,  # Backend for filtering
        filters.SearchFilter,  # Backend for search functionality
        filters.OrderingFilter,  # Backend for ordering results
    ]
    search_fields = ["business_name", "description"]  # Fields to be searchable
    ordering_fields = [
        "created_at",
        "average_rank",
    ]  # Fields by which the results can be ordered

    def get_permissions(self):
        if self.action in ["list", "retrieve", "categories"]:
            return [AllowAny()]  # Allow any user to access these actions
        return [IsAuthenticated()]

    # Dynamically return the appropriate serializer class based on the action
    def get_serializer_class(self):
        # Use the BusinessCreateSerializer for the create action
        if self.action == "create":
            return BusinessCreateSerializer
        # Use the BusinessUpdateSerializer for update or partial_update actions
        elif self.action in ["update", "partial_update"]:
            return BusinessUpdateSerializer
        # Use the default BusinessSerializer for other actions
        return BusinessSerializer

    # Override the perform_create method to set the business_owner as the current user
    def perform_create(self, serializer):
        serializer.save(business_owner=self.request.user, average_rank=0)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="categories",
    )
    def list_categories(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Name of the business to retrieve reviews for.",
                required=False,
            ),
            OpenApiParameter(
                name="id",
                type=str,
                location=OpenApiParameter.QUERY,
                description="ID of the business to retrieve reviews for.",
                required=False,
            ),
        ],
        responses={
            200: ReviewSerializer(many=True),
            400: OpenApiParameter,  # پیام خطا در صورت ورود اشتباه
            404: OpenApiParameter,  # پیام خطا در صورت عدم وجود شرکت
        },
    )
    @action(
        detail=False, methods=["get"], permission_classes=[AllowAny], url_path="reviews"
    )
    def get_reviews(self, request):
        business_name = request.query_params.get("name", None)
        business_id = request.query_params.get("id", None)

        if not business_name and not business_id:
            return Response(
                {"error": "Please provide either 'name' or 'id' as a query parameter."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            if business_name:
                business = Business.objects.get(business_name=business_name)
            elif business_id:
                business = Business.objects.get(id=business_id)
        except Business.DoesNotExist:
            return Response(
                {"error": "Business not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        reviews = Review.objects.filter(business_id=business)
        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# ViewSet for managing Subscription operations (CRUD)
class SubscriptionVeiw(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()  # Get all Subscription records
    serializer_class = (
        SubscriptionSerializer  # Default serializer class for the Subscription model
    )
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    # Custom action to manage a subscription (activate, deactivate, change type)
    @action(detail=True, methods=["post"])
    def manage(self, request, pk=None):
        # Fetch the subscription object based on the provided ID (pk)
        subscription = self.get_object()
        # Get action and subscription type from the request data
        action = request.data.get("action")
        subscription_type = request.data.get("subscription_type")

        # Call the Celery task to manage the subscription asynchronously
        manage_subscription.delay(subscription.id, action, subscription_type)

        # Return a response indicating that the task has been initiated
        return Response(
            {"message": f"Subscription {action} task has been initiated."},
            status=status.HTTP_202_ACCEPTED,
        )
