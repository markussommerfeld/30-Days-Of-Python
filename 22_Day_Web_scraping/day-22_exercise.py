# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:11:28 2024

@author: marku
"""

"""

    Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
    Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
    Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
"""

import requests
from bs4 import BeautifulSoup


url = 'https://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html5lib') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

# tables = soup.find('section', attrs={'class':'stat-section'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
# table1 =  tables.findAll('li') # the result is a list, we are taking out data from it
# for td in table1.find_all('td'):
#     print(td.text)

f = soup.find_all('span',attrs={'class':'stat-figure'})
for i in f:
      print(i.parent.text)
    
#%%

#Python program to scrape website  
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "http://www.values.com/inspirational-quotes" 
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html5lib') 
   
quotes=[]  # a list to store quotes 
   
table = soup.find('div', attrs = {'id':'all_quotes'})  
   
for row in table.findAll('div', 
                         attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.img['alt'].split(" #")[0] 
    quote['author'] = row.img['alt'].split(" #")[1] 
    quotes.append(quote) 
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines','author']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 
