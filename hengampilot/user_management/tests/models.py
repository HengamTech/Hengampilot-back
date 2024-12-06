from django.test import TestCase
from user_management.models import User
from django.db.utils import IntegrityError

class UserModelTest(TestCase):


    def test_create_user(self):
        """Test creating a user with the custom manager"""
        user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpassword123",
            is_active=True
        )
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpassword123"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        """Test creating a superuser with the custom manager"""
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            username="admin",
            password="adminpassword123"
        )
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertEqual(superuser.username, "admin")
        self.assertTrue(superuser.check_password("adminpassword123"))
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_superuser)

    def test_create_user_with_missing_email(self):
        """Test that creating a user without email raises a ValueError"""
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="",
                username="testuser",
                password="testpassword123",
                is_active=True
            )

    def test_create_user_with_missing_username(self):
        """Test that creating a user without username raises a ValueError"""
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="testuser@example.com",
                username="",
                password="testpassword123",
                is_active=True
            )

    def test_str_method(self):
        """Test the string representation of the user"""
        user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpassword123",
            is_active=True
        )
        self.assertEqual(str(user), "testuser@example.com")

    def test_permissions(self):
        """Test user permissions based on is_superuser and is_admin"""
        user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpassword123",
            is_active=True
        )
        self.assertFalse(user.has_perm("can_edit"))
        self.assertFalse(user.has_module_perms("app_name"))

        superuser = User.objects.create_superuser(
            email="admin@example.com",
            username="admin",
            password="adminpassword123"
        )
        self.assertTrue(superuser.has_perm("can_edit"))
        self.assertTrue(superuser.has_module_perms("app_name"))


from django.test import TestCase
from user_management.models import User, Notifications
import uuid
from django.utils import timezone

class NotificationsModelTest(TestCase):

    def setUp(self):
        """Create a user instance for testing"""
        self.user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpassword123",
            is_active=True
        )

    def test_create_notification(self):
        """Test creating a notification"""
        notification = Notifications.objects.create(
            user_notifications=self.user,
            notofication_text="This is a test notification"
        )
        self.assertEqual(notification.user_notifications, self.user)
        self.assertEqual(notification.notofication_text, "This is a test notification")
        self.assertFalse(notification.is_read)  # Default should be False
        self.assertIsInstance(notification.created_at, timezone.datetime)  # should be a DateTime

    def test_str_method(self):
        """Test the string representation of the notification"""
        notification = Notifications.objects.create(
            user_notifications=self.user,
            notofication_text="Test notification"
        )
        self.assertEqual(str(notification), "testuser@example.com")  # This uses user_notifications' email field

    def test_notification_is_read_default(self):
        """Test that a newly created notification has is_read=False by default"""
        notification = Notifications.objects.create(
            user_notifications=self.user,
            notofication_text="Test notification"
        )
        self.assertFalse(notification.is_read)

    def test_foreign_key_relation(self):
        """Test the ForeignKey relationship between Notifications and User"""
        notification = Notifications.objects.create(
            user_notifications=self.user,
            notofication_text="Test notification"
        )
        self.assertEqual(notification.user_notifications, self.user)
        self.assertEqual(self.user.user_notifications.count(), 1)
