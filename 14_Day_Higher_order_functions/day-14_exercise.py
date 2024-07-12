# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:41:33 2024

@author: marku
"""

"""
    Explain the difference between map, filter, and reduce.
    Explain the difference between higher order function, closure and decorator
    Define a call function before map, filter or reduce, see examples.
    Use for loop to print each country in the countries list.
    Use for to print each name in the names list.
    Use for to print each number in the numbers list.

"""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#1 done
#map: iterates a function over a list (iterable) and returns an array of all results
#filter: like map, but only returns array of inputs where function returns true
#filter: like map, but only returns a single value

#2 done
#higher order function: contains 1 or more nested functions 
#closure: Nested function to access the outer scope of the enclosing function.
#decorator: used to add functionality to exisitng function without changing it
#           Decorators are usually called before the definition of a function you want to decorate.

#3 done
from functools import reduce
def square(x):
    return(x**2)

def is_even(num):
    if num%2 ==0:
        return True
    else:
        return False
numbers_squared = map(square, numbers)
print(list(numbers_squared))
numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))

even_numbers = filter(is_even, numbers)
print(list(even_numbers))  
even_squares = filter(is_even,map(square, numbers))    
print(list(even_squares))  

#reduced_squares = reduce(square, numbers) #reduce doesn't work. still don't unterstand
#4  done
for c in countries:
    print(c)
#5  done
for n in names:
    print(n)
#6  done
for i in numbers:
    print(i)

"""
Exercises: Level 2

    Use map to create a new list by changing each country to uppercase in the countries list
    Use map to create a new list by changing each number to its square in the numbers list
    Use map to change each name to uppercase in the names list
    Use filter to filter out countries containing 'land'.
    Use filter to filter out countries having exactly six characters.
    Use filter to filter out countries containing six letters and more in the country list.
    Use filter to filter out countries starting with an 'E'
    Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
    Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
    Use reduce to sum all the numbers in the numbers list.
    Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
    Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
    Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
    Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
    Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

"""

#1 done
countries_capitalized = map(lambda x: x.upper(), countries)
print(list(countries_capitalized))

#2 done
numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))

#3 done
names_capitalized = map(lambda x: x.upper(), names)
print(list(names_capitalized))

#4 done
countries_land = lambda x: True if 'land' in x  else False
print(list(filter(countries_land,countries)))

#5 done
countries_6 = lambda x: True if len(x)==6 else False
print(list(filter(countries_6,countries)))

#6 done
countries_6 = lambda x: True if len(x)>=6 else False
print(list(filter(countries_6,countries)))

#7 done
countries_E = lambda x: True if x.startswith('E') else False
print(list(filter(countries_E,countries)))

#8 done
def square(x):
    return(x**2)

def is_even(num):
    if num%2 ==0:
        return True
    else:
        return False

num_squared = map(square, numbers)
print(list(num_squared))
num_squared_even = filter(is_even, map(square, numbers))
print(list(num_squared_even))

# numbers_squared_even = filter(lambda x: True if map(lambda x: x**2, numbers)%2==0 else False,numbers)
# print(list(numbers_squared_even))

#9 done
import random
list_input = countries + numbers
random.shuffle(list_input)

def get_string_lists (x):
    if isinstance(x, str):
        return True
    else:
        return False
    
list_of_strings = filter(get_string_lists,list_input)
print(list(list_of_strings))

#10 done
def add_2_num(x,y):
    return(x+y)

reduce(add_2_num,numbers)

#11 kind of done
print(reduce(lambda x, y: y + ', ' + x, countries, ' are north European countrtries'))

#12 done
# read the countries variable
runfile('C:/GitHub/30-Days-Of-Python/data/countries.py', wdir='C:/GitHub/30-Days-Of-Python/data')
def categorize_countries(list_in,common_pattern):
    list_out = []
    for i in list_in:
        if common_pattern in i:
            list_out.append(i)
    return(list_out)

categorize_countries(countries,'stan') #'land', 'ia', 'island', 'stan'

#13 done
import string   

def count_countries(list_in):
    first_letter_list = [i[0] for i in list_in]
    key_list = list(string.ascii_uppercase)
    dict_out = {}
    for i in key_list:
        dict_out[i] = first_letter_list.count(i)
    return(dict_out)

count_countries(countries)

#14 done
def get_first_ten_countries(countries):
    return(countries[:10])

#15 done
def get_last_ten_countries(countries):
    return(countries[-10:])

"""
Exercises: Level 3

    Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
        Sort countries by name, by capital, by population
        Sort out the ten most spoken languages by location.
        Sort out the ten most populated countries.
"""
#%%
runfile('C:/GitHub/30-Days-Of-Python/data/countries-data_variable.py', wdir='C:/GitHub/30-Days-Of-Python/data')
country_data=np.array(country_data)
#Sort by name, capital, population
import numpy as np
country_names = list(map(lambda x: x['name'], country_data))
country_capital = list(map(lambda x: x['capital'], country_data))
country_population = list(map(lambda x: x['population'], country_data))

names_index = np.argsort(country_names)
capital_index = np.argsort(country_capital)
population_index = np.argsort(country_population)

country_data[names_index]
country_data[capital_index]
country_data[population_index]

#sort out top ten spoken languages
# done it before, could do it again.

