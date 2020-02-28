from django.test import TestCase
from accounts import forms


class FormTests(TestCase):
    """
    Tests related to the accounts app forms.

    - Check the form input/validation
    """

    def test_user_login_form_validation_for_blank_items(self):
        """Test that empty input is not allowed."""
        form = forms.UserLoginForm(data={"username": "", "password": ""})
        self.assertFalse(form.is_valid())

    def test_user_login_form_validation(self):
        """Test that user input is valid."""
        form = forms.UserLoginForm(data={"username": "TestUser",
                                         "password": "TestPassword"})
        self.assertTrue(form.is_valid())

    def test_user_creation_form_validation(self):
        """Test that user input is valid."""
        form = forms.UserRegistrationForm(data={"first_name": "John",
                                                "last_name": "Doe",
                                                "username": "TestUser",
                                                "email": "TestUser@test.com",
                                                "password1": "TestPassword2",
                                                "password2": "TestPassword2"})
        self.assertTrue(form.is_valid())
