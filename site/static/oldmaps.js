window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")

  // Add the event listener to the radio buttons to update the counter and Rewards column
  Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const treasureId = radio.name.replace('found_oldmap_treasure_', ''); // Extract oldmap ID;
      console.log("treasureId ->", treasureId)
      updateoldmap(radio, treasureId)
      // itemToggle(radio);
    });
    // itemToggle(radio);
  });
});

// Add a listener for the form submission

function updateoldmap(radio, treasureId) {
  console.log("--------UPDATE oldmap ---------")
  const treasureFound = radio.value;

  const data = {
    treasure_id: parseInt(treasureId),
    treasure_done: parseInt(treasureFound),
  };
  console.log("DATA ->", data)
  
  if (treasureFound == 2) {
    fetch('/oldmap_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        treasure_id: treasureId  // Pass the variable to the server
      })
    })
  }
  
  fetch('/update_oldmaps', {
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

// function infoToggle(radio) {
//   var treasureId = radio.id.replace('done_', ''); // Extract point ID
//   console.log("Root ID ->", treasureId)
//   var treasureIdElements = document.querySelectorAll(".root_" + treasureId);
//   console.log("Root Elements ->", treasureIdElements)

//   treasureIdElements.forEach(function (element) {
//     if (radio.checked) {
//       element.classList.remove("hidden_display"); // Show info
//     } else {
//       element.classList.add("hidden_display"); // Hide info
//     }
//   });
// }