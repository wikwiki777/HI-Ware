from django.test import TestCase


# Create your tests here.
class PageTest(TestCase):

    def test_index_page_works(self):
        """Test index page is loaded."""
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)

    def test_products_page_works(self):
        """Test index page is loaded."""
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)
