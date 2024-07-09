# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:07:35 2024

@author: marku
"""

"""

    Create an empty dictionary called dog
    Add name, color, breed, legs, age to the dog dictionary
    Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
    Get the length of the student dictionary
    Get the value of skills and check the data type, it should be a list
    Modify the skills values by adding one or two skills
    Get the dictionary keys as a list
    Get the dictionary values as a list
    Change the dictionary to a list of tuples using items() method
    Delete one of the items in the dictionary
    Delete one of the dictionaries
"""

#1 done
dog = dict()

#2 done
dog['name'], dog['color'], dog['breed'],dog['legs'],dog['age']='Bello', 'golden', 'Golden Retriever', 4,  3

#3 done
student = {'first_name':[],'last_name':[],'gender':[],'age':[],'marital_status':[],
           'skills':[],'country':[],'city ':[],'address':[]}

#4 done 
print(len(student))

#5 done
print(type(student['skills']))

#6 done
student['skills']=['backflip','math']

#7 done
print(student.keys())

#8 done
print(student.values())

#9 done
print(student.items())

#10 done
student.pop('skills')
#del student['skills']

#11 done
del student