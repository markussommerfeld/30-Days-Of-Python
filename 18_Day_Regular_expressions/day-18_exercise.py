# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:55:00 2024

@author: marku
"""

"""
    What is the most frequent word in the following paragraph?
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]

"""
import re
import numpy as np

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# This doesn't work because it includes Satzzeichen . and ,
#list_words = re.split(' ',paragraph)
#set_words = set(list_words)
#[list_words.count(i) for i in set_words]

# use find all to find every instance of a word ignoring . and ,

search_string =  r'\w+' #\w one word character + one or more times
allwords_list = re.findall(search_string, paragraph,re.I)
allwords_set = set(allwords_list)
allwords_count = [allwords_list.count(i) for i in allwords_set]
# USE THIS INSTEAD:     all_words_count = [(allwords_list.count(j), j) for i,j in enumerate(all_words_set)]


print('The most used word in the paragraph is ' + str(list(allwords_set)[allwords_count.index(max(allwords_count))]) + ' with ' +str(max(allwords_count)) + ' uses.')

"""
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
"""

text_with_numbers = ''' The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'''
search_string =  r'-\d+|\d+' #\w one word character + one or more times
points = re.findall(search_string, text_with_numbers,re.I)

int_points = [int(i) for i in points]
sorted_points = int_points.copy()
sorted_points.sort()
distance = max(sorted_points)- min(sorted_points)

#%%
"""
Write a pattern which identifies if a string is a valid python variable

"""
import re

# valid python variables have to be alphanumeric.
# not start with a number
# not include '-'

test_strings = ['first_name','first-name','1first_name','firstname']
def is_valid_variable(string_input):
    if re.match(r'[0-9]',string_input) or re.findall(r'-', string_input) or re.findall(r'[^A-Za-z_]', string_input):
    
        return(False)
    else: 
        return(True)

print(list(map(is_valid_variable, test_strings)))


#%%
"""
Clean the following text. After cleaning, count three most frequent words in the string.
"""
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    return(re.sub('[%@$&#]', '', sentence))
cleaned_text =  clean_text(sentence)

def most_frequent_words(text,n):
 
    all_words_list = re.findall(r'\w+', text,re.I) #\w one word character + one or more times
    all_words_set = set(all_words_list)
    
    all_words_count = [(allwords_list.count(j), j) for i,j in enumerate(all_words_set)]
    
    all_words_count.sort(reverse = True)  

    return(all_words_count[:n])

n = 3
print(most_frequent_words(cleaned_text,n))