
# app/signal_controller.py
def calculate_green_signal_time(total_vehicles, vehicle_density=1.0, avg_pass_time=2):
    """
    Calculate the Green Signal Time (GST) based on vehicle counts and parameters
    
    Args:
        total_vehicles (int): Total number of vehicles detected
        vehicle_density (float): Vehicle density factor
        avg_pass_time (int): Average time for a vehicle to pass through
        
    Returns:
        float: Calculated Green Signal Time in seconds
    """
    # Base formula: GST = (total_vehicles + 5) / 5
    # Enhanced formula with density and pass time factors
    base_gst = (total_vehicles + 5) / 5
    adjusted_gst = base_gst * vehicle_density * avg_pass_time
    
    # Ensure minimum and maximum bounds
    min_gst = 5  # Minimum 5 seconds
    max_gst = 60  # Maximum 60 seconds
    
    return max(min_gst, min(adjusted_gst, max_gst))

# app/utils.py
import os
from datetime import datetime

def get_timestamp():
    """Return current timestamp in a readable format"""
    return datetime.now().strftime('%Y%m%d_%H%M%S')

def ensure_upload_folder_exists(app):
    """Ensure the uploads folder exists"""
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)