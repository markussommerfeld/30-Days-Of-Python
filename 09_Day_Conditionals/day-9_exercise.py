# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:41:41 2024

@author: marku
"""

"""
### Exercises: Level 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.

    Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
""

"""

#1 done
input_age = input('Enter your age: ')

if int(input_age) >= 18:
    print('You are old enough to learn to drive.')
else:
    years_until_drive = 18-int(input_age)
    print('You need ' + str(years_until_drive) + ' more years to learn to drive.')
   

#2 done
my_age = 25
your_age = int(input('Enter your age: '))

if your_age>my_age:
    if your_age - my_age == 1:
        print('You are ' + str(1) + ' year older than me.')
    else:
        print('You are ' + str(your_age - my_age) + ' years older than me.')

elif  your_age == my_age:
    print('We are the same age!')
    
else:
    if your_age - my_age == 1:
        print('I am ' + str(1) + ' year older than you.')
    else:
        print('I am ' + str(my_age- your_age) + ' years older than you.')

    
#3 done
a ,b = input('Enter two numbers').split()

print( 'Enter number one: ' + a + '\n' +  'Enter number two: ' + b)

if int(a) > int(b):
    print(a + ' is greater than ' + b)
elif int(a) < int(b):
    print(a + ' is smaller than ' + b)
else:
    print(a + ' is equal to ' + b)

#%%
"""
### Exercises: Level 2
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""

#1 done
points = int(input('Input the points the student got: '))

if points >= 80 and points <= 100:
    print('Grade: A')
elif points >= 70 and points <80:
    print('Grade: B')
elif points >= 60 and points < 70:
    print('Grade: C')
elif points >= 50 and points < 60:
    print('Grade: D')
elif points < 50:
    print('Grade: F')
else:
    print('Enter points between 0 and 100')

#2 done
month_input = input('Input a month: ')

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
    
#3 done

fruits_list = ['banana', 'orange', 'mango', 'lemon']

fruit_input = input('Input a fruit: ')

if fruit_input.lower() not in fruits_list:
    fruits_list.append(fruit_input.lower()) 
    print(fruits_list)
else:
    print('That fruit already exist in the list')
#%%    
    
"""
### Exercises: Level 3

    Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:

    Asabeneh Yetayeh lives in Finland. He is married.
"""
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    print('The middle skills in the skill list is: ' + str(person['skills'][len(person['skills'])//2]))
    
if 'skills' in person.keys():
    if 'Python' in  person['skills']:
        print('Yes, the person has Python skill!')
    else:
        print('No, the person does not have Python skills!')
        
if 'skills' in person.keys():
    # if set(person['skills']).issubset(set(['JavaScript', 'React'])):
    if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
            print('He is a fullstack developer!')
    elif 'JavaScript' in person['skills'] and  'React' in person['skills']:
        print('He is a front end developer')
        
    elif 'Node' in  person['skills'] and  'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer')
        
    else:
        print('unknown title')
        
        
if person['is_marred'] and person['country'] == 'Finland':
    print(person['first_name']+ ' '+ person['last_name']+ ' lives in ' + person['country'] +'. He is married.')

  
    