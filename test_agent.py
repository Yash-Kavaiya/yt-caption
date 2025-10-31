"""
Simple test script for the YouTube Transcript Agent
Tests basic functionality without requiring actual API calls
"""
import unittest
from main import app


class TestYouTubeTranscriptAgent(unittest.TestCase):
    """Test cases for the YouTube Transcript Agent Flask app"""

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_homepage_loads(self):
        """Test that the homepage loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'YouTube Transcript Fetcher', response.data)
        self.assertIn(b'Bootstrap', response.data)

    def test_homepage_contains_instructions(self):
        """Test that the homepage contains usage instructions"""
        response = self.client.get('/')
        self.assertIn(b'append the YouTube video ID to the URL', response.data)
        self.assertIn(b'http://127.0.0.1:5000/abcd1234', response.data)

    def test_video_id_route_exists(self):
        """Test that the video ID route is accessible (will fail without internet)"""
        # This will fail with connection error since we can't access YouTube
        # but it verifies the route exists and handles errors properly
        response = self.client.get('/test_video_id')
        # Should return 200 even on error (renders error template)
        self.assertEqual(response.status_code, 200)
        # Should contain error message
        self.assertIn(b'Error', response.data)

    def test_flask_app_config(self):
        """Test Flask app configuration"""
        self.assertTrue(self.app.config['TESTING'])
        self.assertIsNotNone(self.app)


if __name__ == '__main__':
    print("Running YouTube Transcript Agent Tests")
    print("=" * 50)
    unittest.main(verbosity=2)
