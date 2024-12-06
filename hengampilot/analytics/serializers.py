from rest_framework import serializers
from .models import AuditLog

# Serializer for the AuditLog model to convert model instances to JSON format and validate data
class AuditLogSerializer(serializers.ModelSerializer):
    # Use StringRelatedField to represent the content_type as a string (human-readable representation)
    content_type = serializers.StringRelatedField()
    
    # Use StringRelatedField to represent the user as a string (human-readable representation of the User)
    user = serializers.StringRelatedField()

    class Meta:
        # Specify the model to be serialized
        model = AuditLog
        
        # Include all fields from the AuditLog model
        fields = '__all__'  # You can also specify specific fields like ['id', 'user', 'action_type'] if needed
