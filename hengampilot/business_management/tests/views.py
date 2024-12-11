import unittest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from user_management.models import User
from .models import Business, Subscription, Category


class UserTestCase(APITestCase):
    # Setup method to create a user, authenticate, and create a category before tests
    def setUp(self):
        self.client = APIClient()  # Create an instance of the APIClient
        self.user = User.objects.create_user(
            email="test27@example.com",
            username="testuser_business27",
            password="testpassword",
            is_active=True,
        )  # Create a new user
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        self.category = Category.objects.create(
            category_name="Tech"
        )  # Create a category

    # Test case for creating a new business
    def test_create_business(self):
        url = reverse(
            "business_management:businesses-list"
        )  # Get URL for businesses list
        data = {
            "business_name": "New Business",
            "description": "A newly created business.",
            "website_url": "https://newbusiness.com",
            "business_category": self.category.id,
            "business_owner": self.user.id,
        }  # Define the business data to be sent in the request
        response = self.client.post(
            url, data, format="json"
        )  # Send a POST request to create the business
        # print(response.content.decode("utf-8"))

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )  # Assert that the status code is 201 (created)
        self.assertEqual(
            response.data["business_name"], data["business_name"]
        )  # Assert business name matches
        self.assertEqual(
            response.data["business_owner"], self.user.id
        )  # Assert business owner matches

    # Test case for listing all businesses
    def test_list_businesses(self):
        Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test business.",
            website_url="https://test.com",
            business_category=self.category,
            average_rank=0,
        )  # Create a test business
        url = reverse(
            "business_management:businesses-list"
        )  # Get URL for businesses list
        response = self.client.get(url)  # Send a GET request to fetch businesses
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # Assert the status code is 200 (OK)
        self.assertGreater(
            len(response.data), 0
        )  # Assert that there is at least one business in the response

    # Test case for updating a business
    def test_update_business(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test business.",
            website_url="https://test.com",
            business_category=self.category,
            average_rank=0,
        )  # Create a business to be updated
        url = reverse(
            "business_management:businesses-detail", kwargs={"pk": business.id}
        )  # Get URL for business detail view
        data = {
            "business_name": "Updated Business Name",  # New business name
            "description": business.description,  # Keep the same description
            "website_url": business.website_url,  # Keep the same website URL
        }
        response = self.client.patch(
            url, data, format="json"
        )  # Send a PATCH request to update the business
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # Assert the status code is 200 (OK)
        self.assertEqual(
            response.data["business_name"], data["business_name"]
        )  # Assert updated name matches


class SubscriptionTestCase(APITestCase):
    # Setup method to create a user, business, and subscription before tests
    def setUp(self):
        self.client = APIClient()  # Create an instance of the APIClient
        self.user = User.objects.create_user(
            email="test2@example.com",
            username="testuser",
            password="testpassword",
            is_active=True,
        )  # Create a new user
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        self.category = Category.objects.create(
            category_name="Tech"
        )  # Create a category
        self.business = Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test business.",
            website_url="https://test.com",
            business_category=self.category,
            average_rank=0,
        )  # Create a business
        self.subscription = Subscription.objects.create(
            business=self.business,
            type="free",  # Create a free subscription
            start_date="2024-01-01T00:00:00Z",  # Subscription start date
            end_date="2024-12-31T23:59:59Z",  # Subscription end date
            is_active=True,  # Set subscription as active
        )
