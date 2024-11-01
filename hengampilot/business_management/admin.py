from django.contrib import admin
from .models import Business

class BusinessAdmin(admin.ModelAdmin):
    list_display = [
        "business_owner",
        "status",
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
        "status",
    ]


admin.site.register(Business, BusinessAdmin)
