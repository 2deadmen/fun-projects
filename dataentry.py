import time

import requests
from forms import Forms
from bs4 import BeautifulSoup

zillow ="https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.8563031328125%2C%22east%22%3A-122.0103558671875%2C%22south%22%3A37.508872488425496%2C%22north%22%3A38.04075479434776%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
form = Forms()
header={
   "User-Agent" :"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,kn;q=0.6",
   "Accept-Language" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}
response = requests.get(zillow, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())
address=soup.find_all(name="address",class_="list-card-addr")
address_list=[]
for i in address:
   text= i.getText()
   address_list.append(text)
price=soup.find_all(name="div",class_="list-card-price")
price_list=[]
for i in price:
   text =i.getText()
   price_list.append(text)
links=soup.select(selector=".list-card-top a")
link_list=[]
for i in links:
   link = i.get("href")
   link_list.append(link)

form.upload(address_list,price_list,link_list)
