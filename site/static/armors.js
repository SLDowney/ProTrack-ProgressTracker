window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
        armorInfoToggle()
});

function armorInfoToggle() {
    let armorTable = document.getElementById('armor-table');
    Array.from(armorTable.getElementsByClassName('armors')).forEach(function (item) {
        console.log("Armors item ->", item);
        console.log("Armors item.getAttribute('value') ->", item.getAttribute('value'));
        console.log("Armors item.getAttribute('name') ->", item.getAttribute('name'));
        let armorId = item.getAttribute('name').replace('acollected_', ''); // Extract armor ID;
        console.log("armor ID ->", armorId)
        var armorIdElements = document.querySelectorAll(".armor_" + armorId);
    
        armorIdElements.forEach(function (element) {
            console.log("Element ->", element)
            if (element.textContent == "None") {
                element.textContent = "GET INFO"
            }
        if (element.getAttribute('value') == 4) {
            if (element.id == "armor_name"
            || element.id == "armor_picture"
            || element.id == "armor_get"
            || element.id == "armor_price"
            || element.id == "armor_price1"
            || element.id == "armor_price2"
            || element.id == "armor_price3"
            || element.id == "armor_price4"
            || element.id == "armor_stat"
            || element.id == "armor_stat1"
            || element.id == "armor_stat2"
            || element.id == "armor_stat3"
            || element.id == "armor_stat4") {
            element.classList.remove("hidden_display");
            } else {
                element.classList.remove("hidden_display"); // Hide info
                element.textContent = "???";
            }
        }
        else if (element.getAttribute('value') == 3) {
    
            if (element.id == "armor_name"
            || element.id == "armor_picture"
            || element.id == "armor_get"
            || element.id == "armor_price"
            || element.id == "armor_price1"
            || element.id == "armor_price2"
            || element.id == "armor_price3"
            || element.id == "armor_stat"
            || element.id == "armor_stat1"
            || element.id == "armor_stat2"
            || element.id == "armor_stat3") {
            element.classList.remove("hidden_display");
            } else {
                element.classList.remove("hidden_display");
                element.textContent = "???";
            }
    
        }
        else if (element.getAttribute('value') == 2) {
    
            if (element.id == "armor_name"
            || element.id == "armor_picture"
            || element.id == "armor_get"
            || element.id == "armor_price"
            || element.id == "armor_price1"
            || element.id == "armor_price2"
            || element.id == "armor_stat"
            || element.id == "armor_stat1"
            || element.id == "armor_stat2") {
            element.classList.remove("hidden_display");
            } else {
                element.classList.remove("hidden_display");
                element.textContent = "???";
            }
    
        }
        else if (element.getAttribute('value') == 1) {
    
            if (element.id == "armor_name"
            || element.id == "armor_picture"
            || element.id == "armor_get"
            || element.id == "armor_price"
            || element.id == "armor_price1"
            || element.id == "armor_stat"
            || element.id == "armor_stat1") {
            element.classList.remove("hidden_display");
            } else {
                element.classList.remove("hidden_display");
                element.textContent = "???";
            }
    
        }
        else if (element.getAttribute('value') == 0) {
            //console.log("Element Zero ->", element)
        }
        else {
            //console.log("Element Else ->", element)
        }
    });
   })
}