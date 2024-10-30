from django.contrib import admin

# Register your models here.

from .models import ActionHistory


class ActionHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "action_time",
        "user",
        "content_type",
        "object_id",
        "object_repr",
        "action_flag",
        "change_message",
    ]
    search_fields = ["user__username", "object_repr"]
    list_filter = ["action_time", "content_type", "action_flag"]


admin.site.register(ActionHistory, ActionHistoryAdmin)
