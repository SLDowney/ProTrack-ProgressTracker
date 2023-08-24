window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var pointsTable = document.getElementById('points-table');

  function updatePercentageCounter() {
    var totalpoints = pointsTable.getElementsByTagName('tr').length - 1;
    var totalFoundpoints = Array.from(pointsTable.querySelectorAll('input[type="checkbox"]')).reduce(function (total, checkbox) {
      return total + (checkbox.checked ? 1 : 0);
    }, 0);

    var percentageFound = (totalFoundpoints / totalpoints) * 100;
    document.getElementById('percentage-found').textContent = percentageFound.toFixed(2);
  }

  // Call the function on page load
  updatePercentageCounter();

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(pointsTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {
        updatePercentageCounter();

        // Update Rewards cell when checkbox is clicked
        const pointId = checkbox.id.replace('points_done_', ''); // Extract point ID
        const pointReward = document.getElementById("point_rewards_" + pointId).getAttribute('data-rewards'); // Get rewards value
      
        updatepoint(checkbox, pointId, pointReward); // Pass pointReward to updatepoint function
        rewardToggle(checkbox);
    });
    rewardToggle(checkbox);
});
 
  });

var pointsTable = document.getElementById('points-table');

function updatepoint(checkbox, pointId, pointReward) {
    console.log("--------UPDATE POINT ---------")
  const pointFound = checkbox.checked ? 1 : 0;

  const data = {
    point_id: parseInt(pointId),
    point_done: pointFound,
    point_reward: pointReward
  };
  console.log("DATA ->", data)
  console.log("REWARDS ->", data.point_reward)

  fetch('/ponypoints_update', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      point_id: parseInt(pointId),
      point_done: pointFound,
      point_reward: pointReward  // Pass the variable to the server
    })
  })

  fetch('/update-point', {
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

      // Update the Rewards cell based on checkbox status
      // const rewardsCell = checkbox.parentNode.nextElementSibling.nextElementSibling.nextElementSibling;
      // if (checkbox.checked) {
      //   rewardsCell.textContent = data.pointReward;
      //   console.log("Rewards Cell Checked ->", data.pointReward) // Use the actual property name from the response
      // } else if (!checkbox.checked) {
      //   rewardsCell.textContent = '???';
      // }
      // else {
      //   rewardsCell.textContent = 'checkbox neither';
      // }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}


function rewardToggle(checkbox) {
  var pointId = checkbox.id.replace('points_done_', ''); // Extract point ID
  var pointRewardsElement = document.getElementById("point_rewards_" + pointId);

  if (checkbox.checked) {
    var rewards = pointRewardsElement.getAttribute('data-rewards'); // Get rewards value using getAttribute
    pointRewardsElement.textContent = rewards; // Show rewards value
  } else {
    pointRewardsElement.textContent = "???"; // Show "???" when unchecked
  }
}