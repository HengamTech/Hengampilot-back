from django.db import models
import uuid
from user_management.models import User
from enum import Enum


class ReasonReport(Enum):
    SEXUAL = "sexual"
    VIOLENCE = "violence"
    ACCUSATIONS = "accusations"
    TERRORISM = "terrorism"


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_review")
    business_id = models.ForeignKey(
        "business_management.Business",
        on_delete=models.CASCADE,
        related_name="review_business",
    )
    rank = models.IntegerField(
        choices=[
            (1, "Very Poor"),
            (2, "Poor"),
            (3, "Medium"),
            (4, "Good"),
            (5, "Very Good"),
        ],
        default=3,
    )
    review_text = models.TextField()
    hidden = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.business_id}"


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_vote")
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_vote"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.review}"


class ReviewResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_response"
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.review}"


class Reports(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review_id = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_report"
    )
    review_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_report"
    )
    reson_select = models.CharField(
        max_length=20,
        choices=[(tag.value, tag.name) for tag in ReasonReport],
        null=False,
        blank=False,
    )
    reason = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.review_id}-{self.reson_select}"
