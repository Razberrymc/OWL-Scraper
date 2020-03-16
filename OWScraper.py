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

    s = randint(1, 5)

    time.sleep(s)


#The above gets the URLS for all 200 OWL players

heroname_list = []

import requests
import csv

csvfile = open("owlranks.csv", "w", newline="", encoding="utf-8")
c = csv.writer(csvfile)

c.writerow(["player url", "username", "player name", "league rank", "most played hero", "time played", "percent played"])

def get_info(player_url):
    driver.get("https://overwatchleague.com" + player_url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    heroes = soup.find_all('div', id="__next")

    for hero in heroes:
        masterlist = []
        try:
            url_list = hero.find("a", class_="language-dropdownstyles__DropdownListItem-sc-1je0eli-5 PeBbO")
            masterlist.append(url_list.attrs["href"])
            print(url_list.attrs["href"])
        except:
            masterlist.append("N/A")
        try:
            username_list = hero.find("div", class_="player-herostyles__PlayerTag-sc-4caowu-16 YPaBi")
            masterlist.append(username_list.get_text())
            print(username_list.get_text())
        except:
            masterlist.append("N/A")
        try:
            playername_list = hero.find("span", class_="player-herostyles__PlayerName-sc-4caowu-15 exNfoX")
            masterlist.append(playername_list.get_text())
            print(playername_list.get_text())
        except:
            masterlist.append("N/A")
        try:
            heroname_list = hero.find("span", class_="table-hero-cardstyles__Name-dh187u-1 iQzJSk resizable-namestyles__Abbreviation-sc-1qh8dp6-1 gYcSYZ")
            masterlist.append(heroname_list.get_text())
            print(heroname_list.get_text())
        except:
            masterlist.append("N/A")
        try:
            timeplayed_list = hero.find("div", class_="hero-rowstyles__TimePlayed-sc-1nswscz-1 fCaUZf")
            masterlist.append(timeplayed_list.get_text())
            print(timeplayed_list.get_text())
        except:
            masterlist.append("N/A")
        try:
            percentplayed_list = hero.find("div", class_="hero-rowstyles__PlayedPercentage-sc-1nswscz-2 bpjkJl")
            masterlist.append(percentplayed_list.get_text())
            print(percentplayed_list.get_text())
        except:
            masterlist.append("N/A")

        c.writerow(masterlist)

    return masterlist

for OWL in OWL_list:
    get_info(OWL)

driver.quit()

csvfile.close()
