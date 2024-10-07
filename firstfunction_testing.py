import requests
from bs4 import BeautifulSoup

def printallurls(user_url):
    req = requests.get(user_url)
    famous_one = BeautifulSoup(req.content, 'html.parser')

    for link in famous_one.find_all('a'):
        print(link.get('href'))

printallurls("https://danielvihorev.ravpage.co.il/privtae-business-page")
