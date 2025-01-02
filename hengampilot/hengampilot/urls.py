from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # Admin panel URL
    path("admin/", admin.site.urls),

    # URLs for user management (included from the user_management app)
    path(
        "user_management/", include("user_management.urls", namespace="user_management")
    ),

    # URLs for business management (included from the business_management app)
    path(
        "business_management/",
        include("business_management.urls", namespace="business_management"),
    ),

    # URLs for platform management (included from the platform_management app)
    path("platform/", include(("platform_management.urls", "platform_management"))),

    # URLs for review and rating (included from the review_rating app)
    path("review_rating/", include("review_rating.urls", namespace="review_rating")),

    # URLs for analytics (included from the analytics app)
    path("analytics/", include("analytics.urls", namespace="analytics")),

    # API Schema generation endpoints
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    # Swagger UI for API documentation
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    
    # ReDoc for API documentation
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    # JWT authentication token endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

