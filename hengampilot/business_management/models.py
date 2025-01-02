from django.db import models
import uuid
from user_management.models import User
from enum import Enum
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError


def validate_image_dimensions(image):
    max_width = 1920  # Maximum width
    max_height = 1080  # Maximum height

    width, height = get_image_dimensions(image)

    if width > max_width or height > max_height:
        raise ValidationError(
            f"Image dimensions must not exceed {max_width}x{max_height} pixels."
        )


def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # Maximum size = 5MB
    if image.size > max_size:
        raise ValidationError("Image size must be 5MB or fewer.")


# Model representing a business entity
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
    business_image = models.ImageField(
        upload_to="business_images/",
        validators=[validate_image_size, validate_image_dimensions],
        null=True,
        blank=True,
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


# Enum class to define subscription types (FREE and PREMIUM)
class SubscriptionType(Enum):
    FREE = "free"
    PREMIUM = "premium"


# Model representing a subscription for a business
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


# Model representing a category of businesses
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    category_name = models.CharField(max_length=256,unique=True)
    category_image = models.ImageField(
        upload_to="category_image/",
        validators=[validate_image_size, validate_image_dimensions],
        null=True,
        blank=True,
    )

    def clean(self):
        if not self.category_name:
            raise ValidationError("Category name cannot be empty.")

    def __str__(self):
        return f"{self.category_name}"
