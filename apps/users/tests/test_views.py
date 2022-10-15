from django.urls import reverse

from rest_framework import status

from apps.users.tests.base import BaseTest


class TestRegisterUserAPIView(BaseTest):
    """Test RegisterUserAPIView"""

    def test_register_user_with_valid_data(self):
        """Test registering user with valid data"""

        extra_data = {"password2": "wookie1234"}
        self.user_attr.update(extra_data)
        response = self.client.post(reverse("register"), self.user_attr)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["username"], self.user_attr["username"])
        self.assertEqual(
            response.data["author_pseudonym"],
            self.user_attr["author_pseudonym"],
        )
        self.assertEqual(response.data["first_name"], self.user_attr["first_name"])
        self.assertEqual(response.data["last_name"], self.user_attr["last_name"])
        self.assertIsNone(response.data.get("password"), None)
        self.assertIsNone(response.data.get("password2"), None)

    def test_register_user_with_passwords_that_do_not_match(self):
        """Test registering users with passwords that do not match"""

        extra_data = {"password2": "12w2qz2`123x@Aw2:"}
        self.user_attr.update(extra_data)
        response = self.client.post(reverse("register"), self.user_attr)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_with_invalid_password(self):
        """Test registering users with invalid password"""

        extra_data = {"password2": "1ez21233"}
        self.user_attr["password"] = "1ez21232"
        self.user_attr.update(extra_data)
        response = self.client.post(reverse("register"), self.user_attr)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestLoginAPIView(BaseTest):
    """Test  LoginAPIView"""

    def test_login_with_correct_credentials(self):
        """Test login with correct credentials"""

        self.user.objects.create_user(**self.user_attr)

        response = self.client.post(
            reverse("login"),
            {
                "username": self.user_attr["username"],
                "password": self.user_attr["password"],
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data["access"])
        self.assertIsNotNone(response.data["refresh"])

    def test_login_with_incorrect_credentials(self):
        """Test login with incorrect credentials"""

        self.user.objects.create_user(**self.user_attr)

        response = self.client.post(
            reverse("login"),
            {"username": "wookieq", "password": self.user_attr["password"]},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_disabled_account(self):
        """Test login with with disabled account credentials"""

        user = self.user.objects.create_user(**self.user_attr)
        user.is_active = False
        user.save()

        response = self.client.post(
            reverse("login"),
            {
                "username": self.user_attr["username"],
                "password": self.user_attr["password"],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data["detail"],
            "No active account found with the given credentials",
        )
