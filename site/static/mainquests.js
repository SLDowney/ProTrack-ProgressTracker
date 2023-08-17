window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var mainTable = document.getElementById('mainquform');
  checks = document.getElementsByClassName('main_checkbox');
  console.log("checks ->", checks);
  let unchecked_checkboxes = []
  let tulin = []
  let riju = []
  let sidon = []
  let yunobo = []
  let spirit = []
  
  for (var i = 0; i < checks.length; i++) {
    var checkbox = checks[i];
    if (checkbox.classList.contains('main_check_10')) {
      riju.push(checkbox)
    }
    else if (checkbox.classList.contains('main_check_11')) {
      yunobo.push(checkbox)
    }
    else if (checkbox.classList.contains('main_check_13')) {
      sidon.push(checkbox)
    }
    else if (checkbox.classList.contains('main_check_18')) {
      spirit.push(checkbox)
    }
    else if (checkbox.classList.contains('main_check_8')) {
      tulin.push(checkbox)
    }
  }
  console.log("RIJU ->", riju)
  console.log("SIDON ->", sidon)
  console.log("TULIN ->", tulin)
  console.log("YUNOBO ->", yunobo)
  console.log("SPIRIT ->", spirit)
  for ( var x = 0; x < riju.length; x++) {
    let parentRow = x.parentNode.parentNode
    parentRow.classList.add('hidden_display'); // Add your class name here
    console.log("RIJU PARENT ->", parentRow)
  }
  for ( var x = 1; x < sidon.length; x++) {
    let parentRow = x.parentNode.parentNode
    parentRow.classList.add('hidden_display'); // Add your class name here
    console.log("SIDON PARENT ->", parentRow)
  }
  for ( var x = 1; x < tulin.length; x++) {
    let parentRow = checkbox.parentNode.parentNode
    parentRow.classList.add('hidden_display'); // Add your class name here
    console.log("TULIN PARENT ->", parentRow)
  }
  for ( var x = 1; x < yunobo.length; x++) {
    let parentRow = x.parentNode.parentNode
    parentRow.classList.add('hidden_display'); // Add your class name here
    console.log("YUNOBO PARENT ->", parentRow)
  }
  for ( var x = 1; x < spirit.length; x++) {
    let parentRow = x.parentNode.parentNode
    parentRow.classList.add('hidden_display'); // Add your class name here
    console.log("SPIRIT PARENT ->", parentRow)
  }

  // Add the event listener to the radios to update the counter and Rewards column
  Array.from(mainTable.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('click', function () {

        // Update Rewards cell when radio is clicked
        const mainId = radio.name.replace('done_', ''); // Extract main ID
      
        updatemain(radio, mainId); // Pass mainReward to updatemain function
    });
    // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(mainTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when radio is clicked
        const secondaryId = checkbox.name.replace('secondary_', ''); // Extract main ID
      
        updatesecondary(checkbox, secondaryId); 
        updateMainFromSecondary(checkbox, secondaryId)
    });
});
})
  });

var mainTable = document.getElementById('mainquform');

function updatesecondary(checkbox, secondaryId) {
  console.log("--------UPDATE main ---------")
  const secondaryFound = checkbox.checked ? 1 : 0;
  //console.log("SecondaryFound ->", secondaryFound)

  const data = {
    secondary_id: parseInt(secondaryId),
    secondary_done: parseInt(secondaryFound),
  };
  //console.log("DATA ->", data)

  fetch('/update_secondary', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response if needed
      //console.log('Response from server:', data);

    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function updatemain(radio, mainId) {
    console.log("--------UPDATE main ---------")
  const mainFound = radio.value;
  //console.log("MainFound ->", mainFound)

  const data = {
    main_id: parseInt(mainId),
    main_done: parseInt(mainFound),
  };
  //console.log("DATA ->", data)

  if (mainFound == 2) {
    fetch('/main_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        main_id: mainId  // Pass the variable to the server
      })
    })
  }

  fetch('/update_mainquests', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response if needed
      //console.log('Response from server:', data);

    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function updateMainFromSecondary(checkbox, secondaryId) {
  console.log("--------UPDATE updateMainFromSecondary ---------")
  const secondaryFound = checkbox.checked ? 1 : 0;
  console.log("SecondFound ->", secondaryFound)

  const data = {
    secondary_id: parseInt(secondaryId),
    secondary_done: parseInt(secondaryFound),
  };
  console.log("DATA ->", data)
  secondaryItemElement = document.getElementById("secondary_item_" + secondaryId).nextElementSibling;

  if (checkbox.checked) {
    secondaryItemElement.classList.remove("hidden_display");
  } else {
    secondaryItemElement.classList.add("hidden_display");
  }

}
