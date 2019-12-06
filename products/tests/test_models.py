from django.test import TestCase
from products import models


class ProductModelTest(TestCase):
    """
    Tests related to the products app models.

    - Check that the data is created in the db.
    """

    def test_create_category(self):
        name = "Motherboards"
        models.Category.objects.create(name=name)
