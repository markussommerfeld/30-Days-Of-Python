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


"""
Exercises: Level 3

    Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
        Sort countries by name, by capital, by population
        Sort out the ten most spoken languages by location.
        Sort out the ten most populated countries.
"""