from django.apps import AppConfig

# Configuration class for the 'business_management' app
class BusinessManagementConfig(AppConfig):
    # Set the default auto field type for primary keys to BigAutoField (64-bit integer)
    default_auto_field = "django.db.models.BigAutoField"
    
    # Set the name of the app (used by Django to reference the app)
    name = "business_management"
