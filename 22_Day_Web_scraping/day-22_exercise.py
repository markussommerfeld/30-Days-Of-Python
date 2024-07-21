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
# Other example from Website

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

#%%
# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
import re
import json

url = 'https://archive.ics.uci.edu/datasets'

response_dataset = requests.get(url)
content_dataset = response_dataset.content_dataset # we get all the content from the website
soup = BeautifulSoup(content_dataset, 'html5lib') # beautiful soup will give a chance to parse
# print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
# print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # gives the whole page on the website
# print(response_dataset.status_code)

f = soup.find_all('span',attrs={'class':'stat-figure'})
for i in f:
      print(i.parent.text)
      
      
#%% 
''' from geeksforgeeks.org'''


# Import the required modules
import requests
from bs4 import BeautifulSoup
import json
 
 
# Function will return a list of dictionaries
# each containing information of books.
def json_from_html_using_bs4(base_url):
 
    # requests.get(url) returns a response that is saved
    # in a response object called page.
    page = requests.get(base_url)
 
    # page.text gives us access to the web data in text
    # format, we pass it as an argument to BeautifulSoup
    # along with the html.parser which will create a
    # parsed tree in soup.
    soup = BeautifulSoup(page.text, "html.parser")
 
    # soup.find_all finds the div's, all having the same
    # class "col-xs-6 col-sm-4 col-md-3 col-lg-3" that is
    # stored in books
    books = soup.find_all(
        'li', attrs={'class': 
                'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
 
    # Initialise the required variables
    star = ['One', 'Two', 'Three', 'Four', 'Five']
    res, book_no = [], 1
     
    # Iterate books classand check for the given tags
    # to get the information of each books.
    for book in books:
 
        # Title of book in <img> tag with "alt" key.
        title = book.find('img')['alt']
 
        # Link of book in <a> tag with "href" key
        link = base_url[:37] + book.find('a')['href']
 
        # Rating of book from 
 
<p> tag
        for index in range(5):
            find_stars = book.find(
            'p', attrs={'class': 'star-rating ' + star[index]})
             
            # Check which star-rating class is not 
            # returning None and then break the loop
            if find_stars is not None:
                stars = star[index] + " out of 5"
                break
 
        # Price of book from 
 
<p> tag in price_color class
        price = book.find('p', attrs={'class': 'price_color'
                                                    }).text
 
        # Stock Status of book from 
 
<p> tag in
        # instock availability class.
        instock = book.find('p', attrs={'class': 
                        'instock availability'}).text.strip()
         
        # Create a dictionary with the above book information
        data = {'book no': str(book_no), 'title': title, 
            'rating': stars, 'price': price, 'link': link, 
            'stock': instock}
 
        # Append the dictionary to the list
        res.append(data)
        book_no += 1
    return res
 
 
# Main Function
if __name__ == "__main__":
 
    # Enter the url of website
    base_url = "https://books.toscrape.com/catalogue/page-1.html"
 
    # Function will return a list of dictionaries
    res = json_from_html_using_bs4(base_url)
 
    # Convert the python objects into json object and export
    # it to books.json file.
    with open('books.json', 'w', encoding='latin-1') as f:
        json.dump(res, f, indent=8, ensure_ascii=False)
    print("Created Json File")

