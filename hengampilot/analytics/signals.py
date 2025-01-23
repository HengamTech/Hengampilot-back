import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .middleware import log_action

logger = logging.getLogger(__name__)

# Signal receiver function to log model changes (creation, update, and deletion)
@receiver([post_save, post_delete])  # Connect the signal to both post_save and post_delete signals
def log_model_change(sender, instance, **kwargs):
    # Check if the instance has a '_meta' attribute (to ensure it's a model instance)
    # And ensure the signal is not coming from the 'analytics' app (to avoid logging from this app)
    if hasattr(instance, '_meta') and sender._meta.app_label != 'analytics':
        
        # Determine the action type based on whether the instance was created or updated
        if 'created' in kwargs:
            action_type = 'CREATE' if kwargs['created'] else 'UPDATE'  # For post_save, check 'created' flag
        else:
            action_type = 'DELETE'  # For post_delete, the action type is always DELETE
        
        # Retrieve the user who performed the action (stored in the instance's '_current_user' attribute)
        user = getattr(instance, '_current_user', None)  # _current_user is assumed to be set by middleware
        logger.debug(f"Log model change: {action_type} for {instance} by {user}")
        log_action(user, action_type, instance)
