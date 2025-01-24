from django.contrib import admin
from .models import AuditLog


# Create a class to manage the AuditLog model in the admin panel
class AuditLogAdmin(admin.ModelAdmin):
    list_display = [
        "action_time",
        "user",
        "get_content_type",
        "object_id",
        "action_type",
        "changes",
        "ip_address",
    ]

    search_fields = ["user__username", "changes"]
    list_filter = ["action_time", "action_type"]
    readonly_fields = [
        "user",
        "action_time",
        "get_content_type",
        "object_id",
        "action_type",
        "changes",
        "ip_address",
        "user_agent",
    ]

    def get_content_type(self, obj):
        return str(obj.content_type)

    get_content_type.short_description = "Content Type"


# Register the AuditLog model with the custom AuditLogAdmin class
admin.site.register(AuditLog, AuditLogAdmin)
