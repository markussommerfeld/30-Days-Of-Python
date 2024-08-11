# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:29:52 2024

@author: marku
"""

# importing basic libraries
import requests
from bs4 import BeautifulSoup


# request for getting the target html.
def get_html(URL):
    scrape_result = requests.get(URL)
    return scrape_result.text
vac_html = get_html("https://ourworldindata.org/covid-vaccinations")

# the BeautifulSoup library for scraping the data, with "html.parser" for parsing.
beatiful_soup = BeautifulSoup(vac_html, "html.parser")

# view the html script.
print(beatiful_soup.prettify())

# finding the content of interest 
get_table = beatiful_soup.find_all("tr")

for x in get_table:
    print("*********")
    print(x)
    
    
#%% above didn't work

import pandas as pd

url = "https://covid.ourworldindata.org/data/internal/megafile--vaccinations-bydose.json"
jsonData = requests.get(url).json()

df = pd.DataFrame(jsonData)

print(df)