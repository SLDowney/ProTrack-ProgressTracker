window.addEventListener('DOMContentLoaded', function() {
  var sortByNameBtn = document.getElementById("sort-by-name-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var chestsList = document.getElementById('chests-list');

  var isNameSortAscending = true;
  var isCoordSortAscending = true;

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
