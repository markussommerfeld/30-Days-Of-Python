# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:28:43 2024

@author: marku
"""

"""
Exercises: Level 1

    Create an empty tuple
    Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
    Join brothers and sisters tuples and assign it to siblings
    How many siblings do you have?
    Modify the siblings tuple and add the name of your father and mother and assign it to family_members

Exercises: Level 2

    Unpack siblings and parents from family_members
    Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
    Change the about food_stuff_tp tuple to a food_stuff_lt list
    Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
    Slice out the first three items and the last three items from food_staff_lt list
    Delete the food_staff_tp tuple completely
    Check if an item exists in tuple:

    Check if 'Estonia' is a nordic country

    Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"""
#1 dpme
empty_tuple = tuple()

#2 dpme
sisters_tuple = ('Iris','Anna')
brothers_tuple = ('Martin','Michael')

#3 done
sibling_tuple = sisters_tuple + brothers_tuple

#4 done
len(sibling_tuple)
 
#5 done

family_members = list(sibling_tuple) +  ['Ingrid','Wolfgang'] 

"""
Exercises: Level 2
"""

#1 done
siblings, parents  = family_members[:-2], family_members[-2:]

#2 done
fruits = ('Banana','Pineapple','Strawberry')
vegetables = ('Paprika','Eggplant','Tomato')
animal_products = ('Milk','Meat','Cheese')
food_stuff_tp = fruits + vegetables + animal_products 

#3 done
food_stuff_lt  = list(food_stuff_tp)

#4 done
print(food_stuff_lt[len(food_stuff_lt)//2])

#5 done
first_3_foodstuff = food_stuff_lt[:3]
last_3_foodstuff = food_stuff_lt[-3:]

#6 done
del(food_stuff_tp )

#7 done
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
