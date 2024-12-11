from django.test import TestCase
from business_management.models import Subscription, SubscriptionType, Business
from user_management.models import User
from business_management.tasks import manage_subscription
from django.utils import timezone
from datetime import timedelta


class SubscriptionTaskTests(TestCase):

    def setUp(self):
        # Create a User instance (business owner)
        self.user = User.objects.create(username="test_user", password="password123")

        # Create a Business instance linked to the User
        self.business = Business.objects.create(
            business_name="Test Business",
            description="This is a test business.",
            business_owner=self.user,
            average_rank=5,
        )

        # Create a Subscription instance for the business
        self.subscription = Subscription.objects.create(
            business=self.business,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=30),
            is_active=False,
        )

    def test_activate_subscription(self):
        # Test subscription activation
        result = manage_subscription(self.subscription.id, "activate")

        # Refresh the subscription from the database
        self.subscription.refresh_from_db()

        # Assert that the subscription is now active
        self.assertTrue(self.subscription.is_active)
        self.assertEqual(
            result, f"Subscription {self.subscription.id} activated successfully."
        )

    def test_deactivate_subscription(self):
        # First, activate the subscription
        self.subscription.is_active = True
        self.subscription.save()

        # Test subscription deactivation
        result = manage_subscription(self.subscription.id, "deactivate")

        # Refresh the subscription from the database
        self.subscription.refresh_from_db()

        # Assert that the subscription is now inactive
        self.assertFalse(self.subscription.is_active)
        self.assertEqual(
            result, f"Subscription {self.subscription.id} deactivated successfully."
        )

    def test_change_subscription_type(self):
        # Test changing subscription type
        new_type = (
            SubscriptionType.PREMIUM.value
        )  # Using value of the Enum for "premium"
        result = manage_subscription(
            self.subscription.id, "change_type", subscription_type=new_type
        )

        # Refresh the subscription from the database
        self.subscription.refresh_from_db()

        # Assert that the subscription type is updated
        self.assertEqual(self.subscription.type, new_type)
        self.assertEqual(
            result, f"Subscription {self.subscription.id} type changed to {new_type}."
        )

    def test_invalid_action(self):
        # Test invalid action scenario
        result = manage_subscription(self.subscription.id, "invalid_action")
        self.assertEqual(result, "Invalid action specified.")
