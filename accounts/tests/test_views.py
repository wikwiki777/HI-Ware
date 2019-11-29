from django.test import TestCase
from django.contrib.auth.models import User


class AccountsPageTest(TestCase):
    """
    Tests related to the accounts app views.

    - Check that the HTTP status code is 200
    - Check the correct template hase been used
    - Check the response for a page name
    """

    def setUp(self):
        """Set a test user to be used in the tests."""
        User.objects.create_user("TestUser",
                                 "TestUser@testemail.com",
                                 "testPassword1",
                                 first_name="John",
                                 last_name="Doe",
                                 pk=7)

    def test_login_page_works(self):
        """Test login page is loaded."""
        response = self.client.get("/accounts/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
        self.assertIn(b"<title>HI-Ware: Login</title>", response.content)

    def test_registration_page_works(self):
        """Test login page is loaded."""
        response = self.client.get("/accounts/register")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration.html")
        self.assertIn(b"<title>HI-Ware: Register</title>", response.content)

    def test_profile_page_works(self):
        """Test profile page is loaded."""
        self.client.login(username="TestUser", password="testPassword1")
        response = self.client.get("/accounts/profile")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile.html")
        self.assertIn(b"<title>HI-Ware: Profile</title>", response.content)
        self.assertIn(b"TestUser@testemail.com", response.content)
