from django.urls import path

from apps.books.views import BookIDView, BookListView, CreateBookView

urlpatterns = [
    path(
        "books/list-books",
        BookListView.as_view(),
        name="unautheticated_book_list",
    ),
    path("books/books", CreateBookView.as_view(), name="create_book"),
    path("books/book-id", BookIDView.as_view(), name="book_id"),
]
