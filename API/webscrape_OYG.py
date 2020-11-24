from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

# Function will scrape the data for each teams allowed yard per game
def get_teams_OYG(team1, team2):
    opp_ypg_url = 'https://www.teamrankings.com/nfl/stat/opponent-yards-per-game'
    opp_ypg_data = urlopen(opp_ypg_url)
    opp_ypg_html = opp_ypg_data.read()
    opp_ypg_data.close()

    page_soup = soup(opp_ypg_html, 'html.parser')

    # List of all opponents' yards per game
    opp_ypg = page_soup.findAll('td', {'class' : 'text-right'})
    # List of teams
    temp = page_soup.findAll('td', {'class' : 'text-left nowrap'})
    _teams = []
    for line in temp:
        _teams.append(line.text)

    # Create list of Opponents yards per game in 2020
    opp_ypg_TT = []
    i=0
    for line in opp_ypg:
        if i % 6 == 0:
            opp_ypg_TT.append(float(line.text))
        i+=1
    # Change abbreviated team names
    teams_text = []
    for team in _teams:
        temp = team
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
    # Create dictionary for opponents yards per game
    opp_ypg_dict = {teams_text[i]: opp_ypg_TT[i] for i in range(len(teams_text))}
    # Get both team stats given from user
    stats1 = opp_ypg_dict[team1]
    stats2 = opp_ypg_dict[team2]

    # Return whichever team has the least amount of yards allowed per game
    if(stats1 < stats2):
        return team1
    else:
        return team2