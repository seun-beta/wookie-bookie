from django.urls import path

from apps.books.views import BookListView, BookView, ListCreateBookView

urlpatterns = [
    path(
        "books/non-auth-books/",
        BookListView.as_view(),
        name="non_auth_book_list",
    ),
    path("books/books/", ListCreateBookView.as_view(), name="list_create_book"),
    path("books/books/<str:id>/", BookView.as_view(), name="book_by_id"),
]
