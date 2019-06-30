from bs4 import BeautifulSoup
import requests

with open("/Users/patrickpower/Documents/Learn/DataScience/Webscrapping/simple.html") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div', class_ = "article"):
    headline = article.h2.a.text
    summary = article.p.text

    print(headline)
    print(summary)
    print()
