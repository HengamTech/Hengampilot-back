from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, AbstractUser

# Create your models here.
from .managers import UserMnagers


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=50, unique=True)
    hidden = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserMnagers()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_admin


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

    def __str__(self):
        return f"{self.user_notifications}"
