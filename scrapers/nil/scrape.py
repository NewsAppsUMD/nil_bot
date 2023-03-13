import requests
from bs4 import BeautifulSoup

url = 'https://www.on3.com/nil/deals/'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())

# Following directions here: https://first-web-scraper-umd.readthedocs.io/en/latest/
# Left off at this step: Next we take all the detective work we did with the page’s HTML above and convert it into a simple, direct command that will instruct BeautifulSoup on how to extract only the table we’re after.