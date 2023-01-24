from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.books.models import Book
from apps.books.serializers import BookListSerializer, BookSerializer
from apps.utility.filters import BookFilter
from apps.utility.pagination import BookPagination
from apps.utility.permissions import IsAuthor


class BookListView(ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all().select_related("author")
    permission_classes = []
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class ListCreateBookView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().select_related()
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def get_queryset(self) -> Book:
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Book.objects.none()

        return self.queryset.filter(author=self.request.user).select_related("author")

    def perform_create(self, serializer: dict) -> dict:
        return serializer.save(author=self.request.user)


class BookView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().select_related("author")
    permission_classes = [IsAuthenticated, IsAuthor]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = "id"
