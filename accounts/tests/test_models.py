from django.test import TestCase
from accounts import models


class CustomerModelTest(TestCase):
    """
    Tests related to the accounts app models.

    - Check that the data is created in the db.
    """

    def test_create_customer_account(self):
        username = "TestCustomer"
        email = "testcustomer@email.com"
        password = "testpassword1"
        models.User.objects.create_user(username,
                                        email,
                                        password)
