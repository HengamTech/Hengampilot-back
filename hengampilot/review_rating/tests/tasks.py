from django.test import TestCase
from review_rating.models import Review, Reports, ReasonReport, ResultReport
from user_management.models import User
from review_rating.tasks import (
    add_review_view,
    add_report_view,
    create_report_for_review,
)
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from business_management.models import Business
import uuid


class CeleryTaskTests(TestCase):

    def setUp(self):
        # Create a sample user
        self.user = User.objects.create(username="test_user", password="password123")
        self.business = Business.objects.create(
            business_name="Test Business",
            description="This is a test business.",
            business_owner=self.user,
            average_rank=5,
        )
        # Create a sample review
        self.review = Review.objects.create(
            user=self.user,
            business_id=self.business,  # Assuming foreign key is nullable for testing
            rank=3,
            review_text="This is a sample review.",
            hidden=False,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

    def test_add_review_view_success(self):
        review_data = {
            "user": self.user.id,
            "review_text": "This is a new review.",
            "rank": 4,
            "hidden": False,
        }

        result = add_review_view(review_data)
        print(result)
        self.assertEqual(result, "Review added successfully")
        self.assertTrue(
            Review.objects.filter(review_text="This is a new review.").exists()
        )

    def test_add_review_view_failure(self):
        review_data = {
            "user": self.user.id,
            "review_text": "",  # Invalid data
            "rank": 4,
            "hidden": False,
        }

        result = add_review_view(review_data)

        self.assertEqual(result, "Error adding review")
        self.assertFalse(Review.objects.filter(review_text="").exists())

    def test_add_report_view_success(self):
        report_data = {
            "review_id": self.review.id,
            "review_user_id": self.user.id,
            "reason": "Inappropriate content",
            "reason_select": ReasonReport.ACCUSATIONS.value,
            "result_report": ResultReport.Unchecked.value,
        }

        result = add_report_view(report_data)

        self.assertEqual(result, "Report added successfully")
        self.assertTrue(Reports.objects.filter(reason="Inappropriate content").exists())

    def test_add_report_view_failure(self):
        report_data = {
            "review_id": self.review.id,
            "review_user_id": self.user.id,
            "reason": "",
            "reason_select": "",
        }

        result = add_report_view(report_data)

        self.assertEqual(result, "Error adding report")
        self.assertFalse(Reports.objects.filter(reason="").exists())

    def test_create_report_for_review_success(self):
        reason = "Inappropriate content"
        reason_select = ReasonReport.ACCUSATIONS.value

        result = create_report_for_review(
            review_id=self.review.id,
            user_id=self.user.id,
            reason=reason,
            reason_select=reason_select,
        )

        # Assert that the report was created successfully
        self.assertEqual(
            result, f"Report for review {self.review.id} created successfully."
        )
        self.assertTrue(
            Reports.objects.filter(review_id=self.review, reason=reason).exists()
        )

    def test_create_report_for_review_review_not_found(self):

        result = create_report_for_review(
            review_id=uuid.uuid4(),  # Non-existent review ID
            user_id=self.user.id,
            reason="Inappropriate content",
        )

        self.assertEqual(result, "Review with ID not found.")

    def test_create_report_for_review_user_not_found(self):
        import uuid

        result = create_report_for_review(
            review_id=self.review.id,
            user_id=uuid.uuid4(),  # Non-existent user ID
            reason="Inappropriate content",
        )

        self.assertEqual(result, "User with ID not found.")
