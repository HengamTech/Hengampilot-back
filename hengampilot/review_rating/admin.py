from django.contrib import admin
from .models import Review, Vote, ReviewResponse, Reports

# Register your models here.


# Custom Admin configuration for the Review model.
class ReviewAdmin(admin.ModelAdmin):
    # List the fields to display in the admin list view.
    list_display = ["user", "business_id", "rank", "hidden"]
    # Add filters to allow the admin user to filter reviews by rank and visibility.
    list_filter = ["rank", "hidden"]
    # Allow searching reviews by user, business ID, and review text.
    search_fields = ["user", "business_id", "review_text"]


# Custom Admin configuration for the Vote model.
class VoteAdmin(admin.ModelAdmin):
    # List the fields to display in the admin list view for votes.
    list_display = ["user", "review", "created_at"]
    # Add filters to filter votes by user, review, and creation date.
    list_filter = ["user", "review", "created_at"]
    # Allow searching for votes by creation date, user, and review.
    search_fields = ["created_at", "user", "review"]


# Custom Admin configuration for the ReviewResponse model.
class ReviewResponseAdmin(admin.ModelAdmin):
    # List the fields to display in the admin list view for review responses.
    list_display = [
        "review",  # Show the associated review.
        "created_at",  # Show the creation timestamp.
        "description",  # Show the response description.
    ]
    # Add filters to filter review responses by the review and creation date.
    list_filter = ["review", "created_at"]
    # Allow searching for review responses by review.
    search_fields = [
        "review",  # Allow searching by review ID.
    ]


# Custom Admin configuration for the Reports model.
class ReportsAdmin(admin.ModelAdmin):
    # List the fields to display in the admin list view for reports.
    list_display = [
        "review_id",  # Show the associated review ID.
        "review_user_id",  # Show the user who made the report.
        "reason_select",  # Show the reason for the report (e.g., 'sexual', 'violence').
        "reason",  # Show the description of the reason.
        "create_at",  # Show the creation date of the report.
    ]
    # Add filters to filter reports by reason, review, user, and creation date.
    list_filter = ["reason_select", "review_id", "review_user_id", "create_at"]
    # Allow searching reports by user, review ID, and reason.
    search_fields = ["review_user_id", "review_id", "reason_select"]


# Register the models with their custom admin configurations.
admin.site.register(Review, ReviewAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(ReviewResponse, ReviewResponseAdmin)
admin.site.register(Reports, ReportsAdmin)
