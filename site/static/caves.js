// caves.js

// Function to handle form submission and filtering by region
function filterByRegion() {
  var selectedRegion = document.getElementById('regionFilter').value;
  var caveForm = document.getElementById('caveform');
  caveForm.action = "/caves"; // Use the relative URL
  if (selectedRegion) {
      caveForm.action += "?region=" + encodeURIComponent(selectedRegion); // Include the region query parameter
  }
  caveForm.submit();
  return false;
}

// Add a listener for the form submission
document.getElementById('regionFilterForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the default form submission behavior
  filterByRegion(); // Call the filterByRegion() function to handle the form submission
});

// ... (your existing JavaScript code)
