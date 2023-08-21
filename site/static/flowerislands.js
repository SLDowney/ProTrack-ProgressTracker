window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var flowerislandTables = document.getElementsByClassName('location_table');
  console.log("Flower Islands Table ->", flowerislandTables)

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(flowerislandTables).forEach(function(table) {
    // Find checkboxes within the current table
    var checkboxes = table.querySelectorAll('input[type="checkbox"]');
    
    // Add an event listener to each checkbox in the current table
    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('click', function() {

        // Update Rewards cell when checkbox is clicked
        const flowerislandId = checkbox.id.replace('done_', ''); // Extract flowerisland ID      console.log("Flower Island ID ->", flowerislandId)
        console.log("Flower Island ID ->", flowerislandId)

        updateflowerisland(checkbox, flowerislandId); // Pass flowerislandReward to updateflowerisland function
    });
});
});
  });

var flowerislandTable = document.getElementsByClassName('location_table');

function updateflowerisland(checkbox, flowerislandId) {
    console.log("--------UPDATE flowerisland ---------")
  const flowerislandFound = checkbox.checked ? 1 : 0;

  const data = {
    flowerisland_id: parseInt(flowerislandId),
    flowerisland_done: flowerislandFound,
  };
  console.log("DATA ->", data)

  fetch('/update_flowerisland', {
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