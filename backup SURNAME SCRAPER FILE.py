#ABT SURNAME SCRAPER FILE
#SEE requirements.txt for dependencies
####
####

#IMPORT LIBRARIES
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver


# INITIALIZE SAFARI SESSION
driver = webdriver.Safari()

url = "https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Europe"

driver.get(url)

# MAKE SOUP
soup = BeautifulSoup(driver.page_source,'lxml')
print(soup.prettify())

# CLOSER BROWSE AND ASSOCIATED WINDOWS, TABS WHEN DONE
driver.quit()

# ALL TABLES OBJECT
tables = soup.find_all('table', class_="wikitable")

all_surnames = []

#FIND SURNAME CELL INDEX FOR EACH TABLE
for table in tables:
    cell_index = 0

    for head in soup.find_all('th'):
        if 'surname' not in head.text:
            cell_index +=1
        else:
            pass
    
    #USE CELL_INDEX TO PRINT SURNAME COLUMN
  
    for row in soup.find_all('tr'):
        try:
            cells = row.find_all('td')
            surnames = cells[cell_index].text
            all_surnames.append(surnames)
        except:
            pass

df = pd.DataFrame(all_surnames)
printfile = df.to_csv('surnames3.csv')

