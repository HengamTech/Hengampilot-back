from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from user_management.models import User
from business_management.models import Business
from review_rating.models import Review, Vote, Reports, ReviewResponse


class ReviewViewSetTestCase(APITestCase):
    def setUp(self):
        """Creating users and businesses for use in tests"""
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_name="Test Business",
            business_owner=self.user,
            description="Test business description",
            average_rank=3,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_review(self):
        """Test creating a review through the viewset"""
        url = reverse("review_rating:reviews-list")
        data = {
            "user": self.user.id,
            "business_id": self.business.id,
            "rank": 5,
            "review_text": "Great business!",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["review_text"], "Great business!")


    def test_add_review_action(self):
        """Test the add_review custom action"""
        url = reverse("review_rating:reviews-list")  # Assuming the action is mapped to this URL
        data = {
            "user": self.user.id,
            "business_id": self.business.id,
            "rank": 5,
            "review_text": "Amazing service!",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        


class VoteViewSetTestCase(APITestCase):
    def setUp(self):
        """Creating users and votes for use in tests"""
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_name="Test Business",
            business_owner=self.user,
            description="Test business description",
            average_rank=3,
        )
        self.review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            rank=4,
            review_text="Nice business!",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_vote(self):
        """Test creating a vote through the viewset"""
        url = reverse("review_rating:votes-list")
        data = {
            "user": self.user.id,
            "review": self.review.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], self.user.id)

    def test_vote_without_user(self):
        """Test creating a vote without a user, which should raise an error"""
        url = reverse("review_rating:votes-list")
        data = {"review": self.review.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReportsViewSetTestCase(APITestCase):
    def setUp(self):
        """Creating users and reports for use in tests"""
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_name="Test Business",
            business_owner=self.user,
            description="Test business description",
            average_rank=3,
        )
        self.review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            rank=4,
            review_text="Nice business!",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_report(self):
        """Test creating a report through the viewset"""
        url = reverse("review_rating:reports-list")
        data = {
            "review_id": self.review.id,
            "review_user_id": self.user.id,
            "reason_select": "terrorism",  # Assuming the values are passed as strings
            "reason": "Inappropriate content.",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["reason"], "Inappropriate content.")

    def test_add_report_action(self):
        """Test the add_report custom action"""
        url = reverse("review_rating:reports-list")  # Assuming the action is mapped to this URL
        data = {
            "review_id": self.review.id,
            "review_user_id": self.user.id,
            "reason_select": "terrorism",
            "reason": "Inappropriate content.",
        }
        response = self.client.post(url, data, format="json")
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        


class ReviewResponseViewSetTestCase(APITestCase):
    def setUp(self):
        """Creating users and review responses for use in tests"""
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_name="Test Business",
            business_owner=self.user,
            description="Test business description",
            average_rank=3,
        )
        self.review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            rank=4,
            review_text="Nice business!",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_review_response(self):
        """Test creating a review response through the viewset"""
        url = reverse("review_rating:review_responses-list")
        data = {
            "review": self.review.id,
            "description": "Thank you for your feedback!",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["description"], "Thank you for your feedback!")
