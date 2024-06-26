from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from account.views import AccountView, JWTCookieTokenObtainPairView, JWTCookieTokenRefreshView, LogoutView, RegisterView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('token/', JWTCookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', JWTCookieTokenRefreshView.as_view(), name='token_refresh'),
    path('account/', AccountView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]