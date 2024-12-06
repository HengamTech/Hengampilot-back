from rest_framework import serializers
from .models import FeatureRequest

class FeatureRequestSerializer(serializers.ModelSerializer):
    # Meta class defines the model and fields to be included in the serializer
    class Meta:
        model = FeatureRequest  # Specifies that the serializer is for the FeatureRequest model
        fields = '__all__'  # Includes all fields from the FeatureRequest model in the serializer
        # Uncomment the following line if you want 'user' and 'status' to be read-only fields
        # read_only_fields = ('user', 'status')  # 'user' and 'status' fields will be read-only for regular users
