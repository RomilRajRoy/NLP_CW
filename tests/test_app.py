import unittest
from app.main import app

class BasicTests(unittest.TestCase):

    # Set up the test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the home page GET request
    def test_home_page_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"index.html", response.data)

    # Test the home page POST request with valid input
    def test_home_page_post_valid(self):
        response = self.app.post('/', data=dict(text="This is a test input"))
        self.assertEqual(response.status_code, 200)
        # Assuming the response will contain the processed text or some result
        self.assertIn(b"results", response.data)

    # Test the home page POST request with no input
    def test_home_page_post_no_input(self):
        response = self.app.post('/', data=dict(text=None))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"No text provided", response.data)

if __name__ == "__main__":
    unittest.main()
