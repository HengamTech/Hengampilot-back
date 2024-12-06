from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, AbstractUser

# Import custom manager for User model
from .managers import UserMnagers


# Custom User model that extends AbstractBaseUser and PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
    # Unique identifier for the user (UUID)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # User's email address (must be unique)
    email = models.EmailField(max_length=30, unique=True)

    # Username for the user (must be unique)
    username = models.CharField(max_length=50, unique=True, help_text="Ehsan")

    # Whether the user is hidden or not
    hidden = models.BooleanField(default=False)

    # Whether the user account is active
    is_active = models.BooleanField(default=True)

    # Whether the user has admin privileges
    is_admin = models.BooleanField(default=False)

    # The timestamp when the user was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Whether the user is a superuser
    is_superuser = models.BooleanField(default=False)

    # Custom manager for user creation
    objects = UserMnagers()

    # Define the field used for authentication (username)
    USERNAME_FIELD = "username"

    # Fields required for user creation apart from the USERNAME_FIELD
    REQUIRED_FIELDS = ["email"]

    # String representation of the user (return email)
    def __str__(self):
        return self.email

    # Check if the user has specific permission (only superuser has all permissions)
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    # Check if the user has permissions for a specific app (only superuser has module perms)
    def has_module_perms(self, app_label):
        return self.is_superuser

    # Property to check if the user is a staff member (i.e. an admin user)
    @property
    def is_staff(self):
        return self.is_admin


# Notifications model for storing notifications for each user
class Notifications(models.Model):
    # Unique identifier for the notification (UUID)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # ForeignKey relation to the User model (notification is associated with a user)
    user_notifications = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="user_notifications",
        null=False,
        blank=False,
    )

    # Whether the notification has been read
    is_read = models.BooleanField(default=False)

    # Text content of the notification
    notofication_text = models.TextField()

    # Timestamp when the notification was created
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the notification (show the user associated with it)
    def __str__(self):
        return f"{self.user_notifications}"
