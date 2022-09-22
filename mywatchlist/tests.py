from django.test import SimpleTestCase

# Create your tests here.
class unitTest(SimpleTestCase):
    def test_url_exist(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
