from django.contrib import admin
from .models import FeatureRequest

# Register your models here.

# Define a custom admin class for managing the FeatureRequest model in the Django admin panel
class FeatureRequestAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ["user", "status", "description"]
    
    # Add filter options for the 'status' field
    list_filter = [
        "status",  # Allows the admin user to filter feature requests by their status (e.g., Pending, Approved, etc.)
    ]
    
    # Add a search bar for searching by 'user' field (username)
    search_fields = [
        "user",  # Allows searching for feature requests by the user (usually the username)
    ]

# Register the FeatureRequest model and the custom admin configuration
admin.site.register(FeatureRequest, FeatureRequestAdmin)
