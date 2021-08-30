#ABT SURNAME SCRAPER FILE
#SEE requirements.txt for dependencies
####
####

#IMPORT LIBRARIES
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver


#INITIALIZE SAFARI SESSION
driver = webdriver.Safari()

url = "https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Europe"

driver.get(url)

#make soup!
soup = BeautifulSoup(driver.page_source,'lxml')
print(soup.prettify())

#CLOSER BROWSER AND ASSOCIATED WINDOWS, TABS WHEN DONE
driver.quit()


#FIND ALL TABLES TO SCRAPE
all_tables = soup.find_all('table', class_="wikitable")

#INITIALIZE EMPTY LISTS FOR DATAFRAME
table_list = []

#LOOP THROUGH ALL TABLES
for table in all_tables:
    row_data = [[cell.text for cell in row.find_all(["th","td"])] for row in table.find_all("tr")]
    table_list.append(row_data)

surnameframe = pd.DataFrame(row_data)
surnameframe.to_csv('test.csv')


