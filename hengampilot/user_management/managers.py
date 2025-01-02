from django.contrib.auth.models import BaseUserManager


# Custom manager for managing User model creation
class UserMnagers(BaseUserManager):

    # Method to create a regular user
    def create_user(
        self, email, username, password, is_active, first_name=None, last_name=None
    ):
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have a username")

        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            username=username,
            email=self.normalize_email(email),  # Normalize the email to lowercase
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)

        user.is_active = is_active

        user.save(using=self._db)

        return user

    # Method to create a superuser
    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, username,
        and password. Sets is_admin and is_superuser to True.
        """
        # Use the create_user method to create a regular user first
        user = self.create_user(
            email, username=username, password=password, is_active=True
        )

        # Set superuser flags to True
        user.is_admin = True
        user.is_superuser = True

        # Save the superuser to the database
        user.save(using=self._db)

        # Return the created superuser instance
        return user