window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var wellTable = document.getElementById('well-table');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(wellTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when checkbox is clicked
        const wellId = checkbox.id.replace('well_done_', ''); // Extract well ID
      
        updatewell(checkbox, wellId); // Pass wellReward to updatewell function
    });
});
 
  });

var wellTable = document.getElementById('well-table');

function updatewell(checkbox, wellId) {
    console.log("--------UPDATE well ---------")
  const wellFound = checkbox.checked ? 1 : 0;

  const data = {
    well_id: parseInt(wellId),
    well_done: wellFound,
  };
  console.log("DATA ->", data)

  fetch('/update-well', {
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