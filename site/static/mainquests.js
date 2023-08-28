window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  var mainTable = document.getElementById('mainquform');
  checks = document.getElementsByClassName('main_checkbox');
  updateAllMainsVisible();
  //// console.log("checks ->", checks);
  // let unchecked_checkboxes = []
  // let tulin = []
  // let riju = []
  // let sidon = []
  // let yunobo = []
  // let spirit = []
  
  // for (var i = 0; i < checks.length; i++) {
  //   var checkbox = checks[i];
  //   if (checkbox.classList.contains('main_check_10')) {
  //     riju.push(checkbox)
  //   }
  //   else if (checkbox.classList.contains('main_check_11')) {
  //     yunobo.push(checkbox)
  //   }
  //   else if (checkbox.classList.contains('main_check_13')) {
  //     sidon.push(checkbox)
  //   }
  //   else if (checkbox.classList.contains('main_check_18')) {
  //     spirit.push(checkbox)
  //   }
  //   else if (checkbox.classList.contains('main_check_8')) {
  //     tulin.push(checkbox)
  //   }
  // }
  // // console.log("RIJU ->", riju)
  // // console.log("SIDON ->", sidon)
  // // console.log("TULIN ->", tulin)
  // // console.log("YUNOBO ->", yunobo)
  // // console.log("SPIRIT ->", spirit)
  // for ( var x = 0; x < riju.length; x++) {
  //   let parentRow = x.parentNode.parentNode
  //   parentRow.classList.add('hidden_display'); // Add your class name here
  //   //// console.log("RIJU PARENT ->", parentRow)
  // }
  // for ( var x = 1; x < sidon.length; x++) {
  //   let parentRow = x.parentNode.parentNode
  //   parentRow.classList.add('hidden_display'); // Add your class name here
  //   //// console.log("SIDON PARENT ->", parentRow)
  // }
  // for ( var x = 1; x < tulin.length; x++) {
  //   let parentRow = checkbox.parentNode.parentNode
  //   parentRow.classList.add('hidden_display'); // Add your class name here
  //   //// console.log("TULIN PARENT ->", parentRow)
  // }
  // for ( var x = 1; x < yunobo.length; x++) {
  //   let parentRow = x.parentNode.parentNode
  //   parentRow.classList.add('hidden_display'); // Add your class name here
  //   //// console.log("YUNOBO PARENT ->", parentRow)
  // }
  // for ( var x = 1; x < spirit.length; x++) {
  //   let parentRow = x.parentNode.parentNode
  //   parentRow.classList.add('hidden_display'); // Add your class name here
  //   //// console.log("SPIRIT PARENT ->", parentRow)
  // }

  // Add the event listener to the radios to update the counter and Rewards column
  Array.from(mainTable.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
    radio.addEventListener('click', function () {

        // Update Rewards cell when radio is clicked
        const mainId = radio.name.replace('done_', ''); // Extract main ID
      
        updatemain(radio, mainId); // Pass mainReward to updatemain function
        
    });
    // Add the event listener to the checkboxes to update the counter and Rewards column
  Array.from(mainTable.querySelectorAll('input[type="checkbox"]')).forEach(function (checkbox) {
    const secondaryLevel = checkbox.id.replace('level_', '');
    
    checkbox.addEventListener('click', function () {

        // Update Rewards cell when radio is clicked
        const secondaryId = checkbox.name.replace('secondary_', ''); // Extract main ID
        const secondaryLevel = checkbox.id.replace('level_', '');
        showSecondary(checkbox, secondaryLevel)
        updatesecondary(checkbox, secondaryId); 
    });
});
})
  });

var mainTable = document.getElementById('mainquform');

function updatesecondary(checkbox, secondaryId) {
  //console.log("--------UPDATE secondary ---------")
  const secondaryFound = checkbox.checked ? 1 : 0;
  //// console.log("SecondaryFound ->", secondaryFound)

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
      //console.error('Error:', error);
    });

  const secondaryLevel = checkbox.id.replace('level_', '');
  showSecondary(checkbox, secondaryLevel)
}

function updatemain(radio, mainId) {
    console.log("--------UPDATE main ---------")
  const mainFound = radio.value;
  let questShow;
  if (mainFound == 0) {
    questShow = 0
  }
  else if (mainFound != 0) {
    questShow = 1
  }
  //// console.log("MainFound ->", mainFound)

  const data = {
    main_id: parseInt(mainId),
    main_done: parseInt(mainFound),
    quest_show: parseInt(questShow)
  };
  //// console.log("DATA ->", data)

  if (mainFound == 2) {
    fetch('/main_update', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        main_id: mainId,  // Pass the variable to the server.
        quest_show: parseInt(questShow)
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
      //console.error('Error:', error);
    });
}
  
function checkCheckboxLevels(checkbox) {
  const secondaryId = checkbox.name.replace('secondary_', '');
  Subquests = document.getElementsByClassName(".subquest_" + secondaryId);
  //Subquests = Subs.getElementsByClassName(".subquest_" + secondaryId);
  
  console.log("Subquests ->", Subquests)
  let allDone = true;
  
  for ( let x = 0; x < Subquests.length; x++) {
    if (Subquests[x].checked) {
      allDone = true;
      console.log("allDone true ->", allDone)
      console.log("Subquests[x] ->", Subquests[x])
    }
    else {
      allDone = false;
      console.log("allDone false ->", allDone)
      console.log("Subquests[x] ->", Subquests[x])
      break;
    }
  }

  return allDone;
}

let ItemSecond = document.getElementsByClassName("subquest_2");
let ItemThird = document.getElementsByClassName("subquest_3");
let ItemFourth = document.getElementsByClassName("subquest_4");

function showSecondary(checkbox, secondaryLevel) {
  //console.log("--------UPDATE showSecondary ---------")
  //// console.log("CHECKBOX ->", checkbox)
  //// console.log("Item Second ->", ItemSecond)
  const secondaryId = checkbox.name.replace('secondary_', '');
  const secondaryFound = checkbox.checked ? 1 : 0;

  const classNames = checkbox.className.split(" "); // Split class names by space
  let mainId;
  for (const className of classNames) {
      if (className.startsWith("id_")) {
        mainId = parseInt(className.substr(3)); // Extract the ID part and convert it to an integer
        //updateMainVisible(mainId)  
        break;
      }
  }
  //console.log("CHECKBOX ->", checkbox)

  try {
    console.log("In Try Statement")
    if (checkbox.checked & secondaryLevel == 1) {
      console.log("In IF STATEMENT")
      if (checkCheckboxLevels(checkbox, secondaryLevel)) {
        console.log("SECOND IF STATEMENT")
        for (const item of ItemSecond) {
          item.classList.remove("hidden_display")
        }
      }else {
        for (const item of ItemSecond) {
          item.classList.add("hidden_display")
        }
      }
    } else if (!checkbox.checked & secondaryLevel == 1) {
      console.log("IN ELSE IF STATEMENT")
      for (const item of ItemSecond) {
        item.classList.add("hidden_display")
      }
    }
    if (checkbox.checked & secondaryLevel == 2) {
      if (checkCheckboxLevels(checkbox, secondaryLevel)) {
        for (const item of ItemThird) {
          item.classList.remove("hidden_display")
        }
      }else {
        for (const item of ItemThird) {
          item.classList.add("hidden_display")
        }
      }
    } else if (!checkbox.checked & secondaryLevel == 2) {
      for (const item of ItemThird) {
        item.classList.add("hidden_display")
      }
    }
    if (checkbox.checked & secondaryLevel == 3) {
      if (checkCheckboxLevels(checkbox, secondaryLevel)) {
        for (const item of ItemFourth) {
          item.classList.remove("hidden_display")
        }
      }else {
        for (const item of ItemFourth) {
          item.classList.add("hidden_display")
        }
      }
    } else if (!checkbox.checked & secondaryLevel == 3) {
      for (const item of ItemFourth) {
        item.classList.add("hidden_display")
      }
    }
    
    const data = {
      secondary_id: parseInt(secondaryId),
      secondary_done: parseInt(secondaryFound),
      main_id: parseInt(mainId)
    };
    // console.log("DATA ->", data)
  

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
      //// console.log('Response from server:', data);

    })
    .catch(error => {
      // console.error('Error:', error);
    });

  } catch (error) {
    // console.error("An error occurred, probably NULL:", error);
}
  
}

function updateMainVisible(mainId) {
  console.log("Main id->>", mainId)
  currentMain = document.getElementById('quest_' + mainId).nextElementSibling
  console.log("CURRENT MAIN ->", currentMain)
  currentMain.classList.remove("hidden_display")
}

function updateAllMainsVisible() {
  allMains = document.getElementsByClassName('questShow_' + 0)
  for ( let x = 0; x < allMains.length; x++) {
    allMains[x].classList.add("hidden_display")
  }
}