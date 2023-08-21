window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var greatfairyTable = document.getElementById('great_fairy_fountain-table');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(greatfairyTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when checkbox is clicked
        const greatfairyId = checkbox.id.replace('done_', ''); // Extract greatfairy ID
      
        updategreatfairy(checkbox, greatfairyId); // Pass greatfairyReward to updategreatfairy function
    });
});
 
  });

var greatfairyTable = document.getElementById('great_fairy_fountain-table');

function updategreatfairy(checkbox, greatfairyId) {
    console.log("--------UPDATE greatfairy ---------")
  const greatfairyFound = checkbox.checked ? 1 : 0;

  const data = {
    greatfairy_id: parseInt(greatfairyId),
    greatfairy_done: greatfairyFound,
  };
  console.log("DATA ->", data)

  fetch('/update_great_fairy_fountain', {
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