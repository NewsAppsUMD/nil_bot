#THIS IS THE CLEAN VERSION OF MY SCRAPE.PY FILE

import requests
from bs4 import BeautifulSoup

url = 'https://api.on3.com/public/v1/deals?page=1'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
json = response.json()

players = []

player_data = json['list'][0]

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

players.append([date, first_name, last_name, school, sport, class_year, class_rank, company_or_collective, url])

print(players)