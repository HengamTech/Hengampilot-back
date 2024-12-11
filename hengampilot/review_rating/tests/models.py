from django.test import TestCase
from user_management.models import User
from business_management.models import Business
from review_rating.models import Review, Vote, ReviewResponse, Reports, ReasonReport
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


class ReviewModelTestCase(TestCase):
    def setUp(self):
        """Creating users and businesses for use in tests"""
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_name="Test Business",
            business_owner=self.user,
            description="Test business description",
            average_rank=3,
        )

    def test_create_review(self):
        """Test creating a Review record correctly"""
        review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            rank=5,
            review_text="Great business!",
        )
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.business_id, self.business)
        self.assertEqual(review.rank, 5)
        self.assertEqual(review.review_text, "Great business!")

    def test_review_without_user(self):
        """Test creating a Review without a user, which should raise an error"""
        with self.assertRaises(IntegrityError):
            Review.objects.create(
                business_id=self.business,
                rank=4,
                review_text="Good business!",
            )

    def test_review_without_business(self):
        """Test creating a Review without a business, which should raise an error"""
        with self.assertRaises(IntegrityError):
            Review.objects.create(
                user=self.user,
                rank=4,
                review_text="Good business!",
            )

    def test_default_rank_value(self):
        """Test the default value of the rank field"""
        review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            review_text="Average business.",
        )
        self.assertEqual(review.rank, 3)  # The default should be 3

    def test_review_str_method(self):
        """Test the __str__ method for Review"""
        review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            rank=4,
            review_text="Nice business!",
        )
        self.assertEqual(str(review), f"{self.user} - {self.business}")


class VoteModelTestCase(TestCase):
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

    def test_create_vote(self):
        """Test creating a Vote record correctly"""
        vote = Vote.objects.create(
            user=self.user,
            review=self.review,
        )
        self.assertEqual(vote.user, self.user)
        self.assertEqual(vote.review, self.review)

    def test_vote_without_user(self):
        """Test creating a Vote without a user, which should raise an error"""
        with self.assertRaises(IntegrityError):
            Vote.objects.create(review=self.review)

    def test_vote_without_review(self):
        """Test creating a Vote without a review, which should raise an error"""
        with self.assertRaises(IntegrityError):
            Vote.objects.create(user=self.user)


class ReviewResponseModelTestCase(TestCase):
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

    def test_create_review_response(self):
        """Test creating a ReviewResponse record correctly"""
        response = ReviewResponse.objects.create(
            review=self.review,
            description="Thank you for your feedback!",
        )
        self.assertEqual(response.review, self.review)
        self.assertEqual(response.description, "Thank you for your feedback!")

    def test_review_response_str_method(self):
        """Test the __str__ method for ReviewResponse"""
        response = ReviewResponse.objects.create(
            review=self.review,
            description="Thanks for the review!",
        )
        self.assertEqual(str(response), f"{self.review}")


class ReportModelTestCase(TestCase):
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

    def test_create_report(self):
        """Test creating a Report record correctly"""
        report = Reports.objects.create(
            review_id=self.review,
            review_user_id=self.user,
            reason_select=ReasonReport.VIOLENCE.value,
            reason="Inappropriate content.",
        )
        self.assertEqual(report.review_id, self.review)
        self.assertEqual(report.review_user_id, self.user)
        self.assertEqual(report.reason_select, ReasonReport.VIOLENCE.value)
        self.assertEqual(report.reason, "Inappropriate content.")

    def test_report_without_review(self):
        """Test creating a Report without a review, which should raise an error"""
        with self.assertRaises(IntegrityError):
            Reports.objects.create(
                review_user_id=self.user,
                reason_select=ReasonReport.VIOLENCE.value,
                reason="Inappropriate content.",
            )

    def test_report_without_user(self):
        """Test creating a Report without a user, which should raise an error"""
        with self.assertRaises(IntegrityError):
            Reports.objects.create(
                review_id=self.review,
                reason_select=ReasonReport.VIOLENCE.value,
                reason="Inappropriate content.",
            )

    def test_report_str_method(self):
        """Test the __str__ method for Report"""
        report = Reports.objects.create(
            review_id=self.review,
            review_user_id=self.user,
            reason_select=ReasonReport.ACCUSATIONS.value,
            reason="False claims.",
        )
        self.assertEqual(str(report), f"{self.review}-{ReasonReport.ACCUSATIONS.value}")
