from django.contrib import admin
from .models import Business, Subscription

# Admin interface for managing Subscription model
class SubscriptionAdmin(admin.ModelAdmin):
    # Fields to display in the list view in the admin panel
    list_display = ["business", "type", "start_date", "end_date", "is_active"]
    
    # Fields that can be searched in the admin search bar
    search_fields = [
        "business",  # Allow searching by business name
    ]
    
    # Filters that can be applied in the admin panel to sort or narrow down the list
    list_filter = ["type", "is_active", "start_date", "end_date"]  # Filters for subscription type, activity status, and date range

# Admin interface for managing Business model
class BusinessAdmin(admin.ModelAdmin):
    # Fields to display in the list view in the admin panel
    list_display = [
        "business_owner",  # Name of the business owner
        "business_name",   # Name of the business
        "website_url",     # Website URL of the business
        "average_rank",    # Average ranking of the business
        "created_at",      # When the business record was created
        "updated_at",      # When the business record was last updated
    ]
    
    # Fields that can be searched in the admin search bar
    search_fields = ["business_owner", "business_name", "website_url"]  # Allow searching by owner, name, or website
    
    # Filters that can be applied in the admin panel to sort or narrow down the list
    list_filter = [
        "created_at",  # Filter by the date the business was created
        "updated_at",  # Filter by the date the business was last updated
    ]

# Register the Business model with the BusinessAdmin interface
admin.site.register(Business, BusinessAdmin)
