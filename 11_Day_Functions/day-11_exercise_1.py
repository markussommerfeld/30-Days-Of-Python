# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:21:13 2024

@author: marku
"""

"""
Exercises: Level 1

    Declare a function add_two_numbers. It takes two parameters and it returns a sum.
    Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
    Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
    Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
    Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    Write a function called calculate_slope which return the slope of a linear equation
    Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
    Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
    Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

    Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
    Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

    Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

    Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050

    Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
    Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
"""

#1 done
def add_two_numbers(num_1,num_2):
    return(num_1+num_2)

#2 done
def area_of_circle(radius):
    pi = 3.14
    return(pi*radius**2)

#3 done
def add_all_nums(*nums):
    sum_out = 0
    for idx_nums in nums:
        if type(idx_nums) == float or type(idx_nums) == int:
            sum_out += idx_nums
        else:
            print(str(idx_nums)+ ' is not a number')
    print('The total sum is: '  + str(sum_out))

#4 done
def convert_celsius_to_fahrenheit(Temp_C):
    return((Temp_C * 9/5) + 32)
#5 done
def check_season(month_input):
    
    if month_input.capitalize() in ['September', 'October', 'November']:
        print(month_input.capitalize() + ' is in season Autumn')
    elif month_input.capitalize() in ['December', 'January', 'February']:
        print(month_input.capitalize() + ' is in season Winter')
    elif month_input.capitalize() in ['March', 'April', 'May']:
        print(month_input.capitalize() + ' is in season Spring')
    elif month_input.capitalize() in ['June', 'July', 'August']:
        print(month_input.capitalize() + ' is in season Summer')
    else:
        print('Enter a propper month. Maybe typo.')

#6 done

def calculate_slope(a,b): #a + b* x
    return(b)

#7 done

def solve_quadratic_eqn(a,b,c): #ax² + bx + c = 0.
    import math
    return((-b-math.sqrt(b**2-4*a*c))/2/a, (-b+math.sqrt(b**2-4*a*c))/2/a)

#8 done

def print_list(list_in): #input must be a list
    if isinstance(list_in, list):
        for idx in list_in:
            print(idx)
    else:
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
#9 done

def reverse_list(list_in):
    if isinstance(list_in, list):
        print('Original List:', list_in)
        # List Reverse
        list_in.reverse()
                
        # updated list
        print('Updated List:', list_in)
        return(list_in)
    else:
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
    
#10 done

def capitalize_list_items(list_in):
    list_out = []
    if isinstance(list_in, list):
        for idx_list in list_in:
            if isinstance(idx_list, str):
                list_out.append(idx_list.capitalize())
    else:
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
    print(list_out)

#11 done

def add_item(list_in,parameter_in):
    if isinstance(list_in, list):
        list_in.append(parameter_in)
        return(list_in)
    else:
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
    
#12 done

def remove_item(list_in,parameter_rem):
    if isinstance(list_in, list):
        if parameter_rem in list_in:
            list_in.remove(parameter_rem)
            return(list_in)
        else:
            print('The parameter to remove is not part of the list!')
    else:
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')

#13 done

def sum_of_numbers(num_in):
    return(sum(range(num_in+1)))

#14 done

def sum_of_odds(num_in):
    total_odd = 0
    for i in range(num_in+1):
        if i%2 == 1:
            total_odd += i
        else:
            continue
    return(total_odd)
            
#15 done

def sum_of_even(num_in):
    total_even = 0
    for i in range(num_in+1):
        if i%2 == 0:
            total_even += i
        else:
            continue
    return(total_even)
