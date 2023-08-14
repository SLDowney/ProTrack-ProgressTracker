window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var fairyTable = document.getElementById('fairyForm');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(fairyTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when checkbox is clicked
        const fairyId = checkbox.id.replace('fairy_', ''); // Extract fairy ID
      
        //updatefairy(checkbox, fairyId); // Pass fairyReward to updatefairy function
    });
});
 
  });

var fairyTable = document.getElementById('fairyForm');

function updatefairy(checkbox, fairyId) {
    console.log("--------UPDATE fairy ---------")
    const fairyFound = checkbox.checked ? 1 : 0;

    const data = {
        fairy_id: parseInt(fairyId),
        fairy_done: fairyFound,
    };
    console.log("DATA ->", data)

    fetch(`/update_greatfairies/${fairyId}/${fairyFound}`, {
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