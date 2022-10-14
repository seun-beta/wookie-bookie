from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
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


class CreateBookView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().select_related()
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user).select_related()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class BookView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().select_related()
    permission_classes = [IsAuthenticated, IsAuthor]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = "id"
