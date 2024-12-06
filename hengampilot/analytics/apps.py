from django.apps import AppConfig

# Define the configuration class for the 'analytics' app
class AnalyticsConfig(AppConfig):
    # Specify the default auto field type for primary keys (BigAutoField is a 64-bit integer)
    default_auto_field = "django.db.models.BigAutoField"
    
    # Set the name of the app (this is used to refer to the app in Django)
    name = "analytics"

    # Override the 'ready' method to import the signals when the app is ready
    def ready(self):
        # Import the signals module, which will connect signal handlers to Django signals
        import analytics.signals
