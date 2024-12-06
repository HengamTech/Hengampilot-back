from django.db import models
import uuid
from user_management.models import User
from enum import Enum
from django.core.exceptions import ValidationError

# Define an Enum for JobStatus with the possible states for the feature request
class JobStatus(Enum):
    PENDING = "pending"   # Request is pending approval
    APPROVED = "approved" # Request has been approved
    REJECTED = "rejected" # Request has been rejected

# Define the FeatureRequest model
class FeatureRequest(models.Model):
    # Unique identifier for the feature request, generated using UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Foreign key to the User model, establishes a relationship between FeatureRequest and the User who submitted the request
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # If the user is deleted, also delete the feature requests they made
        related_name="user_request",  # Name to refer to related feature requests from a User object
        null=False,                  # The field cannot be null
        blank=False,                 # The field cannot be blank
    )
    
    # Description field for the feature request
    description = models.TextField(null=False, blank=False)  # Field cannot be null or blank

    # Status of the feature request, uses the JobStatus enum for predefined choices
    status = models.CharField(
        max_length=20,  # Max length for the status field
        choices=[(tag.value, tag.name) for tag in JobStatus],  # Choices are set to the values and names of the JobStatus enum
        default=JobStatus.PENDING.value,  # Default status is 'pending'
    )

    # String representation of the FeatureRequest object
    def __str__(self):
        return f"{self.user} - {self.status}"  # Returns a string like 'UserName - pending'

    # Custom validation for the 'description' field to ensure it's not empty
    def clean(self):
        if not self.description:
            raise ValidationError("Description cannot be empty.")  # Raises an error if description is empty
