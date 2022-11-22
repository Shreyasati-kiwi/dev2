import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.kiwitech.com/" 
getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
 
soup = BeautifulSoup(getURL.text, 'html.parser')

images = soup.find('img',attrs={"alt": "KiwiTech - Logo"})
logoUnresolved = images.get('src')
logo = requests.compat.urljoin(URL, logoUnresolved)

abouts = soup.find(href=re.compile("contact"))
aboutURL = abouts.get('href')

getNewURL = requests.get(aboutURL, headers={"User-Agent":"Mozilla/5.0"})
soup1 = BeautifulSoup(getNewURL.text, 'html.parser')
address = soup1.find('h2',string=re.compile("Locations"))
for i in address.parent.next_siblings:
    ad = i.get_text().strip().replace("\n", "")
    print(ad)

webs = requests.get(logo)
open('images/' + logo.split('/')[-1], 'wb').write(webs.content)