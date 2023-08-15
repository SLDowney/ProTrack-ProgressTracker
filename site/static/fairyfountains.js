window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var fairyTable = document.getElementById('fairyForm');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(fairyTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        const fairyId = checkbox.id.replace('fairy_', ''); // Extract fairy ID
      
        //updatefairy(checkbox, fairyId); // Pass fairy to updatefairy function
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

  // Function to determine the required number of great fairies based on the armor set and upgrade level
function getRequiredGreatFairies(armorId, upgradeLevel) {
    // Implement your logic to determine the required number of great fairies
    // based on the armor set and upgrade level
    // You can use a switch statement or any other method to calculate the requirements
    let requiredGreatFairies = 0;

    switch (armorId) {
        case "armor_id_1":
            switch (upgradeLevel) {
                case "level1":
                    requiredGreatFairies = 1;
                    break;
                case "level2":
                    requiredGreatFairies = 2;
                    break;
                case "level3":
                    requiredGreatFairies = 3;
                    break;
                case "level4":
                    requiredGreatFairies = 4;
                    break;
            }
            break;
        // Add more cases for other armor sets as needed
        // case "armor_id_2":
        //     // ...
        //     break;
        // ...
    }

    return requiredGreatFairies;
}

// Function to retrieve the number of found great fairies from the checkboxes on the webpage
function getFoundGreatFairies() {
    const greatFairyCheckboxes = document.querySelectorAll(".great-fairy-checkboxes");
    let foundGreatFairies = 0;

    for (const checkbox of greatFairyCheckboxes) {
        if (checkbox.checked) {
            foundGreatFairies++;
        }
    }

    return foundGreatFairies;
}

// Function to update the upgrades display based on collected armors and great fairies
function updateUpgradesDisplay() {
    // Your existing code to update the upgrades display goes here

    // Get the armor sets and iterate through them
    const armorSets = document.querySelectorAll(".armor_set");
    armorSets.forEach((armorSet) => {
        // Get the armor id and upgrade level
        const armorId = armorSet.querySelector(".collected-checkbox").id;
        const upgradeLevel = armorSet.querySelector(".level1-checkbox:checked, .level2-checkbox:checked, .level3-checkbox:checked, .level4-checkbox:checked");

        // Get the required and found great fairies
        const requiredGreatFairies = getRequiredGreatFairies(armorId, upgradeLevel.value);
        const foundGreatFairies = getFoundGreatFairies();

        // Compare and update the display as needed
        const upgradeDiv = armorSet.querySelector(`.armor_upgrade_${upgradeLevel.value}`);
        if (requiredGreatFairies <= foundGreatFairies) {
            upgradeDiv.style.display = "block";
        } else {
            upgradeDiv.style.display = "none";
        }
    });
}

