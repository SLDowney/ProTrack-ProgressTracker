window.addEventListener('DOMContentLoaded', function() {
  var sortByNameBtn = document.getElementById("sort-by-name-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var chestsList = document.getElementById('chests-list');

  var isNameSortAscending = true;
  var isCoordSortAscending = true;
  console.log("-----------------------------")
  var chestTable = document.getElementById('chestform');

  // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(chestTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
      checkbox.addEventListener('click', function () {

        // Update Rewards cell when checkbox is clicked
        const chestId = checkbox.id.replace('chest_id_', ''); // Extract chest ID
      
        updatechest(checkbox, chestId); // Pass chestReward to updatechest function
      });
  });

  if (sortByNameBtn && sortByCoordBtn && chestsList) {
    sortByNameBtn.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent form submission
      sortChests('name');
      isNameSortAscending = !isNameSortAscending; // Toggle sorting order
    });

    sortByCoordBtn.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent form submission
      sortChests('coord');
      isCoordSortAscending = !isCoordSortAscending; // Toggle sorting order
    });
  }

  function sortChests(sortType) {
    var chests = Array.from(chestsList.getElementsByTagName('li'));

    chests.sort(function(a, b) {
      var aValue, bValue;

      if (sortType === 'name') {
        aValue = a.querySelector("p").textContent;
        bValue = b.querySelector("p").textContent;
      } else if (sortType === 'coord') {
        aValue = extractCoord(a);
        bValue = extractCoord(b);
      }

      // Customize your sorting logic here
      if (sortType === 'name') {
        if (aValue < bValue) {
          return isNameSortAscending ? -1 : 1;
        } else if (aValue > bValue) {
          return isNameSortAscending ? 1 : -1;
        } else {
          return 0;
        }
      } else if (sortType === 'coord') {
        if (aValue < bValue) {
          return isCoordSortAscending ? -1 : 1;
        } else if (aValue > bValue) {
          return isCoordSortAscending ? 1 : -1;
        } else {
          return 0;
        }
      }
    });

    chests.forEach(function(chest) {
      chestsList.appendChild(chest);
    });
  }

  function extractCoord(chestElement) {
    var chestCoord = chestElement.querySelector('p:nth-of-type(2)').textContent;
    var coordParts = chestCoord.split(' ');
    return coordParts.join('');
  }
});

var chestTable = document.getElementById('chestform');

function updatechest(checkbox, chestId) {
  console.log("--------UPDATE chest ---------")
  const chestFound = checkbox.value;

  const data = {
    chest_id: parseInt(chestId),
    chest_done: parseInt(chestFound),
  };
  console.log("DATA ->", data)
  
  if (chestFound == 1) {
    fetch('/chest_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        chest_id: chestId  // Pass the variable to the server
      })
    })
  }
  
  fetch('/update_chests', {
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