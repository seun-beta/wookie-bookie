from django.contrib.auth import get_user_model

from djmoney.money import Money
from faker import Faker
from rest_framework.test import APIClient, APITestCase

from apps.books.models import Book

faker = Faker()


class BaseTest(APITestCase):
    """Base class for tests"""

    user = get_user_model()
    client = APIClient()

    def setUp(self):
        """Run before every test case"""
        self.user_attr = {
            "username": "wookie",
            "first_name": "wookie",
            "last_name": "ewok",
            "author_pseudonym": "ewookie",
            "password": "wookie1234",
        }
        self.book_attr = {
            "title": faker.sentence(),
            "description": faker.sentence(),
            "cover_image": faker.url(),
            "price": Money(1234, "USD"),
        }

        self.book_with_image_attr = {
            "title": faker.sentence(),
            "description": faker.sentence(),
            "price": Money(1234, "USD"),
        }
        self.author_name_attr = {"author_name": "Wookie Ewok"}

        self.login_attr = {"username": "wookie", "password": "wookie1234"}

    def tearDown(self):
        """Run after every test case"""

        Book.objects.all().delete()
        self.user.objects.all().delete()
