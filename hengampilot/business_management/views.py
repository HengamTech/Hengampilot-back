from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Business, Subscription
from .serializers import BusinessSerializer, BusinessCreateSerializer, BusinessUpdateSerializer,SubscriptionSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    search_fields = ['business_name', 'description']
    ordering_fields = ['created_at', 'average_rank']

    def get_serializer_class(self):
        if self.action == 'create':
            return BusinessCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return BusinessUpdateSerializer
        return BusinessSerializer

    def perform_create(self, serializer):
        serializer.save(
            business_owner=self.request.user,
            average_rank=0
        )

    # @action(detail=True, methods=['post'])
    # def update_status(self, request, pk=None):
    #     if not request.user.is_admin:
    #         return Response(
    #             {'error': 'Only admins can update status'},
    #             status=status.HTTP_403_FORBIDDEN
    #         )
        
    #     business = self.get_object()
    #     new_status = request.data.get('status')
        
    #     if new_status not in [status.value for status in StatusCategory]:
    #         return Response(
    #             {'error': 'Invalid status'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )

    #     business.status = new_status
    #     business.save()
        
    #     return Response(BusinessSerializer(business).data)

    @action(detail=False, methods=['get'])
    def my_businesses(self, request):
        businesses = self.queryset.filter(business_owner=request.user)
        serializer = self.get_serializer(businesses, many=True)
        return Response(serializer.data)
    



class SubscriptionVeiw(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
