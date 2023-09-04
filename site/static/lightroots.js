function lightrootShow() {
  Array.from(document.getElementsByClassName("lightroot_all")).forEach(function (element) {
    const lightrootStatus = element.id.replace('lightrootStatus_', ''); // Extract lightroot ID;
    if (lightrootStatus != 0) {
      element.classList.remove("hidden_display");
    }
    else {
      element.classList.add("hidden_display");
    }
    console.log("lightroot lightrootStatus ->", lightrootStatus)
})
}

function lightrootFind() {
  let textbox = document.getElementById("find_lightroot");
  let text = textbox.value.toLowerCase();
  console.log("Text ->", text)
  Array.from(document.getElementsByClassName("lightroot_all")).forEach(function (element) {
    console.log("Element ->", element)
    let lightrootName = element.getAttribute('name').toLowerCase();
    
    if (lightrootName && typeof lightrootName === 'string') {
        lightrootName = lightrootName.replace('lightroot_name_', '');
        console.log("lightroot Name ->", lightrootName);
    } else {
        console.log("Element does not have a valid 'name' attribute.");
    }
    console.log("lightroot Name ->", lightrootName)    
    if (lightrootName.includes(text)) {
      element.classList.remove("hidden_display");
    }
    else {
      element.classList.add("hidden_display");
    }
    console.log("lightroot lightrootName ->", lightrootName)
})
}

window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------");
  lightrootShow();
  var lightrootTable = document.getElementById('rootform');
  var checkboxes = document.querySelectorAll('.location_checkbox');

  checkboxes.forEach(function (checkbox) {
    // Check the initial state of the checkbox and apply the class accordingly
    var rootId = checkbox.id.replace('done_', ''); // Extract point ID
    var rootIDElements = document.querySelectorAll(".root_" + rootId);

    rootIDElements.forEach(function (element) {
      if (checkbox.checked) {
        element.classList.remove("hidden_display"); // Show info
      } 
    });
  });
  // Add the event listener to the checkboxs to update the counter and Rewards column
  Array.from(lightrootTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {
      console.log("In array")
        // Update Rewards cell when checkbox is clicked
        const lightrootId = checkbox.name.replace('done_root_', ''); // Extract lightroot ID
        console.log("lightroot ID ->", lightrootId)
      
        updatelightroot(checkbox, lightrootId); // Pass lightrootReward to updatelightroot function
        infoToggle(checkbox)
    });
});
 
  });

var lightrootTable = document.getElementById('rootform');

function updatelightroot(checkbox, lightrootId) {
    console.log("--------UPDATE lightroot ---------")
  const lightrootFound = checkbox.checked ? 1 : 0;
  console.log("lightrootFound ->", lightrootFound)

  const data = {
    lightroot_id: parseInt(lightrootId),
    lightroot_done: parseInt(lightrootFound),
  };
  console.log("DATA ->", data)

  fetch('/update_lightroots', {
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

function infoToggle(checkbox) {
  var rootId = checkbox.id.replace('done_', ''); // Extract point ID
  console.log("Root ID ->", rootId)
  var rootIDElements = document.querySelectorAll(".root_" + rootId);
  console.log("Root Elements ->", rootIDElements)

  rootIDElements.forEach(function (element) {
    if (checkbox.checked) {
      element.classList.remove("hidden_display"); // Show info
    } else {
      element.classList.add("hidden_display"); // Hide info
    }
  });
}
