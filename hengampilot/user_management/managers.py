from django.contrib.auth.models import BaseUserManager

class UserMnagers(BaseUserManager):

    # Method to create a regular user
    def create_user(self, email, username, password, is_active):
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have a username")

        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            username=username,
            email=self.normalize_email(email),  # Normalize the email to lowercase
        )

        user.set_password(password)

        user.is_active = is_active

        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, email, password, **extra_fields)
