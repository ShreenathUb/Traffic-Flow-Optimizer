import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.signal_controller import calculate_green_signal_time

class TestSignalController(unittest.TestCase):
    
    def test_zero_vehicles(self):
        """Test GST calculation with zero vehicles"""
        gst = calculate_green_signal_time(0)
        self.assertEqual(gst, 5)  # Should return minimum GST
    
    def test_minimum_bound(self):
        """Test GST doesn't go below minimum"""
        gst = calculate_green_signal_time(1, 0.1, 1)  # Low values
        self.assertEqual(gst, 5)  # Should return minimum GST
    
    def test_maximum_bound(self):
        """Test GST doesn't exceed maximum"""
        gst = calculate_green_signal_time(1000, 2.0, 5)  # Very high values
        self.assertEqual(gst, 60)  # Should return maximum GST
    
    def test_standard_calculation(self):
        """Test standard GST calculation"""
        # 20 vehicles, density 1.0, avg_pass_time 2
        # Formula: ((20+5)/5) * 1.0 * 2 = 10
        gst = calculate_green_signal_time(20, 1.0, 2)
        self.assertEqual(gst, 10)
    
    def test_density_effect(self):
        """Test effect of vehicle density on GST"""
        # Same vehicles, different density
        base_gst = calculate_green_signal_time(20, 1.0, 2)
        higher_density_gst = calculate_green_signal_time(20, 1.5, 2)
        
        self.assertGreater(higher_density_gst, base_gst)
        self.assertEqual(higher_density_gst, base_gst * 1.5)
    
    def test_pass_time_effect(self):
        """Test effect of average pass time on GST"""
        # Same vehicles, different pass time
        base_gst = calculate_green_signal_time(20, 1.0, 2)
        slower_pass_gst = calculate_green_signal_time(20, 1.0, 3)
        
        self.assertGreater(slower_pass_gst, base_gst)
        self.assertEqual(slower_pass_gst, base_gst * 1.5)  # 3/2 = 1.5

if __name__ == '__main__':
    unittest.main()