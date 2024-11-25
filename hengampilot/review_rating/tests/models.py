from django.test import TestCase
from user_management.models import User
from business_management.models import Business
from review_rating.models import Review, Vote, ReviewResponse, Reports, ReasonReport
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


class ReviewModelTestCase(TestCase):
    def setUp(self):
        """ایجاد کاربران و کسب و کار برای استفاده در تست‌ها"""
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_name="Test Business",
            business_owner=self.user,
            description="Test business description",
            average_rank=3,
        )

    def test_create_review(self):
        """تست ایجاد یک رکورد Review به درستی"""
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
        """تست ایجاد Review بدون کاربر که باید خطا دهد"""
        with self.assertRaises(IntegrityError):
            Review.objects.create(
                business_id=self.business,
                rank=4,
                review_text="Good business!",
            )

    def test_review_without_business(self):
        """تست ایجاد Review بدون کسب و کار که باید خطا دهد"""
        with self.assertRaises(IntegrityError):
            Review.objects.create(
                user=self.user,
                rank=4,
                review_text="Good business!",
            )

    def test_default_rank_value(self):
        """تست مقدار پیش‌فرض فیلد rank"""
        review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            review_text="Average business.",
        )
        self.assertEqual(review.rank, 3)  # پیش‌فرض باید 3 باشد

    def test_review_str_method(self):
        """تست متد __str__ برای Review"""
        review = Review.objects.create(
            user=self.user,
            business_id=self.business,
            rank=4,
            review_text="Nice business!",
        )
        self.assertEqual(str(review), f"{self.user} - {self.business}")


class VoteModelTestCase(TestCase):
    def setUp(self):
        """ایجاد کاربران و رای‌دهی برای استفاده در تست‌ها"""
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
        """تست ایجاد یک رکورد Vote به درستی"""
        vote = Vote.objects.create(
            user=self.user,
            review=self.review,
        )
        self.assertEqual(vote.user, self.user)
        self.assertEqual(vote.review, self.review)

    def test_vote_without_user(self):
        """تست ایجاد Vote بدون کاربر که باید خطا دهد"""
        with self.assertRaises(IntegrityError):
            Vote.objects.create(review=self.review)

    def test_vote_without_review(self):
        """تست ایجاد Vote بدون review که باید خطا دهد"""
        with self.assertRaises(IntegrityError):
            Vote.objects.create(user=self.user)


class ReviewResponseModelTestCase(TestCase):
    def setUp(self):
        """ایجاد کاربران و پاسخ به بررسی برای استفاده در تست‌ها"""
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
        """تست ایجاد یک رکورد ReviewResponse به درستی"""
        response = ReviewResponse.objects.create(
            review=self.review,
            description="Thank you for your feedback!",
        )
        self.assertEqual(response.review, self.review)
        self.assertEqual(response.description, "Thank you for your feedback!")

    def test_review_response_str_method(self):
        """تست متد __str__ برای ReviewResponse"""
        response = ReviewResponse.objects.create(
            review=self.review,
            description="Thanks for the review!",
        )
        self.assertEqual(str(response), f"{self.review}")


class ReportModelTestCase(TestCase):
    def setUp(self):
        """ایجاد کاربران و گزارش برای استفاده در تست‌ها"""
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
        """تست ایجاد یک رکورد Report به درستی"""
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
        """تست ایجاد Report بدون review که باید خطا دهد"""
        with self.assertRaises(IntegrityError):
            Reports.objects.create(
                review_user_id=self.user,
                reason_select=ReasonReport.VIOLENCE.value,
                reason="Inappropriate content.",
            )

    def test_report_without_user(self):
        """تست ایجاد Report بدون user که باید خطا دهد"""
        with self.assertRaises(IntegrityError):
            Reports.objects.create(
                review_id=self.review,
                reason_select=ReasonReport.VIOLENCE.value,
                reason="Inappropriate content.",
            )

    def test_report_str_method(self):
        """تست متد __str__ برای Report"""
        report = Reports.objects.create(
            review_id=self.review,
            review_user_id=self.user,
            reason_select=ReasonReport.ACCUSATIONS.value,
            reason="False claims.",
        )
        self.assertEqual(str(report), f"{self.review}-{ReasonReport.ACCUSATIONS.value}")
