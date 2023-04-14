# Using this file to download every single NIL deal on the website, which I will then use in R to see if there are any Big Ten teams with school name aliases that we are not capturing.

import csv
import math
import requests
from datetime import datetime

base_url = 'https://api.on3.com/public/v1/deals?page={}'
results = []

response = requests.get(base_url.format(1), headers={'User-Agent': 'Mozilla/5.0'})
json = response.json()
total_count = json['pagination']['count']
items_per_page = json['pagination']['itemsPerPage']

total_pages = math.ceil(total_count/items_per_page)

for page_num in range(1, total_pages+1):
    url = base_url.format(page_num)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    json = response.json()
    player_data_list = json['list']
    for player_data in json['list']:
        class_year = player_data['person']['classYear']
        class_rank = player_data['person']['classRank']
        name = player_data['person']['fullName']
        if 'sport' in player_data and 'name' in player_data['sport']:
            sport = player_data['sport']['name']
        elif player_data.get('rating') and 'sport' in player_data['rating']:
            sport = player_data['rating']['sport']['name']
        else:
            sport = None
        if 'company' in player_data and player_data['company']:
            company_name = player_data['company']['name']
        else:
            company_name = None
        if 'collectiveGroup' in player_data and player_data['collectiveGroup']:
            collective_name = player_data['collectiveGroup']['name']
        else:
            collective_name = None
        if 'agent' in player_data and player_data['agent']:
            agent_name = player_data['agent']['name']
        else:
            agent_name = None
        if company_name and collective_name:
            partner = f"{collective_name}, {company_name}"
        elif company_name:
            partner = company_name
        elif collective_name:
            partner = collective_name
        elif agent_name:
            partner = agent_name
        else:
            partner = None
        if company_name and collective_name:
            type = 'Collective and company'
        elif company_name:
            type = 'Company'
        elif collective_name:
            type = 'Collective'
        elif agent_name:
            type = 'NIL representation'
        else:
            type = None
        date = player_data['date']
        formatted_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S').strftime('%m/%d/%Y')
        url = player_data['sourceUrl']
        if 'status' in player_data and player_data['status'] is not None and 'committedAsset' in player_data['status'] and player_data['status']['committedAsset'] is not None:
            school = player_data['status']['committedAsset']['fullName']
        elif 'rpm' in player_data and player_data['rpm'] is not None and 'fullName' in player_data['rpm'] and player_data['rpm']['fullName'] is not None:
            school = player_data['rpm']['fullName']
        else:
            school = None

        results.append([formatted_date, name, school, sport, class_year, class_rank, type, partner, url])
        
#print(results)

headers = ['Date', 'Name', 'School', 'Sport', 'Class Year', 'Class Rank', 'Type', 'Partner', 'URL']

with open("./all-nil.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(results)