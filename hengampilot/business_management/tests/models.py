from django.test import TestCase
from django.utils.timezone import now, timedelta
from user_management.models import User
from business_management.models import Business, Subscription, Category, SubscriptionType
from django.core.exceptions import ValidationError


class BusinessModelTestCase(TestCase):
    def setUp(self):
        # ایجاد یک کاربر تست
        self.user = User.objects.create(username="testuser", password="testpass")
        # ایجاد یک دسته‌بندی تست
        self.category = Category.objects.create(category_name="Test Category")

    def test_create_business(self):
        """تست ایجاد موفقیت‌آمیز یک کسب‌وکار"""
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
        """تست عدم ایجاد کسب‌وکار بدون نام"""
        business = Business(
            business_owner=self.user,
            business_category=self.category,
            description="This is a test description.",
            average_rank=4,
        )
        with self.assertRaises(ValidationError):
            business.clean()


    def test_delete_category_deletes_business(self):
        """تست حذف دسته‌بندی و تأثیر آن بر کسب‌وکار مرتبط"""
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
        """تست متد __str__ مدل Business"""
        business = Business.objects.create(
            business_owner=self.user,
            business_category=self.category,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
        )
        self.assertEqual(str(business), "Test Business - https://example.com")


class SubscriptionModelTestCase(TestCase):
    def setUp(self):
        # ایجاد یک کاربر و کسب‌وکار تست
        self.user = User.objects.create(username="testuser", password="testpass")
        self.business = Business.objects.create(
            business_owner=self.user,
            business_name="Test Business",
            description="This is a test description.",
            website_url="https://example.com",
            average_rank=4,
        )

    def test_create_subscription(self):
        """تست ایجاد اشتراک"""
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        self.assertEqual(subscription.type, SubscriptionType.FREE.value)
        self.assertTrue(subscription.is_active)





    def test_delete_business_deletes_subscription(self):
        """تست حذف کسب‌وکار و تأثیر آن بر اشتراک مرتبط"""
        subscription = Subscription.objects.create(
            business=self.business,
            type=SubscriptionType.FREE.value,
            end_date=now() + timedelta(days=30),
        )
        self.business.delete()
        with self.assertRaises(Subscription.DoesNotExist):
            Subscription.objects.get(id=subscription.id)


class CategoryModelTestCase(TestCase):
    def test_create_category(self):
        """تست ایجاد موفقیت‌آمیز دسته‌بندی"""
        category = Category.objects.create(category_name="Test Category")
        self.assertEqual(category.category_name, "Test Category")

    def test_category_without_name(self):
        """تست عدم ایجاد دسته‌بندی بدون نام"""
        category = Category()  # بدون مقداردهی به `category_name`
        with self.assertRaises(ValidationError):
            category.full_clean()


    def test_delete_category(self):
        """تست حذف موفقیت‌آمیز دسته‌بندی"""
        category = Category.objects.create(category_name="Test Category")
        category.delete()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=category.id)

def test_category_name_length(self):
    """تست محدودیت طول نام دسته‌بندی"""
    category = Category(category_name="A" * 31)  # طول 31 کاراکتر
    with self.assertRaises(ValidationError):
        category.full_clean()

