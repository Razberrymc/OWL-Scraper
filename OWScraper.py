import time
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup

# load your driver
driver = webdriver.Chrome('C:/Users/User/Desktop/Adv Web Apps/scraping2020/chromedriver')

# get the web page
driver.get('https://overwatchleague.com/en-us/players');

OWL_list = []

page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

list = soup.find_all('a', class_='players-liststyles__PlayerCard-sc-1jhwo3g-21')
for item in list:
    OWL_list.append(item.get('href'))

for n in range(9):
    driver.find_element_by_css_selector('.icon-ChevronRight.iconstyles__StyledIcon-maju6z-1.cDYfNM').click()

    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")

    list = soup.find_all('a', class_='players-liststyles__PlayerCard-sc-1jhwo3g-21')
    for item in list:
        OWL_list.append(item.get('href'))

    s = randint(1, 3)
    #change 3 to 10 when finished

    time.sleep(s)

print(OWL_list)

driver.quit()

#The above gets the URLS for all 200 OWL players

import requests

url = "https://overwatchleague.com"

def get_info(player_url):
    page = requests.get(url + player_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    body = soup.find("body")
    print(body.get_text())
    info_div = soup.find("div", class_="player-herostyles__PlayerInfo-sc-4caowu-9.inZfKK")
    print(info_div)
    #for spn in info_div:
        #playername = spn.find("span", class_=".player-herostyles__PlayerName-sc-4caowu-15.exNfoX")
        #try:
            #print(playername.get_text())
        #except:
            #pass

    #print(playername)
    #username = soup.find("div", class_=".player-herostyles__PlayerTag-sc-4caowu-16.YPaBi")
    #print(username)

for OWL in OWL_list:
    get_info(OWL)
