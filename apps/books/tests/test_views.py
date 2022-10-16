# flake8: noqa
from django.urls import reverse

from djmoney.money import Money

from apps.books.models import Book
from apps.books.tests.base import BaseTest


class TestBookListView(BaseTest):
    """Test BookListView"""

    def test_list_books_for_un_authenticated_users(self):
        """Test list books for un-authenticated users"""

        user = self.user.objects.create_user(**self.user_attr)
        Book.objects.create(**self.book_attr, author=user)

        response = self.client.get(reverse("non_auth_book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], self.book_attr["title"])
        self.assertEqual(
            response.data["results"][0]["description"],
            self.book_attr["description"],
        )
        self.assertEqual(
            response.data["results"][0]["cover_image"],
            self.book_attr["cover_image"],
        )
        self.assertEqual(
            Money(response.data["results"][0]["price"], "USD"),
            self.book_attr["price"],
        )
        self.assertEqual(
            response.data["results"][0]["author_name"],
            self.author_name_attr["author_name"],
        )

    def test_list_books_for_un_authenticated_users_when_no_books_exist(self):
        """Test list books for un-authenticated users"""

        Book.objects.all().delete()

        response = self.client.get(reverse("non_auth_book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 0)


class TestCreateBookView(BaseTest):
    """Test CreateBookView"""

    def test_create_book_for_un_authenticated_users(self):
        """Test create books for un-authenticated users"""

        with open("apps/books/tests/test_image.png", "rb") as fp:

            response = self.client.post(
                reverse("list_create_book"),
                {
                    "title": "title",
                    "description": "title",
                    "price": 1234,
                    "cover_image": fp,
                },
            )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data["detail"],
            "Authentication credentials were not provided.",
        )

    def test_create_book_for_authenticated_users(self):
        """Test create books for authenticated users"""

        user = self.user.objects.create_user(**self.user_attr)
        self.client.force_authenticate(user=user)
        with open("apps/books/tests/test_image.png", "rb") as fp:
            book_data = self.book_with_image_attr
            book_data["cover_image"] = fp
            response = self.client.post(reverse("list_create_book"), book_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], self.book_with_image_attr["title"])
        self.assertEqual(
            response.data["description"],
            self.book_with_image_attr["description"],
        )
        self.assertIsNone(response.data["cover_image"])
        self.assertEqual(
            response.data["price"],
            self.book_with_image_attr["price"],
        )


class TestPatchBookView(BaseTest):
    """Test PatchBookView"""

    def test_patch_book_created_by_owner(self):
        """Test patch books created by owner"""

        user = self.user.objects.create_user(**self.user_attr)
        book = Book.objects.create(**self.book_attr, author=user)
        self.client.force_authenticate(user=user)
        with open("apps/books/tests/test_image.png", "rb") as fp:
            book_data = self.book_with_image_attr
            book_data["cover_image"] = fp

            response = self.client.patch(
                reverse("book_by_id", kwargs={"id": book.id}), book_data
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], self.book_with_image_attr["title"])
        self.assertEqual(
            response.data["description"],
            self.book_with_image_attr["description"],
        )
        self.assertIsNone(response.data["cover_image"])
        self.assertEqual(
            response.data["price"],
            self.book_with_image_attr["price"],
        )

    def test_patch_book_for_un_authenticated_users(self):
        """Test patch books for un-authenticated users"""

        user = self.user.objects.create_user(**self.user_attr)
        book = Book.objects.create(**self.book_attr, author=user)
        with open("apps/books/tests/test_image.png", "rb") as fp:
            book_data = self.book_with_image_attr
            book_data["cover_image"] = fp

            response = self.client.patch(
                reverse("book_by_id", kwargs={"id": book.id}), book_data
            )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data["detail"],
            "Authentication credentials were not provided.",
        )


class TestPutBookView(BaseTest):
    """Test PutBookView"""

    def test_put_book_created_by_owner(self):
        """Test put books created by owner"""

        user = self.user.objects.create_user(**self.user_attr)
        book = Book.objects.create(**self.book_attr, author=user)
        self.client.force_authenticate(user=user)

        with open("apps/books/tests/test_image.png", "rb") as fp:
            book_data = self.book_with_image_attr
            book_data["cover_image"] = fp

            response = self.client.put(
                reverse("book_by_id", kwargs={"id": book.id}), book_data
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], self.book_with_image_attr["title"])
        self.assertEqual(
            response.data["description"],
            self.book_with_image_attr["description"],
        )
        self.assertIsNone(response.data["cover_image"])
        self.assertEqual(
            response.data["price"],
            self.book_with_image_attr["price"],
        )

    def test_put_book_for_un_authenticated_users(self):
        """Test put books for un-authenticated users"""

        user = self.user.objects.create_user(**self.user_attr)
        book = Book.objects.create(**self.book_attr, author=user)

        with open("apps/books/tests/test_image.png", "rb") as fp:
            book_data = self.book_with_image_attr
            book_data["cover_image"] = fp

            response = self.client.put(
                reverse("book_by_id", kwargs={"id": book.id}), book_data
            )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data["detail"],
            "Authentication credentials were not provided.",
        )


class TestDeleteBookView(BaseTest):
    """Test DeleteBookView"""

    def test_delete_book_created_by_owner(self):
        """Test delete books created by owner"""

        user = self.user.objects.create_user(**self.user_attr)
        book = Book.objects.create(**self.book_attr, author=user)

        self.client.force_authenticate(user=user)
        response = self.client.delete(reverse("book_by_id", kwargs={"id": book.id}))

        self.assertEqual(response.status_code, 204)

    def test_delete_book_for_un_authenticated_users(self):
        """Test delete books for un-authenticated users"""

        user = self.user.objects.create_user(**self.user_attr)
        book = Book.objects.create(**self.book_attr, author=user)

        response = self.client.delete(reverse("book_by_id", kwargs={"id": book.id}))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data["detail"],
            "Authentication credentials were not provided.",
        )


class TestListCreateView(BaseTest):
    """Test BookListView"""

    def test_list_books_for_authenticated_users(self):
        """Test list books for authenticated users"""

        user = self.user.objects.create_user(**self.user_attr)
        Book.objects.create(**self.book_attr, author=user)

        self.client.force_authenticate(user=user)
        response = self.client.get(reverse("list_create_book"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], self.book_attr["title"])
        self.assertEqual(
            response.data["results"][0]["description"],
            self.book_attr["description"],
        )

        self.assertEqual(
            Money(response.data["results"][0]["price"], "USD"),
            self.book_attr["price"],
        )

    def test_list_books_for_un_authenticated_users(self):
        """Test list books for un-authenticated users"""

        user = self.user.objects.create_user(**self.user_attr)
        Book.objects.create(**self.book_attr, author=user)
        response = self.client.get(reverse("list_create_book"))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(
            response.data["detail"],
            "Authentication credentials were not provided.",
        )
