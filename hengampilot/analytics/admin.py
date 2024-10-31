from django.contrib import admin
from .models import AuditLog

class AuditLogAdmin(admin.ModelAdmin):
    list_display = [
        "action_time",
        "user",
        "content_type",
        "object_id",
        "action_type",
        "changes",
        "ip_address"
    ]
    search_fields = ["user__username", "changes"]
    list_filter = ["action_time", "content_type", "action_type"]
    readonly_fields = [
        "user",
        "action_time",
        "content_type",
        "object_id",
        "action_type",
        "changes",
        "ip_address",
        "user_agent"
    ]

admin.site.register(AuditLog, AuditLogAdmin)