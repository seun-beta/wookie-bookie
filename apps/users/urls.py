from django.urls import path

from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import RegisterUserView

urlpatterns = [
    path("users/register/", RegisterUserView.as_view(), name="register"),
    path("users/login/", TokenObtainPairView.as_view(), name="login"),
    path(
        "users/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("users/logout", TokenBlacklistView.as_view(), name="logout"),
]
