from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.books.urls import urlpatterns as books_urlpatterns
from apps.users.urls import urlpatterns as users_urlpatterns
from configurations.swagger_scheme_generator import SwaggerSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Wookie Bookie",
        default_version="v1",
        description="Wookie Bookie",
        contact=openapi.Contact(email="seunfunmi.adegoke@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=SwaggerSchemaGenerator,
)


urlpatterns = [
    path("admin/", admin.site.urls),
]


if settings.DEBUG is True:
    urlpatterns += [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]

urlpatterns.extend(users_urlpatterns)
urlpatterns.extend(books_urlpatterns)
admin.site.site_header = "Wookie Bookie"
