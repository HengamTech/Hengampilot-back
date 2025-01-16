import unittest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from user_management.models import User
from .models import Business, Subscription, Category


class UserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test27@example.com",
            username="testuser_business27",
            password="testpassword",
            is_active=True,
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(category_name="Tech")

    def test_create_business(self):
        url = reverse("business_management:businesses-list")
        data = {
            "business_name": "New Business",
            "description": "A newly created business.",
            "website_url": "https://newbusiness.com",
            "business_category": self.category.id,
            "business_owner": self.user.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["business_name"], data["business_name"])
        self.assertEqual(response.data["business_owner"], self.user.id)

    def test_list_businesses(self):
        Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test business.",
            website_url="https://test.com",
            business_category=self.category,
            average_rank=0,
        )
        url = reverse("business_management:businesses-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_update_business(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test business.",
            website_url="https://test.com",
            business_category=self.category,
            average_rank=0,
        )
        url = reverse(
            "business_management:businesses-detail", kwargs={"pk": business.id}
        )
        data = {
            "business_name": "Updated Business Name",
            "description": business.description,
            "website_url": business.website_url,
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["business_name"], data["business_name"])

    def test_get_businesses_by_category(self):
        # Create a business under the "Tech" category
        Business.objects.create(
            business_owner=self.user,
            business_name="Tech Business",
            description="A business in the tech category.",
            business_category=self.category,
            average_rank=0,
        )
        url = reverse("business_management:businesses-list")
        response = self.client.get(url, {"category_name": "Tech"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Assert that we get some businesses

    def test_create_category(self):
        url = reverse("business_management:catgory-list")
        data = {"category_name": "Health"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["category_name"], data["category_name"])




###



    def test_filter_by_category(self):
        url = reverse("business_management:businesses-list")
        response = self.client.get(url, {"business_category": self.category.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_filter_by_average_rank(self):
        url = reverse("business_management:businesses-list")
        response = self.client.get(url, {"ordering": "average_rank"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if len(response.data) > 1:
            self.assertTrue(response.data[0]["average_rank"] >= response.data[1]["average_rank"])
        else:
            print("Not enough data to compare average rank.")

    def test_search_by_name(self):
        url = reverse("business_management:businesses-list")
        response = self.client.get(url, {"search": "Tech Business 1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if len(response.data) > 1:
            self.assertTrue(response.data[0]["average_rank"] >= response.data[1]["average_rank"])
        else:
            print("Not enough data to compare average rank.")

class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test2@example.com",
            username="testuser",
            password="testpassword",
            is_active=True,
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(category_name="Tech")
        self.business = Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test business.",
            website_url="https://test.com",
            business_category=self.category,
            average_rank=0,
        )
        self.subscription = Subscription.objects.create(
            business=self.business,
            type="free",
            start_date="2024-01-01T00:00:00Z",
            end_date="2024-12-31T23:59:59Z",
            is_active=True,
        )



    # def test_manage_subscription_change_type(self):
    #     # Test changing subscription type to "premium"
    #     url = reverse("business_management:subscription-manage", kwargs={"pk": self.subscription.id})
    #     data = {"action": "change_type", "subscription_type": "premium"}
    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
    #     self.subscription.refresh_from_db()
    #     self.assertEqual(self.subscription.type, "premium")

    # def test_manage_subscription_invalid_action(self):
    #     # Test sending an invalid action
    #     url = reverse("business_management:subscription-manage", kwargs={"pk": self.subscription.id})
    #     data = {"action": "invalid_action", "subscription_type": "premium"}
    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data["error"], "Invalid action specified.")

    # def test_invalid_subscription_id(self):
    #     # Test with an invalid subscription ID
    #     url = reverse("business_management:subscription-manage", kwargs={"pk": 9999})  # Non-existent ID
    #     data = {"action": "activate"}
    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertEqual(response.data["error"], "Subscription with ID 9999 not found.")

    # def test_login_invalid_user(self):
    #     # Test login with invalid credentials
    #     self.client.logout()  # Log out the current user
    #     response = self.client.post(reverse("user_management:login"), {"username": "wronguser", "password": "wrongpass"})
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.assertEqual(response.data["error"], "Invalid credentials.")







class BusinessAccessTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test27@example.com",
            username="testuser_business27",
            password="testpassword",
            is_active=True,
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(category_name="Business Category")
        self.business = Business.objects.create(
            business_owner=self.user,
            business_name="Business 1",
            description="A description",
            business_category=self.category,
            average_rank=3
        )

    def test_access_without_authentication(self):
        self.client.logout()
        url = reverse("business_management:businesses-detail", kwargs={"pk": self.business.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_with_authorization(self):
        url = reverse("business_management:businesses-detail", kwargs={"pk": self.business.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_forbidden_for_non_owner(self):
        another_user = User.objects.create_user(
            email="anotheruser@example.com", username="anotheruser", password="password"
        )
        self.client.force_authenticate(user=another_user)
        url = reverse("business_management:businesses-detail", kwargs={"pk": self.business.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



class CategoryViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@example.com", username="testuser", password="password"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_category(self):
        url = reverse("business_management:category-list")
        data = {"category_name": "New Category"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["category_name"], "New Category")

    def test_list_categories(self):
        Category.objects.create(category_name="Category 1")
        Category.objects.create(category_name="Category 2")
        url = reverse("business_management:category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_retrieve_category(self):
        category = Category.objects.create(category_name="Category 1")
        url = reverse("business_management:category-detail", kwargs={"pk": category.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["category_name"], category.category_name)
