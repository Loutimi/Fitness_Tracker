from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, UserViewSet, ActivityViewSet, LeaderboardViewSet, RegisterView, LoginView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('api/', include(router.urls)),  # Include all router URLs
    path('home/', home, name='home'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),  # Register endpoint
    path('api/auth/login/', LoginView.as_view(), name='login'),  # Login endpoint
    path('api/auth/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token obtain
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT Token refresh
    # DRF-Spectacular documentation URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # OpenAPI schema in JSON format
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # ReDoc UI
]
