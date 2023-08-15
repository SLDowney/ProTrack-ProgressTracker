window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var mainTable = document.getElementById('mainquform');

  // Add the event listener to the radios to update the counter and Rewards column
  Array.from(mainTable.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('click', function () {

        // Update Rewards cell when radio is clicked
        const mainId = radio.name.replace('done_', ''); // Extract main ID
      
        updatemain(radio, mainId); // Pass mainReward to updatemain function
    });
});
 
  });

var mainTable = document.getElementById('mainquform');

function updatemain(radio, mainId) {
    console.log("--------UPDATE main ---------")
  const mainFound = radio.value;
  console.log("MainFound ->", mainFound)

  const data = {
    main_id: parseInt(mainId),
    main_done: parseInt(mainFound),
  };
  console.log("DATA ->", data)

  if (mainFound == 2) {
    fetch('/main_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        main_id: mainId  // Pass the variable to the server
      })
    })
  }

  fetch('/update-mainquests', {
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