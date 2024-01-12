from .models import User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


def login_user(email, password):
    user = authenticate(email=email, password=password)
    user_token = TokenObtainPairSerializer.get_token(user)
    return {
        "refresh": str(user_token),
        "access": str(user_token.access_token),
        "user_data": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    }


def register_social_user(provider, first_name, last_name, email):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:
            return login_user(email, settings.GOOGLE_CLIENT_SECRET)
        else:
            raise AuthenticationFailed(
                detail="Please continue your login using "
                + filtered_user_by_email[0].auth_provider
            )

    else:
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": settings.GOOGLE_CLIENT_SECRET,
        }
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()
        return login_user(user.email, settings.GOOGLE_CLIENT_SECRET)
