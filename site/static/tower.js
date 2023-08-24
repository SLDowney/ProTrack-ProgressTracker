window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var towerTable = document.getElementById('tower-table');
  var checkboxes = document.querySelectorAll('.tower_checkbox');

  checkboxes.forEach(function (checkbox) {
    // Check the initial state of the checkbox and apply the class accordingly
    var towerId = checkbox.id.replace('done_', ''); // Extract point ID
    var towerIDElements = document.querySelectorAll(".tower_" + towerId);

    towerIDElements.forEach(function (element) {
      if (checkbox.checked) {
        element.classList.remove("hidden_display"); // Show info
      } 
    });
  });

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(towerTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when checkbox is clicked
        const towerId = checkbox.id.replace('done_', ''); // Extract tower ID
      
        updatetower(checkbox, towerId); // Pass towerReward to updatetower function
        infoToggle(checkbox)
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

  fetch('/update_tower', {
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

function infoToggle(checkbox) {
  var towerId = checkbox.id.replace('done_', ''); // Extract point ID
  console.log("tower ID ->", towerId)
  var towerIDElements = document.querySelectorAll(".tower_" + towerId);
  console.log("tower Elements ->", towerIDElements)

  towerIDElements.forEach(function (element) {
    if (checkbox.checked) {
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
  });
}