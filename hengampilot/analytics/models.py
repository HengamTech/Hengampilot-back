# analytics/models.py

from django.db import models
from user_management.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import uuid

# Model to store audit logs of user actions
class AuditLog(models.Model):
    # UUID field for primary key, automatically generated using uuid4
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ForeignKey to the User model to track which user performed the action
    user = models.ForeignKey(
        'user_management.User',  # Reference to the User model in 'user_management' app
        on_delete=models.SET_NULL,  # If the user is deleted, set the user field to null
        null=True
    )
    
    # The time when the action was performed
    action_time = models.DateTimeField(auto_now_add=True)
    
    # The type of action performed (e.g., create, update, delete)
    action_type = models.CharField(max_length=50)
    
    # ForeignKey to ContentType model to link to any model in the system (for generic relationships)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    
    # CharField to store the object ID that was affected by the action
    # This will be used for referencing any object in any model
    object_id = models.CharField(max_length=50)  # use plain CharField, treat generic UUIDs/IDs safely
    
    # GenericForeignKey to link the action to any model instance
    content_object = GenericForeignKey('content_type', 'object_id')
    
    # A field to store the changes made (e.g., JSON, string format for changes)
    changes = models.TextField(null=True)  # Ensuring no JSONField (changes will be stored as text)
    
    # IP address of the user performing the action
    ip_address = models.GenericIPAddressField(null=True)
    
    # The user agent (browser details) of the user performing the action
    user_agent = models.TextField(null=True)

    class Meta:
        # Define ordering by action_time (descending order: most recent actions first)
        ordering = ['-action_time']

    def __str__(self):
        # String representation for easy identification of the audit log entry
        return f"{self.user} - {self.action_type} on {self.content_type}"
