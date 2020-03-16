# OWL-Scraper
Scrape Overwatch League Players

When scraping the player pages on the Overwatch League website I wanted to get the page URL, player usernames, player actual names, their top hero, the time they have played that hero in the league and the percent they have played that hero in the league.

# What was used

First I had to get the URLs from the Overwatch League player roster, but I had to use selenium to click through the list because there were no links to other pages.

I used...

list = soup.find_all('a', class_='players-liststyles__PlayerCard-sc-1jhwo3g-21')
for item in list:
    OWL_list.append(item.get('href'))
    
to scrape all the URLs off of the page.

I then used...

for n in range(9)
    driver.find_element_by_css_selector('.icon-ChevronRight.iconstyles__StyledIcon-maju6z-1.cDYfNM').click()
   
to click a button to get to the next page and use the the prior function to append the URLs in a list.

After getting the list of URLs I used def get_info(player_url) to loop through the partial URLs to get to the individual player pages and scrape the info from there.

Initially, I was having trouble scraping anything off of the player pages, but after changing where my hero in heroes loop was, I could get all of the information I wasn't getting initially. 

# Data problems

Since the season has been postponed due to the coronavirus, many of the players have not had the opportunity to play this season, and some player data is missing from the csv file.
