window.addEventListener('DOMContentLoaded', function() {
  var sortByLocationBtn = document.getElementById("sort-by-location-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var sortByTypeBtn = document.getElementById("sort-by-type-btn");
  var enemiesTable = document.getElementById('enemies-table');

  var isLocationSortAscending = true;
  var isCoordSortAscending = true;
  var isTypeSortAscending = true;
  var isStartSortAscending = true;
  var isFoundSortAscending = true;

  sortByLocationBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortenemies('location');
    isLocationSortAscending = !isLocationSortAscending;
  });

  sortByCoordBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortenemies('coord');
    isCoordSortAscending = !isCoordSortAscending;
  });

  sortByTypeBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortenemies('type');
    isTypeSortAscending = !isTypeSortAscending;
  });

  function sortenemies(sortType) {
    var enemies = Array.from(enemiesTable.getElementsByTagName('tr'));
    enemies.shift(); // Remove header row from sorting

    enemies.sort(function(a, b) {
      var aValue, bValue;

      if (sortType === 'location') {
        aValue = a.cells[1].textContent.toLowerCase();
        bValue = b.cells[1].textContent.toLowerCase();
      } else if (sortType === 'coord') {
        aValue = extractCoord(a);
        bValue = extractCoord(b);
      } else if (sortType === 'type') {
        aValue = a.cells[3].textContent.toLowerCase();
        bValue = b.cells[3].textContent.toLowerCase();
      } else if (sortType === 'found') {
        aValue = a.cells[0].querySelector('input[type="checkbox"]').checked;
        bValue = b.cells[0].querySelector('input[type="checkbox"]').checked;
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

    var tbody = enemiesTable.querySelector('tbody');
    enemies.forEach(function(enemy) {
      tbody.appendChild(enemy);
    });
  }

  function extractCoord(enemyRow) {
    var coordCell = enemyRow.cells[4];
    if (coordCell) {
      var coordParts = coordCell.textContent.split(', ');
      return coordParts.join('');
    }
    return '';
  }
});
