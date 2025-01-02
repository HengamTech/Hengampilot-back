from django.test import TestCase
from django.utils.timezone import now, timedelta
from user_management.models import User
from business_management.models import (
    Business,
    Subscription,
    Category,
    SubscriptionType,
)
from django.db import IntegrityError

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile


class BusinessModelTestCase1(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpass")
        self.category = Category.objects.create(category_name="Test Category")

    def test_create_business(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
        )
        self.assertEqual(business.business_name, "Test Business")
        self.assertEqual(business.business_owner, self.user)

    def test_business_without_name(self):
        business = Business(
            business_owner=self.user,
            business_category=self.category,
            description="This is a test description.",
            average_rank=4,
        )
        with self.assertRaises(ValidationError):
            business.clean()

    def test_delete_category_deletes_business(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
        )
        self.category.delete()
        with self.assertRaises(Business.DoesNotExist):
            Business.objects.get(id=business.id)

    def test_business_str_method(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
        )
        self.assertEqual(str(business), "Test Business - https://example.com")

    def test_business_image_valid_dimensions(self):
        image = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg"
        )
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
            business_image=image,
        )
        self.assertTrue(
            business.business_image.name.startswith("business_images/test_image")
        )

    def test_business_image_invalid_dimensions(self):
        image = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg"
        )
        business = Business(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
            business_image=image,
        )

        with self.assertRaises(ValidationError):
            business.full_clean()

    def test_create_business_without_image(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Business Without Image",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
        )
        self.assertIsNone(business.business_image.name)

    # def test_business_image_invalid_size(self):
    #     image = SimpleUploadedFile(
    #         "test_image.jpg",
    #         b"file_content" * 1024 * 1024,  # ایجاد تصویری با حجم بیش از 5MB
    #         content_type="image/jpeg"
    #     )
    #     with self.assertRaises(ValidationError):
    #         Business.objects.create(
    #             business_owner=self.user,
    #             business_category=self.category,
    #             business_name="Test Business",
    #             description="This is a test description.",
    #             website_url="https://example.com",
    #             average_rank=4,
    #             business_image=image
    #         )


class SubscriptionModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
        )

    def test_create_subscription(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        self.assertEqual(subscription.type, SubscriptionType.FREE.value)
        self.assertTrue(subscription.is_active)

    def test_delete_business_deletes_subscription(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        self.business.delete()
        with self.assertRaises(Subscription.DoesNotExist):
            Subscription.objects.get(id=subscription.id)

    def test_toggle_subscription_active_status(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.PREMIUM.value,
            end_date=now() + timedelta(days=30),
            is_active=True,
        )
        subscription.is_active = False
        subscription.save()

        subscription.refresh_from_db()
        self.assertFalse(subscription.is_active)

    def test_subscription_with_past_end_date(self):
        past_date = now() - timedelta(days=1)
        subscription = Subscription(
            business=self.business, type=SubscriptionType.FREE.value, end_date=past_date
        )
        with self.assertRaises(ValidationError):
            subscription.full_clean()

    def test_edit_subscription_type(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        subscription.type = SubscriptionType.PREMIUM.value
        subscription.save()

        subscription.refresh_from_db()
        self.assertEqual(subscription.type, SubscriptionType.PREMIUM.value)


class CategoryModelTestCase(TestCase):
    def test_create_category(self):
        category = Category.objects.create(category_name="Test Category")
        self.assertEqual(category.category_name, "Test Category")

    def test_category_without_name(self):
        category = Category()
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_delete_category(self):
        category = Category.objects.create(category_name="Test Category")
        category.delete()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=category.id)

    def test_category_name_length(self):
        category = Category(category_name="A" * 1300)
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_edit_category_name(self):
        category = Category.objects.create(category_name="Old Category")
        category.category_name = "Updated Category"
        category.save()

        category.refresh_from_db()
        self.assertEqual(category.category_name, "Updated Category")

    def test_category_name_too_long(self):
        """تست ایجاد دسته‌بندی با نام بیش از حد طولانی"""
        long_name = "A" * 257  # نام دسته‌بندی بیشتر از 256 کاراکتر
        category = Category(category_name=long_name)
        with self.assertRaises(ValidationError):
            category.full_clean()


def test_create_category_with_duplicate_name(self):
    Category.objects.create(category_name="Test Category")
    with self.assertRaises(IntegrityError):
        Category.objects.create(category_name="Test Category")
