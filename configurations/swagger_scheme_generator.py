from django.conf import settings

from drf_yasg.generators import OpenAPISchemaGenerator


class SwaggerSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"] if settings.DEBUG else ["https", "http"]
        return schema
