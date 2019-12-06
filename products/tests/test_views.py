from django.test import TestCase


# Create your tests here.
class IndexPageTest(TestCase):

    def test_index_page_works(self):
        """Test index page is loaded."""
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertIn(
            b"<title>HI-Ware: High-End PC Hardware</title>", response.content)
