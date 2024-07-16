# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:27:49 2024

@author: marku
"""

"""

    Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
    Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
        the min, max, mean, median, standard deviation of cats' weight in metric units.
        the min, max, mean, median, standard deviation of cats' lifespan in years.
        Create a frequency table of country and breed of cats
    Read the countries API and find
        the 10 largest countries
        the 10 most spoken languages
        the total number of languages in the countries API
    UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

"""



#1 done
import requests # importing the request module
import re
import numpy as np

def find_most_common_words(text, n):
      
    all_words_list = re.findall(r'\w+', text,re.I) #\w one word character + one or more times
    all_words_set = set(all_words_list)
    
    all_words_count = [(all_words_list.count(j), j) for i,j in enumerate(all_words_set)]
    
    all_words_count.sort(reverse = True)  
    return(all_words_count[:n])

url = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text[:10]) #

print(find_most_common_words(response.text, 10))

#2 done

url = 'https://api.thecatapi.com/v1/breeds'  # countries api
response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
cats = response.json()
# print(cats[:1])  # we slic  # countries api.

# min, max, mean, median, standard deviation of cats' weight in metric units.

weight_range_str = [cats[i]['weight']['metric'] for i in range(len(cats))]
weight_range_int = [(int(i[:i.find('-')-1]),int(i[i.find('-')+1:])) for i in weight_range_str]
weight_range_np = [np.arange(i[0],i[1]+1) for i in weight_range_int]

weight_flattened = np.concatenate(weight_range_np).ravel()
weight_metric_mean = np.mean(weight_flattened)
weight_metric_median = np.median(weight_flattened)
weight_metric_std = np.std(weight_flattened)

print(f'The maximum cat weight is {max(weight_flattened):.0f} kg.')
print(f'The minimum cat weight is {min(weight_flattened):.0f} kg.')
print(f'The mean cat weight is {weight_metric_mean:.2f} kg.')
print(f'The median cat weight is {weight_metric_median:.2f} kg.')
print(f'The standard deviation is {weight_metric_std:.2f} kg.' )

# life_span

lifespan_range_str = [cats[i]['life_span'] for i in range(len(cats))]
lifespan_range_int = [(int(i[:i.find('-')-1]),int(i[i.find('-')+1:])) for i in lifespan_range_str]
lifespan_range_np = [np.arange(i[0],i[1]+1) for i in lifespan_range_int]

lifespan_flattened = np.concatenate(lifespan_range_np).ravel()
lifespan_mean = np.mean(lifespan_flattened)
lifespan_median = np.median(lifespan_flattened)
lifespan_std = np.std(lifespan_flattened)

print(f'The maximum cat lifespan is {max(lifespan_flattened):.0f} years.')
print(f'The minimum cat lifespan is {min(lifespan_flattened):.0f} years.')
print(f'The mean cat lifespan is {lifespan_mean:.2f} years.')
print(f'The median cat lifespan is {lifespan_median:.2f} years.')
print(f'The standard deviation is {lifespan_std:.2f} years.' )

# frequency table of country and breed of cats
# all country: number of breeds

all_countries = [cats[i]['origin'] for i in range(len(cats))]
all_country_set = set(all_countries)

frequency_dict = dict.fromkeys(list(all_country_set), 0)

for i in list(all_country_set):
    for j in cats:
        if i == j['origin']:
            frequency_dict[i] += 1 
        
        
#3 web link doesn't work anymore
#%%
#4 also doen't work anymore. The website seems to have updated their API???
# Can still be accessed via

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
census_income = fetch_ucirepo(id=20) 
  
# data (as pandas dataframes) 
X = census_income.data.features 
y = census_income.data.targets 
  
# metadata 
print(census_income.metadata) 
  
# variable information 
print(census_income.variables) 