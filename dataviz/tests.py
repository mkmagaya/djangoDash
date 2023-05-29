from django.test import TestCase

import unittest
from dash.testing.application_runners import import_app

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Import the Dash app
        self.app = import_app("dash_app")

        # Create a test client
        self.client = self.app.test_client()

    def test_homepage_loads_successfully(self):
        # Send a GET request to the homepage
        response = self.client.get("/")

        # Assert that the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

    def test_map_displays_markers(self):
        # Send a GET request to the map page
        response = self.client.get("/map")

        # Assert that the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Assert that the map contains markers
        self.assertIn(b"mapboxgl-marker", response.data)

if __name__ == "__main__":
    unittest.main()

