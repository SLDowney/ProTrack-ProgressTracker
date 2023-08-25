function infoToggle(radio) {
  const sideId = radio.name.replace('done_', ''); // Extract side ID;
  //console.log("side ID ->", sideId)
  var sideIdElements = document.querySelectorAll(".subquest_" + sideId);
  //console.log("sub Elements ->", sideIdElements)

  sideIdElements.forEach(function (element) {
    if (sideId == 259) {
      if (radio.value == "2") {
        //console.log("ELEMENT 2 ->", element)
        element.classList.remove("hidden_display"); // Show info
      } else {
        element.classList.add("hidden_display"); // Hide info
      }
    }
    else if (radio.value == "1") {
      //console.log("ELEMENT 2 ->", element)
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
  });
}
function secondToggle(radio) {
  const secondId = radio.name.replace('secondary_', ''); // Extract side ID;
  console.log("Second ID ->", secondId)
  console.log("radio value ->", radio.value)
  var secondIdElements = document.querySelectorAll(".tiertwo_" + secondId);
  console.log("Query Selector ->", ".tiertwo_" + secondId)
  console.log("second Elements ->", secondIdElements)

  secondIdElements.forEach(function (element) {
    if (radio.value == "1") {
      console.log("ELEMENT 2 ->", element)
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
  });
}

window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")

  // Add the event listener to the radio buttons to update the counter and Rewards column
  Array.from(document.getElementsByClassName('main_radio')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const sideId = radio.name.replace('done_', ''); // Extract side ID;
      console.log("sideID ->", sideId)
      updateside(radio, sideId)
      infoToggle(radio)
    });
    infoToggle(radio)
    secondToggle(radio);
  });
  Array.from(document.querySelectorAll('.two_radio')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const subId = radio.name.replace('secondary_', ''); // Extract sub ID;
      const sideName = radio.className.replace('quest_', ''); //Extract side ID;
      console.log("subId ->", subId)
      updatesub(radio, subId, sideName)
      secondToggle(radio);
    });
    secondToggle(radio);
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

function updatesub(radio, subId, sideName) {
  console.log("--------UPDATE side ---------")
  const subFound = radio.value;

  const data = {
    sub_id: parseInt(subId),
    sub_done: parseInt(subFound),
    side_name: sideName
  };
  console.log("DATA ->", data)
  
  fetch('/update_subquests', {
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