// Function to update great fairies
function updatefairy(fairyId, fairyDone) {
    // Update the database and perform any necessary UI updates
    fetch('/update_great_fairy_fountain', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            fairy_id: parseInt(fairyId), // Pass the variable to the server
            fairy_done: fairyDone
        })
    })
    console.log("Fairy ID ->", fairyId)
}

// Function to update armor upgrades display
function updateUpgradesDisplay() {
    var armorSets = document.getElementsByClassName("armor_set");
    var greatFairyCheckboxes = document.getElementsByClassName("great-fairy-checkboxes");
    console.log("Armor Sets ->", armorSets)
    //console.log("Great Fairy Checkboxes ->", greatFairyCheckboxes)
    checkedFairies = 0
    //const towerFound = checkbox.checked ? 1 : 0;
    Array.from(greatFairyCheckboxes).forEach(function (checkbox) {
        //console.log("Checkboxes ->", checkbox)
        if (checkbox.checked) {
            checkedFairies = checkedFairies + 1
        }
    })
  
    
    //console.log("Upgrade 1 div? ->", upgradeDiv)
    
    // Loop through armor sets
    for (var i = 0; i < armorSets.length; i++) {
        var armorSet = armorSets[i];
        //console.log("Armor Set ->", armorSet)
        let collectedCheckboxes = armorSet.getElementsByClassName("collected-checkbox");
        let upgrade_1_Checkboxes = armorSet.getElementsByClassName("level1-checkbox");
        let upgrade_2_Checkboxes = armorSet.getElementsByClassName("level2-checkbox");
        let upgrade_3_Checkboxes = armorSet.getElementsByClassName("level3-checkbox");
        let upgrade_4_Checkboxes = armorSet.getElementsByClassName("level4-checkbox");
        
        // Loop through the checkboxes within the current armorSet
        Array.from(collectedCheckboxes).forEach(function (checkbox) {
            //console.log("In array");
            //console.log("Checked Fairies ->", checkedFairies);
    
            // Get the corresponding upgradeDiv for the current checkbox
            var upgradeDiv = armorSet.querySelector('.armor_upgrade_container#armor_upgrade_1');
            //console.log("Upgrade Div ->", upgradeDiv)
            if (checkbox.checked && checkedFairies >= 1) {
                upgradeDiv.classList.remove("hidden_display");
                //console.log("REMOVED HIDDEN ->", upgradeDiv);
            }
            else {
                upgradeDiv.classList.add("hidden_display");
            }
        });

        Array.from(upgrade_1_Checkboxes).forEach(function (checkbox) {
            //console.log("In array");
            //console.log("Checked Fairies ->", checkedFairies);
    
            // Get the corresponding upgradeDiv for the current checkbox
            var upgradeDiv1 = armorSet.querySelector('.armor_upgrade_container#armor_upgrade_2');
            //console.log("Upgrade Div ->", upgradeDiv)
            if (checkbox.checked && checkedFairies >= 2) {
                upgradeDiv1.classList.remove("hidden_display");
                //console.log("REMOVED HIDDEN ->", upgradeDiv);
            }
            else {
                upgradeDiv1.classList.add("hidden_display");
            }
        });

        Array.from(upgrade_2_Checkboxes).forEach(function (checkbox) {
            //console.log("In array");
            //console.log("Checked Fairies ->", checkedFairies);
    
            // Get the corresponding upgradeDiv for the current checkbox
            var upgradeDiv2 = armorSet.querySelector('.armor_upgrade_container#armor_upgrade_3');
            //console.log("Upgrade Div ->", upgradeDiv)
            if (checkbox.checked && checkedFairies >= 3) {
                upgradeDiv2.classList.remove("hidden_display");
                //console.log("REMOVED HIDDEN ->", upgradeDiv);
            }
            else {
                upgradeDiv2.classList.add("hidden_display");
            }
        });

        Array.from(upgrade_3_Checkboxes).forEach(function (checkbox) {
            //console.log("In array");
            //console.log("Checked Fairies ->", checkedFairies);
    
            // Get the corresponding upgradeDiv for the current checkbox
            var upgradeDiv3 = armorSet.querySelector('.armor_upgrade_container#armor_upgrade_4');
            //console.log("Upgrade Div ->", upgradeDiv)
            if (checkbox.checked && checkedFairies >= 4) {
                upgradeDiv3.classList.remove("hidden_display");
                //console.log("REMOVED HIDDEN ->", upgradeDiv);
            }
            else {
                upgradeDiv3.classList.add("hidden_display");
            }
        });
    
    
        // Check the criteria for armor set upgrades
        //var shouldShowUpgrades = false; // Adjust this based on your criteria
        
        // Show/hide upgrade divs based on criteria
        
        //var upgradeDivs = armorSet.getElementsByClassName("armor_upgrade_container");
        // Array.from(upgradeDivs).forEach(function (div) {
        //     let upgrade_1 = div.querySelector("armor_upgrade_1")
        //     console.log("div ->", div)
        //     console.log("Upgrade 1 ->", upgrade_1)

        
        
        //console.log("Upgrade Div's ->", upgradeDivs)
        // for (var j = 0; j < upgradeDivs.length; j++) {
        //     var upgradeDiv = upgradeDivs[j];
        //     console.log("Each Upgrade Div ->", upgradeDiv)
        //     console.log("Collected Check ->", collectedCheck)
        //     Array.from(collectedCheck).forEach(function (checkbox) {
        //         if (checkbox.checked AND )
        //     }
        //     if (collectedCheck.checked)
        //     upgradeDiv.style.display = shouldShowUpgrades ? "block" : "none";
        // }
    }
    
    // Handle great fairy checkboxes if needed
    // ...
}

// Add event listeners to armor checkboxes
// var armorCheckboxes = document.getElementsByClassName("collected-checkbox");
// for (var i = 0; i < armorCheckboxes.length; i++) {
//     armorCheckboxes[i].addEventListener("click", updateUpgradesDisplay);
// }

// Add event listeners to great fairy checkboxes
var greatFairyCheckboxes = document.getElementsByClassName("great-fairy-checkboxes");
for (var i = 0; i < greatFairyCheckboxes.length; i++) {
    //greatFairyCheckboxes[i].addEventListener("click", updatefairy);
    greatFairyCheckboxes[i].addEventListener("click", updateUpgradesDisplay);
}

window.addEventListener('DOMContentLoaded', function () {
    console.log("-----------------------------")
    var armorTable = document.getElementById('armorForm');
    let armor_collected = this.document.getElementById('armor_collected')
    let armor_upgrade_1 = this.document.getElementById('armor_upgrade_1')
    let armor_upgrade_2 = this.document.getElementById('armor_upgrade_2')
    let armor_upgrade_3 = this.document.getElementById('armor_upgrade_3')
    let armor_upgrade_4 = this.document.getElementById('armor_upgrade_4')
    var fairyTable = document.getElementById('fairyForm');
    updateUpgradesDisplay();
  
    // Add the event listener to the checkboxes to update the counter and Rewards column
    Array.from(fairyTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
        checkbox.addEventListener('click', function () {
    
            const fairyId = checkbox.id.replace('fairy_', ''); // Extract fairy ID
            const fairyDone = checkbox.checked ? 1 : 0;
          
            updatefairy(fairyId, fairyDone); // Pass fairy to updatefairy function
            updateUpgradesDisplay();
        });
    });
    // Add the event listener to the checkboxes to update the counter and Rewards column
    Array.from(armor_collected.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
      checkbox.addEventListener('click', function () {
  
          const armorId = checkbox.id.replace('armor_id_', ''); // Extract armor ID
          if (armorId != 97 || armorId != 98 || armorId != 99) {
            console.log("Armor ID ->", armorId)
            updatearmor(checkbox, armorId); // Pass armor to updatearmor function
            updateUpgradesDisplay();
          }
      });
  });

    Array.from(armor_upgrade_1.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
        checkbox.addEventListener('click', function () {

            const armorId = checkbox.id.replace('armor_up1_', ''); // Extract armor ID
            if (armorId != 97 || armorId != 98 || armorId != 99) {
                armorUpgrade1(checkbox, armorId); // Pass armor to updatearmor function
                updateUpgradesDisplay();
            }
        });
    });

    Array.from(armor_upgrade_2.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
        checkbox.addEventListener('click', function () {

            const armorId = checkbox.id.replace('armor_up2_', ''); // Extract armor ID
            if (armorId != 97 || armorId != 98 || armorId != 99) {
                armorUpgrade2(checkbox, armorId); // Pass armor to updatearmor function
                updateUpgradesDisplay();
            }
        });
    });

    Array.from(armor_upgrade_3.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
        checkbox.addEventListener('click', function () {

            const armorId = checkbox.id.replace('armor_up3_', ''); // Extract armor ID
            if (armorId != 97 || armorId != 98 || armorId != 99) {
                armorUpgrade3(checkbox, armorId); // Pass armor to updatearmor function
                updateUpgradesDisplay();
            }
        });
    });

    Array.from(armor_upgrade_4.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
        checkbox.addEventListener('click', function () {

            const armorId = checkbox.id.replace('armor_up4_', ''); // Extract armor ID
            if (armorId != 97 || armorId != 98 || armorId != 99) {
                armorUpgrade4(checkbox, armorId); // Pass armor to updatearmor function
                updateUpgradesDisplay();
            }
        });
    });
   
    });
  
//   var fairyTable = document.getElementById('fairyForm');
  
//   function updatefairy(checkbox, fairyId) {
//       console.log("--------UPDATE fairy ---------")
//       const fairyFound = checkbox.checked ? 1 : 0;
  
//       const data = {
//           fairy_id: parseInt(fairyId),
//           fairy_done: fairyFound,
//       };
//       console.log("DATA ->", data)
  
//       fetch(`/update_greatfairies/${fairyId}/${fairyFound}`, {
//           method: 'POST',
//           headers: {
//               'Content-Type': 'application/json',
//           },
//           body: JSON.stringify(data),
//       })
//         .then(response => response.json())
//         .then(data => {
//             // Handle the response if needed
//             console.log('Response from server:', data);
  
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     }
  
//     // Function to determine the required number of great fairies based on the armor set and upgrade level
//   function getRequiredGreatFairies(armorId, upgradeLevel) {
//       // Implement your logic to determine the required number of great fairies
//       // based on the armor set and upgrade level
//       // You can use a switch statement or any other method to calculate the requirements
//       let requiredGreatFairies = 0;
  
//       switch (armorId) {
//           case "armor_id_1":
//               switch (upgradeLevel) {
//                   case "level1":
//                       requiredGreatFairies = 1;
//                       break;
//                   case "level2":
//                       requiredGreatFairies = 2;
//                       break;
//                   case "level3":
//                       requiredGreatFairies = 3;
//                       break;
//                   case "level4":
//                       requiredGreatFairies = 4;
//                       break;
//               }
//               break;
//           // Add more cases for other armor sets as needed
//           // case "armor_id_2":
//           //     // ...
//           //     break;
//           // ...
//       }
  
//       return requiredGreatFairies;
//   }
  
//   // Function to retrieve the number of found great fairies from the checkboxes on the webpage
//   function getFoundGreatFairies() {
//       const greatFairyCheckboxes = document.querySelectorAll(".great-fairy-checkboxes");
//       let foundGreatFairies = 0;
  
//       for (const checkbox of greatFairyCheckboxes) {
//           if (checkbox.checked) {
//               foundGreatFairies++;
//           }
//       }
  
//       return foundGreatFairies;
//   }
  
//   // Function to update the upgrades display based on collected armors and great fairies
//   function updateUpgradesDisplay() {
//       // Your existing code to update the upgrades display goes here
  
//       // Get the armor sets and iterate through them
//       const armorSets = document.querySelectorAll(".armor_set");
//       armorSets.forEach((armorSet) => {
//           // Get the armor id and upgrade level
//           const armorId = armorSet.querySelector(".collected-checkbox").id;
//           const upgradeLevel = armorSet.querySelector(".level1-checkbox:checked, .level2-checkbox:checked, .level3-checkbox:checked, .level4-checkbox:checked");
  
//           // Get the required and found great fairies
//           //const requiredGreatFairies = getRequiredGreatFairies(armorId, upgradeLevel.value);
//           //const foundGreatFairies = getFoundGreatFairies();
  
//           // Compare and update the display as needed
//           const upgradeDiv = armorSet.querySelector(`.armor_upgrade_${upgradeLevel.value}`);
//           if (requiredGreatFairies <= foundGreatFairies) {
//               upgradeDiv.style.display = "block";
//           } else {
//               upgradeDiv.style.display = "none";
//           }
//       });
//   }
var armorTable = document.getElementById('armorForm');
//let upgrade_1_Checkboxes = armorSet.getElementsByClassName("level1-checkbox");
//let upgrade_2_Checkboxes = armorSet.getElementsByClassName("level2-checkbox");
//let upgrade_3_Checkboxes = armorSet.getElementsByClassName("level3-checkbox");
//let upgrade_4_Checkboxes = armorSet.getElementsByClassName("level4-checkbox");

  
  
function updatearmor(checkbox, armorId) {
    console.log("--------UPDATE armor ---------")
    const armorFound = checkbox.checked ? 1 : 0;

    const data = {
        armor_id: parseInt(armorId),
        armor_done: armorFound,
    };
    console.log("DATA ->", data)
    
    fetch('/update_armor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        armor_id: parseInt(armorId), // Pass the variable to the server
        armor_done: armorFound
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

function armorUpgrade1(checkbox, armorId) {
    console.log("--------UPDATE armor ---------")
    const armorFound = checkbox.checked ? 1 : 0;

    const data = {
        armor_id: parseInt(armorId),
        armor_done: armorFound,
    };
    console.log("DATA ->", data)
    if (armorId != 97 || armorId != 98 || armorId != 99) {
    fetch('/update_armor_1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
            armor_id: parseInt(armorId), // Pass the variable to the server
            armor_done: armorFound
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response if needed
            console.log('Response from server:', data);

        })
        .catch(error => {
            console.error('Error:', error);
        });
    }}

function armorUpgrade2(checkbox, armorId) {
    console.log("--------UPDATE armor ---------")
    const armorFound = checkbox.checked ? 1 : 0;

    const data = {
        armor_id: parseInt(armorId),
        armor_done: armorFound,
    };
    console.log("DATA ->", data)
    if (armorId != 97 || armorId != 98 || armorId != 99) {
    fetch('/update_armor_2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
            armor_id: parseInt(armorId), // Pass the variable to the server
            armor_done: armorFound
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response if needed
            console.log('Response from server:', data);

        })
        .catch(error => {
            console.error('Error:', error);
        });
}}

function armorUpgrade3(checkbox, armorId) {
    console.log("--------UPDATE armor ---------")
    const armorFound = checkbox.checked ? 1 : 0;

    const data = {
        armor_id: parseInt(armorId),
        armor_done: armorFound,
    };
    console.log("DATA ->", data)
    if (armorId != 97 || armorId != 98 || armorId != 99) {
    fetch('/update_armor_3', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
            armor_id: parseInt(armorId), // Pass the variable to the server
            armor_done: armorFound
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response if needed
            console.log('Response from server:', data);

        })
        .catch(error => {
            console.error('Error:', error);
        });
}}

function armorUpgrade4(checkbox, armorId) {
    console.log("--------UPDATE armor ---------")
    const armorFound = checkbox.checked ? 1 : 0;

    const data = {
        armor_id: parseInt(armorId),
        armor_done: armorFound,
    };
    console.log("DATA ->", data)
    if (armorId != 97 || armorId != 98 || armorId != 99) {
    fetch('/update_armor_4', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
            armor_id: parseInt(armorId), // Pass the variable to the server
            armor_done: armorFound
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
}