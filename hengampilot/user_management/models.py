from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
# Import custom manager for User model
from .managers import UserMnagers

# class UserMnagers(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         """
#         Creates and saves a User with the given username, email, and password.
#         """
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):

#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)
#         return self.create_user(username, email, password, **extra_fields)


# Custom User model that extends AbstractBaseUser and PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
    # Unique identifier for the user (UUID)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # User's email address (must be unique)
    email = models.EmailField(max_length=30, unique=True)
    # Username for the user (must be unique)
    username = models.CharField(max_length=50, unique=True, help_text="Ehsan")
    # First name and last name
    first_name = models.CharField(max_length=50, blank=True, null=True, help_text="First Name")
    last_name = models.CharField(max_length=50, blank=True, null=True, help_text="Last Name")
    # Profile picture
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, help_text="Profile Picture")
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

    # @property
    # def is_staff(self):
    #     return self.is_admin Cuz it was pre defined and certain by super user admin!!
    # Add is_staff as a field instead of a property
    is_staff = models.BooleanField(default=False)
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
