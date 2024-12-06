from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Business, Subscription
from .serializers import (
    BusinessSerializer,
    BusinessCreateSerializer,
    BusinessUpdateSerializer,
    SubscriptionSerializer,
)
from .tasks import create_subscription, deactivate_subscription


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
