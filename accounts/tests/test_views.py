from django.test import TestCase


class AccountsPageTest(TestCase):
    """
    Tests related to the accounts app views.

    - Check that the HTTP status code is 200
    - Check the correct template hase been used
    - Check the response for a page name
    """

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
