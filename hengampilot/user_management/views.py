from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Notifications
from .serializers import UserSerializer, NotificationSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
from review_rating.models import Review

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    @extend_schema(
        parameters=[
            OpenApiParameter('username', str, description='The username of the user you want to fetch.', required=True)
        ],
        responses={200: UserSerializer, 404: 'User not found', 400: 'Bad Request'}
    )
    @action(detail=False, methods=["get"], url_path='fetch-by-username')
    def fetch_by_username(self, request):
        username = request.query_params.get('username', None)
        if username is not None:
            try:
                user = User.objects.get(username=username)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "Username query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path="update-password")
    def update_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get("password")
        if not new_password:
            return Response({"detail": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated], url_path="total-users") 
    def total_users(self, request): 
        count = User.objects.count() 
        return Response({"total_users": count}, status=status.HTTP_200_OK) 
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated], url_path="active-users") 
    def active_users(self, request): 
        count = User.objects.filter(is_active=True).count() 
        return Response({"active_users": count}, status=status.HTTP_200_OK) 
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated], url_path="inactive-users") 
    def inactive_users(self, request): 
        count = User.objects.filter(is_active=False).count() 
        return Response({"inactive_users": count}, status=status.HTTP_200_OK)
    
    @extend_schema( 
        parameters=[ 
            OpenApiParameter('user_id', str, description='The ID of the user whose reviews you want to count.', required=True)
              ], 
              responses={200: "Review count"} ) 
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated], url_path="user-review-count") 
    def user_review_count(self, request): 
        user_id = request.query_params.get('user_id', None) 
        if user_id: 
            try: 
                user = User.objects.get(id=user_id) 
                count = Review.objects.filter(user=user).count() 
                return Response({"user_review_count": count}, status=status.HTTP_200_OK) 
            except User.DoesNotExist: 
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND) 
        else: 
            return Response({"detail": "User ID query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user_notifications=self.request.user)

    # @action(detail=True, methods=['post'])
    # def mark_as_read(self, request, pk=None):
    #     notification = self.get_object()
    #     notification.is_read = True
    #     notification.save()
    #     return Response({'status': 'notification marked as read'})
