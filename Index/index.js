var teams = [
    {"name": "Arizona Cardinals"},
    {"name": "Atlanta Falcons"},
    {"name": "Buffalo Bills"},
    {"name": " Baltimore Ravens"},
    {"name": "Carolina Panthers"},
    {"name": " Cincinnati Bengals"},
    {"name": "Cleveland Browns"},
    {"name": "Chicago Bears"},
    {"name": "Dallas Cowboys"},
    {"name": "Denver Broncos"},
    {"name": "Detroit Lions"},
    {"name": "Green Bay Packers"},
    {"name": "Houston Texans"},
    {"name": "Indianapolis Colts"},
    {"name": "Kansas City Chiefs"},
    {"name": "Los Angeles Chargers"},
    {"name": "Los Angeles Rams"},
    {"name": "Jacksonville Jaguars"},
    {"name": "Miami Dolphins"},
    {"name": "Minnesota Vikings"},
    {"name": "New England Patrios"},
    {"name": "New Orleans Saints"},
    {"name": "New York Giants"},
    {"name": "New York Jets"},
    {"name": "Las Vegas Raiders"},
    {"name": "Philadelphia Eagles"},
    {"name": "San Fransisco 49ers"},
    {"name": "Seattle Seahawks"},
    {"name": "Pittsburgh Steelers"},
    {"name": "Tampa Bay Buccaneers"},
    {"name": "Tennessee Titans"},
    {"name": "Washington Football Team"}
]

// Load this file as soon as webpage opens
window.onload = show();

// Function used to populate drop down box values
function populate(element) {
    for(var i = 0; i < teams.length; i++) {
        element.innerHTML = element.innerHTML + 
        '<option>' + 
        teams[i]['name'] + '</option>';
    }
    return element;
}

// Function controls the showing of values in drop down box
function show() {
    // Populate select element
    var element1 = document.getElementById('firstT');
    var element2 = document.getElementById('secondT');
    element1 = populate(element1);
    element2 = populate(element2);
}

// Function to upade the web page once value is submitted
function changePage(result){
    // Get the document id to replace with answer 
    var msg = document.getElementById('drp');
    var head = document.getElementById('header');
    var button = document.getElementById('btn');

    // Replace the document ID with result message
    head.parentNode.removeChild(head);
    button.parentNode.removeChild(button);
    msg.innerHTML = '<p1 style="font-size: 45px;" id="header">Result:</p1><br><br>'
     + '<p2 style="color: red;">' + result + '</p2>'
     + '<br><br><button class="submit" onclick="history.go(0);">Try Again</button>';
}

// Function will use AJAX to use a Get Request
function getWinner(team1, team2) {
    // Send info to python API url 
    // Example: http://127.0.0.1:5000/api/v1/winner?team1=Dallas_Cowboys&team2=Atlanta_Falcons
    const Http = new XMLHttpRequest();
    const url = "http://127.0.0.1:5000/api/v1/winner?team1=" + team1 + "&team2=" + team2;
    Http.onreadystatechange=function(){
        if (Http.readyState==4 && Http.status==200){
          var obj = JSON.parse(Http.responseText);
          changePage(obj.result);
        }
    }
    Http.open("GET", url);
    Http.send();
}

function getTeam() {
    // Get the selected value from firstT and secondT element to show
    var team1 = document.getElementById('firstT').value;
    var team2 = document.getElementById('secondT').value;
    
    // Check if same teams given
    // Check if either team is empty
    if(team1 == "" || team2 == ""){
        changePage("Error, not enough teams given!");
    }
    else if(team1 == team2){
        changePage(team1);
    }
    else {
        // Call the API to get result of team
        getWinner(team1, team2);
    }
}