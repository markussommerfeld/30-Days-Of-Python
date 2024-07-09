# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:30:14 2024

@author: marku
"""

"""

Exercises: Level 1

    Find the length of the set it_companies
    Add 'Twitter' to it_companies
    Insert multiple IT companies at once to the set it_companies
    Remove one of the companies from the set it_companies
    What is the difference between remove and discard

"""
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 done
print(len(it_companies))

#2 done
it_companies.add('Twitter')

#3 done
it_companies.update(['SAP','Rakuten'])

#4 done
it_companies.remove('Rakuten')
it_companies.discard('SAP')
#5 done
# using discard is like remove, but doesn't raise a KeyError! 

"""
Exercises: Level 2

    Join A and B
    Find A intersection B
    Is A subset of B
    Are A and B disjoint sets
    Join A with B and B with A
    What is the symmetric difference between A and B
    Delete the sets completely
"""

#1 done
C = A.union(B)

#2 done
print(A.intersection(B))

#3 done
print(B.issubset(A))
print(A.issubset(B)) #A is subset of B

#4 done
print(A.isdisjoint(B)) # not disjoint, because they have entries in common

#5 done
C = A.union(B) # same
D = B.union(A) # same

#6 done
print(A.symmetric_difference(B)) #same 
print(B.symmetric_difference(A)) # same

#7 done
del A,B

"""
Exercises: Level 3

    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    Explain the difference between the following data types: string, list, tuple and set
    I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""

#1 done
age_set = set(age)
print(len(age_set))
print(len(age))

#2 done

# string: text 
# list: ordered, mutable, can contain duplicates
# tuple: ordered, immutable, can contain duplicates
# set: ordered, mutable, can not contain duplicates

#3 done
text = 'I am a teacher and I love to inspire and teach people.'
text_list = text.split(' ')
print('There are '+ str(len(set(text_list)))+ ' unique words in :' + text )