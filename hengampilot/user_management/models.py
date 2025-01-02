from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
    BaseUserManager,
)
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from .managers import UserMnagers

# Custom User model that extends AbstractBaseUser and PermissionsMixin
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

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=50, unique=True, help_text="Ehsan")
    user_image = models.ImageField(
        upload_to="user_images/",
        validators=[validate_image_size, validate_image_dimensions],
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=50, blank=True, null=True, help_text="First Name"
    )
    last_name = models.CharField(
        max_length=50, blank=True, null=True, help_text="Last Name"
    )

    hidden = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserMnagers()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    # String representation of the user (return email)
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


# Notifications model for storing notifications for each user
class Notifications(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user_notifications = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="user_notifications",
        null=False,
        blank=False,
    )

    is_read = models.BooleanField(default=False)

    notofication_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the notification (show the user associated with it)
    def __str__(self):
        return f"{self.user_notifications}"
