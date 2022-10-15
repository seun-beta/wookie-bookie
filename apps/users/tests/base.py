from django.contrib.auth import get_user_model
from django.test import TestCase

from faker import Faker
from rest_framework.test import APIClient

faker = Faker()


class BaseTest(TestCase):
    """Base class for tests"""

    user = get_user_model()
    client = APIClient()

    def setUp(self):
        """Run before every test case"""

        self.user_attr = {
            "username": faker.first_name(),
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "author_pseudonym": faker.first_name(),
            "password": "wookie1234",
        }

    def tearDown(self):
        """Run after every test case"""

        self.user.objects.all().delete()
