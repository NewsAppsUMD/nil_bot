import requests
from bs4 import BeautifulSoup

url = 'https://www.on3.com/nil/deals/'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
rows = soup.find_all('li', attrs={'class': 'DealTrackerItem_container__yWF2E'})

for row in rows:
    if row.find_all('img')[1]['title'] == 'houston cougars':
        # will change == later to maryland
        # next two lines: defining a variable (class year) and then telling it to print that
        year = row.find_all('h6')[1].text
        print(year)
        name = row.find('div', {'class': 'PlayerDealItem_playerContainer__XILE3'}).find('div').find('a').text
        print(name)
        # other things I want it to pull: sport, player name, deal type, collective/company name, date
        #where can I find sport: 
    # otherwise i don't care
    else:
        continue


# Eventually, within the loop, we are going to transform the list of rows and place the data into a list of cells that will put the data neatly into a row.

# Following directions here: https://first-web-scraper-umd.readthedocs.io/en/latest/
# Left off at this step: Next we take all the detective work we did with the page’s HTML above and convert it into a simple, direct command that will instruct BeautifulSoup on how to extract only the table we’re after.