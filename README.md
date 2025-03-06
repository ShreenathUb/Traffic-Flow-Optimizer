<<<<<<< HEAD
# Traffic-Flow-Optimizer
=======
# Traffic Flow Optimizer

An intelligent traffic management system that uses computer vision to detect vehicles and optimize traffic signal timings.

## Features

- **Real-time Vehicle Detection**: Upload traffic images for each road to detect and count vehicles by type
- **Dynamic Signal Timing**: Automatically calculates optimal green signal times based on traffic density
- **Traffic Simulation**: Visualizes traffic light sequences with countdown timers
- **Emergency Override**: Ability to override normal signal patterns for emergency situations

## Technology Stack

- **Backend**: Python, Flask
- **Computer Vision**: OpenCV, cvlib
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: NumPy, Pandas

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/traffic-flow-optimizer.git
   cd traffic-flow-optimizer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python run.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. Set the Vehicle Density Factor and Average Pass Time parameters
2. Upload traffic images for each road
3. Click "Start Traffic Simulation" to analyze images and begin the signal sequence
4. View vehicle detection results and automatically calculated green signal times
5. Use "Emergency Override" for emergency situations

## Project Structure

```
traffic-flow-optimizer/
├── app/
│   ├── __init__.py          # Flask application initialization
│   ├── config.py            # Configuration settings
│   ├── routes.py            # API endpoints and routes
│   ├── models.py            # Data models
│   ├── vehicle_detection.py # Computer vision algorithms
│   ├── signal_controller.py # Traffic signal timing logic
│   └── utils.py             # Utility functions
├── static/                  # Static assets
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   ├── img/                 # Images
│   └── uploads/             # Uploaded traffic images
├── templates/               # HTML templates
├── tests/                   # Unit and integration tests
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

## Requirements

- Python 3.8+
- Flask
- OpenCV
- cvlib
- NumPy
- Pandas

## License

This project is licensed under the MIT License - see the LICENSE file for details.
>>>>>>> e32ed7a (Initial commit)
