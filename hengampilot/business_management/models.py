from django.db import models
import uuid
from user_management.models import User
from enum import Enum
from django.core.exceptions import ValidationError

# Model representing a business entity
class Business(models.Model):
    # UUID as the primary key for the business model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ForeignKey linking the business to a category (optional, can be null)
    business_category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    
    # ForeignKey linking the business to a business owner (User model)
    business_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="business_owner",  # Related name for reverse relation
        null=False,
        blank=False,
    )
    
    # Fields for business name, description, and website URL
    business_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    website_url = models.CharField(max_length=50, null=True, blank=True)
    
    # Average rank for the business
    average_rank = models.IntegerField()
    
    # Timestamps for when the business is created and last updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Return a string representation of the business
        return f"{self.business_name} - {self.website_url}"

    def clean(self):
        # Custom validation to ensure business name is not empty
        if not self.business_name:
            raise ValidationError("Business name cannot be empty.")

# Enum class to define subscription types (FREE and PREMIUM)
class SubscriptionType(Enum):
    FREE = "free"
    PREMIUM = "premium"

# Model representing a subscription for a business
class Subscription(models.Model):
    # UUID as the primary key for the subscription model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ForeignKey linking the subscription to a specific business
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="subscriptions"
    )
    
    # The type of subscription (either FREE or PREMIUM), using choices from SubscriptionType enum
    type = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in SubscriptionType],
        default=SubscriptionType.FREE.value,
    )
    
    # Subscription start and end dates
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    
    # Whether the subscription is currently active
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # Return a string representation of the subscription
        return f"{self.business.business_name} - {self.type}"

# Model representing a category of businesses
class Category(models.Model):
    # UUID as the primary key for the category model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Name of the category
    category_name = models.CharField(max_length=256)
    
    def clean(self):
        # Custom validation to ensure category name is not empty
        if not self.category_name:
            raise ValidationError("Category name cannot be empty.")
