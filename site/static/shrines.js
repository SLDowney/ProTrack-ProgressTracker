// shrines.js

// Function to handle form submission and filtering by region
function filterByRegion() {
  var selectedRegion = document.getElementById('regionFilter').value;
  var shrineForm = document.getElementById('shrineform');
  shrineForm.action = "/shrines"; // Use the relative URL
  if (selectedRegion) {
      shrineForm.action += "?region=" + encodeURIComponent(selectedRegion); // Include the region query parameter
  }
  shrineForm.submit();
  return false;
}

// Add a listener for the form submission
document.getElementById('regionFilterForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the default form submission behavior
  filterByRegion(); // Call the filterByRegion() function to handle the form submission
});

// ... (your existing JavaScript code)
