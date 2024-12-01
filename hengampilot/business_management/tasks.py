# tasks.py

from celery import shared_task
from .models import Subscription, SubscriptionType


@shared_task
def manage_subscription(subscription_id, action, subscription_type=None):
    try:
        subscription = Subscription.objects.get(id=subscription_id)

        if action == "activate":
            if not subscription.is_active:
                subscription.is_active = True
                subscription.save()
                return f"Subscription {subscription_id} activated successfully."
            return f"Subscription {subscription_id} is already active."

        elif action == "deactivate":
            if subscription.is_active:
                subscription.is_active = False
                subscription.save()
                return f"Subscription {subscription_id} deactivated successfully."
            return f"Subscription {subscription_id} is already inactive."

        elif action == "change_type":
            if subscription_type:
                if subscription_type not in [tag.value for tag in SubscriptionType]:
                    return f"Invalid subscription type {subscription_type}."
                subscription.type = subscription_type
                subscription.save()
                return f"Subscription {subscription_id} type changed to {subscription_type}."
            return "Subscription type must be provided for change_type action."

        else:
            return "Invalid action specified."

    except Subscription.DoesNotExist:
        return f"Subscription with ID {subscription_id} not found."
