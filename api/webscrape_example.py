from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

def get_team_stats(team1, team2):
    turnover_margin_url = 'https://www.teamrankings.com/nfl/stat/turnover-margin-per-game'
    turnover_margin_data = urlopen(turnover_margin_url)
    turnover_margin_html = turnover_margin_data.read()
    turnover_margin_data.close()

    # String of entire page
    page_soup = soup(turnover_margin_html, 'html.parser')

    # Create lists of teams and turnover margins (looks for 'td' tag and specific classes for team names and turnover margins)
    teams = page_soup.findAll('td', {'class' : 'text-left nowrap'})
    turnover_margins = page_soup.findAll('td', {'class' : 'text-right'})

    # Convert turnover margins to floats
    tm_text = []
    teams_text = []
    for tm in turnover_margins:
        tm_text.append(float(tm.text))

    # Change abbreviated team names and put team names in list
    for team in teams:
        temp = team.text
        if "LA" in temp:
            if "Rams" in temp:
                temp = "Los Angeles Rams"
            if "Chargers" in temp:
                temp = "Los Angeles Chargers"
        if "NY" in temp:
            if "Giants" in temp:
                temp = "New York Giants"
            if "Jets" in temp:
                temp = "New York Jets"
        teams_text.append(temp)

    # Find average turnover margin (scewed towards last few games)
    avg_tm = []
    for i in range(len(tm_text)):
        if(i > 0):
            if (i % 5) == 0:
                temp = (tm_text[i-3] + tm_text[i-4] + tm_text[i-5]) / 3
                avg_tm.append(temp)

    # Create dictionary with team name & turnover margin
    avg_tm_dict = {teams_text[i]: avg_tm[i] for i in range(len(teams_text))}

    # Get both team input stats and compare
    stats1 = avg_tm_dict[team1]
    stats2 = avg_tm_dict[team2]

    # Return the higher of the stats
    if(stats1 > stats2):
        return team1
    else:
        return team2