from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from .user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    auth_provider_choice = (("email", _("email")), ("google", _("google")))

    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=100)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=100)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    auth_provider = models.CharField(
        verbose_name=_("Auth Provider"),
        choices=auth_provider_choice,
        default="email",
        max_length=10,
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
