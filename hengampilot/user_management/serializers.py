from rest_framework import serializers
from .models import User, Notifications

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'is_active', 'created_at')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user



    def create(self, validated_data):
        # Create the user using validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            # Optional: You can explicitly pass the is_active flag if needed
            is_active=True,  # (This is optional, as the default is True)
        )
        return user
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'