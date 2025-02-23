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
from .permission import AllowAnyGet

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all() 
    serializer_class = (BusinessSerializer)
    permission_classes = [AllowAnyGet]  
    filter_backends = [
        DjangoFilterBackend,  
        filters.SearchFilter,  
        filters.OrderingFilter,  
    ]
    search_fields = ["business_name", "description"]  
    ordering_fields = [
        "created_at",
        "average_rank",
    ]  

    def get_serializer_class(self):
        if self.action == "create":
            return BusinessCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return BusinessUpdateSerializer
        return BusinessSerializer

    def perform_create(self, serializer):
        serializer.save(business_owner=self.request.user, average_rank=0)

    @action(detail=False,methods=["get"],url_path="categories")
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
            400: OpenApiParameter, 
            404: OpenApiParameter,  
        },
    )
    @action(detail=False, methods=["get"], url_path="reviews")
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

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="category_name",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Name of the category to retrieve business for.",
                required=False,
            ),
        ],
        responses={
            200: OpenApiParameter,
            400: OpenApiParameter,  
            404: OpenApiParameter,  
        },
    )
    @action(detail=False,methods=["get"],url_path="category-businesses",)
    def get_businesses_by_category(self, request):
        category_name = request.query_params.get("category_name", None)

        if not category_name:
            return Response(
                {"error": "Please provide a category name as a query parameter."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            #category = Category.objects.get(category_name=category_name)
            category = Category.objects.filter(category_name__iexact=category_name).first()
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        businesses = Business.objects.filter(business_category=category)
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ViewSet for managing Subscription operations (CRUD)
class SubscriptionVeiw(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()  # Get all Subscription records
    serializer_class = (
        SubscriptionSerializer  # Default serializer class for the Subscription model
    )
    permission_classes = [AllowAnyGet]  # Only authenticated users can access

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


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAnyGet]