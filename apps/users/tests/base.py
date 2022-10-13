from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient


class BaseTest(TestCase):
    """Base class for tests"""

    user = get_user_model()
    client = APIClient()
    user_attr = user_attr = {
        "username": "wookie",
        "first_name": "wookie",
        "last_name": "ewok",
        "author_pseudonym": "ewookie",
        "password": "wookie",
    }

    def setUp(self):
        """Run before every test case"""

        self.user_attr = {
            "username": "wookie",
            "first_name": "wookie",
            "last_name": "ewok",
            "author_pseudonym": "ewookie",
            "password": "wookie",
        }

    def tearDown(self):
        """Run after every test case"""

        self.user.objects.all().delete()
