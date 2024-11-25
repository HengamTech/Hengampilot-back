from django.test import TestCase
from user_management.models import User
from platform_management.models import FeatureRequest, JobStatus
from django.core.exceptions import ValidationError
import uuid


class FeatureRequestModelTestCase(TestCase):

    def setUp(self):
        # ایجاد یک کاربر تست
        self.user = User.objects.create(username="testuserqqw", password="testpass")


    def test_create_feature_request(self):
        """تست ایجاد یک درخواست جدید"""
        feature_request = FeatureRequest.objects.create(
            user=self.user,  # کاربر به فیلد user اختصاص داده شده است
            description="This is a test feature request.",
        )
        self.assertEqual(feature_request.user, self.user)
        self.assertEqual(feature_request.status, JobStatus.PENDING.value)
        self.assertEqual(feature_request.description, "This is a test feature request.")

    # def test_feature_request_without_user(self):
    #     """تست خطا در صورت نبودن کاربر"""
    #     with self.assertRaises(ValueError):
    #         FeatureRequest.objects.create(
    #             user=None,
    #             description="This is a test feature request.",
    #         )

    def test_feature_request_without_description(self):
        """تست خطا در صورت نبودن توضیحات"""
        feature_request = FeatureRequest(
            user=self.user,
            description="",  # توضیحات خالی
        )
        with self.assertRaises(ValidationError):
            feature_request.full_clean()  # باید اعتبارسنجی را انجام دهد

    def test_status_default_value(self):
        """تست مقدار پیش‌فرض فیلد وضعیت"""
        feature_request = FeatureRequest.objects.create(
            user=self.user,
            description="This is a test feature request.",
        )
        self.assertEqual(feature_request.status, JobStatus.PENDING.value)

    def test_invalid_status_value(self):
        """تست مقدار نامعتبر برای فیلد وضعیت"""
        feature_request = FeatureRequest(
            user=self.user,
            description="This is a test feature request.",
            status="invalid_status",
        )
        with self.assertRaises(ValidationError):
            feature_request.full_clean()

    def test_str_method(self):
        """تست مقدار بازگشتی متد __str__"""
        feature_request = FeatureRequest.objects.create(
            user=self.user,
            description="This is a test feature request.",
            status=JobStatus.APPROVED.value,
        )
        self.assertEqual(
            str(feature_request), f"{self.user} - {JobStatus.APPROVED.value}"
        )
