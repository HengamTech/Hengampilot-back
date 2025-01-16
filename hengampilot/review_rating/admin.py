from django.contrib import admin
from .models import Review, Vote, ReviewResponse, Reports

# Register your models here.


# Custom Admin configuration for the Review model.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "business_id", "rank", "hidden"]
    list_filter = ["rank", "hidden"]
    search_fields = ["user", "business_id", "review_text"]


# Custom Admin configuration for the Vote model.
class VoteAdmin(admin.ModelAdmin):
    list_display = ["user", "review", "created_at"]
    list_filter = ["user", "review", "created_at"]
    search_fields = ["created_at", "user", "review"]


# Custom Admin configuration for the ReviewResponse model.
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


# Custom Admin configuration for the Reports model.
class ReportsAdmin(admin.ModelAdmin):
    list_display = [
        "review_id", 
        "review_user_id",  
        "reason_select",  
        "reason",  
        "create_at",  
    ]
    list_filter = ["reason_select", "review_id", "review_user_id", "create_at"]
    search_fields = ["review_user_id", "review_id", "reason_select"]


# Register the models with their custom admin configurations.
admin.site.register(Review, ReviewAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(ReviewResponse, ReviewResponseAdmin)
admin.site.register(Reports, ReportsAdmin)
