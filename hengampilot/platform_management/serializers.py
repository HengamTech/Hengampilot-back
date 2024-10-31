from rest_framework import serializers
from .models import FeatureRequest

class FeatureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureRequest
        fields = '__all__'
        # read_only_fields = ('user', 'status')  # admin mitoone manage kone