function compFind() {
  let textbox = document.getElementById("find_comp");
  let text = textbox.value.toLowerCase();
  console.log("Text ->", text)
  Array.from(document.getElementsByClassName("comp_all")).forEach(function (element) {
    console.log("Element ->", element)
    let compName = element.getAttribute('name').toLowerCase();
    
    if (compName && typeof compName === 'string') {
        compName = compName.replace('comp_name_', '');
        console.log("comp Name ->", compName);
    } else {
        console.log("Element does not have a valid 'name' attribute.");
    }
    console.log("comp Name ->", compName)    
    if (compName.includes(text)) {
      element.classList.remove("hidden_display");
    }
    else {
      element.classList.add("hidden_display");
    }
    console.log("comp compName ->", compName)
})
}

function compShow() {
  location.reload();
}

window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  const findCompInput = document.getElementById("find_comp");
  const searchButton = document.getElementById("searchButton");

  findCompInput.focus(); // Set focus on the input field

  // Add an event listener to detect "Enter" key press
  findCompInput.addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
          // Activate the search button when Enter is pressed
          searchButton.click();
      }
  });
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