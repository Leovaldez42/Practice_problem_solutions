import requests
from bs4 import BeautifulSoup 
import parser


url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html5lib')
content1 = soup.find_all('div', {"class:", "dek"})
for item in content1:
   print(item.text)
content = soup.find_all('section',{"class:", "content-section"})
for item in content:
    print(item.text.strip()) 