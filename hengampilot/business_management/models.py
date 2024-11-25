from django.db import models
import uuid
from user_management.models import User
from enum import Enum
from user_management.models import User
from django.core.exceptions import ValidationError


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    business_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="business_owner",
        null=False,
        blank=False,
    )

    business_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    website_url = models.CharField(max_length=50, null=True, blank=True)
    average_rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business_name} - {self.website_url}"

    def clean(self):
        if not self.business_name:
            raise ValidationError("Business name cannot be empty.")


class SubscriptionType(Enum):
    FREE = "free"
    PREMIUM = "premium"


class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="subscriptions"
    )
    type = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in SubscriptionType],
        default=SubscriptionType.FREE.value,
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.business.business_name} - {self.type}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=256)
    def clean(self):
        if not self.category_name:
            raise ValidationError("Category name cannot be empty.")
