from django.contrib import admin
from .models import User, Notifications

# Register your models here.


# Custom admin configuration for the User model
class UserAdmin(admin.ModelAdmin):
    # Fields to display in the list view of User records
    list_display = [
        "email",  # Display the user's email
        "username",  # Display the user's username
        "hidden",  # Display the user's hidden status
        "is_active",  # Display whether the user is active
        "is_admin",  # Display whether the user has admin privileges
        "is_superuser",  # Display whether the user is a superuser
    ]

    # Filters to apply in the list view
    list_filter = [
        "hidden",  # Filter by hidden status
        "is_active",  # Filter by active status
        "is_admin",  # Filter by admin status
        "is_superuser",  # Filter by superuser status
        "created_at",  # Filter by creation date
    ]

    # Fields to enable search functionality in the admin panel
    search_fields = ["username", "email"]  # Search by username or email


# Custom admin configuration for the Notifications model
class NotificationAdmin(admin.ModelAdmin):
    # Fields to display in the list view of Notifications records
    list_display = [
        "user_notifications",
        "is_read",
    ]  # Show notification text and read status

    # Fields to enable search functionality in the admin panel
    search_fields = [
        "user_notifications",  # Search by the notification text
    ]

    # Filters to apply in the list view
    list_filter = ["created_at", "is_read"]  # Filter by creation date and read status


# Register models with the admin site, using custom admin configurations
admin.site.register(
    User, UserAdmin
)  # Register the User model with custom UserAdmin configuration
admin.site.register(
    Notifications, NotificationAdmin
)  # Register the Notifications model with custom NotificationAdmin configuration
