window.addEventListener('DOMContentLoaded', function() {
  var sortByLocationBtn = document.getElementById("sort-by-location-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var sortByTypeBtn = document.getElementById("sort-by-type-btn");
  var sortByStartBtn = document.getElementById("sort-by-start-btn");
  var sortByFoundBtn = document.getElementById("sort-by-found-btn");
  var koroksTable = document.getElementById('koroks-table');

  var isLocationSortAscending = true;
  var isCoordSortAscending = true;
  var isTypeSortAscending = true;
  var isStartSortAscending = true;
  var isFoundSortAscending = true;

  sortByLocationBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortKoroks('location');
    isLocationSortAscending = !isLocationSortAscending;
  });

  sortByCoordBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortKoroks('coord');
    isCoordSortAscending = !isCoordSortAscending;
  });

  sortByTypeBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortKoroks('type');
    isTypeSortAscending = !isTypeSortAscending;
  });

  sortByStartBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortKoroks('start');
    isStartSortAscending = !isStartSortAscending;
  });

  sortByFoundBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortKoroks('found');
    isFoundSortAscending = !isFoundSortAscending;
  });

  function sortKoroks(sortType) {
    var koroks = Array.from(koroksTable.getElementsByTagName('tr'));
    koroks.shift(); // Remove header row from sorting

    koroks.sort(function(a, b) {
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
      } else if (sortType === 'start') {
        aValue = a.cells[5].textContent.toLowerCase();
        bValue = b.cells[5].textContent.toLowerCase();
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

    var tbody = koroksTable.querySelector('tbody');
    koroks.forEach(function(korok) {
      tbody.appendChild(korok);
    });
  }

  function extractCoord(korokRow) {
    var coordCell = korokRow.cells[4];
    if (coordCell) {
      var coordParts = coordCell.textContent.split(', ');
      return coordParts.join('');
    }
    return '';
  }
});
