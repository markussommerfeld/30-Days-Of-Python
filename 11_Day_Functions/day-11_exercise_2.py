# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:21:13 2024

@author: marku
"""

"""
Exercises: Level 2

    Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

    Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
    Call your function is_empty, it takes a parameter and it checks if it is empty or not
    Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

"""

#1 done
def evens_and_odds(int_in): #input needs to be positive integer
    # counts number of evens and odds in the number.
    
    if isinstance(int_in, int):
        count_even = 0
        count_odd  = 0
        for i in range(int_in+1):
            if i%2 == 0:
                count_even += 1
            else:
                count_odd += 1

    else:
        print('The input is of type: ' + str(type(int_in)) + ', but has to be a integer!')
    print('The number of odds are ' + str(count_odd) + '.' + '\n' + 'The number of odds are ' + str(count_even) + '.')
    return(count_even, count_odd)

#2 done

def factorial(int_in): #input needs to be positive integer
    fact_out = 1
    if isinstance(int_in, int):
        for i in range(int_in):
            fact_out *= (i+1) 
    else:
        print('The input is of type: ' + str(type(int_in)) + ', but has to be a integer!')
    return(fact_out)
    
#3 done

def is_empty(var_in):
    if len(var_in)>0:
        print('variable is not empty')
    else: 
        print('variable is empty')
     
#4 done
# input has to be list of numbers
def calculate_mean(list_in): # avg value
    if isinstance(list_in, list) and all(isinstance(x, int) for x in list_in):
        mean_val = sum(list_in)/len(list_in)
        print('The mean value is ' + str(mean_val))
        return(mean_val)
    elif not isinstance(list_in, list):
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
    elif  not all(isinstance(x, int) for x in list_in):
        print('At least one entry is not a number')
    
def calculate_median(list_in): # middle value
    if isinstance(list_in, list) and all(isinstance(x, int) for x in list_in):
        list_in.sort()
        if len(list_in)%2 == 0:
            median = (list_in[len(list_in)//2-1] + list_in[len(list_in)//2])/2
        else:
            median = list_in[len(list_in)//2]
        print('The median value is ' + str(median))
        return(median)
    elif not isinstance(list_in, list):
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
    elif  not all(isinstance(x, int) for x in list_in):
        print('At least one entry is not a number')
    
    
def calculate_mode(list_in): # most occuring value
    if isinstance(list_in, list) and all(isinstance(x, int) for x in list_in):
        num_set = set(list_in)
        counter_list = []
        for i in num_set:
            counter_list.append(list_in.count(i))
        mode_val = list(num_set)[counter_list.index(max(counter_list))]
        print('The mode value is ' + str(mode_val))
        return(mode_val)
    elif not isinstance(list_in, list):
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
    elif  not all(isinstance(x, int) for x in list_in):
        print('At least one entry is not a number')    
    

def calculate_range(list_in): # difference between lowest and highest value
    if isinstance(list_in, list) and all(isinstance(x, int) for x in list_in):
        range_val = max(list_in) - min(list_in)
        print('The range value is ' + str(range_val))
        return(range_val)
    elif not isinstance(list_in, list):
        print('The input is of type: ' + str(type(list_in)) + ', but has to be a list!')
    elif  not all(isinstance(x, int) for x in list_in):
        print('At least one entry is not a number')    

def calculate_variance(list_in): # measure of how spread out numbers are.
    mean_value = calculate_mean(list_in)
    diff_to_mean = []
    for i in list_in:
        diff_to_mean.append(round((i - mean_value)**2,2))
    variance = sum(diff_to_mean) / len(list_in)
    print('The variance is ' + str(int(variance)))
    return(variance)
        
def calculate_std(list_in): #  sqrt of variance
    import math    
    variance = calculate_variance(list_in)
    std = math.sqrt(variance)
    print('The standard deviation is ' + str(int(std)))
    return(std)