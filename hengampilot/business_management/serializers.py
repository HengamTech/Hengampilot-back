from rest_framework import serializers
from .models import Business, Subscription, Category
from review_rating.models import Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BusinessSerializer(serializers.ModelSerializer):
    # Custom fields for additional data
    average_rating = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    business_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = "__all__"
        read_only_fields = ("business_owner", "average_rank")

    # Calculate the average rating for the business
    def get_average_rating(self, obj):
        reviews = Review.objects.filter(business_id=obj)
        if reviews.exists():
            return sum(review.rank for review in reviews) / reviews.count()
        return 0

    # Count the total number of reviews for the business
    def get_total_reviews(self, obj):
        return Review.objects.filter(business_id=obj).count()

    # Generate the full URL for the business image
    def get_business_image_url(self, obj):
        request = self.context.get("request")
        if obj.business_image:
            return request.build_absolute_uri(obj.business_image.url)
        return None


class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            "business_image",
            "business_owner",
            "business_name",
            "description",
            "website_url",
            "business_category",
        )


class BusinessUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            "business_image",
            "business_owner",
            "business_name",
            "description",
            "website_url",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
