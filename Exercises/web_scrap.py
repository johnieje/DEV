from bs4 import BeautifulSoup
import requests

url = 'https://www.bbc.com'
r_html = requests.get(url).text

soup = BeautifulSoup(r_html, 'lxml')

articles = soup.find_all('div', class_='module__content')
# print(articles.prettify())
for article in articles:

    # Print Heading
    try:
        heading = article.h3.a.text
        article_url = article.a.get('href')
        print(heading)
        # Print Summary
        summary = article.p.text
        print(summary)
        # Print Heading Url
        print(url + article_url)
        tag = article.find('a', class_='media__tag tag tag--news')
        tag_url = tag.get('href')
        print(tag.text)
        print(url + tag_url)
        print()
    except Exception as e:
        pass
