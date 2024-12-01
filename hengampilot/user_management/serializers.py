from rest_framework import serializers
from .models import User, Notifications


# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Define which fields to include in the serialized representation
        fields = ("id", "email", "username", "password", "is_active", "created_at")
        # Make password field write-only for security (it should not be returned in responses)
        extra_kwargs = {"password": {"write_only": True}}

    # Method to create a new user
    def create(self, validated_data):
        # Create a user using the validated data and the custom manager's create_user method
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            # Set is_active flag to True (could be omitted as True is the default)
            is_active=True,  # Optional, default is True, but you can explicitly set it here
        )
        return user


# Serializer for the Notifications model
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        # Include all fields from the Notifications model in the serialized representation
        fields = "__all__"
