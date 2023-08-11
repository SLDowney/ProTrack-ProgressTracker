window.addEventListener('DOMContentLoaded', function() {
  
  var device_dispensersTable = document.getElementById('device_dispensers-table');
  
  // Add the event listener to the checkboxes to update the counter when checkboxes are clicked
  Array.from(device_dispensersTable.querySelectorAll('input[type="checkbox"]')).forEach(function(checkbox) {
    checkbox.addEventListener('click', function() {
    });
  });
  
});
var device_dispensersTable = document.getElementById('device_dispensers-table');

function updatedevice_dispenser(checkbox, device_dispenserId) {
  const device_dispenserFound = checkbox.checked ? 1 : 0;

  const data = {
      dis_id: device_dispenserId,
      dis_done: device_dispenserFound,
  };

  console.log('Data sent to server:', data); // Add this line for debugging

  fetch('/update-device_dispenser', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
      // Handle the response if needed
      console.log('Response from server:', data); // Add this line for debugging
  })
  .catch(error => {
      console.error('Error:', error);
  });
  
};
