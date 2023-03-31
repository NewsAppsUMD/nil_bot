#IN THIS VERSION OF MY SCRAPE.PY FILE, I AM PUTTING IN A LOT OF NOTES TO HELP ME UNDERSTAND WHAT IS HAPPENING

import requests
# requests is a Python library that opens a URL, downloads HTML, and passes it to BeautifulSoup
from bs4 import BeautifulSoup
# BeautifulSoup is a Python library that parses and extracts HTML

url = 'https://api.on3.com/public/v1/deals?page=1'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
json = response.json()
# downloads the json version of the On3NIL page

players = []
# creates an empty list called players that we will use to store the data

player_data = json['list'][0]
# I think we're making a variable called player_data that gets the json version of everything that is under 'list' on On3NIL for the first player (0)

class_year = player_data['person']['classYear']
class_rank = player_data['person']['classRank']
first_name = player_data['person']['firstName']
last_name = player_data['person']['lastName']
if 'sport' in player_data:
    sport = player_data['sport']['name']
else:
    sport = player_data['rating']['sport']['name']
if 'company' in player_data:
    company_or_collective = player_data['company']['name']
else:
    company_or_collective = player_data['collectiveGroup']['name']
date = player_data['date']
url = player_data['sourceUrl']
school = player_data['status']['committedAsset']['fullName']
# A list (dictionary?) of all the variables for each player we want to pull within the 'list' section of On3NIL
# Can we clean up date output?

players.append([date, first_name, last_name, school, sport, class_year, class_rank, company_or_collective, url])
# Here, we're saying take the dictionary I made above and append it to the empty list (players) we made earlier.

print(players)
# Output the players list

# Getting errors when there is no sport or when the player got a deal from a collective ('NoneType' object is not subscriptable). Also getting same error message for other variables (e.g., school).

big_ten_teams = ['Illinois Fighting Illini', 'Indiana Hoosiers', 'Iowa Hawkeyes', 'Maryland Terrapins', 'Michigan Wolverines', 'Michigan State Spartans', 'Minnesota Golden Gophers', 'Nebraska Cornhuskers', 'Northwestern Wildcats', 'Ohio State Buckeyes', 'Penn State Nittany Lions', 'Purdue Boilermakers', 'Rutgers Scarlet Knights', 'Wisconsin Badgers']
# In Python, an equal sign assigns a variable. We've created a variable with all the Big Ten teams.