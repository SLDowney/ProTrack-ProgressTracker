function infoToggle(radio) {
  const shrineId = radio.name.replace('done_', ''); // Extract shrine ID;
  console.log("shrine ID ->", shrineId)
  var shrineIDElements = document.querySelectorAll(".shrine_" + shrineId);
  console.log("shrine Elements ->", shrineIDElements)

  shrineIDElements.forEach(function (element) {
    if (radio.value == "2") {
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
    if (radio.value == "1") {
      console.log("ELEMENT ->", element)

      if (element.id == "shrine_location" || element.id == "shrine_coord" || element.id == "shrine_region") {
        element.classList.remove("hidden_display");
      } else {
          element.classList.add("hidden_display"); // Hide info
      }

    }
  });
}

window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")

  Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const shrineId = radio.name.replace('done_', ''); // Extract shrine ID;
      console.log("shrineID ->", shrineId)
      updateshrine(radio, shrineId)
      infoToggle(radio);
    });
    if (radio.checked) {
      infoToggle(radio);
    }
    //infoToggle(radio);
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

