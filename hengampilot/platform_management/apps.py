from django.apps import AppConfig

# Define the configuration for the 'platform_management' app
class PlatformManagementConfig(AppConfig):
    # Default field type for auto-incrementing primary keys
    default_auto_field = "django.db.models.BigAutoField"
    
    # The name of the application. This should match the app directory name
    name = "platform_management"
