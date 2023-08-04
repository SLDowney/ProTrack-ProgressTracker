let progressBars;

// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  progressBars = document.querySelectorAll(".progress-bar");

  // ... (rest of the code)

  // Add event listeners to the radio buttons for each lock
  progressBars.forEach((progressBar) => {
    const notDoneRadio = document.getElementById(
      `${progressBar.dataset.templeName}_lock_${progressBar.dataset.lockIndex}_not_done`
    );
    const doneRadio = document.getElementById(
      `${progressBar.dataset.templeName}_lock_${progressBar.dataset.lockIndex}_done`
    );

    notDoneRadio.addEventListener("change", () => {
      updateLockStatus(notDoneRadio);
    });

    doneRadio.addEventListener("change", () => {
      updateLockStatus(doneRadio);
    });
  });
});


// Function to update the lock status in the database
function updateLockStatus(radio) {
  const progressBars = document.querySelectorAll(".progress-bar");
  const templeId = radio.dataset.templeId;
  const lockIndex = parseInt(radio.value);
  const status = radio.checked ? 1 : 0;

  // Create the JSON data for the request
  const data = {
    temple_id: templeId,
    lock_index: lockIndex,
    status: status,
  };

  // Send the request to update the lock status
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
        // Update the progress bar in the DOM after successful update in the database
        const progressBar = progressBars[templeId * 5 + lockIndex - 1]; // Adjusted index calculation
        progressBar.style.width = `${status * 20}%`;
        progressBar.textContent = `Lock ${lockIndex}: ${status * 20}%`;
      } else {
        console.error("Error updating lock status:", data.error);
        console.log("lock index:", lockIndex);
      }
    })
    .catch((error) => {
      console.error("Error updating lock status:", error);
    });
}
