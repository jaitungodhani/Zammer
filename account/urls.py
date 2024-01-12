from django.urls import path, include
from .views import LoginView, RefreshTokenView
from rest_framework import routers
from .views import UserManagerView, GoogleSocialAuthView

router = routers.DefaultRouter()
router.register("usermanage", UserManagerView)


urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view()),
    path("refresh_token/", RefreshTokenView.as_view()),
    path("goole_social_auth/", GoogleSocialAuthView.as_view()),
]
