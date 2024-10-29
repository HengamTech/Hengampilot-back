from django.contrib import admin
from .models import Review, Vote, ReviewResponse, Reports

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "business_id", "rank", "hidden"]
    list_filter = ["rank", "hidden"]
    search_fields = ["user", "business_id", "review_text"]


class VoteAdmin(admin.ModelAdmin):
    list_display = ["user", "review", "created_at"]
    list_filter = ["user", "review", "created_at"]
    search_fields = ["created_at", "user", "review"]


class ReviewResponseAdmin(admin.ModelAdmin):
    list_display = [
        "review",
        "created_at",
        "description",
    ]
    list_filter = ["review", "created_at"]
    search_fields = [
        "review",
    ]


class ReportsAdmin(admin.ModelAdmin):
    list_display = [
        "review_id",
        "review_user_id",
        "reson_select",
        "reason",
        "create_at",
    ]
    list_filter = ["reson_select", "review_id", "review_user_id", "create_at"]
    search_fields = ["review_user_id", "review_id", "reson_select"]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(ReviewResponse, ReviewResponseAdmin)
admin.site.register(Reports, ReportsAdmin)
