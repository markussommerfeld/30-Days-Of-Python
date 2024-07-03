# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:01:22 2024

@author: marku
"""

"""
    Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    Write a python comment saying 'Day 2: 30 Days of python programming'
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line
"""

#1. done
#2. Day 2: 30 Days of python programming; done

first_name = 'Markus' #3 done
last_name = 'Sommerfeld' #4 done
full_name = first_name + ' ' + last_name #5 done
country = 'Japan' #6 done
city = 'Tokyo' #7 done
age = 37 #8 done
year = 2024 #9 done
is_married, is_true,is_light_on  = True, True, True #10 - 13 done

#%%
"""

    Check the data type of all your variables using type() built-in function
    Using the len() built-in function, find the length of your first name
    Compare the length of your first name and your last name
    Declare 5 as num_one and 4 as num_two
        Add num_one and num_two and assign the value to a variable total
        Subtract num_two from num_one and assign the value to a variable diff
        Multiply num_two and num_one and assign the value to a variable product
        Divide num_one by num_two and assign the value to a variable division
        Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
        Calculate num_one to the power of num_two and assign the value to a variable exp
        Find floor division of num_one by num_two and assign the value to a variable floor_division
    The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
    Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
    Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""
for i in (first_name,last_name, full_name, age, year, is_married, is_true, is_light_on):
    print(i,': ', type(i)) # 1 done

if len(first_name)> len(last_name): #2,3 done
    print('My first name is longer than my last name')
else:
    print('My last name is longer than my first name')
    
# 4 done
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
prduct = num_one * num_two
division  = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two

#  5 done
radius = 30
pi = 3.14159
area_of_circle = pi*radius**2
circum_of_circle = 2*pi*radius

radius_input = input('Enter the radius of the circle: ')
print(pi*float(radius_input)**2)

# 6 done
input_first_name, input_last_name, input_country, input_age = input("Enter: first name, last name, country and age (seperated by a space, everything is a string by default)").split()
print("Your first name: ", input_first_name)
print("Your last name: ", input_last_name)
print("Your country: ", input_country)
print("Your age: ", input_age)

#7 done
help('keywords')