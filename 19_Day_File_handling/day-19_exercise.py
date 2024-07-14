# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:40:20 2024

@author: marku
"""

"""
Write a function which count number of lines and number of words in a text. 
All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b)
 Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count 
number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

Read the countries_data.json data file in data directory, create a function that creates a list of 
the ten most populated countries

"""

#1 done
text_dir = '../data/obama_speech.txt'
def count_lines(text_dir):
    f = open(text_dir)
    lines = f.readlines()
    f.close()
    return(len(lines))

def count_words(text_dir):
    import re
    f = open(text_dir)
    text = f.read()
    
    all_words_list = re.findall(r'\w+', text,re.I) #\w one word character + one or more times

    f.close()

    return(len(all_words_list))

list_of_dirs = ['../data/' + i for i in ['obama_speech.txt','michelle_obama_speech.txt','donald_speech.txt','melina_trump_speech.txt']]
for i in list_of_dirs:
    print(f'{i[i.rfind('/')+1:]} has {count_words(i)} words and {count_lines(i)} lines!')


#2 & 3  Doesn't work. I don't know why. 
# import json
# file_dir = '../data/countries_data.json'

# with open(file_dir, 'w', encoding='utf-8') as f:
#     country_dict = json.loads(file_dir)
# f = open('../data/countries_data_long.json')
# data = json.load(f)
