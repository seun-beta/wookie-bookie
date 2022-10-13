from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.forms import UserChangeForm, UserCreationForm
from apps.users.models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["username"]
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "pkid",
        "id",
        "username",
        "first_name",
        "last_name",
        "author_pseudonym",
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    list_display_links = ["id", "username"]
    list_filter = ["username", "author_pseudonym"]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "author_pseudonym",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ["username", "author_pseudonym"]


admin.site.register(User, UserAdmin)
