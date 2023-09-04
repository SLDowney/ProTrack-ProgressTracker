window.addEventListener('DOMContentLoaded', function() {
  var camp_chestTable = document.getElementById('camp_chests-list');

  Array.from(camp_chestTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

      // Update Rewards cell when checkbox is clicked
      const camp_chestId = checkbox.id.replace('camp_chest_id_', ''); // Extract chest ID
    
      updatechest(checkbox, camp_chestId); // Pass chestReward to updatechest function
    });
});
  var sortByNameBtn = document.getElementById("sort-by-name-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var camp_chestsList = document.getElementById('camp_chests-list');

  var isNameSortAscending = true;
  var isCoordSortAscending = true;

  if (sortByNameBtn && sortByCoordBtn && camp_chestsList) {
    sortByNameBtn.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent form submission
      sortcamp_chests('name');
      isNameSortAscending = !isNameSortAscending; // Toggle sorting order
    });

    sortByCoordBtn.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent form submission
      sortcamp_chests('coord');
      isCoordSortAscending = !isCoordSortAscending; // Toggle sorting order
    });
  }

  function sortcamp_chests(sortType) {
    var camp_chests = Array.from(camp_chestsList.getElementsByTagName('li'));

    camp_chests.sort(function(a, b) {
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

    camp_chests.forEach(function(camp_chest) {
      camp_chestsList.appendChild(camp_chest);
    });
  }

  function extractCoord(camp_chestElement) {
    var camp_chestCoord = camp_chestElement.querySelector('p:nth-of-type(2)').textContent;
    var coordParts = camp_chestCoord.split(' ');
    return coordParts.join('');
  }
});

var camp_chestTable = document.getElementById('camp_chests-list');

function updatechest(checkbox, camp_chestId) {
  console.log("--------UPDATE camp_chest ---------")
  const camp_chestFound = checkbox.checked ? 1 : 0;;

  const data = {
    camp_chest_id: parseInt(camp_chestId),
    camp_chest_done: parseInt(camp_chestFound),
  };
  console.log("DATA ->", data)
  
    fetch('/camp_chest_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        camp_chest_id: camp_chestId,  // Pass the variable to the server
        camp_chest_done: camp_chestFound
      })
    })
  
  fetch('/update_camp_chests', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      camp_chest_id: camp_chestId,  // Pass the variable to the server
      camp_chest_done: camp_chestFound
    })
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