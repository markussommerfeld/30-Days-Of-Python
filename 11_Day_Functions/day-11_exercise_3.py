# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:21:13 2024

@author: marku
"""

"""

    Write a function called is_prime, which checks if a number is prime.
    Write a functions which checks if all items are unique in the list.
    Write a function which checks if all the items of the list are of the same data type.
    Write a function which check if provided variable is a valid python variable
    Go to the data folder and access the countries-data.py file.

    Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
    Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
"""

# 1 done
def is_prime(num):
    if num > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
    
    return()


# 2 done
def all_unique(list_in):
    set_in = set(list_in)
    if len(list(set_in)) == len(list_in):
        print('There are no duplicates in the list!')
    else:
        print('There are duplicates in the list!')    
    return()

# 3 done
def all_same_type(list_in):
    type_list = []
    for i in list_in:
        type_list.append(type(i))
    if len(set(type_list)) == 1:
        print('All entries of the list have the same type: ' + str(type_list[0]))
    else:
        print('There are multiple types in this list!')
    return()

# 4 done
def valid_variabel(): #?!
    return()


# 5 done
# could adjust code similar to exercise 10, but takes too much time.

country_data = runcell(0, 'C:/GitHub/30-Days-Of-Python/data/countries-data.py')

def most_spoken_languages(country_data):
    list_languages=[]
    set_languages = set()

    for i in country_data:
        for idx_lang in i['languages']:
            set_languages.add(idx_lang)  
            list_languages.append(idx_lang)
    count_lang = []
    for i_lang in set_languages:
        count_lang.append(list_languages.count(i_lang))
    language_most = list(set_languages)[count_lang.index(max(count_lang))]
    print('The most spoken language is ' + language_most + ' with ' + str(max(count_lang)))
    return(language_most)

def most_populated_countries(country_data):
    list_countries = []
    list_population = []
    for idx_country in range(len(country_data)):
        list_countries.append(country_data[idx_country]['name'])
        list_population.append(country_data[idx_country]['population'])
    print('The most populated contry is ' + list_countries[list_population.index(max(list_population))] + ' with ' + str(max(list_population)) + ' people.')
    return()