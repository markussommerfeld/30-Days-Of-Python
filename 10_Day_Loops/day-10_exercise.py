# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:06:27 2024

@author: marku
"""

"""
Exercises: Level 1

Iterate 0 to 10 using for loop, do the same using while loop.

Iterate 10 to 0 using for loop, do the same using while loop.

Write a loop that makes seven calls to print(), so we get on the output the following triangle:
    
Use nested loops to create the following:
    
Print the following pattern:

Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers

    
"""

#1 done
for idx in range(11):
    print(idx)
  
idx = 0
while idx < 11:
    print(idx)
    idx += 1
    
#2 done
for idx in reversed(range(11)):
    print(idx)
    
idx = 10
while idx >= 0:
    print(idx)
    idx -= 1
    
#3 done
for idx in range(1,8):
    print('#'*idx)
    
#4 done 
for idx in range(1,9):
    out_string = ''
    for idx2 in range(1,9):
        out_string += '# '
    print(out_string)
    
#5 done
for num in range(11):
    print(str(num) + ' x ' +str(num) + ' = ' + str(num*num))
    
#6 done
string_list = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for string in string_list:
    print(string)
    
#7 done
for idx in range(101):
    if idx%2==0:
        print(idx)

#8 done
for idx in range(101):
    if idx%2==1:
        print(idx)

#%%

"""

Use for loop to iterate from 0 to 100 and print the sum of all numbers.

The sum of all numbers is 5050.

Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.

"""

#1 done
final_sum = 0
for idx in range(101):
    final_sum += idx
print('The sum of all numbers is ' + str(final_sum))

#2 done
even_sum = 0
odd_sum = 0
for idx in range(101):
    if idx%2==0:
        even_sum += idx
    else:
        odd_sum += idx
print('The sum of all evens is ' + str(even_sum) + '. And the sum of all odds is ' + str(odd_sum) + '.')


#%%

"""

    Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
    This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
    Go to the data folder and use the countries_data.py file.
        What are the total number of languages in the data
        Find the ten most spoken languages from the data
        Find the 10 most populated countries in the world

"""

#1 done
import sys
sys.path.insert(1, 'C:\GitHub\30-Days-Of-Python\data\countries.py')
from countries import *  

country_list = []
for idx_country in countries:
    if 'land' in idx_country:
        country_list.append(idx_country)
        
#2 done
fruit_list = ['banana', 'orange', 'mango', 'lemon']
fruit_out = []

for idx_fruit in reversed(fruit_list):
    fruit_out.append(idx_fruit)    
    
#3 done
#Go to the data folder and use the countries_data.py file. 

country_data = runcell(0, 'C:/GitHub/30-Days-Of-Python/data/countries-data.py')
set_language = set()
list_languages = []
list_countries = []
list_population = []
for idx_country in range(len(country_data)):
    list_countries.append(country_data[idx_country]['name'])
    list_population.append(country_data[idx_country]['population'])
    for idx_lang in country_data[idx_country]['languages']:
        set_language.add(idx_lang)
        list_languages.append(idx_lang)
print('There are a total of ' + str(len(set_language)) + ' in the country list.')

        
count_lang = []
for idx_lang in set_language:
    count_lang.append(list_languages.count(idx_lang))
    
index_max_lang = []
temp_country_list = count_lang.copy()
for idx_lan_counter in range(10):
    index_max_lang.append(temp_country_list.index(max(temp_country_list)))
    temp_country_list.pop(index_max_lang[-1])
    
    print('language: ' + str(list(set_language)[index_max_lang[-1]]) + ' with: ' + str(max(temp_country_list)) + ' mentions.')
   

index_max_pop = []
temp_country_temp_pop = list_population.copy()
list_countries_temp = list_countries.copy()

for idx_country in range(10):
    index_max_pop.append(temp_country_temp_pop.index(max(temp_country_temp_pop)))
   
    print('country: ' + list_countries_temp[index_max_pop[-1]] + ' with a population of: ' + str(max(temp_country_temp_pop)))
    temp_country_temp_pop.pop(index_max_pop[-1])
    list_countries_temp.pop(index_max_pop[-1]) 
    
    


