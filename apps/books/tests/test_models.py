from apps.books.models import Book
from apps.books.tests.base import BaseTest


class TestBookModel(BaseTest):
    """Define test for book model."""

    def test_book_model_attr(self):
        """Test that all book model attributes are accurate."""
        user = self.user.objects.create_user(**self.user_attr)
        book = Book.objects.create(**self.book_attr, author=user)
        book_obj = Book.objects.get(pkid=book.pkid)
        self.assertEqual(book_obj.title, book.title)
        self.assertEqual(book_obj.description, book.description)
        self.assertEqual(book_obj.cover_image, book.cover_image)
        self.assertEqual(book_obj.price, book.price)
        self.assertEqual(book_obj.author, book.author)
