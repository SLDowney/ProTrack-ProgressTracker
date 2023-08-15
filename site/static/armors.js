window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var armorTable = document.getElementById('armorForm');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(armorTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        const armorId = checkbox.id.replace('armor_id_', ''); // Extract armor ID
      
        updatearmor(checkbox, armorId); // Pass armor to updatearmor function
    });
});
 
  });

var armorTable = document.getElementById('armorForm');

function updatearmor(checkbox, armorId) {
    console.log("--------UPDATE armor ---------")
    const armorFound = checkbox.checked ? 1 : 0;

    const data = {
        armor_id: parseInt(armorId),
        armor_done: armorFound,
    };
    console.log("DATA ->", data)

    fetch(`/update_armor/${armorId}/${armorFound}`, {
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