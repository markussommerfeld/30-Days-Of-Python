# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:51:11 2024

@author: marku
"""

"""

Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
"""
#1 done
empty_list =[]
#2 done
long_list = [10,20,30,40,50,60,70]
#3 done
print(len(long_list))
#4 done
first_item = long_list[0]
mid_item = long_list[len(long_list)//2]
last_item = long_list[-1]
#5 done
mixed_data_types = ['Markus', 37, 1.78, True, 'Tokyo']
#6 done
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7 done
print(it_companies)
#8 done
print(len(it_companies))
#9 done
first_comp = it_companies[0]
mid_comp = it_companies[len(it_companies)//2]
last_comp = it_companies[-1]
#10 done
it_companies[3] = 'Orange'
print(it_companies)
#11 done
it_companies.append('SAP')
#12 done
it_companies.insert(len(it_companies)//2,'NVidea')
#13 done
it_companies[1] = it_companies[1].upper()
#14 done
it_companies.append('#; ') 
#15 done
print('Facebook' in it_companies)
#16 done
it_companies.sort()
#17 done
it_companies.reverse()
#18 done
it_companies[0:3]
#19 done
it_companies[-3:]
#20 done
it_companies[len(it_companies)//2]
#21 done
it_companies.remove(it_companies[0])
#22 done
it_companies.remove(it_companies[len(it_companies)//2])
#23 done
it_companies.pop()
#24 done
it_companies.clear()
#25 done
del(it_companies)
#26 done
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
#27 done
full_stack = front_end.copy()
# full_stack.insert(full_stack.index('Redux')+1,'SQL')
# full_stack.insert(full_stack.index('Redux')+1,'Python')
# or 
full_stack[full_stack.index('Redux'):full_stack.index('Redux')] = ['SQL', 'Python']
