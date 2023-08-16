window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var adventureTable = document.getElementById('adventureform');
  console.log("Adventure Table ->", adventureTable)

  // Add the event listener to the radios to update the counter and Rewards column
  Array.from(adventureTable.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('click', function () {
      console.log("In array")
        // Update Rewards cell when radio is clicked
        const adventureId = radio.name.replace('done_', ''); // Extract adventure ID
        console.log("Adventure ID ->", adventureId)
      
        updateadventure(radio, adventureId); // Pass adventureReward to updateadventure function
    });
});
 
  });

var adventureTable = document.getElementById('adventureform');

function updateadventure(radio, adventureId) {
    console.log("--------UPDATE adventure ---------")
  const adventureFound = radio.value;
  console.log("adventureFound ->", adventureFound)

  const data = {
    adventure_id: parseInt(adventureId),
    adventure_done: parseInt(adventureFound),
  };
  console.log("DATA ->", data)

  if (adventureFound == 2 || adventureFound == 0) {
    console.log("adventures_update YES");
    fetch('/adventures_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        adventure_id: adventureId,  // Pass the variable to the server
        adventure_done: adventureFound
      })
    })
  }

  fetch('/update_adventures', {
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