from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.espn.com/mens-college-basketball/team/_/id/356/illinois-fighting-illini"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
schedule_section = soup.find("section", class_="Schedule__Group")
game_urls = [link.get('href') for link in schedule_section.findAll('a')]
#print(game_urls)

rtest = requests.get(game_urls[0].replace("/game/", "/boxscore/"))
df_list = pd.read_html(rtest.text) # this parses all the tables in webpages to a list
print(pd.concat([df_list[1], df_list[2]], axis=1))


# TODO: logic for parsing box score
# for game_url in game_urls:
#   concat dfs
#   add gameId, teamID
#   save to some sink?


## TODO: figure out how to get last seasons?
