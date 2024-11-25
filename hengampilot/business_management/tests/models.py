from django.test import TestCase
from django.utils.timezone import now, timedelta
from user_management.models import User
from .models import Business, Subscription, Category, SubscriptionType
import uuid


class BusinessModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpass")
        self.category = Category.objects.create(category_name="Test Category")

    def test_create_business(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="A test description",
            website_url="https://test.com",
            average_rank=5,
        )
        self.assertEqual(business.business_name, "Test Business")

    def test_business_without_name(self):
        with self.assertRaises(ValueError):
            Business.objects.create(
                business_owner=self.user,
                business_category=self.category,
                description="A test description",
                average_rank=5,
            )

    def test_delete_category_deletes_business(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="A test description",
            website_url="https://test.com",
            average_rank=5,
        )
        self.category.delete()
        with self.assertRaises(Business.DoesNotExist):
            Business.objects.get(id=business.id)

    def test_delete_user_deletes_business(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="A test description",
            website_url="https://test.com",
            average_rank=5,
        )
        self.user.delete()
        with self.assertRaises(Business.DoesNotExist):
            Business.objects.get(id=business.id)

    def test_business_str(self):
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="A test description",
            website_url="https://test.com",
            average_rank=5,
        )
        self.assertEqual(str(business), "Test Business - https://test.com")

    def test_average_rank_negative_value(self):
        with self.assertRaises(ValueError):
            Business.objects.create(
                business_owner=self.user,
                business_category=self.category,
                business_name="Test Business",
                description="A test description",
                website_url="https://test.com",
                average_rank=-5,
            )


class SubscriptionModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="A test description",
            website_url="https://test.com",
            average_rank=5,
        )

    def test_create_subscription(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        self.assertTrue(subscription.is_active)

    def test_subscription_with_invalid_dates(self):
        with self.assertRaises(ValueError):
            Subscription.objects.create(
                business=self.business,
                type=SubscriptionType.FREE.value,
                end_date=now() - timedelta(days=1),
            )

    def test_subscription_str(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        self.assertEqual(
            str(subscription), f"{self.business.business_name} - free"
        )

    def test_subscription_premium_type(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.PREMIUM.value,
            end_date=now() + timedelta(days=30),
        )
        self.assertEqual(subscription.type, SubscriptionType.PREMIUM.value)

    def test_subscription_auto_deactivation(self):
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() - timedelta(days=1),
        )
        subscription.is_active = False
        subscription.save()
        self.assertFalse(subscription.is_active)

    def test_multiple_subscriptions_for_business(self):
        Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.PREMIUM.value,
            end_date=now() + timedelta(days=60),
        )
        self.assertEqual(self.business.subscriptions.count(), 2)


class CategoryModelTestCase(TestCase):
    def test_create_category(self):
        category = Category.objects.create(category_name="Test Category")
        self.assertEqual(category.category_name, "Test Category")

    def test_category_without_name(self):
        with self.assertRaises(ValueError):
            Category.objects.create()

    def test_delete_category(self):
        category = Category.objects.create(category_name="Test Category")
        category.delete()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=category.id)

    def test_duplicate_category_names(self):
        Category.objects.create(category_name="Test Category")
        with self.assertRaises(Exception):
            Category.objects.create(category_name="Test Category")

    def test_category_max_length(self):
        with self.assertRaises(ValueError):
            Category.objects.create(category_name="A" * 31)
