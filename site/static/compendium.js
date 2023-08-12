window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(document.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {
        
      // Update Rewards cell when checkbox is clicked
        const compId = checkbox.id.replace('done_', ''); // Extract comp ID
        console.log("compID ->", compId)
      
        updatecomp(checkbox, compId)
        itemToggle(checkbox)
      });
      itemToggle(checkbox)
  });
});

var compendiumTable = document.getElementsByClassName('location_table');

function updatecomp(checkbox, compId) {
    console.log("--------UPDATE comp ---------")
  const compFound = checkbox.checked ? 1 : 0;

  const data = {
    comp_id: parseInt(compId),
    comp_done: compFound,
  };
  console.log("DATA ->", data)

  fetch('/update-comp', {
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

function itemToggle(checkbox) {
  var compId = checkbox.id.replace('done_', ''); // Extract comp ID
  var compItemElement = document.getElementById("comp_item_" + compId);
  var items = compItemElement.nextElementSibling.textContent; // Get rewards value using getAttribute

  if (checkbox.checked) {
    compItemElement.textContent = items; // Show rewards value
  } else {
    compItemElement.textContent = "???"; // Show "???" when unchecked
  }
}