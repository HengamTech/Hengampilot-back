from django.db import models
import uuid
from user_management.models import User


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_owner = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="business_owner",
        null=False,
        blank=True,
    )
    business_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextChoices(null=False, blank=False)
    website_url = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
