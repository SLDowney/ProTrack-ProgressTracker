window.addEventListener('DOMContentLoaded', function() {
  //var sortByLocationBtn = document.getElementById("sort-by-location-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  console.log("Sort By Coord Button ->", sortByCoordBtn)
  var sortByTypeBtn = document.getElementById("sort-by-type-btn");
  var sortByFoundBtn = document.getElementById("sort-by-found-btn");
  var enemiesTable = document.getElementById('enemies-table');

  var isLocationSortAscending = true;
  var isCoordSortAscending = true;
  var isTypeSortAscending = true;
  var isStartSortAscending = true;
  var isFoundSortAscending = true;

  Array.from(enemiesTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

      // Update Done cell when checkbox is clicked
      const enemyId = checkbox.name.replace('e_found_', ''); // Extract enemy ID
      console.log("Enemy ID ->", enemyId)
    
      updateenemy(checkbox, enemyId); // Pass enemyId to updateenemy function
    });
});
  

  // sortByLocationBtn.addEventListener("click", function(event) {
  //   event.preventDefault();
  //   sortenemies('location');
  //   isLocationSortAscending = !isLocationSortAscending;
  // });

  sortByCoordBtn.addEventListener("click", function(event) {
    console.log("Clicked Sort by Coord")
    event.preventDefault();
    sortenemies('coord');
    isCoordSortAscending = !isCoordSortAscending;
  });

  sortByTypeBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortenemies('type');
    isTypeSortAscending = !isTypeSortAscending;
  });

  

  
});

var enemyTable = document.getElementById('enemies-table');

function extractCoord(enemyRow) {
  var coordCell = enemyRow.cells[4];
  if (coordCell) {
    var coordParts = coordCell.textContent.split(', ');
    return coordParts.join('');
  }
  return '';
}

function updateenemy(checkbox, enemyId) {
    console.log("--------UPDATE enemy ---------")
  const enemyFound = checkbox.checked ? 1 : 0;
  console.log("Enemy ID ->", enemyId)
  console.log("Enemy Found ->", enemyFound)

  const data = {
    enemy_id: parseInt(enemyId),
    enemy_done: enemyFound,
  };
  console.log("DATA ->", data)
  console.log("Enemy ID ->", enemyId)
  console.log("Enemy Found ->", enemyFound)
  fetch('/update_enemy', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      enemy_id: enemyId,
      enemy_done: enemyFound  // Pass the variable to the server
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

function sortenemies(sortType) {
  var enemies = Array.from(enemyTable.getElementsByTagName('tr'));
  enemies.shift(); // Remove header row from sorting

  enemies.sort(function(a, b) {
    var aValue, bValue;

    // if (sortType === 'location') {
    //   aValue = a.cells[1].textContent.toLowerCase();
    //   bValue = b.cells[1].textContent.toLowerCase();
    // } else 
    if (sortType === 'coord') {
      aValue = extractCoord(a);
      bValue = extractCoord(b);
    } else if (sortType === 'type') {
      aValue = a.cells[3].textContent.toLowerCase();
      bValue = b.cells[3].textContent.toLowerCase();
    } else if (sortType === 'found') {
      aValue = a.cells[0].querySelector('input[type="checkbox"]').checked;
      bValue = b.cells[0].querySelector('input[type="checkbox"]').checked;
      console.log("aValue ->", aValue)
      console.log("bValue ->", bValue)

    }

    if (aValue && bValue) {
      if (aValue < bValue) {
        return sortType === 'found' ? (isFoundSortAscending ? -1 : 1) : -1;
      } else if (aValue > bValue) {
        return sortType === 'found' ? (isFoundSortAscending ? 1 : -1) : 1;
      } else {
        return 0;
      }
    } else if (aValue) {
      return -1;
    } else if (bValue) {
      return 1;
    }
  });

  var tbody = enemyTable.querySelector('tbody');
  enemies.forEach(function(enemy) {
    tbody.appendChild(enemy);
  });
}