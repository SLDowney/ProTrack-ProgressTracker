window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var chasmTable = document.getElementsByClassName('location_table');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(chasmTable).forEach(function(table) {
    // Find checkboxes within the current table
    var checkboxes = table.querySelectorAll('input[type="checkbox"]');
    
    // Add an event listener to each checkbox in the current table
    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('click', function() {


        // Update Rewards cell when checkbox is clicked
        const chasmId = checkbox.id.replace('done_', ''); // Extract chasm ID
      
        updatechasm(checkbox, chasmId); // Pass chasmReward to updatechasm function
    });
});
});
  });

var chasmTable = document.getElementById('location_table');

function updatechasm(checkbox, chasmId) {
    console.log("--------UPDATE chasm ---------")
  const chasmFound = checkbox.checked ? 1 : 0;

  const data = {
    chasm_id: parseInt(chasmId),
    chasm_done: chasmFound,
  };
  console.log("DATA ->", data)

  fetch('/update_chasm', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response if needed
      console.log('Response from server:', data);

    })
    .catch(error => {
      console.error('Error:', error);
    });
}