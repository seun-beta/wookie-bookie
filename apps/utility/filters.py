import django_filters as filters

from apps.books.models import Book


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name="author__username", lookup_expr="icontains")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    created_at = filters.IsoDateTimeFilter(field_name="created_at")
    updated_at = filters.IsoDateTimeFilter(field_name="updated_at")

    start_date = filters.DateFilter(field_name="created_at", lookup_expr="date__gte")
    end_date = filters.DateFilter(field_name="created_at", lookup_expr="date__lte")

    class Meta:
        model = Book
        fields = [
            "author",
            "title",
            "created_at",
            "updated_at",
            "start_date",
            "end_date",
        ]
