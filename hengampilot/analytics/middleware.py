from django.utils.deprecation import MiddlewareMixin
from django.contrib.contenttypes.models import ContentType
from .models import AuditLog
import logging

logger = logging.getLogger(__name__)

# Create middleware for automatically logging actions
class AuditLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Add IP address and user agent data to the request object for use in logging
        request.audit_log_data = {
            'ip_address': request.META.get('REMOTE_ADDR'),  # Get IP address from request metadata
            'user_agent': request.META.get('HTTP_USER_AGENT'),  # Get user agent from request headers
        }

        # Add the current authenticated user to the request
        if request.user.is_authenticated:
            request._current_user = request.user
            # setattr(request, '_current_user', request.user)
            logger.debug(f"Set current user: {request.user}")

# Helper function to log user actions into the AuditLog model
def log_action(user, action_type, instance, changes=None):
    """
    Helper function to log actions such as create, update, or delete.
    This function records details like the user, action type, model instance, changes, 
    IP address, and user agent for auditing purposes.
    """
    logger.debug(f"Logging action: {action_type} for {instance} by {user}")

    AuditLog.objects.create(
        user=user,  # The user who performed the action
        action_type=action_type,  # The type of action (e.g., 'create', 'update', 'delete')
        content_type=ContentType.objects.get_for_model(instance),  # Get the content type for the model instance
        object_id=str(instance.pk),  # ID of the affected object
        changes=changes,  # The changes made (if any)
        ip_address= user.audit_log_data.get('ip_address') if user else None,# getattr(user, 'audit_log_data', {}).get('ip_address'),  # Get the IP address from the middleware
        user_agent= user.audit_log_data.get('user_agent') if user else None,# getattr(user, 'audit_log_data', {}).get('user_agent'),  # Get the user agent from the middleware
    )
