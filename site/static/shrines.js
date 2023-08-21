window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")

  var radioes = document.querySelectorAll('.shrine_radio');

  radioes.forEach(function (radio) {
    // Check the initial state of the radio and apply the class accordingly
    var shrineId = radio.name.replace('done_', ''); // Extract point ID
    var shrineIDElements = document.querySelectorAll(".shrine_" + shrineId);

    shrineIDElements.forEach(function (element) {
      if (radio.value == "2") {
        console.log("Radio Value ->", radio.value)
        console.log("Element ->", element)
        element.classList.remove("hidden_display"); // Show info
      } 
    });
  });

  // Add the event listener to the radio buttons to update the counter and Rewards column
  Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const shrineId = radio.name.replace('done_', ''); // Extract shrine ID;
      console.log("shrineID ->", shrineId)
      updateshrine(radio, shrineId)
      // itemToggle(radio);
    });
    // itemToggle(radio);
  });
});


// Function to handle form submission and filtering by region
function filterByRegion() {
  var selectedRegion = document.getElementById('regionFilter').value;
  var shrineForm = document.getElementById('shrineform');
  shrineForm.action = "/shrines"; // Use the relative URL
  if (selectedRegion) {
      shrineForm.action += "?region=" + encodeURIComponent(selectedRegion); // Include the region query parameter
  }
  shrineForm.submit();
  return false;
}

// Add a listener for the form submission
document.getElementById('regionFilterForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the default form submission behavior
  filterByRegion(); // Call the filterByRegion() function to handle the form submission
});

function updateshrine(radio, shrineId) {
  console.log("--------UPDATE shrine ---------")
  const shrineFound = radio.value;

  const data = {
    shrine_id: parseInt(shrineId),
    shrine_done: parseInt(shrineFound),
  };
  console.log("DATA ->", data)
  
  if (shrineFound == 2) {
    fetch('/shrine_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        shrine_id: shrineId  // Pass the variable to the server
      })
    })
  }
  
  fetch('/update-shrines', {
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

function infoToggle(radio) {
  var shrineId = radio.name.replace('done_', ''); // Extract point ID
  console.log("shrine ID ->", shrineId)
  var shrineIDElements = document.querySelectorAll(".shrine_" + shrineId);
  console.log("shrine Elements ->", shrineIDElements)

  shrineIDElements.forEach(function (element) {
    if (radio.value == "2") {
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
  });
}