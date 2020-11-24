from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

# Will return the average point differential per game
def get_teams_point_diff(team1, team2):
    avg_point_differential_url = 'https://www.teamrankings.com/nfl/stat/average-scoring-margin'
    avg_point_differential_data = urlopen(avg_point_differential_url)
    avg_point_differential_html = avg_point_differential_data.read()
    avg_point_differential_data.close()
    page_soup = soup(avg_point_differential_html, 'html.parser')

    # Create lists of teams and avg_point differential
    teams = page_soup.findAll('td', {'class' : 'text-left nowrap'})
    avg_point_differentials = page_soup.findAll('td', {'class' : 'text-right'})
    pd_text = []
    teams_text = []
    for pd in avg_point_differentials:
        pd_text.append(float(pd.text))

    # Change abbreviated team names
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

    # Find average point differential (scewed towards last few games)
    avg_pd = []
    j = 1
    for i in range(len(pd_text)):
        if(i > 0):
            if (j % 6) == 0:
            #    print(pd_text[i-3], pd_text[i-4])
                temp = (pd_text[i-4] + pd_text[i-5]) / 2
                avg_pd.append(temp)
        j+=1

    # Create dictionary with team name & avg_point differential
    pd_dict = {teams_text[i]: avg_pd[i] for i in range(len(teams_text))}
    # Get both input teams point differential
    stats1 = pd_dict[team1]
    stats2 = pd_dict[team2]

    # Return whichever team has the best point differential
    if(stats1 > stats2):
        return team1
    else:
        return team2