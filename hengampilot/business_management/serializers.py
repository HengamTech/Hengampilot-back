from rest_framework import serializers
from .models import Business, Subscription, Category
from review_rating.models import Review

class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category 
        fields = "__all__" # Include all fields of the Category model

# Serializer for Business model, including additional fields for average rating and total reviews
class BusinessSerializer(serializers.ModelSerializer):
    # Adding custom fields for average rating and total reviews
    average_rating = (
        serializers.SerializerMethodField()
    )  # Custom method field for average rating
    total_reviews = (
        serializers.SerializerMethodField()
    )  # Custom method field for total number of reviews

    class Meta:
        model = Business
        fields = "__all__"  # Include all fields of the Business model
        read_only_fields = (
            "business_owner",  # Make business_owner field read-only
            "average_rank",  # Make average_rank field read-only
        )

    # Method to calculate the average rating for the business
    def get_average_rating(self, obj):
        # Fetch all reviews for the given business
        reviews = Review.objects.filter(business_id=obj)
        # If there are reviews, calculate the average rating
        if reviews.exists():
            return sum(review.rank for review in reviews) / reviews.count()
        return 0  # Return 0 if there are no reviews

    # Method to get the total number of reviews for the business
    def get_total_reviews(self, obj):
        # Count the total number of reviews for the given business
        return Review.objects.filter(business_id=obj).count()


# Serializer for creating a new Business
class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            "business_image",
            "business_owner",  # Owner of the business (should be provided by the user)
            "business_name",  # Name of the business
            "description",  # Description of the business
            "website_url",  # URL of the business website (optional)
            "business_category"
        )


# Serializer for updating an existing Business
class BusinessUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            "business_image",
            "business_owner",  # Owner of the business (can be updated if necessary)
            "business_name",  # Name of the business (can be updated)
            "description",  # Description of the business (can be updated)
            "website_url",  # URL of the business website (can be updated)
        )


# Serializer for Subscription model (representing the subscription for a business)
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"  # Include all fields of the Subscription model

