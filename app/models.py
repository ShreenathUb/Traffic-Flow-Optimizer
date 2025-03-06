from datetime import datetime

class TrafficData:
    """
    Class to represent traffic data and analytics
    """
    def __init__(self, road_id, image_path=None):
        self.road_id = road_id
        self.image_path = image_path
        self.timestamp = datetime.now()
        self.vehicle_counts = {
            'cars': 0,
            'buses': 0,
            'bikes': 0,
            'trucks': 0,
            'motorcycles': 0
        }
        self.total_vehicles = 0
        self.green_signal_time = 0
        self.density_factor = 1.0
        
    def calculate_total(self):
        """Calculate total vehicle count from individual counts"""
        self.total_vehicles = sum(self.vehicle_counts.values())
        return self.total_vehicles
    
    def to_dict(self):
        """Convert object to dictionary for JSON serialization"""
        return {
            'road_id': self.road_id,
            'timestamp': self.timestamp.isoformat(),
            'vehicle_counts': self.vehicle_counts,
            'total_vehicles': self.total_vehicles,
            'green_signal_time': self.green_signal_time,
            'density_factor': self.density_factor
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create object from dictionary"""
        traffic_data = cls(data['road_id'])
        traffic_data.vehicle_counts = data['vehicle_counts']
        traffic_data.total_vehicles = data['total_vehicles']
        traffic_data.green_signal_time = data['green_signal_time']
        traffic_data.density_factor = data.get('density_factor', 1.0)
        return traffic_data