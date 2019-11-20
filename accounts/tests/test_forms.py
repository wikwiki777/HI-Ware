from django.test import TestCase
from accounts import forms


class FormTests(TestCase):
    """
    Tests related to the accounts app forms.

    - Check that the data is created in the db.
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
