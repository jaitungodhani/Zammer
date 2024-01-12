from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from .views import UserManagerView, GoogleSocialAuthView

router = routers.DefaultRouter()
router.register("usermanage", UserManagerView)


urlpatterns = [
    path("", include(router.urls)),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh_token/", TokenRefreshView.as_view()),
    path("goole_social_auth/", GoogleSocialAuthView.as_view()),
]
