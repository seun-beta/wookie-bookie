from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.books.models import Book
from apps.books.serializers import BookListSerializer, BookSerializer
from apps.utility.permissions import IsAuthor


class BookListView(ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all().select_related()
    permission_classes = []


class CreateBookView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().select_related()
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class BookIDView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().select_related()
    permission_classes = [IsAuthenticated, IsAuthor]
    parser_classes = [MultiPartParser, FormParser]
