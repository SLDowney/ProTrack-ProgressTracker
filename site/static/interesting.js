window.addEventListener('DOMContentLoaded', function() {
  var sortByLocationBtn = document.getElementById("sort-by-location-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var sortByTypeBtn = document.getElementById("sort-by-type-btn");
  var interestingTable = document.getElementById('items-table');

  var isLocationSortAscending = true;
  var isCoordSortAscending = true;
  var isTypeSortAscending = true;
  var isStartSortAscending = true;
  var isFoundSortAscending = true;

  sortByLocationBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortinteresting('location');
    isLocationSortAscending = !isLocationSortAscending;
  });

  sortByCoordBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortinteresting('coord');
    isCoordSortAscending = !isCoordSortAscending;
  });

  sortByTypeBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortinteresting('type');
    isTypeSortAscending = !isTypeSortAscending;
  });

  function sortinteresting(sortType) {
    var interesting = Array.from(interestingTable.getElementsByTagName('tr'));
    interesting.shift(); // Remove header row from sorting

    interesting.sort(function(a, b) {
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

    var tbody = interestingTable.querySelector('tbody');
    interesting.forEach(function(thing) {
      tbody.appendChild(thing);
    });
  }

  function extractCoord(thingRow) {
    var coordCell = thingRow.cells[4];
    if (coordCell) {
      var coordParts = coordCell.textContent.split(', ');
      return coordParts.join('');
    }
    return '';
  }

  function updateitem(itemId, checked) {
    fetch('/update_thing', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        thingId: itemId,     // Assuming the 'thing[0]' contains the itemId
        thingFound: checked, // Assuming 'checked' is the updated found status
      }),
    })
      .then(function(response) {
        // Handle the response from the server if needed
      })
      .catch(function(error) {
        console.error('Error updating thing:', error);
      });
  }
  

  // Add event listener to checkboxes
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function(event) {
      var itemId = checkbox.getAttribute('data-id');
      var checked = checkbox.checked;
      updateitem(itemId, checked);
    });
  });
});
