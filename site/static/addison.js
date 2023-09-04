window.addEventListener('DOMContentLoaded', function () {
    console.log("-----------------------------")
    var addisonTable = document.getElementById('addisonform');
    var checkboxes = document.querySelectorAll('.addison_checkbox');
  
    checkboxes.forEach(function (checkbox) {
      // Check the initial state of the checkbox and apply the class accordingly
      var addisonId = checkbox.id.replace('done_', ''); // Extract point ID
      var addisonIDElements = document.querySelectorAll(".addison_" + addisonId);
  
      addisonIDElements.forEach(function (element) {
        if (checkbox.checked) {
          element.classList.remove("hidden_display"); // Show info
        } 
      });
    });
  
    // Add the event listener to the checkboxes to update the counter and Rewards column
    Array.from(addisonTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
      checkbox.addEventListener('click', function () {
  
          // Update Rewards cell when checkbox is clicked
          const addisonId = checkbox.id.replace('done_', ''); // Extract addison ID
        
          updateaddison(checkbox, addisonId); // Pass addisonReward to updateaddison function
          infoToggle(checkbox)
      });
    });
  });
  
  var addisonTable = document.getElementById('addison-table');
  
  function updateaddison(checkbox, addisonId) {
      console.log("--------UPDATE addison ---------")
    const addisonFound = checkbox.checked ? 1 : 0;
  
    const data = {
      addison_id: parseInt(addisonId),
      addison_done: addisonFound,
    };
    console.log("DATA ->", data)
  
    fetch('/update_addison', {
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
    var addisonId = checkbox.id.replace('done_', ''); // Extract point ID
    console.log("addison ID ->", addisonId)
    var addisonIDElements = document.querySelectorAll(".addison_" + addisonId);
    console.log("addison Elements ->", addisonIDElements)
  
    addisonIDElements.forEach(function (element) {
      if (checkbox.checked) {
        element.classList.remove("hidden_display"); // Show info
      } else {
        element.classList.add("hidden_display"); // Hide info
      }
    });
  }