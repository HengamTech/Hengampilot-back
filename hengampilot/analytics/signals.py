import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .middleware import log_action

logger = logging.getLogger(__name__)


@receiver([post_save, post_delete])
def log_model_change(sender, instance, **kwargs):
    if hasattr(instance, "_meta") and sender._meta.app_label != "analytics":
        action_type = (
            "CREATE"
            if kwargs.get("created")
            else "DELETE" if "created" not in kwargs else "UPDATE"
        )
        user = (
            getattr(instance, "_current_user", None) or "Anonymous"
        )  # مقدار پیش‌فرض برای کاربر
        logger.debug(f"Log model change: {action_type} for {instance} by {user}")
        log_action(user, action_type, instance)
