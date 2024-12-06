# from django.test import TestCase
# from django.db.utils import IntegrityError
# from user_management.models import User, Notifications


# class UserModelTestCase(TestCase):
#     def setUp(self):
#         """ایجاد یک کاربر برای استفاده در تست‌ها"""
#         self.user = User.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpass123",
#             is_active=True  # افزودن is_active به هنگام ایجاد کاربر
#         )
#     def test_create_user(self):
#         """تست ایجاد یک کاربر با مقدار صحیح"""
#         user = self.user
#         self.assertEqual(user.username, "testuser")
#         self.assertEqual(user.email, "testuser@example.com")
#         self.assertTrue(user.check_password("testpass123"))
#         self.assertFalse(user.hidden)
#         self.assertTrue(user.is_active)

#     def test_user_str_method(self):
#         """تست متد __str__ برای User"""
#         user = self.user
#         self.assertEqual(str(user), "testuser@example.com")

#     # def test_create_user_without_username(self):
#     #     """تست ایجاد کاربر بدون نام کاربری که باید خطا دهد"""
#     #     with self.assertRaises(ValueError):
#     #         User.objects.create_user(
#     #             email="testuser@example.com",
#     #             password="testpass123"
#     #         )

#     def test_user_permissions(self):
#         """تست بررسی دسترسی‌ها و مجوزها برای کاربر"""
#         user = self.user
#         self.assertTrue(user.has_perm("some_permission"))  # کاربر باید دسترسی سوپر یوزر داشته باشد
#         self.assertTrue(user.has_module_perms("some_app"))

# #     def test_is_staff_property(self):
# #         """تست ویژگی is_staff"""
# #         user = self.user
# #         self.assertFalse(user.is_staff)  # چون is_admin در حال حاضر False است


# # class NotificationsModelTestCase(TestCase):
# #     def setUp(self):
# #         """ایجاد یک کاربر و یک نوتیفیکیشن برای استفاده در تست‌ها"""
# #         self.user = User.objects.create_user(
# #             username="testuser",
# #             email="testuser@example.com",
# #             password="testpass123"
# #         )
# #         self.notification = Notifications.objects.create(
# #             user_notifications=self.user,
# #             notofication_text="This is a test notification",
# #         )

# #     def test_create_notification(self):
# #         """تست ایجاد یک نوتیفیکیشن با مقدار صحیح"""
# #         notification = self.notification
# #         self.assertEqual(notification.user_notifications, self.user)
# #         self.assertEqual(notification.notofication_text, "This is a test notification")
# #         self.assertFalse(notification.is_read)

# #     def test_notification_str_method(self):
# #         """تست متد __str__ برای Notification"""
# #         notification = self.notification
# #         self.assertEqual(str(notification), f"{self.user}")

# #     def test_notification_without_user(self):
# #         """تست ایجاد نوتیفیکیشن بدون کاربر که باید خطا دهد"""
# #         with self.assertRaises(IntegrityError):
# #             Notifications.objects.create(
# #                 notofication_text="This notification has no user"
# #             )

# #     def test_notification_with_read_flag(self):
# #         """تست تغییر وضعیت is_read برای نوتیفیکیشن"""
# #         notification = self.notification
# #         notification.is_read = True
# #         notification.save()
# #         self.assertTrue(notification.is_read)


