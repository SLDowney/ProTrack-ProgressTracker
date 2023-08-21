window.addEventListener('DOMContentLoaded', function() {
  
  var schemasTable = document.getElementById('schemas-table');
  
  // Add the event listener to the checkboxes to update the counter when checkboxes are clicked
  Array.from(schemasTable.querySelectorAll('input[type="checkbox"]')).forEach(function(checkbox) {
    checkbox.addEventListener('click', function() {
    });
  });
  
});
var schemasTable = document.getElementById('schemas-table');

function updateschema(checkbox, schemaId) {
  const schemaFound = checkbox.checked ? 1 : 0;

  const data = {
      schema_id: schemaId,
      schema_done: schemaFound,
  };

  console.log('Data sent to server:', data); // Add this line for debugging

  fetch('/update_schema', {
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
