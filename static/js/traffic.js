// static/js/traffic.js
document.addEventListener('DOMContentLoaded', function() {
    // Image form submission
    const imageForm = document.getElementById('imageForm');
    const startButton = document.getElementById('startButton');
    let simulationRunning = false;
    let simulationInterval;
    let currentActiveSignal = null;
    let timers = {};
    
    // Function to show image previews
    function setupImagePreviews() {
        const roads = ['A', 'B', 'C', 'D'];
        
        roads.forEach(road => {
            const input = document.getElementById(`road${road}Image`);
            const preview = document.getElementById(`preview${road}`);
            
            input.addEventListener('change', function() {
                if (this.files && this.files[0]) {
                    const reader = new FileReader();
                    
                    reader.onload = function(e) {
                        preview.innerHTML = '';
                        const img = document.createElement('img');
                        img.src = e.target.result;
                        preview.appendChild(img);
                    };
                    
                    reader.readAsDataURL(this.files[0]);
                }
            });
        });
    }
    
    // Function to update UI with vehicle counts and GST
    function updateResults(data) {
        const roads = ['A', 'B', 'C', 'D'];
        
        roads.forEach(road => {
            if (data[road]) {
                const roadData = data[road];
                const counts = roadData.vehicle_counts;
                
                // Update individual vehicle counts
                document.getElementById(`cars${road}`).textContent = counts.cars || 0;
                document.getElementById(`buses${road}`).textContent = counts.buses || 0;
                document.getElementById(`bikes${road}`).textContent = counts.bikes || 0;
                document.getElementById(`trucks${road}`).textContent = counts.trucks || 0;
                
                // Update total and GST
                document.getElementById(`total${road}`).textContent = roadData.total_vehicles || 0;
                document.getElementById(`gst${road}`).textContent = Math.round(roadData.gst || 0);
                
                // Store GST value for traffic light control
                timers[road] = Math.round(roadData.gst || 5);
            }
        });
    }
    
    // Function to run traffic light sequence
    function runTrafficLightSequence() {
        if (simulationRunning) {
            stopSimulation();
        }
        
        simulationRunning = true;
        const roads = ['A', 'B', 'C', 'D'];
        let currentIndex = 0;
        
        // Reset all signals to red
        roads.forEach(road => {
            setSignalState(road, 'red');
        });
        
        // Start the sequence
        simulationInterval = setInterval(() => {
            const currentRoad = roads[currentIndex];
            const nextIndex = (currentIndex + 1) % roads.length;
            const nextRoad = roads[nextIndex];
            
            // Get GST for current road
            const gst = timers[currentRoad] || 5;
            
            // Set current road to green
            setSignalState(currentRoad, 'green');
            currentActiveSignal = currentRoad;
            
            // Start countdown for green light
            startCountdown(currentRoad, gst, () => {
                // Change to yellow for 3 seconds
                setSignalState(currentRoad, 'yellow');
                
                startCountdown(currentRoad, 3, () => {
                    // Change to red
                    setSignalState(currentRoad, 'red');
                    currentIndex = nextIndex;
                });
            });
        }, (timers[currentActiveSignal] || 5) * 1000 + 3000); // GST + yellow time
    }
    
    // Function to set signal state (red, yellow, green)
    function setSignalState(road, state) {
        const signal = document.getElementById(`signal${road}`);
        const lights = signal.querySelectorAll('.light');
        
        // Reset all lights
        lights.forEach(light => {
            light.classList.remove('active');
        });
        
        // Activate specified light
        if (state === 'red') {
            signal.querySelector('.light.red').classList.add('active');
        } else if (state === 'yellow') {
            signal.querySelector('.light.yellow').classList.add('active');
        } else if (state === 'green') {
            signal.querySelector('.light.green').classList.add('active');
        }
    }
    
    // Function to start countdown timer
    function startCountdown(road, seconds, callback) {
        const timerElement = document.getElementById(`timer${road}`);
        let timeLeft = seconds;
        
        timerElement.textContent = timeLeft;
        
        const countdown = setInterval(() => {
            timeLeft--;
            timerElement.textContent = timeLeft;
            
            if (timeLeft <= 0) {
                clearInterval(countdown);
                timerElement.textContent = '';
                if (callback) callback();
            }
        }, 1000);
    }
    
    // Function to stop simulation
    function stopSimulation() {
        clearInterval(simulationInterval);
        simulationRunning = false;
        
        const roads = ['A', 'B', 'C', 'D'];
        roads.forEach(road => {
            const timerElement = document.getElementById(`timer${road}`);
            timerElement.textContent = '';
            setSignalState(road, 'red');
        });
    }
    
    // Handle form submission
    imageForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        startButton.disabled = true;
        
        // Create FormData object
        const formData = new FormData(imageForm);
        
        try {
            const response = await fetch('/process_images', {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                const data = await response.json();
                updateResults(data);
                runTrafficLightSequence();
            } else {
                const error = await response.json();
                alert('Error: ' + (error.error || 'Unknown error'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while processing the images.');
        } finally {
            startButton.disabled = false;
        }
    });
    
    // Initialize image previews
    setupImagePreviews();
    
    // Handle page unload
    window.addEventListener('beforeunload', function() {
        if (simulationRunning) {
            stopSimulation();
        }
    });
});