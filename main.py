import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
soup = BeautifulSoup(response.text , "html.parser")
listings = soup.find_all("li", class_ = "ListItem-c11n-8-84-3-StyledListCardWrapper")

prices = soup.find_all("span", class_ = "PropertyCardWrapper__StyledPriceLine")

adresses = soup.find_all("address")

links = soup.find_all("a", class_ = "StyledPropertyCardDataArea-anchor")

print(len(prices))
print(len(adresses))
print(len(links))