from rest_framework import serializers
from .models import User, Notifications
from django.contrib.auth.password_validation import validate_password

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    # Add password validation
    password = serializers.CharField(write_only=True, required=False, allow_blank=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password", "is_active", "created_at")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_active=True,
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        
        # Check and update password if provided
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)  # Hash the password
        
        instance.save()
        return instance

# Serializer for the Notifications model
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"
