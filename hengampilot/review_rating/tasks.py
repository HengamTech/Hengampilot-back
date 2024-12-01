from celery import shared_task
from .models import Review, Reports
from .serializers import ReviewSerializer, ReportsSerializer
from rest_framework.response import Response
from user_management.models import User


@shared_task
def add_review_view(review_data):
    """
    Celery task to add a review asynchronously.
    This task accepts review data, validates it using the ReviewSerializer,
    and if valid, saves the review.
    """
    # Serialize the incoming review data
    serializer = ReviewSerializer(data=review_data)
    
    # Check if the serialized data is valid
    if serializer.is_valid():
        # Save the review to the database
        serializer.save()
        return "Review added successfully"  # Return success message
    return "Error adding review"  # Return failure message if data is invalid


@shared_task
def add_report_view(report_data):
    """
    Celery task to add a report for a specific review asynchronously.
    This task receives report data, validates it using the ReportsSerializer,
    and saves the report if valid.
    """
    # Serialize the incoming report data
    serializer = ReportsSerializer(data=report_data)
    
    # Check if the serialized data is valid
    if serializer.is_valid():
        # Save the report to the database
        serializer.save()
        return "Report added successfully"  # Return success message
    return "Error adding report"  # Return failure message if data is invalid


@shared_task
def create_report_for_review(review_id, user_id, reason, reason_select="accusations"):
    """
    Celery task to create a report for a specific review asynchronously.
    This task accepts a review ID, user ID, report reason, and optional reason type
    (defaults to "accusations"). It fetches the corresponding review and user,
    and creates a report entry for the review.
    """
    try:
        # Fetch the review using the provided review ID
        review = Review.objects.get(id=review_id)
        
        # Fetch the user using the provided user ID
        user = User.objects.get(id=user_id)
        
        # Create a new report for the review
        report = Reports.objects.create(
            review_id=review,
            review_user_id=user,
            reason=reason,
            reason_select=reason_select,
        )
        
        return f"Report for review {review_id} created successfully."  # Success message
    except Review.DoesNotExist:
        # If the review doesn't exist, return an error message
        return f"Review with ID {review_id} not found."
    except User.DoesNotExist:
        # If the user doesn't exist, return an error message
        return f"User with ID {user_id} not found."
