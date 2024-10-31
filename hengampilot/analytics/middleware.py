from django.utils.deprecation import MiddlewareMixin
from django.contrib.contenttypes.models import ContentType
from .models import AuditLog

# create middleware for automatically log actions !
class AuditLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.audit_log_data = {
            'ip_address': request.META.get('REMOTE_ADDR'),
            'user_agent': request.META.get('HTTP_USER_AGENT'),
        }

def log_action(user, action_type, instance, changes=None):
    """
    Helper function to log actions
    """
    AuditLog.objects.create(
        user=user,
        action_type=action_type,
        content_type=ContentType.objects.get_for_model(instance),
        object_id=str(instance.pk),
        changes=changes,
        ip_address=getattr(user, 'audit_log_data', {}).get('ip_address'),
        user_agent=getattr(user, 'audit_log_data', {}).get('user_agent'),
    )