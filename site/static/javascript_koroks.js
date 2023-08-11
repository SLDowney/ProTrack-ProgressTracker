var koroksTable = document.getElementById('koroks-table');

function updateKorok(checkbox, korokId) {
  const korokFound = checkbox.checked ? 1 : 0;

  const data = {
      korok_id: korokId,
      korok_done: korokFound,
  };

  console.log('Data sent to server:', data); // Add this line for debugging

  fetch('/update-korok', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
      // Handle the response if needed
      console.log('Response from server:', data); // Add this line for debugging
  })
  .catch(error => {
      console.error('Error:', error);
  });
}
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
    } else if (sortType === 'korok_done') {
      aValue = a.cells[0].querySelector('input[type="checkbox"]').checked;
      bValue = b.cells[0].querySelector('input[type="checkbox"]').checked;
    }

    if (aValue && bValue) {
      if (aValue < bValue) {
        return sortType === 'korok_done' ? (isFoundSortAscending ? -1 : 1) : -1;
      } else if (aValue > bValue) {
        return sortType === 'korok_done' ? (isFoundSortAscending ? 1 : -1) : 1;
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

window.addEventListener('DOMContentLoaded', function() {
  var sortByLocationBtn = document.getElementById("sort-by-location-btn");
  var sortByCoordBtn = document.getElementById("sort-by-coord-btn");
  var sortByTypeBtn = document.getElementById("sort-by-type-btn");
  var sortByFoundBtn = document.getElementById("sort-by-found-btn");
  var koroksTable = document.getElementById('koroks-table');

  var isLocationSortAscending = true;
  var isCoordSortAscending = true;
  var isTypeSortAscending = true;
  var isStartSortAscending = true;
  var isFoundSortAscending = true;

  
    


  function updatePercentageCounter() {
    var totalKoroks = koroksTable.getElementsByTagName('tr').length - 1; // Exclude the header row
    var totalFoundKoroks = Array.from(koroksTable.querySelectorAll('input[type="checkbox"]')).reduce(function(total, checkbox) {
        return total + (checkbox.checked ? 1 : 0);
    }, 0);
  
    var percentageFound = (totalFoundKoroks / totalKoroks) * 100;
    document.getElementById('percentage-found').textContent = percentageFound.toFixed(2);
  }
  
  // Call the function on page load
  updatePercentageCounter();
  
  // Add the event listener to the checkboxes to update the counter when checkboxes are clicked
  Array.from(koroksTable.querySelectorAll('input[type="checkbox"]')).forEach(function(checkbox) {
    checkbox.addEventListener('click', function() {
        updatePercentageCounter();
    });
  });
  
  
  function extractCoord(korokRow) {
    var coordCell = korokRow.cells[4];
    if (coordCell) {
      var coordParts = coordCell.textContent.split(', ');
      return coordParts.join('');
    }
    return '';
  }
  
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

  sortByFoundBtn.addEventListener("click", function(event) {
    event.preventDefault();
    sortKoroks('found');
    isFoundSortAscending = !isFoundSortAscending;
});

 
});
