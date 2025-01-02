from django.contrib import admin
from .models import Business, Subscription, Category


# Admin interface for managing Subscription model
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["business", "type", "start_date", "end_date", "is_active"]

    search_fields = [
        "business",
    ]

    list_filter = [
        "type",
        "is_active",
        "start_date",
        "end_date",
    ]


# Admin interface for managing Business model
class BusinessAdmin(admin.ModelAdmin):
    list_display = [
        "business_owner",
        "business_name",
        "website_url",
        "average_rank",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "business_owner",
        "business_name",
        "website_url",
    ]

    # Filters that can be applied in the admin panel to sort or narrow down the list
    list_filter = [
        "created_at",
        "updated_at",
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]
    list_filter = ["category_name"]


# Register the Business model with the BusinessAdmin interface
admin.site.register(Business, BusinessAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Category, CategoryAdmin)
