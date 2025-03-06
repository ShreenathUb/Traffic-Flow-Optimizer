import unittest
import os
import sys
import numpy as np
import cv2

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.vehicle_detection import detect_vehicles

class TestVehicleDetection(unittest.TestCase):
    
    def setUp(self):
        # Create a test directory if it doesn't exist
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test_images')
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        
        # Create a simple test image
        self.test_image_path = os.path.join(self.test_dir, 'test_traffic.jpg')
        test_image = np.ones((300, 400, 3), dtype=np.uint8) * 255  # White image
        cv2.imwrite(self.test_image_path, test_image)
    
    def test_detect_vehicles_empty_image(self):
        """Test vehicle detection on an empty white image"""
        counts = detect_vehicles(self.test_image_path)
        
        # Check if all counts are zero for a plain white image
        self.assertEqual(counts['cars'], 0)
        self.assertEqual(counts['buses'], 0)
        self.assertEqual(counts['bikes'], 0)
        self.assertEqual(counts['trucks'], 0)
        self.assertEqual(counts['motorcycles'], 0)
    
    def test_detect_vehicles_invalid_path(self):
        """Test vehicle detection with invalid image path"""
        invalid_path = os.path.join(self.test_dir, 'nonexistent.jpg')
        counts = detect_vehicles(invalid_path)
        
        # Check if function handles errors gracefully
        self.assertEqual(counts['cars'], 0)
        self.assertEqual(counts['buses'], 0)
        self.assertEqual(counts['bikes'], 0)
        self.assertEqual(counts['trucks'], 0)
        self.assertEqual(counts['motorcycles'], 0)
    
    def test_vehicle_counts_structure(self):
        """Test that the return structure is correct"""
        counts = detect_vehicles(self.test_image_path)
        
        # Check if all expected keys are present
        expected_keys = ['cars', 'buses', 'bikes', 'trucks', 'motorcycles']
        for key in expected_keys:
            self.assertIn(key, counts)
    
    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)
        
        # Remove test directory if empty
        if os.path.exists(self.test_dir) and not os.listdir(self.test_dir):
            os.rmdir(self.test_dir)

if __name__ == '__main__':
    unittest.main()