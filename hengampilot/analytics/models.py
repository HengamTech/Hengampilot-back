# analytics/models.py

from django.db import models
from user_management.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import uuid

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        'user_management.User',
        on_delete=models.SET_NULL,
        null=True
    )
    action_time = models.DateTimeField(auto_now_add=True)
    action_type = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=50)  # use plain CharField, treat generic UUIDs/IDs safely
    content_object = GenericForeignKey('content_type', 'object_id')  # Generic FK stays
    changes = models.TextField(null=True)  # Ensure no JSONField
    ip_address = models.GenericIPAddressField(null=True)
    user_agent = models.TextField(null=True)

    class Meta:
        ordering = ['-action_time']

    def __str__(self):
        return f"{self.user} - {self.action_type} on {self.content_type}"