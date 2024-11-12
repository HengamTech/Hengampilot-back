from django.contrib import admin
from .models import Business, Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["business", "type", "start_date", "end_date", "is_active"]
    search_fields = [
        "business",
    ]
    list_filter = ["type", "is_active", "start_date", "end_date"]


class BusinessAdmin(admin.ModelAdmin):
    list_display = [
        "business_owner",
        "business_name",
        "website_url",
        "average_rank",
        "created_at",
        "updated_at",
    ]
    search_fields = ["business_owner", "business_name", "website_url"]
    list_filter = [
        "created_at",
        "updated_at",
    ]


admin.site.register(Business, BusinessAdmin)
