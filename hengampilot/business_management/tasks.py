from celery import shared_task
from .models import Subscription, SubscriptionType


# Celery task to manage subscription actions (activate, deactivate, change type)
@shared_task
def manage_subscription(subscription_id, action, subscription_type=None):
    try:
        # Try to fetch the subscription by its ID
        subscription = Subscription.objects.get(id=subscription_id)

        # Handle action for activating the subscription
        if action == "activate":
            # Check if the subscription is already active
            if not subscription.is_active:
                subscription.is_active = True
                subscription.save()  # Save the updated subscription
                return f"Subscription {subscription_id} activated successfully."
            return f"Subscription {subscription_id} is already active."

        # Handle action for deactivating the subscription
        elif action == "deactivate":
            # Check if the subscription is already inactive
            if subscription.is_active:
                subscription.is_active = False
                subscription.save()  # Save the updated subscription
                return f"Subscription {subscription_id} deactivated successfully."
            return f"Subscription {subscription_id} is already inactive."

        # Handle action for changing the subscription type
        elif action == "change_type":
            if subscription_type:
                # Validate the provided subscription type
                if subscription_type not in [tag.value for tag in SubscriptionType]:
                    return f"Invalid subscription type {subscription_type}."
                subscription.type = subscription_type
                subscription.save()  # Save the updated subscription
                return f"Subscription {subscription_id} type changed to {subscription_type}."
            return "Subscription type must be provided for change_type action."

        else:
            return "Invalid action specified."

    except Subscription.DoesNotExist:
        # If the subscription does not exist, handle the exception
        return f"Subscription with ID {subscription_id} not found."
