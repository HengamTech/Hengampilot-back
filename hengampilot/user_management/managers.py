from django.contrib.auth.models import BaseUserManager


# Custom manager for managing User model creation
class UserMnagers(BaseUserManager):

    # Method to create a regular user
    def create_user(self, email, username, password, is_active):
        # Check if the email is provided
        if not email:
            raise ValueError("Users must have an email address")

        # Check if the username is provided
        if not username:
            raise ValueError("Users must have a username")

        # Check if the password is provided
        if not password:
            raise ValueError("Users must have a password")

        # Create the user instance and normalize the email
        user = self.model(
            username=username,
            email=self.normalize_email(email),  # Normalize the email to lowercase
        )

        # Set the user's password
        user.set_password(password)

        # Set the user's active status
        user.is_active = is_active

        # Save the user to the database
        user.save(using=self._db)

        # Return the created user instance
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
