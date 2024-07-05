# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:51:19 2024

@author: marku
"""

"""
1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3 Declare a variable named company and assign it to an initial value "Coding For All".
4 Print the variable company using print().
5 Print the length of the company string using len() method and print().
6 Change all the characters to uppercase letters using upper() method.
7 Change all the characters to lowercase letters using lower() method.
8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
9 Cut(slice) out the first word of Coding For All string.
10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
11 Replace the word coding in the string 'Coding For All' to Python.
12 Change Python for Everyone to Python for All using the replace method or other methods.
13 Split the string 'Coding For All' using space as the separator (split()) .
14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
15 What is the character at index 0 in the string Coding For All.
16 What is the last index of the string Coding For All.
17 What character is at index 10 in "Coding For All" string.
18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
19 Create an acronym or an abbreviation for the name 'Coding For All'.
20 Use index to determine the position of the first occurrence of C in Coding For All.
21 Use index to determine the position of the first occurrence of F in Coding For All.
22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
28 Does ''Coding For All' start with a substring Coding?
29 Does 'Coding For All' end with a substring coding?
30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
31 Which one of the following variables return True when we use the method isidentifier():

    30DaysOfPython
    thirty_days_of_python

32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
33 Use the new line escape sequence to separate the following sentences.

I am enjoying this challenge.
I just wonder what is next.

34 Use a tab escape sequence to write the following lines.

Name      Age     Country   City
Asabeneh  250     Finland   Helsinki

35    Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.

36    Make the following using string formatting methods:

8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

"""

#1 done
print( 'Thirty'+' '+ 'Days'+' '+ 'Of'+' '+ 'Python' )
#2 done
print('Coding' +' '+ 'For' +' '+ 'All')
#3 done
company = 'Coding' +' '+ 'For' +' '+ 'All'
company_list = ['Coding','For','All']
company = ' '.join(company_list)
#4 done
print(company)
#5 done
print(len(company))
#6 done
print(company.upper())
#7 done
print(company.lower())
#8 done
print(company.capitalize()+ '\n' + company.title() +'\n' + company.swapcase())
#9 done
print(company.strip('Coding'))
#10 done
print(company.find('Coding'))
print('Coding' in company)
#11 done
print(company.replace('Coding', 'Python'))
#12 done
print('Python for Everyone'.replace('Everyone', 'All'))
#13 done
print(company.split(' '))
#14 done
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
#15 done
print(company[0])
#16 done
print(company[-1])
#17 done
print(company[10])
#18 done
print(''.join([c for c in 'Python For Everyone' if c.isupper()]))
#19 done
print(''.join([c for c in company if c.isupper()]))
#20 done
print(company.find('C'))
#21 done
print(company.find('F'))
#22 done
print(company.rfind('l'))
#23 done
print('You cannot end a sentence with because because because is a conjunction'.index('because'))
#24 done
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
#25 done
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))
#26 done
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
#27 done, same as 25
#28 done
print(company.startswith('Coding'))
#29 done
print(company.startswith('coding'))
#30 done
print('   Coding For All      '.strip(' '))
#31 done
print('30DaysOfPython'.isidentifier(), 'thirty_days_of_python'.isidentifier())
#32 done
name_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
'# '.join(name_list)
#33 done
print('I am enjoying this challenge. \nI just wonder what is next.')
#34 done
print('Name \tAge \tCountry \tCity \t\nAsabeneh \t250 \tFinland \tHelsinki')
#35 done
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {:.0f} meters square.'.format(radius,area))
#36 done
a = 8
b = 6

print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))
