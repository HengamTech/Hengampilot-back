from django.db import models
import uuid


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="user_review"
    )
    business_id = models.ForeignKey(
        "Business", on_delete=models.CASCADE, related_name="review_business"
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


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_vote")
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_vote"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_response"
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
