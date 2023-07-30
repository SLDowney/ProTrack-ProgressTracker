window.addEventListener('DOMContentLoaded', function() {
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
