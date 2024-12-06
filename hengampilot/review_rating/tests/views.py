# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from rest_framework.test import APIClient
# from review_rating.models import Review, Vote, Reports, ReviewResponse
# from user_management.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
# from uuid import uuid4

# class ReviewViewSetTestCase(APITestCase):
#     def setUp(self):
#         # Create a user for authentication
#         self.user = User.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             is_active=True
#         )
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)  # authenticate as the test user
#         self.url = reverse('review_rating:review-list')  # URL for reviews endpoint

#     def test_create_review(self):
#         # Test creating a new review
#         data = {
#             'user': str(self.user.id),
#             'business_id': str(uuid4()),  # You can replace this with a valid business id
#             'rank': 4,
#             'review_text': 'Great service!',
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_add_review_task(self):
#         # Test the custom action that triggers a review background task
#         add_review_url = reverse('review_rating:review-add_review')  # Custom action URL
#         data = {
#             'user': str(self.user.id),
#             'business_id': str(uuid4()),
#             'rank': 4,
#             'review_text': 'Excellent!',
#         }
#         response = self.client.post(add_review_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
#         self.assertEqual(response.data['message'], 'Review addition task initiated successfully')


# class VoteViewSetTestCase(APITestCase):
#     def setUp(self):
#         # Create a user and review
#         self.user = User.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             is_active=True
#         )
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         self.review = Review.objects.create(
#             user=self.user,
#             business_id=str(uuid4()),
#             rank=5,
#             review_text='Great product!'
#         )
#         self.url = reverse('review_rating:vote-list')

#     def test_create_vote(self):
#         # Test creating a new vote on a review
#         data = {
#             'user': str(self.user.id),
#             'review': str(self.review.id),
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class ReportsViewSetTestCase(APITestCase):
#     def setUp(self):
#         # Create a user and review
#         self.user = User.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             is_active=True
#         )
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         self.review = Review.objects.create(
#             user=self.user,
#             business_id=str(uuid4()),
#             rank=3,
#             review_text="Bad experience."
#         )
#         self.url = reverse('review_rating:reports-list')

#     def test_create_report(self):
#         # Test creating a new report on a review
#         data = {
#             'review_id': str(self.review.id),
#             'review_user_id': str(self.user.id),
#             'reason_select': 'violence',
#             'reason': 'Offensive content',
#             'result_report': 'Unchecked',
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_add_report_task(self):
#         # Test the custom action that triggers a report background task
#         add_report_url = reverse('review_rating:reports-add_report')  # Custom action URL
#         data = {
#             'review_id': str(self.review.id),
#             'review_user_id': str(self.user.id),
#             'reason_select': 'sexual',
#             'reason': 'Inappropriate content',
#         }
#         response = self.client.post(add_report_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
#         self.assertEqual(response.data['message'], 'Report creation task initiated successfully')


# class ReviewResponseViewSetTestCase(APITestCase):
#     def setUp(self):
#         # Create a user and review
#         self.user = User.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="testpassword",
#             is_active=True
#         )
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#         self.review = Review.objects.create(
#             user=self.user,
#             business_id=str(uuid4()),
#             rank=5,
#             review_text='Great product!'
#         )
#         self.url = reverse('review_rating:reviewresponse-list')

#     def test_create_review_response(self):
#         # Test creating a new review response
#         data = {
#             'review': str(self.review.id),
#             'description': 'Thank you for your feedback!',
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertE
