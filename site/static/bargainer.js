window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var bargainTable = document.getElementById('bargainer_statue-table');
  console.log("Bargain Table ->", bargainTable)

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(bargainTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when checkbox is clicked
        const bargainId = checkbox.id.replace('done_', ''); // Extract bargain ID
        console.log("Bargain ID ->", bargainId)
      
        updatebargain(checkbox, bargainId); // Pass bargainReward to updatebargain function
    });
});
 
  });

var bargainTable = document.getElementById('bargainer_statue-table');

function updatebargain(checkbox, bargainId) {
    console.log("--------UPDATE bargain ---------")
  const bargainFound = checkbox.checked ? 1 : 0;

  const data = {
    bargain_id: parseInt(bargainId),
    bargain_done: bargainFound,
  };
  console.log("DATA ->", data)

  fetch('/update_bargain', {
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