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

    def test_activate_subscription_already_active(self):
        # Activate the subscription first
        self.subscription.is_active = True
        self.subscription.save()

        # Try to activate again
        result = manage_subscription(self.subscription.id, "activate")

        # Assert that the subscription is still active and proper message is returned
        self.assertTrue(self.subscription.is_active)
        self.assertEqual(
            result, f"Subscription {self.subscription.id} is already active."
        )

    def test_deactivate_subscription_already_inactive(self):
        # Make sure the subscription is inactive
        self.subscription.is_active = False
        self.subscription.save()

        # Try to deactivate again
        result = manage_subscription(self.subscription.id, "deactivate")

        # Assert that the subscription is still inactive and proper message is returned
        self.assertFalse(self.subscription.is_active)
        self.assertEqual(
            result, f"Subscription {self.subscription.id} is already inactive."
        )

    def test_invalid_subscription_type(self):
        # Try to change the subscription type to an invalid type
        result = manage_subscription(self.subscription.id, "change_type", subscription_type="INVALID_TYPE")

        # Assert that an invalid subscription type returns the correct error message
        self.assertEqual(result, "Invalid subscription type INVALID_TYPE.")

    def test_subscription_does_not_exist(self):
        # Try to manage a non-existent subscription
        result = manage_subscription(999999, "activate")  # Assuming ID 999999 does not exist

        # Assert that the proper error message is returned
        self.assertEqual(result, "Subscription with ID 999999 not found.")

    def test_change_subscription_type_to_valid(self):
        # Test changing subscription type to a valid type (e.g., PREMIUM)
        new_type = SubscriptionType.PREMIUM.value
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

    def test_subscription_with_no_action(self):
        # Test the scenario where no action is specified
        result = manage_subscription(self.subscription.id, "")
        self.assertEqual(result, "Invalid action specified.")