from django.utils.deprecation import MiddlewareMixin
from django.contrib.contenttypes.models import ContentType
from .models import AuditLog
import logging
from user_management.models import User
logger = logging.getLogger(__name__)


class AuditLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.audit_log_data = {
            "ip_address": request.META.get("REMOTE_ADDR", "0.0.0.0"),
            "user_agent": request.META.get("HTTP_USER_AGENT", "Unknown"),
        }

        if request.user.is_authenticated:
            request._current_user = request.user
            logger.debug(f"Set current user: {request.user}")


def log_action(user, action_type, instance, changes=None):
    logger.debug(f"Logging action: {action_type} for {instance} by {user}")
    audit_log_data = getattr(user, 'audit_log_data', {}) if user and hasattr(user, 'audit_log_data') else {}
    AuditLog.objects.create(
        user=user if isinstance(user, User) else None,  # اطمینان از اینکه user یا None باشد
        action_type=action_type,
        content_type=ContentType.objects.get_for_model(instance),
        object_id=str(instance.pk),
        changes=changes,
        ip_address=audit_log_data.get('ip_address', '0.0.0.0'),
        user_agent=audit_log_data.get('user_agent', 'Unknown')
    )