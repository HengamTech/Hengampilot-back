from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from user_management.models import User
from platform_management.models import FeatureRequest, JobStatus
from rest_framework.permissions import IsAuthenticated


class FeatureRequestViewSetTestCase(APITestCase):
    def setUp(self):
        # Set up the user
        self.user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="password",
            is_active=True,
        )
        self.client.force_authenticate(user=self.user)  # Force authenticate the user

        # Set up the FeatureRequest data
        self.feature_request_data = {
            "description": "Description of the new feature",
            "user": self.user.id,
            "status": JobStatus.PENDING.value,  # Set initial status to PENDING
        }
        self.url = reverse(
            "platform_management:featurerequest-list"
        )  # URL for listing feature requests

    def test_create_feature_request(self):
        # Send a POST request to create a feature request
        response = self.client.post(self.url, self.feature_request_data, format="json")
        # print(response.data)

        # Check if the request was successful and the feature request is created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["description"], self.feature_request_data["description"]
        )
        self.assertEqual(response.data["status"], JobStatus.PENDING.value)

    def test_list_feature_requests(self):
        # Create a feature request instance
        FeatureRequest.objects.create(
            description="Test description 1",
            user=self.user,
            status=JobStatus.APPROVED.value,
        )

        # Send a GET request to list feature requests
        response = self.client.get(self.url)

        # Check if the list is returned and contains the created feature request
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(
            len(response.data), 0
        )  # Ensure there's at least one feature request in the list

    def test_create_feature_request_unauthenticated(self):
        # Unauthenticate the client
        self.client.force_authenticate(user=None)

        # Send a POST request to create a feature request (should fail since user is not authenticated)
        response = self.client.post(self.url, self.feature_request_data, format="json")

        # Check if the request fails with status 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_feature_request_permissions(self):
        # Create a new user who is not authenticated
        unauthenticated_user = User.objects.create_user(
            email="unauthuser@example.com",
            username="unauthuser",
            password="password",
            is_active=True,
        )

        # Force authenticate the unauthenticated user
        self.client.force_authenticate(user=unauthenticated_user)

        # Send a POST request to create a feature request (should succeed as user is authenticated)
        response = self.client.post(self.url, self.feature_request_data, format="json")

        # Check if the request is successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_feature_request_invalid_description(self):
        # Set up invalid data (empty description)
        invalid_data = {
            "description": "",  # Invalid empty description
            "user": self.user.id,
            "status": JobStatus.PENDING.value,
        }

        # Send a POST request with invalid data
        response = self.client.post(self.url, invalid_data, format="json")

        # Check that the request fails with a validation error for the description
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "description", response.data
        )  # Ensure the error relates to the description field

    def test_create_feature_request_with_invalid_status(self):
        # Set up invalid status (not in the JobStatus Enum)
        invalid_data = {
            "description": "Valid description",
            "user": self.user.id,
            "status": "invalid_status",  # Invalid status value
        }

        # Send a POST request with invalid data
        response = self.client.post(self.url, invalid_data, format="json")

        # Check that the request fails with a validation error for the status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "status", response.data
        )  # Ensure the error relates to the status field
