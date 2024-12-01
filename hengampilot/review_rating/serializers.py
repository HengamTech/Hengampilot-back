from rest_framework import serializers
from .models import Review, Vote, Reports, ReviewResponse


# Serializer for the Review model.
class ReviewSerializer(serializers.ModelSerializer):
    # The Meta class defines the model and the fields that should be serialized.
    class Meta:
        model = Review  # The model to serialize.
        fields = (
            "__all__"  # Include all fields of the Review model in the serialization.
        )


# Serializer for the Vote model.
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote  # The model to serialize.
        fields = "__all__"  # Include all fields of the Vote model in the serialization.


# Serializer for the ReviewResponse model.
class ReviewResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewResponse  # The model to serialize.
        fields = "__all__"  # Include all fields of the ReviewResponse model in the serialization.


# Serializer for the Reports model.
class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports  # The model to serialize.
        fields = (
            "__all__"  # Include all fields of the Reports model in the serialization.
        )
