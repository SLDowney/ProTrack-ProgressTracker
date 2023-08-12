window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")

  // Add the event listener to the radio buttons to update the counter and Rewards column
  Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const caveId = radio.id.replace('done_', ''); // Extract cave ID
      console.log("caveID ->", caveId)
      console.log("radio.value:", radio.value)

      // itemToggle(radio);
    });
    // itemToggle(radio);
  });
});


// Function to handle form submission and filtering by region
function filterByRegion() {
  var selectedRegion = document.getElementById('regionFilter').value;
  var caveForm = document.getElementById('caveform');
  caveForm.action = "/caves"; // Use the relative URL
  if (selectedRegion) {
      caveForm.action += "?region=" + encodeURIComponent(selectedRegion); // Include the region query parameter
  }
  caveForm.submit();
  return false;
}

// Add a listener for the form submission
document.getElementById('regionFilterForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the default form submission behavior
  filterByRegion(); // Call the filterByRegion() function to handle the form submission
});

function updatecave(radio, caveId) {
  console.log("--------UPDATE cave ---------")
  const caveFound = radio.value;

  const data = {
    cave_id: parseInt(caveId),
    cave_done: parseInt(caveFound),
  };
  console.log("DATA ->", data)

  fetch('/update-cave', {
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