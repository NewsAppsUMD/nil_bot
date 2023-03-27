import requests
from bs4 import BeautifulSoup

big_ten_teams = ['Illinois Fighting Illini', 'Indiana Hoosiers', 'Iowa Hawkeyes', 'Maryland Terrapins', 'Michigan Wolverines', 'Michigan State Spartans', 'Minnesota Golden Gophers', 'Nebraska Cornhuskers', 'Northwestern Wildcats', 'Ohio State Buckeyes', 'Penn State Nittany Lions', 'Purdue Boilermakers', 'Rutgers Scarlet Knights', 'Wisconsin Badgers']

players = []
# creates a blank frame that we will fill in

# range loop
# build the page url
url = 'https://www.on3.com/nil/deals/'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
json = response.json()

player_data = json['list'][2]

# class year is ['person']['classYear']
class_year = player_data['person']['classYear']
# class rank is ['person']['classRank']
class_rank = player_data['person']['classRank']
# first name is ['person']['firstName']
first_name = player_data['person']['firstName']
# last name is ['person']['lastName']
last_name = player_data['person']['lastName']
# sport is ['rating']['sport']['name']
sport = player_data['sport']['name']
# company is ['company']['name']
company = player_data['company']['name']
# collective is ['collectiveGroup']['name']
collective = player_data['collectiveGroup']['name']
# date is ['date']
date = player_data['date']
# url is ['sourceUrl']
url = player_data['sourceUrl']
# school is ['status']['committedAsset']['fullName']
school = player_data['status']['committedAsset']['fullName']

#is this working?
player = [date, first_name, last_name, school, class_year, class_rank, sport, company, collective, url]

#player makes one row, then we put rows together (players), then we tackle the pagination
players.append(player)

for row in rows:
    if row.find_all('img')[1]['title'] in big_ten_teams:
        # change to maryland terrapins - just using houston for testing
        # defining a variable (with Derek's help) and then telling it to print that variable
        year = row.find_all('h6')[1].text
        print(year)
        name = row.find('div', {'class': 'PlayerDealItem_playerContainer__XILE3'}).find('div').find('a').text
        print(name)
        # continue to define variables except this time by myself (and I think this worked?)
        date = row.find('span', {'class': 'MuiTypography-root DealTrackerItem_date__I5gVl MuiTypography-caption MuiTypography-colorTextPrimary'}).text
        print(date)
        deal = row.find('div', {'class': 'DealTrackerItem_companyWrapper__RFysQ'}).find('h6').text
        print(deal)
        company = row.find('div', {'class': 'DealTrackerItem_companyWrapper__RFysQ'}).find('h5').text
        print(company)
        # other things I want it to pull: sport
    # this next set of code: if it's not the team I care about, please skip and continue
    else:
        continue

# Following directions here: https://first-web-scraper-umd.readthedocs.io/en/latest/
# Left off at this step: Next we take all the detective work we did with the page’s HTML above and convert it into a simple, direct command that will instruct BeautifulSoup on how to extract only the table we’re after.

# Next steps:
# Figure out the sport mess
# Will this work for Maryland? Is there enough data for it to be an interesting bot for just Maryland, or should it be a Big Ten bot?
# Eventually, within the loop, we are going to transform the list of rows and place the data into a list of cells that will put the data neatly into a row.
# How do I search beyond page 1 of the site?
