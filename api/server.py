import flask
from flask import request, jsonify
from webscrape_turnover import get_teams_turnover
from webscrape_point_diff import get_teams_point_diff
from webscrape_OYG import get_teams_OYG
from teams import teams

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Will return the winner with the better team stats
def get_winner(tracker, team1, team2):
    if(tracker[team1] > tracker[team2]):
        return team1
    else:
        return team2

# A route to return the predicted winner of both teams given
@app.route('/api/v1/winner', methods=['GET'])
def api_all():
    # Get both parameters given
    team1 = request.args['team1']
    team2 = request.args['team2']

    # Convert the team name into the correct format above
    team1 = teams[team1]
    team2 = teams[team2]

    # Create dictionary of both teams to keep track of values
    tracker = {
        team1: 0,
        team2: 0
    }

    # Call the web scraper function and return stats for selected team
    tracker[get_teams_turnover(team1, team2)] += 1
    tracker[get_teams_point_diff(team1, team2)] += 1
    tracker[get_teams_OYG(team1, team2)] += 1

    # Check to see who is the winner with better stats
    result = get_winner(tracker, team1, team2)

    # Convert into a json object after getting correct key again
    result = list(teams.keys())[list(teams.values()).index(result)]
    winner = {'result': result}

    # Return as a json package
    return jsonify(winner)

# Run the Server App API
app.run()