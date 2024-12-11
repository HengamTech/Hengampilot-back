from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user_management.models import User, Notifications
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSetTest(APITestCase):
    def setUp(self):
        """Create a test user and superuser"""
        self.user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpassword123",
            is_active=True,
        )
        self.superuser = User.objects.create_superuser(
            email="admin@example.com", username="admin", password="adminpassword123"
        )

        # Get the JWT token for authentication
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.superuser_token = str(RefreshToken.for_user(self.superuser).access_token)

    def test_create_user(self):
        """Test that a user can be created by anyone (public access)"""
        url = reverse("user_management:url_user_view-list")  # Use the proper name
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpassword123",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_user_by_username_success(self):
        """Test fetching user by username successfully"""
        url = (
            reverse("user_management:url_user_view-fetch-by-username")
            + "?username=testuser"
        )  # Use the proper name
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")

    def test_fetch_user_by_username_not_found(self):
        """Test fetching a non-existing user by username"""
        url = (
            reverse("user_management:url_user_view-fetch-by-username")
            + "?username=nonexistentuser"
        )  # Use the proper name
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_fetch_user_by_username_missing_param(self):
        """Test that missing the 'username' parameter results in a bad request"""
        url = reverse(
            "user_management:url_user_view-fetch-by-username"
        )  # Use the proper name
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fetch_user_me(self):
        """Test fetching the authenticated user's own data"""
        url = reverse("user_management:url_user_view-me")  # Use the proper name
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")

    def test_fetch_user_me_unauthenticated(self):
        """Test that accessing the 'me' endpoint without authentication is forbidden"""
        url = reverse("user_management:url_user_view-me")  # Use the proper name
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class NotificationViewSetTest(APITestCase):
    def setUp(self):
        """Create test user and notification"""
        self.user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpassword123",
            is_active=True,
        )

        self.notification = Notifications.objects.create(
            user_notifications=self.user,
            notofication_text="This is a test notification",
        )

        # Get the JWT token for authentication
        self.token = str(RefreshToken.for_user(self.user).access_token)

    def test_fetch_notifications(self):
        """Test fetching notifications for the authenticated user"""
        url = reverse(
            "user_management:url_notification_view-list"
        )  # Use the proper name
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["notofication_text"], "This is a test notification"
        )

    def test_fetch_notifications_unauthenticated(self):
        """Test that accessing the notification list without authentication is forbidden"""
        url = reverse(
            "user_management:url_notification_view-list"
        )  # Use the proper name
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_notification_is_associated_with_user(self):
        """Test that the notification is correctly associated with the user"""
        url = reverse(
            "user_management:url_notification_view-list"
        )  # Use the proper name
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get(url, format="json")
        self.assertEqual(
            str(response.data[0]["user_notifications"]), str(self.user.id)
        )  # Check if the notification is related to the current user
