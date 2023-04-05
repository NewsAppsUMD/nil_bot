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
# creates an empty list called results that we will use to store the data

big_ten_teams = ['Illinois Fighting Illini', 'Indiana Hoosiers', 'Iowa Hawkeyes', 'Maryland Terrapins', 'Michigan Wolverines', 'Michigan State Spartans', 'Minnesota Golden Gophers', 'Nebraska Cornhuskers', 'Northwestern Wildcats', 'Ohio State Buckeyes', 'Penn State Nittany Lions', 'Purdue Boilermakers', 'Rutgers Scarlet Knights', 'Wisconsin Badgers']
# In Python, an equal sign assigns a variable. We've created a variable with all the Big Ten teams.

for player_data in json['list']:
    class_year = player_data['person']['classYear']
    class_rank = player_data['person']['classRank']
    first_name = player_data['person']['firstName']
    last_name = player_data['person']['lastName']
    if 'sport' in player_data and 'name' in player_data['sport']:
        sport = player_data['sport']['name']
    elif player_data.get('rating') and 'sport' in player_data['rating']:
        sport = player_data['rating']['sport']['name']
    else:
        sport = None
    if 'company' in player_data and player_data['company']:
        company = player_data['company']['name']
    elif 'collectiveGroup' in player_data and player_data['collectiveGroup']:
        company = player_data['collectiveGroup']['name']
    else:
        company = None
    date = player_data['date']
    url = player_data['sourceUrl']
    if 'status' in player_data and player_data['status'] is not None and 'committedAsset' in player_data['status'] and player_data['status']['committedAsset'] is not None:
        school = player_data['status']['committedAsset']['fullName']
    else:
        school = None
# ideally, I think I would like this code to be "if there is something in 'company,' print the word "company," otherwise print the word "collective;" then a separate line of code would pull the name of the company or the collective
# is there a way to clean up the date output?

    if school in big_ten_teams:
        results.append([date, first_name, last_name, school, sport, class_year, class_rank, company, url])
    else:
        continue
    # Here, we're saying take the dictionary I made above and append it to the empty list (players) we made earlier.

print(results)
# Output the players list
