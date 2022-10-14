from django.urls import path

from apps.books.views import BookListView, BookView, CreateBookView

urlpatterns = [
    path(
        "books/non-auth-books/",
        BookListView.as_view(),
        name="non_auth_book_list",
    ),
    path("books/books/", CreateBookView.as_view(), name="create_book"),
    path("books/books/<str:id>/", BookView.as_view(), name="book"),
]
