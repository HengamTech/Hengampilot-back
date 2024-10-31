from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .middleware import log_action

@receiver([post_save, post_delete])
def log_model_change(sender, instance, **kwargs):
    if hasattr(instance, '_meta') and not sender._meta.app_label == 'analytics':
        if 'created' in kwargs:
            action_type = 'CREATE' if kwargs['created'] else 'UPDATE'
        else:
            action_type = 'DELETE'
        
        user = getattr(instance, '_current_user', None)  # get current user from thread
        if user:
            log_action(user, action_type, instance)