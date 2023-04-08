#IN THIS VERSION OF MY SCRAPE.PY FILE, I AM PUTTING IN A LOT OF NOTES TO HELP ME UNDERSTAND WHAT IS HAPPENING

# resources:
# https://first-web-scraper-umd.readthedocs.io/en/latest/
# ChatGPT useful for specific questions and debugging errors
# for git scraping: https://github.com/NewsAppsUMD/git-scraping

import csv
import math
import requests
from datetime import datetime
#bringing in libraries we need

base_url = 'https://api.on3.com/public/v1/deals?page={}'
results = []
# creates an empty list called results that we will use to store the data
# resource for identifying json keys: https://jsonlint.com/
# In Python, an equals sign means we are defining a variable

big_ten_teams = ['Illinois Fighting Illini', 'Indiana Hoosiers', 'Iowa Hawkeyes', 'Maryland Terrapins', 'Michigan Wolverines', 'Michigan State Spartans', 'Minnesota Golden Gophers', 'Nebraska Cornhuskers', 'Northwestern Wildcats', 'Ohio State Buckeyes', 'Penn State Nittany Lions', 'Purdue Boilermakers', 'Rutgers Scarlet Knights', 'Wisconsin Badgers']

response = requests.get(base_url.format(1), headers={'User-Agent': 'Mozilla/5.0'})
json = response.json()
total_count = json['pagination']['count']
items_per_page = json['pagination']['itemsPerPage']
# downloads the json version of the On3NIL page
# defining some variables to help us figure out the end range of the scrape
# json keys are enclosed in quotation marks

total_pages = math.ceil(total_count/items_per_page)
# defining another variable to help us figure out the end range of the scrape; when we add this to the loop, we will add a +1 in case total_count/items is a fraction

for page_num in range(1, total_pages+1):
    url = base_url.format(page_num)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    json = response.json()
    player_data_list = json['list']
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
            type = 'Company'
        elif 'collectiveGroup' in player_data and player_data['collectiveGroup']:
            type = 'Collective'
        else:
            type = None
        if 'company' in player_data and player_data['company']:
            partner = player_data['company']['name']
        elif 'collectiveGroup' in player_data and player_data['collectiveGroup']:
            partner = player_data['collectiveGroup']['name']
        else:
            partner = None
        date = player_data['date']
        formatted_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S').strftime('%m/%d/%Y')
        url = player_data['sourceUrl']
        if 'status' in player_data and player_data['status'] is not None and 'committedAsset' in player_data['status'] and player_data['status']['committedAsset'] is not None:
            school = player_data['status']['committedAsset']['fullName']
        else:
            school = None
#this is the bulk of the code; we are creating ways for the values from various json keys to pull into our code

        if school in big_ten_teams:
            results.append([formatted_date, last_name, first_name, school, sport, class_year, class_rank, type, partner, url])
        else:
            continue
# here, we're saying take the variables I defined above and appending them to the empty list (players) we made earlier.

#print(results)
# this is commented out because we no longer want the output to print in the terminal; instead, it will print to a CSV

headers = ['Date', 'Last Name', 'First Name', 'School', 'Sport', 'Class Year', 'Class Rank', 'Type', 'Partner', 'URL']
# define headers for output table

with open("./big-ten-nil.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(results)
#write headers and results to CSV file that will be accessible in code directory