from django.test import TestCase
from user_management.models import User
from django.core.exceptions import ValidationError


class UserManagerTests(TestCase):
    def test_create_user_success(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123",
            is_active=True,
        )

        self.assertIsNotNone(user)

    def test_create_user_success1(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123",
            is_active=True,
        )

        self.assertEqual(user.email, "test@example.com")

    def test_create_user_success2(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123",
            is_active=True,
        )

        self.assertEqual(user.username, "testuser")

    def test_create_user_success3(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123",
            is_active=True,
        )

        self.assertTrue(user.is_active)

    def test_create_user_success4(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123",
            is_active=True,
        )

        self.assertFalse(user.is_admin)

    def test_create_user_success5(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123",
            is_active=True,
        )

        self.assertFalse(user.is_superuser)

    def test_create_user_success6(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="password123",
            is_active=True,
        )

        self.assertTrue(user.check_password("password123"))

    def test_create_user_missing_email(self):
        with self.assertRaisesMessage(ValueError, "Users must have an email address"):
            User.objects.create_user(
                email=None, username="testuser", password="password123", is_active=True
            )

    def test_create_user_missing_username(self):
        with self.assertRaisesMessage(ValueError, "Users must have a username"):
            User.objects.create_user(
                email="test@example.com",
                username=None,
                password="password123",
                is_active=True,
            )

    def test_create_user_missing_password(self):
        with self.assertRaisesMessage(ValueError, "Users must have a password"):
            User.objects.create_user(
                email="test@example.com",
                username="testuser",
                password=None,
                is_active=True,
            )

    def test_create_superuser_success(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com", username="adminuser", password="adminpassword"
        )

        self.assertIsNotNone(superuser)
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertEqual(superuser.username, "adminuser")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.check_password("adminpassword"))

    def test_create_superuser_is_active_default(self):
        superuser = User.objects.create_superuser(
            email="admin2@example.com", username="adminuser2", password="adminpassword2"
        )

        self.assertTrue(superuser.is_active)

    def test_create_superuser_missing_fields(self):
        with self.assertRaisesMessage(ValueError, "Users must have an email address"):
            User.objects.create_superuser(
                email=None, username="adminuser", password="adminpassword"
            )

        with self.assertRaisesMessage(ValueError, "Users must have a username"):
            User.objects.create_superuser(
                email="admin@example.com", username=None, password="adminpassword"
            )

        with self.assertRaisesMessage(ValueError, "Users must have a password"):
            User.objects.create_superuser(
                email="admin@example.com", username="adminuser", password=None
            )
