from django.contrib.auth.models import BaseUserManager


class UserMnagers(BaseUserManager):
    def create_user(self, email, username, password,is_active):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an phone number")

        if not password:
            raise ValueError("Users must have an password")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, username=username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
