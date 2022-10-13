import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(
        verbose_name=_("username"), db_index=True, max_length=256, unique=True
    )
    author_pseudonym = models.CharField(
        verbose_name=_("author_pseudonym"), db_index=True, max_length=256, unique=True
    )
    first_name = models.CharField(verbose_name=_("first name"), max_length=256)
    last_name = models.CharField(verbose_name=_("last name"), max_length=256)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "author_pseudonym",
        "first_name",
        "last_name",
    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def get_short_name(self):
        return self.first_name
