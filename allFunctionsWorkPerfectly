
import requests
from bs4 import BeautifulSoup


def printallurls(user_url):
   req = requests.get(user_url)
   famous_one = BeautifulSoup(req.content, 'html.parser')


   for link in famous_one.find_all('a'):
       print(link.get('href'))


printallurls("https://google.com")

def printallurls(url):
   links = []
   req = requests.get(url)
   req_text = req.text
   soup = BeautifulSoup(req_text, 'html.parser')
   soup2 = soup.find_all('a')
   for link in soup.find_all('a'):
       links.append(link.get('href'))


   for link in links:
       print(link)
import requests
from bs4 import BeautifulSoup




class Myfancycralwer:


   def __init__(self, url):
       self.url = url


   def printallurls(self):
       links = []    #creating a empty list
       req = requests.get(self.url) #get the html code
       req_text = req.text # make a new variable that is the text from the html(without the variable exc)
       soup = BeautifulSoup(req_text, 'html.parser') #parse the html code into small pices
       for link in soup.find_all('a'):
           links.append(link.get('href'))
       for link in links:
           print(link)


   def findingpath(self):
       req = requests.get(self.url)
       i = 0
       listpaths = ["about.html", "contact-us.php","home.html","blog/index.php","products/index.html","support/faq.html","page.html","media.html","solutions.html","messages.php","log-in.php","register.php"]
       for path in listpaths:
            path_test = self.url + listpaths[i]
            print(path_test)
            if requests.get(path_test).status_code == 200:
                print("the path is on the site")
            else:
                print("the path is not on the site")
            i=i+1





attack = Myfancycralwer("https://www.facebook.com/")
# attack = Myfancycralwer("https://www.google.com/")
# attack = Myfancycralwer("https://www.instgram.com/")
# attack = Myfancycralwer("https://www.https://www.gov.il/")
# attack = Myfancycralwer("#https://www.audible.com/")
# attack = Myfancycralwer("#https://https://maccabi-dent.com/")
# attack = Myfancycralwer("#https://www.maccabi4u.co.il/")
# attack = Myfancycralwer("#https://www.maccabi4u.co.il/")



attack.printallurls()
attack.findingpath()
