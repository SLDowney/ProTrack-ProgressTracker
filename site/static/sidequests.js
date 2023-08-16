window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")

  // Add the event listener to the radio buttons to update the counter and Rewards column
  Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const sideId = radio.name.replace('done_', ''); // Extract side ID;
      console.log("sideID ->", sideId)
      updateside(radio, sideId)
      // itemToggle(radio);
    });
    // itemToggle(radio);
  });
});


// Function to handle form submission and filtering by region
function filterByRegion() {
  var selectedRegion = document.getElementById('regionFilter').value;
  var sideForm = document.getElementById('sideform');
  sideForm.action = "/sidequests"; // Use the relative URL
  if (selectedRegion) {
      sideForm.action += "?region=" + encodeURIComponent(selectedRegion); // Include the region query parameter
  }
  sideForm.submit();
  return false;
}

// Add a listener for the form submission
document.getElementById('regionFilterForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the default form submission behavior
  filterByRegion(); // Call the filterByRegion() function to handle the form submission
});

function updateside(radio, sideId) {
  console.log("--------UPDATE side ---------")
  const sideFound = radio.value;

  const data = {
    side_id: parseInt(sideId),
    side_done: parseInt(sideFound),
  };
  console.log("DATA ->", data)
  
  fetch('/side_update', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      side_id: sideId,  // Pass the variable to the server
      side_done: parseInt(sideFound)

    })
  })
  
  fetch('/update_sidequests', {
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

// function itemToggle(radio) {
//   var compId = radio.id.replace('done_', ''); // Extract comp ID
//   var compItemElement = document.getElementById("comp_item_" + compId);
//   var items = compItemElement.nextElementSibling.textContent; // Get rewards value using getAttribute

//   if (radio.checked) {
//     compItemElement.textContent = items; // Show rewards value
//   } else {
//     compItemElement.textContent = "???"; // Show "???" when unchecked
//   }
// }