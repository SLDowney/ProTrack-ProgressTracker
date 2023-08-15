let progressBars = {}; // Declare an object to store progress bars by temple ID

// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Retrieve the progress bars from the DOM and store them in the object
  const progressElements = document.querySelectorAll(".progress");
  progressElements.forEach((progressElement) => {
    const templeId = progressElement.dataset.templeId;
    const templeName = progressElement.dataset.templeName;
    progressBars[templeId] = progressElement.querySelector(".progress-bar");
    console.log("Temple ID ->", templeId)
  });

  // Add event listener to the entire form to handle checkbox clicks
  document.querySelector("form").addEventListener("change", (event) => {
    const target = event.target;
    if (target.classList.contains("temple-boss-checkbox")) {
      updateTempleBossStatus(target);
    } else if (
      target.classList.contains("_locks")
    ) {
      updateLockStatus(target);
    }
  });
});

// Function to update the lock status in the database
function updateLockStatus(checkbox) {
  const templeId = checkbox.dataset.templeId;
  const isLock = checkbox.getAttribute("name").endsWith("_locks"); // Determine if it's a lock checkbox
  const lockIndex = parseInt(checkbox.value); // Extract lock number from checkbox value
  const value = checkbox.checked ? 1 : 0;

  // Create the JSON data for the request
  const data = {
    temple_id: templeId,
    is_lock: isLock,
    lock_index: lockIndex, // Include the lock number in the JSON data
    value: lockIndex
  };

  // Send the request to update the lock status or temple boss
  fetch("/update_lock_status", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.success) {
      // Update the progress bar in the DOM immediately 
      if (templeId == 1 || templeId == 3) {
        progress_percentage = lockIndex * 20
      }
      else {
        progress_percentage = lockIndex * 25
      }
		const progressBarId = templeId; // Replace with the ID you want to target
        console.log("progressBarID ->", progressBarId)
        let progressBars = document.getElementById(progressBarId);
		console.log("progressBars ->", progressBars)
		progressBars.style.width = `${progress_percentage}%`;
		console.log("Progress Percentage ->", progress_percentage)

      // Update temple boss checkmark visibility
      const templeBossCheckmark = document.getElementById("temple-boss-checkmark");
      if (templeBossCheckmark) {
        templeBossCheckmark.addEventListener("change", () => {
          updateTempleBossStatus(templeBossCheckmark);
        });
      }
    } else {
      console.error("Error updating lock status:", data.error);
    }
  })
  .catch((error) => {
    console.error("Error updating lock status:", error);
  });
}


// Function to update the temple boss status in the database
function updateTempleBossStatus(checkbox) {
  let templeId = checkbox.dataset.templeId;
  const isBoss = true; // Since this function is for the boss checkbox
  const value = checkbox.checked ? 1 : 0;

  // Create the JSON data for the request
  const data = {
    temple_id: templeId,
    is_lock: !isBoss, // Invert isBoss for lock status
    lock_index: null, // No lock index for boss checkbox
    value: value,
    temple_boss: value, // Use the checkbox value for temple boss status
  };

  // Send the request to update the boss status
  fetch("/update_lock_status", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.success) {
      // Update the progress bar in the DOM after successful update
      if (data.success) {
        if (templeId == 1 || templeId == 3) {
          progress_percentage = value * 100
          console.log("progress bar IF Value ->", value)
        }
        else {
          progress_percentage = value * 100
          console.log("progress bar ELSE Value ->", value)
        }
        const progressBarId = templeId; // Replace with the ID you want to target
        console.log("progressBarID ->", progressBarId)
        let progressBars = document.getElementById(progressBarId);
        console.log("progressBars ->", progressBars)
        // Calculate the color based on progress_percentage
        const color = progress_percentage >= 100 ? "green" : "blue"; // Change color thresholds as needed

        // Set the background color of the progress bar
        progressBars.style.backgroundColor = color;

        console.log("progressBars.style.backgroundColor ->", color)
      }
      // Update temple boss checkmark visibility
      const templeBossCheckmark = document.querySelector("temple-boss-checkmark");
      if (templeBossCheckmark) {
        templeBossCheckmark.style.display = value === 1 ? "inline" : "none";
      }
     else {
      console.error("Error updating boss status:", data.error);
      }
  }})
  .catch((error) => {
    console.error("Error updating boss status:", error);
  });
}
