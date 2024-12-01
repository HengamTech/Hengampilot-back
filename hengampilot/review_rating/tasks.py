from celery import shared_task
from .models import Review, Reports
from .serializers import ReviewSerializer, ReportsSerializer
from rest_framework.response import Response
from user_management.models import User


@shared_task
def add_review_view(review_data):
    serializer = ReviewSerializer(data=review_data)
    if serializer.is_valid():
        serializer.save()
        return "Review added successfully"
    return "Error adding review"


@shared_task
def add_report_view(report_data):
    """
    تسک برای افزودن گزارش برای یک نظر خاص
    """
    serializer = ReportsSerializer(data=report_data)
    if serializer.is_valid():
        serializer.save()
        return "Report added successfully"
    return "Error adding report"


@shared_task
def create_report_for_review(review_id, user_id, reason, reason_select="accusations"):
    """
    تسک برای ایجاد گزارش برای یک نظر خاص
    """
    try:
        review = Review.objects.get(id=review_id)
        user = User.objects.get(id=user_id)
        report = Reports.objects.create(
            review_id=review,
            review_user_id=user,
            reason=reason,
            reason_select=reason_select,
        )
        return f"Report for review {review_id} created successfully."
    except Review.DoesNotExist:
        return f"Review with ID {review_id} not found."
    except User.DoesNotExist:
        return f"User with ID {user_id} not found."
