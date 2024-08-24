import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b"Welcome to the Flask Web Application!")

    def test_add(self):
        result = self.app.get('/add?a=10&b=5')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json['result'], 15)

    def test_subtract(self):
        result = self.app.get('/subtract?a=10&b=5')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json['result'], 5)

if __name__ == "__main__":
    unittest.main()