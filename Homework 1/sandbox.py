'''from requests import get
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)\
print(response.text[:500])'''


#This will not run on online IDE
import requests
from bs4 import BeautifulSoup

URL = "http://www.apnews.com/d73064c57a624f47b28e370f53f82f7c"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print soup.get_text().encode('UTF-8')
#print("text")

with open("../WebCrawler/testFile.txt","w") as oFile:
    oFile.write(soup.get_text().encode('UTF-8'))
    oFile.close()


# In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, and push them into an array so that I can manipulate and do fun stuff with the data.
