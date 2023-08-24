window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var gemsTable = document.getElementById('gems-table');

  function updatePercentageCounter() {
    var totalgems = gemsTable.getElementsByTagName('tr').length - 1;
    var totalFoundgems = Array.from(gemsTable.querySelectorAll('input[type="checkbox"]')).reduce(function (total, checkbox) {
      return total + (checkbox.checked ? 1 : 0);
    }, 0);

    var percentageFound = (totalFoundgems / totalgems) * 100;
    document.getElementById('percentage-found').textContent = percentageFound.toFixed(2);
  }

  // Call the function on page load
  updatePercentageCounter();

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(gemsTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {
        updatePercentageCounter();

        // Update Rewards cell when checkbox is clicked
        const gemId = checkbox.id.replace('gems_done_', ''); // Extract gem ID
        const gemReward = document.getElementById("gem_rewards_" + gemId).getAttribute('data-rewards'); // Get rewards value
      
        updategem(checkbox, gemId, gemReward); // Pass gemReward to updategem function
        rewardToggle(checkbox);
    });
    rewardToggle(checkbox);
});
 
  });

var gemsTable = document.getElementById('gems-table');

function updategem(checkbox, gemId, gemReward) {
    console.log("--------UPDATE gem ---------")
  const gemFound = checkbox.checked ? 1 : 0;

  const data = {
    gem_id: parseInt(gemId),
    gem_done: gemFound,
    gem_reward: gemReward
  };
  console.log("DATA ->", data)
  console.log("REWARDS ->", data.gem_reward)

  fetch('/update-gem', {
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
      //   rewardsCell.textContent = data.gemReward;
      //   console.log("Rewards Cell Checked ->", data.gemReward) // Use the actual property name from the response
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
  var gemId = checkbox.id.replace('gems_done_', ''); // Extract gem ID
  var gemRewardsElement = document.getElementById("gem_rewards_" + gemId);

  if (checkbox.checked) {
    var rewards = gemRewardsElement.getAttribute('data-rewards'); // Get rewards value using getAttribute
    gemRewardsElement.textContent = rewards; // Show rewards value
  } else {
    gemRewardsElement.textContent = "???"; // Show "???" when unchecked
  }
}