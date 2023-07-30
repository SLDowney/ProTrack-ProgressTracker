window.addEventListener('DOMContentLoaded', function() {
  // Function to hide all armor upgrade sections
  function hideAllArmorUpgrades() {
    document.querySelectorAll('.armor_upgrade').forEach(function(section) {
      section.style.display = 'none';
    });
  }

  function updateArmorSections() {
    // Use the correct class name for the Great Fairy checkboxes
    var checkedGreatFairies = document.querySelectorAll('.form-checkbox-input:checked');

    // Hide all armor upgrade sections initially
    hideAllArmorUpgrades();

    // Show the specific armor upgrade section based on the number of Great Fairies checked
    if (checkedGreatFairies.length >= 1) {
      document.querySelectorAll('.level-1').forEach(function(section) {
        section.style.display = 'block';
      });
    }
    if (checkedGreatFairies.length >= 2) {
      document.querySelectorAll('.level-2').forEach(function(section) {
        section.style.display = 'block';
      });
    }
    if (checkedGreatFairies.length >= 3) {
      document.querySelectorAll('.level-3').forEach(function(section) {
        section.style.display = 'block';
      });
    }
    if (checkedGreatFairies.length >= 4) {
      document.querySelectorAll('.level-4').forEach(function(section) {
        section.style.display = 'block';
      });
    }
  }

  // Add event listeners to the Great Fairy checkboxes
  document.querySelectorAll('input[name^="greatFairy_"]').forEach(function(checkbox) {
    checkbox.addEventListener('change', updateArmorSections);
  });

  // Initially hide all armor upgrade sections
  hideAllArmorUpgrades();

  // Update armor sections when the page loads
  updateArmorSections();

  var armorForm = document.getElementById("armor-form");

  armorForm.addEventListener("submit", function(event) {
    console.log("Submit clicked");
    event.preventDefault(); // Prevent form submission
    console.log("after prevent default")

    var checkboxes = document.querySelectorAll('input[name^="have_"]');
    console.log("Checkboxes -> ", checkboxes)
    checkboxes.forEach(function(checkbox) {
      console.log("forEach checkbox");
      var armorId = checkbox.value;
      var armorFound = checkbox.checked ? '1' : '0';

      // Perform AJAX request to update armor in the database
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/armors/update", true);
      xhr.setRequestHeader("Content-Type", "application/json");

      xhr.onreadystatechange = function() {
        console.log("onreadystatechange");
        console.log("Ready state:", xhr.readyState);
        console.log("Status:", xhr.status);
        if (xhr.readyState === XMLHttpRequest.DONE) {
          console.log("Request completed");
          if (xhr.status === 200) {
            console.log("Armor updated successfully");
          } else {
            console.error("Failed to update armor");
          }
        }
      };

      xhr.onerror = function() {
        console.error("An error occurred during the request");
      };

      var data = JSON.stringify({ armorId: armorId, armorFound: armorFound });
      xhr.send(data);
    });
  });
});
