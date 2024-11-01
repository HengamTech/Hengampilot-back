from django.db import models
import uuid
from user_management.models import User
from enum import Enum
from user_management.models import User


class JobStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class FeatureRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_request",
        null=False,
        blank=True,
    )
    description = models.TextField(null=False, blank=False)
    status = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in JobStatus], # choices=[(tag.value, tag.name.capitalize()) for tag in JobStatus]
        default=JobStatus.PENDING.value,
    )

    def __str__(self):
        return f"{self.user} - {self.status}"
