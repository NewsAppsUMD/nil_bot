#IN THIS VERSION OF MY SCRAPE.PY FILE, I AM PUTTING IN A LOT OF NOTES TO HELP ME UNDERSTAND WHAT IS HAPPENING

import requests
# requests is a Python library that opens a URL, downloads HTML, and passes it to BeautifulSoup
from bs4 import BeautifulSoup
# BeautifulSoup is a Python library that parses and extracts HTML

url = 'https://api.on3.com/public/v1/deals?page=1'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
json = response.json()
# downloads the json version of the On3NIL page
# resource for parsing json keys: https://jsonlint.com/

results = []
# creates an empty list called players that we will use to store the data

big_ten_teams = ['Illinois Fighting Illini', 'Indiana Hoosiers', 'Iowa Hawkeyes', 'Maryland Terrapins', 'Michigan Wolverines', 'Michigan State Spartans', 'Minnesota Golden Gophers', 'Nebraska Cornhuskers', 'Northwestern Wildcats', 'Ohio State Buckeyes', 'Penn State Nittany Lions', 'Purdue Boilermakers', 'Rutgers Scarlet Knights', 'Wisconsin Badgers']
# In Python, an equal sign assigns a variable. We've created a variable with all the Big Ten teams.

players = json['list']
# I think we're making a variable called player_data that gets the json version of everything that is under 'list' on On3NIL for the first player (0)

for player_data in players:

    # might need a statement here like: for player in players: (potential resource: https://www.w3schools.com/python/python_for_loops.asp)
    # might need to put all of this in an if statement that says: if the team is in the big ten:
    print(player_data)
    class_year = player_data['person']['classYear']
    class_rank = player_data['person']['classRank']
    first_name = player_data['person']['firstName']
    last_name = player_data['person']['lastName']
    if 'sport' in player_data and 'name' in player_data['sport']:
        sport = player_data['sport']['name']
    elif player_data['rating'] is not None:
        sport = player_data['rating']['sport']['name']
    else:
        sport = None
    # https://www.w3schools.com/python/python_conditions.asp
    if player_data['company'] is not None:
        company = player_data['company']['name']
    else:
        company = None
    if player_data['collectiveGroup'] is not None:
        collective = player_data['collectiveGroup']['name']
    else:
        collective = None
    # ideally, I think I would like this code to be "if there is something in 'company,' print the word "company," otherwise print the word "collective;" then a separate line of code would pull the name of the company or the collective
    date = player_data['date']
    # is there a way to clean up this output?
    url = player_data['sourceUrl']
    school = player_data['status']['committedAsset']['fullName']
    # might need to put an else statement here that says: if the team is not in the big ten, then continue

    results.append([date, first_name, last_name, school, sport, class_year, class_rank, company, collective, url])
    # Here, we're saying take the dictionary I made above and append it to the empty list (players) we made earlier.

print(results)
# Output the players list

# This is working for many players, but getting errors when there is no sport or when the player got a deal from a collective ('NoneType' object is not subscriptable). Also getting same error message for some players in other variables (e.g., school).