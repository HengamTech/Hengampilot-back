from django.contrib import admin
from .models import AuditLog

# Create a class to manage the AuditLog model in the admin panel
class AuditLogAdmin(admin.ModelAdmin):
    # Fields to display in the list view in the admin panel
    list_display = [
        "action_time",  # Time the action took place
        "user",         # The user who performed the action
        "content_type", # The type of content that was modified
        "object_id",    # The ID of the object that was affected
        "action_type",  # The type of action (e.g., add, edit, delete)
        "changes",      # The changes that were made
        "ip_address"    # The IP address of the user
    ]
    
    # Fields that can be searched in the admin search bar
    search_fields = ["user__username", "changes"]
    
    # Filters that can be used to filter or sort the data in the admin panel
    list_filter = ["action_time", "content_type", "action_type"]
    
    # Fields that are read-only (non-editable)
    readonly_fields = [
        "user",         # The user who performed the action
        "action_time",  # The time the action was performed
        "content_type", # The content type that was affected
        "object_id",    # The object ID that was affected
        "action_type",  # The type of action (add/edit/delete)
        "changes",      # The changes made during the action
        "ip_address",   # The IP address of the user
        "user_agent"    # The user agent (browser details) of the user
    ]

# Register the AuditLog model with the custom AuditLogAdmin class
admin.site.register(AuditLog, AuditLogAdmin)
