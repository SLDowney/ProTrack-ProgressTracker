window.addEventListener('DOMContentLoaded', function() {
    var armorForm = document.getElementById("armor-form");
  
    armorForm.addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent form submission
  
      var checkboxes = document.querySelectorAll('input[name^="have_armor_"]');
      checkboxes.forEach(function(checkbox) {
        var armorId = checkbox.value;
        var armorFound = checkbox.checked ? '1' : '0';
        
        // Perform AJAX request to update armor in the database
        updateArmor(armorId, armorFound);
      });
    });
  
    function updateArmor(armorId, armorFound) {
      // Perform AJAX request to update armor in the database
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/armors/update", true);
      xhr.setRequestHeader("Content-Type", "application/json");
  
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            console.log("Armor updated successfully");
          } else {
            console.error("Failed to update armor");
          }
        }
      };
  
      var data = JSON.stringify({ armorId: armorId, armorFound: armorFound });
      xhr.send(data);
    }
  });
  