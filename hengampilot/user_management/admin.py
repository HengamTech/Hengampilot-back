from django.contrib import admin
from .models import User, Notifications

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",  
        "username",  
        "hidden",  
        "is_active",  
        "is_admin",  
        "is_superuser",  
    ]

    list_filter = [
        "hidden",  
        "is_active",  
        "is_admin",  
        "is_superuser", 
        "created_at",  
    ]

    search_fields = ["username", "email"]  


# Custom admin configuration for the Notifications model
class NotificationAdmin(admin.ModelAdmin):
    list_display = [
        "user_notifications",
        "is_read",
    ]  

    search_fields = [
        "user_notifications",  
    ]

    list_filter = ["created_at", "is_read"]  


admin.site.register(
    User, UserAdmin
)  
admin.site.register(
    Notifications, NotificationAdmin
)  
