#Установить MongoDB и реализовать хранение доĸументов по ĸатегориям

# смотреть news.new_zealand.csv

import pymongo
from bs4 import BeautifulSoup
import requests

client = pymongo.MongoClient("localhost", 27017)
db = client.news
news_collection = db["new_zealand"]


urls = [
        'https://en.wikinews.org/wiki/New_Zealand_raises_interest_rates_in_second_straight_month_to_0.75%25',
        'https://en.wikinews.org/wiki/New_Zealand_announces_new_Matariki_public_holiday',
        'https://en.wikinews.org/wiki/Three_earthquakes_hit_off_New_Zealand%27s_coastal_areas,_residents_warned_to_avoid_coast'
       ]

for url in urls:

    r = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find the content of the article
    s = soup.find('div', class_='mw-parser-output')

    lines = s.find_all('p')
    text = []
    for line in lines:
        text.append(line.text)

    # Add the content of the article to the collection
    dict = {"content": text}
    news_collection.insert_one(dict)


