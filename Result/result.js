// Load the result on loading
window.onload = loadData();

function loadData(){
    // Load the team names from local data
    var result = localStorage.getItem("Result");
    console.log(result);
    // Put value onto result page
    var msg = document.getElementById('msg');
    msg.innerHTML = '<br><br><br><br><b>' + result + '<b>';
}