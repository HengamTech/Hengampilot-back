from django.db import models
import uuid
from user_management.models import User
from enum import Enum
from user_management.models import User

class StatusCategory(Enum):
    GOLDEN = "golden"
    SILVER = "silver"
    TAN = "tan"


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="business_owner",
        null=False,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in StatusCategory],
        default=StatusCategory.TAN.value,
    )
    business_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    website_url = models.CharField(max_length=50, null=True, blank=True)
    average_rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.business_name} - {self.website_url}"