from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Notifications
from rest_framework.test import APIClient

class UserViewSetTest(APITestCase):

    def setUp(self):
        # Set up a user and an API client
        self.client = APIClient()
        self.user_data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "securepassword"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_user(self):
        url = reverse('user-list')  # Assuming you have a 'user-list' URL in your routing
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpassword"
        }
        response = self.client.post(url, data, format='json')

        # Check that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # One user should be created

    def test_fetch_user_by_username_success(self):
        url = reverse('user-fetch-by-username') + '?username=testuser'
        response = self.client.get(url)

        # Check that the response status code is 200 OK and returns the correct user data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_fetch_user_by_username_not_found(self):
        url = reverse('user-fetch-by-username') + '?username=nonexistentuser'
        response = self.client.get(url)

        # Check that the response status code is 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_fetch_user_by_username_bad_request(self):
        url = reverse('user-fetch-by-username')  # Missing the 'username' parameter
        response = self.client.get(url)

        # Check that the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_me_endpoint(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('user-me')  # Assuming you have a 'user-me' URL in your routing
        response = self.client.get(url)

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)


class NotificationViewSetTest(APITestCase):

    def setUp(self):
        # Set up a user and a notification
        self.client = APIClient()
        self.user_data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "securepassword"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.notification = Notifications.objects.create(
            user_notifications=self.user,
            notofication_text="Test notification",
        )

    def test_get_notifications(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('notification-list')  # Assuming you have a 'notification-list' URL
        response = self.client.get(url)

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One notification should be returned

    def test_notification_is_read(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('notification-detail', args=[str(self.notification.id)])  # Assuming you have a 'notification-detail' URL
        response = self.client.patch(url, {'is_read': True})

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.notification.refresh_from_db()
        self.assertTrue(self.notification.is_read)  # The notification should be marked as read
