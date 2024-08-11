# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:09:01 2024

@author: marku
"""

"""
data scrap JLPT N3 list from: https://jlptstudy.net/N3/?kanji-list
create list of kanji 
get most common words from https://jisho.org/
Create a csv file from list

"""

import requests
from bs4 import BeautifulSoup


url = 'https://jlptstudy.net/N3/?kanji-list'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html5lib') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

#%%
import requests
from bs4 import BeautifulSoup


kanji_list = []

for page_counter in range(1,20):
    # Define the URL to scrape
    url = 'https://jisho.org/search/%20%23kanji%20%23jlpt-n3?page=' + str(page_counter)
    
    # Set headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Find the container that holds the Kanji information
        kanji_items = soup.find_all('div', class_='kanji_light_content')
    
        # Extract and print the Kanji, readings, and meanings
        for item in kanji_items:
            kanji = item.find('span', class_='character literal japanese_gothic').text.strip()
            meanings = item.find('div', class_='meanings english sense').text.strip()
            if item.find('div', class_='kun readings'):
                kunyomi = item.find('div', class_='kun readings').text.strip() 
            onyomi = item.find('div', class_='on readings').text.strip()
    
            kanji_list.append({
                'Kanji': kanji,
                'Onyomi': onyomi.replace('On: ','').replace('\n',''),
                'Kunyomi': kunyomi.replace('Kun: ','').replace('\n',''),
                'Meanings': meanings.replace('\n','')
            })
    
# Print the extracted Kanji list
for kanji in kanji_list:
        print(f"Kanji: {kanji['Kanji']}, Onyomi: {kanji['Onyomi']}, Kunyomi: {kanji['Kunyomi']}, Meanings: {kanji['Meanings']}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")