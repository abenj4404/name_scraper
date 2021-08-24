#PRACTICE SCRAPER FILE
#IMPORT TOOLS
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#MAKES SURE RESULTS ARE IN ENGLISH
headers = {"Accept-Language": "en-US, en;q=0.5"}

#INITIALIZE LISTS
first_names = []
gender = []
usage = []
description = []

#SPECIFY URLS TO SCRAPE
urls = ["https://www.behindthename.com/names/usage/mythology", 
'https://www.behindthename.com/names/usage/mythology/2',
'https://www.behindthename.com/names/usage/mythology/3',
'https://www.behindthename.com/names/usage/mythology/4',
'https://www.behindthename.com/names/usage/mythology/5']

for url in urls:
    results = requests.get(url, headers=headers) 

    soup = BeautifulSoup(results.text, "html.parser")
    #FURTHER STRUCTURES FORMAT
    print(soup.prettify())

    container  = soup.find_all('div', class_="browsename")


    #LOOP THROUGH EACH CONTAINER TO GET ALL DATA DESIRED
    for div in container:

        name = div.span.a.text
        first_names.append(name)

        gen = div.find('span', class_='listgender').span.text
        gender.append(gen)

        use = div.find('span', class_='listusage').a.text
        usage.append(use)

        desc = div.text
        description.append(desc)

#create dataframe with pandas
#recall that in these key value pairs, the keys are the df column names and
#the values are the lists of data that have been scraped
firstnameframe = pd.DataFrame({
    'first_name': first_names,
    'genders': gender,
    'use': usage,
    'descriptions': description,
 })

#SAVE DATA TO CSV FILE USING PANDAS
firstnameframe.to_csv('firstnames.csv')
