import flask
from flask import request, jsonify
from webscrape_example import get_team_stats

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Values of team with names to pass to scraper function in correct format
teams = {
    'Arizona Cardinals': 'Arizona',
    'Atlanta Falcons': 'Atlanta',
    'Buffalo Bills': 'Buffalo',
    'Baltimore Ravens': 'Baltimore',
     'Carolina Panthers': 'Carolina',
     'Cincinnati Bengals': 'Cincinnati',
     'Cleveland Browns': 'Cleveland',
     'Chicago Bears': 'Chicago',
     'Dallas Cowboys': 'Dallas',
     'Denver Broncos': 'Denver',
     'Detroit Lions': 'Detroit',
     'Green Bay Packers': 'Green Bay',
     'Houston Texans': 'Houston',
     'Indianapolis Colts': 'Indianapolis',
     'Kansas City Chiefs': 'Kansas City',
     'Los Angeles Chargers' : 'Los Angeles Chargers',
     'Los Angeles Rams': 'Los Angeles Rams',
     'Jacksonville Jaguars': 'Jacksonville',
     'Miami Dolphins': 'Miami',
     'Minnesota Vikings': 'Minnesota',
     'New England Patrios': 'New England',
     'New Orleans Saints': 'New Orleans',
     'New York Giants': 'New York Giants',
     'New York Jets': 'New York Jets',
     'Las Vegas Raiders': 'Las Vegas',
     'Philadelphia Eagles': 'Philadelphia',
     'San Fransisco 49ers': 'San Fransisco',
     'Seattle Seahawks': 'Seattle',
     'Pittsburgh Steelers': 'Pittsburgh',
     'Tampa Bay Buccaneers': 'Tampa Bay',
     'Tennessee Titans': 'Tennessee',
     'Washington Football Team': 'Washington'
}

# A route to return the predicted winner of both teams given
@app.route('/api/v1/winner', methods=['GET'])
def api_all():
    # Get both parameters given
    team1 = request.args['team1']
    team2 = request.args['team2']

    # Convert the team name into the correct format above
    team1 = teams[team1]
    team2 = teams[team2]

    # Call the web scraper function and return stats for selected team
    result = get_team_stats(team1, team2)

    # Convert into a json object after getting correct key again
    result = list(teams.keys())[list(teams.values()).index(result)]
    winner = {'result': result}

    # Return as a json package
    return jsonify(winner)

app.run()