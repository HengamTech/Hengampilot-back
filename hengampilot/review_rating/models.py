from django.db import models
import uuid
from user_management.models import User
from enum import Enum


# Enum class to define the possible reasons for reporting a review.
class ReasonReport(Enum):
    SEXUAL = "sexual"  # Report reason for sexual content.
    VIOLENCE = "violence"  # Report reason for violence.
    ACCUSATIONS = "accusations"  # Report reason for accusations.
    TERRORISM = "terrorism"  # Report reason for terrorism-related content.


class ResultReport(Enum):
    Ignore = "ignore"
    Unchecked = "Unchecked"
    Remove = "Remove"
    User_Ban = "UserBan"


# Model for a review on a business.
class Review(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # Unique identifier for the review.
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_review"
    )  # User who posted the review.
    business_id = models.ForeignKey(
        "business_management.Business",
        on_delete=models.CASCADE,
        related_name="review_business",
    )  # The business being reviewed.
    rank = models.IntegerField(
        choices=[  # Rank choices for the review.
            (1, "Very Poor"),
            (2, "Poor"),
            (3, "Medium"),
            (4, "Good"),
            (5, "Very Good"),
        ],
        default=3,  # Default rank is "Medium".
    )
    review_text = models.TextField()  # The content of the review.
    hidden = models.BooleanField(default=False)  # If the review is hidden or not.
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the review was created.
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Timestamp when the review was last updated.

    def __str__(self):
        # String representation of the Review object (shows the user and business).
        return f"{self.user} - {self.business_id}"


# Model for a vote on a review.
class Vote(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # Unique identifier for the vote.
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_vote"
    )  # User who cast the vote.
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_vote"
    )  # Review being voted on.
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the vote was created.

    def __str__(self):
        # String representation of the Vote object (shows the user and review).
        return f"{self.user} - {self.review}"


# Model for a response to a review.
class ReviewResponse(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # Unique identifier for the response.
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_response"
    )  # Review being responded to.
    description = models.TextField()  # Content of the response.
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the response was created.

    def __str__(self):
        # String representation of the ReviewResponse object (shows the review being responded to).
        return f"{self.review}"


# Model for reports on reviews.
class Reports(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # Unique identifier for the report.
    review_id = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_report"
    )  # Review that is being reported.
    review_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_report"
    )  # User who is reporting.
    reason_select = models.CharField(
        max_length=256,
        choices=[
            (tag.value, tag.name) for tag in ReasonReport
        ],  # Choices for the reason of the report (from ReasonReport Enum).
        null=False,
        blank=False,
    )
    result_report = models.CharField(
        max_length=256,
        choices=[
            (tag.value, tag.name) for tag in ResultReport
        ],  # Choices for the result of the report (from ResultReport Enum).
        null=False,
        blank=False,
        default= ResultReport.Unchecked
    )
    reason = models.TextField()  # Description of why the review is being reported.
    create_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the report was created.

    def __str__(self):
        # String representation of the Report object (shows the review and reason for report).
        return f"{self.review_id}-{self.reason_select}"
