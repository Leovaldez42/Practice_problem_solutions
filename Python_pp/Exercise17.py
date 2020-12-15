from bs4 import BeautifulSoup
import requests
import parser

def web_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')

    for title in soup.find_all('h2', {'class' : 'story-heading'}):
        t = title.string
        if t is not None:
            print(t)

web_page('https://www.nytimes.com')