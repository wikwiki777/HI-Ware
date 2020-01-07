from django.test import TestCase
from products.models import Category, BaseProduct


# Create your tests here.
class PageTest(TestCase):
    def setUp(self):
        Category.objects.create(name="Motherboards")
        Category.objects.create(name="Processors")
        Category.objects.create(name="Graphics")

        BaseProduct.objects.create(
            description="Motherboard description",
            category=Category.objects.get(name="Motherboards"))
        BaseProduct.objects.create(
            description="Processor description",
            category=Category.objects.get(name="Processors"))
        BaseProduct.objects.create(
            description="Graphics description",
            category=Category.objects.get(name="Graphics"))

    def test_index_page_works(self):
        """Test index page is loaded."""
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)

    def test_products_page_works(self):
        """Test products page is loaded."""
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)

    def test_products_motherboards_page_works(self):
        """Test products/motherboards page is loaded."""
        response = self.client.get("/products/motherboards/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)

    def test_products_processors_page_works(self):
        """Test products/processors page is loaded."""
        response = self.client.get("/products/processors/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)

    def test_products_graphics_page_works(self):
        """Test products/graphics page is loaded."""
        response = self.client.get("/products/graphics/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)
