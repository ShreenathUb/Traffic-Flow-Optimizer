# app/routes.py
from flask import Blueprint, render_template, request, jsonify, current_app
from flask_uploads import UploadSet, IMAGES
import os
from app.vehicle_detection import detect_vehicles
from app.signal_controller import calculate_green_signal_time

main_bp = Blueprint('main', __name__, template_folder='../templates',
                static_folder='../static')
photos = UploadSet('photos', IMAGES)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/process_images', methods=['POST'])
def process_images():
    try:
        # Parse input parameters
        vehicle_density = float(request.form.get('vehicleDensity', 1.0))
        avg_pass_time = int(request.form.get('avgPassTime', 2))
        
        # Initialize results for each road
        roads = ['A', 'B', 'C', 'D']
        road_results = {}
        
        # Process each road's image
        for road in roads:
            image_key = f'road{road}Image'
            if image_key in request.files:
                image_file = request.files[image_key]
                if image_file.filename:
                    # Save the uploaded image
                    filename = photos.save(image_file)
                    image_path = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename)
                    
                    # Detect vehicles in the image
                    vehicle_counts = detect_vehicles(image_path)
                    
                    # Calculate green signal time
                    total_vehicles = sum(vehicle_counts.values())
                    gst = calculate_green_signal_time(total_vehicles, vehicle_density, avg_pass_time)
                    
                    # Store results for this road
                    road_results[road] = {
                        'vehicle_counts': vehicle_counts,
                        'total_vehicles': total_vehicles,
                        'gst': gst
                    }
            else:
                # If no image provided, use default values
                road_results[road] = {
                    'vehicle_counts': {'cars': 0, 'buses': 0, 'bikes': 0, 'trucks': 0, 'motorcycles': 0},
                    'total_vehicles': 0,
                    'gst': 5  # Default minimum GST
                }
        
        return jsonify(road_results)
        
    except Exception as e:
        current_app.logger.error(f"Error processing images: {str(e)}")
        return jsonify({'error': str(e)}), 500