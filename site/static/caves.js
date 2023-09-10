function caveShow() {
  Array.from(document.getElementsByClassName("cave_all")).forEach(function (element) {
    let caveStatus = element.id.replace('caveStatus_', ''); // Extract cave ID;
    console.log("CaveStatus ->", caveStatus)
    console.log("ELEMENT ! ->", element)
    if (caveStatus == 2) {
      console.log("ELEMENT 2 ->", element)
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
    if (caveStatus == 1) {
      console.log("ELEMENT 1 ID ->", element.id)
      // if (element.id == "cave_name" || element.id == "cave_location" || element.id == "cave_coord" || element.id == "cave_region") {
      //   console.log("Element 1 ID ->", element.id)
      //   element.classList.remove("hidden_display");
      // } else {
      //     element.classList.add("hidden_display"); // Hide info
      // }
    }
    if (caveStatus == 0) {
      console.log("ELEMENT 0 ->", element)

      if (element.id == "cave_name") {
        element.classList.remove("hidden_display");
      } else {
          element.classList.add("hidden_display"); // Hide info
      }

    }
})
}

function caveFind() {
  let textbox = document.getElementById("find_cave");
  let text = textbox.value.toLowerCase();
  console.log("Text ->", text)
  Array.from(document.getElementsByClassName("cave_all")).forEach(function (element) {
    console.log("Element ->", element)
    let caveName = element.getAttribute('name').toLowerCase();
    
    if (caveName && typeof caveName === 'string') {
        caveName = caveName.replace('cave_name_', '');
        console.log("cave Name ->", caveName);
    } else {
        console.log("Element does not have a valid 'name' attribute.");
    }
    console.log("cave Name ->", caveName)    
    if (caveName.includes(text)) {
      element.classList.remove("hidden_display");
    }
    else {
      element.classList.add("hidden_display");
    }
    console.log("cave caveName ->", caveName)
})
}

function infoToggle(radio) {
  const caveId = radio.name.replace('done_', ''); // Extract cave ID;
  console.log("cave ID ->", caveId)
  var caveIDElements = document.querySelectorAll(".cave_" + caveId);
  console.log("cave Elements ->", caveIDElements)

  caveIDElements.forEach(function (element) {
    if (radio.value == "2") {
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
    if (radio.value == "1") {
      console.log("ELEMENT ->", element)

      if (element.id == "cave_name" || element.id == "cave_location" || element.id == "cave_coord" || element.id == "cave_region") {
        element.classList.remove("hidden_display");
      } else {
          element.classList.add("hidden_display"); // Hide info
      }
    }
    if (radio.value == "0") {
      console.log("ELEMENT ->", element)

      if (element.id == "cave_name") {
        element.classList.remove("hidden_display");
      } else {
          element.classList.add("hidden_display"); // Hide info
      }

    }
    });
  }


window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  caveShow()
  // Add the event listener to the radio buttons to update the counter and Rewards column
  Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const caveId = radio.name.replace('done_', ''); // Extract cave ID
      console.log("caveID ->", caveId)
      console.log("radio.value:", radio.value)
      //caveShow()
      infoToggle(radio)
    });
  });
});


// Function to handle form submission and filtering by region
// function filterByRegion() {
//   var selectedRegion = document.getElementById('regionFilter').value;
//   var caveForm = document.getElementById('caveform');
//   caveForm.action = "/caves"; // Use the relative URL
//   if (selectedRegion) {
//       caveForm.action += "?region=" + encodeURIComponent(selectedRegion); // Include the region query parameter
//   }
//   caveForm.submit();
//   return false;
// }

// Add a listener for the form submission
// document.getElementById('regionFilterForm').addEventListener('submit', function (event) {
//   event.preventDefault(); // Prevent the default form submission behavior
//   filterByRegion(); // Call the filterByRegion() function to handle the form submission
// });

function updatecave(radio, caveId) {
  console.log("--------UPDATE cave ---------")
  const caveFound = radio.value; 

  const data = {
    cave_id: parseInt(caveId),
    cave_done: parseInt(caveFound),
  };
  console.log("DATA ->", data)

  if (caveFound == 2) {
    fetch('/cave_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        cave_id: caveId  // Pass the variable to the server
      })
    })
  }

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