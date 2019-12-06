from django.test import TestCase
from products import models


class ProductModelTest(TestCase):
    """
    Tests related to the products app models.

    - Check that the data is created in the db.
    """

    def test_create_category(self):
        """Test category can be created"""
        name = "Motherboards"
        models.Category.objects.create(name=name)
        get_data = models.Category.objects.get(name=name)
        self.assertEqual(name, get_data.name)

    def test_create_base_product(self):
        """Test base product can created"""
        description = "Motherboards or mainboards"
        name = "Motherboards"
        models.Category.objects.create(name=name)
        category = models.Category.objects.get(name=name)
        models.BaseProduct.objects.create(
            category=category, description=description)
        get_data = models.BaseProduct.objects.get(category=category.id)
        self.assertEqual(description, get_data.description)
