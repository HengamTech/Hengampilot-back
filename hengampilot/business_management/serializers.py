from rest_framework import serializers
from .models import Business
from review_rating.models import Review

class BusinessSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ('business_owner', 'average_rank', 'status')

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(business_id=obj)
        if reviews.exists():
            return sum(review.rank for review in reviews) / reviews.count()
        return 0

    def get_total_reviews(self, obj):
        return Review.objects.filter(business_id=obj).count()

class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('business_name', 'description', 'website_url')

class BusinessUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('business_name', 'description', 'website_url')