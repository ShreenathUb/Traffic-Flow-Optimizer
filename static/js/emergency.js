document.addEventListener('DOMContentLoaded', function() {
    const emergencyButton = document.getElementById('emergencyButton');
    let emergencyMode = false;
    let emergencyInterval;
    
    // Function to handle emergency mode activation
    function activateEmergencyMode() {
        // Stop any ongoing simulation
        if (window.simulationInterval) {
            clearInterval(window.simulationInterval);
        }
        
        emergencyMode = true;
        emergencyButton.textContent = 'Cancel Emergency';
        emergencyButton.classList.add('active');
        
        // Get all signals
        const roads = ['A', 'B', 'C', 'D'];
        
        // Make all signals flash red
        emergencyInterval = setInterval(() => {
            roads.forEach(road => {
                const signal = document.getElementById(`signal${road}`);
                const redLight = signal.querySelector('.light.red');
                
                redLight.classList.toggle('active');
            });
        }, 500); // Flash every 500ms
        
        // Add emergency class to body for global styling
        document.body.classList.add('emergency-mode');
    }
    
    // Function to deactivate emergency mode
    function deactivateEmergencyMode() {
        emergencyMode = false;
        emergencyButton.textContent = 'Emergency Override';
        emergencyButton.classList.remove('active');
        
        // Stop flashing
        clearInterval(emergencyInterval);
        
        // Reset all signals to red (non-flashing)
        const roads = ['A', 'B', 'C', 'D'];
        roads.forEach(road => {
            const signal = document.getElementById(`signal${road}`);
            const redLight = signal.querySelector('.light.red');
            
            // Ensure red light is on steadily
            redLight.classList.add('active');
            
            // Clear any countdown timers
            const timerElement = document.getElementById(`timer${road}`);
            timerElement.textContent = '';
        });
        
        // Remove emergency class from body
        document.body.classList.remove('emergency-mode');
    }
    
    // Toggle emergency mode when button is clicked
    emergencyButton.addEventListener('click', function() {
        if (emergencyMode) {
            deactivateEmergencyMode();
        } else {
            activateEmergencyMode();
        }
    });
    
    // Handle page unload to clean up
    window.addEventListener('beforeunload', function() {
        if (emergencyMode) {
            clearInterval(emergencyInterval);
        }
    });
});