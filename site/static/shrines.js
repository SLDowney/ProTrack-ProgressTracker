function shrineShow() {
  Array.from(document.getElementsByClassName("shrine_all")).forEach(function (element) {
    const shrineStatus = element.id.replace('shrineStatus_', ''); // Extract shrine ID;
    if (shrineStatus != 0) {
      element.classList.remove("hidden_display");
    }
    else {
      element.classList.add("hidden_display");
    }
    console.log("shrine shrineStatus ->", shrineStatus)
})
}

function shrineFind() {
  let textbox = document.getElementById("find_shrine");
  let text = textbox.value.toLowerCase();
  console.log("Text ->", text)
  Array.from(document.getElementsByClassName("shrine_all")).forEach(function (element) {
    console.log("Element ->", element)
    let shrineName = element.getAttribute('name').toLowerCase();
    
    if (shrineName && typeof shrineName === 'string') {
        shrineName = shrineName.replace('shrine_name_', '');
        console.log("Shrine Name ->", shrineName);
    } else {
        console.log("Element does not have a valid 'name' attribute.");
    }
    console.log("Shrine Name ->", shrineName)    
    if (shrineName.includes(text)) {
      element.classList.remove("hidden_display");
    }
    else {
      element.classList.add("hidden_display");
    }
    console.log("shrine shrineName ->", shrineName)
})
}

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

  const findShrineInput = document.getElementById("find_shrine");
  const searchButton = document.getElementById("searchButton");

  findShrineInput.focus(); // Set focus on the input field

  // Add an event listener to detect "Enter" key press
  findShrineInput.addEventListener("keyup", function (event) {
      if (event.key === "Enter") {
          // Activate the search button when Enter is pressed
          searchButton.click();
      }
  });
  shrineShow()
  Array.from(document.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('change', function () {
      const shrineId = radio.name.replace('done_', ''); // Extract shrine ID;
      console.log("shrineID ->", shrineId)
      updateshrine(radio, shrineId)
      infoToggle(radio);
      shrineShow()
    });
    if (radio.checked) {
      infoToggle(radio);
      shrineShow()
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

window.addEventListener("scroll", function () {
  var button = document.getElementById("return-to-top");
  if (window.scrollY > 300) {
      button.style.display = "block";
  } else {
      button.style.display = "none";
  }
});

// Smooth scrolling to the top when the button is clicked
document.getElementById("return-to-top").addEventListener("click", function () {
  window.scrollTo({
      top: 0,
      behavior: "smooth"
  });
});

function scrollToLetter(letter) {
  const section = document.getElementById(`letter-${letter}`);
  if (section) {
      section.scrollIntoView({ behavior: "smooth" });
  }
}

// Add click event listeners to index links
const indexLinks = document.querySelectorAll('.shrine-index-link');
indexLinks.forEach(link => {
  link.addEventListener('click', (event) => {
      event.preventDefault();
      const letter = event.target.textContent;
      scrollToLetter(letter);
  });
});