window.addEventListener('DOMContentLoaded', function() {
  var sortByNameBtn = document.getElementById("sort-by-name-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var miscsList = document.getElementById('miscs-list');

  var isNameSortAscending = true;
  var isCoordSortAscending = true;

  if (sortByNameBtn && sortByCoordBtn && miscsList) {
    sortByNameBtn.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent form submission
      sortmiscs('name');
      isNameSortAscending = !isNameSortAscending; // Toggle sorting order
    });

    sortByCoordBtn.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent form submission
      sortmiscs('coord');
      isCoordSortAscending = !isCoordSortAscending; // Toggle sorting order
    });
  }

  function sortmiscs(sortType) {
    var miscs = Array.from(miscsList.getElementsByTagName('li'));

    miscs.sort(function(a, b) {
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

    miscs.forEach(function(misc) {
      miscsList.appendChild(misc);
    });
  }

  function extractCoord(miscElement) {
    var miscCoord = miscElement.querySelector('p:nth-of-type(2)').textContent;
    var coordParts = miscCoord.split(' ');
    return coordParts.join('');
  }
});
