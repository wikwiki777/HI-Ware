from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
from django.template.loader import get_template
from django.contrib.auth.tokens import (PasswordResetTokenGenerator,
                                        int_to_base36)


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
                                 last_name="Doe")

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

    def test_user_logout_works(self):
        """Test user is logged out and redirected."""
        self.client.login(username="TestUser", password="testPassword1")
        response = self.client.get("/accounts/logout", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
        self.assertIn(b"You have successfully been logged out!",
                      response.content)

    def test_user_password_reset_page_works(self):
        """Test password reset page is loaded."""
        response = self.client.get("/accounts/password-reset/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "password_reset_form.html")
        self.assertIn(b"<title>HI-Ware: Password Reset</title>",
                      response.content)

    def test_user_password_reset_sent_succesfull(self):
        """Test password reset sent page is loaded."""
        response = self.client.post("/accounts/password-reset/",
                                    {"email": "TestUser@testemail.com"},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "password_reset_done.html")
        self.assertIn(b"<title>HI-Ware: Password Reset Sent</title>",
                      response.content)

    def test_reset_password_email_is_sent(self):
        "Test the email with the link to reset the password is sent."
        user = User.objects.get(email="TestUser@testemail.com")
        uid = int_to_base36(user.id)
        token = PasswordResetTokenGenerator()
        protocol = "http"
        domain = "127.0.0.1:8000"
        email_template = get_template("password_reset_email.html")
        context = {"protocol": protocol,
                   "domain": domain,
                   "uid": uid,
                   "token": token.make_token(user)}
        mail.send_mail(
            "Password Reset",
            email_template.render(context),
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Password Reset", str(mail.outbox[0].subject))
        self.assertIn("{0}://{1}/accounts/password-reset/{2}-{3}".
                      format(protocol, domain, uid, token.make_token(user)),
                      mail.outbox[0].body)

    def test_user_password_reset_page_link(self):
        """Test password reset link opens page."""
        user = User.objects.get(email="TestUser@testemail.com")
        uid = int_to_base36(user.id)
        token = PasswordResetTokenGenerator()
        response = self.client.get("/accounts/password-reset/{0}-{1}".
                                   format(uid, token.make_token(user)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "password_reset_confirm.html")
        self.assertIn(b"<title>HI-Ware: Enter New Password</title>",
                      response.content)

    def test_user_password_reset_is_successfull(self):
        """Test user sees page that password reset was completed."""
        response = self.client.get("/accounts/password-reset/complete")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "password_reset_complete.html")
        self.assertIn(b"<title>HI-Ware: Successfully Reset Password!</title>",
                      response.content)
