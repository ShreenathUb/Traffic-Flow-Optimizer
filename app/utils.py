import os
import json
from datetime import datetime
import logging

def setup_logging(app):
    """Configure application logging"""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    log_file = os.path.join('logs', f'app_{datetime.now().strftime("%Y%m%d")}.log')
    
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    ))
    
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

def save_traffic_data(data, filename="traffic_data.json"):
    """Save traffic data to JSON file"""
    try:
        # Convert datetime objects to strings
        serializable_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                serializable_data[key] = value.copy()
                if 'timestamp' in serializable_data[key]:
                    if isinstance(serializable_data[key]['timestamp'], datetime):
                        serializable_data[key]['timestamp'] = serializable_data[key]['timestamp'].isoformat()
            else:
                serializable_data[key] = value
                
        with open(filename, 'w') as f:
            json.dump(serializable_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving traffic data: {str(e)}")
        return False

def load_traffic_data(filename="traffic_data.json"):
    """Load traffic data from JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return {}
    except Exception as e:
        print(f"Error loading traffic data: {str(e)}")
        return {}

def generate_report(data, output_file="traffic_report.txt"):
    """Generate a text report from traffic data"""
    with open(output_file, 'w') as f:
        f.write("TRAFFIC FLOW OPTIMIZER - ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for road_id, road_data in data.items():
            f.write(f"Road {road_id} Analysis:\n")
            f.write("-" * 20 + "\n")
            
            counts = road_data.get('vehicle_counts', {})
            f.write(f"Cars: {counts.get('cars', 0)}\n")
            f.write(f"Buses: {counts.get('buses', 0)}\n")
            f.write(f"Bikes: {counts.get('bikes', 0)}\n")
            f.write(f"Trucks: {counts.get('trucks', 0)}\n")
            f.write(f"Motorcycles: {counts.get('motorcycles', 0)}\n")
            
            f.write(f"Total vehicles: {road_data.get('total_vehicles', 0)}\n")
            f.write(f"Green signal time: {road_data.get('gst', 0)} seconds\n\n")
        
        f.write("Summary:\n")
        f.write("-" * 20 + "\n")
        
        total_vehicles = sum(rd.get('total_vehicles', 0) for rd in data.values())
        f.write(f"Total vehicles across all roads: {total_vehicles}\n")
        
        if data:
            avg_gst = sum(rd.get('gst', 0) for rd in data.values()) / len(data)
            f.write(f"Average green signal time: {avg_gst:.2f} seconds\n")
            
    return output_file