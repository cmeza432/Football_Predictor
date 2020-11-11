# Football_Predictor

App for predicting winner of two NFL teams given by user

## How it works

### HTML, CSS, JS

This webapp is created in HTML, CSS and JS. User will select two NFL teams from GUI. Once both items are selected, a JS file will then use AJAX to send a GET request using both teams selected as part of the url header. This will be sent to the custom API created by me in Python and get a JSON body for the selected winner of both teams. Once the winner is selected it will then redirect to another page with answer.

### Python

The Python file is an API created in Flask. It will receive a GET request with two teams selected by the user. It will then call a webscraper created to extract values of current team turnover differentials(More calculations to determing winner will come soon) and select team with higher value. It will then create a JSON object and send it as a response to the request made in JS.

## How to run

First run the python server file in the api folder by typing the following command
`python server.py`
Then navigate to the Index folder and run or double click the `index.html` file. After that just select teams and enjoy!!
