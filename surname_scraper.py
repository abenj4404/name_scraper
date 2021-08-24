#ABT SURNAME SCRAPER FILE
#SEE requirements.txt for dependencies
####
####

#IMPORT TOOLS
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#ENGLISH RESULTS HEADER
headers = {"Accept-Language": "en-US, en;q=0.5"}

#INITIALIZE LISTS TO STORE SCRAPED DATA TO BE PAIRED WITH DATAFRAME COLUMNS
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

#LOOP THROUGH URLS AND APPEND TO EMPTY LISTS
for url in urls:
    results = requests.get(url, headers=headers) 

    soup = BeautifulSoup(results.text, "html.parser")
    
    #FORMAT DATA BETTER
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

#CREATE DATAFRAME WITH PANDAS
firstnameframe = pd.DataFrame({
    'first_name': first_names,
    'genders': gender,
    'use': usage,
    'descriptions': description,
 })

#SAVE DATA TO CSV FILE
firstnameframe.to_csv('firstnames.csv')
