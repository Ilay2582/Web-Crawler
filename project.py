import requests
from bs4 import BeautifulSoup

site_url = input("enter the url of the site:")
new_type = requests.get(site_url)

famous_one = BeautifulSoup(new_type,'html.parser')

#while famous_one.find_all('a'):

link_elements = famous_one.select("a[href]")

urls = []
for link_element in link_elements:
   url = link_element['href']
   if "https://scrapeme.live/shop" in url:
      urls.append(url)




