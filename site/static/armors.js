document.addEventListener("DOMContentLoaded", function () {
  const armorForm = document.getElementById("armorForm");

  armorForm.addEventListener("change", (event) => {
    const target = event.target;

    if (target.classList.contains("armor_set") || target.classList.contains("collected-checkbox")) {
      const armorId = target.id.replace("armor_id_", "");
      const armorValue = target.checked ? "1" : "0";

      // Send the request to update armor collected status
      fetch(`/update_armor/${armorId}/${armorValue}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          console.log(`Armor ${armorId} collected status updated: ${armorValue}`);
          const armorSet = target.closest(".armor_set");
          updateUpgradesDisplay(armorSet);
        } else {
          console.error("Error updating armor collected status:", data.error);
        }
      })
      .catch((error) => {
        console.error("Error updating armor collected status:", error);
      });
    }
  
  // Hide all upgrade divs on page load
  const upgradeDivs = document.querySelectorAll(".armor_set_piece_upgrade");
  upgradeDivs.forEach(function (upgrade) {
    upgrade.style.display = "none";
  });

  // Trigger initial update for each armor set
  const armorSets = document.querySelectorAll(".armor_set");
  // armorSets.forEach(function (armorSet) {
  //   updateUpgradesDisplay(armorSet);
  // });

  });
});

  // function updateUpgradesDisplay(armorSet) {
  //   const greatFairyCheckboxes = armorSet.querySelectorAll(".great-fairy-checkboxes");
  //   const collectedCheckbox = armorSet.querySelector(".collected-checkbox");
  //   if (!collectedCheckbox) {
  //     return; // Exit if the collected-checkbox cannot be found
  //   }

  //   const upgrades = armorSet.querySelectorAll(".armor_set_piece_upgrade");

  //   const numGreatFairies = Array.from(greatFairyCheckboxes).filter((checkbox) => checkbox.checked).length;
  //   const level1Checkbox = armorSet.querySelector(".level1-checkbox");
  //   const level2Checkbox = armorSet.querySelector(".level2-checkbox");
  //   const level3Checkbox = armorSet.querySelector(".level3-checkbox");
  //   const level4Checkbox = armorSet.querySelector(".level4-checkbox");

  //   upgrades.forEach(function (upgrade) {
  //     upgrade.style.display = "none";
  //   });

  //   if (numGreatFairies >= 1 && collectedCheckbox.checked) {
  //     armorSet.querySelector(".armor_set_piece_upgrade1").style.display = "table-row-group";
  //   }

  //   if (numGreatFairies >= 2 && level1Checkbox && level1Checkbox.checked) {
  //     armorSet.querySelector(".armor_set_piece_upgrade2").style.display = "table-row-group";
  //   }

  //   if (numGreatFairies >= 3 && level2Checkbox && level2Checkbox.checked) {
  //     armorSet.querySelector(".armor_set_piece_upgrade3").style.display = "table-row-group";
  //   }

  //   if (numGreatFairies >= 4 && level3Checkbox && level3Checkbox.checked) {
  //     armorSet.querySelector(".armor_set_piece_upgrade4").style.display = "table-row-group";
  //   }
  // }

