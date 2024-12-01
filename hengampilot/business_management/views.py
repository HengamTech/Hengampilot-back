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


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ["business_name", "description"]
    ordering_fields = ["created_at", "average_rank"]

    def get_serializer_class(self):
        if self.action == "create":
            return BusinessCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return BusinessUpdateSerializer
        return BusinessSerializer

    def perform_create(self, serializer):
        serializer.save(business_owner=self.request.user, average_rank=0)


class SubscriptionVeiw(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def manage(self, request, pk=None):
        subscription = self.get_object()
        action = request.data.get("action")
        subscription_type = request.data.get("subscription_type")

        manage_subscription.delay(subscription.id, action, subscription_type)

        return Response(
            {"message": f"Subscription {action} task has been initiated."},
            status=status.HTTP_202_ACCEPTED,
        )
