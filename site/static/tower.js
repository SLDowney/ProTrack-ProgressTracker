window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var towerTable = document.getElementById('tower-table');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(towerTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when checkbox is clicked
        const towerId = checkbox.id.replace('tower_done_', ''); // Extract tower ID
      
        updatetower(checkbox, towerId); // Pass towerReward to updatetower function
    });
});
 
  });

var towerTable = document.getElementById('tower-table');

function updatetower(checkbox, towerId) {
    console.log("--------UPDATE tower ---------")
  const towerFound = checkbox.checked ? 1 : 0;

  const data = {
    tower_id: parseInt(towerId),
    tower_done: towerFound,
  };
  console.log("DATA ->", data)

  fetch('/update-tower', {
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