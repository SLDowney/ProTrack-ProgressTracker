window.addEventListener('DOMContentLoaded', function() {
  
  var coliseumsTable = document.getElementById('location_table');
  
  // Add the event listener to the checkboxes to update the counter when checkboxes are clicked
  Array.from(coliseumsTable.querySelectorAll('input[type="checkbox"]')).forEach(function(checkbox) {
    checkbox.addEventListener('click', function() {
    });
  });

});
var coliseumsTable = document.getElementById('location_table');

function updatecoliseum(checkbox, coliseumId) {
  const coliseumFound = checkbox.checked ? 1 : 0;

  const data = {
      coli_id: coliseumId,
      coli_done: coliseumFound,
  };

  console.log('Data sent to server:', data); // Add this line for debugging

  fetch('/update-coliseum', {
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
  
};
