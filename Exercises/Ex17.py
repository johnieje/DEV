import requests
from bs4 import BeautifulSoup

url = 'http://nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

# print(soup.title.string) class="balancedHeadline

headings = soup.find_all('a')

for heading in headings:
    print(heading)
print(len(headings))



