# app/vehicle_detection.py
import cv2
import cvlib as cv

def detect_vehicles(image_path):
    """
    Detect and count vehicles in an image using OpenCV and cvlib
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        dict: Dictionary containing counts of different vehicle types
    """
    # Initialize counters
    vehicle_counts = {
        'cars': 0,
        'buses': 0,
        'bikes': 0,
        'trucks': 0,
        'motorcycles': 0
    }
    
    try:
        # Read the image
        image = cv2.imread(image_path)
        
        # Detect common objects in the image
        bbox, labels, conf = cv.detect_common_objects(image)
        
        # Count vehicles by type
        for label in labels:
            if label == 'car':
                vehicle_counts['cars'] += 1
            elif label == 'bus':
                vehicle_counts['buses'] += 1
            elif label == 'bicycle':
                vehicle_counts['bikes'] += 1
            elif label == 'truck':
                vehicle_counts['trucks'] += 1
            elif label == 'motorcycle':
                vehicle_counts['motorcycles'] += 1
                
        # Optional: Draw bounding boxes on the image and save for visualization
        # output_img = cv.draw_bbox(image, bbox, labels, conf)
        # cv2.imwrite(image_path.replace('.', '_detected.'), output_img)
        
    except Exception as e:
        print(f"Error in vehicle detection: {str(e)}")
    
    return vehicle_counts